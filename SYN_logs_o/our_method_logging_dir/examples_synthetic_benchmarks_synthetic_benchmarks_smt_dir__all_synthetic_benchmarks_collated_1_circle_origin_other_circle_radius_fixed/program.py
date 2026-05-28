import sympy
from sympy import *
from NQS.helper_program_cav import get_lambda_val

def pre_condition_0(r:sympy.Rational):
	#Ne(r - 5, 0) & Ne(r + 5, 0) & ((r - 5 > 0) | (r + 5 < 0))

	pre_cond = And(Unequality(Add(Symbol('r'), Integer(-5)), Integer(0)), Unequality(Add(Symbol('r'), Integer(5)), Integer(0)), Or(StrictGreaterThan(Add(Symbol('r'), Integer(-5)), Integer(0)), StrictLessThan(Add(Symbol('r'), Integer(5)), Integer(0))))

	eval = pre_cond.subs( { 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1(r:sympy.Rational):
	#Ne(r - 5, 0) & Ne(r + 5, 0) & ((r - 5 > 0) | (r + 5 < 0))

	pre_cond = And(Unequality(Add(Symbol('r'), Integer(-5)), Integer(0)), Unequality(Add(Symbol('r'), Integer(5)), Integer(0)), Or(StrictGreaterThan(Add(Symbol('r'), Integer(-5)), Integer(0)), StrictLessThan(Add(Symbol('r'), Integer(5)), Integer(0))))

	eval = pre_cond.subs( { 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def post_condition(r:sympy.Rational, x:sympy.Rational, y:sympy.Rational):
	# (0 > -r**2 + x**2 + y**2) & (0 > -x**2 - y**2 + 25)

	post_cond =  And(StrictGreaterThan(Integer(0), Add(Mul(Integer(-1), Pow(Symbol('r'), Integer(2))), Pow(Symbol('x'), Integer(2)), Pow(Symbol('y'), Integer(2)))), StrictGreaterThan(Integer(0), Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Integer(25))))

	eval = post_cond.subs( { 'r':r, 'x':x, 'y':y })

	return eval == sympy.logic.boolalg.BooleanTrue



#return post-condition single variable
def return_post_condition_single_var(post_condition, r:sympy.Rational=None, x:sympy.Rational=None, y:sympy.Rational=None):
	assert r!=None


	if x==None:
		assert y!=None
		return lambda x: post_condition(r=r, x=x, y=y)

	if y==None:
		assert x!=None
		return lambda y: post_condition(r=r, x=x, y=y)


	return post_condition(r=r, x=x, y=y)


def get_univariate_poly( r:sympy.Rational, x:sympy.Rational, y:sympy.Rational ):


	post_cond =  And(StrictGreaterThan(Integer(0), Add(Mul(Integer(-1), Pow(Symbol('r'), Integer(2))), Pow(Symbol('x'), Integer(2)), Pow(Symbol('y'), Integer(2)))), StrictGreaterThan(Integer(0), Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Integer(25))))

	eval = post_cond.subs( { 'r':r, 'x':x, 'y':y })
	return eval



if __name__=="__main__":
	
	ip_0=int(input("enter numerator of r:\n"))
	ip_1=int(input("enter denominator of r:\n"))
	assert(ip_1!=0), ("Error denominator entered is 0")
	r=sympy.Rational(ip_0,ip_1)
	
	
	lambda_var_0 = sympy.symbols('lambda_var_0')
	
	
	if pre_condition_0(r=r)==True:
		all_vals = dict()
		all_vals['r'] = r
		all_vals['x'] = Add(Symbol('lambda_var_0'), Rational(1, 8))
		all_vals['y'] = Integer(5)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_0 SAT")

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_1(r=r)==True:
		all_vals = dict()
		all_vals['r'] = r
		all_vals['x'] = Rational(1, 8)
		all_vals['y'] = Add(Symbol('lambda_var_0'), Integer(5))
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
