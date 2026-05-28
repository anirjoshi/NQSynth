import sympy
from sympy import *

def pre_condition_0(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**2 > 0) & (b - z**2 > 0) & (-c + y**2 + z**2 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2)))), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2)))), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > 0) & (b - z**2 > 0) & (c - z**2 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2)))), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2)))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_2(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > 0) & (b > 0) & (c > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(0)), StrictGreaterThan(Symbol('b'), Integer(0)), StrictGreaterThan(Symbol('c'), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def post_condition(a:sympy.Rational, b:sympy.Rational, c:sympy.Rational, x:sympy.Rational, y:sympy.Rational, z:sympy.Rational):
	# (0 > -a + x**2 + y**2) & (0 > -b + x**2 + z**2) & (0 > -c + y**2 + z**2)

	post_cond =  And(StrictGreaterThan(Integer(0), Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('x'), Integer(2)), Pow(Symbol('y'), Integer(2)))), StrictGreaterThan(Integer(0), Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('x'), Integer(2)), Pow(Symbol('z'), Integer(2)))), StrictGreaterThan(Integer(0), Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)))))

	eval = post_cond.subs( { 'a':a, 'b':b, 'c':c, 'x':x, 'y':y, 'z':z })

	return eval == sympy.logic.boolalg.BooleanTrue





if __name__=="__main__":
	
	ip_0=int(input("enter integer numerator of a:\n"))
	ip_1=int(input("enter integer denominator of a:\n"))
	assert(ip_1!=0), ("Error denominator entered is 0")
	a=sympy.Rational(ip_0,ip_1)
	
	
	ip_0=int(input("enter integer numerator of b:\n"))
	ip_1=int(input("enter integer denominator of b:\n"))
	assert(ip_1!=0), ("Error denominator entered is 0")
	b=sympy.Rational(ip_0,ip_1)
	
	
	ip_0=int(input("enter integer numerator of c:\n"))
	ip_1=int(input("enter integer denominator of c:\n"))
	assert(ip_1!=0), ("Error denominator entered is 0")
	c=sympy.Rational(ip_0,ip_1)
	
	
	
	
	if pre_condition_0(a=a,b=b,c=c)==True:
		print("pre_condition_0 SAT")
		print('x = 0')
		print('y = 0')
		print('a = 1')
		print('z = 0')
		print('b = 1')
		print('c = 1')
		exit(0)
	
	
	if pre_condition_1(a=a,b=b,c=c)==True:
		print("pre_condition_1 SAT")
		print('x = 0')
		print('y = 0')
		print('a = 1')
		print('z = 0')
		print('b = 1')
		print('c = 1')
		exit(0)
	
	
	if pre_condition_2(a=a,b=b,c=c)==True:
		print("pre_condition_2 SAT")
		print('x = 0')
		print('y = 0')
		print('a = 1')
		print('z = 0')
		print('b = 1')
		print('c = 1')
		exit(0)


	print("Weakest pre-condition UNSAT")
	exit(0)
