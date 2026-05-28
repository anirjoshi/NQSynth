import sympy
from sympy import *
from NQS.helper_program_cav import get_lambda_val

def pre_condition_0(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > 0) & (b > 0) & (c > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(0)), StrictGreaterThan(Symbol('b'), Integer(0)), StrictGreaterThan(Symbol('c'), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > 0) & (b > 0) & (c > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(0)), StrictGreaterThan(Symbol('b'), Integer(0)), StrictGreaterThan(Symbol('c'), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_2(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > 0) & (b > 0) & (c > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(0)), StrictGreaterThan(Symbol('b'), Integer(0)), StrictGreaterThan(Symbol('c'), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def post_condition(a:sympy.Rational, b:sympy.Rational, c:sympy.Rational, x:sympy.Rational, y:sympy.Rational, z:sympy.Rational):
	# (0 > -a + x**2 + y**2) & (0 > -b + x**2 + z**2) & (0 > -c + y**2 + z**2)

	post_cond =  And(StrictGreaterThan(Integer(0), Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('x'), Integer(2)), Pow(Symbol('y'), Integer(2)))), StrictGreaterThan(Integer(0), Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('x'), Integer(2)), Pow(Symbol('z'), Integer(2)))), StrictGreaterThan(Integer(0), Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)))))

	eval = post_cond.subs( { 'a':a, 'b':b, 'c':c, 'x':x, 'y':y, 'z':z })

	return eval == sympy.logic.boolalg.BooleanTrue



#return post-condition single variable
def return_post_condition_single_var(post_condition, a:sympy.Rational=None, b:sympy.Rational=None, c:sympy.Rational=None, x:sympy.Rational=None, y:sympy.Rational=None, z:sympy.Rational=None):
	assert a!=None
	assert b!=None
	assert c!=None


	if x==None:
		assert y!=None
		assert z!=None
		return lambda x: post_condition(a=a, b=b, c=c, x=x, y=y, z=z)

	if y==None:
		assert x!=None
		assert z!=None
		return lambda y: post_condition(a=a, b=b, c=c, x=x, y=y, z=z)

	if z==None:
		assert x!=None
		assert y!=None
		return lambda z: post_condition(a=a, b=b, c=c, x=x, y=y, z=z)


	return post_condition(a=a, b=b, c=c, x=x, y=y, z=z)


def get_univariate_poly( a:sympy.Rational, b:sympy.Rational, c:sympy.Rational, x:sympy.Rational, y:sympy.Rational, z:sympy.Rational ):


	post_cond =  And(StrictGreaterThan(Integer(0), Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('x'), Integer(2)), Pow(Symbol('y'), Integer(2)))), StrictGreaterThan(Integer(0), Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('x'), Integer(2)), Pow(Symbol('z'), Integer(2)))), StrictGreaterThan(Integer(0), Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)))))

	eval = post_cond.subs( { 'a':a, 'b':b, 'c':c, 'x':x, 'y':y, 'z':z })
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
	
	
	ip_0=int(input("enter numerator of c:\n"))
	ip_1=int(input("enter denominator of c:\n"))
	assert(ip_1!=0), ("Error denominator entered is 0")
	c=sympy.Rational(ip_0,ip_1)
	
	
	lambda_var_0 = sympy.symbols('lambda_var_0')
	
	
	if pre_condition_0(a=a,b=b,c=c)==True:
		all_vals = dict()
		all_vals['a'] = a
		all_vals['b'] = b
		all_vals['c'] = c
		all_vals['x'] = Symbol('lambda_var_0')
		all_vals['y'] = Integer(0)
		all_vals['z'] = Integer(0)
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
	
	
	if pre_condition_1(a=a,b=b,c=c)==True:
		all_vals = dict()
		all_vals['a'] = a
		all_vals['b'] = b
		all_vals['c'] = c
		all_vals['x'] = Integer(0)
		all_vals['y'] = Symbol('lambda_var_0')
		all_vals['z'] = Integer(0)
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
	
	
	if pre_condition_2(a=a,b=b,c=c)==True:
		all_vals = dict()
		all_vals['a'] = a
		all_vals['b'] = b
		all_vals['c'] = c
		all_vals['x'] = Integer(0)
		all_vals['y'] = Integer(0)
		all_vals['z'] = Symbol('lambda_var_0')
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
