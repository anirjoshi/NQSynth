import sympy
from sympy import *
from NQS.helper_program_cav import get_lambda_val

def pre_condition_0(a:sympy.Rational):
	#(65*a - 64 < 0) & (512*a**2 + 1536*a + 127 > 0) & ((2*a + 3 > 0) | (212992*a**3 + 635712*a**2 - 316624*a + 29645 < 0))

	pre_cond = And(StrictLessThan(Add(Mul(Integer(65), Symbol('a')), Integer(-64)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(512), Pow(Symbol('a'), Integer(2))), Mul(Integer(1536), Symbol('a')), Integer(127)), Integer(0)), Or(StrictGreaterThan(Add(Mul(Integer(2), Symbol('a')), Integer(3)), Integer(0)), StrictLessThan(Add(Mul(Integer(212992), Pow(Symbol('a'), Integer(3))), Mul(Integer(635712), Pow(Symbol('a'), Integer(2))), Mul(Integer(-1), Integer(316624), Symbol('a')), Integer(29645)), Integer(0))))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1(a:sympy.Rational):
	#4*a - 3 < 0

	pre_cond = StrictLessThan(Add(Mul(Integer(4), Symbol('a')), Integer(-3)), Integer(0))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_2(a:sympy.Rational):
	#2048*a - 1 > 0

	pre_cond = StrictGreaterThan(Add(Mul(Integer(2048), Symbol('a')), Integer(-1)), Integer(0))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def post_condition(a:sympy.Rational, x:sympy.Rational, y:sympy.Rational, z:sympy.Rational):
	# (0 > a*y**2 + a + x**2 - z**2) & (0 > -2*a*x - 3*a + x**2 + y**3 - 2*y)

	post_cond =  And(StrictGreaterThan(Integer(0), Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(2))), Symbol('a'), Pow(Symbol('x'), Integer(2)), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))))), StrictGreaterThan(Integer(0), Add(Mul(Integer(-1), Integer(2), Symbol('a'), Symbol('x')), Mul(Integer(-1), Integer(3), Symbol('a')), Pow(Symbol('x'), Integer(2)), Pow(Symbol('y'), Integer(3)), Mul(Integer(-1), Integer(2), Symbol('y')))))

	eval = post_cond.subs( { 'a':a, 'x':x, 'y':y, 'z':z })

	return eval == sympy.logic.boolalg.BooleanTrue



#return post-condition single variable
def return_post_condition_single_var(post_condition, a:sympy.Rational=None, x:sympy.Rational=None, y:sympy.Rational=None, z:sympy.Rational=None):
	assert a!=None


	if x==None:
		assert y!=None
		assert z!=None
		return lambda x: post_condition(a=a, x=x, y=y, z=z)

	if y==None:
		assert x!=None
		assert z!=None
		return lambda y: post_condition(a=a, x=x, y=y, z=z)

	if z==None:
		assert x!=None
		assert y!=None
		return lambda z: post_condition(a=a, x=x, y=y, z=z)


	return post_condition(a=a, x=x, y=y, z=z)


def get_univariate_poly( a:sympy.Rational, x:sympy.Rational, y:sympy.Rational, z:sympy.Rational ):


	post_cond =  And(StrictGreaterThan(Integer(0), Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(2))), Symbol('a'), Pow(Symbol('x'), Integer(2)), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))))), StrictGreaterThan(Integer(0), Add(Mul(Integer(-1), Integer(2), Symbol('a'), Symbol('x')), Mul(Integer(-1), Integer(3), Symbol('a')), Pow(Symbol('x'), Integer(2)), Pow(Symbol('y'), Integer(3)), Mul(Integer(-1), Integer(2), Symbol('y')))))

	eval = post_cond.subs( { 'a':a, 'x':x, 'y':y, 'z':z })
	return eval



if __name__=="__main__":
	
	ip_0=int(input("enter numerator of a:\n"))
	ip_1=int(input("enter denominator of a:\n"))
	assert(ip_1!=0), ("Error denominator entered is 0")
	a=sympy.Rational(ip_0,ip_1)
	
	
	lambda_var_0 = sympy.symbols('lambda_var_0')
	
	
	if pre_condition_0(a=a)==True:
		all_vals = dict()
		all_vals['a'] = a
		all_vals['x'] = Add(Symbol('lambda_var_0'), Rational(1, 2))
		all_vals['y'] = Rational(1, 8)
		all_vals['z'] = Integer(1)
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
	
	
	if pre_condition_1(a=a)==True:
		all_vals = dict()
		all_vals['a'] = a
		all_vals['x'] = Rational(1, 2)
		all_vals['y'] = Add(Symbol('lambda_var_0'), Rational(1, 8))
		all_vals['z'] = Integer(1)
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
	
	
	if pre_condition_2(a=a)==True:
		all_vals = dict()
		all_vals['a'] = a
		all_vals['x'] = Rational(1, 2)
		all_vals['y'] = Rational(1, 8)
		all_vals['z'] = Add(Symbol('lambda_var_0'), Integer(1))
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


	print("Weakest pre-condition UNSAT")
