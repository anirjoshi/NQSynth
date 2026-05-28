import sympy
from sympy import *

def pre_condition_0(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 9/20) & (delta >= skoSINS**2 + 143) & (delta >= -skoSINS**2 - 143) & (2*skoS*(skoS*(skoS - 15) + 3) + 38 <= -skoSINS*(2*skoS*(skoS*(skoS + 3) - 3) + skoSINS*(skoS + 1) + 14)/4)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(9, 20)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(143))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-143))), LessThan(Add(Mul(Integer(2), Symbol('skoS'), Add(Mul(Symbol('skoS'), Add(Symbol('skoS'), Integer(-15))), Integer(3))), Integer(38)), Mul(Integer(-1), Rational(1, 4), Symbol('skoSINS'), Add(Mul(Integer(2), Symbol('skoS'), Add(Mul(Symbol('skoS'), Add(Symbol('skoS'), Integer(3))), Integer(-3))), Mul(Symbol('skoSINS'), Add(Symbol('skoS'), Integer(1))), Integer(14)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 432) & (skoS >= 9/20) & (26*skoS**3 + 222*skoS**2 - 415*skoS >= 203)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(432)), GreaterThan(Symbol('skoS'), Rational(9, 20)), GreaterThan(Add(Mul(Integer(26), Pow(Symbol('skoS'), Integer(3))), Mul(Integer(222), Pow(Symbol('skoS'), Integer(2))), Mul(Integer(-1), Integer(415), Symbol('skoS'))), Integer(203)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_2(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 9/20) & (delta >= skoSINS**2 + 99) & (delta >= -skoSINS**2 - 99) & (2*skoS*(skoS*(skoS - 12) - 2) + 22 <= -skoSINS*(2*skoS*(skoS*(skoS + 3) - 3) + skoSINS*(skoS + 1) + 10)/4)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(9, 20)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(99))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-99))), LessThan(Add(Mul(Integer(2), Symbol('skoS'), Add(Mul(Symbol('skoS'), Add(Symbol('skoS'), Integer(-12))), Integer(-2))), Integer(22)), Mul(Integer(-1), Rational(1, 4), Symbol('skoSINS'), Add(Mul(Integer(2), Symbol('skoS'), Add(Mul(Symbol('skoS'), Add(Symbol('skoS'), Integer(3))), Integer(-3))), Mul(Symbol('skoSINS'), Add(Symbol('skoS'), Integer(1))), Integer(10)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_3(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 100) & (skoS >= 9/20) & (-10*skoS**3 + 90*skoS**2 + 21*skoS >= 99)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(100)), GreaterThan(Symbol('skoS'), Rational(9, 20)), GreaterThan(Add(Mul(Integer(-1), Integer(10), Pow(Symbol('skoS'), Integer(3))), Mul(Integer(90), Pow(Symbol('skoS'), Integer(2))), Mul(Integer(21), Symbol('skoS'))), Integer(99)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_4(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 9/20) & (delta >= skoSINS**2 + 48) & (delta >= -skoSINS**2 - 48) & (skoS*(2*skoS*(2*skoS - 15) - 23)/2 + 11/2 <= -skoSINS*(2*skoS*(skoS*(skoS + 3) - 3) + skoSINS*(skoS + 1) + 4)/4)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(9, 20)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(48))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-48))), LessThan(Add(Mul(Rational(1, 2), Symbol('skoS'), Add(Mul(Integer(2), Symbol('skoS'), Add(Mul(Integer(2), Symbol('skoS')), Integer(-15))), Integer(-23))), Rational(11, 2)), Mul(Integer(-1), Rational(1, 4), Symbol('skoSINS'), Add(Mul(Integer(2), Symbol('skoS'), Add(Mul(Symbol('skoS'), Add(Symbol('skoS'), Integer(3))), Integer(-3))), Mul(Symbol('skoSINS'), Add(Symbol('skoS'), Integer(1))), Integer(4)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_5(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 97) & (skoS >= 9/20) & (2*skoS**3 + 34*skoS**2 - 15*skoS >= 43/3)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(97)), GreaterThan(Symbol('skoS'), Rational(9, 20)), GreaterThan(Add(Mul(Integer(2), Pow(Symbol('skoS'), Integer(3))), Mul(Integer(34), Pow(Symbol('skoS'), Integer(2))), Mul(Integer(-1), Integer(15), Symbol('skoS'))), Rational(43, 3)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_6(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 9/20) & (delta >= skoSINS**2 + 24) & (delta >= -skoSINS**2 - 24) & (skoS*(2*skoS*(2*skoS - 9) - 23)/2 - 1/2 <= -skoSINS*(2*skoS*(skoS*(skoS + 3) - 3) + skoSINS*(skoS + 1))/4)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(9, 20)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(24))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-24))), LessThan(Add(Mul(Rational(1, 2), Symbol('skoS'), Add(Mul(Integer(2), Symbol('skoS'), Add(Mul(Integer(2), Symbol('skoS')), Integer(-9))), Integer(-23))), Rational(-1, 2)), Mul(Integer(-1), Rational(1, 4), Symbol('skoSINS'), Add(Mul(Integer(2), Symbol('skoS'), Add(Mul(Symbol('skoS'), Add(Symbol('skoS'), Integer(3))), Integer(-3))), Mul(Symbol('skoSINS'), Add(Symbol('skoS'), Integer(1)))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_7(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 673/16) & (skoS >= 9/20) & (8*skoS**3 + 984*skoS**2 + 39*skoS >= 257)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(673, 16)), GreaterThan(Symbol('skoS'), Rational(9, 20)), GreaterThan(Add(Mul(Integer(8), Pow(Symbol('skoS'), Integer(3))), Mul(Integer(984), Pow(Symbol('skoS'), Integer(2))), Mul(Integer(39), Symbol('skoS'))), Integer(257)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_8(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 9/20) & (delta >= skoSINS**2 + 35) & (delta >= -skoSINS**2 - 35) & (2*skoS*(skoS*(skoS - 6) - 6) + 2 <= -skoSINS*(2*skoS*(skoS*(skoS + 3) - 3) + skoSINS*(skoS + 1) + 2)/4)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(9, 20)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(35))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-35))), LessThan(Add(Mul(Integer(2), Symbol('skoS'), Add(Mul(Symbol('skoS'), Add(Symbol('skoS'), Integer(-6))), Integer(-6))), Integer(2)), Mul(Integer(-1), Rational(1, 4), Symbol('skoSINS'), Add(Mul(Integer(2), Symbol('skoS'), Add(Mul(Symbol('skoS'), Add(Symbol('skoS'), Integer(3))), Integer(-3))), Mul(Symbol('skoSINS'), Add(Symbol('skoS'), Integer(1))), Integer(2)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_9(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 849/16) & (skoS >= 9/20) & (8*skoS**3 + 1176*skoS**2 + 71*skoS >= 281)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(849, 16)), GreaterThan(Symbol('skoS'), Rational(9, 20)), GreaterThan(Add(Mul(Integer(8), Pow(Symbol('skoS'), Integer(3))), Mul(Integer(1176), Pow(Symbol('skoS'), Integer(2))), Mul(Integer(71), Symbol('skoS'))), Integer(281)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_10(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 9/20) & (delta >= skoSINS**2 + 2145/64) & (delta >= -skoSINS**2 - 2145/64) & (skoS*(16*skoS*(16*skoS - 93) - 1535)/128 + 209/128 <= -skoSINS*(8*skoS*(skoS*(skoS + 3) - 3) + 4*skoSINS*(skoS + 1) + 7)/16)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(9, 20)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(2145, 64))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Rational(-2145, 64))), LessThan(Add(Mul(Rational(1, 128), Symbol('skoS'), Add(Mul(Integer(16), Symbol('skoS'), Add(Mul(Integer(16), Symbol('skoS')), Integer(-93))), Integer(-1535))), Rational(209, 128)), Mul(Integer(-1), Rational(1, 16), Symbol('skoSINS'), Add(Mul(Integer(8), Symbol('skoS'), Add(Mul(Symbol('skoS'), Add(Symbol('skoS'), Integer(3))), Integer(-3))), Mul(Integer(4), Symbol('skoSINS'), Add(Symbol('skoS'), Integer(1))), Integer(7)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_11(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 13341/256) & (skoS >= 9/20) & (160*skoS**3 + 18528*skoS**2 + 895*skoS >= 4501)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(13341, 256)), GreaterThan(Symbol('skoS'), Rational(9, 20)), GreaterThan(Add(Mul(Integer(160), Pow(Symbol('skoS'), Integer(3))), Mul(Integer(18528), Pow(Symbol('skoS'), Integer(2))), Mul(Integer(895), Symbol('skoS'))), Integer(4501)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_12(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 9/20) & (delta >= skoSINS**2 + 8393/256) & (delta >= -skoSINS**2 - 8393/256) & (skoS*(32*skoS*(32*skoS - 183) - 6135)/512 + 745/512 <= -skoSINS*(16*skoS*(skoS*(skoS + 3) - 3) + 8*skoSINS*(skoS + 1) + 13)/32)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(9, 20)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(8393, 256))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Rational(-8393, 256))), LessThan(Add(Mul(Rational(1, 512), Symbol('skoS'), Add(Mul(Integer(32), Symbol('skoS'), Add(Mul(Integer(32), Symbol('skoS')), Integer(-183))), Integer(-6135))), Rational(745, 512)), Mul(Integer(-1), Rational(1, 32), Symbol('skoSINS'), Add(Mul(Integer(16), Symbol('skoS'), Add(Mul(Symbol('skoS'), Add(Symbol('skoS'), Integer(3))), Integer(-3))), Mul(Integer(8), Symbol('skoSINS'), Add(Symbol('skoS'), Integer(1))), Integer(13)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_13(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 3317169/65536) & (skoS >= 9/20) & (29184*skoS**3 + 4658688*skoS**2 + 312143*skoS >= 1100305)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(3317169, 65536)), GreaterThan(Symbol('skoS'), Rational(9, 20)), GreaterThan(Add(Mul(Integer(29184), Pow(Symbol('skoS'), Integer(3))), Mul(Integer(4658688), Pow(Symbol('skoS'), Integer(2))), Mul(Integer(312143), Symbol('skoS'))), Integer(1100305)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_14(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 9/20) & (delta >= skoSINS**2 + 15) & (delta >= -skoSINS**2 - 15) & (2*skoS*(skoS*(skoS - 3) - 5) - 2 <= -skoSINS*(2*skoS*(skoS*(skoS + 3) - 3) + skoSINS*(skoS + 1) - 2)/4)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(9, 20)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(15))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(-15))), LessThan(Add(Mul(Integer(2), Symbol('skoS'), Add(Mul(Symbol('skoS'), Add(Symbol('skoS'), Integer(-3))), Integer(-5))), Integer(-2)), Mul(Integer(-1), Rational(1, 4), Symbol('skoSINS'), Add(Mul(Integer(2), Symbol('skoS'), Add(Mul(Symbol('skoS'), Add(Symbol('skoS'), Integer(3))), Integer(-3))), Mul(Symbol('skoSINS'), Add(Symbol('skoS'), Integer(1))), Integer(-2)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_15(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 61/4) & (skoS >= 9/20) & (-28*skoS**3 + 108*skoS**2 + 147*skoS >= -27)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(61, 4)), GreaterThan(Symbol('skoS'), Rational(9, 20)), GreaterThan(Add(Mul(Integer(-1), Integer(28), Pow(Symbol('skoS'), Integer(3))), Mul(Integer(108), Pow(Symbol('skoS'), Integer(2))), Mul(Integer(147), Symbol('skoS'))), Integer(-27)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_16(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 9/20) & (delta >= skoSINS**2 + 16353/4096) & (delta >= -skoSINS**2 - 16353/4096) & (skoS*(128*skoS*(128*skoS - 45) - 40223)/8192 - 18079/8192 <= -skoSINS*(64*skoS*(skoS*(skoS + 3) - 3) + 32*skoSINS*(skoS + 1) - 177)/128)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(9, 20)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(16353, 4096))), GreaterThan(Symbol('delta'), Add(Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Rational(-16353, 4096))), LessThan(Add(Mul(Rational(1, 8192), Symbol('skoS'), Add(Mul(Integer(128), Symbol('skoS'), Add(Mul(Integer(128), Symbol('skoS')), Integer(-45))), Integer(-40223))), Rational(-18079, 8192)), Mul(Integer(-1), Rational(1, 128), Symbol('skoSINS'), Add(Mul(Integer(64), Symbol('skoS'), Add(Mul(Symbol('skoS'), Add(Symbol('skoS'), Integer(3))), Integer(-3))), Mul(Integer(32), Symbol('skoSINS'), Add(Symbol('skoS'), Integer(1))), Integer(-177)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_17(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 32737/4096) & (skoS >= 9/20) & (-8192*skoS**3 + 30336*skoS**2 + 7455*skoS >= 12769)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(32737, 4096)), GreaterThan(Symbol('skoS'), Rational(9, 20)), GreaterThan(Add(Mul(Integer(-1), Integer(8192), Pow(Symbol('skoS'), Integer(3))), Mul(Integer(30336), Pow(Symbol('skoS'), Integer(2))), Mul(Integer(7455), Symbol('skoS'))), Integer(12769)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def post_condition(delta:sympy.Rational, skoS:sympy.Rational, skoCOSS:sympy.Rational, skoSINS:sympy.Rational):
	# (0 <= delta) & (9/20 <= skoS) & (skoCOSS**2 + skoSINS**2 - 1 <= delta) & (-skoCOSS**2 - skoSINS**2 + 1 <= delta) & (skoSINS*(-skoCOSS/2 + skoS*(skoS*(skoS/2 + 3/2) - 3/2) + skoSINS*(skoS/4 + 1/4) - 5/2) <= skoCOSS*(-skoCOSS/2 - 3) + skoS*(skoCOSS*(-skoCOSS/2 - 6) + skoS*(-3*skoCOSS - 2*skoS - 6) - 6) - 2)

	post_cond =  And(LessThan(Integer(0), Symbol('delta')), LessThan(Rational(9, 20), Symbol('skoS')), LessThan(Add(Pow(Symbol('skoCOSS'), Integer(2)), Pow(Symbol('skoSINS'), Integer(2)), Integer(-1)), Symbol('delta')), LessThan(Add(Mul(Integer(-1), Pow(Symbol('skoCOSS'), Integer(2))), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(1)), Symbol('delta')), LessThan(Mul(Symbol('skoSINS'), Add(Mul(Integer(-1), Rational(1, 2), Symbol('skoCOSS')), Mul(Symbol('skoS'), Add(Mul(Symbol('skoS'), Add(Mul(Rational(1, 2), Symbol('skoS')), Rational(3, 2))), Rational(-3, 2))), Mul(Symbol('skoSINS'), Add(Mul(Rational(1, 4), Symbol('skoS')), Rational(1, 4))), Rational(-5, 2))), Add(Mul(Symbol('skoCOSS'), Add(Mul(Integer(-1), Rational(1, 2), Symbol('skoCOSS')), Integer(-3))), Mul(Symbol('skoS'), Add(Mul(Symbol('skoCOSS'), Add(Mul(Integer(-1), Rational(1, 2), Symbol('skoCOSS')), Integer(-6))), Mul(Symbol('skoS'), Add(Mul(Integer(-1), Integer(3), Symbol('skoCOSS')), Mul(Integer(-1), Integer(2), Symbol('skoS')), Integer(-6))), Integer(-6))), Integer(-2))))

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
		print('delta = 433')
		print('skoS = 2')
		print('skoCOSS = -12')
		print('skoSINS = -17')
		exit(0)
	
	
	if pre_condition_1(delta=delta,skoS=skoS)==True:
		print("pre_condition_1 SAT")
		print('delta = 433')
		print('skoS = 2')
		print('skoCOSS = -12')
		print('skoSINS = -17')
		exit(0)
	
	
	if pre_condition_2(delta=delta,skoS=skoS)==True:
		print("pre_condition_2 SAT")
		print('delta = 101')
		print('skoS = 1')
		print('skoCOSS = -10')
		print('skoSINS = 1')
		exit(0)
	
	
	if pre_condition_3(delta=delta,skoS=skoS)==True:
		print("pre_condition_3 SAT")
		print('delta = 101')
		print('skoS = 1')
		print('skoCOSS = -10')
		print('skoSINS = 1')
		exit(0)
	
	
	if pre_condition_4(delta=delta,skoS=skoS)==True:
		print("pre_condition_4 SAT")
		print('delta = 98')
		print('skoS = 1')
		print('skoCOSS = -7')
		print('skoSINS = -7')
		exit(0)
	
	
	if pre_condition_5(delta=delta,skoS=skoS)==True:
		print("pre_condition_5 SAT")
		print('delta = 98')
		print('skoS = 1')
		print('skoCOSS = -7')
		print('skoSINS = -7')
		exit(0)
	
	
	if pre_condition_6(delta=delta,skoS=skoS)==True:
		print("pre_condition_6 SAT")
		print('delta = 43')
		print('skoS = 1/2')
		print('skoCOSS = -5')
		print('skoSINS = -17/4')
		exit(0)
	
	
	if pre_condition_7(delta=delta,skoS=skoS)==True:
		print("pre_condition_7 SAT")
		print('delta = 43')
		print('skoS = 1/2')
		print('skoCOSS = -5')
		print('skoSINS = -17/4')
		exit(0)
	
	
	if pre_condition_8(delta=delta,skoS=skoS)==True:
		print("pre_condition_8 SAT")
		print('delta = 54')
		print('skoS = 15/32')
		print('skoCOSS = -6')
		print('skoSINS = -17/4')
		exit(0)
	
	
	if pre_condition_9(delta=delta,skoS=skoS)==True:
		print("pre_condition_9 SAT")
		print('delta = 54')
		print('skoS = 15/32')
		print('skoCOSS = -6')
		print('skoSINS = -17/4')
		exit(0)
	
	
	if pre_condition_10(delta=delta,skoS=skoS)==True:
		print("pre_condition_10 SAT")
		print('delta = 53')
		print('skoS = 15/32')
		print('skoCOSS = -47/8')
		print('skoSINS = -69/16')
		exit(0)
	
	
	if pre_condition_11(delta=delta,skoS=skoS)==True:
		print("pre_condition_11 SAT")
		print('delta = 53')
		print('skoS = 15/32')
		print('skoCOSS = -47/8')
		print('skoSINS = -69/16')
		exit(0)
	
	
	if pre_condition_12(delta=delta,skoS=skoS)==True:
		print("pre_condition_12 SAT")
		print('delta = 51')
		print('skoS = 29/64')
		print('skoCOSS = -93/16')
		print('skoSINS = -1081/256')
		exit(0)
	
	
	if pre_condition_13(delta=delta,skoS=skoS)==True:
		print("pre_condition_13 SAT")
		print('delta = 51')
		print('skoS = 29/64')
		print('skoCOSS = -93/16')
		print('skoSINS = -1081/256')
		exit(0)
	
	
	if pre_condition_14(delta=delta,skoS=skoS)==True:
		print("pre_condition_14 SAT")
		print('delta = 16')
		print('skoS = 29/64')
		print('skoCOSS = -4')
		print('skoSINS = -1/2')
		exit(0)
	
	
	if pre_condition_15(delta=delta,skoS=skoS)==True:
		print("pre_condition_15 SAT")
		print('delta = 16')
		print('skoS = 29/64')
		print('skoCOSS = -4')
		print('skoSINS = -1/2')
		exit(0)
	
	
	if pre_condition_16(delta=delta,skoS=skoS)==True:
		print("pre_condition_16 SAT")
		print('delta = 8')
		print('skoS = 9/8')
		print('skoCOSS = -143/64')
		print('skoSINS = -2')
		exit(0)
	
	
	if pre_condition_17(delta=delta,skoS=skoS)==True:
		print("pre_condition_17 SAT")
		print('delta = 8')
		print('skoS = 9/8')
		print('skoCOSS = -143/64')
		print('skoSINS = -2')
		exit(0)


	print("UNKNOWN")
	exit(0)
