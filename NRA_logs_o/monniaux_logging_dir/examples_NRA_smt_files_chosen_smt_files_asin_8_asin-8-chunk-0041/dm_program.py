import sympy
from sympy import *

def pre_condition_0(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (skoX*(8*skoSM + 33)/8 < 0) & (pi*skoS2/8 + pi/16 + 1/160 < skoSM*(20*pi*skoS2 + 10*pi - 1)/20 - 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictLessThan(Mul(Rational(1, 8), Symbol('skoX'), Add(Mul(Integer(8), Symbol('skoSM')), Integer(33))), Integer(0)), StrictLessThan(Add(Mul(Rational(1, 8), Symbol('pi'), Symbol('skoS2')), Mul(Rational(1, 16), Symbol('pi')), Rational(1, 160)), Add(Mul(Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(-1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (6*pi*skoS2 + 3*pi - 1/10 < -pi*skoS2/8 - pi/16 - 1/160)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictLessThan(Add(Mul(Integer(6), Symbol('pi'), Symbol('skoS2')), Mul(Integer(3), Symbol('pi')), Rational(-1, 10)), Add(Mul(Integer(-1), Rational(1, 8), Symbol('pi'), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 16), Symbol('pi')), Rational(-1, 160))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_2(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (skoX*(1 - skoSM) > 0) & (5*pi*skoS2 + 5*pi/2 + 1/4 > -skoSM*(20*pi*skoS2 + 10*pi - 1)/20 + 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Mul(Symbol('skoX'), Add(Integer(1), Mul(Integer(-1), Symbol('skoSM')))), Integer(0)), StrictGreaterThan(Add(Mul(Integer(5), Symbol('pi'), Symbol('skoS2')), Mul(Rational(5, 2), Symbol('pi')), Rational(1, 4)), Add(Mul(Integer(-1), Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_3(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (5*pi*skoS2 + 5*pi/2 + 1/4 > 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Integer(5), Symbol('pi'), Symbol('skoS2')), Mul(Rational(5, 2), Symbol('pi')), Rational(1, 4)), Rational(1, 5)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def post_condition(delta:sympy.Rational, skoX:sympy.Rational, skoS2:sympy.Rational, pi:sympy.Rational, skoSP:sympy.Rational, skoSM:sympy.Rational):
	# (0 <= delta) & (1 > skoX) & (31415927/10000000 > pi) & (pi > 15707963/5000000) & (skoX > 0) & (skoX*(-skoSM - skoSP - 4) > 0) & (skoSP*(-pi*skoS2 - pi/2 - 1/20) > skoSM*(-pi*skoS2 - pi/2 + 1/20) + 1/5)

	post_cond =  And(LessThan(Integer(0), Symbol('delta')), StrictGreaterThan(Integer(1), Symbol('skoX')), StrictGreaterThan(Rational(31415927, 10000000), Symbol('pi')), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictGreaterThan(Mul(Symbol('skoX'), Add(Mul(Integer(-1), Symbol('skoSM')), Mul(Integer(-1), Symbol('skoSP')), Integer(-4))), Integer(0)), StrictGreaterThan(Mul(Symbol('skoSP'), Add(Mul(Integer(-1), Symbol('pi'), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 2), Symbol('pi')), Rational(-1, 20))), Add(Mul(Symbol('skoSM'), Add(Mul(Integer(-1), Symbol('pi'), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 2), Symbol('pi')), Rational(1, 20))), Rational(1, 5))))

	eval = post_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi, 'skoSP':skoSP, 'skoSM':skoSM })

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
	
	
	ip_0=int(input("enter integer numerator of pi:\n"))
	ip_1=int(input("enter integer denominator of pi:\n"))
	assert(ip_1!=0), ("Error denominator entered is 0")
	pi=sympy.Rational(ip_0,ip_1)
	
	
	
	
	if pre_condition_0(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_0 SAT")
		print('delta = 0')
		print('skoX = 1/2')
		print('pi = 26353589/8388608')
		print('skoSM = -6')
		print('skoSP = 1/8')
		print('skoS2 = -2')
		exit(0)
	
	
	if pre_condition_1(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_1 SAT")
		print('delta = 0')
		print('skoX = 1/2')
		print('pi = 26353589/8388608')
		print('skoSM = -6')
		print('skoSP = 1/8')
		print('skoS2 = -2')
		exit(0)
	
	
	if pre_condition_2(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_2 SAT")
		print('delta = 0')
		print('skoX = 1/2')
		print('pi = 26353589/8388608')
		print('skoSM = 0')
		print('skoSP = -5')
		print('skoS2 = 8388608/26353589')
		exit(0)
	
	
	if pre_condition_3(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_3 SAT")
		print('delta = 0')
		print('skoX = 1/2')
		print('pi = 26353589/8388608')
		print('skoSM = 0')
		print('skoSP = -5')
		print('skoS2 = 8388608/26353589')
		exit(0)


	print("Weakest pre-condition UNSAT")
	exit(0)
