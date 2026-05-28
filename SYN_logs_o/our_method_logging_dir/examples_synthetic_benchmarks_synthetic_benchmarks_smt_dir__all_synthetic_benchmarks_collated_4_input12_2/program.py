import sympy
from sympy import *
from NQS.helper_program_cav import get_lambda_val

def pre_condition_0(r:sympy.Rational,c:sympy.Rational):
	#Ne(8*r - 1, 0) & Ne(8*r + 1, 0) & (-64*c**2 - 128*c + 64*r + 1 < 0) & (((128*c + 7 > 0) & (8*r + 1 < 0)) | ((128*c**2 + 128*c - 11 < 0) & (-4*c**2 - 4*c + 6*r**2 + 6*r + 1 <= 0)) | ((8*r + 1 < 0) & (-4*c**2*r - 4*c*r - 2*c + 2*r**3 + 3*r**2 + r < 0)) | (-64*c**2*r**2 + 65*c**2 - 64*c*r**2 - 64*c*r + 16*r**4 + 32*r**3 + 16*r**2 < 0) | ((128*c - 9 > 0) & (8*r - 1 > 0) & (-4*c**2*r - 4*c*r - 2*c + 2*r**3 + 3*r**2 + r < 0)) | ((2*r + 1 < 0) & (-4*c**2 - 4*c + 6*r**2 + 6*r + 1 > 0) & (266240*c**6 + 1064960*c**5 + 922496*c**4 + 246528*c**3 + 8945*c**2 - 1264*c - 63 >= 0)) | ((-4*c**2 - 4*c + 6*r**2 + 6*r + 1 > 0) & (4096*c**4 + 16384*c**3 + 12160*c**2 - 256*c - 63 > 0) & (-4*c**2*r - 4*c*r - 2*c + 2*r**3 + 3*r**2 + r > 0)))

	pre_cond = And(Unequality(Add(Mul(Integer(8), Symbol('r')), Integer(-1)), Integer(0)), Unequality(Add(Mul(Integer(8), Symbol('r')), Integer(1)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Integer(64), Pow(Symbol('c'), Integer(2))), Mul(Integer(-1), Integer(128), Symbol('c')), Mul(Integer(64), Symbol('r')), Integer(1)), Integer(0)), Or(And(StrictGreaterThan(Add(Mul(Integer(128), Symbol('c')), Integer(7)), Integer(0)), StrictLessThan(Add(Mul(Integer(8), Symbol('r')), Integer(1)), Integer(0))), And(StrictLessThan(Add(Mul(Integer(128), Pow(Symbol('c'), Integer(2))), Mul(Integer(128), Symbol('c')), Integer(-11)), Integer(0)), LessThan(Add(Mul(Integer(-1), Integer(4), Pow(Symbol('c'), Integer(2))), Mul(Integer(-1), Integer(4), Symbol('c')), Mul(Integer(6), Pow(Symbol('r'), Integer(2))), Mul(Integer(6), Symbol('r')), Integer(1)), Integer(0))), And(StrictLessThan(Add(Mul(Integer(8), Symbol('r')), Integer(1)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Integer(4), Pow(Symbol('c'), Integer(2)), Symbol('r')), Mul(Integer(-1), Integer(4), Symbol('c'), Symbol('r')), Mul(Integer(-1), Integer(2), Symbol('c')), Mul(Integer(2), Pow(Symbol('r'), Integer(3))), Mul(Integer(3), Pow(Symbol('r'), Integer(2))), Symbol('r')), Integer(0))), StrictLessThan(Add(Mul(Integer(-1), Integer(64), Pow(Symbol('c'), Integer(2)), Pow(Symbol('r'), Integer(2))), Mul(Integer(65), Pow(Symbol('c'), Integer(2))), Mul(Integer(-1), Integer(64), Symbol('c'), Pow(Symbol('r'), Integer(2))), Mul(Integer(-1), Integer(64), Symbol('c'), Symbol('r')), Mul(Integer(16), Pow(Symbol('r'), Integer(4))), Mul(Integer(32), Pow(Symbol('r'), Integer(3))), Mul(Integer(16), Pow(Symbol('r'), Integer(2)))), Integer(0)), And(StrictGreaterThan(Add(Mul(Integer(128), Symbol('c')), Integer(-9)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(8), Symbol('r')), Integer(-1)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Integer(4), Pow(Symbol('c'), Integer(2)), Symbol('r')), Mul(Integer(-1), Integer(4), Symbol('c'), Symbol('r')), Mul(Integer(-1), Integer(2), Symbol('c')), Mul(Integer(2), Pow(Symbol('r'), Integer(3))), Mul(Integer(3), Pow(Symbol('r'), Integer(2))), Symbol('r')), Integer(0))), And(StrictLessThan(Add(Mul(Integer(2), Symbol('r')), Integer(1)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Integer(4), Pow(Symbol('c'), Integer(2))), Mul(Integer(-1), Integer(4), Symbol('c')), Mul(Integer(6), Pow(Symbol('r'), Integer(2))), Mul(Integer(6), Symbol('r')), Integer(1)), Integer(0)), GreaterThan(Add(Mul(Integer(266240), Pow(Symbol('c'), Integer(6))), Mul(Integer(1064960), Pow(Symbol('c'), Integer(5))), Mul(Integer(922496), Pow(Symbol('c'), Integer(4))), Mul(Integer(246528), Pow(Symbol('c'), Integer(3))), Mul(Integer(8945), Pow(Symbol('c'), Integer(2))), Mul(Integer(-1), Integer(1264), Symbol('c')), Integer(-63)), Integer(0))), And(StrictGreaterThan(Add(Mul(Integer(-1), Integer(4), Pow(Symbol('c'), Integer(2))), Mul(Integer(-1), Integer(4), Symbol('c')), Mul(Integer(6), Pow(Symbol('r'), Integer(2))), Mul(Integer(6), Symbol('r')), Integer(1)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(4096), Pow(Symbol('c'), Integer(4))), Mul(Integer(16384), Pow(Symbol('c'), Integer(3))), Mul(Integer(12160), Pow(Symbol('c'), Integer(2))), Mul(Integer(-1), Integer(256), Symbol('c')), Integer(-63)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Integer(4), Pow(Symbol('c'), Integer(2)), Symbol('r')), Mul(Integer(-1), Integer(4), Symbol('c'), Symbol('r')), Mul(Integer(-1), Integer(2), Symbol('c')), Mul(Integer(2), Pow(Symbol('r'), Integer(3))), Mul(Integer(3), Pow(Symbol('r'), Integer(2))), Symbol('r')), Integer(0)))))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1(r:sympy.Rational,c:sympy.Rational):
	#Ne(2*r - 1, 0) & Ne(2*r + 1, 0) & (-12*c + 4*r + 1 < 0) & ((2*r - 1 > 0) | (2*r + 1 < 0))

	pre_cond = And(Unequality(Add(Mul(Integer(2), Symbol('r')), Integer(-1)), Integer(0)), Unequality(Add(Mul(Integer(2), Symbol('r')), Integer(1)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Integer(12), Symbol('c')), Mul(Integer(4), Symbol('r')), Integer(1)), Integer(0)), Or(StrictGreaterThan(Add(Mul(Integer(2), Symbol('r')), Integer(-1)), Integer(0)), StrictLessThan(Add(Mul(Integer(2), Symbol('r')), Integer(1)), Integer(0))))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_2(r:sympy.Rational,c:sympy.Rational):
	#Ne(r, 0) & (-c**2 - 2*c + r < 0) & ((c + 1 > 0) | (r + 1 < 0) | (2*c*r - 2*c + r**2 + r < 0) | ((c + 3 < 0) & (2*c + 2*r + 1 > 0)))

	pre_cond = And(Unequality(Symbol('r'), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Pow(Symbol('c'), Integer(2))), Mul(Integer(-1), Integer(2), Symbol('c')), Symbol('r')), Integer(0)), Or(StrictGreaterThan(Add(Symbol('c'), Integer(1)), Integer(0)), StrictLessThan(Add(Symbol('r'), Integer(1)), Integer(0)), StrictLessThan(Add(Mul(Integer(2), Symbol('c'), Symbol('r')), Mul(Integer(-1), Integer(2), Symbol('c')), Pow(Symbol('r'), Integer(2)), Symbol('r')), Integer(0)), And(StrictLessThan(Add(Symbol('c'), Integer(3)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(2), Symbol('c')), Mul(Integer(2), Symbol('r')), Integer(1)), Integer(0)))))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_3(r:sympy.Rational,c:sympy.Rational):
	#Ne(32*r - 1, 0) & Ne(32*r + 1, 0) & (-2112*c + 1024*r + 1 < 0) & ((32*r - 1 > 0) | (32*r + 1 < 0))

	pre_cond = And(Unequality(Add(Mul(Integer(32), Symbol('r')), Integer(-1)), Integer(0)), Unequality(Add(Mul(Integer(32), Symbol('r')), Integer(1)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Integer(2112), Symbol('c')), Mul(Integer(1024), Symbol('r')), Integer(1)), Integer(0)), Or(StrictGreaterThan(Add(Mul(Integer(32), Symbol('r')), Integer(-1)), Integer(0)), StrictLessThan(Add(Mul(Integer(32), Symbol('r')), Integer(1)), Integer(0))))

	eval = pre_cond.subs( { 'r':r, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def post_condition(r:sympy.Rational, c:sympy.Rational, x:sympy.Rational, l:sympy.Rational):
	# (0 > l**2 - r**2 + x**2) & (0 > -2*c*x - 2*c + l**2 + r + x**2)

	post_cond =  And(StrictGreaterThan(Integer(0), Add(Pow(Symbol('l'), Integer(2)), Mul(Integer(-1), Pow(Symbol('r'), Integer(2))), Pow(Symbol('x'), Integer(2)))), StrictGreaterThan(Integer(0), Add(Mul(Integer(-1), Integer(2), Symbol('c'), Symbol('x')), Mul(Integer(-1), Integer(2), Symbol('c')), Pow(Symbol('l'), Integer(2)), Symbol('r'), Pow(Symbol('x'), Integer(2)))))

	eval = post_cond.subs( { 'r':r, 'c':c, 'x':x, 'l':l })

	return eval == sympy.logic.boolalg.BooleanTrue



#return post-condition single variable
def return_post_condition_single_var(post_condition, r:sympy.Rational=None, c:sympy.Rational=None, x:sympy.Rational=None, l:sympy.Rational=None):
	assert r!=None
	assert c!=None


	if x==None:
		assert l!=None
		return lambda x: post_condition(r=r, c=c, x=x, l=l)

	if l==None:
		assert x!=None
		return lambda l: post_condition(r=r, c=c, x=x, l=l)


	return post_condition(r=r, c=c, x=x, l=l)


def get_univariate_poly( r:sympy.Rational, c:sympy.Rational, x:sympy.Rational, l:sympy.Rational ):


	post_cond =  And(StrictGreaterThan(Integer(0), Add(Pow(Symbol('l'), Integer(2)), Mul(Integer(-1), Pow(Symbol('r'), Integer(2))), Pow(Symbol('x'), Integer(2)))), StrictGreaterThan(Integer(0), Add(Mul(Integer(-1), Integer(2), Symbol('c'), Symbol('x')), Mul(Integer(-1), Integer(2), Symbol('c')), Pow(Symbol('l'), Integer(2)), Symbol('r'), Pow(Symbol('x'), Integer(2)))))

	eval = post_cond.subs( { 'r':r, 'c':c, 'x':x, 'l':l })
	return eval



if __name__=="__main__":
	
	ip_0=int(input("enter numerator of r:\n"))
	ip_1=int(input("enter denominator of r:\n"))
	assert(ip_1!=0), ("Error denominator entered is 0")
	r=sympy.Rational(ip_0,ip_1)
	
	
	ip_0=int(input("enter numerator of c:\n"))
	ip_1=int(input("enter denominator of c:\n"))
	assert(ip_1!=0), ("Error denominator entered is 0")
	c=sympy.Rational(ip_0,ip_1)
	
	
	lambda_var_0 = sympy.symbols('lambda_var_0')
	
	
	if pre_condition_0(r=r,c=c)==True:
		all_vals = dict()
		all_vals['r'] = r
		all_vals['c'] = c
		all_vals['x'] = Add(Symbol('lambda_var_0'), Rational(1, 2))
		all_vals['l'] = Rational(1, 8)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_0 SAT")

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("l=", all_vals["l"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_1(r=r,c=c)==True:
		all_vals = dict()
		all_vals['r'] = r
		all_vals['c'] = c
		all_vals['x'] = Rational(1, 2)
		all_vals['l'] = Add(Symbol('lambda_var_0'), Rational(1, 8))
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_1 SAT")

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("l=", all_vals["l"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_2(r=r,c=c)==True:
		all_vals = dict()
		all_vals['r'] = r
		all_vals['c'] = c
		all_vals['x'] = Add(Symbol('lambda_var_0'), Rational(1, 32))
		all_vals['l'] = Integer(0)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_2 SAT")

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("l=", all_vals["l"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_3(r=r,c=c)==True:
		all_vals = dict()
		all_vals['r'] = r
		all_vals['c'] = c
		all_vals['x'] = Rational(1, 32)
		all_vals['l'] = Symbol('lambda_var_0')
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_3 SAT")

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("l=", all_vals["l"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass


	print("Weakest pre-condition UNSAT")
