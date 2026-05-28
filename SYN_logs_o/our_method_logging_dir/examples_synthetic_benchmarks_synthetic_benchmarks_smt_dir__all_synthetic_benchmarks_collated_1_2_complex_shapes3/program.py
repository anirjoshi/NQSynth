import sympy
from sympy import *
from NQS.helper_program_cav import get_lambda_val

def pre_condition_0(a:sympy.Rational,r:sympy.Rational):
	#(r > 0) & (a - 2560 < 0) & ((a + 512 < 0) | (-a**2 - 1024*a + 9437184*r - 262144 > 0))

	pre_cond = And(StrictGreaterThan(Symbol('r'), Integer(0)), StrictLessThan(Add(Symbol('a'), Integer(-2560)), Integer(0)), Or(StrictLessThan(Add(Symbol('a'), Integer(512)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('a'), Integer(2))), Mul(Integer(-1), Integer(1024), Symbol('a')), Mul(Integer(9437184), Symbol('r')), Integer(-262144)), Integer(0))))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1(a:sympy.Rational,r:sympy.Rational):
	#(r > 0) & Ne(a, 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Integer(0)), Unequality(Symbol('a'), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def post_condition(a:sympy.Rational, r:sympy.Rational, x:sympy.Rational, y:sympy.Rational):
	# (0 > x**2 - 1) & (0 > -r + x**2) & (0 > a*y**3 - 6*x + 1)

	post_cond =  And(StrictGreaterThan(Integer(0), Add(Pow(Symbol('x'), Integer(2)), Integer(-1))), StrictGreaterThan(Integer(0), Add(Mul(Integer(-1), Symbol('r')), Pow(Symbol('x'), Integer(2)))), StrictGreaterThan(Integer(0), Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Mul(Integer(-1), Integer(6), Symbol('x')), Integer(1))))

	eval = post_cond.subs( { 'a':a, 'r':r, 'x':x, 'y':y })

	return eval == sympy.logic.boolalg.BooleanTrue



#return post-condition single variable
def return_post_condition_single_var(post_condition, a:sympy.Rational=None, r:sympy.Rational=None, x:sympy.Rational=None, y:sympy.Rational=None):
	assert a!=None
	assert r!=None


	if x==None:
		assert y!=None
		return lambda x: post_condition(a=a, r=r, x=x, y=y)

	if y==None:
		assert x!=None
		return lambda y: post_condition(a=a, r=r, x=x, y=y)


	return post_condition(a=a, r=r, x=x, y=y)


def get_univariate_poly( a:sympy.Rational, r:sympy.Rational, x:sympy.Rational, y:sympy.Rational ):


	post_cond =  And(StrictGreaterThan(Integer(0), Add(Pow(Symbol('x'), Integer(2)), Integer(-1))), StrictGreaterThan(Integer(0), Add(Mul(Integer(-1), Symbol('r')), Pow(Symbol('x'), Integer(2)))), StrictGreaterThan(Integer(0), Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Mul(Integer(-1), Integer(6), Symbol('x')), Integer(1))))

	eval = post_cond.subs( { 'a':a, 'r':r, 'x':x, 'y':y })
	return eval



if __name__=="__main__":
	
	ip_0=int(input("enter numerator of a:\n"))
	ip_1=int(input("enter denominator of a:\n"))
	assert(ip_1!=0), ("Error denominator entered is 0")
	a=sympy.Rational(ip_0,ip_1)
	
	
	ip_0=int(input("enter numerator of r:\n"))
	ip_1=int(input("enter denominator of r:\n"))
	assert(ip_1!=0), ("Error denominator entered is 0")
	r=sympy.Rational(ip_0,ip_1)
	
	
	lambda_var_0 = sympy.symbols('lambda_var_0')
	
	
	if pre_condition_0(a=a,r=r)==True:
		all_vals = dict()
		all_vals['a'] = a
		all_vals['r'] = r
		all_vals['x'] = Symbol('lambda_var_0')
		all_vals['y'] = Rational(1, 8)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_0 SAT")

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_1(a=a,r=r)==True:
		all_vals = dict()
		all_vals['a'] = a
		all_vals['r'] = r
		all_vals['x'] = Integer(0)
		all_vals['y'] = Add(Symbol('lambda_var_0'), Rational(1, 8))
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_1 SAT")

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass


	print("Weakest pre-condition UNSAT")
