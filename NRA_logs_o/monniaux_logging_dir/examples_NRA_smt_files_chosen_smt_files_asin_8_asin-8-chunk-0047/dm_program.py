import sympy
from sympy import *

def pre_condition_0(delta:sympy.Rational,skoX:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (skoX*(skoSM + 4) < 0)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictLessThan(Mul(Symbol('skoX'), Add(Symbol('skoSM'), Integer(4))), Integer(0)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1(delta:sympy.Rational,skoX:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def post_condition(delta:sympy.Rational, skoX:sympy.Rational, pi:sympy.Rational, skoSP:sympy.Rational, skoSM:sympy.Rational):
	# (0 <= delta) & (1 > skoX) & (31415927/10000000 > pi) & (pi > 15707963/5000000) & (skoX > 0) & (skoX*(-skoSM - skoSP - 4) > 0)

	post_cond =  And(LessThan(Integer(0), Symbol('delta')), StrictGreaterThan(Integer(1), Symbol('skoX')), StrictGreaterThan(Rational(31415927, 10000000), Symbol('pi')), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictGreaterThan(Mul(Symbol('skoX'), Add(Mul(Integer(-1), Symbol('skoSM')), Mul(Integer(-1), Symbol('skoSP')), Integer(-4))), Integer(0)))

	eval = post_cond.subs( { 'delta':delta, 'skoX':skoX, 'pi':pi, 'skoSP':skoSP, 'skoSM':skoSM })

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
	
	
	ip_0=int(input("enter integer numerator of pi:\n"))
	ip_1=int(input("enter integer denominator of pi:\n"))
	assert(ip_1!=0), ("Error denominator entered is 0")
	pi=sympy.Rational(ip_0,ip_1)
	
	
	
	
	if pre_condition_0(delta=delta,skoX=skoX,pi=pi)==True:
		print("pre_condition_0 SAT")
		print('delta = 0')
		print('skoX = 1/2')
		print('pi = 26353589/8388608')
		print('skoSM = -5')
		print('skoSP = 0')
		exit(0)
	
	
	if pre_condition_1(delta=delta,skoX=skoX,pi=pi)==True:
		print("pre_condition_1 SAT")
		print('delta = 0')
		print('skoX = 1/2')
		print('pi = 26353589/8388608')
		print('skoSM = -5')
		print('skoSP = 0')
		exit(0)


	print("Weakest pre-condition UNSAT")
	exit(0)
