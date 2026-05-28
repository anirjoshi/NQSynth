import sympy
from sympy import *

def pre_condition_0(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (delta >= skoM) & (skoM >= 2) & (skoS >= 2) & (delta >= -skoM) & (delta >= skoSINS**2 - 63/64) & (delta >= 63/64 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('delta'), Symbol('skoM')), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM'))), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-63, 64))), GreaterThan(Symbol('delta'), Add(Rational(63, 64), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (delta >= skoM) & (skoM >= 2) & (delta >= -skoM) & (delta >= skoSINS**2 - 63/64) & (delta >= 63/64 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('delta'), Symbol('skoM')), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM'))), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-63, 64))), GreaterThan(Symbol('delta'), Add(Rational(63, 64), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_2(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (delta >= skoM) & (skoM >= 2) & (skoS >= 2) & (delta >= -skoM) & (delta >= skoSINS**2 - 1) & (delta >= 1 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('delta'), Symbol('skoM')), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('skoS'), Integer(2)), GreaterThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM'))), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(1), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_3(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (delta >= skoM) & (skoM >= 2) & (delta >= -skoM) & (delta >= skoSINS**2 - 1) & (delta >= 1 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('delta'), Symbol('skoM')), GreaterThan(Symbol('skoM'), Integer(2)), GreaterThan(Symbol('delta'), Mul(Integer(-1), Symbol('skoM'))), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(1), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def post_condition(delta:sympy.Rational, skoSINS:sympy.Rational, skoM:sympy.Rational, skoCOSS:sympy.Rational, skoS:sympy.Rational):
	# (0 <= delta) & (2 <= skoM) & (2 <= skoS) & (skoM <= delta) & (-skoM <= delta) & (skoCOSS**2 + skoSINS**2 - 1 <= delta) & (-skoCOSS**2 - skoSINS**2 + 1 <= delta)

	post_cond =  And(LessThan(Integer(0), Symbol('delta')), LessThan(Integer(2), Symbol('skoM')), LessThan(Integer(2), Symbol('skoS')), LessThan(Symbol('skoM'), Symbol('delta')), LessThan(Mul(Integer(-1), Symbol('skoM')), Symbol('delta')), LessThan(Add(Pow(Symbol('skoCOSS'), Integer(2)), Pow(Symbol('skoSINS'), Integer(2)), Integer(-1)), Symbol('delta')), LessThan(Add(Mul(Integer(-1), Pow(Symbol('skoCOSS'), Integer(2))), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(1)), Symbol('delta')))

	eval = post_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM, 'skoCOSS':skoCOSS, 'skoS':skoS })

	return eval == sympy.logic.boolalg.BooleanTrue





if __name__=="__main__":
	
	ip_0=int(input("enter integer numerator of delta:\n"))
	ip_1=int(input("enter integer denominator of delta:\n"))
	assert(ip_1!=0), ("Error denominator entered is 0")
	delta=sympy.Rational(ip_0,ip_1)
	
	
	ip_0=int(input("enter integer numerator of skoSINS:\n"))
	ip_1=int(input("enter integer denominator of skoSINS:\n"))
	assert(ip_1!=0), ("Error denominator entered is 0")
	skoSINS=sympy.Rational(ip_0,ip_1)
	
	
	ip_0=int(input("enter integer numerator of skoM:\n"))
	ip_1=int(input("enter integer denominator of skoM:\n"))
	assert(ip_1!=0), ("Error denominator entered is 0")
	skoM=sympy.Rational(ip_0,ip_1)
	
	
	
	
	if pre_condition_0(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_0 SAT")
		print('delta = 2')
		print('skoM = 2')
		print('skoS = 2')
		print('skoCOSS = 1/8')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_1(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_1 SAT")
		print('delta = 2')
		print('skoM = 2')
		print('skoS = 2')
		print('skoCOSS = 1/8')
		print('skoSINS = 1/2')
		exit(0)
	
	
	if pre_condition_2(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_2 SAT")
		print('delta = 385/128')
		print('skoM = 3')
		print('skoS = 2')
		print('skoCOSS = 0')
		print('skoSINS = 2')
		exit(0)
	
	
	if pre_condition_3(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		print("pre_condition_3 SAT")
		print('delta = 385/128')
		print('skoM = 3')
		print('skoS = 2')
		print('skoCOSS = 0')
		print('skoSINS = 2')
		exit(0)


	print("Weakest pre-condition UNSAT")
	exit(0)
