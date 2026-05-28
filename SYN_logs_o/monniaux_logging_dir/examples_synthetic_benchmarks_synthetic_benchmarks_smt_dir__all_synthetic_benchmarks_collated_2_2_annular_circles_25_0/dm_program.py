import sympy
from sympy import *

def pre_condition_0(y:sympy.Rational):
	#(y >= -sqrt(1599)/8) & (y <= sqrt(1599)/8)

	pre_cond = And(GreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 8), Pow(Integer(1599), Rational(1, 2)))), LessThan(Symbol('y'), Mul(Rational(1, 8), Pow(Integer(1599), Rational(1, 2)))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1(y:sympy.Rational):
	#(y >= -5) & (y <= 5)

	pre_cond = And(GreaterThan(Symbol('y'), Integer(-5)), LessThan(Symbol('y'), Integer(5)))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def post_condition(y:sympy.Rational, x:sympy.Rational):
	# (0 >= x**2 + y**2 - 25) & (0 >= -x**2 - y**2)

	post_cond =  And(GreaterThan(Integer(0), Add(Pow(Symbol('x'), Integer(2)), Pow(Symbol('y'), Integer(2)), Integer(-25))), GreaterThan(Integer(0), Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))))))

	eval = post_cond.subs( { 'y':y, 'x':x })

	return eval == sympy.logic.boolalg.BooleanTrue





if __name__=="__main__":
	
	ip_0=int(input("enter integer numerator of y:\n"))
	ip_1=int(input("enter integer denominator of y:\n"))
	assert(ip_1!=0), ("Error denominator entered is 0")
	y=sympy.Rational(ip_0,ip_1)
	
	
	
	
	if pre_condition_0(y=y)==True:
		print("pre_condition_0 SAT")
		print('x = 1/8')
		print('y = -4')
		exit(0)
	
	
	if pre_condition_1(y=y)==True:
		print("pre_condition_1 SAT")
		print('x = 0')
		print('y = -5119/1024')
		exit(0)


	print("Weakest pre-condition UNSAT")
	exit(0)
