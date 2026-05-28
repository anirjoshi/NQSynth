import sympy
from sympy import *

def pre_condition_0(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 63/64) & (delta >= 63/64 - skoSINS**2) & (skoS*(8*skoS*(8*skoS + 27) + 41)/32 - 55/32 <= -skoSINS*(4*skoS*(skoS*(skoS + 2) - 4) + 4*skoSINS*(skoS + 1) - 13)/4)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-63, 64))), GreaterThan(Symbol('delta'), Add(Rational(63, 64), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), LessThan(Add(Mul(Rational(1, 32), Symbol('skoS'), Add(Mul(Integer(8), Symbol('skoS'), Add(Mul(Integer(8), Symbol('skoS')), Integer(27))), Integer(41))), Rational(-55, 32)), Mul(Integer(-1), Rational(1, 4), Symbol('skoSINS'), Add(Mul(Integer(4), Symbol('skoS'), Add(Mul(Symbol('skoS'), Add(Symbol('skoS'), Integer(2))), Integer(-4))), Mul(Integer(4), Symbol('skoSINS'), Add(Symbol('skoS'), Integer(1))), Integer(-13)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 6337/64) & (skoS >= 217/100) & (256*skoS**3 + 424*skoS**2 - 4521*skoS >= 4185)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(6337, 64)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Add(Mul(Integer(256), Pow(Symbol('skoS'), Integer(3))), Mul(Integer(424), Pow(Symbol('skoS'), Integer(2))), Mul(Integer(-1), Integer(4521), Symbol('skoS'))), Integer(4185)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_2(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 255/256) & (delta >= 255/256 - skoSINS**2) & (skoS*(16*skoS*(16*skoS + 51) + 81)/128 - 239/128 <= -skoSINS*(8*skoS*(skoS*(skoS + 2) - 4) + 8*skoSINS*(skoS + 1) - 25)/8)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-255, 256))), GreaterThan(Symbol('delta'), Add(Rational(255, 256), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), LessThan(Add(Mul(Rational(1, 128), Symbol('skoS'), Add(Mul(Integer(16), Symbol('skoS'), Add(Mul(Integer(16), Symbol('skoS')), Integer(51))), Integer(81))), Rational(-239, 128)), Mul(Integer(-1), Rational(1, 8), Symbol('skoSINS'), Add(Mul(Integer(8), Symbol('skoS'), Add(Mul(Symbol('skoS'), Add(Symbol('skoS'), Integer(2))), Integer(-4))), Mul(Integer(8), Symbol('skoSINS'), Add(Symbol('skoS'), Integer(1))), Integer(-25)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_3(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 16129/256) & (skoS >= 217/100) & (768*skoS**3 + 1232*skoS**2 - 12369*skoS >= 11153)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(16129, 256)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Add(Mul(Integer(768), Pow(Symbol('skoS'), Integer(3))), Mul(Integer(1232), Pow(Symbol('skoS'), Integer(2))), Mul(Integer(-1), Integer(12369), Symbol('skoS'))), Integer(11153)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_4(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 + 63) & (delta >= -skoSINS**2 - 63) & (2*skoS*(skoS*(skoS - 21) + 24) + 110 <= -skoSINS*(skoS*(skoS*(skoS + 2) - 4) + skoSINS*(skoS + 1) + 13))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(63))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-63))), LessThan(Add(Mul(Integer(2), Symbol('skoS'), Add(Mul(Symbol('skoS'), Add(Symbol('skoS'), Integer(-21))), Integer(24))), Integer(110)), Mul(Integer(-1), Symbol('skoSINS'), Add(Mul(Symbol('skoS'), Add(Mul(Symbol('skoS'), Add(Symbol('skoS'), Integer(2))), Integer(-4))), Mul(Symbol('skoSINS'), Add(Symbol('skoS'), Integer(1))), Integer(13)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_5(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 64) & (skoS >= 217/100) & (3*skoS**3 - 40*skoS**2 + 45*skoS <= -124)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(64)), GreaterThan(Symbol('skoS'), Rational(217, 100)), LessThan(Add(Mul(Integer(3), Pow(Symbol('skoS'), Integer(3))), Mul(Integer(-1), Integer(40), Pow(Symbol('skoS'), Integer(2))), Mul(Integer(45), Symbol('skoS'))), Integer(-124)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_6(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 1) & (delta >= 1 - skoSINS**2) & (2*skoS**2*(skoS + 3) - 2 <= -skoSINS*(skoS*(skoS*(skoS + 2) - 4) + skoSINS*(skoS + 1) - 3))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(1), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), LessThan(Add(Mul(Integer(2), Pow(Symbol('skoS'), Integer(2)), Add(Symbol('skoS'), Integer(3))), Integer(-2)), Mul(Integer(-1), Symbol('skoSINS'), Add(Mul(Symbol('skoS'), Add(Mul(Symbol('skoS'), Add(Symbol('skoS'), Integer(2))), Integer(-4))), Mul(Symbol('skoSINS'), Add(Symbol('skoS'), Integer(1))), Integer(-3)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_7(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 63) & (skoS >= 217/100) & (3*skoS**3 + 5*skoS**2 - 48*skoS >= 43)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(63)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Add(Mul(Integer(3), Pow(Symbol('skoS'), Integer(3))), Mul(Integer(5), Pow(Symbol('skoS'), Integer(2))), Mul(Integer(-1), Integer(48), Symbol('skoS'))), Integer(43)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_8(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 1023/1024) & (delta >= 1023/1024 - skoSINS**2) & (skoS*(32*skoS*(32*skoS + 93) - 159)/512 - 1055/512 <= -skoSINS*(16*skoS*(skoS*(skoS + 2) - 4) + 16*skoSINS*(skoS + 1) - 47)/16)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-1023, 1024))), GreaterThan(Symbol('delta'), Add(Rational(1023, 1024), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), LessThan(Add(Mul(Rational(1, 512), Symbol('skoS'), Add(Mul(Integer(32), Symbol('skoS'), Add(Mul(Integer(32), Symbol('skoS')), Integer(93))), Integer(-159))), Rational(-1055, 512)), Mul(Integer(-1), Rational(1, 16), Symbol('skoSINS'), Add(Mul(Integer(16), Symbol('skoS'), Add(Mul(Symbol('skoS'), Add(Symbol('skoS'), Integer(2))), Integer(-4))), Mul(Integer(16), Symbol('skoSINS'), Add(Symbol('skoS'), Integer(1))), Integer(-47)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_9(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 815636809/22429696) & (skoS >= 217/100) & (92243072*skoS**3 + 143832320*skoS**2 - 1379488985*skoS >= 1194565649)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(815636809, 22429696)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Add(Mul(Integer(92243072), Pow(Symbol('skoS'), Integer(3))), Mul(Integer(143832320), Pow(Symbol('skoS'), Integer(2))), Mul(Integer(-1), Integer(1379488985), Symbol('skoS'))), Integer(1194565649)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_10(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 261183/262144) & (delta >= 261183/262144 - skoSINS**2) & (skoS*(512*skoS*(512*skoS + 1443) - 78399)/131072 - 277055/131072 <= -skoSINS*(256*skoS*(skoS*(skoS + 2) - 4) + 256*skoSINS*(skoS + 1) - 737)/256)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-261183, 262144))), GreaterThan(Symbol('delta'), Add(Rational(261183, 262144), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), LessThan(Add(Mul(Rational(1, 131072), Symbol('skoS'), Add(Mul(Integer(512), Symbol('skoS'), Add(Mul(Integer(512), Symbol('skoS')), Integer(1443))), Integer(-78399))), Rational(-277055, 131072)), Mul(Integer(-1), Rational(1, 256), Symbol('skoSINS'), Add(Mul(Integer(256), Symbol('skoS'), Add(Mul(Symbol('skoS'), Add(Symbol('skoS'), Integer(2))), Integer(-4))), Mul(Integer(256), Symbol('skoSINS'), Add(Symbol('skoS'), Integer(1))), Integer(-737)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_11(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 3183553/262144) & (skoS >= 217/100) & (212992*skoS**3 + 211456*skoS**2 - 3544513*skoS >= 2813185)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(3183553, 262144)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Add(Mul(Integer(212992), Pow(Symbol('skoS'), Integer(3))), Mul(Integer(211456), Pow(Symbol('skoS'), Integer(2))), Mul(Integer(-1), Integer(3544513), Symbol('skoS'))), Integer(2813185)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_12(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4095/4096) & (delta >= 4095/4096 - skoSINS**2) & (skoS*(64*skoS*(64*skoS + 189) - 319)/2048 - 4159/2048 <= -skoSINS*(32*skoS*(skoS*(skoS + 2) - 4) + 32*skoSINS*(skoS + 1) - 95)/32)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4095, 4096))), GreaterThan(Symbol('delta'), Add(Rational(4095, 4096), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), LessThan(Add(Mul(Rational(1, 2048), Symbol('skoS'), Add(Mul(Integer(64), Symbol('skoS'), Add(Mul(Integer(64), Symbol('skoS')), Integer(189))), Integer(-319))), Rational(-4159, 2048)), Mul(Integer(-1), Rational(1, 32), Symbol('skoSINS'), Add(Mul(Integer(32), Symbol('skoS'), Add(Mul(Symbol('skoS'), Add(Symbol('skoS'), Integer(2))), Integer(-4))), Mul(Integer(32), Symbol('skoSINS'), Add(Symbol('skoS'), Integer(1))), Integer(-95)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_13(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 78849/4096) & (skoS >= 217/100) & (5120*skoS**3 + 6336*skoS**2 - 78017*skoS >= 64673)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(78849, 4096)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Add(Mul(Integer(5120), Pow(Symbol('skoS'), Integer(3))), Mul(Integer(6336), Pow(Symbol('skoS'), Integer(2))), Mul(Integer(-1), Integer(78017), Symbol('skoS'))), Integer(64673)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_14(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 16383/16384) & (delta >= 16383/16384 - skoSINS**2) & (skoS*(128*skoS*(128*skoS + 381) - 639)/8192 - 16511/8192 <= -skoSINS*(64*skoS*(skoS*(skoS + 2) - 4) + 64*skoSINS*(skoS + 1) - 191)/64)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-16383, 16384))), GreaterThan(Symbol('delta'), Add(Rational(16383, 16384), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), LessThan(Add(Mul(Rational(1, 8192), Symbol('skoS'), Add(Mul(Integer(128), Symbol('skoS'), Add(Mul(Integer(128), Symbol('skoS')), Integer(381))), Integer(-639))), Rational(-16511, 8192)), Mul(Integer(-1), Rational(1, 64), Symbol('skoSINS'), Add(Mul(Integer(64), Symbol('skoS'), Add(Mul(Symbol('skoS'), Add(Symbol('skoS'), Integer(2))), Integer(-4))), Mul(Integer(64), Symbol('skoSINS'), Add(Symbol('skoS'), Integer(1))), Integer(-191)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_15(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 573441/16384) & (skoS >= 217/100) & (32768*skoS**3 + 49536*skoS**2 - 490881*skoS >= 425089)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(573441, 16384)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Add(Mul(Integer(32768), Pow(Symbol('skoS'), Integer(3))), Mul(Integer(49536), Pow(Symbol('skoS'), Integer(2))), Mul(Integer(-1), Integer(490881), Symbol('skoS'))), Integer(425089)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_16(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 262095/262144) & (delta >= 262095/262144 - skoSINS**2) & (skoS*(512*skoS*(512*skoS + 1515) - 17871)/131072 - 265679/131072 <= -skoSINS*(256*skoS*(skoS*(skoS + 2) - 4) + 256*skoSINS*(skoS + 1) - 761)/256)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-262095, 262144))), GreaterThan(Symbol('delta'), Add(Rational(262095, 262144), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), LessThan(Add(Mul(Rational(1, 131072), Symbol('skoS'), Add(Mul(Integer(512), Symbol('skoS'), Add(Mul(Integer(512), Symbol('skoS')), Integer(1515))), Integer(-17871))), Rational(-265679, 131072)), Mul(Integer(-1), Rational(1, 256), Symbol('skoSINS'), Add(Mul(Integer(256), Symbol('skoS'), Add(Mul(Symbol('skoS'), Add(Symbol('skoS'), Integer(2))), Integer(-4))), Mul(Integer(256), Symbol('skoSINS'), Add(Symbol('skoS'), Integer(1))), Integer(-761)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_17(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 7667761/262144) & (skoS >= 217/100) & (458752*skoS**3 + 666112*skoS**2 - 6830641*skoS >= 5842225)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(7667761, 262144)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Add(Mul(Integer(458752), Pow(Symbol('skoS'), Integer(3))), Mul(Integer(666112), Pow(Symbol('skoS'), Integer(2))), Mul(Integer(-1), Integer(6830641), Symbol('skoS'))), Integer(5842225)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_18(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 1048527/1048576) & (delta >= 1048527/1048576 - skoSINS**2) & (skoS*(1024*skoS*(1024*skoS + 3051) - 35791)/524288 - 1055695/524288 <= -skoSINS*(512*skoS*(skoS*(skoS + 2) - 4) + 512*skoSINS*(skoS + 1) - 1529)/512)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-1048527, 1048576))), GreaterThan(Symbol('delta'), Add(Rational(1048527, 1048576), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), LessThan(Add(Mul(Rational(1, 524288), Symbol('skoS'), Add(Mul(Integer(1024), Symbol('skoS'), Add(Mul(Integer(1024), Symbol('skoS')), Integer(3051))), Integer(-35791))), Rational(-1055695, 524288)), Mul(Integer(-1), Rational(1, 512), Symbol('skoSINS'), Add(Mul(Integer(512), Symbol('skoS'), Add(Mul(Symbol('skoS'), Add(Symbol('skoS'), Integer(2))), Integer(-4))), Mul(Integer(512), Symbol('skoSINS'), Add(Symbol('skoS'), Integer(1))), Integer(-1529)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_19(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 23871537/1048576) & (skoS >= 217/100) & (1507328*skoS**3 + 1987584*skoS**2 - 22647857*skoS >= 19037105)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(23871537, 1048576)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Add(Mul(Integer(1507328), Pow(Symbol('skoS'), Integer(3))), Mul(Integer(1987584), Pow(Symbol('skoS'), Integer(2))), Mul(Integer(-1), Integer(22647857), Symbol('skoS'))), Integer(19037105)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_20(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4194135/4194304) & (delta >= 4194135/4194304 - skoSINS**2) & (skoS*(2048*skoS*(2048*skoS + 6105) - 132951)/2097152 - 4220759/2097152 <= -skoSINS*(1024*skoS*(skoS*(skoS + 2) - 4) + 1024*skoSINS*(skoS + 1) - 3059)/1024)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4194135, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4194135, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), LessThan(Add(Mul(Rational(1, 2097152), Symbol('skoS'), Add(Mul(Integer(2048), Symbol('skoS'), Add(Mul(Integer(2048), Symbol('skoS')), Integer(6105))), Integer(-132951))), Rational(-4220759, 2097152)), Mul(Integer(-1), Rational(1, 1024), Symbol('skoSINS'), Add(Mul(Integer(1024), Symbol('skoS'), Add(Mul(Symbol('skoS'), Add(Symbol('skoS'), Integer(2))), Integer(-4))), Mul(Integer(1024), Symbol('skoSINS'), Add(Symbol('skoS'), Integer(1))), Integer(-3059)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_21(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 95486121/4194304) & (skoS >= 217/100) & (6029312*skoS**3 + 7944192*skoS**2 - 90601641*skoS >= 76160425)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(95486121, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Add(Mul(Integer(6029312), Pow(Symbol('skoS'), Integer(3))), Mul(Integer(7944192), Pow(Symbol('skoS'), Integer(2))), Mul(Integer(-1), Integer(90601641), Symbol('skoS'))), Integer(76160425)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_22(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 4193575/4194304) & (delta >= 4193575/4194304 - skoSINS**2) & (skoS*(2048*skoS*(2048*skoS + 6063) - 275751)/2097152 - 4248871/2097152 <= -skoSINS*(1024*skoS*(skoS*(skoS + 2) - 4) + 1024*skoSINS*(skoS + 1) - 3045)/1024)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4193575, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4193575, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), LessThan(Add(Mul(Rational(1, 2097152), Symbol('skoS'), Add(Mul(Integer(2048), Symbol('skoS'), Add(Mul(Integer(2048), Symbol('skoS')), Integer(6063))), Integer(-275751))), Rational(-4248871, 2097152)), Mul(Integer(-1), Rational(1, 1024), Symbol('skoSINS'), Add(Mul(Integer(1024), Symbol('skoS'), Add(Mul(Symbol('skoS'), Add(Symbol('skoS'), Integer(2))), Integer(-4))), Mul(Integer(1024), Symbol('skoSINS'), Add(Symbol('skoS'), Integer(1))), Integer(-3045)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_23(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 134480601/4194304) & (skoS >= 217/100) & (7864320*skoS**3 + 11700224*skoS**2 - 117295833*skoS >= 100946137)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(134480601, 4194304)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Add(Mul(Integer(7864320), Pow(Symbol('skoS'), Integer(3))), Mul(Integer(11700224), Pow(Symbol('skoS'), Integer(2))), Mul(Integer(-1), Integer(117295833), Symbol('skoS'))), Integer(100946137)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_24(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (delta >= skoSINS**2 - 67097415/67108864) & (delta >= 67097415/67108864 - skoSINS**2) & (skoS*(8192*skoS*(8192*skoS + 24255) - 4371271)/33554432 - 67973959/33554432 <= -skoSINS*(4096*skoS*(skoS*(skoS + 2) - 4) + 4096*skoSINS*(skoS + 1) - 12181)/4096)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-67097415, 67108864))), GreaterThan(Symbol('delta'), Add(Rational(67097415, 67108864), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))), LessThan(Add(Mul(Rational(1, 33554432), Symbol('skoS'), Add(Mul(Integer(8192), Symbol('skoS'), Add(Mul(Integer(8192), Symbol('skoS')), Integer(24255))), Integer(-4371271))), Rational(-67973959, 33554432)), Mul(Integer(-1), Rational(1, 4096), Symbol('skoSINS'), Add(Mul(Integer(4096), Symbol('skoS'), Add(Mul(Symbol('skoS'), Add(Symbol('skoS'), Integer(2))), Integer(-4))), Mul(Integer(4096), Symbol('skoSINS'), Add(Symbol('skoS'), Integer(1))), Integer(-12181)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_25(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 2151689401/67108864) & (skoS >= 217/100) & (125829120*skoS**3 + 187179008*skoS**2 - 1876774073*skoS >= 1615193273)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2151689401, 67108864)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Add(Mul(Integer(125829120), Pow(Symbol('skoS'), Integer(3))), Mul(Integer(187179008), Pow(Symbol('skoS'), Integer(2))), Mul(Integer(-1), Integer(1876774073), Symbol('skoS'))), Integer(1615193273)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def post_condition(delta:sympy.Rational, skoS:sympy.Rational, skoCOSS:sympy.Rational, skoSINS:sympy.Rational):
	# (0 <= delta) & (217/100 <= skoS) & (skoCOSS**2 + skoSINS**2 - 1 <= delta) & (-skoCOSS**2 - skoSINS**2 + 1 <= delta) & (skoSINS*(-2*skoCOSS + skoS*(skoS*(skoS + 2) - 4) + skoSINS*(skoS + 1) - 3) <= skoCOSS*(-2*skoCOSS - 2) + skoS*(skoCOSS*(-2*skoCOSS - 10) + skoS*(-6*skoCOSS - 2*skoS - 6)) + 2)

	post_cond =  And(LessThan(Integer(0), Symbol('delta')), LessThan(Rational(217, 100), Symbol('skoS')), LessThan(Add(Pow(Symbol('skoCOSS'), Integer(2)), Pow(Symbol('skoSINS'), Integer(2)), Integer(-1)), Symbol('delta')), LessThan(Add(Mul(Integer(-1), Pow(Symbol('skoCOSS'), Integer(2))), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(1)), Symbol('delta')), LessThan(Mul(Symbol('skoSINS'), Add(Mul(Integer(-1), Integer(2), Symbol('skoCOSS')), Mul(Symbol('skoS'), Add(Mul(Symbol('skoS'), Add(Symbol('skoS'), Integer(2))), Integer(-4))), Mul(Symbol('skoSINS'), Add(Symbol('skoS'), Integer(1))), Integer(-3))), Add(Mul(Symbol('skoCOSS'), Add(Mul(Integer(-1), Integer(2), Symbol('skoCOSS')), Integer(-2))), Mul(Symbol('skoS'), Add(Mul(Symbol('skoCOSS'), Add(Mul(Integer(-1), Integer(2), Symbol('skoCOSS')), Integer(-10))), Mul(Symbol('skoS'), Add(Mul(Integer(-1), Integer(6), Symbol('skoCOSS')), Mul(Integer(-1), Integer(2), Symbol('skoS')), Integer(-6))))), Integer(2))))

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
		print('delta = 101')
		print('skoS = 4')
		print('skoCOSS = 1/8')
		print('skoSINS = -10')
		exit(0)
	
	
	if pre_condition_1(delta=delta,skoS=skoS)==True:
		print("pre_condition_1 SAT")
		print('delta = 101')
		print('skoS = 4')
		print('skoCOSS = 1/8')
		print('skoSINS = -10')
		exit(0)
	
	
	if pre_condition_2(delta=delta,skoS=skoS)==True:
		print("pre_condition_2 SAT")
		print('delta = 64')
		print('skoS = 15/4')
		print('skoCOSS = 1/16')
		print('skoSINS = -8')
		exit(0)
	
	
	if pre_condition_3(delta=delta,skoS=skoS)==True:
		print("pre_condition_3 SAT")
		print('delta = 64')
		print('skoS = 15/4')
		print('skoCOSS = 1/16')
		print('skoSINS = -8')
		exit(0)
	
	
	if pre_condition_4(delta=delta,skoS=skoS)==True:
		print("pre_condition_4 SAT")
		print('delta = 65')
		print('skoS = 3')
		print('skoCOSS = -8')
		print('skoSINS = 1')
		exit(0)
	
	
	if pre_condition_5(delta=delta,skoS=skoS)==True:
		print("pre_condition_5 SAT")
		print('delta = 65')
		print('skoS = 3')
		print('skoCOSS = -8')
		print('skoSINS = 1')
		exit(0)
	
	
	if pre_condition_6(delta=delta,skoS=skoS)==True:
		print("pre_condition_6 SAT")
		print('delta = 32257/512')
		print('skoS = 12')
		print('skoCOSS = 0')
		print('skoSINS = -8')
		exit(0)
	
	
	if pre_condition_7(delta=delta,skoS=skoS)==True:
		print("pre_condition_7 SAT")
		print('delta = 32257/512')
		print('skoS = 12')
		print('skoCOSS = 0')
		print('skoSINS = -8')
		exit(0)
	
	
	if pre_condition_8(delta=delta,skoS=skoS)==True:
		print("pre_condition_8 SAT")
		print('delta = 18619/512')
		print('skoS = 29/8')
		print('skoCOSS = -1/32')
		print('skoSINS = -28949/4736')
		exit(0)
	
	
	if pre_condition_9(delta=delta,skoS=skoS)==True:
		print("pre_condition_9 SAT")
		print('delta = 18619/512')
		print('skoS = 29/8')
		print('skoCOSS = -1/32')
		print('skoSINS = -28949/4736')
		exit(0)
	
	
	if pre_condition_10(delta=delta,skoS=skoS)==True:
		print("pre_condition_10 SAT")
		print('delta = 99487/8192')
		print('skoS = 4')
		print('skoCOSS = -31/512')
		print('skoSINS = -29/8')
		exit(0)
	
	
	if pre_condition_11(delta=delta,skoS=skoS)==True:
		print("pre_condition_11 SAT")
		print('delta = 99487/8192')
		print('skoS = 4')
		print('skoCOSS = -31/512')
		print('skoSINS = -29/8')
		exit(0)
	
	
	if pre_condition_12(delta=delta,skoS=skoS)==True:
		print("pre_condition_12 SAT")
		print('delta = 39425/2048')
		print('skoS = 15/4')
		print('skoCOSS = -1/64')
		print('skoSINS = -9/2')
		exit(0)
	
	
	if pre_condition_13(delta=delta,skoS=skoS)==True:
		print("pre_condition_13 SAT")
		print('delta = 39425/2048')
		print('skoS = 15/4')
		print('skoCOSS = -1/64')
		print('skoSINS = -9/2')
		exit(0)
	
	
	if pre_condition_14(delta=delta,skoS=skoS)==True:
		print("pre_condition_14 SAT")
		print('delta = 286721/8192')
		print('skoS = 29/8')
		print('skoCOSS = -1/128')
		print('skoSINS = -6')
		exit(0)
	
	
	if pre_condition_15(delta=delta,skoS=skoS)==True:
		print("pre_condition_15 SAT")
		print('delta = 286721/8192')
		print('skoS = 29/8')
		print('skoCOSS = -1/128')
		print('skoSINS = -6')
		exit(0)
	
	
	if pre_condition_16(delta=delta,skoS=skoS)==True:
		print("pre_condition_16 SAT")
		print('delta = 958471/32768')
		print('skoS = 29/8')
		print('skoCOSS = -7/512')
		print('skoSINS = -11/2')
		exit(0)
	
	
	if pre_condition_17(delta=delta,skoS=skoS)==True:
		print("pre_condition_17 SAT")
		print('delta = 958471/32768')
		print('skoS = 29/8')
		print('skoCOSS = -7/512')
		print('skoSINS = -11/2')
		exit(0)
	
	
	if pre_condition_18(delta=delta,skoS=skoS)==True:
		print("pre_condition_18 SAT")
		print('delta = 2983943/131072')
		print('skoS = 59/16')
		print('skoCOSS = -7/1024')
		print('skoSINS = -39/8')
		exit(0)
	
	
	if pre_condition_19(delta=delta,skoS=skoS)==True:
		print("pre_condition_19 SAT")
		print('delta = 2983943/131072')
		print('skoS = 59/16')
		print('skoCOSS = -7/1024')
		print('skoSINS = -39/8')
		exit(0)
	
	
	if pre_condition_20(delta=delta,skoS=skoS)==True:
		print("pre_condition_20 SAT")
		print('delta = 1491971/65536')
		print('skoS = 59/16')
		print('skoCOSS = -13/2048')
		print('skoSINS = -39/8')
		exit(0)
	
	
	if pre_condition_21(delta=delta,skoS=skoS)==True:
		print("pre_condition_21 SAT")
		print('delta = 1491971/65536')
		print('skoS = 59/16')
		print('skoCOSS = -13/2048')
		print('skoSINS = -39/8')
		exit(0)
	
	
	if pre_condition_22(delta=delta,skoS=skoS)==True:
		print("pre_condition_22 SAT")
		print('delta = 525315/16384')
		print('skoS = 463/128')
		print('skoCOSS = -27/2048')
		print('skoSINS = -23/4')
		exit(0)
	
	
	if pre_condition_23(delta=delta,skoS=skoS)==True:
		print("pre_condition_23 SAT")
		print('delta = 525315/16384')
		print('skoS = 463/128')
		print('skoCOSS = -27/2048')
		print('skoSINS = -23/4')
		exit(0)
	
	
	if pre_condition_24(delta=delta,skoS=skoS)==True:
		print("pre_condition_24 SAT")
		print('delta = 8405037/262144')
		print('skoS = 463/128')
		print('skoCOSS = -107/8192')
		print('skoSINS = -23/4')
		exit(0)
	
	
	if pre_condition_25(delta=delta,skoS=skoS)==True:
		print("pre_condition_25 SAT")
		print('delta = 8405037/262144')
		print('skoS = 463/128')
		print('skoCOSS = -107/8192')
		print('skoSINS = -23/4')
		exit(0)


	print("UNKNOWN")
	exit(0)
