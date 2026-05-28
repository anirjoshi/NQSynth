import sympy
from sympy import *

def pre_condition_0(x:sympy.Rational):
	#(x <= 1) & (x >= -3**(1/4))

	pre_cond = And(LessThan(Symbol('x'), Integer(1)), GreaterThan(Symbol('x'), Mul(Integer(-1), Pow(Integer(3), Rational(1, 4)))))

	eval = pre_cond.subs( { 'x':x })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1(x:sympy.Rational):
	#Abs(x) <= 2**(1/4)

	pre_cond = LessThan(Abs(Symbol('x')), Pow(Integer(2), Rational(1, 4)))

	eval = pre_cond.subs( { 'x':x })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_2(x:sympy.Rational):
	#Abs(x) <= 1149**(1/4)*2**(3/4)/8

	pre_cond = LessThan(Abs(Symbol('x')), Mul(Rational(1, 8), Pow(Integer(1149), Rational(1, 4)), Pow(Integer(2), Rational(3, 4))))

	eval = pre_cond.subs( { 'x':x })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_3(x:sympy.Rational):
	#Abs(x) <= 2**(3/4)*4725745**(1/4)/64

	pre_cond = LessThan(Abs(Symbol('x')), Mul(Rational(1, 64), Pow(Integer(2), Rational(3, 4)), Pow(Integer(4725745), Rational(1, 4))))

	eval = pre_cond.subs( { 'x':x })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_4(x:sympy.Rational):
	#(x >= -154873375329**(1/4)/512) & (x <= 154873375329**(1/4)/512)

	pre_cond = And(GreaterThan(Symbol('x'), Mul(Integer(-1), Rational(1, 512), Pow(Integer(154873375329), Rational(1, 4)))), LessThan(Symbol('x'), Mul(Rational(1, 512), Pow(Integer(154873375329), Rational(1, 4)))))

	eval = pre_cond.subs( { 'x':x })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_5(x:sympy.Rational):
	#(x <= 8686259432229000019711**(1/3)/16777216) & (x >= -sqrt(2)*40599208722942145**(1/4)/16384)

	pre_cond = And(LessThan(Symbol('x'), Mul(Rational(1, 16777216), Pow(Integer(8686259432229000019711), Rational(1, 3)))), GreaterThan(Symbol('x'), Mul(Integer(-1), Rational(1, 16384), Pow(Integer(2), Rational(1, 2)), Pow(Integer(40599208722942145), Rational(1, 4)))))

	eval = pre_cond.subs( { 'x':x })

	if eval==True:
		assert eval!=False
		return True
	return False


def post_condition(x:sympy.Rational, y:sympy.Rational):
	# (0 >= x**2 + y**2 - 8) & (0 >= x**3 + y**4 - 2) & (0 >= x**4 + y**3 - 2)

	post_cond =  And(GreaterThan(Integer(0), Add(Pow(Symbol('x'), Integer(2)), Pow(Symbol('y'), Integer(2)), Integer(-8))), GreaterThan(Integer(0), Add(Pow(Symbol('x'), Integer(3)), Pow(Symbol('y'), Integer(4)), Integer(-2))), GreaterThan(Integer(0), Add(Pow(Symbol('x'), Integer(4)), Pow(Symbol('y'), Integer(3)), Integer(-2))))

	eval = post_cond.subs( { 'x':x, 'y':y })

	return eval == sympy.logic.boolalg.BooleanTrue





if __name__=="__main__":
	
	ip_0=int(input("enter integer numerator of x:\n"))
	ip_1=int(input("enter integer denominator of x:\n"))
	assert(ip_1!=0), ("Error denominator entered is 0")
	x=sympy.Rational(ip_0,ip_1)
	
	
	
	
	if pre_condition_0(x=x)==True:
		print("pre_condition_0 SAT")
		print('x = 1/8')
		print('y = -1')
		exit(0)
	
	
	if pre_condition_1(x=x)==True:
		print("pre_condition_1 SAT")
		print('x = 9/8')
		print('y = 0')
		exit(0)
	
	
	if pre_condition_2(x=x)==True:
		print("pre_condition_2 SAT")
		print('x = 39/32')
		print('y = -5/8')
		exit(0)
	
	
	if pre_condition_3(x=x)==True:
		print("pre_condition_3 SAT")
		print('x = 627/512')
		print('y = -81/128')
		exit(0)
	
	
	if pre_condition_4(x=x)==True:
		print("pre_condition_4 SAT")
		print('x = 10037/8192')
		print('y = -2593/4096')
		exit(0)
	
	
	if pre_condition_5(x=x)==True:
		print("pre_condition_5 SAT")
		print('x = 2569533/2097152')
		print('y = -165953/262144')
		exit(0)


	print("Weakest pre-condition UNSAT")
	exit(0)
