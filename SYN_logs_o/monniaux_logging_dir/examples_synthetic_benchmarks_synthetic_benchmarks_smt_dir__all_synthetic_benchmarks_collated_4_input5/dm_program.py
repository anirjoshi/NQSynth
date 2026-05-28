import sympy
from sympy import *

def pre_condition_0(c:sympy.Rational,d:sympy.Rational):
	#(d - y**2 > 0) & (c - y**2 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2)))), Integer(0)), StrictLessThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2)))), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1(c:sympy.Rational,d:sympy.Rational):
	#(d > 0) & (c < 0)

	pre_cond = And(StrictGreaterThan(Symbol('d'), Integer(0)), StrictLessThan(Symbol('c'), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def post_condition(c:sympy.Rational, d:sympy.Rational, x:sympy.Rational, y:sympy.Rational):
	# (0 > -d + y**2) & (0 > c + x**2 - y**2)

	post_cond =  And(StrictGreaterThan(Integer(0), Add(Mul(Integer(-1), Symbol('d')), Pow(Symbol('y'), Integer(2)))), StrictGreaterThan(Integer(0), Add(Symbol('c'), Pow(Symbol('x'), Integer(2)), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))))))

	eval = post_cond.subs( { 'c':c, 'd':d, 'x':x, 'y':y })

	return eval == sympy.logic.boolalg.BooleanTrue





if __name__=="__main__":
	
	ip_0=int(input("enter integer numerator of c:\n"))
	ip_1=int(input("enter integer denominator of c:\n"))
	assert(ip_1!=0), ("Error denominator entered is 0")
	c=sympy.Rational(ip_0,ip_1)
	
	
	ip_0=int(input("enter integer numerator of d:\n"))
	ip_1=int(input("enter integer denominator of d:\n"))
	assert(ip_1!=0), ("Error denominator entered is 0")
	d=sympy.Rational(ip_0,ip_1)
	
	
	
	
	if pre_condition_0(c=c,d=d)==True:
		print("pre_condition_0 SAT")
		print('y = 0')
		print('d = 1')
		print('c = -1')
		print('x = 0')
		exit(0)
	
	
	if pre_condition_1(c=c,d=d)==True:
		print("pre_condition_1 SAT")
		print('y = 0')
		print('d = 1')
		print('c = -1')
		print('x = 0')
		exit(0)


	print("Weakest pre-condition UNSAT")
	exit(0)
