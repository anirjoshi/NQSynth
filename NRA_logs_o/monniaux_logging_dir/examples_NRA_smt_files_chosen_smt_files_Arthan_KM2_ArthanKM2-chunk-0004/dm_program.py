import sympy
from sympy import *

def pre_condition_0(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 9/20) & (2*skoS*(skoS**2 - 2) - 2 > -skoSINS*(2*skoS*(skoS*(skoS + 3) - 3) + skoSINS*(skoS + 1) - 6)/4)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(9, 20)), StrictGreaterThan(Add(Mul(Integer(2), Symbol('skoS'), Add(Pow(Symbol('skoS'), Integer(2)), Integer(-2))), Integer(-2)), Mul(Integer(-1), Rational(1, 4), Symbol('skoSINS'), Add(Mul(Integer(2), Symbol('skoS'), Add(Mul(Symbol('skoS'), Add(Symbol('skoS'), Integer(3))), Integer(-3))), Mul(Symbol('skoSINS'), Add(Symbol('skoS'), Integer(1))), Integer(-6)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 9/20) & (176*skoS**3 + 16*skoS**2 - 357*skoS > 559/3)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(9, 20)), StrictGreaterThan(Add(Mul(Integer(176), Pow(Symbol('skoS'), Integer(3))), Mul(Integer(16), Pow(Symbol('skoS'), Integer(2))), Mul(Integer(-1), Integer(357), Symbol('skoS'))), Rational(559, 3)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_2(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 9/20) & (2*skoS*(skoS*(skoS + 3) + 3) + 2 > -skoSINS*(2*skoS*(skoS*(skoS + 3) - 3) + skoSINS*(skoS + 1) - 10)/4)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(9, 20)), StrictGreaterThan(Add(Mul(Integer(2), Symbol('skoS'), Add(Mul(Symbol('skoS'), Add(Symbol('skoS'), Integer(3))), Integer(3))), Integer(2)), Mul(Integer(-1), Rational(1, 4), Symbol('skoSINS'), Add(Mul(Integer(2), Symbol('skoS'), Add(Mul(Symbol('skoS'), Add(Symbol('skoS'), Integer(3))), Integer(-3))), Mul(Symbol('skoSINS'), Add(Symbol('skoS'), Integer(1))), Integer(-10)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_3(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (skoS >= 9/20) & (skoS**3 + 3*skoS**2 + 3*skoS > -1)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(9, 20)), StrictGreaterThan(Add(Pow(Symbol('skoS'), Integer(3)), Mul(Integer(3), Pow(Symbol('skoS'), Integer(2))), Mul(Integer(3), Symbol('skoS'))), Integer(-1)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def post_condition(delta:sympy.Rational, skoS:sympy.Rational, skoCOSS:sympy.Rational, skoSINS:sympy.Rational):
	# (0 <= delta) & (9/20 <= skoS) & (skoSINS*(-skoCOSS/2 + skoS*(skoS*(skoS/2 + 3/2) - 3/2) + skoSINS*(skoS/4 + 1/4) - 5/2) > skoCOSS*(-skoCOSS/2 - 3) + skoS*(skoCOSS*(-skoCOSS/2 - 6) + skoS*(-3*skoCOSS - 2*skoS - 6) - 6) - 2)

	post_cond =  And(LessThan(Integer(0), Symbol('delta')), LessThan(Rational(9, 20), Symbol('skoS')), StrictGreaterThan(Mul(Symbol('skoSINS'), Add(Mul(Integer(-1), Rational(1, 2), Symbol('skoCOSS')), Mul(Symbol('skoS'), Add(Mul(Symbol('skoS'), Add(Mul(Rational(1, 2), Symbol('skoS')), Rational(3, 2))), Rational(-3, 2))), Mul(Symbol('skoSINS'), Add(Mul(Rational(1, 4), Symbol('skoS')), Rational(1, 4))), Rational(-5, 2))), Add(Mul(Symbol('skoCOSS'), Add(Mul(Integer(-1), Rational(1, 2), Symbol('skoCOSS')), Integer(-3))), Mul(Symbol('skoS'), Add(Mul(Symbol('skoCOSS'), Add(Mul(Integer(-1), Rational(1, 2), Symbol('skoCOSS')), Integer(-6))), Mul(Symbol('skoS'), Add(Mul(Integer(-1), Integer(3), Symbol('skoCOSS')), Mul(Integer(-1), Integer(2), Symbol('skoS')), Integer(-6))), Integer(-6))), Integer(-2))))

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
		print('skoS = 2')
		print('skoSINS = 1/8')
		print('skoCOSS = -2')
		exit(0)
	
	
	if pre_condition_1(delta=delta,skoS=skoS)==True:
		print("pre_condition_1 SAT")
		print('delta = 0')
		print('skoS = 2')
		print('skoSINS = 1/8')
		print('skoCOSS = -2')
		exit(0)
	
	
	if pre_condition_2(delta=delta,skoS=skoS)==True:
		print("pre_condition_2 SAT")
		print('delta = 0')
		print('skoS = 9/20')
		print('skoSINS = 0')
		print('skoCOSS = 0')
		exit(0)
	
	
	if pre_condition_3(delta=delta,skoS=skoS)==True:
		print("pre_condition_3 SAT")
		print('delta = 0')
		print('skoS = 9/20')
		print('skoSINS = 0')
		print('skoCOSS = 0')
		exit(0)


	print("Weakest pre-condition UNSAT")
	exit(0)
