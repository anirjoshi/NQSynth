import sympy
from sympy import *

def pre_condition_0(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (2*skoS*(skoS*(skoS - 3) - 6) + 2 <= -skoSINS*(skoS*(skoS*(skoS + 2) - 4) + skoSINS*(skoS + 1) + 1))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), LessThan(Add(Mul(Integer(2), Symbol('skoS'), Add(Mul(Symbol('skoS'), Add(Symbol('skoS'), Integer(-3))), Integer(-6))), Integer(2)), Mul(Integer(-1), Symbol('skoSINS'), Add(Mul(Symbol('skoS'), Add(Mul(Symbol('skoS'), Add(Symbol('skoS'), Integer(2))), Integer(-4))), Mul(Symbol('skoSINS'), Add(Symbol('skoS'), Integer(1))), Integer(1)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (-136*skoS**3 + 368*skoS**2 + 799*skoS >= 137)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Add(Mul(Integer(-1), Integer(136), Pow(Symbol('skoS'), Integer(3))), Mul(Integer(368), Pow(Symbol('skoS'), Integer(2))), Mul(Integer(799), Symbol('skoS'))), Integer(137)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_2(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (2*skoS*(skoS*(skoS - 39) + 126) + 362 <= -skoSINS*(skoS*(skoS*(skoS + 2) - 4) + skoSINS*(skoS + 1) + 25))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), LessThan(Add(Mul(Integer(2), Symbol('skoS'), Add(Mul(Symbol('skoS'), Add(Symbol('skoS'), Integer(-39))), Integer(126))), Integer(362)), Mul(Integer(-1), Symbol('skoSINS'), Add(Mul(Symbol('skoS'), Add(Mul(Symbol('skoS'), Add(Symbol('skoS'), Integer(2))), Integer(-4))), Mul(Symbol('skoSINS'), Add(Symbol('skoS'), Integer(1))), Integer(25)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_3(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (28*skoS**3 - 1256*skoS**2 + 4049*skoS <= -5693)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), LessThan(Add(Mul(Integer(28), Pow(Symbol('skoS'), Integer(3))), Mul(Integer(-1), Integer(1256), Pow(Symbol('skoS'), Integer(2))), Mul(Integer(4049), Symbol('skoS'))), Integer(-5693)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_4(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (2*skoS*(skoS*(skoS - 36) + 104) + 310 <= -skoSINS*(skoS*(skoS*(skoS + 2) - 4) + skoSINS*(skoS + 1) + 23))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), LessThan(Add(Mul(Integer(2), Symbol('skoS'), Add(Mul(Symbol('skoS'), Add(Symbol('skoS'), Integer(-36))), Integer(104))), Integer(310)), Mul(Integer(-1), Symbol('skoSINS'), Add(Mul(Symbol('skoS'), Add(Mul(Symbol('skoS'), Add(Symbol('skoS'), Integer(2))), Integer(-4))), Mul(Symbol('skoSINS'), Add(Symbol('skoS'), Integer(1))), Integer(23)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_5(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (23*skoS**3 + 122*skoS**2 - 933*skoS >= 360)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Add(Mul(Integer(23), Pow(Symbol('skoS'), Integer(3))), Mul(Integer(122), Pow(Symbol('skoS'), Integer(2))), Mul(Integer(-1), Integer(933), Symbol('skoS'))), Integer(360)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_6(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (2*skoS*(skoS*(skoS - 30) + 66) + 218 <= -skoSINS*(skoS*(skoS*(skoS + 2) - 4) + skoSINS*(skoS + 1) + 19))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), LessThan(Add(Mul(Integer(2), Symbol('skoS'), Add(Mul(Symbol('skoS'), Add(Symbol('skoS'), Integer(-30))), Integer(66))), Integer(218)), Mul(Integer(-1), Symbol('skoSINS'), Add(Mul(Symbol('skoS'), Add(Mul(Symbol('skoS'), Add(Symbol('skoS'), Integer(2))), Integer(-4))), Mul(Symbol('skoSINS'), Add(Symbol('skoS'), Integer(1))), Integer(19)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_7(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (21*skoS**3 + 106*skoS**2 - 753*skoS >= 310)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Add(Mul(Integer(21), Pow(Symbol('skoS'), Integer(3))), Mul(Integer(106), Pow(Symbol('skoS'), Integer(2))), Mul(Integer(-1), Integer(753), Symbol('skoS'))), Integer(310)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_8(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (2*skoS*(skoS*(skoS - 21) + 24) + 110 <= -skoSINS*(skoS*(skoS*(skoS + 2) - 4) + skoSINS*(skoS + 1) + 13))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), LessThan(Add(Mul(Integer(2), Symbol('skoS'), Add(Mul(Symbol('skoS'), Add(Symbol('skoS'), Integer(-21))), Integer(24))), Integer(110)), Mul(Integer(-1), Symbol('skoSINS'), Add(Mul(Symbol('skoS'), Add(Mul(Symbol('skoS'), Add(Symbol('skoS'), Integer(2))), Integer(-4))), Mul(Symbol('skoSINS'), Add(Symbol('skoS'), Integer(1))), Integer(13)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_9(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (10*skoS**3 + 43*skoS**2 - 310*skoS >= 154)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Add(Mul(Integer(10), Pow(Symbol('skoS'), Integer(3))), Mul(Integer(43), Pow(Symbol('skoS'), Integer(2))), Mul(Integer(-1), Integer(310), Symbol('skoS'))), Integer(154)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_10(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (2*skoS*(skoS*(skoS - 27) + 50) + 178 <= -skoSINS*(skoS*(skoS*(skoS + 2) - 4) + skoSINS*(skoS + 1) + 17))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), LessThan(Add(Mul(Integer(2), Symbol('skoS'), Add(Mul(Symbol('skoS'), Add(Symbol('skoS'), Integer(-27))), Integer(50))), Integer(178)), Mul(Integer(-1), Symbol('skoSINS'), Add(Mul(Symbol('skoS'), Add(Mul(Symbol('skoS'), Add(Symbol('skoS'), Integer(2))), Integer(-4))), Mul(Symbol('skoSINS'), Add(Symbol('skoS'), Integer(1))), Integer(17)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_11(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (316*skoS**3 + 1560*skoS**2 - 10561*skoS >= 4501)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Add(Mul(Integer(316), Pow(Symbol('skoS'), Integer(3))), Mul(Integer(1560), Pow(Symbol('skoS'), Integer(2))), Mul(Integer(-1), Integer(10561), Symbol('skoS'))), Integer(4501)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_12(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (2*skoS*(skoS*(skoS - 24) + 36) + 142 <= -skoSINS*(skoS*(skoS*(skoS + 2) - 4) + skoSINS*(skoS + 1) + 15))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), LessThan(Add(Mul(Integer(2), Symbol('skoS'), Add(Mul(Symbol('skoS'), Add(Symbol('skoS'), Integer(-24))), Integer(36))), Integer(142)), Mul(Integer(-1), Symbol('skoSINS'), Add(Mul(Symbol('skoS'), Add(Mul(Symbol('skoS'), Add(Symbol('skoS'), Integer(2))), Integer(-4))), Mul(Symbol('skoSINS'), Add(Symbol('skoS'), Integer(1))), Integer(15)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_13(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 217/100) & (316*skoS**3 + 1464*skoS**2 - 10113*skoS >= 4621)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(217, 100)), GreaterThan(Add(Mul(Integer(316), Pow(Symbol('skoS'), Integer(3))), Mul(Integer(1464), Pow(Symbol('skoS'), Integer(2))), Mul(Integer(-1), Integer(10113), Symbol('skoS'))), Integer(4621)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def post_condition(delta:sympy.Rational, skoS:sympy.Rational, skoCOSS:sympy.Rational, skoSINS:sympy.Rational):
	# (0 <= delta) & (217/100 <= skoS) & (skoSINS*(-2*skoCOSS + skoS*(skoS*(skoS + 2) - 4) + skoSINS*(skoS + 1) - 3) <= skoCOSS*(-2*skoCOSS - 2) + skoS*(skoCOSS*(-2*skoCOSS - 10) + skoS*(-6*skoCOSS - 2*skoS - 6)) + 2)

	post_cond =  And(LessThan(Integer(0), Symbol('delta')), LessThan(Rational(217, 100), Symbol('skoS')), LessThan(Mul(Symbol('skoSINS'), Add(Mul(Integer(-1), Integer(2), Symbol('skoCOSS')), Mul(Symbol('skoS'), Add(Mul(Symbol('skoS'), Add(Symbol('skoS'), Integer(2))), Integer(-4))), Mul(Symbol('skoSINS'), Add(Symbol('skoS'), Integer(1))), Integer(-3))), Add(Mul(Symbol('skoCOSS'), Add(Mul(Integer(-1), Integer(2), Symbol('skoCOSS')), Integer(-2))), Mul(Symbol('skoS'), Add(Mul(Symbol('skoCOSS'), Add(Mul(Integer(-1), Integer(2), Symbol('skoCOSS')), Integer(-10))), Mul(Symbol('skoS'), Add(Mul(Integer(-1), Integer(6), Symbol('skoCOSS')), Mul(Integer(-1), Integer(2), Symbol('skoS')), Integer(-6))))), Integer(2))))

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
		print('skoS = 4')
		print('skoSINS = 1/8')
		print('skoCOSS = -2')
		exit(0)
	
	
	if pre_condition_1(delta=delta,skoS=skoS)==True:
		print("pre_condition_1 SAT")
		print('delta = 0')
		print('skoS = 4')
		print('skoSINS = 1/8')
		print('skoCOSS = -2')
		exit(0)
	
	
	if pre_condition_2(delta=delta,skoS=skoS)==True:
		print("pre_condition_2 SAT")
		print('delta = 0')
		print('skoS = 5')
		print('skoSINS = -1/4')
		print('skoCOSS = -14')
		exit(0)
	
	
	if pre_condition_3(delta=delta,skoS=skoS)==True:
		print("pre_condition_3 SAT")
		print('delta = 0')
		print('skoS = 5')
		print('skoSINS = -1/4')
		print('skoCOSS = -14')
		exit(0)
	
	
	if pre_condition_4(delta=delta,skoS=skoS)==True:
		print("pre_condition_4 SAT")
		print('delta = 0')
		print('skoS = 9/2')
		print('skoSINS = -25')
		print('skoCOSS = -13')
		exit(0)
	
	
	if pre_condition_5(delta=delta,skoS=skoS)==True:
		print("pre_condition_5 SAT")
		print('delta = 0')
		print('skoS = 9/2')
		print('skoSINS = -25')
		print('skoCOSS = -13')
		exit(0)
	
	
	if pre_condition_6(delta=delta,skoS=skoS)==True:
		print("pre_condition_6 SAT")
		print('delta = 0')
		print('skoS = 17/4')
		print('skoSINS = -23')
		print('skoCOSS = -11')
		exit(0)
	
	
	if pre_condition_7(delta=delta,skoS=skoS)==True:
		print("pre_condition_7 SAT")
		print('delta = 0')
		print('skoS = 17/4')
		print('skoSINS = -23')
		print('skoCOSS = -11')
		exit(0)
	
	
	if pre_condition_8(delta=delta,skoS=skoS)==True:
		print("pre_condition_8 SAT")
		print('delta = 0')
		print('skoS = 33/8')
		print('skoSINS = -22')
		print('skoCOSS = -8')
		exit(0)
	
	
	if pre_condition_9(delta=delta,skoS=skoS)==True:
		print("pre_condition_9 SAT")
		print('delta = 0')
		print('skoS = 33/8')
		print('skoSINS = -22')
		print('skoCOSS = -8')
		exit(0)
	
	
	if pre_condition_10(delta=delta,skoS=skoS)==True:
		print("pre_condition_10 SAT")
		print('delta = 0')
		print('skoS = 131/32')
		print('skoSINS = -87/4')
		print('skoCOSS = -10')
		exit(0)
	
	
	if pre_condition_11(delta=delta,skoS=skoS)==True:
		print("pre_condition_11 SAT")
		print('delta = 0')
		print('skoS = 131/32')
		print('skoSINS = -87/4')
		print('skoCOSS = -10')
		exit(0)
	
	
	if pre_condition_12(delta=delta,skoS=skoS)==True:
		print("pre_condition_12 SAT")
		print('delta = 0')
		print('skoS = 523/128')
		print('skoSINS = -87/4')
		print('skoCOSS = -9')
		exit(0)
	
	
	if pre_condition_13(delta=delta,skoS=skoS)==True:
		print("pre_condition_13 SAT")
		print('delta = 0')
		print('skoS = 523/128')
		print('skoSINS = -87/4')
		print('skoCOSS = -9')
		exit(0)


	print("Weakest pre-condition UNSAT")
	exit(0)
