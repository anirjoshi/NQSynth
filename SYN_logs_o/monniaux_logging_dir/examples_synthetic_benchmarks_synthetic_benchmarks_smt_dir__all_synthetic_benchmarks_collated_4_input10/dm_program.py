import sympy
from sympy import *

def pre_condition_0(r:sympy.Rational):
	#r - x**2 >= 0

	pre_cond = GreaterThan(Add(Symbol('r'), Mul(Integer(-1), Pow(Symbol('x'), Integer(2)))), Integer(0))

	eval = pre_cond.subs( { 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1(r:sympy.Rational):
	#r >= 0

	pre_cond = GreaterThan(Symbol('r'), Integer(0))

	eval = pre_cond.subs( { 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def post_condition(r:sympy.Rational, y:sympy.Rational, x:sympy.Rational):
	# 0 >= -r + x**2 + y**2

	post_cond =  GreaterThan(Integer(0), Add(Mul(Integer(-1), Symbol('r')), Pow(Symbol('x'), Integer(2)), Pow(Symbol('y'), Integer(2))))

	eval = post_cond.subs( { 'r':r, 'y':y, 'x':x })

	return eval == sympy.logic.boolalg.BooleanTrue





if __name__=="__main__":
	
	ip_0=int(input("enter integer numerator of r:\n"))
	ip_1=int(input("enter integer denominator of r:\n"))
	assert(ip_1!=0), ("Error denominator entered is 0")
	r=sympy.Rational(ip_0,ip_1)
	
	
	
	
	if pre_condition_0(r=r)==True:
		print("pre_condition_0 SAT")
		print('x = 0')
		print('y = 0')
		print('r = 0')
		exit(0)
	
	
	if pre_condition_1(r=r)==True:
		print("pre_condition_1 SAT")
		print('x = 0')
		print('y = 0')
		print('r = 0')
		exit(0)


	print("Weakest pre-condition UNSAT")
	exit(0)
