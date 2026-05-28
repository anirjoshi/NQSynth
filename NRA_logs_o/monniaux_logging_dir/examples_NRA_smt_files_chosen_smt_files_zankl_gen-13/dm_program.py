import sympy
from sympy import *

def pre_condition_0(delta:sympy.Rational):
	#delta >= 129/64

	pre_cond = GreaterThan(Symbol('delta'), Rational(129, 64))

	eval = pre_cond.subs( { 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1(delta:sympy.Rational):
	#delta >= 2

	pre_cond = GreaterThan(Symbol('delta'), Integer(2))

	eval = pre_cond.subs( { 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def post_condition(delta:sympy.Rational, a:sympy.Rational):
	# (0 <= delta) & (a**2 + 2 <= delta) & (-a**2 - 2 <= delta)

	post_cond =  And(LessThan(Integer(0), Symbol('delta')), LessThan(Add(Pow(Symbol('a'), Integer(2)), Integer(2)), Symbol('delta')), LessThan(Add(Mul(Integer(-1), Pow(Symbol('a'), Integer(2))), Integer(-2)), Symbol('delta')))

	eval = post_cond.subs( { 'delta':delta, 'a':a })

	return eval == sympy.logic.boolalg.BooleanTrue





if __name__=="__main__":
	
	ip_0=int(input("enter integer numerator of delta:\n"))
	ip_1=int(input("enter integer denominator of delta:\n"))
	assert(ip_1!=0), ("Error denominator entered is 0")
	delta=sympy.Rational(ip_0,ip_1)
	
	
	
	
	if pre_condition_0(delta=delta)==True:
		print("pre_condition_0 SAT")
		print('delta = 4')
		print('a = 1/8')
		exit(0)
	
	
	if pre_condition_1(delta=delta)==True:
		print("pre_condition_1 SAT")
		print('delta = 2')
		print('a = 0')
		exit(0)


	print("Weakest pre-condition UNSAT")
	exit(0)
