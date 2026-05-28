import sympy
from sympy import *
from NQS.helper_program_cav import get_lambda_val

def pre_condition_0(r:sympy.Rational):
	#Ne(2*r - 1, 0) & Ne(2*r + 1, 0) & ((2*r - 1 > 0) | (2*r + 1 < 0))

	pre_cond = And(Unequality(Add(Mul(Integer(2), Symbol('r')), Integer(-1)), Integer(0)), Unequality(Add(Mul(Integer(2), Symbol('r')), Integer(1)), Integer(0)), Or(StrictGreaterThan(Add(Mul(Integer(2), Symbol('r')), Integer(-1)), Integer(0)), StrictLessThan(Add(Mul(Integer(2), Symbol('r')), Integer(1)), Integer(0))))

	eval = pre_cond.subs( { 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1(r:sympy.Rational):
	#Ne(8*r - 1, 0) & Ne(8*r + 1, 0) & ((8*r - 1 > 0) | (8*r + 1 < 0))

	pre_cond = And(Unequality(Add(Mul(Integer(8), Symbol('r')), Integer(-1)), Integer(0)), Unequality(Add(Mul(Integer(8), Symbol('r')), Integer(1)), Integer(0)), Or(StrictGreaterThan(Add(Mul(Integer(8), Symbol('r')), Integer(-1)), Integer(0)), StrictLessThan(Add(Mul(Integer(8), Symbol('r')), Integer(1)), Integer(0))))

	eval = pre_cond.subs( { 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_2(r:sympy.Rational):
	#Ne(32*r - 1, 0) & Ne(32*r + 1, 0) & ((32*r - 1 > 0) | (32*r + 1 < 0))

	pre_cond = And(Unequality(Add(Mul(Integer(32), Symbol('r')), Integer(-1)), Integer(0)), Unequality(Add(Mul(Integer(32), Symbol('r')), Integer(1)), Integer(0)), Or(StrictGreaterThan(Add(Mul(Integer(32), Symbol('r')), Integer(-1)), Integer(0)), StrictLessThan(Add(Mul(Integer(32), Symbol('r')), Integer(1)), Integer(0))))

	eval = pre_cond.subs( { 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_3(r:sympy.Rational):
	#Ne(r, 0)

	pre_cond = Unequality(Symbol('r'), Integer(0))

	eval = pre_cond.subs( { 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def post_condition(r:sympy.Rational, x:sympy.Rational, y:sympy.Rational):
	# 0 > -r**2 + x**2 + y**2

	post_cond =  StrictGreaterThan(Integer(0), Add(Mul(Integer(-1), Pow(Symbol('r'), Integer(2))), Pow(Symbol('x'), Integer(2)), Pow(Symbol('y'), Integer(2))))

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


	post_cond =  StrictGreaterThan(Integer(0), Add(Mul(Integer(-1), Pow(Symbol('r'), Integer(2))), Pow(Symbol('x'), Integer(2)), Pow(Symbol('y'), Integer(2))))

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
		all_vals['y'] = Rational(1, 2)
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
		all_vals['y'] = Add(Symbol('lambda_var_0'), Rational(1, 2))
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_1 SAT")

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_2(r=r)==True:
		all_vals = dict()
		all_vals['r'] = r
		all_vals['x'] = Symbol('lambda_var_0')
		all_vals['y'] = Rational(1, 32)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_2 SAT")

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_3(r=r)==True:
		all_vals = dict()
		all_vals['r'] = r
		all_vals['x'] = Integer(0)
		all_vals['y'] = Add(Symbol('lambda_var_0'), Rational(1, 32))
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_3 SAT")

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass


	print("Weakest pre-condition UNSAT")
