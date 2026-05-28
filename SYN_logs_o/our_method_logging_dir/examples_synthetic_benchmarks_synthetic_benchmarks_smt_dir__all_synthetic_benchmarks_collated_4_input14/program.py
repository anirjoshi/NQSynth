import sympy
from sympy import *
from NQS.helper_program_cav import get_lambda_val

def pre_condition_0(x:sympy.Rational):
	#x**2 - 7 <= 0

	pre_cond = LessThan(Add(Pow(Symbol('x'), Integer(2)), Integer(-7)), Integer(0))

	eval = pre_cond.subs( { 'x':x })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1(x:sympy.Rational):
	#4*x**2 - 63 <= 0

	pre_cond = LessThan(Add(Mul(Integer(4), Pow(Symbol('x'), Integer(2))), Integer(-63)), Integer(0))

	eval = pre_cond.subs( { 'x':x })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_2(x:sympy.Rational):
	#(x + 4 >= 0) & (x - 4 <= 0)

	pre_cond = And(GreaterThan(Add(Symbol('x'), Integer(4)), Integer(0)), LessThan(Add(Symbol('x'), Integer(-4)), Integer(0)))

	eval = pre_cond.subs( { 'x':x })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_3(x:sympy.Rational):
	#(x + 4 >= 0) & (x - 4 <= 0)

	pre_cond = And(GreaterThan(Add(Symbol('x'), Integer(4)), Integer(0)), LessThan(Add(Symbol('x'), Integer(-4)), Integer(0)))

	eval = pre_cond.subs( { 'x':x })

	if eval==True:
		assert eval!=False
		return True
	return False


def post_condition(x:sympy.Rational, y:sympy.Rational, z:sympy.Rational):
	# 0 >= x**2 + y**2 + z**2 - 16

	post_cond =  GreaterThan(Integer(0), Add(Pow(Symbol('x'), Integer(2)), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Integer(-16)))

	eval = post_cond.subs( { 'x':x, 'y':y, 'z':z })

	return eval == sympy.logic.boolalg.BooleanTrue



#return post-condition single variable
def return_post_condition_single_var(post_condition, x:sympy.Rational=None, y:sympy.Rational=None, z:sympy.Rational=None):
	assert x!=None


	if y==None:
		assert z!=None
		return lambda y: post_condition(x=x, y=y, z=z)

	if z==None:
		assert y!=None
		return lambda z: post_condition(x=x, y=y, z=z)


	return post_condition(x=x, y=y, z=z)


def get_univariate_poly( x:sympy.Rational, y:sympy.Rational, z:sympy.Rational ):


	post_cond =  GreaterThan(Integer(0), Add(Pow(Symbol('x'), Integer(2)), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Integer(-16)))

	eval = post_cond.subs( { 'x':x, 'y':y, 'z':z })
	return eval



if __name__=="__main__":
	
	ip_0=int(input("enter numerator of x:\n"))
	ip_1=int(input("enter denominator of x:\n"))
	assert(ip_1!=0), ("Error denominator entered is 0")
	x=sympy.Rational(ip_0,ip_1)
	
	
	lambda_var_0 = sympy.symbols('lambda_var_0')
	
	
	if pre_condition_0(x=x)==True:
		all_vals = dict()
		all_vals['x'] = x
		all_vals['y'] = Add(Symbol('lambda_var_0'), Rational(1, 2))
		all_vals['z'] = Integer(-3)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_0 SAT")

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("z=", all_vals["z"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_1(x=x)==True:
		all_vals = dict()
		all_vals['x'] = x
		all_vals['y'] = Rational(1, 2)
		all_vals['z'] = Add(Symbol('lambda_var_0'), Integer(-3))
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_1 SAT")

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("z=", all_vals["z"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_2(x=x)==True:
		all_vals = dict()
		all_vals['x'] = x
		all_vals['y'] = Symbol('lambda_var_0')
		all_vals['z'] = Integer(0)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_2 SAT")

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("z=", all_vals["z"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_3(x=x)==True:
		all_vals = dict()
		all_vals['x'] = x
		all_vals['y'] = Integer(0)
		all_vals['z'] = Symbol('lambda_var_0')
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_3 SAT")

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("z=", all_vals["z"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass


	print("Weakest pre-condition UNSAT")
