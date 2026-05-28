import sympy
from sympy import *

def pre_condition_0(c:sympy.Rational):
	#(c <= y) & (c**2 - y**2 >= 0)

	pre_cond = And(LessThan(Symbol('c'), Symbol('y')), GreaterThan(Add(Pow(Symbol('c'), Integer(2)), Mul(Integer(-1), Pow(Symbol('y'), Integer(2)))), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1(c:sympy.Rational):
	#(c <= 1/8) & (c**2 >= 1/64)

	pre_cond = And(LessThan(Symbol('c'), Rational(1, 8)), GreaterThan(Pow(Symbol('c'), Integer(2)), Rational(1, 64)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def post_condition(c:sympy.Rational, x:sympy.Rational, y:sympy.Rational):
	# (0 >= c + x**2 - y) & (0 >= -c**2 + x**2 + y**2)

	post_cond =  And(GreaterThan(Integer(0), Add(Symbol('c'), Pow(Symbol('x'), Integer(2)), Mul(Integer(-1), Symbol('y')))), GreaterThan(Integer(0), Add(Mul(Integer(-1), Pow(Symbol('c'), Integer(2))), Pow(Symbol('x'), Integer(2)), Pow(Symbol('y'), Integer(2)))))

	eval = post_cond.subs( { 'c':c, 'x':x, 'y':y })

	return eval == sympy.logic.boolalg.BooleanTrue





if __name__=="__main__":
	
	ip_0=int(input("enter integer numerator of c:\n"))
	ip_1=int(input("enter integer denominator of c:\n"))
	assert(ip_1!=0), ("Error denominator entered is 0")
	c=sympy.Rational(ip_0,ip_1)
	
	
	
	
	if pre_condition_0(c=c)==True:
		print("pre_condition_0 SAT")
		print('c = 1/8')
		print('x = 0')
		print('y = 1/8')
		exit(0)
	
	
	if pre_condition_1(c=c)==True:
		print("pre_condition_1 SAT")
		print('c = 1/8')
		print('x = 0')
		print('y = 1/8')
		exit(0)


	print("Weakest pre-condition UNSAT")
	exit(0)
