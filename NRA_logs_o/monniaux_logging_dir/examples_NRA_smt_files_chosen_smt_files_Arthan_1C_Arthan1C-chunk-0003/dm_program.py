import sympy
from sympy import *

def pre_condition_0(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (2*skoS*(skoS*(skoS - 3) - 6) + 2 > -skoSINS*(skoS*(skoS*(skoS + 2) - 4) + skoSINS*(skoS + 1) + 1))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Add(Mul(Integer(2), Symbol('skoS'), Add(Mul(Symbol('skoS'), Add(Symbol('skoS'), Integer(-3))), Integer(-6))), Integer(2)), Mul(Integer(-1), Symbol('skoSINS'), Add(Mul(Symbol('skoS'), Add(Mul(Symbol('skoS'), Add(Symbol('skoS'), Integer(2))), Integer(-4))), Mul(Symbol('skoSINS'), Add(Symbol('skoS'), Integer(1))), Integer(1)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (-2*skoS**3 + 4*skoS**2 + 11*skoS < 11/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Integer(2), Pow(Symbol('skoS'), Integer(3))), Mul(Integer(4), Pow(Symbol('skoS'), Integer(2))), Mul(Integer(11), Symbol('skoS'))), Rational(11, 5)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_2(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (2*skoS*(skoS*(skoS + 6) + 6) + 2 > -skoSINS*(skoS*(skoS*(skoS + 2) - 4) + skoSINS*(skoS + 1) - 5))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Add(Mul(Integer(2), Symbol('skoS'), Add(Mul(Symbol('skoS'), Add(Symbol('skoS'), Integer(6))), Integer(6))), Integer(2)), Mul(Integer(-1), Symbol('skoSINS'), Add(Mul(Symbol('skoS'), Add(Mul(Symbol('skoS'), Add(Symbol('skoS'), Integer(2))), Integer(-4))), Mul(Symbol('skoSINS'), Add(Symbol('skoS'), Integer(1))), Integer(-5)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_3(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS**3 + 6*skoS**2 + 6*skoS > -1)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Add(Pow(Symbol('skoS'), Integer(3)), Mul(Integer(6), Pow(Symbol('skoS'), Integer(2))), Mul(Integer(6), Symbol('skoS'))), Integer(-1)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_4(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (2*skoS*(skoS*(skoS + 9) + 14) + 10 > -skoSINS*(skoS*(skoS*(skoS + 2) - 4) + skoSINS*(skoS + 1) - 7))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Add(Mul(Integer(2), Symbol('skoS'), Add(Mul(Symbol('skoS'), Add(Symbol('skoS'), Integer(9))), Integer(14))), Integer(10)), Mul(Integer(-1), Symbol('skoSINS'), Add(Mul(Symbol('skoS'), Add(Mul(Symbol('skoS'), Add(Symbol('skoS'), Integer(2))), Integer(-4))), Mul(Symbol('skoSINS'), Add(Symbol('skoS'), Integer(1))), Integer(-7)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_5(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (120*skoS**3 + 1136*skoS**2 + 1825*skoS > -697)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Add(Mul(Integer(120), Pow(Symbol('skoS'), Integer(3))), Mul(Integer(1136), Pow(Symbol('skoS'), Integer(2))), Mul(Integer(1825), Symbol('skoS'))), Integer(-697)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_6(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (2*skoS*(skoS*(skoS + 15) + 36) + 38 > -skoSINS*(skoS*(skoS*(skoS + 2) - 4) + skoSINS*(skoS + 1) - 11))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Add(Mul(Integer(2), Symbol('skoS'), Add(Mul(Symbol('skoS'), Add(Symbol('skoS'), Integer(15))), Integer(36))), Integer(38)), Mul(Integer(-1), Symbol('skoSINS'), Add(Mul(Symbol('skoS'), Add(Mul(Symbol('skoS'), Add(Symbol('skoS'), Integer(2))), Integer(-4))), Mul(Symbol('skoSINS'), Add(Symbol('skoS'), Integer(1))), Integer(-11)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_7(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (25*skoS**3 + 37*skoS**2 - 1492*skoS < 1657)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictLessThan(Add(Mul(Integer(25), Pow(Symbol('skoS'), Integer(3))), Mul(Integer(37), Pow(Symbol('skoS'), Integer(2))), Mul(Integer(-1), Integer(1492), Symbol('skoS'))), Integer(1657)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_8(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (2*skoS*(skoS*(skoS + 18) + 50) + 58 > -skoSINS*(skoS*(skoS*(skoS + 2) - 4) + skoSINS*(skoS + 1) - 13))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Add(Mul(Integer(2), Symbol('skoS'), Add(Mul(Symbol('skoS'), Add(Symbol('skoS'), Integer(18))), Integer(50))), Integer(58)), Mul(Integer(-1), Symbol('skoSINS'), Add(Mul(Symbol('skoS'), Add(Mul(Symbol('skoS'), Add(Symbol('skoS'), Integer(2))), Integer(-4))), Mul(Symbol('skoSINS'), Add(Symbol('skoS'), Integer(1))), Integer(-13)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_9(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (3*skoS**3 + 4*skoS**2 - 175*skoS < 401/2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictLessThan(Add(Mul(Integer(3), Pow(Symbol('skoS'), Integer(3))), Mul(Integer(4), Pow(Symbol('skoS'), Integer(2))), Mul(Integer(-1), Integer(175), Symbol('skoS'))), Rational(401, 2)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_10(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (2*skoS*(skoS*(skoS + 69) + 594) + 1010 > -skoSINS*(skoS*(skoS*(skoS + 2) - 4) + skoSINS*(skoS + 1) - 47))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Add(Mul(Integer(2), Symbol('skoS'), Add(Mul(Symbol('skoS'), Add(Symbol('skoS'), Integer(69))), Integer(594))), Integer(1010)), Mul(Integer(-1), Symbol('skoSINS'), Add(Mul(Symbol('skoS'), Add(Mul(Symbol('skoS'), Add(Symbol('skoS'), Integer(2))), Integer(-4))), Mul(Symbol('skoSINS'), Add(Symbol('skoS'), Integer(1))), Integer(-47)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_11(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (-47*skoS**3 + 40*skoS**2 + 3785*skoS > -5714)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Integer(47), Pow(Symbol('skoS'), Integer(3))), Mul(Integer(40), Pow(Symbol('skoS'), Integer(2))), Mul(Integer(3785), Symbol('skoS'))), Integer(-5714)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_12(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (2*skoS*(skoS*(skoS + 27) + 104) + 142 > -skoSINS*(skoS*(skoS*(skoS + 2) - 4) + skoSINS*(skoS + 1) - 19))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Add(Mul(Integer(2), Symbol('skoS'), Add(Mul(Symbol('skoS'), Add(Symbol('skoS'), Integer(27))), Integer(104))), Integer(142)), Mul(Integer(-1), Symbol('skoSINS'), Add(Mul(Symbol('skoS'), Add(Mul(Symbol('skoS'), Add(Symbol('skoS'), Integer(2))), Integer(-4))), Mul(Symbol('skoSINS'), Add(Symbol('skoS'), Integer(1))), Integer(-19)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_13(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (47*skoS**3 + 44*skoS**2 - 2805*skoS < 3474)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictLessThan(Add(Mul(Integer(47), Pow(Symbol('skoS'), Integer(3))), Mul(Integer(44), Pow(Symbol('skoS'), Integer(2))), Mul(Integer(-1), Integer(2805), Symbol('skoS'))), Integer(3474)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def post_condition(delta:sympy.Rational, skoS:sympy.Rational, skoCOSS:sympy.Rational, skoSINS:sympy.Rational):
	# (0 <= delta) & (skoSINS*(-2*skoCOSS + skoS*(skoS*(skoS + 2) - 4) + skoSINS*(skoS + 1) - 3) > skoCOSS*(-2*skoCOSS - 2) + skoS*(skoCOSS*(-2*skoCOSS - 10) + skoS*(-6*skoCOSS - 2*skoS - 6)) + 2)

	post_cond =  And(LessThan(Integer(0), Symbol('delta')), StrictGreaterThan(Mul(Symbol('skoSINS'), Add(Mul(Integer(-1), Integer(2), Symbol('skoCOSS')), Mul(Symbol('skoS'), Add(Mul(Symbol('skoS'), Add(Symbol('skoS'), Integer(2))), Integer(-4))), Mul(Symbol('skoSINS'), Add(Symbol('skoS'), Integer(1))), Integer(-3))), Add(Mul(Symbol('skoCOSS'), Add(Mul(Integer(-1), Integer(2), Symbol('skoCOSS')), Integer(-2))), Mul(Symbol('skoS'), Add(Mul(Symbol('skoCOSS'), Add(Mul(Integer(-1), Integer(2), Symbol('skoCOSS')), Integer(-10))), Mul(Symbol('skoS'), Add(Mul(Integer(-1), Integer(6), Symbol('skoCOSS')), Mul(Integer(-1), Integer(2), Symbol('skoS')), Integer(-6))))), Integer(2))))

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
		print('skoSINS = 1/2')
		print('skoCOSS = -2')
		print('skoS = 1/8')
		exit(0)
	
	
	if pre_condition_1(delta=delta,skoS=skoS)==True:
		print("pre_condition_1 SAT")
		print('delta = 0')
		print('skoSINS = 1/2')
		print('skoCOSS = -2')
		print('skoS = 1/8')
		exit(0)
	
	
	if pre_condition_2(delta=delta,skoS=skoS)==True:
		print("pre_condition_2 SAT")
		print('delta = 0')
		print('skoSINS = 0')
		print('skoCOSS = 1')
		print('skoS = -2')
		exit(0)
	
	
	if pre_condition_3(delta=delta,skoS=skoS)==True:
		print("pre_condition_3 SAT")
		print('delta = 0')
		print('skoSINS = 0')
		print('skoCOSS = 1')
		print('skoS = -2')
		exit(0)
	
	
	if pre_condition_4(delta=delta,skoS=skoS)==True:
		print("pre_condition_4 SAT")
		print('delta = 0')
		print('skoSINS = -1/8')
		print('skoCOSS = 2')
		print('skoS = -5')
		exit(0)
	
	
	if pre_condition_5(delta=delta,skoS=skoS)==True:
		print("pre_condition_5 SAT")
		print('delta = 0')
		print('skoSINS = -1/8')
		print('skoCOSS = 2')
		print('skoS = -5')
		exit(0)
	
	
	if pre_condition_6(delta=delta,skoS=skoS)==True:
		print("pre_condition_6 SAT")
		print('delta = 0')
		print('skoSINS = -52')
		print('skoCOSS = 4')
		print('skoS = -8')
		exit(0)
	
	
	if pre_condition_7(delta=delta,skoS=skoS)==True:
		print("pre_condition_7 SAT")
		print('delta = 0')
		print('skoSINS = -52')
		print('skoCOSS = 4')
		print('skoS = -8')
		exit(0)
	
	
	if pre_condition_8(delta=delta,skoS=skoS)==True:
		print("pre_condition_8 SAT")
		print('delta = 0')
		print('skoSINS = -50')
		print('skoCOSS = 5')
		print('skoS = -31/4')
		exit(0)
	
	
	if pre_condition_9(delta=delta,skoS=skoS)==True:
		print("pre_condition_9 SAT")
		print('delta = 0')
		print('skoSINS = -50')
		print('skoCOSS = 5')
		print('skoS = -31/4')
		exit(0)
	
	
	if pre_condition_10(delta=delta,skoS=skoS)==True:
		print("pre_condition_10 SAT")
		print('delta = 0')
		print('skoSINS = -49')
		print('skoCOSS = 22')
		print('skoS = -61/8')
		exit(0)
	
	
	if pre_condition_11(delta=delta,skoS=skoS)==True:
		print("pre_condition_11 SAT")
		print('delta = 0')
		print('skoSINS = -49')
		print('skoCOSS = 22')
		print('skoS = -61/8')
		exit(0)
	
	
	if pre_condition_12(delta=delta,skoS=skoS)==True:
		print("pre_condition_12 SAT")
		print('delta = 0')
		print('skoSINS = -49')
		print('skoCOSS = 8')
		print('skoS = -121/16')
		exit(0)
	
	
	if pre_condition_13(delta=delta,skoS=skoS)==True:
		print("pre_condition_13 SAT")
		print('delta = 0')
		print('skoSINS = -49')
		print('skoCOSS = 8')
		print('skoS = -121/16')
		exit(0)


	print("Weakest pre-condition UNSAT")
	exit(0)
