import sympy
from sympy import *

def pre_condition_0(r2:sympy.Rational):
	#(y**3 + y > 8577/16384) & (-r2 + y**2 + 1/64 < 0)

	pre_cond = And(StrictGreaterThan(Add(Pow(Symbol('y'), Integer(3)), Symbol('y')), Rational(8577, 16384)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(2)), Rational(1, 64)), Integer(0)))

	eval = pre_cond.subs( { 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1(r2:sympy.Rational):
	#r2 > 65/64

	pre_cond = StrictGreaterThan(Symbol('r2'), Rational(65, 64))

	eval = pre_cond.subs( { 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_2(r2:sympy.Rational):
	#(y**3 + y > 1/2) & (r2 - y**2 > 0)

	pre_cond = And(StrictGreaterThan(Add(Pow(Symbol('y'), Integer(3)), Symbol('y')), Rational(1, 2)), StrictGreaterThan(Add(Symbol('r2'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2)))), Integer(0)))

	eval = pre_cond.subs( { 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_3(r2:sympy.Rational):
	#r2 > 1

	pre_cond = StrictGreaterThan(Symbol('r2'), Integer(1))

	eval = pre_cond.subs( { 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def post_condition(r2:sympy.Rational, x:sympy.Rational, y:sympy.Rational):
	# (0 > -r2 + x**2 + y**2) & (0 > x**4 + 6*x**2 - 4*y**3 - 4*y + 2)

	post_cond =  And(StrictGreaterThan(Integer(0), Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('x'), Integer(2)), Pow(Symbol('y'), Integer(2)))), StrictGreaterThan(Integer(0), Add(Pow(Symbol('x'), Integer(4)), Mul(Integer(6), Pow(Symbol('x'), Integer(2))), Mul(Integer(-1), Integer(4), Pow(Symbol('y'), Integer(3))), Mul(Integer(-1), Integer(4), Symbol('y')), Integer(2))))

	eval = post_cond.subs( { 'r2':r2, 'x':x, 'y':y })

	return eval == sympy.logic.boolalg.BooleanTrue





if __name__=="__main__":
	
	ip_0=int(input("enter integer numerator of r2:\n"))
	ip_1=int(input("enter integer denominator of r2:\n"))
	assert(ip_1!=0), ("Error denominator entered is 0")
	r2=sympy.Rational(ip_0,ip_1)
	
	
	
	
	if pre_condition_0(r2=r2)==True:
		print("pre_condition_0 SAT")
		print('x = 1/8')
		print('y = 1')
		print('r2 = 129/64')
		exit(0)
	
	
	if pre_condition_1(r2=r2)==True:
		print("pre_condition_1 SAT")
		print('x = 1/8')
		print('y = 1')
		print('r2 = 129/64')
		exit(0)
	
	
	if pre_condition_2(r2=r2)==True:
		print("pre_condition_2 SAT")
		print('x = 0')
		print('y = 1')
		print('r2 = 129/128')
		exit(0)
	
	
	if pre_condition_3(r2=r2)==True:
		print("pre_condition_3 SAT")
		print('x = 0')
		print('y = 1')
		print('r2 = 129/128')
		exit(0)


	print("Weakest pre-condition UNSAT")
	exit(0)
