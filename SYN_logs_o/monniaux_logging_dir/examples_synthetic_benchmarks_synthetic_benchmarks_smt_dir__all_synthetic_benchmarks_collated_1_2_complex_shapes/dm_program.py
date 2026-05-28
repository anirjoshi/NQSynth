import sympy
from sympy import *

def pre_condition_0(a:sympy.Rational,r:sympy.Rational):
	#(-r + x**4 + 1/16 < 0) & (2*a**4 - 20*a**3*x + 3*a**2/2 - 260*a*x**3 + 90*a*x**2 - r + 257*x**4 + 126*x**3 + 51*x**2/2 - 23/8 < 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(-1), Symbol('r')), Pow(Symbol('x'), Integer(4)), Rational(1, 16)), Integer(0)), StrictLessThan(Add(Mul(Integer(2), Pow(Symbol('a'), Integer(4))), Mul(Integer(-1), Integer(20), Pow(Symbol('a'), Integer(3)), Symbol('x')), Mul(Rational(3, 2), Pow(Symbol('a'), Integer(2))), Mul(Integer(-1), Integer(260), Symbol('a'), Pow(Symbol('x'), Integer(3))), Mul(Integer(90), Symbol('a'), Pow(Symbol('x'), Integer(2))), Mul(Integer(-1), Symbol('r')), Mul(Integer(257), Pow(Symbol('x'), Integer(4))), Mul(Integer(126), Pow(Symbol('x'), Integer(3))), Mul(Rational(51, 2), Pow(Symbol('x'), Integer(2))), Rational(-23, 8)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1(a:sympy.Rational,r:sympy.Rational):
	#(r > 257/4096) & (2*a**4 - 5*a**3/2 + 3*a**2/2 + 115*a/128 - r - 8879/4096 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(257, 4096)), StrictLessThan(Add(Mul(Integer(2), Pow(Symbol('a'), Integer(4))), Mul(Integer(-1), Rational(5, 2), Pow(Symbol('a'), Integer(3))), Mul(Rational(3, 2), Pow(Symbol('a'), Integer(2))), Mul(Rational(115, 128), Symbol('a')), Mul(Integer(-1), Symbol('r')), Rational(-8879, 4096)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_2(a:sympy.Rational,r:sympy.Rational):
	#(r - x**4 > 0) & (-2*a**4 + 20*a**3*x + 260*a*x**3 + r - 257*x**4 + 3 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('r'), Mul(Integer(-1), Pow(Symbol('x'), Integer(4)))), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Integer(2), Pow(Symbol('a'), Integer(4))), Mul(Integer(20), Pow(Symbol('a'), Integer(3)), Symbol('x')), Mul(Integer(260), Symbol('a'), Pow(Symbol('x'), Integer(3))), Symbol('r'), Mul(Integer(-1), Integer(257), Pow(Symbol('x'), Integer(4))), Integer(3)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_3(a:sympy.Rational,r:sympy.Rational):
	#(r > 16) & (2*a**4 + 40*a**3 + 2080*a - r + 4109 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Integer(16)), StrictLessThan(Add(Mul(Integer(2), Pow(Symbol('a'), Integer(4))), Mul(Integer(40), Pow(Symbol('a'), Integer(3))), Mul(Integer(2080), Symbol('a')), Mul(Integer(-1), Symbol('r')), Integer(4109)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_4(a:sympy.Rational,r:sympy.Rational):
	#(-r + x**4 + 1/256 < 0) & (2*a**4 - 20*a**3*x + 3*a**2/8 - 260*a*x**3 + 45*a*x**2 - r + 257*x**4 + 63*x**3 + 51*x**2/8 - 383/128 < 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(-1), Symbol('r')), Pow(Symbol('x'), Integer(4)), Rational(1, 256)), Integer(0)), StrictLessThan(Add(Mul(Integer(2), Pow(Symbol('a'), Integer(4))), Mul(Integer(-1), Integer(20), Pow(Symbol('a'), Integer(3)), Symbol('x')), Mul(Rational(3, 8), Pow(Symbol('a'), Integer(2))), Mul(Integer(-1), Integer(260), Symbol('a'), Pow(Symbol('x'), Integer(3))), Mul(Integer(45), Symbol('a'), Pow(Symbol('x'), Integer(2))), Mul(Integer(-1), Symbol('r')), Mul(Integer(257), Pow(Symbol('x'), Integer(4))), Mul(Integer(63), Pow(Symbol('x'), Integer(3))), Mul(Rational(51, 8), Pow(Symbol('x'), Integer(2))), Rational(-383, 128)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_5(a:sympy.Rational,r:sympy.Rational):
	#(r > 257/256) & (2*a**4 + 20*a**3 + 3*a**2/8 + 305*a - r + 25265/128 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(257, 256)), StrictLessThan(Add(Mul(Integer(2), Pow(Symbol('a'), Integer(4))), Mul(Integer(20), Pow(Symbol('a'), Integer(3))), Mul(Rational(3, 8), Pow(Symbol('a'), Integer(2))), Mul(Integer(305), Symbol('a')), Mul(Integer(-1), Symbol('r')), Rational(25265, 128)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def post_condition(a:sympy.Rational, r:sympy.Rational, y:sympy.Rational, x:sympy.Rational):
	# (0 > -r + x**4 + y**4) & (0 > 2*a**4 - 20*a**3*x + 6*a**2*y**2 - 260*a*x**3 + 180*a*x**2*y - r + 257*x**4 + 252*x**3*y + 102*x**2*y**2 + 2*y**4 - 3)

	post_cond =  And(StrictGreaterThan(Integer(0), Add(Mul(Integer(-1), Symbol('r')), Pow(Symbol('x'), Integer(4)), Pow(Symbol('y'), Integer(4)))), StrictGreaterThan(Integer(0), Add(Mul(Integer(2), Pow(Symbol('a'), Integer(4))), Mul(Integer(-1), Integer(20), Pow(Symbol('a'), Integer(3)), Symbol('x')), Mul(Integer(6), Pow(Symbol('a'), Integer(2)), Pow(Symbol('y'), Integer(2))), Mul(Integer(-1), Integer(260), Symbol('a'), Pow(Symbol('x'), Integer(3))), Mul(Integer(180), Symbol('a'), Pow(Symbol('x'), Integer(2)), Symbol('y')), Mul(Integer(-1), Symbol('r')), Mul(Integer(257), Pow(Symbol('x'), Integer(4))), Mul(Integer(252), Pow(Symbol('x'), Integer(3)), Symbol('y')), Mul(Integer(102), Pow(Symbol('x'), Integer(2)), Pow(Symbol('y'), Integer(2))), Mul(Integer(2), Pow(Symbol('y'), Integer(4))), Integer(-3))))

	eval = post_cond.subs( { 'a':a, 'r':r, 'y':y, 'x':x })

	return eval == sympy.logic.boolalg.BooleanTrue





if __name__=="__main__":
	
	ip_0=int(input("enter integer numerator of a:\n"))
	ip_1=int(input("enter integer denominator of a:\n"))
	assert(ip_1!=0), ("Error denominator entered is 0")
	a=sympy.Rational(ip_0,ip_1)
	
	
	ip_0=int(input("enter integer numerator of r:\n"))
	ip_1=int(input("enter integer denominator of r:\n"))
	assert(ip_1!=0), ("Error denominator entered is 0")
	r=sympy.Rational(ip_0,ip_1)
	
	
	
	
	if pre_condition_0(a=a,r=r)==True:
		print("pre_condition_0 SAT")
		print('x = 1/8')
		print('y = 1/2')
		print('r = 2')
		print('a = -1/2')
		exit(0)
	
	
	if pre_condition_1(a=a,r=r)==True:
		print("pre_condition_1 SAT")
		print('x = 1/8')
		print('y = 1/2')
		print('r = 2')
		print('a = -1/2')
		exit(0)
	
	
	if pre_condition_2(a=a,r=r)==True:
		print("pre_condition_2 SAT")
		print('x = -2')
		print('y = 0')
		print('r = 513/32')
		print('a = -2')
		exit(0)
	
	
	if pre_condition_3(a=a,r=r)==True:
		print("pre_condition_3 SAT")
		print('x = -2')
		print('y = 0')
		print('r = 513/32')
		print('a = -2')
		exit(0)
	
	
	if pre_condition_4(a=a,r=r)==True:
		print("pre_condition_4 SAT")
		print('x = -1')
		print('y = 1/4')
		print('r = 33/32')
		print('a = -7/8')
		exit(0)
	
	
	if pre_condition_5(a=a,r=r)==True:
		print("pre_condition_5 SAT")
		print('x = -1')
		print('y = 1/4')
		print('r = 33/32')
		print('a = -7/8')
		exit(0)


	print("UNKNOWN")
	exit(0)
