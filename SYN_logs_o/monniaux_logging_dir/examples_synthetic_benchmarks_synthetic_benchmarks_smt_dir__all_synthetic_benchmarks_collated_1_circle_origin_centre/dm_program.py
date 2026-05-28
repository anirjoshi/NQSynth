import sympy
from sympy import *

def pre_condition_0(r:sympy.Rational):
	#-r**2 + y**2 + 1/64 < 0

	pre_cond = StrictLessThan(Add(Mul(Integer(-1), Pow(Symbol('r'), Integer(2))), Pow(Symbol('y'), Integer(2)), Rational(1, 64)), Integer(0))

	eval = pre_cond.subs( { 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1(r:sympy.Rational):
	#r**2 > 17/64

	pre_cond = StrictGreaterThan(Pow(Symbol('r'), Integer(2)), Rational(17, 64))

	eval = pre_cond.subs( { 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_2(r:sympy.Rational):
	#r**2 - y**2 > 0

	pre_cond = StrictGreaterThan(Add(Pow(Symbol('r'), Integer(2)), Mul(Integer(-1), Pow(Symbol('y'), Integer(2)))), Integer(0))

	eval = pre_cond.subs( { 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_3(r:sympy.Rational):
	#r**2 > 961/4096

	pre_cond = StrictGreaterThan(Pow(Symbol('r'), Integer(2)), Rational(961, 4096))

	eval = pre_cond.subs( { 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def post_condition(r:sympy.Rational, x:sympy.Rational, y:sympy.Rational):
	# 0 > -r**2 + x**2 + y**2

	post_cond =  StrictGreaterThan(Integer(0), Add(Mul(Integer(-1), Pow(Symbol('r'), Integer(2))), Pow(Symbol('x'), Integer(2)), Pow(Symbol('y'), Integer(2))))

	eval = post_cond.subs( { 'r':r, 'x':x, 'y':y })

	return eval == sympy.logic.boolalg.BooleanTrue





if __name__=="__main__":
	
	ip_0=int(input("enter integer numerator of r:\n"))
	ip_1=int(input("enter integer denominator of r:\n"))
	assert(ip_1!=0), ("Error denominator entered is 0")
	r=sympy.Rational(ip_0,ip_1)
	
	
	
	
	if pre_condition_0(r=r)==True:
		print("pre_condition_0 SAT")
		print('x = 1/8')
		print('y = 1/2')
		print('r = -1')
		exit(0)
	
	
	if pre_condition_1(r=r)==True:
		print("pre_condition_1 SAT")
		print('x = 1/8')
		print('y = 1/2')
		print('r = -1')
		exit(0)
	
	
	if pre_condition_2(r=r)==True:
		print("pre_condition_2 SAT")
		print('x = 0')
		print('y = 31/64')
		print('r = 1/2')
		exit(0)
	
	
	if pre_condition_3(r=r)==True:
		print("pre_condition_3 SAT")
		print('x = 0')
		print('y = 31/64')
		print('r = 1/2')
		exit(0)


	print("Weakest pre-condition UNSAT")
	exit(0)
