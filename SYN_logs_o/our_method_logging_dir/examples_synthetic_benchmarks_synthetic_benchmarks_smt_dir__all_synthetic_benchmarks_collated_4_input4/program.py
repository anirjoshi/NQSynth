import sympy
from sympy import *
from NQS.helper_program_cav import get_lambda_val

def pre_condition_0(c:sympy.Rational,d:sympy.Rational):
	#(d > 0) & (c < 0)

	pre_cond = And(StrictGreaterThan(Symbol('d'), Integer(0)), StrictLessThan(Symbol('c'), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1(c:sympy.Rational,d:sympy.Rational):
	#(d > 0) & (-c + d > 0)

	pre_cond = And(StrictGreaterThan(Symbol('d'), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('c')), Symbol('d')), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def post_condition(c:sympy.Rational, d:sympy.Rational, x:sympy.Rational, y:sympy.Rational):
	# (0 > c + x**2 - y**2) & (0 > -d + x**2 + y**2)

	post_cond =  And(StrictGreaterThan(Integer(0), Add(Symbol('c'), Pow(Symbol('x'), Integer(2)), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))))), StrictGreaterThan(Integer(0), Add(Mul(Integer(-1), Symbol('d')), Pow(Symbol('x'), Integer(2)), Pow(Symbol('y'), Integer(2)))))

	eval = post_cond.subs( { 'c':c, 'd':d, 'x':x, 'y':y })

	return eval == sympy.logic.boolalg.BooleanTrue



#return post-condition single variable
def return_post_condition_single_var(post_condition, c:sympy.Rational=None, d:sympy.Rational=None, x:sympy.Rational=None, y:sympy.Rational=None):
	assert c!=None
	assert d!=None


	if x==None:
		assert y!=None
		return lambda x: post_condition(c=c, d=d, x=x, y=y)

	if y==None:
		assert x!=None
		return lambda y: post_condition(c=c, d=d, x=x, y=y)


	return post_condition(c=c, d=d, x=x, y=y)


def get_univariate_poly( c:sympy.Rational, d:sympy.Rational, x:sympy.Rational, y:sympy.Rational ):


	post_cond =  And(StrictGreaterThan(Integer(0), Add(Symbol('c'), Pow(Symbol('x'), Integer(2)), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))))), StrictGreaterThan(Integer(0), Add(Mul(Integer(-1), Symbol('d')), Pow(Symbol('x'), Integer(2)), Pow(Symbol('y'), Integer(2)))))

	eval = post_cond.subs( { 'c':c, 'd':d, 'x':x, 'y':y })
	return eval



if __name__=="__main__":
	
	ip_0=int(input("enter numerator of c:\n"))
	ip_1=int(input("enter denominator of c:\n"))
	assert(ip_1!=0), ("Error denominator entered is 0")
	c=sympy.Rational(ip_0,ip_1)
	
	
	ip_0=int(input("enter numerator of d:\n"))
	ip_1=int(input("enter denominator of d:\n"))
	assert(ip_1!=0), ("Error denominator entered is 0")
	d=sympy.Rational(ip_0,ip_1)
	
	
	lambda_var_0 = sympy.symbols('lambda_var_0')
	
	
	if pre_condition_0(c=c,d=d)==True:
		all_vals = dict()
		all_vals['c'] = c
		all_vals['d'] = d
		all_vals['x'] = Symbol('lambda_var_0')
		all_vals['y'] = Integer(0)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_0 SAT")

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_1(c=c,d=d)==True:
		all_vals = dict()
		all_vals['c'] = c
		all_vals['d'] = d
		all_vals['x'] = Integer(0)
		all_vals['y'] = Symbol('lambda_var_0')
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
