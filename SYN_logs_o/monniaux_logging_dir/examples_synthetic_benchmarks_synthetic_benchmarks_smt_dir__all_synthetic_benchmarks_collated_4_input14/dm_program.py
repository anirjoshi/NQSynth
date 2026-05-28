import sympy
from sympy import *

def pre_condition_0(x:sympy.Rational):
	#x**2 + z**2 - 63/4 <= 0

	pre_cond = LessThan(Add(Pow(Symbol('x'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(-63, 4)), Integer(0))

	eval = pre_cond.subs( { 'x':x })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1(x:sympy.Rational):
	#x**2 <= 27/4

	pre_cond = LessThan(Pow(Symbol('x'), Integer(2)), Rational(27, 4))

	eval = pre_cond.subs( { 'x':x })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_2(x:sympy.Rational):
	#x**2 + z**2 - 255/16 <= 0

	pre_cond = LessThan(Add(Pow(Symbol('x'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(-255, 16)), Integer(0))

	eval = pre_cond.subs( { 'x':x })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_3(x:sympy.Rational):
	#x**2 <= 579/64

	pre_cond = LessThan(Pow(Symbol('x'), Integer(2)), Rational(579, 64))

	eval = pre_cond.subs( { 'x':x })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_4(x:sympy.Rational):
	#x**2 + z**2 - 16 <= 0

	pre_cond = LessThan(Add(Pow(Symbol('x'), Integer(2)), Pow(Symbol('z'), Integer(2)), Integer(-16)), Integer(0))

	eval = pre_cond.subs( { 'x':x })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_5(x:sympy.Rational):
	#x**2 <= 16

	pre_cond = LessThan(Pow(Symbol('x'), Integer(2)), Integer(16))

	eval = pre_cond.subs( { 'x':x })

	if eval==True:
		assert eval!=False
		return True
	return False


def post_condition(x:sympy.Rational, y:sympy.Rational, z:sympy.Rational):
	# 0 >= x**2 + y**2 + z**2 - 16

	post_cond =  GreaterThan(Integer(0), Add(Pow(Symbol('x'), Integer(2)), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Integer(-16)))

	eval = post_cond.subs( { 'x':x, 'y':y, 'z':z })

	return eval == sympy.logic.boolalg.BooleanTrue





if __name__=="__main__":
	
	ip_0=int(input("enter integer numerator of x:\n"))
	ip_1=int(input("enter integer denominator of x:\n"))
	assert(ip_1!=0), ("Error denominator entered is 0")
	x=sympy.Rational(ip_0,ip_1)
	
	
	
	
	if pre_condition_0(x=x)==True:
		print("pre_condition_0 SAT")
		print('x = 1/8')
		print('y = 1/2')
		print('z = -3')
		exit(0)
	
	
	if pre_condition_1(x=x)==True:
		print("pre_condition_1 SAT")
		print('x = 1/8')
		print('y = 1/2')
		print('z = -3')
		exit(0)
	
	
	if pre_condition_2(x=x)==True:
		print("pre_condition_2 SAT")
		print('x = -3')
		print('y = 1/4')
		print('z = 21/8')
		exit(0)
	
	
	if pre_condition_3(x=x)==True:
		print("pre_condition_3 SAT")
		print('x = -3')
		print('y = 1/4')
		print('z = 21/8')
		exit(0)
	
	
	if pre_condition_4(x=x)==True:
		print("pre_condition_4 SAT")
		print('x = -4')
		print('y = 0')
		print('z = 0')
		exit(0)
	
	
	if pre_condition_5(x=x)==True:
		print("pre_condition_5 SAT")
		print('x = -4')
		print('y = 0')
		print('z = 0')
		exit(0)


	print("Weakest pre-condition UNSAT")
	exit(0)
