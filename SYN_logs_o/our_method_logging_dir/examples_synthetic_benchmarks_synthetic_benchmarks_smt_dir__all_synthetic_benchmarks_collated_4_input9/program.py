import sympy
from sympy import *
from NQS.helper_program_cav import get_lambda_val

def pre_condition_0(r1:sympy.Rational,r2:sympy.Rational):
	#(64*r2 - 1 > 0) & Ne(16*r1 - 1, 0) & ((16*r1 - 1 > 0) | (64*r1*r2 - 65*r1 + 4 < 0))

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(64), Symbol('r2')), Integer(-1)), Integer(0)), Unequality(Add(Mul(Integer(16), Symbol('r1')), Integer(-1)), Integer(0)), Or(StrictGreaterThan(Add(Mul(Integer(16), Symbol('r1')), Integer(-1)), Integer(0)), StrictLessThan(Add(Mul(Integer(64), Symbol('r1'), Symbol('r2')), Mul(Integer(-1), Integer(65), Symbol('r1')), Integer(4)), Integer(0))))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 0) & (4*r2 - 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Integer(0)), StrictGreaterThan(Add(Mul(Integer(4), Symbol('r2')), Integer(-1)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_2(r1:sympy.Rational,r2:sympy.Rational):
	#(r2 > 0) & Ne(r1, 0) & ((r1 > 0) | (r2 - 1 > 0))

	pre_cond = And(StrictGreaterThan(Symbol('r2'), Integer(0)), Unequality(Symbol('r1'), Integer(0)), Or(StrictGreaterThan(Symbol('r1'), Integer(0)), StrictGreaterThan(Add(Symbol('r2'), Integer(-1)), Integer(0))))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_3(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 < 0) & (r2 - 4 > 0)

	pre_cond = And(StrictLessThan(Symbol('r1'), Integer(0)), StrictGreaterThan(Add(Symbol('r2'), Integer(-4)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def post_condition(r1:sympy.Rational, r2:sympy.Rational, y:sympy.Rational, x:sympy.Rational):
	# (0 > -r2 + x**2 + y**2) & (0 > r1*y**2 - r1 + 4*x**2)

	post_cond =  And(StrictGreaterThan(Integer(0), Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('x'), Integer(2)), Pow(Symbol('y'), Integer(2)))), StrictGreaterThan(Integer(0), Add(Mul(Symbol('r1'), Pow(Symbol('y'), Integer(2))), Mul(Integer(-1), Symbol('r1')), Mul(Integer(4), Pow(Symbol('x'), Integer(2))))))

	eval = post_cond.subs( { 'r1':r1, 'r2':r2, 'y':y, 'x':x })

	return eval == sympy.logic.boolalg.BooleanTrue



#return post-condition single variable
def return_post_condition_single_var(post_condition, r1:sympy.Rational=None, r2:sympy.Rational=None, y:sympy.Rational=None, x:sympy.Rational=None):
	assert r1!=None
	assert r2!=None


	if y==None:
		assert x!=None
		return lambda y: post_condition(r1=r1, r2=r2, y=y, x=x)

	if x==None:
		assert y!=None
		return lambda x: post_condition(r1=r1, r2=r2, y=y, x=x)


	return post_condition(r1=r1, r2=r2, y=y, x=x)


def get_univariate_poly( r1:sympy.Rational, r2:sympy.Rational, y:sympy.Rational, x:sympy.Rational ):


	post_cond =  And(StrictGreaterThan(Integer(0), Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('x'), Integer(2)), Pow(Symbol('y'), Integer(2)))), StrictGreaterThan(Integer(0), Add(Mul(Symbol('r1'), Pow(Symbol('y'), Integer(2))), Mul(Integer(-1), Symbol('r1')), Mul(Integer(4), Pow(Symbol('x'), Integer(2))))))

	eval = post_cond.subs( { 'r1':r1, 'r2':r2, 'y':y, 'x':x })
	return eval



if __name__=="__main__":
	
	ip_0=int(input("enter numerator of r1:\n"))
	ip_1=int(input("enter denominator of r1:\n"))
	assert(ip_1!=0), ("Error denominator entered is 0")
	r1=sympy.Rational(ip_0,ip_1)
	
	
	ip_0=int(input("enter numerator of r2:\n"))
	ip_1=int(input("enter denominator of r2:\n"))
	assert(ip_1!=0), ("Error denominator entered is 0")
	r2=sympy.Rational(ip_0,ip_1)
	
	
	lambda_var_0 = sympy.symbols('lambda_var_0')
	
	
	if pre_condition_0(r1=r1,r2=r2)==True:
		all_vals = dict()
		all_vals['r1'] = r1
		all_vals['r2'] = r2
		all_vals['y'] = Add(Symbol('lambda_var_0'), Rational(1, 2))
		all_vals['x'] = Rational(1, 8)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_0 SAT")

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_1(r1=r1,r2=r2)==True:
		all_vals = dict()
		all_vals['r1'] = r1
		all_vals['r2'] = r2
		all_vals['y'] = Rational(1, 2)
		all_vals['x'] = Add(Symbol('lambda_var_0'), Rational(1, 8))
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_1 SAT")

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_2(r1=r1,r2=r2)==True:
		all_vals = dict()
		all_vals['r1'] = r1
		all_vals['r2'] = r2
		all_vals['y'] = Add(Symbol('lambda_var_0'), Integer(-2))
		all_vals['x'] = Integer(0)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_2 SAT")

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_3(r1=r1,r2=r2)==True:
		all_vals = dict()
		all_vals['r1'] = r1
		all_vals['r2'] = r2
		all_vals['y'] = Integer(-2)
		all_vals['x'] = Symbol('lambda_var_0')
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_3 SAT")

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass


	print("Weakest pre-condition UNSAT")
