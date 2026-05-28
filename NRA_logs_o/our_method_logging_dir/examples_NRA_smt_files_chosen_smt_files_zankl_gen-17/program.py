import sympy
from sympy import *
from NQS.helper_program_cav import get_lambda_val

def pre_condition_0(b:sympy.Rational,delta:sympy.Rational):
	#(b**3 + delta - 3 >= 0) & (-b**3 + delta + 3 >= 0) & ((delta - 2 > 0) | (b**2 - 2*b*delta + delta**2 - delta - 2 <= 0))

	pre_cond = And(GreaterThan(Add(Pow(Symbol('b'), Integer(3)), Symbol('delta'), Integer(-3)), Integer(0)), GreaterThan(Add(Mul(Integer(-1), Pow(Symbol('b'), Integer(3))), Symbol('delta'), Integer(3)), Integer(0)), Or(StrictGreaterThan(Add(Symbol('delta'), Integer(-2)), Integer(0)), LessThan(Add(Pow(Symbol('b'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('b'), Symbol('delta')), Pow(Symbol('delta'), Integer(2)), Mul(Integer(-1), Symbol('delta')), Integer(-2)), Integer(0))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def post_condition(b:sympy.Rational, delta:sympy.Rational, a:sympy.Rational):
	# (0 <= delta) & (-a + b <= delta) & (a - b <= delta) & (a**2 - 2 <= delta) & (b**3 - 3 <= delta) & (2 - a**2 <= delta) & (3 - b**3 <= delta)

	post_cond =  And(LessThan(Integer(0), Symbol('delta')), LessThan(Add(Mul(Integer(-1), Symbol('a')), Symbol('b')), Symbol('delta')), LessThan(Add(Symbol('a'), Mul(Integer(-1), Symbol('b'))), Symbol('delta')), LessThan(Add(Pow(Symbol('a'), Integer(2)), Integer(-2)), Symbol('delta')), LessThan(Add(Pow(Symbol('b'), Integer(3)), Integer(-3)), Symbol('delta')), LessThan(Add(Integer(2), Mul(Integer(-1), Pow(Symbol('a'), Integer(2)))), Symbol('delta')), LessThan(Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3)))), Symbol('delta')))

	eval = post_cond.subs( { 'b':b, 'delta':delta, 'a':a })

	return eval == sympy.logic.boolalg.BooleanTrue



#return post-condition single variable
def return_post_condition_single_var(post_condition, b:sympy.Rational=None, delta:sympy.Rational=None, a:sympy.Rational=None):
	assert b!=None
	assert delta!=None


	if a==None:
		return lambda a: post_condition(b=b, delta=delta, a=a)


	return post_condition(b=b, delta=delta, a=a)


def get_univariate_poly( b:sympy.Rational, delta:sympy.Rational, a:sympy.Rational ):


	post_cond =  And(LessThan(Integer(0), Symbol('delta')), LessThan(Add(Mul(Integer(-1), Symbol('a')), Symbol('b')), Symbol('delta')), LessThan(Add(Symbol('a'), Mul(Integer(-1), Symbol('b'))), Symbol('delta')), LessThan(Add(Pow(Symbol('a'), Integer(2)), Integer(-2)), Symbol('delta')), LessThan(Add(Pow(Symbol('b'), Integer(3)), Integer(-3)), Symbol('delta')), LessThan(Add(Integer(2), Mul(Integer(-1), Pow(Symbol('a'), Integer(2)))), Symbol('delta')), LessThan(Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3)))), Symbol('delta')))

	eval = post_cond.subs( { 'b':b, 'delta':delta, 'a':a })
	return eval



if __name__=="__main__":
	
	ip_0=int(input("enter numerator of b:\n"))
	ip_1=int(input("enter denominator of b:\n"))
	assert(ip_1!=0), ("Error denominator entered is 0")
	b=sympy.Rational(ip_0,ip_1)
	
	
	ip_0=int(input("enter numerator of delta:\n"))
	ip_1=int(input("enter denominator of delta:\n"))
	assert(ip_1!=0), ("Error denominator entered is 0")
	delta=sympy.Rational(ip_0,ip_1)
	
	
	lambda_var_0 = sympy.symbols('lambda_var_0')
	
	
	if pre_condition_0(b=b,delta=delta)==True:
		all_vals = dict()
		all_vals['b'] = b
		all_vals['delta'] = delta
		all_vals['a'] = Add(Symbol('lambda_var_0'), Rational(1, 2))
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_0 SAT")

			print("a=", all_vals["a"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass


	print("Weakest pre-condition UNSAT")
