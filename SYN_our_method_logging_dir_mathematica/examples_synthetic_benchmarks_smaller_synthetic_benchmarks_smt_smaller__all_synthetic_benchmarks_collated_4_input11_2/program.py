import sympy
from sympy import *
from NQS.helper_program_cav import get_lambda_val

def pre_condition_0(c:sympy.Rational,d:sympy.Rational):
	#((c > 0) & (d > 0)) | ((d > 0) & (c + d > 0))

	pre_cond = Or(And(StrictGreaterThan(Symbol('c'), Integer(0)), StrictGreaterThan(Symbol('d'), Integer(0))), And(StrictGreaterThan(Symbol('d'), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Symbol('d')), Integer(0))))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1(c:sympy.Rational,d:sympy.Rational):
	#((c > 0) & (d > 0)) | ((c > 0) & (c - d**2 > 0))

	pre_cond = Or(And(StrictGreaterThan(Symbol('c'), Integer(0)), StrictGreaterThan(Symbol('d'), Integer(0))), And(StrictGreaterThan(Symbol('c'), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('d'), Integer(2)))), Integer(0))))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_2(c:sympy.Rational,d:sympy.Rational):
	#((d > -1/4) & (c + d > -3/16)) | ((c < 1/16) & (c + d > -3/16))

	pre_cond = Or(And(StrictGreaterThan(Symbol('d'), Rational(-1, 4)), StrictGreaterThan(Add(Symbol('c'), Symbol('d')), Rational(-3, 16))), And(StrictLessThan(Symbol('c'), Rational(1, 16)), StrictGreaterThan(Add(Symbol('c'), Symbol('d')), Rational(-3, 16))))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_3(c:sympy.Rational,d:sympy.Rational):
	#((c > -25/256) & (d > 25/256)) | (128*c - 128*d**2 + 25*d > -5775/512) | ((d > 25/256) & Eq(128*c - 128*d**2 + 25*d, -5775/512))

	pre_cond = Or(And(StrictGreaterThan(Symbol('c'), Rational(-25, 256)), StrictGreaterThan(Symbol('d'), Rational(25, 256))), StrictGreaterThan(Add(Mul(Integer(128), Symbol('c')), Mul(Integer(-1), Integer(128), Pow(Symbol('d'), Integer(2))), Mul(Integer(25), Symbol('d'))), Rational(-5775, 512)), And(StrictGreaterThan(Symbol('d'), Rational(25, 256)), Equality(Add(Mul(Integer(128), Symbol('c')), Mul(Integer(-1), Integer(128), Pow(Symbol('d'), Integer(2))), Mul(Integer(25), Symbol('d'))), Rational(-5775, 512))))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_4(c:sympy.Rational,d:sympy.Rational):
	#((d > -1/2) & (c + d > -1/4)) | ((c < 1/4) & (c + d > -1/4))

	pre_cond = Or(And(StrictGreaterThan(Symbol('d'), Rational(-1, 2)), StrictGreaterThan(Add(Symbol('c'), Symbol('d')), Rational(-1, 4))), And(StrictLessThan(Symbol('c'), Rational(1, 4)), StrictGreaterThan(Add(Symbol('c'), Symbol('d')), Rational(-1, 4))))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_5(c:sympy.Rational,d:sympy.Rational):
	#((c > -32761/4194304) & (d > 32761/4194304)) | (2097152*c - 2097152*d**2 + 32761*d > -136336310223/8388608) | ((d > 32761/4194304) & Eq(2097152*c - 2097152*d**2 + 32761*d, -136336310223/8388608))

	pre_cond = Or(And(StrictGreaterThan(Symbol('c'), Rational(-32761, 4194304)), StrictGreaterThan(Symbol('d'), Rational(32761, 4194304))), StrictGreaterThan(Add(Mul(Integer(2097152), Symbol('c')), Mul(Integer(-1), Integer(2097152), Pow(Symbol('d'), Integer(2))), Mul(Integer(32761), Symbol('d'))), Rational(-136336310223, 8388608)), And(StrictGreaterThan(Symbol('d'), Rational(32761, 4194304)), Equality(Add(Mul(Integer(2097152), Symbol('c')), Mul(Integer(-1), Integer(2097152), Pow(Symbol('d'), Integer(2))), Mul(Integer(32761), Symbol('d'))), Rational(-136336310223, 8388608))))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def post_condition(c:sympy.Rational, d:sympy.Rational, x:sympy.Rational, y:sympy.Rational):
	# (0 > -d + x**2 - y) & (0 > -c - x**2 + y**2)

	post_cond =  And(StrictGreaterThan(Integer(0), Add(Mul(Integer(-1), Symbol('d')), Pow(Symbol('x'), Integer(2)), Mul(Integer(-1), Symbol('y')))), StrictGreaterThan(Integer(0), Add(Mul(Integer(-1), Symbol('c')), Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Pow(Symbol('y'), Integer(2)))))

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


	post_cond =  And(StrictGreaterThan(Integer(0), Add(Mul(Integer(-1), Symbol('d')), Pow(Symbol('x'), Integer(2)), Mul(Integer(-1), Symbol('y')))), StrictGreaterThan(Integer(0), Add(Mul(Integer(-1), Symbol('c')), Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Pow(Symbol('y'), Integer(2)))))

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
	
	
	if pre_condition_2(c=c,d=d)==True:
		all_vals = dict()
		all_vals['c'] = c
		all_vals['d'] = d
		all_vals['x'] = Add(Symbol('lambda_var_0'), Rational(5, 16))
		all_vals['y'] = Rational(1, 4)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_2 SAT")

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_3(c=c,d=d)==True:
		all_vals = dict()
		all_vals['c'] = c
		all_vals['d'] = d
		all_vals['x'] = Rational(5, 16)
		all_vals['y'] = Add(Symbol('lambda_var_0'), Rational(1, 4))
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_3 SAT")

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_4(c=c,d=d)==True:
		all_vals = dict()
		all_vals['c'] = c
		all_vals['d'] = d
		all_vals['x'] = Add(Symbol('lambda_var_0'), Rational(-181, 2048))
		all_vals['y'] = Rational(1, 2)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_4 SAT")

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_5(c=c,d=d)==True:
		all_vals = dict()
		all_vals['c'] = c
		all_vals['d'] = d
		all_vals['x'] = Rational(-181, 2048)
		all_vals['y'] = Add(Symbol('lambda_var_0'), Rational(1, 2))
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_5 SAT")

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass


	print("Weakest pre-condition UNSAT")
