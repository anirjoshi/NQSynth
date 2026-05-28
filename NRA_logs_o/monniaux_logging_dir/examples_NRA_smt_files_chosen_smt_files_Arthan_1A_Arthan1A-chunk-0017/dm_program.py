import sympy
from sympy import *

def pre_condition_0(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (skoS >= skoSINS) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & (skoS*(8*skoS*(8*skoS + 27) + 41)/32 - 55/32 <= -skoSINS*(4*skoS*(skoS*(skoS + 2) - 4) + 4*skoSINS*(skoS + 1) - 13)/4)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), GreaterThan(Symbol('skoS'), Symbol('skoSINS')), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), LessThan(Add(Mul(Rational(1, 32), Symbol('skoS'), Add(Mul(Integer(8), Symbol('skoS'), Add(Mul(Integer(8), Symbol('skoS')), Integer(27))), Integer(41))), Rational(-55, 32)), Mul(Integer(-1), Rational(1, 4), Symbol('skoSINS'), Add(Mul(Integer(4), Symbol('skoS'), Add(Mul(Symbol('skoS'), Add(Symbol('skoS'), Integer(2))), Integer(-4))), Mul(Integer(4), Symbol('skoSINS'), Add(Symbol('skoS'), Integer(1))), Integer(-13)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & (64*skoS**3 + 216*skoS**2 + 41*skoS <= 55)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), LessThan(Add(Mul(Integer(64), Pow(Symbol('skoS'), Integer(3))), Mul(Integer(216), Pow(Symbol('skoS'), Integer(2))), Mul(Integer(41), Symbol('skoS'))), Integer(55)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_2(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (skoS >= skoSINS) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & (skoS*(64*skoS*(64*skoS + 195) + 321)/2048 - 4031/2048 <= -skoSINS*(32*skoS*(skoS*(skoS + 2) - 4) + 32*skoSINS*(skoS + 1) - 97)/32)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), GreaterThan(Symbol('skoS'), Symbol('skoSINS')), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), LessThan(Add(Mul(Rational(1, 2048), Symbol('skoS'), Add(Mul(Integer(64), Symbol('skoS'), Add(Mul(Integer(64), Symbol('skoS')), Integer(195))), Integer(321))), Rational(-4031, 2048)), Mul(Integer(-1), Rational(1, 32), Symbol('skoSINS'), Add(Mul(Integer(32), Symbol('skoS'), Add(Mul(Symbol('skoS'), Add(Symbol('skoS'), Integer(2))), Integer(-4))), Mul(Integer(32), Symbol('skoSINS'), Add(Symbol('skoS'), Integer(1))), Integer(-97)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_3(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & (4096*skoS**3 + 12480*skoS**2 + 321*skoS <= 4031)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), LessThan(Add(Mul(Integer(4096), Pow(Symbol('skoS'), Integer(3))), Mul(Integer(12480), Pow(Symbol('skoS'), Integer(2))), Mul(Integer(321), Symbol('skoS'))), Integer(4031)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_4(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (skoS >= skoSINS) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & (skoS*(2048*skoS*(2048*skoS + 6147) + 10241)/2097152 - 4192255/2097152 <= -skoSINS*(1024*skoS*(skoS*(skoS + 2) - 4) + 1024*skoSINS*(skoS + 1) - 3073)/1024)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), GreaterThan(Symbol('skoS'), Symbol('skoSINS')), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), LessThan(Add(Mul(Rational(1, 2097152), Symbol('skoS'), Add(Mul(Integer(2048), Symbol('skoS'), Add(Mul(Integer(2048), Symbol('skoS')), Integer(6147))), Integer(10241))), Rational(-4192255, 2097152)), Mul(Integer(-1), Rational(1, 1024), Symbol('skoSINS'), Add(Mul(Integer(1024), Symbol('skoS'), Add(Mul(Symbol('skoS'), Add(Symbol('skoS'), Integer(2))), Integer(-4))), Mul(Integer(1024), Symbol('skoSINS'), Add(Symbol('skoS'), Integer(1))), Integer(-3073)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_5(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & (4194304*skoS**3 + 12589056*skoS**2 + 10241*skoS <= 4192255)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), LessThan(Add(Mul(Integer(4194304), Pow(Symbol('skoS'), Integer(3))), Mul(Integer(12589056), Pow(Symbol('skoS'), Integer(2))), Mul(Integer(10241), Symbol('skoS'))), Integer(4192255)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_6(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (skoS >= skoSINS) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & (skoS*(4096*skoS*(4096*skoS + 12291) + 20481)/8388608 - 16773119/8388608 <= -skoSINS*(2048*skoS*(skoS*(skoS + 2) - 4) + 2048*skoSINS*(skoS + 1) - 6145)/2048)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), GreaterThan(Symbol('skoS'), Symbol('skoSINS')), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), LessThan(Add(Mul(Rational(1, 8388608), Symbol('skoS'), Add(Mul(Integer(4096), Symbol('skoS'), Add(Mul(Integer(4096), Symbol('skoS')), Integer(12291))), Integer(20481))), Rational(-16773119, 8388608)), Mul(Integer(-1), Rational(1, 2048), Symbol('skoSINS'), Add(Mul(Integer(2048), Symbol('skoS'), Add(Mul(Symbol('skoS'), Add(Symbol('skoS'), Integer(2))), Integer(-4))), Mul(Integer(2048), Symbol('skoSINS'), Add(Symbol('skoS'), Integer(1))), Integer(-6145)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_7(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & (16777216*skoS**3 + 50343936*skoS**2 + 20481*skoS <= 16773119)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), LessThan(Add(Mul(Integer(16777216), Pow(Symbol('skoS'), Integer(3))), Mul(Integer(50343936), Pow(Symbol('skoS'), Integer(2))), Mul(Integer(20481), Symbol('skoS'))), Integer(16773119)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_8(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (skoS >= skoSINS) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & (skoS*(8192*skoS*(8192*skoS + 24579) + 40961)/33554432 - 67100671/33554432 <= -skoSINS*(4096*skoS*(skoS*(skoS + 2) - 4) + 4096*skoSINS*(skoS + 1) - 12289)/4096)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), GreaterThan(Symbol('skoS'), Symbol('skoSINS')), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), LessThan(Add(Mul(Rational(1, 33554432), Symbol('skoS'), Add(Mul(Integer(8192), Symbol('skoS'), Add(Mul(Integer(8192), Symbol('skoS')), Integer(24579))), Integer(40961))), Rational(-67100671, 33554432)), Mul(Integer(-1), Rational(1, 4096), Symbol('skoSINS'), Add(Mul(Integer(4096), Symbol('skoS'), Add(Mul(Symbol('skoS'), Add(Symbol('skoS'), Integer(2))), Integer(-4))), Mul(Integer(4096), Symbol('skoSINS'), Add(Symbol('skoS'), Integer(1))), Integer(-12289)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_9(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 697/1024) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & (17989632*skoS**3 + 49405952*skoS**2 - 15154067*skoS <= 120078247/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(697, 1024)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), LessThan(Add(Mul(Integer(17989632), Pow(Symbol('skoS'), Integer(3))), Mul(Integer(49405952), Pow(Symbol('skoS'), Integer(2))), Mul(Integer(-1), Integer(15154067), Symbol('skoS'))), Rational(120078247, 5)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_10(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (skoS >= skoSINS) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & (skoS*(32768*skoS*(32768*skoS + 98307) + 163841)/536870912 - 1073709055/536870912 <= -skoSINS*(16384*skoS*(skoS*(skoS + 2) - 4) + 16384*skoSINS*(skoS + 1) - 49153)/16384)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), GreaterThan(Symbol('skoS'), Symbol('skoSINS')), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), LessThan(Add(Mul(Rational(1, 536870912), Symbol('skoS'), Add(Mul(Integer(32768), Symbol('skoS'), Add(Mul(Integer(32768), Symbol('skoS')), Integer(98307))), Integer(163841))), Rational(-1073709055, 536870912)), Mul(Integer(-1), Rational(1, 16384), Symbol('skoSINS'), Add(Mul(Integer(16384), Symbol('skoS'), Add(Mul(Symbol('skoS'), Add(Symbol('skoS'), Integer(2))), Integer(-4))), Mul(Integer(16384), Symbol('skoSINS'), Add(Symbol('skoS'), Integer(1))), Integer(-49153)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_11(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 411/2048) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & (1181483008*skoS**3 + 3436806144*skoS**2 - 409179007*skoS <= 1375317295)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(411, 2048)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), LessThan(Add(Mul(Integer(1181483008), Pow(Symbol('skoS'), Integer(3))), Mul(Integer(3436806144), Pow(Symbol('skoS'), Integer(2))), Mul(Integer(-1), Integer(409179007), Symbol('skoS'))), Integer(1375317295)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_12(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (skoS >= skoSINS) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & (skoS*(65536*skoS*(65536*skoS + 196611) + 327681)/2147483648 - 4294901759/2147483648 <= -skoSINS*(32768*skoS*(skoS*(skoS + 2) - 4) + 32768*skoSINS*(skoS + 1) - 98305)/32768)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), GreaterThan(Symbol('skoS'), Symbol('skoSINS')), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), LessThan(Add(Mul(Rational(1, 2147483648), Symbol('skoS'), Add(Mul(Integer(65536), Symbol('skoS'), Add(Mul(Integer(65536), Symbol('skoS')), Integer(196611))), Integer(327681))), Rational(-4294901759, 2147483648)), Mul(Integer(-1), Rational(1, 32768), Symbol('skoSINS'), Add(Mul(Integer(32768), Symbol('skoS'), Add(Mul(Symbol('skoS'), Add(Symbol('skoS'), Integer(2))), Integer(-4))), Mul(Integer(32768), Symbol('skoSINS'), Add(Symbol('skoS'), Integer(1))), Integer(-98305)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_13(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 751/1024) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & (5869928448*skoS**3 + 16035020800*skoS**2 - 5144442879*skoS <= 7864759231)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(751, 1024)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), LessThan(Add(Mul(Integer(5869928448), Pow(Symbol('skoS'), Integer(3))), Mul(Integer(16035020800), Pow(Symbol('skoS'), Integer(2))), Mul(Integer(-1), Integer(5144442879), Symbol('skoS'))), Integer(7864759231)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_14(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (skoS >= skoSINS) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & (skoS*(131072*skoS*(131072*skoS + 393219) + 655361)/8589934592 - 17179738111/8589934592 <= -skoSINS*(65536*skoS*(skoS*(skoS + 2) - 4) + 65536*skoSINS*(skoS + 1) - 196609)/65536)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), GreaterThan(Symbol('skoS'), Symbol('skoSINS')), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), LessThan(Add(Mul(Rational(1, 8589934592), Symbol('skoS'), Add(Mul(Integer(131072), Symbol('skoS'), Add(Mul(Integer(131072), Symbol('skoS')), Integer(393219))), Integer(655361))), Rational(-17179738111, 8589934592)), Mul(Integer(-1), Rational(1, 65536), Symbol('skoSINS'), Add(Mul(Integer(65536), Symbol('skoS'), Add(Mul(Symbol('skoS'), Add(Symbol('skoS'), Integer(2))), Integer(-4))), Mul(Integer(65536), Symbol('skoSINS'), Add(Symbol('skoS'), Integer(1))), Integer(-196609)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_15(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 4701/16384) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & (19644547072*skoS**3 + 56469356544*skoS**2 - 9150875359*skoS <= 23866628551)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(4701, 16384)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), LessThan(Add(Mul(Integer(19644547072), Pow(Symbol('skoS'), Integer(3))), Mul(Integer(56469356544), Pow(Symbol('skoS'), Integer(2))), Mul(Integer(-1), Integer(9150875359), Symbol('skoS'))), Integer(23866628551)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_16(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (skoS >= skoSINS) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & (skoS*(262144*skoS*(262144*skoS + 786435) + 1310721)/34359738368 - 68719214591/34359738368 <= -skoSINS*(131072*skoS*(skoS*(skoS + 2) - 4) + 131072*skoSINS*(skoS + 1) - 393217)/131072)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), GreaterThan(Symbol('skoS'), Symbol('skoSINS')), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), LessThan(Add(Mul(Rational(1, 34359738368), Symbol('skoS'), Add(Mul(Integer(262144), Symbol('skoS'), Add(Mul(Integer(262144), Symbol('skoS')), Integer(786435))), Integer(1310721))), Rational(-68719214591, 34359738368)), Mul(Integer(-1), Rational(1, 131072), Symbol('skoSINS'), Add(Mul(Integer(131072), Symbol('skoS'), Add(Mul(Symbol('skoS'), Add(Symbol('skoS'), Integer(2))), Integer(-4))), Mul(Integer(131072), Symbol('skoSINS'), Add(Symbol('skoS'), Integer(1))), Integer(-393217)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_17(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 687/2048) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & (80245424128*skoS**3 + 229211111424*skoS**2 - 42236108799*skoS <= 99430774655)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(687, 2048)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), LessThan(Add(Mul(Integer(80245424128), Pow(Symbol('skoS'), Integer(3))), Mul(Integer(229211111424), Pow(Symbol('skoS'), Integer(2))), Mul(Integer(-1), Integer(42236108799), Symbol('skoS'))), Integer(99430774655)))

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
		print('skoCOSS = 1/8')
		print('skoS = 1/16')
		print('skoSINS = 0')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_1(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_1 SAT")
		print('delta = 0')
		print('skoCOSS = 1/8')
		print('skoS = 1/16')
		print('skoSINS = 0')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_2(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_2 SAT")
		print('delta = 0')
		print('skoCOSS = 1/64')
		print('skoS = 1/2')
		print('skoSINS = 0')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_3(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_3 SAT")
		print('delta = 0')
		print('skoCOSS = 1/64')
		print('skoS = 1/2')
		print('skoSINS = 0')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_4(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_4 SAT")
		print('delta = 0')
		print('skoCOSS = 1/2048')
		print('skoS = 17/32')
		print('skoSINS = 0')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_5(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_5 SAT")
		print('delta = 0')
		print('skoCOSS = 1/2048')
		print('skoS = 17/32')
		print('skoSINS = 0')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_6(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_6 SAT")
		print('delta = 0')
		print('skoCOSS = 1/4096')
		print('skoS = 1089/2048')
		print('skoSINS = 0')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_7(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_7 SAT")
		print('delta = 0')
		print('skoCOSS = 1/4096')
		print('skoS = 1089/2048')
		print('skoSINS = 0')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_8(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_8 SAT")
		print('delta = 0')
		print('skoCOSS = 1/8192')
		print('skoS = 3/4')
		print('skoSINS = 697/1024')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_9(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_9 SAT")
		print('delta = 0')
		print('skoCOSS = 1/8192')
		print('skoS = 3/4')
		print('skoSINS = 697/1024')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_10(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_10 SAT")
		print('delta = 0')
		print('skoCOSS = 1/32768')
		print('skoS = 5/8')
		print('skoSINS = 411/2048')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_11(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_11 SAT")
		print('delta = 0')
		print('skoCOSS = 1/32768')
		print('skoS = 5/8')
		print('skoSINS = 411/2048')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_12(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_12 SAT")
		print('delta = 0')
		print('skoCOSS = 1/65536')
		print('skoS = 97/128')
		print('skoSINS = 751/1024')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_13(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_13 SAT")
		print('delta = 0')
		print('skoCOSS = 1/65536')
		print('skoS = 97/128')
		print('skoSINS = 751/1024')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_14(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_14 SAT")
		print('delta = 0')
		print('skoCOSS = 1/131072')
		print('skoS = 21/32')
		print('skoSINS = 4701/16384')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_15(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_15 SAT")
		print('delta = 0')
		print('skoCOSS = 1/131072')
		print('skoS = 21/32')
		print('skoSINS = 4701/16384')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_16(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_16 SAT")
		print('delta = 0')
		print('skoCOSS = 1/262144')
		print('skoS = 43/64')
		print('skoSINS = 687/2048')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_17(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_17 SAT")
		print('delta = 0')
		print('skoCOSS = 1/262144')
		print('skoS = 43/64')
		print('skoSINS = 687/2048')
		print('pi = 26353589/8388608')
		exit(0)


	print("UNKNOWN")
	exit(0)
