import sympy
from sympy import *
from NQS.helper_program_cav import get_lambda_val

def pre_condition_0(a:sympy.Rational,b:sympy.Rational,r:sympy.Rational):
	#Ne(b, 0) & Ne(2*a - 1, 0) & Ne(2*a + 1, 0) & Ne(2*r - 19, 0) & Ne(2*r + 19, 0) & (((2*r - 19 > 0) & (4*a**2*b**2 - 400*a**2 - b**2 > 0)) | ((2*r + 19 < 0) & (4*a**2*b**2 - 400*a**2 - b**2 > 0)) | ((2*a - 1 > 0) & (-4*a**2*b**2 + 4*a**2*r**2 - 761*a**2 + b**2 > 0)) | ((2*a + 1 < 0) & (-4*a**2*b**2 + 4*a**2*r**2 - 761*a**2 + b**2 > 0)) | (16*a**4*b**4 - 32*a**4*b**2*r**2 - 312*a**4*b**2 + 16*a**4*r**4 - 6088*a**4*r**2 + 579121*a**4 - 8*a**2*b**4 + 8*a**2*b**2*r**2 + 78*a**2*b**2 + b**4 < 0))

	pre_cond = And(Unequality(Symbol('b'), Integer(0)), Unequality(Add(Mul(Integer(2), Symbol('a')), Integer(-1)), Integer(0)), Unequality(Add(Mul(Integer(2), Symbol('a')), Integer(1)), Integer(0)), Unequality(Add(Mul(Integer(2), Symbol('r')), Integer(-19)), Integer(0)), Unequality(Add(Mul(Integer(2), Symbol('r')), Integer(19)), Integer(0)), Or(And(StrictGreaterThan(Add(Mul(Integer(2), Symbol('r')), Integer(-19)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(4), Pow(Symbol('a'), Integer(2)), Pow(Symbol('b'), Integer(2))), Mul(Integer(-1), Integer(400), Pow(Symbol('a'), Integer(2))), Mul(Integer(-1), Pow(Symbol('b'), Integer(2)))), Integer(0))), And(StrictLessThan(Add(Mul(Integer(2), Symbol('r')), Integer(19)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(4), Pow(Symbol('a'), Integer(2)), Pow(Symbol('b'), Integer(2))), Mul(Integer(-1), Integer(400), Pow(Symbol('a'), Integer(2))), Mul(Integer(-1), Pow(Symbol('b'), Integer(2)))), Integer(0))), And(StrictGreaterThan(Add(Mul(Integer(2), Symbol('a')), Integer(-1)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Integer(4), Pow(Symbol('a'), Integer(2)), Pow(Symbol('b'), Integer(2))), Mul(Integer(4), Pow(Symbol('a'), Integer(2)), Pow(Symbol('r'), Integer(2))), Mul(Integer(-1), Integer(761), Pow(Symbol('a'), Integer(2))), Pow(Symbol('b'), Integer(2))), Integer(0))), And(StrictLessThan(Add(Mul(Integer(2), Symbol('a')), Integer(1)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Integer(4), Pow(Symbol('a'), Integer(2)), Pow(Symbol('b'), Integer(2))), Mul(Integer(4), Pow(Symbol('a'), Integer(2)), Pow(Symbol('r'), Integer(2))), Mul(Integer(-1), Integer(761), Pow(Symbol('a'), Integer(2))), Pow(Symbol('b'), Integer(2))), Integer(0))), StrictLessThan(Add(Mul(Integer(16), Pow(Symbol('a'), Integer(4)), Pow(Symbol('b'), Integer(4))), Mul(Integer(-1), Integer(32), Pow(Symbol('a'), Integer(4)), Pow(Symbol('b'), Integer(2)), Pow(Symbol('r'), Integer(2))), Mul(Integer(-1), Integer(312), Pow(Symbol('a'), Integer(4)), Pow(Symbol('b'), Integer(2))), Mul(Integer(16), Pow(Symbol('a'), Integer(4)), Pow(Symbol('r'), Integer(4))), Mul(Integer(-1), Integer(6088), Pow(Symbol('a'), Integer(4)), Pow(Symbol('r'), Integer(2))), Mul(Integer(579121), Pow(Symbol('a'), Integer(4))), Mul(Integer(-1), Integer(8), Pow(Symbol('a'), Integer(2)), Pow(Symbol('b'), Integer(4))), Mul(Integer(8), Pow(Symbol('a'), Integer(2)), Pow(Symbol('b'), Integer(2)), Pow(Symbol('r'), Integer(2))), Mul(Integer(78), Pow(Symbol('a'), Integer(2)), Pow(Symbol('b'), Integer(2))), Pow(Symbol('b'), Integer(4))), Integer(0))))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1(a:sympy.Rational,b:sympy.Rational,r:sympy.Rational):
	#Ne(a, 0) & Ne(8*b - 1, 0) & Ne(8*b + 1, 0) & Ne(8*r - 79, 0) & Ne(8*r + 79, 0) & (((8*r - 79 > 0) & (64*a**2*b**2 - a**2 - 6400*b**2 > 0)) | ((8*r + 79 < 0) & (64*a**2*b**2 - a**2 - 6400*b**2 > 0)) | ((8*b - 1 > 0) & (-64*a**2*b**2 + a**2 + 64*b**2*r**2 - 12641*b**2 > 0)) | ((8*b + 1 < 0) & (-64*a**2*b**2 + a**2 + 64*b**2*r**2 - 12641*b**2 > 0)) | (4096*a**4*b**4 - 128*a**4*b**2 + a**4 - 8192*a**2*b**4*r**2 - 20352*a**2*b**4 + 128*a**2*b**2*r**2 + 318*a**2*b**2 + 4096*b**4*r**4 - 1618048*b**4*r**2 + 159794881*b**4 < 0))

	pre_cond = And(Unequality(Symbol('a'), Integer(0)), Unequality(Add(Mul(Integer(8), Symbol('b')), Integer(-1)), Integer(0)), Unequality(Add(Mul(Integer(8), Symbol('b')), Integer(1)), Integer(0)), Unequality(Add(Mul(Integer(8), Symbol('r')), Integer(-79)), Integer(0)), Unequality(Add(Mul(Integer(8), Symbol('r')), Integer(79)), Integer(0)), Or(And(StrictGreaterThan(Add(Mul(Integer(8), Symbol('r')), Integer(-79)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(64), Pow(Symbol('a'), Integer(2)), Pow(Symbol('b'), Integer(2))), Mul(Integer(-1), Pow(Symbol('a'), Integer(2))), Mul(Integer(-1), Integer(6400), Pow(Symbol('b'), Integer(2)))), Integer(0))), And(StrictLessThan(Add(Mul(Integer(8), Symbol('r')), Integer(79)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(64), Pow(Symbol('a'), Integer(2)), Pow(Symbol('b'), Integer(2))), Mul(Integer(-1), Pow(Symbol('a'), Integer(2))), Mul(Integer(-1), Integer(6400), Pow(Symbol('b'), Integer(2)))), Integer(0))), And(StrictGreaterThan(Add(Mul(Integer(8), Symbol('b')), Integer(-1)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Integer(64), Pow(Symbol('a'), Integer(2)), Pow(Symbol('b'), Integer(2))), Pow(Symbol('a'), Integer(2)), Mul(Integer(64), Pow(Symbol('b'), Integer(2)), Pow(Symbol('r'), Integer(2))), Mul(Integer(-1), Integer(12641), Pow(Symbol('b'), Integer(2)))), Integer(0))), And(StrictLessThan(Add(Mul(Integer(8), Symbol('b')), Integer(1)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Integer(64), Pow(Symbol('a'), Integer(2)), Pow(Symbol('b'), Integer(2))), Pow(Symbol('a'), Integer(2)), Mul(Integer(64), Pow(Symbol('b'), Integer(2)), Pow(Symbol('r'), Integer(2))), Mul(Integer(-1), Integer(12641), Pow(Symbol('b'), Integer(2)))), Integer(0))), StrictLessThan(Add(Mul(Integer(4096), Pow(Symbol('a'), Integer(4)), Pow(Symbol('b'), Integer(4))), Mul(Integer(-1), Integer(128), Pow(Symbol('a'), Integer(4)), Pow(Symbol('b'), Integer(2))), Pow(Symbol('a'), Integer(4)), Mul(Integer(-1), Integer(8192), Pow(Symbol('a'), Integer(2)), Pow(Symbol('b'), Integer(4)), Pow(Symbol('r'), Integer(2))), Mul(Integer(-1), Integer(20352), Pow(Symbol('a'), Integer(2)), Pow(Symbol('b'), Integer(4))), Mul(Integer(128), Pow(Symbol('a'), Integer(2)), Pow(Symbol('b'), Integer(2)), Pow(Symbol('r'), Integer(2))), Mul(Integer(318), Pow(Symbol('a'), Integer(2)), Pow(Symbol('b'), Integer(2))), Mul(Integer(4096), Pow(Symbol('b'), Integer(4)), Pow(Symbol('r'), Integer(4))), Mul(Integer(-1), Integer(1618048), Pow(Symbol('b'), Integer(4)), Pow(Symbol('r'), Integer(2))), Mul(Integer(159794881), Pow(Symbol('b'), Integer(4)))), Integer(0))))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_2(a:sympy.Rational,b:sympy.Rational,r:sympy.Rational):
	#Ne(b, 0) & Ne(128*a - 25, 0) & Ne(128*a + 25, 0) & Ne(128*r - 1255, 0) & Ne(128*r + 1255, 0) & (((128*r - 1255 > 0) & (16384*a**2*b**2 - 1638400*a**2 - 625*b**2 > 0)) | ((128*r + 1255 < 0) & (16384*a**2*b**2 - 1638400*a**2 - 625*b**2 > 0)) | ((128*a - 25 > 0) & (-16384*a**2*b**2 + 16384*a**2*r**2 - 3213425*a**2 + 625*b**2 > 0)) | ((128*a + 25 < 0) & (-16384*a**2*b**2 + 16384*a**2*r**2 - 3213425*a**2 + 625*b**2 > 0)) | (268435456*a**4*b**4 - 536870912*a**4*b**2*r**2 - 2076672000*a**4*b**2 + 268435456*a**4*r**4 - 105297510400*a**4*r**2 + 10326100230625*a**4 - 20480000*a**2*b**4 + 20480000*a**2*b**2*r**2 + 79218750*a**2*b**2 + 390625*b**4 < 0))

	pre_cond = And(Unequality(Symbol('b'), Integer(0)), Unequality(Add(Mul(Integer(128), Symbol('a')), Integer(-25)), Integer(0)), Unequality(Add(Mul(Integer(128), Symbol('a')), Integer(25)), Integer(0)), Unequality(Add(Mul(Integer(128), Symbol('r')), Integer(-1255)), Integer(0)), Unequality(Add(Mul(Integer(128), Symbol('r')), Integer(1255)), Integer(0)), Or(And(StrictGreaterThan(Add(Mul(Integer(128), Symbol('r')), Integer(-1255)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(16384), Pow(Symbol('a'), Integer(2)), Pow(Symbol('b'), Integer(2))), Mul(Integer(-1), Integer(1638400), Pow(Symbol('a'), Integer(2))), Mul(Integer(-1), Integer(625), Pow(Symbol('b'), Integer(2)))), Integer(0))), And(StrictLessThan(Add(Mul(Integer(128), Symbol('r')), Integer(1255)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(16384), Pow(Symbol('a'), Integer(2)), Pow(Symbol('b'), Integer(2))), Mul(Integer(-1), Integer(1638400), Pow(Symbol('a'), Integer(2))), Mul(Integer(-1), Integer(625), Pow(Symbol('b'), Integer(2)))), Integer(0))), And(StrictGreaterThan(Add(Mul(Integer(128), Symbol('a')), Integer(-25)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Integer(16384), Pow(Symbol('a'), Integer(2)), Pow(Symbol('b'), Integer(2))), Mul(Integer(16384), Pow(Symbol('a'), Integer(2)), Pow(Symbol('r'), Integer(2))), Mul(Integer(-1), Integer(3213425), Pow(Symbol('a'), Integer(2))), Mul(Integer(625), Pow(Symbol('b'), Integer(2)))), Integer(0))), And(StrictLessThan(Add(Mul(Integer(128), Symbol('a')), Integer(25)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Integer(16384), Pow(Symbol('a'), Integer(2)), Pow(Symbol('b'), Integer(2))), Mul(Integer(16384), Pow(Symbol('a'), Integer(2)), Pow(Symbol('r'), Integer(2))), Mul(Integer(-1), Integer(3213425), Pow(Symbol('a'), Integer(2))), Mul(Integer(625), Pow(Symbol('b'), Integer(2)))), Integer(0))), StrictLessThan(Add(Mul(Integer(268435456), Pow(Symbol('a'), Integer(4)), Pow(Symbol('b'), Integer(4))), Mul(Integer(-1), Integer(536870912), Pow(Symbol('a'), Integer(4)), Pow(Symbol('b'), Integer(2)), Pow(Symbol('r'), Integer(2))), Mul(Integer(-1), Integer(2076672000), Pow(Symbol('a'), Integer(4)), Pow(Symbol('b'), Integer(2))), Mul(Integer(268435456), Pow(Symbol('a'), Integer(4)), Pow(Symbol('r'), Integer(4))), Mul(Integer(-1), Integer(105297510400), Pow(Symbol('a'), Integer(4)), Pow(Symbol('r'), Integer(2))), Mul(Integer(10326100230625), Pow(Symbol('a'), Integer(4))), Mul(Integer(-1), Integer(20480000), Pow(Symbol('a'), Integer(2)), Pow(Symbol('b'), Integer(4))), Mul(Integer(20480000), Pow(Symbol('a'), Integer(2)), Pow(Symbol('b'), Integer(2)), Pow(Symbol('r'), Integer(2))), Mul(Integer(79218750), Pow(Symbol('a'), Integer(2)), Pow(Symbol('b'), Integer(2))), Mul(Integer(390625), Pow(Symbol('b'), Integer(4)))), Integer(0))))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_3(a:sympy.Rational,b:sympy.Rational,r:sympy.Rational):
	#Ne(a, 0) & Ne(4*b - 39, 0) & Ne(4*b + 39, 0) & Ne(4*r - 1, 0) & Ne(4*r + 1, 0) & (((4*r - 1 > 0) & (16*a**2*b**2 - 1521*a**2 - 1600*b**2 > 0)) | ((4*r + 1 < 0) & (16*a**2*b**2 - 1521*a**2 - 1600*b**2 > 0)) | ((4*b - 39 > 0) & (-16*a**2*b**2 + 1521*a**2 + 16*b**2*r**2 - 1601*b**2 > 0)) | ((4*b + 39 < 0) & (-16*a**2*b**2 + 1521*a**2 + 16*b**2*r**2 - 1601*b**2 > 0)) | (256*a**4*b**4 - 48672*a**4*b**2 + 2313441*a**4 - 512*a**2*b**4*r**2 - 51168*a**2*b**4 + 48672*a**2*b**2*r**2 + 4864158*a**2*b**2 + 256*b**4*r**4 - 51232*b**4*r**2 + 2563201*b**4 < 0))

	pre_cond = And(Unequality(Symbol('a'), Integer(0)), Unequality(Add(Mul(Integer(4), Symbol('b')), Integer(-39)), Integer(0)), Unequality(Add(Mul(Integer(4), Symbol('b')), Integer(39)), Integer(0)), Unequality(Add(Mul(Integer(4), Symbol('r')), Integer(-1)), Integer(0)), Unequality(Add(Mul(Integer(4), Symbol('r')), Integer(1)), Integer(0)), Or(And(StrictGreaterThan(Add(Mul(Integer(4), Symbol('r')), Integer(-1)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(16), Pow(Symbol('a'), Integer(2)), Pow(Symbol('b'), Integer(2))), Mul(Integer(-1), Integer(1521), Pow(Symbol('a'), Integer(2))), Mul(Integer(-1), Integer(1600), Pow(Symbol('b'), Integer(2)))), Integer(0))), And(StrictLessThan(Add(Mul(Integer(4), Symbol('r')), Integer(1)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(16), Pow(Symbol('a'), Integer(2)), Pow(Symbol('b'), Integer(2))), Mul(Integer(-1), Integer(1521), Pow(Symbol('a'), Integer(2))), Mul(Integer(-1), Integer(1600), Pow(Symbol('b'), Integer(2)))), Integer(0))), And(StrictGreaterThan(Add(Mul(Integer(4), Symbol('b')), Integer(-39)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Integer(16), Pow(Symbol('a'), Integer(2)), Pow(Symbol('b'), Integer(2))), Mul(Integer(1521), Pow(Symbol('a'), Integer(2))), Mul(Integer(16), Pow(Symbol('b'), Integer(2)), Pow(Symbol('r'), Integer(2))), Mul(Integer(-1), Integer(1601), Pow(Symbol('b'), Integer(2)))), Integer(0))), And(StrictLessThan(Add(Mul(Integer(4), Symbol('b')), Integer(39)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Integer(16), Pow(Symbol('a'), Integer(2)), Pow(Symbol('b'), Integer(2))), Mul(Integer(1521), Pow(Symbol('a'), Integer(2))), Mul(Integer(16), Pow(Symbol('b'), Integer(2)), Pow(Symbol('r'), Integer(2))), Mul(Integer(-1), Integer(1601), Pow(Symbol('b'), Integer(2)))), Integer(0))), StrictLessThan(Add(Mul(Integer(256), Pow(Symbol('a'), Integer(4)), Pow(Symbol('b'), Integer(4))), Mul(Integer(-1), Integer(48672), Pow(Symbol('a'), Integer(4)), Pow(Symbol('b'), Integer(2))), Mul(Integer(2313441), Pow(Symbol('a'), Integer(4))), Mul(Integer(-1), Integer(512), Pow(Symbol('a'), Integer(2)), Pow(Symbol('b'), Integer(4)), Pow(Symbol('r'), Integer(2))), Mul(Integer(-1), Integer(51168), Pow(Symbol('a'), Integer(2)), Pow(Symbol('b'), Integer(4))), Mul(Integer(48672), Pow(Symbol('a'), Integer(2)), Pow(Symbol('b'), Integer(2)), Pow(Symbol('r'), Integer(2))), Mul(Integer(4864158), Pow(Symbol('a'), Integer(2)), Pow(Symbol('b'), Integer(2))), Mul(Integer(256), Pow(Symbol('b'), Integer(4)), Pow(Symbol('r'), Integer(4))), Mul(Integer(-1), Integer(51232), Pow(Symbol('b'), Integer(4)), Pow(Symbol('r'), Integer(2))), Mul(Integer(2563201), Pow(Symbol('b'), Integer(4)))), Integer(0))))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def post_condition(a:sympy.Rational, b:sympy.Rational, r:sympy.Rational, x:sympy.Rational, y:sympy.Rational):
	# (0 > -r**2 + x**2 - 20*x + y**2 - 20*y + 200) & (0 > -a**2*b**2 + a**2*x**2 + b**2*y**2)

	post_cond =  And(StrictGreaterThan(Integer(0), Add(Mul(Integer(-1), Pow(Symbol('r'), Integer(2))), Pow(Symbol('x'), Integer(2)), Mul(Integer(-1), Integer(20), Symbol('x')), Pow(Symbol('y'), Integer(2)), Mul(Integer(-1), Integer(20), Symbol('y')), Integer(200))), StrictGreaterThan(Integer(0), Add(Mul(Integer(-1), Pow(Symbol('a'), Integer(2)), Pow(Symbol('b'), Integer(2))), Mul(Pow(Symbol('a'), Integer(2)), Pow(Symbol('x'), Integer(2))), Mul(Pow(Symbol('b'), Integer(2)), Pow(Symbol('y'), Integer(2))))))

	eval = post_cond.subs( { 'a':a, 'b':b, 'r':r, 'x':x, 'y':y })

	return eval == sympy.logic.boolalg.BooleanTrue



#return post-condition single variable
def return_post_condition_single_var(post_condition, a:sympy.Rational=None, b:sympy.Rational=None, r:sympy.Rational=None, x:sympy.Rational=None, y:sympy.Rational=None):
	assert a!=None
	assert b!=None
	assert r!=None


	if x==None:
		assert y!=None
		return lambda x: post_condition(a=a, b=b, r=r, x=x, y=y)

	if y==None:
		assert x!=None
		return lambda y: post_condition(a=a, b=b, r=r, x=x, y=y)


	return post_condition(a=a, b=b, r=r, x=x, y=y)


def get_univariate_poly( a:sympy.Rational, b:sympy.Rational, r:sympy.Rational, x:sympy.Rational, y:sympy.Rational ):


	post_cond =  And(StrictGreaterThan(Integer(0), Add(Mul(Integer(-1), Pow(Symbol('r'), Integer(2))), Pow(Symbol('x'), Integer(2)), Mul(Integer(-1), Integer(20), Symbol('x')), Pow(Symbol('y'), Integer(2)), Mul(Integer(-1), Integer(20), Symbol('y')), Integer(200))), StrictGreaterThan(Integer(0), Add(Mul(Integer(-1), Pow(Symbol('a'), Integer(2)), Pow(Symbol('b'), Integer(2))), Mul(Pow(Symbol('a'), Integer(2)), Pow(Symbol('x'), Integer(2))), Mul(Pow(Symbol('b'), Integer(2)), Pow(Symbol('y'), Integer(2))))))

	eval = post_cond.subs( { 'a':a, 'b':b, 'r':r, 'x':x, 'y':y })
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
	
	
	ip_0=int(input("enter numerator of r:\n"))
	ip_1=int(input("enter denominator of r:\n"))
	assert(ip_1!=0), ("Error denominator entered is 0")
	r=sympy.Rational(ip_0,ip_1)
	
	
	lambda_var_0 = sympy.symbols('lambda_var_0')
	
	
	if pre_condition_0(a=a,b=b,r=r)==True:
		all_vals = dict()
		all_vals['a'] = a
		all_vals['b'] = b
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
	
	
	if pre_condition_1(a=a,b=b,r=r)==True:
		all_vals = dict()
		all_vals['a'] = a
		all_vals['b'] = b
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
	
	
	if pre_condition_2(a=a,b=b,r=r)==True:
		all_vals = dict()
		all_vals['a'] = a
		all_vals['b'] = b
		all_vals['r'] = r
		all_vals['x'] = Add(Symbol('lambda_var_0'), Rational(39, 4))
		all_vals['y'] = Rational(25, 128)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_2 SAT")

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_3(a=a,b=b,r=r)==True:
		all_vals = dict()
		all_vals['a'] = a
		all_vals['b'] = b
		all_vals['r'] = r
		all_vals['x'] = Rational(39, 4)
		all_vals['y'] = Add(Symbol('lambda_var_0'), Rational(25, 128))
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_3 SAT")

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass


	print("UNKNOWN")
