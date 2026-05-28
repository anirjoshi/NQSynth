import sympy
from sympy import *
from NQS.helper_program_cav import get_lambda_val

def pre_condition_0(a:sympy.Rational,b:sympy.Rational):
	#(64*a - 17 > 0) & (-a + b < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(64), Symbol('a')), Integer(-17)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Symbol('b')), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1(a:sympy.Rational,b:sympy.Rational):
	#(2*a - 1 > 0) & (-a + b < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(2), Symbol('a')), Integer(-1)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Symbol('b')), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_2(a:sympy.Rational,b:sympy.Rational):
	#(64*a - 17 > 0) & (-a + b < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(64), Symbol('a')), Integer(-17)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Symbol('b')), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_3(a:sympy.Rational,b:sympy.Rational):
	#(4*a - 1 > 0) & (-a + b < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(4), Symbol('a')), Integer(-1)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Symbol('b')), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_4(a:sympy.Rational,b:sympy.Rational):
	#(a > 0) & (-a + b < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Symbol('b')), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_5(a:sympy.Rational,b:sympy.Rational):
	#(4*a - 1 > 0) & (-a + b < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(4), Symbol('a')), Integer(-1)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Symbol('b')), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def post_condition(a:sympy.Rational, b:sympy.Rational, x:sympy.Rational, y:sympy.Rational, z:sympy.Rational):
	# (0 > -a + x**2 + y**2 + z**2) & (0 > b - x**2 - y**2 - z**2) & (0 > -2*a*x - 3*a + x**2 + y**3 - 2*y)

	post_cond =  And(StrictGreaterThan(Integer(0), Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('x'), Integer(2)), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)))), StrictGreaterThan(Integer(0), Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))))), StrictGreaterThan(Integer(0), Add(Mul(Integer(-1), Integer(2), Symbol('a'), Symbol('x')), Mul(Integer(-1), Integer(3), Symbol('a')), Pow(Symbol('x'), Integer(2)), Pow(Symbol('y'), Integer(3)), Mul(Integer(-1), Integer(2), Symbol('y')))))

	eval = post_cond.subs( { 'a':a, 'b':b, 'x':x, 'y':y, 'z':z })

	return eval == sympy.logic.boolalg.BooleanTrue



#return post-condition single variable
def return_post_condition_single_var(post_condition, a:sympy.Rational=None, b:sympy.Rational=None, x:sympy.Rational=None, y:sympy.Rational=None, z:sympy.Rational=None):
	assert a!=None
	assert b!=None


	if x==None:
		assert y!=None
		assert z!=None
		return lambda x: post_condition(a=a, b=b, x=x, y=y, z=z)

	if y==None:
		assert x!=None
		assert z!=None
		return lambda y: post_condition(a=a, b=b, x=x, y=y, z=z)

	if z==None:
		assert x!=None
		assert y!=None
		return lambda z: post_condition(a=a, b=b, x=x, y=y, z=z)


	return post_condition(a=a, b=b, x=x, y=y, z=z)


def get_univariate_poly( a:sympy.Rational, b:sympy.Rational, x:sympy.Rational, y:sympy.Rational, z:sympy.Rational ):


	post_cond =  And(StrictGreaterThan(Integer(0), Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('x'), Integer(2)), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)))), StrictGreaterThan(Integer(0), Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))))), StrictGreaterThan(Integer(0), Add(Mul(Integer(-1), Integer(2), Symbol('a'), Symbol('x')), Mul(Integer(-1), Integer(3), Symbol('a')), Pow(Symbol('x'), Integer(2)), Pow(Symbol('y'), Integer(3)), Mul(Integer(-1), Integer(2), Symbol('y')))))

	eval = post_cond.subs( { 'a':a, 'b':b, 'x':x, 'y':y, 'z':z })
	return eval



if __name__=="__main__":
	
	ip_0=int(input("enter numerator of a:\n"))
	ip_1=int(input("enter denominator of a:\n"))
	assert(ip_1!=0), ("Error denominator entered is 0")
	a=sympy.Rational(ip_0,ip_1)
	
	
	ip_0=int(input("enter numerator of b:\n"))
	ip_1=int(input("enter denominator of b:\n"))
	assert(ip_1!=0), ("Error denominator entered is 0")
	b=sympy.Rational(ip_0,ip_1)
	
	
	lambda_var_0 = sympy.symbols('lambda_var_0')
	
	
	if pre_condition_0(a=a,b=b)==True:
		all_vals = dict()
		all_vals['a'] = a
		all_vals['b'] = b
		all_vals['x'] = Add(Symbol('lambda_var_0'), Rational(1, 2))
		all_vals['y'] = Rational(1, 8)
		all_vals['z'] = Rational(-1, 2)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_0 SAT")

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("z=", all_vals["z"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_1(a=a,b=b)==True:
		all_vals = dict()
		all_vals['a'] = a
		all_vals['b'] = b
		all_vals['x'] = Rational(1, 2)
		all_vals['y'] = Add(Symbol('lambda_var_0'), Rational(1, 8))
		all_vals['z'] = Rational(-1, 2)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_1 SAT")

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("z=", all_vals["z"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_2(a=a,b=b)==True:
		all_vals = dict()
		all_vals['a'] = a
		all_vals['b'] = b
		all_vals['x'] = Rational(1, 2)
		all_vals['y'] = Rational(1, 8)
		all_vals['z'] = Add(Symbol('lambda_var_0'), Rational(-1, 2))
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_2 SAT")

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("z=", all_vals["z"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_3(a=a,b=b)==True:
		all_vals = dict()
		all_vals['a'] = a
		all_vals['b'] = b
		all_vals['x'] = Symbol('lambda_var_0')
		all_vals['y'] = Rational(1, 2)
		all_vals['z'] = Integer(0)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_3 SAT")

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("z=", all_vals["z"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_4(a=a,b=b)==True:
		all_vals = dict()
		all_vals['a'] = a
		all_vals['b'] = b
		all_vals['x'] = Integer(0)
		all_vals['y'] = Add(Symbol('lambda_var_0'), Rational(1, 2))
		all_vals['z'] = Integer(0)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_4 SAT")

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("z=", all_vals["z"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_5(a=a,b=b)==True:
		all_vals = dict()
		all_vals['a'] = a
		all_vals['b'] = b
		all_vals['x'] = Integer(0)
		all_vals['y'] = Rational(1, 2)
		all_vals['z'] = Symbol('lambda_var_0')
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_5 SAT")

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("z=", all_vals["z"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass


	print("Weakest pre-condition UNSAT")
