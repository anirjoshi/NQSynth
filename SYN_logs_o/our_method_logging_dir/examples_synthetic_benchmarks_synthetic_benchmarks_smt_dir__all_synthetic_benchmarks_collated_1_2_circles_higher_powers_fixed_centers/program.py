import sympy
from sympy import *
from NQS.helper_program_cav import get_lambda_val

def pre_condition_0(r1:sympy.Rational,r2:sympy.Rational):
	#(r2 > 0) & (r1 - 1 > 0) & ((r1 - 2 > 0) | (-r1**3 + 3*r1**2*r2 - 28*r1**2 - 3*r1*r2**2 - 68*r1*r2 + 28*r1 + r2**3 + 68*r2 > 0) | (r1**4 - 4*r1**3*r2 - 8*r1**3 + 6*r1**2*r2**2 - 112*r1**2*r2 + 24*r1**2 - 4*r1*r2**3 - 136*r1*r2**2 + 112*r1*r2 - 32*r1 + r2**4 + 136*r2**2 + 16 < 0))

	pre_cond = And(StrictGreaterThan(Symbol('r2'), Integer(0)), StrictGreaterThan(Add(Symbol('r1'), Integer(-1)), Integer(0)), Or(StrictGreaterThan(Add(Symbol('r1'), Integer(-2)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('r1'), Integer(3))), Mul(Integer(3), Pow(Symbol('r1'), Integer(2)), Symbol('r2')), Mul(Integer(-1), Integer(28), Pow(Symbol('r1'), Integer(2))), Mul(Integer(-1), Integer(3), Symbol('r1'), Pow(Symbol('r2'), Integer(2))), Mul(Integer(-1), Integer(68), Symbol('r1'), Symbol('r2')), Mul(Integer(28), Symbol('r1')), Pow(Symbol('r2'), Integer(3)), Mul(Integer(68), Symbol('r2'))), Integer(0)), StrictLessThan(Add(Pow(Symbol('r1'), Integer(4)), Mul(Integer(-1), Integer(4), Pow(Symbol('r1'), Integer(3)), Symbol('r2')), Mul(Integer(-1), Integer(8), Pow(Symbol('r1'), Integer(3))), Mul(Integer(6), Pow(Symbol('r1'), Integer(2)), Pow(Symbol('r2'), Integer(2))), Mul(Integer(-1), Integer(112), Pow(Symbol('r1'), Integer(2)), Symbol('r2')), Mul(Integer(24), Pow(Symbol('r1'), Integer(2))), Mul(Integer(-1), Integer(4), Symbol('r1'), Pow(Symbol('r2'), Integer(3))), Mul(Integer(-1), Integer(136), Symbol('r1'), Pow(Symbol('r2'), Integer(2))), Mul(Integer(112), Symbol('r1'), Symbol('r2')), Mul(Integer(-1), Integer(32), Symbol('r1')), Pow(Symbol('r2'), Integer(4)), Mul(Integer(136), Pow(Symbol('r2'), Integer(2))), Integer(16)), Integer(0))))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1(r1:sympy.Rational,r2:sympy.Rational):
	#(r2 > 0) & (r1 - 1 > 0) & ((r1 - 2 > 0) | (-r1**3 + 3*r1**2*r2 - 28*r1**2 - 3*r1*r2**2 - 68*r1*r2 + 28*r1 + r2**3 + 68*r2 > 0) | (r1**4 - 4*r1**3*r2 - 8*r1**3 + 6*r1**2*r2**2 - 112*r1**2*r2 + 24*r1**2 - 4*r1*r2**3 - 136*r1*r2**2 + 112*r1*r2 - 32*r1 + r2**4 + 136*r2**2 + 16 < 0))

	pre_cond = And(StrictGreaterThan(Symbol('r2'), Integer(0)), StrictGreaterThan(Add(Symbol('r1'), Integer(-1)), Integer(0)), Or(StrictGreaterThan(Add(Symbol('r1'), Integer(-2)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('r1'), Integer(3))), Mul(Integer(3), Pow(Symbol('r1'), Integer(2)), Symbol('r2')), Mul(Integer(-1), Integer(28), Pow(Symbol('r1'), Integer(2))), Mul(Integer(-1), Integer(3), Symbol('r1'), Pow(Symbol('r2'), Integer(2))), Mul(Integer(-1), Integer(68), Symbol('r1'), Symbol('r2')), Mul(Integer(28), Symbol('r1')), Pow(Symbol('r2'), Integer(3)), Mul(Integer(68), Symbol('r2'))), Integer(0)), StrictLessThan(Add(Pow(Symbol('r1'), Integer(4)), Mul(Integer(-1), Integer(4), Pow(Symbol('r1'), Integer(3)), Symbol('r2')), Mul(Integer(-1), Integer(8), Pow(Symbol('r1'), Integer(3))), Mul(Integer(6), Pow(Symbol('r1'), Integer(2)), Pow(Symbol('r2'), Integer(2))), Mul(Integer(-1), Integer(112), Pow(Symbol('r1'), Integer(2)), Symbol('r2')), Mul(Integer(24), Pow(Symbol('r1'), Integer(2))), Mul(Integer(-1), Integer(4), Symbol('r1'), Pow(Symbol('r2'), Integer(3))), Mul(Integer(-1), Integer(136), Symbol('r1'), Pow(Symbol('r2'), Integer(2))), Mul(Integer(112), Symbol('r1'), Symbol('r2')), Mul(Integer(-1), Integer(32), Symbol('r1')), Pow(Symbol('r2'), Integer(4)), Mul(Integer(136), Pow(Symbol('r2'), Integer(2))), Integer(16)), Integer(0))))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def post_condition(r1:sympy.Rational, r2:sympy.Rational, x:sympy.Rational, y:sympy.Rational):
	# (0 > -r2 + x**4 + y**4) & (0 > -r1 + x**4 - 4*x**3 + 6*x**2 - 4*x + y**4 - 4*y**3 + 6*y**2 - 4*y + 2)

	post_cond =  And(StrictGreaterThan(Integer(0), Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('x'), Integer(4)), Pow(Symbol('y'), Integer(4)))), StrictGreaterThan(Integer(0), Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('x'), Integer(4)), Mul(Integer(-1), Integer(4), Pow(Symbol('x'), Integer(3))), Mul(Integer(6), Pow(Symbol('x'), Integer(2))), Mul(Integer(-1), Integer(4), Symbol('x')), Pow(Symbol('y'), Integer(4)), Mul(Integer(-1), Integer(4), Pow(Symbol('y'), Integer(3))), Mul(Integer(6), Pow(Symbol('y'), Integer(2))), Mul(Integer(-1), Integer(4), Symbol('y')), Integer(2))))

	eval = post_cond.subs( { 'r1':r1, 'r2':r2, 'x':x, 'y':y })

	return eval == sympy.logic.boolalg.BooleanTrue



#return post-condition single variable
def return_post_condition_single_var(post_condition, r1:sympy.Rational=None, r2:sympy.Rational=None, x:sympy.Rational=None, y:sympy.Rational=None):
	assert r1!=None
	assert r2!=None


	if x==None:
		assert y!=None
		return lambda x: post_condition(r1=r1, r2=r2, x=x, y=y)

	if y==None:
		assert x!=None
		return lambda y: post_condition(r1=r1, r2=r2, x=x, y=y)


	return post_condition(r1=r1, r2=r2, x=x, y=y)


def get_univariate_poly( r1:sympy.Rational, r2:sympy.Rational, x:sympy.Rational, y:sympy.Rational ):


	post_cond =  And(StrictGreaterThan(Integer(0), Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('x'), Integer(4)), Pow(Symbol('y'), Integer(4)))), StrictGreaterThan(Integer(0), Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('x'), Integer(4)), Mul(Integer(-1), Integer(4), Pow(Symbol('x'), Integer(3))), Mul(Integer(6), Pow(Symbol('x'), Integer(2))), Mul(Integer(-1), Integer(4), Symbol('x')), Pow(Symbol('y'), Integer(4)), Mul(Integer(-1), Integer(4), Pow(Symbol('y'), Integer(3))), Mul(Integer(6), Pow(Symbol('y'), Integer(2))), Mul(Integer(-1), Integer(4), Symbol('y')), Integer(2))))

	eval = post_cond.subs( { 'r1':r1, 'r2':r2, 'x':x, 'y':y })
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
	
	
	if pre_condition_1(r1=r1,r2=r2)==True:
		all_vals = dict()
		all_vals['r1'] = r1
		all_vals['r2'] = r2
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


	print("UNKNOWN")
