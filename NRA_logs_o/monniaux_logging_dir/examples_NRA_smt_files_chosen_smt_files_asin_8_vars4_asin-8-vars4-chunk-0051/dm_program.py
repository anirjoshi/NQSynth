import sympy
from sympy import *

def pre_condition_0(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 8) & (delta >= skoS2**2 - 2) & (delta - skoX >= -8) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (189*skoS2/20 - skoSM*(126*skoS2 + 61)/40 + 203/40 >= skoX*(40*skoSM + skoX*(378*skoS2 - skoSM*(126*skoS2 + 61) + 203) + 280)/40)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Integer(8)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-8)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), GreaterThan(Add(Mul(Rational(189, 20), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(203, 40)), Mul(Rational(1, 40), Symbol('skoX'), Add(Mul(Integer(40), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(378), Symbol('skoS2')), Mul(Integer(-1), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(203))), Integer(280)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= skoX) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta >= -skoX) & (delta + skoX >= 8) & (delta >= skoS2**2 - 2) & (delta - skoX >= -8) & (delta >= 2 - skoS2**2) & (63*skoS2/10 + 71/20 >= skoX*(skoX*(126*skoS2 + 71) + 160)/20)

	pre_cond = And(GreaterThan(Symbol('delta'), Symbol('skoX')), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Integer(8)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-8)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Add(Mul(Rational(63, 10), Symbol('skoS2')), Rational(71, 20)), Mul(Rational(1, 20), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(71))), Integer(160)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_2(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 24) & (delta >= skoS2**2 - 2) & (delta - skoX >= -24) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (63*skoS2/4 - skoSM*(126*skoS2 + 61)/40 + 333/40 >= skoX*(40*skoSM + skoX*(630*skoS2 - skoSM*(126*skoS2 + 61) + 333) + 360)/40)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Integer(24)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-24)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), GreaterThan(Add(Mul(Rational(63, 4), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(333, 40)), Mul(Rational(1, 40), Symbol('skoX'), Add(Mul(Integer(40), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(630), Symbol('skoS2')), Mul(Integer(-1), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(333))), Integer(360)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_3(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= skoX) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta >= -skoX) & (delta + skoX >= 24) & (delta >= skoS2**2 - 2) & (delta - skoX >= -24) & (delta >= 2 - skoS2**2) & (63*skoS2/5 + 34/5 >= skoX*(skoX*(63*skoS2 + 34) + 50)/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Symbol('skoX')), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Integer(24)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-24)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Add(Mul(Rational(63, 5), Symbol('skoS2')), Rational(34, 5)), Mul(Rational(1, 5), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(63), Symbol('skoS2')), Integer(34))), Integer(50)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_4(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 15) & (delta >= skoS2**2 - 2) & (delta - skoX >= -15) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (63*skoS2/5 - skoSM*(126*skoS2 + 61)/40 + 67/10 >= skoX*(40*skoSM + skoX*(504*skoS2 - skoSM*(126*skoS2 + 61) + 268) + 320)/40)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Integer(15)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-15)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), GreaterThan(Add(Mul(Rational(63, 5), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(67, 10)), Mul(Rational(1, 40), Symbol('skoX'), Add(Mul(Integer(40), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(504), Symbol('skoS2')), Mul(Integer(-1), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(268))), Integer(320)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_5(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= skoX) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta >= -skoX) & (delta + skoX >= 15) & (delta >= skoS2**2 - 2) & (delta - skoX >= -15) & (delta >= 2 - skoS2**2) & (189*skoS2/20 + 207/40 >= 9*skoX*(skoX*(42*skoS2 + 23) + 40)/40)

	pre_cond = And(GreaterThan(Symbol('delta'), Symbol('skoX')), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Integer(15)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-15)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Add(Mul(Rational(189, 20), Symbol('skoS2')), Rational(207, 40)), Mul(Rational(9, 40), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(42), Symbol('skoS2')), Integer(23))), Integer(40)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_6(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 5985/256) & (delta >= skoS2**2 - 2) & (delta - skoX >= -5985/256) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (4977*skoS2/320 - skoSM*(126*skoS2 + 61)/40 + 5263/640 >= skoX*(640*skoSM + skoX*(9954*skoS2 - 16*skoSM*(126*skoS2 + 61) + 5263) + 5720)/640)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(5985, 256)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-5985, 256)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), GreaterThan(Add(Mul(Rational(4977, 320), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(5263, 640)), Mul(Rational(1, 640), Symbol('skoX'), Add(Mul(Integer(640), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(9954), Symbol('skoS2')), Mul(Integer(-1), Integer(16), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(5263))), Integer(5720)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_7(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 5985/256) & (delta >= skoS2**2 - 2) & (delta - skoX >= -63/64) & (delta >= 2 - skoS2**2) & (4851*skoS2/320 + 5141/640 >= skoX*(skoX*(9702*skoS2 + 5141) + 5800)/640)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(5985, 256)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-63, 64)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Add(Mul(Rational(4851, 320), Symbol('skoS2')), Rational(5141, 640)), Mul(Rational(1, 640), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(9702), Symbol('skoS2')), Integer(5141))), Integer(5800)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_8(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 288) & (delta >= skoS2**2 - 2) & (delta - skoX >= -288) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (1071*skoS2/20 - skoSM*(126*skoS2 + 61)/40 + 1113/40 >= skoX*(40*skoSM + skoX*(2142*skoS2 - skoSM*(126*skoS2 + 61) + 1113) + 840)/40)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Integer(288)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-288)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), GreaterThan(Add(Mul(Rational(1071, 20), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(1113, 40)), Mul(Rational(1, 40), Symbol('skoX'), Add(Mul(Integer(40), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(2142), Symbol('skoS2')), Mul(Integer(-1), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(1113))), Integer(840)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_9(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= skoX) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta >= -skoX) & (delta + skoX >= 288) & (delta >= skoS2**2 - 2) & (delta - skoX >= -288) & (delta >= 2 - skoS2**2) & (252*skoS2/5 + 263/10 >= skoX*(skoX*(504*skoS2 + 263) + 220)/10)

	pre_cond = And(GreaterThan(Symbol('delta'), Symbol('skoX')), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Integer(288)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-288)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Add(Mul(Rational(252, 5), Symbol('skoS2')), Rational(263, 10)), Mul(Rational(1, 10), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(504), Symbol('skoS2')), Integer(263))), Integer(220)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_10(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 255) & (delta >= skoS2**2 - 2) & (delta - skoX >= -255) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (252*skoS2/5 - skoSM*(126*skoS2 + 61)/40 + 131/5 >= skoX*(40*skoSM + skoX*(2016*skoS2 - skoSM*(126*skoS2 + 61) + 1048) + 800)/40)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Integer(255)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-255)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), GreaterThan(Add(Mul(Rational(252, 5), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(131, 5)), Mul(Rational(1, 40), Symbol('skoX'), Add(Mul(Integer(40), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(2016), Symbol('skoS2')), Mul(Integer(-1), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(1048))), Integer(800)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_11(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= skoX) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta >= -skoX) & (delta + skoX >= 255) & (delta >= skoS2**2 - 2) & (delta - skoX >= -255) & (delta >= 2 - skoS2**2) & (189*skoS2/4 + 987/40 >= 21*skoX*(skoX*(90*skoS2 + 47) + 40)/40)

	pre_cond = And(GreaterThan(Symbol('delta'), Symbol('skoX')), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Integer(255)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-255)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Add(Mul(Rational(189, 4), Symbol('skoS2')), Rational(987, 40)), Mul(Rational(21, 40), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(90), Symbol('skoS2')), Integer(47))), Integer(40)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_12(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 1085/4) & (delta >= skoS2**2 - 2) & (delta - skoX >= -1085/4) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (2079*skoS2/40 - skoSM*(126*skoS2 + 61)/40 + 2161/80 >= skoX*(80*skoSM + skoX*(4158*skoS2 - 2*skoSM*(126*skoS2 + 61) + 2161) + 1640)/80)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(1085, 4)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-1085, 4)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), GreaterThan(Add(Mul(Rational(2079, 40), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(2161, 80)), Mul(Rational(1, 80), Symbol('skoX'), Add(Mul(Integer(80), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(4158), Symbol('skoS2')), Mul(Integer(-1), Integer(2), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(2161))), Integer(1640)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_13(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 1085/4) & (delta >= skoS2**2 - 2) & (delta - skoX >= -55/64) & (delta >= 2 - skoS2**2) & (8127*skoS2/160 + 8461/320 >= skoX*(skoX*(16254*skoS2 + 8461) + 6680)/320)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(1085, 4)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-55, 64)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Add(Mul(Rational(8127, 160), Symbol('skoS2')), Rational(8461, 320)), Mul(Rational(1, 320), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(16254), Symbol('skoS2')), Integer(8461))), Integer(6680)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_14(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 17097/64) & (delta >= skoS2**2 - 2) & (delta - skoX >= -17097/64) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (8253*skoS2/160 - skoSM*(126*skoS2 + 61)/40 + 8579/320 >= skoX*(320*skoSM + skoX*(16506*skoS2 - 8*skoSM*(126*skoS2 + 61) + 8579) + 6520)/320)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(17097, 64)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-17097, 64)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), GreaterThan(Add(Mul(Rational(8253, 160), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(8579, 320)), Mul(Rational(1, 320), Symbol('skoX'), Add(Mul(Integer(320), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(16506), Symbol('skoS2')), Mul(Integer(-1), Integer(8), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(8579))), Integer(6520)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_15(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 17097/64) & (delta >= skoS2**2 - 2) & (delta - skoX >= -247/256) & (delta >= 2 - skoS2**2) & (16317*skoS2/320 + 3395/128 >= 7*skoX*(skoX*(4662*skoS2 + 2425) + 1880)/640)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(17097, 64)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-247, 256)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Add(Mul(Rational(16317, 320), Symbol('skoS2')), Rational(3395, 128)), Mul(Rational(7, 640), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(4662), Symbol('skoS2')), Integer(2425))), Integer(1880)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_16(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 4209/16) & (delta >= skoS2**2 - 2) & (delta - skoX >= -4209/16) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (819*skoS2/16 - skoSM*(126*skoS2 + 61)/40 + 4257/160 >= skoX*(160*skoSM + skoX*(8190*skoS2 - 4*skoSM*(126*skoS2 + 61) + 4257) + 3240)/160)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(4209, 16)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-4209, 16)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), GreaterThan(Add(Mul(Rational(819, 16), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(4257, 160)), Mul(Rational(1, 160), Symbol('skoX'), Add(Mul(Integer(160), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(8190), Symbol('skoS2')), Mul(Integer(-1), Integer(4), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(4257))), Integer(3240)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_17(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 4209/16) & (delta >= skoS2**2 - 2) & (delta - skoX >= -55/64) & (delta >= 2 - skoS2**2) & (8001*skoS2/160 + 8331/320 >= 3*skoX*(skoX*(5334*skoS2 + 2777) + 2200)/320)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(4209, 16)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-55, 64)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Add(Mul(Rational(8001, 160), Symbol('skoS2')), Rational(8331, 320)), Mul(Rational(3, 320), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(5334), Symbol('skoS2')), Integer(2777))), Integer(2200)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_18(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 67865/256) & (delta >= skoS2**2 - 2) & (delta - skoX >= -67865/256) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (16443*skoS2/320 - skoSM*(126*skoS2 + 61)/40 + 17093/640 >= skoX*(640*skoSM + skoX*(32886*skoS2 - 16*skoSM*(126*skoS2 + 61) + 17093) + 13000)/640)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(67865, 256)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-67865, 256)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), GreaterThan(Add(Mul(Rational(16443, 320), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(17093, 640)), Mul(Rational(1, 640), Symbol('skoX'), Add(Mul(Integer(640), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(32886), Symbol('skoS2')), Mul(Integer(-1), Integer(16), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(17093))), Integer(13000)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_19(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 67865/256) & (delta >= skoS2**2 - 2) & (delta - skoX >= -247/256) & (delta >= 2 - skoS2**2) & (8127*skoS2/160 + 1691/64 >= skoX*(skoX*(16254*skoS2 + 8455) + 6560)/320)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(67865, 256)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-247, 256)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Add(Mul(Rational(8127, 160), Symbol('skoS2')), Rational(1691, 64)), Mul(Rational(1, 320), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(16254), Symbol('skoS2')), Integer(8455))), Integer(6560)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_20(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 1083753/4096) & (delta >= skoS2**2 - 2) & (delta - skoX >= -1083753/4096) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (65709*skoS2/1280 - skoSM*(126*skoS2 + 61)/40 + 68307/2560 >= skoX*(2560*skoSM + skoX*(131418*skoS2 - 64*skoSM*(126*skoS2 + 61) + 68307) + 51960)/2560)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(1083753, 4096)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-1083753, 4096)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), GreaterThan(Add(Mul(Rational(65709, 1280), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(68307, 2560)), Mul(Rational(1, 2560), Symbol('skoX'), Add(Mul(Integer(2560), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(131418), Symbol('skoS2')), Mul(Integer(-1), Integer(64), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(68307))), Integer(51960)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_21(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 1083753/4096) & (delta >= skoS2**2 - 2) & (delta - skoX >= -247/256) & (delta >= 2 - skoS2**2) & (64953*skoS2/1280 + 13515/512 >= 3*skoX*(skoX*(43302*skoS2 + 22525) + 17480)/2560)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(1083753, 4096)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-247, 256)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Add(Mul(Rational(64953, 1280), Symbol('skoS2')), Rational(13515, 512)), Mul(Rational(3, 2560), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(43302), Symbol('skoS2')), Integer(22525))), Integer(17480)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_22(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 272505/1024) & (delta >= skoS2**2 - 2) & (delta - skoX >= -272505/1024) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (32949*skoS2/640 - skoSM*(126*skoS2 + 61)/40 + 34251/1280 >= skoX*(1280*skoSM + skoX*(65898*skoS2 - 32*skoSM*(126*skoS2 + 61) + 34251) + 26040)/1280)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(272505, 1024)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-272505, 1024)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), GreaterThan(Add(Mul(Rational(32949, 640), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(34251, 1280)), Mul(Rational(1, 1280), Symbol('skoX'), Add(Mul(Integer(1280), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(65898), Symbol('skoS2')), Mul(Integer(-1), Integer(32), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(34251))), Integer(26040)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_23(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 272505/1024) & (delta >= skoS2**2 - 2) & (delta - skoX >= -16263/16384) & (delta >= 2 - skoS2**2) & (131103*skoS2/2560 + 136333/5120 >= skoX*(skoX*(262206*skoS2 + 136333) + 104600)/5120)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(272505, 1024)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-16263, 16384)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Add(Mul(Rational(131103, 2560), Symbol('skoS2')), Rational(136333, 5120)), Mul(Rational(1, 5120), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(262206), Symbol('skoS2')), Integer(136333))), Integer(104600)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_24(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 1224) & (delta >= skoS2**2 - 2) & (delta - skoX >= -1224) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (441*skoS2/4 - skoSM*(126*skoS2 + 61)/40 + 2283/40 >= skoX*(40*skoSM + skoX*(4410*skoS2 - skoSM*(126*skoS2 + 61) + 2283) + 1560)/40)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Integer(1224)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-1224)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), GreaterThan(Add(Mul(Rational(441, 4), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(2283, 40)), Mul(Rational(1, 40), Symbol('skoX'), Add(Mul(Integer(40), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(4410), Symbol('skoS2')), Mul(Integer(-1), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(2283))), Integer(1560)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_25(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= skoX) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta >= -skoX) & (delta + skoX >= 1224) & (delta >= skoS2**2 - 2) & (delta - skoX >= -1224) & (delta >= 2 - skoS2**2) & (1071*skoS2/10 + 1111/20 >= skoX*(skoX*(2142*skoS2 + 1111) + 800)/20)

	pre_cond = And(GreaterThan(Symbol('delta'), Symbol('skoX')), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Integer(1224)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-1224)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Add(Mul(Rational(1071, 10), Symbol('skoS2')), Rational(1111, 20)), Mul(Rational(1, 20), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(2142), Symbol('skoS2')), Integer(1111))), Integer(800)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_26(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 18161/64) & (delta >= skoS2**2 - 2) & (delta - skoX >= -18161/64) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (1701*skoS2/32 - skoSM*(126*skoS2 + 61)/40 + 8839/320 >= skoX*(320*skoSM + skoX*(17010*skoS2 - 8*skoSM*(126*skoS2 + 61) + 8839) + 6680)/320)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(18161, 64)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-18161, 64)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), GreaterThan(Add(Mul(Rational(1701, 32), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(8839, 320)), Mul(Rational(1, 320), Symbol('skoX'), Add(Mul(Integer(320), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(17010), Symbol('skoS2')), Mul(Integer(-1), Integer(8), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(8839))), Integer(6680)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_27(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 18161/64) & (delta >= skoS2**2 - 2) & (delta - skoX >= -1023/1024) & (delta >= 2 - skoS2**2) & (33957*skoS2/640 + 7059/256 >= 3*skoX*(skoX*(22638*skoS2 + 11765) + 8920)/1280)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(18161, 64)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-1023, 1024)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Add(Mul(Rational(33957, 640), Symbol('skoS2')), Rational(7059, 256)), Mul(Rational(3, 1280), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(22638), Symbol('skoS2')), Integer(11765))), Integer(8920)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_28(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 9024) & (delta >= skoS2**2 - 2) & (delta - skoX >= -9024) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (1197*skoS2/4 - skoSM*(126*skoS2 + 61)/40 + 6183/40 >= skoX*(40*skoSM + skoX*(11970*skoS2 - skoSM*(126*skoS2 + 61) + 6183) + 3960)/40)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Integer(9024)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-9024)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), GreaterThan(Add(Mul(Rational(1197, 4), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(6183, 40)), Mul(Rational(1, 40), Symbol('skoX'), Add(Mul(Integer(40), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(11970), Symbol('skoS2')), Mul(Integer(-1), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(6183))), Integer(3960)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_29(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= skoX) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta >= -skoX) & (delta + skoX >= 9024) & (delta >= skoS2**2 - 2) & (delta - skoX >= -9024) & (delta >= 2 - skoS2**2) & (2961*skoS2/10 + 3061/20 >= skoX*(skoX*(5922*skoS2 + 3061) + 2000)/20)

	pre_cond = And(GreaterThan(Symbol('delta'), Symbol('skoX')), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Integer(9024)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-9024)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Add(Mul(Rational(2961, 10), Symbol('skoS2')), Rational(3061, 20)), Mul(Rational(1, 20), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(5922), Symbol('skoS2')), Integer(3061))), Integer(2000)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_30(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 1196835) & (delta >= skoS2**2 - 2) & (delta - skoX >= -1196835) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (34461*skoS2/10 - skoSM*(126*skoS2 + 61)/40 + 35559/20 >= skoX*(40*skoSM + skoX*(137844*skoS2 - skoSM*(126*skoS2 + 61) + 71118) + 43920)/40)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Integer(1196835)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-1196835)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), GreaterThan(Add(Mul(Rational(34461, 10), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(35559, 20)), Mul(Rational(1, 40), Symbol('skoX'), Add(Mul(Integer(40), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(137844), Symbol('skoS2')), Mul(Integer(-1), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(71118))), Integer(43920)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_31(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= skoX) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta >= -skoX) & (delta + skoX >= 1196835) & (delta >= skoS2**2 - 2) & (delta - skoX >= -1196835) & (delta >= 2 - skoS2**2) & (68859*skoS2/20 + 71057/40 >= 7*skoX*(skoX*(19674*skoS2 + 10151) + 6280)/40)

	pre_cond = And(GreaterThan(Symbol('delta'), Symbol('skoX')), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Integer(1196835)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-1196835)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Add(Mul(Rational(68859, 20), Symbol('skoS2')), Rational(71057, 40)), Mul(Rational(7, 40), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(19674), Symbol('skoS2')), Integer(10151))), Integer(6280)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_32(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 1194648) & (delta >= skoS2**2 - 2) & (delta - skoX >= -1194648) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (68859*skoS2/20 - skoSM*(126*skoS2 + 61)/40 + 71053/40 >= skoX*(40*skoSM + skoX*(137718*skoS2 - skoSM*(126*skoS2 + 61) + 71053) + 43880)/40)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Integer(1194648)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-1194648)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), GreaterThan(Add(Mul(Rational(68859, 20), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(71053, 40)), Mul(Rational(1, 40), Symbol('skoX'), Add(Mul(Integer(40), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(137718), Symbol('skoS2')), Mul(Integer(-1), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(71053))), Integer(43880)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_33(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= skoX) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta >= -skoX) & (delta + skoX >= 1194648) & (delta >= skoS2**2 - 2) & (delta - skoX >= -1194648) & (delta >= 2 - skoS2**2) & (17199*skoS2/5 + 8874/5 >= 9*skoX*(skoX*(1911*skoS2 + 986) + 610)/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Symbol('skoX')), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Integer(1194648)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-1194648)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Add(Mul(Rational(17199, 5), Symbol('skoS2')), Rational(8874, 5)), Mul(Rational(9, 5), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(1911), Symbol('skoS2')), Integer(986))), Integer(610)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_34(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 4774221/4) & (delta >= skoS2**2 - 2) & (delta - skoX >= -4774221/4) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (27531*skoS2/8 - skoSM*(126*skoS2 + 61)/40 + 142041/80 >= skoX*(80*skoSM + skoX*(275310*skoS2 - 2*skoSM*(126*skoS2 + 61) + 142041) + 87720)/80)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(4774221, 4)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-4774221, 4)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), GreaterThan(Add(Mul(Rational(27531, 8), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(142041, 80)), Mul(Rational(1, 80), Symbol('skoX'), Add(Mul(Integer(80), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(275310), Symbol('skoS2')), Mul(Integer(-1), Integer(2), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(142041))), Integer(87720)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_35(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= skoX) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta >= -skoX) & (delta + skoX >= 4774221/4) & (delta >= skoS2**2 - 2) & (delta - skoX >= -4774221/4) & (delta >= 2 - skoS2**2) & (137529*skoS2/40 + 141919/80 >= skoX*(skoX*(275058*skoS2 + 141919) + 87800)/80)

	pre_cond = And(GreaterThan(Symbol('delta'), Symbol('skoX')), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(4774221, 4)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-4774221, 4)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Add(Mul(Rational(137529, 40), Symbol('skoS2')), Rational(141919, 80)), Mul(Rational(1, 80), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(275058), Symbol('skoS2')), Integer(141919))), Integer(87800)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_36(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 11102223) & (delta >= skoS2**2 - 2) & (delta - skoX >= -11102223) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (52479*skoS2/5 - skoSM*(126*skoS2 + 61)/40 + 54147/10 >= skoX*(40*skoSM + skoX*(419832*skoS2 - skoSM*(126*skoS2 + 61) + 216588) + 133440)/40)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Integer(11102223)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-11102223)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), GreaterThan(Add(Mul(Rational(52479, 5), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(54147, 10)), Mul(Rational(1, 40), Symbol('skoX'), Add(Mul(Integer(40), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(419832), Symbol('skoS2')), Mul(Integer(-1), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(216588))), Integer(133440)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_37(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= skoX) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta >= -skoX) & (delta + skoX >= 11102223) & (delta >= skoS2**2 - 2) & (delta - skoX >= -11102223) & (delta >= 2 - skoS2**2) & (209853*skoS2/20 + 216527/40 >= skoX*(skoX*(419706*skoS2 + 216527) + 133480)/40)

	pre_cond = And(GreaterThan(Symbol('delta'), Symbol('skoX')), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Integer(11102223)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-11102223)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Add(Mul(Rational(209853, 20), Symbol('skoS2')), Rational(216527, 40)), Mul(Rational(1, 40), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(419706), Symbol('skoS2')), Integer(216527))), Integer(133480)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_38(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 46730895) & (delta >= skoS2**2 - 2) & (delta - skoX >= -46730895) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (107667*skoS2/5 - skoSM*(126*skoS2 + 61)/40 + 111087/10 >= skoX*(40*skoSM + skoX*(861336*skoS2 - skoSM*(126*skoS2 + 61) + 444348) + 273600)/40)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Integer(46730895)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-46730895)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), GreaterThan(Add(Mul(Rational(107667, 5), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(111087, 10)), Mul(Rational(1, 40), Symbol('skoX'), Add(Mul(Integer(40), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(861336), Symbol('skoS2')), Mul(Integer(-1), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(444348))), Integer(273600)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_39(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= skoX) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta >= -skoX) & (delta + skoX >= 46730895) & (delta >= skoS2**2 - 2) & (delta - skoX >= -46730895) & (delta >= 2 - skoS2**2) & (86121*skoS2/4 + 444287/40 >= skoX*(skoX*(861210*skoS2 + 444287) + 273640)/40)

	pre_cond = And(GreaterThan(Symbol('delta'), Symbol('skoX')), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Integer(46730895)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-46730895)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Add(Mul(Rational(86121, 4), Symbol('skoS2')), Rational(444287, 40)), Mul(Rational(1, 40), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(861210), Symbol('skoS2')), Integer(444287))), Integer(273640)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_40(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 208109475) & (delta >= skoS2**2 - 2) & (delta - skoX >= -208109475) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (454419*skoS2/10 - skoSM*(126*skoS2 + 61)/40 + 468849/20 >= skoX*(40*skoSM + skoX*(1817676*skoS2 - skoSM*(126*skoS2 + 61) + 937698) + 577200)/40)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Integer(208109475)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-208109475)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), GreaterThan(Add(Mul(Rational(454419, 10), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(468849, 20)), Mul(Rational(1, 40), Symbol('skoX'), Add(Mul(Integer(40), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(1817676), Symbol('skoS2')), Mul(Integer(-1), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(937698))), Integer(577200)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_41(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= skoX) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta >= -skoX) & (delta + skoX >= 208109475) & (delta >= skoS2**2 - 2) & (delta - skoX >= -208109475) & (delta >= 2 - skoS2**2) & (181755*skoS2/4 + 937637/40 >= skoX*(skoX*(1817550*skoS2 + 937637) + 577240)/40)

	pre_cond = And(GreaterThan(Symbol('delta'), Symbol('skoX')), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Integer(208109475)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-208109475)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Add(Mul(Rational(181755, 4), Symbol('skoS2')), Rational(937637, 40)), Mul(Rational(1, 40), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(1817550), Symbol('skoS2')), Integer(937637))), Integer(577240)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_42(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 208080624) & (delta >= skoS2**2 - 2) & (delta - skoX >= -208080624) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (181755*skoS2/4 - skoSM*(126*skoS2 + 61)/40 + 937633/40 >= skoX*(40*skoSM + skoX*(1817550*skoS2 - skoSM*(126*skoS2 + 61) + 937633) + 577160)/40)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Integer(208080624)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-208080624)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), GreaterThan(Add(Mul(Rational(181755, 4), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(937633, 40)), Mul(Rational(1, 40), Symbol('skoX'), Add(Mul(Integer(40), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(1817550), Symbol('skoS2')), Mul(Integer(-1), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(937633))), Integer(577160)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_43(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= skoX) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta >= -skoX) & (delta + skoX >= 208080624) & (delta >= skoS2**2 - 2) & (delta - skoX >= -208080624) & (delta >= 2 - skoS2**2) & (227178*skoS2/5 + 234393/10 >= 3*skoX*(skoX*(151452*skoS2 + 78131) + 48100)/10)

	pre_cond = And(GreaterThan(Symbol('delta'), Symbol('skoX')), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Integer(208080624)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-208080624)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Add(Mul(Rational(227178, 5), Symbol('skoS2')), Rational(234393, 10)), Mul(Rational(3, 10), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(151452), Symbol('skoS2')), Integer(78131))), Integer(48100)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_44(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 1052742915) & (delta >= skoS2**2 - 2) & (delta - skoX >= -1052742915) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (1022049*skoS2/10 - skoSM*(126*skoS2 + 61)/40 + 1054499/20 >= skoX*(40*skoSM + skoX*(4088196*skoS2 - skoSM*(126*skoS2 + 61) + 2108998) + 1298000)/40)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Integer(1052742915)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-1052742915)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), GreaterThan(Add(Mul(Rational(1022049, 10), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(1054499, 20)), Mul(Rational(1, 40), Symbol('skoX'), Add(Mul(Integer(40), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(4088196), Symbol('skoS2')), Mul(Integer(-1), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(2108998))), Integer(1298000)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_45(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= skoX) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta >= -skoX) & (delta + skoX >= 1052742915) & (delta >= skoS2**2 - 2) & (delta - skoX >= -1052742915) & (delta >= 2 - skoS2**2) & (408807*skoS2/4 + 2108937/40 >= 3*skoX*(skoX*(1362690*skoS2 + 702979) + 432680)/40)

	pre_cond = And(GreaterThan(Symbol('delta'), Symbol('skoX')), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Integer(1052742915)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-1052742915)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Add(Mul(Rational(408807, 4), Symbol('skoS2')), Rational(2108937, 40)), Mul(Rational(3, 40), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(1362690), Symbol('skoS2')), Integer(702979))), Integer(432680)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_46(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 1052029224) & (delta >= skoS2**2 - 2) & (delta - skoX >= -1052029224) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (408681*skoS2/4 - skoSM*(126*skoS2 + 61)/40 + 2108283/40 >= skoX*(40*skoSM + skoX*(4086810*skoS2 - skoSM*(126*skoS2 + 61) + 2108283) + 1297560)/40)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Integer(1052029224)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-1052029224)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), GreaterThan(Add(Mul(Rational(408681, 4), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(2108283, 40)), Mul(Rational(1, 40), Symbol('skoX'), Add(Mul(Integer(40), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(4086810), Symbol('skoS2')), Mul(Integer(-1), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(2108283))), Integer(1297560)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_47(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 1052029224) & (delta >= skoS2**2 - 2) & (delta - skoX >= -255/256) & (delta >= 2 - skoS2**2) & (32694417*skoS2/320 + 33732467/640 >= skoX*(skoX*(65388834*skoS2 + 33732467) + 20761000)/640)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Integer(1052029224)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-255, 256)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Add(Mul(Rational(32694417, 320), Symbol('skoS2')), Rational(33732467, 640)), Mul(Rational(1, 640), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(65388834), Symbol('skoS2')), Integer(33732467))), Integer(20761000)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_48(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 7471182095) & (delta >= skoS2**2 - 2) & (delta - skoX >= -7471182095) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (1361367*skoS2/5 - skoSM*(126*skoS2 + 61)/40 + 1404587/10 >= skoX*(40*skoSM + skoX*(10890936*skoS2 - skoSM*(126*skoS2 + 61) + 5618348) + 3457600)/40)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Integer(7471182095)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-7471182095)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), GreaterThan(Add(Mul(Rational(1361367, 5), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(1404587, 10)), Mul(Rational(1, 40), Symbol('skoX'), Add(Mul(Integer(40), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(10890936), Symbol('skoS2')), Mul(Integer(-1), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(5618348))), Integer(3457600)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_49(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= skoX) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta >= -skoX) & (delta + skoX >= 7471182095) & (delta >= skoS2**2 - 2) & (delta - skoX >= -7471182095) & (delta >= 2 - skoS2**2) & (1089081*skoS2/4 + 5618287/40 >= skoX*(skoX*(10890810*skoS2 + 5618287) + 3457640)/40)

	pre_cond = And(GreaterThan(Symbol('delta'), Symbol('skoX')), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Integer(7471182095)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-7471182095)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Add(Mul(Rational(1089081, 4), Symbol('skoS2')), Rational(5618287, 40)), Mul(Rational(1, 40), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(10890810), Symbol('skoS2')), Integer(5618287))), Integer(3457640)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_50(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 264934619523) & (delta >= skoS2**2 - 2) & (delta - skoX >= -264934619523) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (16213617*skoS2/10 - skoSM*(126*skoS2 + 61)/40 + 16728339/20 >= skoX*(40*skoSM + skoX*(64854468*skoS2 - skoSM*(126*skoS2 + 61) + 33456678) + 20588880)/40)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Integer(264934619523)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-264934619523)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), GreaterThan(Add(Mul(Rational(16213617, 10), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(16728339, 20)), Mul(Rational(1, 40), Symbol('skoX'), Add(Mul(Integer(40), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(64854468), Symbol('skoS2')), Mul(Integer(-1), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(33456678))), Integer(20588880)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_51(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= skoX) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta >= -skoX) & (delta + skoX >= 264934619523) & (delta >= skoS2**2 - 2) & (delta - skoX >= -264934619523) & (delta >= 2 - skoS2**2) & (32427171*skoS2/20 + 33456617/40 >= skoX*(skoX*(64854342*skoS2 + 33456617) + 20588920)/40)

	pre_cond = And(GreaterThan(Symbol('delta'), Symbol('skoX')), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Integer(264934619523)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-264934619523)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Add(Mul(Rational(32427171, 20), Symbol('skoS2')), Rational(33456617, 40)), Mul(Rational(1, 40), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(64854342), Symbol('skoS2')), Integer(33456617))), Integer(20588920)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_52(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 1828761268488) & (delta >= skoS2**2 - 2) & (delta - skoX >= -1828761268488) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (85195971*skoS2/20 - skoSM*(126*skoS2 + 61)/40 + 87900613/40 >= skoX*(40*skoSM + skoX*(170391942*skoS2 - skoSM*(126*skoS2 + 61) + 87900613) + 54092840)/40)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Integer(1828761268488)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-1828761268488)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), GreaterThan(Add(Mul(Rational(85195971, 20), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(87900613, 40)), Mul(Rational(1, 40), Symbol('skoX'), Add(Mul(Integer(40), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(170391942), Symbol('skoS2')), Mul(Integer(-1), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(87900613))), Integer(54092840)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_53(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= skoX) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta >= -skoX) & (delta + skoX >= 1828761268488) & (delta >= skoS2**2 - 2) & (delta - skoX >= -1828761268488) & (delta >= 2 - skoS2**2) & (21298977*skoS2/5 + 10987569/5 >= 27*skoX*(skoX*(788851*skoS2 + 406947) + 250430)/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Symbol('skoX')), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Integer(1828761268488)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-1828761268488)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Add(Mul(Rational(21298977, 5), Symbol('skoS2')), Rational(10987569, 5)), Mul(Rational(27, 5), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(788851), Symbol('skoS2')), Integer(406947))), Integer(250430)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_54(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 1621109539983) & (delta >= skoS2**2 - 2) & (delta - skoX >= -1621109539983) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (20053341*skoS2/5 - skoSM*(126*skoS2 + 61)/40 + 20689957/10 >= skoX*(40*skoSM + skoX*(160426728*skoS2 - skoSM*(126*skoS2 + 61) + 82759828) + 50929280)/40)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Integer(1621109539983)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-1621109539983)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), GreaterThan(Add(Mul(Rational(20053341, 5), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(20689957, 10)), Mul(Rational(1, 40), Symbol('skoX'), Add(Mul(Integer(40), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(160426728), Symbol('skoS2')), Mul(Integer(-1), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(82759828))), Integer(50929280)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_55(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 1621109539983) & (delta >= skoS2**2 - 2) & (delta - skoX >= -15/16) & (delta >= 2 - skoS2**2) & (320853393*skoS2/80 + 331039251/160 >= 27*skoX*(skoX*(23766918*skoS2 + 12260713) + 7545080)/160)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Integer(1621109539983)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-15, 16)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Add(Mul(Rational(320853393, 80), Symbol('skoS2')), Rational(331039251, 160)), Mul(Rational(27, 160), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(23766918), Symbol('skoS2')), Integer(12260713))), Integer(7545080)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_56(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 1554298291224) & (delta >= skoS2**2 - 2) & (delta - skoX >= -1554298291224) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (15708609*skoS2/4 - skoSM*(126*skoS2 + 61)/40 + 81036483/40 >= skoX*(40*skoSM + skoX*(157086090*skoS2 - skoSM*(126*skoS2 + 61) + 81036483) + 49868760)/40)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Integer(1554298291224)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-1554298291224)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), GreaterThan(Add(Mul(Rational(15708609, 4), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(81036483, 40)), Mul(Rational(1, 40), Symbol('skoX'), Add(Mul(Integer(40), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(157086090), Symbol('skoS2')), Mul(Integer(-1), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(81036483))), Integer(49868760)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_57(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 1554298291224) & (delta >= skoS2**2 - 2) & (delta - skoX >= -255/256) & (delta >= 2 - skoS2**2) & (1256688657*skoS2/320 + 1296583667/640 >= skoX*(skoX*(2513377314*skoS2 + 1296583667) + 797900200)/640)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Integer(1554298291224)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-255, 256)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Add(Mul(Rational(1256688657, 320), Symbol('skoS2')), Rational(1296583667, 640)), Mul(Rational(1, 640), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(2513377314), Symbol('skoS2')), Integer(1296583667))), Integer(797900200)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_58(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 6217188178037/4) & (delta >= skoS2**2 - 2) & (delta - skoX >= -6217188178037/4) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (157086027*skoS2/40 - skoSM*(126*skoS2 + 61)/40 + 162072901/80 >= skoX*(80*skoSM + skoX*(314172054*skoS2 - 2*skoSM*(126*skoS2 + 61) + 162072901) + 99737480)/80)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(6217188178037, 4)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-6217188178037, 4)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), GreaterThan(Add(Mul(Rational(157086027, 40), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(162072901, 80)), Mul(Rational(1, 80), Symbol('skoX'), Add(Mul(Integer(80), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(314172054), Symbol('skoS2')), Mul(Integer(-1), Integer(2), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(162072901))), Integer(99737480)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_59(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 6217188178037/4) & (delta >= skoS2**2 - 2) & (delta - skoX >= -255/256) & (delta >= 2 - skoS2**2) & (1256688153*skoS2/320 + 1296583147/640 >= skoX*(skoX*(2513376306*skoS2 + 1296583147) + 797899880)/640)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(6217188178037, 4)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-255, 256)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Add(Mul(Rational(1256688153, 320), Symbol('skoS2')), Rational(1296583147, 640)), Mul(Rational(1, 640), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(2513376306), Symbol('skoS2')), Integer(1296583147))), Integer(797899880)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_60(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 1269971224899) & (delta >= skoS2**2 - 2) & (delta - skoX >= -1269971224899) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (7099659*skoS2/2 - skoSM*(126*skoS2 + 61)/40 + 36625229/20 >= skoX*(40*skoSM + skoX*(141993180*skoS2 - skoSM*(126*skoS2 + 61) + 73250458) + 45077360)/40)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Integer(1269971224899)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-1269971224899)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), GreaterThan(Add(Mul(Rational(7099659, 2), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(36625229, 20)), Mul(Rational(1, 40), Symbol('skoX'), Add(Mul(Integer(40), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(141993180), Symbol('skoS2')), Mul(Integer(-1), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(73250458))), Integer(45077360)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_61(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 1269971224899) & (delta >= skoS2**2 - 2) & (delta - skoX >= -3/4) & (delta >= 2 - skoS2**2) & (141993117*skoS2/40 + 29300171/16 >= skoX*(skoX*(283986234*skoS2 + 146500855) + 90154760)/80)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Integer(1269971224899)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-3, 4)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Add(Mul(Rational(141993117, 40), Symbol('skoS2')), Rational(29300171, 16)), Mul(Rational(1, 80), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(283986234), Symbol('skoS2')), Integer(146500855))), Integer(90154760)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_62(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 1615865541888) & (delta >= skoS2**2 - 2) & (delta - skoX >= -1615865541888) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (80083521*skoS2/20 - skoSM*(126*skoS2 + 61)/40 + 82625863/40 >= skoX*(40*skoSM + skoX*(160167042*skoS2 - skoSM*(126*skoS2 + 61) + 82625863) + 50846840)/40)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Integer(1615865541888)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-1615865541888)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), GreaterThan(Add(Mul(Rational(80083521, 20), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(82625863, 40)), Mul(Rational(1, 40), Symbol('skoX'), Add(Mul(Integer(40), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(160167042), Symbol('skoS2')), Mul(Integer(-1), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(82625863))), Integer(50846840)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_63(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 1615865541888) & (delta >= skoS2**2 - 2) & (delta - skoX >= -1023/1024) & (delta >= 2 - skoS2**2) & (2562672609*skoS2/640 + 528805511/256 >= skoX*(skoX*(5125345218*skoS2 + 2644027555) + 1627098920)/1280)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Integer(1615865541888)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-1023, 1024)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Add(Mul(Rational(2562672609, 640), Symbol('skoS2')), Rational(528805511, 256)), Mul(Rational(1, 1280), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(5125345218), Symbol('skoS2')), Integer(2644027555))), Integer(1627098920)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_64(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 1536389998143) & (delta >= skoS2**2 - 2) & (delta - skoX >= -1536389998143) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (19522314*skoS2/5 - skoSM*(126*skoS2 + 61)/40 + 10071036/5 >= skoX*(40*skoSM + skoX*(156178512*skoS2 - skoSM*(126*skoS2 + 61) + 80568288) + 49580640)/40)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Integer(1536389998143)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-1536389998143)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), GreaterThan(Add(Mul(Rational(19522314, 5), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(10071036, 5)), Mul(Rational(1, 40), Symbol('skoX'), Add(Mul(Integer(40), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(156178512), Symbol('skoS2')), Mul(Integer(-1), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(80568288))), Integer(49580640)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_65(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 1536389998143) & (delta >= skoS2**2 - 2) & (delta - skoX >= -4095/4096) & (delta >= 2 - skoS2**2) & (4997712321*skoS2/1280 + 5156370371/2560 >= skoX*(skoX*(9995424642*skoS2 + 5156370371) + 3173161000)/2560)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Integer(1536389998143)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-4095, 4096)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Add(Mul(Rational(4997712321, 1280), Symbol('skoS2')), Rational(5156370371, 2560)), Mul(Rational(1, 2560), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(9995424642), Symbol('skoS2')), Integer(5156370371))), Integer(3173161000)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_66(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 6145555034525/4) & (delta >= skoS2**2 - 2) & (delta - skoX >= -6145555034525/4) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (156178449*skoS2/40 - skoSM*(126*skoS2 + 61)/40 + 161136511/80 >= skoX*(80*skoSM + skoX*(312356898*skoS2 - 2*skoSM*(126*skoS2 + 61) + 161136511) + 99161240)/80)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(6145555034525, 4)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-6145555034525, 4)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), GreaterThan(Add(Mul(Rational(156178449, 40), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(161136511, 80)), Mul(Rational(1, 80), Symbol('skoX'), Add(Mul(Integer(80), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(312356898), Symbol('skoS2')), Mul(Integer(-1), Integer(2), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(161136511))), Integer(99161240)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_67(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 6145555034525/4) & (delta >= skoS2**2 - 2) & (delta - skoX >= -4095/4096) & (delta >= 2 - skoS2**2) & (999542061*skoS2/256 + 5156368291/2560 >= skoX*(skoX*(9995420610*skoS2 + 5156368291) + 3173159720)/2560)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(6145555034525, 4)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-4095, 4096)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Add(Mul(Rational(999542061, 256), Symbol('skoS2')), Rational(5156368291, 2560)), Mul(Rational(1, 2560), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(9995420610), Symbol('skoS2')), Integer(5156368291))), Integer(3173159720)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_68(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 1790118230208) & (delta >= skoS2**2 - 2) & (delta - skoX >= -1790118230208) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (84291039*skoS2/20 - skoSM*(126*skoS2 + 61)/40 + 86966953/40 >= skoX*(40*skoSM + skoX*(168582078*skoS2 - skoSM*(126*skoS2 + 61) + 86966953) + 53518280)/40)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Integer(1790118230208)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-1790118230208)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), GreaterThan(Add(Mul(Rational(84291039, 20), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(86966953, 40)), Mul(Rational(1, 40), Symbol('skoX'), Add(Mul(Integer(40), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(168582078), Symbol('skoS2')), Mul(Integer(-1), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(86966953))), Integer(53518280)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_69(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 1790118230208) & (delta >= skoS2**2 - 2) & (delta - skoX >= -255/256) & (delta >= 2 - skoS2**2) & (1348656561*skoS2/320 + 1391471187/640 >= 3*skoX*(skoX*(899104374*skoS2 + 463823729) + 285430840)/640)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Integer(1790118230208)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-255, 256)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Add(Mul(Rational(1348656561, 320), Symbol('skoS2')), Rational(1391471187, 640)), Mul(Rational(3, 640), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(899104374), Symbol('skoS2')), Integer(463823729))), Integer(285430840)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_70(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 52663744206440) & (delta >= skoS2**2 - 2) & (delta - skoX >= -52663744206440) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (457189677*skoS2/20 - skoSM*(126*skoS2 + 61)/40 + 471703643/40 >= skoX*(40*skoSM + skoX*(914379354*skoS2 - skoSM*(126*skoS2 + 61) + 471703643) + 290279320)/40)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Integer(52663744206440)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-52663744206440)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), GreaterThan(Add(Mul(Rational(457189677, 20), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(471703643, 40)), Mul(Rational(1, 40), Symbol('skoX'), Add(Mul(Integer(40), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(914379354), Symbol('skoS2')), Mul(Integer(-1), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(471703643))), Integer(290279320)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_71(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= skoX) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta >= -skoX) & (delta + skoX >= 52663744206440) & (delta >= skoS2**2 - 2) & (delta - skoX >= -52663744206440) & (delta >= 2 - skoS2**2) & (228594807*skoS2/10 + 235851791/20 >= 7*skoX*(skoX*(65312802*skoS2 + 33693113) + 20734240)/20)

	pre_cond = And(GreaterThan(Symbol('delta'), Symbol('skoX')), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Integer(52663744206440)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-52663744206440)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Add(Mul(Rational(228594807, 10), Symbol('skoS2')), Rational(235851791, 20)), Mul(Rational(7, 20), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(65312802), Symbol('skoS2')), Integer(33693113))), Integer(20734240)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_72(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 1773992239568) & (delta >= skoS2**2 - 2) & (delta - skoX >= -1773992239568) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (83910519*skoS2/20 - skoSM*(126*skoS2 + 61)/40 + 86574353/40 >= skoX*(40*skoSM + skoX*(167821038*skoS2 - skoSM*(126*skoS2 + 61) + 86574353) + 53276680)/40)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Integer(1773992239568)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-1773992239568)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), GreaterThan(Add(Mul(Rational(83910519, 20), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(86574353, 40)), Mul(Rational(1, 40), Symbol('skoX'), Add(Mul(Integer(40), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(167821038), Symbol('skoS2')), Mul(Integer(-1), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(86574353))), Integer(53276680)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_73(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 1773992239568) & (delta >= skoS2**2 - 2) & (delta - skoX >= -4095/4096) & (delta >= 2 - skoS2**2) & (5370273153*skoS2/1280 + 5540758531/2560 >= 7*skoX*(skoX*(1534363758*skoS2 + 791536933) + 487101080)/2560)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Integer(1773992239568)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-4095, 4096)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Add(Mul(Rational(5370273153, 1280), Symbol('skoS2')), Rational(5540758531, 2560)), Mul(Rational(7, 2560), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(1534363758), Symbol('skoS2')), Integer(791536933))), Integer(487101080)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_74(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 255271399156224) & (delta >= skoS2**2 - 2) & (delta - skoX >= -255271399156224) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (201312909*skoS2/4 - skoSM*(126*skoS2 + 61)/40 + 1038518983/40 >= skoX*(40*skoSM + skoX*(2013129090*skoS2 - skoSM*(126*skoS2 + 61) + 1038518983) + 639088760)/40)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Integer(255271399156224)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-255271399156224)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), GreaterThan(Add(Mul(Rational(201312909, 4), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(1038518983, 40)), Mul(Rational(1, 40), Symbol('skoX'), Add(Mul(Integer(40), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(2013129090), Symbol('skoS2')), Mul(Integer(-1), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(1038518983))), Integer(639088760)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_75(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= skoX) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta >= -skoX) & (delta + skoX >= 255271399156224) & (delta >= skoS2**2 - 2) & (delta - skoX >= -255271399156224) & (delta >= 2 - skoS2**2) & (503282241*skoS2/10 + 519259461/20 >= 21*skoX*(skoX*(47931642*skoS2 + 24726641) + 15216400)/20)

	pre_cond = And(GreaterThan(Symbol('delta'), Symbol('skoX')), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Integer(255271399156224)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-255271399156224)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Add(Mul(Rational(503282241, 10), Symbol('skoS2')), Rational(519259461, 20)), Mul(Rational(21, 20), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(47931642), Symbol('skoS2')), Integer(24726641))), Integer(15216400)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_76(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 1601986856429583) & (delta >= skoS2**2 - 2) & (delta - skoX >= -1601986856429583) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (630391041*skoS2/5 - skoSM*(126*skoS2 + 61)/40 + 650403457/10 >= skoX*(40*skoSM + skoX*(5043128328*skoS2 - skoSM*(126*skoS2 + 61) + 2601613828) + 1600993280)/40)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Integer(1601986856429583)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-1601986856429583)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), GreaterThan(Add(Mul(Rational(630391041, 5), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(650403457, 10)), Mul(Rational(1, 40), Symbol('skoX'), Add(Mul(Integer(40), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(5043128328), Symbol('skoS2')), Mul(Integer(-1), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(2601613828))), Integer(1600993280)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_77(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= skoX) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta >= -skoX) & (delta + skoX >= 1601986856429583) & (delta >= skoS2**2 - 2) & (delta - skoX >= -1601986856429583) & (delta >= 2 - skoS2**2) & (2521564101*skoS2/20 + 2601613767/40 >= 3*skoX*(skoX*(1681042734*skoS2 + 867204589) + 533664440)/40)

	pre_cond = And(GreaterThan(Symbol('delta'), Symbol('skoX')), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Integer(1601986856429583)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-1601986856429583)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Add(Mul(Rational(2521564101, 20), Symbol('skoS2')), Rational(2601613767, 40)), Mul(Rational(3, 40), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(1681042734), Symbol('skoS2')), Integer(867204589))), Integer(533664440)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_78(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 26164843721316035) & (delta >= skoS2**2 - 2) & (delta - skoX >= -26164843721316035) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (5095298439*skoS2/10 - skoSM*(126*skoS2 + 61)/40 + 5257053949/20 >= skoX*(40*skoSM + skoX*(20381193756*skoS2 - skoSM*(126*skoS2 + 61) + 10514107898) + 6470220400)/40)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Integer(26164843721316035)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-26164843721316035)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), GreaterThan(Add(Mul(Rational(5095298439, 10), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(5257053949, 20)), Mul(Rational(1, 40), Symbol('skoX'), Add(Mul(Integer(40), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(20381193756), Symbol('skoS2')), Mul(Integer(-1), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(10514107898))), Integer(6470220400)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_79(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= skoX) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta >= -skoX) & (delta + skoX >= 26164843721316035) & (delta >= skoS2**2 - 2) & (delta - skoX >= -26164843721316035) & (delta >= 2 - skoS2**2) & (2038119363*skoS2/4 + 10514107837/40 >= skoX*(skoX*(20381193630*skoS2 + 10514107837) + 6470220440)/40)

	pre_cond = And(GreaterThan(Symbol('delta'), Symbol('skoX')), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Integer(26164843721316035)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-26164843721316035)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Add(Mul(Rational(2038119363, 4), Symbol('skoS2')), Rational(10514107837, 40)), Mul(Rational(1, 40), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(20381193630), Symbol('skoS2')), Integer(10514107837))), Integer(6470220440)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_80(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 255271367201795) & (delta >= skoS2**2 - 2) & (delta - skoX >= -255271367201795) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (503282241*skoS2/10 - skoSM*(126*skoS2 + 61)/40 + 519259459/20 >= skoX*(40*skoSM + skoX*(2013128964*skoS2 - skoSM*(126*skoS2 + 61) + 1038518918) + 639088720)/40)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Integer(255271367201795)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-255271367201795)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), GreaterThan(Add(Mul(Rational(503282241, 10), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(519259459, 20)), Mul(Rational(1, 40), Symbol('skoX'), Add(Mul(Integer(40), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(2013128964), Symbol('skoS2')), Mul(Integer(-1), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(1038518918))), Integer(639088720)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_81(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= skoX) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta >= -skoX) & (delta + skoX >= 255271367201795) & (delta >= skoS2**2 - 2) & (delta - skoX >= -255271367201795) & (delta >= 2 - skoS2**2) & (1006564419*skoS2/20 + 1038518857/40 >= skoX*(skoX*(2013128838*skoS2 + 1038518857) + 639088760)/40)

	pre_cond = And(GreaterThan(Symbol('delta'), Symbol('skoX')), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Integer(255271367201795)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-255271367201795)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Add(Mul(Rational(1006564419, 20), Symbol('skoS2')), Rational(1038518857, 40)), Mul(Rational(1, 40), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(2013128838), Symbol('skoS2')), Integer(1038518857))), Integer(639088760)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_82(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 1367159203213455) & (delta >= skoS2**2 - 2) & (delta - skoX >= -1367159203213455) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (582358077*skoS2/5 - skoSM*(126*skoS2 + 61)/40 + 600845637/10 >= skoX*(40*skoSM + skoX*(4658864616*skoS2 - skoSM*(126*skoS2 + 61) + 2403382548) + 1479004800)/40)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Integer(1367159203213455)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Integer(-1367159203213455)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), GreaterThan(Add(Mul(Rational(582358077, 5), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(600845637, 10)), Mul(Rational(1, 40), Symbol('skoX'), Add(Mul(Integer(40), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(4658864616), Symbol('skoS2')), Mul(Integer(-1), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(2403382548))), Integer(1479004800)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_83(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 1367159203213455) & (delta >= skoS2**2 - 2) & (delta - skoX >= -15/16) & (delta >= 2 - skoS2**2) & (9317729169*skoS2/80 + 9613530131/160 >= skoX*(skoX*(18635458338*skoS2 + 9613530131) + 5916019240)/160)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Integer(1367159203213455)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-15, 16)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Add(Mul(Rational(9317729169, 80), Symbol('skoS2')), Rational(9613530131, 160)), Mul(Rational(1, 160), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(18635458338), Symbol('skoS2')), Integer(9613530131))), Integer(5916019240)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_84(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 7541502747745674229011117699497985/288230376151711744) & (delta >= skoS2**2 - 2) & (delta - skoX >= -7541502747745674229011117699497985/288230376151711744) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (5471035039716212799*skoS2/10737418240 - skoSM*(126*skoS2 + 61)/40 + 5644718696065663041/21474836480 >= skoX*(21474836480*skoSM + skoX*(10942070079432425598*skoS2 - 536870912*skoSM*(126*skoS2 + 61) + 5644718696065663041) + 3473673126989004840)/21474836480)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(7541502747745674229011117699497985, 288230376151711744)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-7541502747745674229011117699497985, 288230376151711744)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), GreaterThan(Add(Mul(Rational(5471035039716212799, 10737418240), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(5644718696065663041, 21474836480)), Mul(Rational(1, 21474836480), Symbol('skoX'), Add(Mul(Integer(21474836480), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(10942070079432425598), Symbol('skoS2')), Mul(Integer(-1), Integer(536870912), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(5644718696065663041))), Integer(3473673126989004840)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_85(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 7541502747745674229011117699497985/288230376151711744) & (delta >= skoS2**2 - 2) & (delta - skoX >= -1058348875876581321604942186931023/1298074214633706907132624082305024) & (delta >= 2 - skoS2**2) & (367154945444116753122838023*skoS2/720575940379279360 + 378810658348060878275294613/1441151880758558720 >= 3*skoX*(skoX*(244769963629411168748558682*skoS2 + 126270219449353626091764871) + 77704752692960834349710600)/1441151880758558720)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(7541502747745674229011117699497985, 288230376151711744)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-1058348875876581321604942186931023, 1298074214633706907132624082305024)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Add(Mul(Rational(367154945444116753122838023, 720575940379279360), Symbol('skoS2')), Rational(378810658348060878275294613, 1441151880758558720)), Mul(Rational(3, 1441151880758558720), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(244769963629411168748558682), Symbol('skoS2')), Integer(126270219449353626091764871))), Integer(77704752692960834349710600)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_86(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 482656175855723157604057614947188905/18446744073709551616) & (delta >= skoS2**2 - 2) & (delta - skoX >= -482656175855723157604057614947188905/18446744073709551616) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (43768280317729702707*skoS2/85899345920 - skoSM*(126*skoS2 + 61)/40 + 45157749568525304653/171798691840 >= skoX*(171798691840*skoSM + skoX*(87536560635459405414*skoS2 - 4294967296*skoSM*(126*skoS2 + 61) + 45157749568525304653) + 27789385015912038920)/171798691840)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(482656175855723157604057614947188905, 18446744073709551616)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-482656175855723157604057614947188905, 18446744073709551616)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), GreaterThan(Add(Mul(Rational(43768280317729702707, 85899345920), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(45157749568525304653, 171798691840)), Mul(Rational(1, 171798691840), Symbol('skoX'), Add(Mul(Integer(171798691840), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(87536560635459405414), Symbol('skoS2')), Mul(Integer(-1), Integer(4294967296), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(45157749568525304653))), Integer(27789385015912038920)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_87(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 482656175855723157604057614947188905/18446744073709551616) & (delta >= skoS2**2 - 2) & (delta - skoX >= -317732007298024511225973736335615/324518553658426726783156020576256) & (delta >= 2 - skoS2**2) & (36715494609130731749166861*skoS2/72057594037927936 + 189405329487352855304856131/720575940379279360 >= skoX*(skoX*(367154946091307317491668610*skoS2 + 189405329487352855304856131) + 116557128833983931180436520)/720575940379279360)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(482656175855723157604057614947188905, 18446744073709551616)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-317732007298024511225973736335615, 324518553658426726783156020576256)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Add(Mul(Rational(36715494609130731749166861, 72057594037927936), Symbol('skoS2')), Rational(189405329487352855304856131, 720575940379279360)), Mul(Rational(1, 720575940379279360), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(367154946091307317491668610), Symbol('skoS2')), Integer(189405329487352855304856131))), Integer(116557128833983931180436520)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_88(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 30166010990982697263411774906957833/1152921504606846976) & (delta >= skoS2**2 - 2) & (delta - skoX >= -30166010990982697263411774906957833/1152921504606846976) & (delta >= skoSM**2 + skoX - 1) & (delta >= 2 - skoS2**2) & (delta >= -skoSM**2 - skoX + 1) & (10942070079432425661*skoS2/21474836480 - skoSM*(126*skoS2 + 61)/40 + 11289437392131326147/42949672960 >= skoX*(42949672960*skoSM + skoX*(21884140158864851322*skoS2 - 1073741824*skoSM*(126*skoS2 + 61) + 11289437392131326147) + 6947346253978009720)/42949672960)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(30166010990982697263411774906957833, 1152921504606846976)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-30166010990982697263411774906957833, 1152921504606846976)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1))), GreaterThan(Add(Mul(Rational(10942070079432425661, 21474836480), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(11289437392131326147, 42949672960)), Mul(Rational(1, 42949672960), Symbol('skoX'), Add(Mul(Integer(42949672960), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(21884140158864851322), Symbol('skoS2')), Mul(Integer(-1), Integer(1073741824), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(11289437392131326147))), Integer(6947346253978009720)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_89(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (delta + skoX >= 30166010990982697263411774906957833/1152921504606846976) & (delta >= skoS2**2 - 2) & (delta - skoX >= -81129298315621288386584942460783/81129638414606681695789005144064) & (delta >= 2 - skoS2**2) & (18357747320745129934100331*skoS2/36028797018963968 + 18940532964401406284848065/72057594037927936 >= 3*skoX*(skoX*(12238498213830086622733554*skoS2 + 6313510988133802094949355) + 3885237624375175671651560)/72057594037927936)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), GreaterThan(Add(Symbol('delta'), Symbol('skoX')), Rational(30166010990982697263411774906957833, 1152921504606846976)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2))), GreaterThan(Add(Symbol('delta'), Mul(Integer(-1), Symbol('skoX'))), Rational(-81129298315621288386584942460783, 81129638414606681695789005144064)), GreaterThan(Symbol('delta'), Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2))))), GreaterThan(Add(Mul(Rational(18357747320745129934100331, 36028797018963968), Symbol('skoS2')), Rational(18940532964401406284848065, 72057594037927936)), Mul(Rational(3, 72057594037927936), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(12238498213830086622733554), Symbol('skoS2')), Integer(6313510988133802094949355))), Integer(3885237624375175671651560)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def post_condition(delta:sympy.Rational, skoX:sympy.Rational, skoS2:sympy.Rational, skoSP:sympy.Rational, skoSM:sympy.Rational):
	# (0 <= delta) & (1 > skoX) & (skoS2 > 0) & (skoSM > 0) & (skoSP > 0) & (skoX > 0) & (skoS2**2 - 2 <= delta) & (skoSM**2 + skoX - 1 <= delta) & (2 - skoS2**2 <= delta) & (-skoSP**2 + skoX + 1 <= delta) & (skoSP**2 - skoX - 1 <= delta) & (-skoSM**2 - skoX + 1 <= delta) & (skoX*(skoSM + skoSP + skoX*(skoSM*(-63*skoS2/20 - 61/40) + skoSP*(63*skoS2/20 + 13/8) + 1/5) + 4) <= skoSM*(-63*skoS2/20 - 61/40) + skoSP*(63*skoS2/20 + 13/8) + 1/5)

	post_cond =  And(LessThan(Integer(0), Symbol('delta')), StrictGreaterThan(Integer(1), Symbol('skoX')), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoSP'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), LessThan(Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2)), Symbol('delta')), LessThan(Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1)), Symbol('delta')), LessThan(Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2)))), Symbol('delta')), LessThan(Add(Mul(Integer(-1), Pow(Symbol('skoSP'), Integer(2))), Symbol('skoX'), Integer(1)), Symbol('delta')), LessThan(Add(Pow(Symbol('skoSP'), Integer(2)), Mul(Integer(-1), Symbol('skoX')), Integer(-1)), Symbol('delta')), LessThan(Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1)), Symbol('delta')), LessThan(Mul(Symbol('skoX'), Add(Symbol('skoSM'), Symbol('skoSP'), Mul(Symbol('skoX'), Add(Mul(Symbol('skoSM'), Add(Mul(Integer(-1), Rational(63, 20), Symbol('skoS2')), Rational(-61, 40))), Mul(Symbol('skoSP'), Add(Mul(Rational(63, 20), Symbol('skoS2')), Rational(13, 8))), Rational(1, 5))), Integer(4))), Add(Mul(Symbol('skoSM'), Add(Mul(Integer(-1), Rational(63, 20), Symbol('skoS2')), Rational(-61, 40))), Mul(Symbol('skoSP'), Add(Mul(Rational(63, 20), Symbol('skoS2')), Rational(13, 8))), Rational(1, 5))))

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
		print('delta = 9')
		print('skoX = 1/2')
		print('skoS2 = 1')
		print('skoSM = 1')
		print('skoSP = 3')
		exit(0)
	
	
	if pre_condition_1(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_1 SAT")
		print('delta = 9')
		print('skoX = 1/2')
		print('skoS2 = 1')
		print('skoSM = 1')
		print('skoSP = 3')
		exit(0)
	
	
	if pre_condition_2(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_2 SAT")
		print('delta = 25')
		print('skoX = 1/2')
		print('skoS2 = 1/4')
		print('skoSM = 1')
		print('skoSP = 5')
		exit(0)
	
	
	if pre_condition_3(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_3 SAT")
		print('delta = 25')
		print('skoX = 1/2')
		print('skoS2 = 1/4')
		print('skoSM = 1')
		print('skoSP = 5')
		exit(0)
	
	
	if pre_condition_4(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_4 SAT")
		print('delta = 15')
		print('skoX = 1/2')
		print('skoS2 = 1/4')
		print('skoSM = 1')
		print('skoSP = 4')
		exit(0)
	
	
	if pre_condition_5(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_5 SAT")
		print('delta = 15')
		print('skoX = 1/2')
		print('skoS2 = 1/4')
		print('skoSM = 1')
		print('skoSP = 4')
		exit(0)
	
	
	if pre_condition_6(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_6 SAT")
		print('delta = 23')
		print('skoX = 3/4')
		print('skoS2 = 1/2')
		print('skoSM = 1/8')
		print('skoSP = 79/16')
		exit(0)
	
	
	if pre_condition_7(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_7 SAT")
		print('delta = 23')
		print('skoX = 3/4')
		print('skoS2 = 1/2')
		print('skoSM = 1/8')
		print('skoSP = 79/16')
		exit(0)
	
	
	if pre_condition_8(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_8 SAT")
		print('delta = 289')
		print('skoX = 3/4')
		print('skoS2 = 1/4')
		print('skoSM = 1')
		print('skoSP = 17')
		exit(0)
	
	
	if pre_condition_9(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_9 SAT")
		print('delta = 289')
		print('skoX = 3/4')
		print('skoS2 = 1/4')
		print('skoSM = 1')
		print('skoSP = 17')
		exit(0)
	
	
	if pre_condition_10(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_10 SAT")
		print('delta = 255')
		print('skoX = 3/4')
		print('skoS2 = 1/4')
		print('skoSM = 1')
		print('skoSP = 16')
		exit(0)
	
	
	if pre_condition_11(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_11 SAT")
		print('delta = 255')
		print('skoX = 3/4')
		print('skoS2 = 1/4')
		print('skoSM = 1')
		print('skoSP = 16')
		exit(0)
	
	
	if pre_condition_12(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_12 SAT")
		print('delta = 271')
		print('skoX = 3/4')
		print('skoS2 = 3/16')
		print('skoSM = 3/8')
		print('skoSP = 33/2')
		exit(0)
	
	
	if pre_condition_13(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_13 SAT")
		print('delta = 271')
		print('skoX = 3/4')
		print('skoS2 = 3/16')
		print('skoSM = 3/8')
		print('skoSP = 33/2')
		exit(0)
	
	
	if pre_condition_14(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_14 SAT")
		print('delta = 267')
		print('skoX = 3/4')
		print('skoS2 = 11/64')
		print('skoSM = 3/16')
		print('skoSP = 131/8')
		exit(0)
	
	
	if pre_condition_15(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_15 SAT")
		print('delta = 267')
		print('skoX = 3/4')
		print('skoS2 = 11/64')
		print('skoSM = 3/16')
		print('skoSP = 131/8')
		exit(0)
	
	
	if pre_condition_16(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_16 SAT")
		print('delta = 263')
		print('skoX = 3/4')
		print('skoS2 = 3/16')
		print('skoSM = 3/8')
		print('skoSP = 65/4')
		exit(0)
	
	
	if pre_condition_17(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_17 SAT")
		print('delta = 263')
		print('skoX = 3/4')
		print('skoS2 = 3/16')
		print('skoSM = 3/8')
		print('skoSP = 65/4')
		exit(0)
	
	
	if pre_condition_18(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_18 SAT")
		print('delta = 265')
		print('skoX = 3/4')
		print('skoS2 = 11/64')
		print('skoSM = 3/16')
		print('skoSP = 261/16')
		exit(0)
	
	
	if pre_condition_19(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_19 SAT")
		print('delta = 265')
		print('skoX = 3/4')
		print('skoS2 = 11/64')
		print('skoSM = 3/16')
		print('skoSP = 261/16')
		exit(0)
	
	
	if pre_condition_20(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_20 SAT")
		print('delta = 264')
		print('skoX = 3/4')
		print('skoS2 = 11/64')
		print('skoSM = 3/16')
		print('skoSP = 1043/64')
		exit(0)
	
	
	if pre_condition_21(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_21 SAT")
		print('delta = 264')
		print('skoX = 3/4')
		print('skoS2 = 11/64')
		print('skoSM = 3/16')
		print('skoSP = 1043/64')
		exit(0)
	
	
	if pre_condition_22(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_22 SAT")
		print('delta = 266')
		print('skoX = 3/4')
		print('skoS2 = 21/128')
		print('skoSM = 11/128')
		print('skoSP = 523/32')
		exit(0)
	
	
	if pre_condition_23(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_23 SAT")
		print('delta = 266')
		print('skoX = 3/4')
		print('skoS2 = 21/128')
		print('skoSM = 11/128')
		print('skoSP = 523/32')
		exit(0)
	
	
	if pre_condition_24(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_24 SAT")
		print('delta = 1225')
		print('skoX = 3/4')
		print('skoS2 = 1/8')
		print('skoSM = 1')
		print('skoSP = 35')
		exit(0)
	
	
	if pre_condition_25(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_25 SAT")
		print('delta = 1225')
		print('skoX = 3/4')
		print('skoS2 = 1/8')
		print('skoSM = 1')
		print('skoSP = 35')
		exit(0)
	
	
	if pre_condition_26(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_26 SAT")
		print('delta = 284')
		print('skoX = 3/4')
		print('skoS2 = 5/32')
		print('skoSM = 1/32')
		print('skoSP = 135/8')
		exit(0)
	
	
	if pre_condition_27(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_27 SAT")
		print('delta = 284')
		print('skoX = 3/4')
		print('skoS2 = 5/32')
		print('skoSM = 1/32')
		print('skoSP = 135/8')
		exit(0)
	
	
	if pre_condition_28(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_28 SAT")
		print('delta = 9025')
		print('skoX = 3/4')
		print('skoS2 = 1/16')
		print('skoSM = 1')
		print('skoSP = 95')
		exit(0)
	
	
	if pre_condition_29(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_29 SAT")
		print('delta = 9025')
		print('skoX = 3/4')
		print('skoS2 = 1/16')
		print('skoSM = 1')
		print('skoSP = 95')
		exit(0)
	
	
	if pre_condition_30(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_30 SAT")
		print('delta = 1196836')
		print('skoX = 3/4')
		print('skoS2 = 1/32')
		print('skoSM = 1')
		print('skoSP = 1094')
		exit(0)
	
	
	if pre_condition_31(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_31 SAT")
		print('delta = 1196836')
		print('skoX = 3/4')
		print('skoS2 = 1/32')
		print('skoSM = 1')
		print('skoSP = 1094')
		exit(0)
	
	
	if pre_condition_32(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_32 SAT")
		print('delta = 1194648')
		print('skoX = 3/4')
		print('skoS2 = 1/32')
		print('skoSM = 1')
		print('skoSP = 1093')
		exit(0)
	
	
	if pre_condition_33(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_33 SAT")
		print('delta = 1194648')
		print('skoX = 3/4')
		print('skoS2 = 1/32')
		print('skoSM = 1')
		print('skoSP = 1093')
		exit(0)
	
	
	if pre_condition_34(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_34 SAT")
		print('delta = 1193555')
		print('skoX = 3/4')
		print('skoS2 = 1/32')
		print('skoSM = 1')
		print('skoSP = 2185/2')
		exit(0)
	
	
	if pre_condition_35(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_35 SAT")
		print('delta = 1193555')
		print('skoX = 3/4')
		print('skoS2 = 1/32')
		print('skoSM = 1')
		print('skoSP = 2185/2')
		exit(0)
	
	
	if pre_condition_36(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_36 SAT")
		print('delta = 11102224')
		print('skoX = 3/4')
		print('skoS2 = 15/512')
		print('skoSM = 1')
		print('skoSP = 3332')
		exit(0)
	
	
	if pre_condition_37(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_37 SAT")
		print('delta = 11102224')
		print('skoX = 3/4')
		print('skoS2 = 15/512')
		print('skoSM = 1')
		print('skoSP = 3332')
		exit(0)
	
	
	if pre_condition_38(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_38 SAT")
		print('delta = 46730896')
		print('skoX = 3/4')
		print('skoS2 = 59/2048')
		print('skoSM = 1')
		print('skoSP = 6836')
		exit(0)
	
	
	if pre_condition_39(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_39 SAT")
		print('delta = 46730896')
		print('skoX = 3/4')
		print('skoS2 = 59/2048')
		print('skoSM = 1')
		print('skoSP = 6836')
		exit(0)
	
	
	if pre_condition_40(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_40 SAT")
		print('delta = 208109476')
		print('skoX = 3/4')
		print('skoS2 = 117/4096')
		print('skoSM = 1')
		print('skoSP = 14426')
		exit(0)
	
	
	if pre_condition_41(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_41 SAT")
		print('delta = 208109476')
		print('skoX = 3/4')
		print('skoS2 = 117/4096')
		print('skoSM = 1')
		print('skoSP = 14426')
		exit(0)
	
	
	if pre_condition_42(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_42 SAT")
		print('delta = 208080624')
		print('skoX = 3/4')
		print('skoS2 = 117/4096')
		print('skoSM = 1')
		print('skoSP = 14425')
		exit(0)
	
	
	if pre_condition_43(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_43 SAT")
		print('delta = 208080624')
		print('skoX = 3/4')
		print('skoS2 = 117/4096')
		print('skoSM = 1')
		print('skoSP = 14425')
		exit(0)
	
	
	if pre_condition_44(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_44 SAT")
		print('delta = 1052742916')
		print('skoX = 3/4')
		print('skoS2 = 233/8192')
		print('skoSM = 1')
		print('skoSP = 32446')
		exit(0)
	
	
	if pre_condition_45(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_45 SAT")
		print('delta = 1052742916')
		print('skoX = 3/4')
		print('skoS2 = 233/8192')
		print('skoSM = 1')
		print('skoSP = 32446')
		exit(0)
	
	
	if pre_condition_46(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_46 SAT")
		print('delta = 1052029224')
		print('skoX = 3/4')
		print('skoS2 = 931/32768')
		print('skoSM = 1/16')
		print('skoSP = 32435')
		exit(0)
	
	
	if pre_condition_47(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_47 SAT")
		print('delta = 1052029224')
		print('skoX = 3/4')
		print('skoS2 = 931/32768')
		print('skoSM = 1/16')
		print('skoSP = 32435')
		exit(0)
	
	
	if pre_condition_48(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_48 SAT")
		print('delta = 7471182096')
		print('skoX = 3/4')
		print('skoS2 = 465/16384')
		print('skoSM = 1')
		print('skoSP = 86436')
		exit(0)
	
	
	if pre_condition_49(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_49 SAT")
		print('delta = 7471182096')
		print('skoX = 3/4')
		print('skoS2 = 465/16384')
		print('skoSM = 1')
		print('skoSP = 86436')
		exit(0)
	
	
	if pre_condition_50(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_50 SAT")
		print('delta = 264934619524')
		print('skoX = 3/4')
		print('skoS2 = 929/32768')
		print('skoSM = 1')
		print('skoSP = 514718')
		exit(0)
	
	
	if pre_condition_51(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_51 SAT")
		print('delta = 264934619524')
		print('skoX = 3/4')
		print('skoS2 = 929/32768')
		print('skoSM = 1')
		print('skoSP = 514718')
		exit(0)
	
	
	if pre_condition_52(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_52 SAT")
		print('delta = 1828761268489')
		print('skoX = 3/4')
		print('skoS2 = 7431/262144')
		print('skoSM = 1')
		print('skoSP = 1352317')
		exit(0)
	
	
	if pre_condition_53(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_53 SAT")
		print('delta = 1828761268489')
		print('skoX = 3/4')
		print('skoS2 = 7431/262144')
		print('skoSM = 1')
		print('skoSP = 1352317')
		exit(0)
	
	
	if pre_condition_54(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_54 SAT")
		print('delta = 1621109539983')
		print('skoX = 3/4')
		print('skoS2 = 59447/2097152')
		print('skoSM = 1/4')
		print('skoSP = 1273228')
		exit(0)
	
	
	if pre_condition_55(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_55 SAT")
		print('delta = 1621109539983')
		print('skoX = 3/4')
		print('skoS2 = 59447/2097152')
		print('skoSM = 1/4')
		print('skoSP = 1273228')
		exit(0)
	
	
	if pre_condition_56(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_56 SAT")
		print('delta = 1554298291224')
		print('skoX = 3/4')
		print('skoS2 = 237787/8388608')
		print('skoSM = 1/16')
		print('skoSP = 1246715')
		exit(0)
	
	
	if pre_condition_57(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_57 SAT")
		print('delta = 1554298291224')
		print('skoX = 3/4')
		print('skoS2 = 237787/8388608')
		print('skoSM = 1/16')
		print('skoSP = 1246715')
		exit(0)
	
	
	if pre_condition_58(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_58 SAT")
		print('delta = 1554297044509')
		print('skoX = 3/4')
		print('skoS2 = 237787/8388608')
		print('skoSM = 1/16')
		print('skoSP = 2493429/2')
		exit(0)
	
	
	if pre_condition_59(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_59 SAT")
		print('delta = 1554297044509')
		print('skoX = 3/4')
		print('skoS2 = 237787/8388608')
		print('skoSM = 1/16')
		print('skoSP = 2493429/2')
		exit(0)
	
	
	if pre_condition_60(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_60 SAT")
		print('delta = 1269971224899')
		print('skoX = 3/4')
		print('skoS2 = 7431/262144')
		print('skoSM = 1/2')
		print('skoSP = 1126930')
		exit(0)
	
	
	if pre_condition_61(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_61 SAT")
		print('delta = 1269971224899')
		print('skoX = 3/4')
		print('skoS2 = 7431/262144')
		print('skoSM = 1/2')
		print('skoSP = 1126930')
		exit(0)
	
	
	if pre_condition_62(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_62 SAT")
		print('delta = 1615865541888')
		print('skoX = 3/4')
		print('skoS2 = 475573/16777216')
		print('skoSM = 1/32')
		print('skoSP = 1271167')
		exit(0)
	
	
	if pre_condition_63(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_63 SAT")
		print('delta = 1615865541888')
		print('skoX = 3/4')
		print('skoS2 = 475573/16777216')
		print('skoSM = 1/32')
		print('skoSP = 1271167')
		exit(0)
	
	
	if pre_condition_64(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_64 SAT")
		print('delta = 1536389998143')
		print('skoX = 3/4')
		print('skoS2 = 951147/33554432')
		print('skoSM = 1/64')
		print('skoSP = 1239512')
		exit(0)
	
	
	if pre_condition_65(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_65 SAT")
		print('delta = 1536389998143')
		print('skoX = 3/4')
		print('skoS2 = 951147/33554432')
		print('skoSM = 1/64')
		print('skoSP = 1239512')
		exit(0)
	
	
	if pre_condition_66(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_66 SAT")
		print('delta = 1536388758631')
		print('skoX = 3/4')
		print('skoS2 = 951147/33554432')
		print('skoSM = 1/64')
		print('skoSP = 2479023/2')
		exit(0)
	
	
	if pre_condition_67(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_67 SAT")
		print('delta = 1536388758631')
		print('skoX = 3/4')
		print('skoS2 = 951147/33554432')
		print('skoSM = 1/64')
		print('skoSP = 2479023/2')
		exit(0)
	
	
	if pre_condition_68(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_68 SAT")
		print('delta = 1790118230208')
		print('skoX = 3/4')
		print('skoS2 = 118893/4194304')
		print('skoSM = 1/16')
		print('skoSP = 1337953')
		exit(0)
	
	
	if pre_condition_69(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_69 SAT")
		print('delta = 1790118230208')
		print('skoX = 3/4')
		print('skoS2 = 118893/4194304')
		print('skoSM = 1/16')
		print('skoSP = 1337953')
		exit(0)
	
	
	if pre_condition_70(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_70 SAT")
		print('delta = 52663744206441')
		print('skoX = 3/4')
		print('skoS2 = 14861/524288')
		print('skoSM = 1')
		print('skoSP = 7256979')
		exit(0)
	
	
	if pre_condition_71(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_71 SAT")
		print('delta = 52663744206441')
		print('skoX = 3/4')
		print('skoS2 = 14861/524288')
		print('skoSM = 1')
		print('skoSP = 7256979')
		exit(0)
	
	
	if pre_condition_72(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_72 SAT")
		print('delta = 1773992239568')
		print('skoX = 3/4')
		print('skoS2 = 951143/33554432')
		print('skoSM = 1/64')
		print('skoSP = 1331913')
		exit(0)
	
	
	if pre_condition_73(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_73 SAT")
		print('delta = 1773992239568')
		print('skoX = 3/4')
		print('skoS2 = 951143/33554432')
		print('skoSM = 1/64')
		print('skoSP = 1331913')
		exit(0)
	
	
	if pre_condition_74(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_74 SAT")
		print('delta = 255271399156225')
		print('skoX = 3/4')
		print('skoS2 = 118887/4194304')
		print('skoSM = 1')
		print('skoSP = 15977215')
		exit(0)
	
	
	if pre_condition_75(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_75 SAT")
		print('delta = 255271399156225')
		print('skoX = 3/4')
		print('skoS2 = 118887/4194304')
		print('skoSM = 1')
		print('skoSP = 15977215')
		exit(0)
	
	
	if pre_condition_76(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_76 SAT")
		print('delta = 1601986856429584')
		print('skoX = 3/4')
		print('skoS2 = 237773/8388608')
		print('skoSM = 1')
		print('skoSP = 40024828')
		exit(0)
	
	
	if pre_condition_77(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_77 SAT")
		print('delta = 1601986856429584')
		print('skoX = 3/4')
		print('skoS2 = 237773/8388608')
		print('skoSM = 1')
		print('skoSP = 40024828')
		exit(0)
	
	
	if pre_condition_78(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_78 SAT")
		print('delta = 26164843721316036')
		print('skoX = 3/4')
		print('skoS2 = 475545/16777216')
		print('skoSM = 1')
		print('skoSP = 161755506')
		exit(0)
	
	
	if pre_condition_79(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_79 SAT")
		print('delta = 26164843721316036')
		print('skoX = 3/4')
		print('skoS2 = 475545/16777216')
		print('skoSM = 1')
		print('skoSP = 161755506')
		exit(0)
	
	
	if pre_condition_80(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_80 SAT")
		print('delta = 255271367201795')
		print('skoX = 3/4')
		print('skoS2 = 118887/4194304')
		print('skoSM = 1')
		print('skoSP = 15977214')
		exit(0)
	
	
	if pre_condition_81(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_81 SAT")
		print('delta = 255271367201795')
		print('skoX = 3/4')
		print('skoS2 = 118887/4194304')
		print('skoSM = 1')
		print('skoSP = 15977214')
		exit(0)
	
	
	if pre_condition_82(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_82 SAT")
		print('delta = 1367159203213455')
		print('skoX = 3/4')
		print('skoS2 = 1902183/67108864')
		print('skoSM = 1/4')
		print('skoSP = 36975116')
		exit(0)
	
	
	if pre_condition_83(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_83 SAT")
		print('delta = 1367159203213455')
		print('skoX = 3/4')
		print('skoS2 = 1902183/67108864')
		print('skoSM = 1/4')
		print('skoSP = 36975116')
		exit(0)
	
	
	if pre_condition_84(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_84 SAT")
		print('delta = 209318749770528281/8')
		print('skoX = 3/4')
		print('skoS2 = 7608719/268435456')
		print('skoSM = 15483066193655751/36028797018963968')
		print('skoSP = 86841826027241473/536870912')
		exit(0)
	
	
	if pre_condition_85(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_85 SAT")
		print('delta = 209318749770528281/8')
		print('skoX = 3/4')
		print('skoS2 = 7608719/268435456')
		print('skoSM = 15483066193655751/36028797018963968')
		print('skoSP = 86841826027241473/536870912')
		exit(0)
	
	
	if pre_condition_86(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_86 SAT")
		print('delta = 1674549998164226255/64')
		print('skoX = 3/4')
		print('skoS2 = 15217437/536870912')
		print('skoSM = 2605100067253121/18014398509481984')
		print('skoSP = 694734608217931789/4294967296')
		exit(0)
	
	
	if pre_condition_87(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_87 SAT")
		print('delta = 1674549998164226255/64')
		print('skoX = 3/4')
		print('skoS2 = 15217437/536870912')
		print('skoSM = 2605100067253121/18014398509481984')
		print('skoSP = 694734608217931789/4294967296')
		exit(0)
	
	
	if pre_condition_88(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_88 SAT")
		print('delta = 418637499541056563/16')
		print('skoX = 3/4')
		print('skoS2 = 30434873/1073741824')
		print('skoSM = 18441772837591/9007199254740992')
		print('skoSP = 173683652054482947/1073741824')
		exit(0)
	
	
	if pre_condition_89(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_89 SAT")
		print('delta = 418637499541056563/16')
		print('skoX = 3/4')
		print('skoS2 = 30434873/1073741824')
		print('skoSM = 18441772837591/9007199254740992')
		print('skoSP = 173683652054482947/1073741824')
		exit(0)


	print("UNKNOWN")
	exit(0)
