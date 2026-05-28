import sympy
from sympy import *
from NQS.helper_program_cav import get_lambda_val

def pre_condition_0(c:sympy.Rational):
	#256*c - 1 < 0

	pre_cond = StrictLessThan(Add(Mul(Integer(256), Symbol('c')), Integer(-1)), Integer(0))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1(c:sympy.Rational):
	#(4*c + 1 < 0) & (2*c**2 + c - 5 < 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(4), Symbol('c')), Integer(1)), Integer(0)), StrictLessThan(Add(Mul(Integer(2), Pow(Symbol('c'), Integer(2))), Symbol('c'), Integer(-5)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_2(c:sympy.Rational):
	#4*c - 9 < 0

	pre_cond = StrictLessThan(Add(Mul(Integer(4), Symbol('c')), Integer(-9)), Integer(0))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_3(c:sympy.Rational):
	#c - 3 < 0

	pre_cond = StrictLessThan(Add(Symbol('c'), Integer(-3)), Integer(0))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_4(c:sympy.Rational):
	#(c + 15 < 0) & (c**2 + 30*c - 150 < 0)

	pre_cond = And(StrictLessThan(Add(Symbol('c'), Integer(15)), Integer(0)), StrictLessThan(Add(Pow(Symbol('c'), Integer(2)), Mul(Integer(30), Symbol('c')), Integer(-150)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_5(c:sympy.Rational):
	#(64*c + 961 < 0) & (32*c**2 + 961*c - 4805 < 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(64), Symbol('c')), Integer(961)), Integer(0)), StrictLessThan(Add(Mul(Integer(32), Pow(Symbol('c'), Integer(2))), Mul(Integer(961), Symbol('c')), Integer(-4805)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_6(c:sympy.Rational):
	#(c + 15 < 0) & (c**2 + 30*c - 150 < 0)

	pre_cond = And(StrictLessThan(Add(Symbol('c'), Integer(15)), Integer(0)), StrictLessThan(Add(Pow(Symbol('c'), Integer(2)), Mul(Integer(30), Symbol('c')), Integer(-150)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_7(c:sympy.Rational):
	#(64*c + 961 < 0) & (32*c**2 + 961*c - 4805 < 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(64), Symbol('c')), Integer(961)), Integer(0)), StrictLessThan(Add(Mul(Integer(32), Pow(Symbol('c'), Integer(2))), Mul(Integer(961), Symbol('c')), Integer(-4805)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_8(c:sympy.Rational):
	#(c + 15 < 0) & (c**2 + 30*c - 150 < 0)

	pre_cond = And(StrictLessThan(Add(Symbol('c'), Integer(15)), Integer(0)), StrictLessThan(Add(Pow(Symbol('c'), Integer(2)), Mul(Integer(30), Symbol('c')), Integer(-150)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_9(c:sympy.Rational):
	#(64*c + 961 < 0) & (32*c**2 + 961*c - 4805 < 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(64), Symbol('c')), Integer(961)), Integer(0)), StrictLessThan(Add(Mul(Integer(32), Pow(Symbol('c'), Integer(2))), Mul(Integer(961), Symbol('c')), Integer(-4805)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_10(c:sympy.Rational):
	#(c + 15 < 0) & (c**2 + 30*c - 150 < 0)

	pre_cond = And(StrictLessThan(Add(Symbol('c'), Integer(15)), Integer(0)), StrictLessThan(Add(Pow(Symbol('c'), Integer(2)), Mul(Integer(30), Symbol('c')), Integer(-150)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_11(c:sympy.Rational):
	#(64*c + 961 < 0) & (32*c**2 + 961*c - 4805 < 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(64), Symbol('c')), Integer(961)), Integer(0)), StrictLessThan(Add(Mul(Integer(32), Pow(Symbol('c'), Integer(2))), Mul(Integer(961), Symbol('c')), Integer(-4805)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_12(c:sympy.Rational):
	#(c + 15 < 0) & (c**2 + 30*c - 150 < 0)

	pre_cond = And(StrictLessThan(Add(Symbol('c'), Integer(15)), Integer(0)), StrictLessThan(Add(Pow(Symbol('c'), Integer(2)), Mul(Integer(30), Symbol('c')), Integer(-150)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_13(c:sympy.Rational):
	#(64*c + 961 < 0) & (32*c**2 + 961*c - 4805 < 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(64), Symbol('c')), Integer(961)), Integer(0)), StrictLessThan(Add(Mul(Integer(32), Pow(Symbol('c'), Integer(2))), Mul(Integer(961), Symbol('c')), Integer(-4805)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_14(c:sympy.Rational):
	#(c + 15 < 0) & (c**2 + 30*c - 150 < 0)

	pre_cond = And(StrictLessThan(Add(Symbol('c'), Integer(15)), Integer(0)), StrictLessThan(Add(Pow(Symbol('c'), Integer(2)), Mul(Integer(30), Symbol('c')), Integer(-150)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_15(c:sympy.Rational):
	#(64*c + 961 < 0) & (32*c**2 + 961*c - 4805 < 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(64), Symbol('c')), Integer(961)), Integer(0)), StrictLessThan(Add(Mul(Integer(32), Pow(Symbol('c'), Integer(2))), Mul(Integer(961), Symbol('c')), Integer(-4805)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_16(c:sympy.Rational):
	#(c + 15 < 0) & (c**2 + 30*c - 150 < 0)

	pre_cond = And(StrictLessThan(Add(Symbol('c'), Integer(15)), Integer(0)), StrictLessThan(Add(Pow(Symbol('c'), Integer(2)), Mul(Integer(30), Symbol('c')), Integer(-150)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_17(c:sympy.Rational):
	#(64*c + 961 < 0) & (32*c**2 + 961*c - 4805 < 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(64), Symbol('c')), Integer(961)), Integer(0)), StrictLessThan(Add(Mul(Integer(32), Pow(Symbol('c'), Integer(2))), Mul(Integer(961), Symbol('c')), Integer(-4805)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_18(c:sympy.Rational):
	#(c + 15 < 0) & (c**2 + 30*c - 150 < 0)

	pre_cond = And(StrictLessThan(Add(Symbol('c'), Integer(15)), Integer(0)), StrictLessThan(Add(Pow(Symbol('c'), Integer(2)), Mul(Integer(30), Symbol('c')), Integer(-150)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_19(c:sympy.Rational):
	#(64*c + 961 < 0) & (32*c**2 + 961*c - 4805 < 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(64), Symbol('c')), Integer(961)), Integer(0)), StrictLessThan(Add(Mul(Integer(32), Pow(Symbol('c'), Integer(2))), Mul(Integer(961), Symbol('c')), Integer(-4805)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_20(c:sympy.Rational):
	#(c + 15 < 0) & (c**2 + 30*c - 150 < 0)

	pre_cond = And(StrictLessThan(Add(Symbol('c'), Integer(15)), Integer(0)), StrictLessThan(Add(Pow(Symbol('c'), Integer(2)), Mul(Integer(30), Symbol('c')), Integer(-150)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_21(c:sympy.Rational):
	#(64*c + 961 < 0) & (32*c**2 + 961*c - 4805 < 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(64), Symbol('c')), Integer(961)), Integer(0)), StrictLessThan(Add(Mul(Integer(32), Pow(Symbol('c'), Integer(2))), Mul(Integer(961), Symbol('c')), Integer(-4805)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_22(c:sympy.Rational):
	#(c + 15 < 0) & (c**2 + 30*c - 150 < 0)

	pre_cond = And(StrictLessThan(Add(Symbol('c'), Integer(15)), Integer(0)), StrictLessThan(Add(Pow(Symbol('c'), Integer(2)), Mul(Integer(30), Symbol('c')), Integer(-150)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def post_condition(c:sympy.Rational, y:sympy.Rational, x:sympy.Rational):
	# (0 > c - x*y + y**2) & (0 > x**2 - y**2 - 10)

	post_cond =  And(StrictGreaterThan(Integer(0), Add(Symbol('c'), Mul(Integer(-1), Symbol('x'), Symbol('y')), Pow(Symbol('y'), Integer(2)))), StrictGreaterThan(Integer(0), Add(Pow(Symbol('x'), Integer(2)), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Integer(-10))))

	eval = post_cond.subs( { 'c':c, 'y':y, 'x':x })

	return eval == sympy.logic.boolalg.BooleanTrue



#return post-condition single variable
def return_post_condition_single_var(post_condition, c:sympy.Rational=None, y:sympy.Rational=None, x:sympy.Rational=None):
	assert c!=None


	if y==None:
		assert x!=None
		return lambda y: post_condition(c=c, y=y, x=x)

	if x==None:
		assert y!=None
		return lambda x: post_condition(c=c, y=y, x=x)


	return post_condition(c=c, y=y, x=x)


def get_univariate_poly( c:sympy.Rational, y:sympy.Rational, x:sympy.Rational ):


	post_cond =  And(StrictGreaterThan(Integer(0), Add(Symbol('c'), Mul(Integer(-1), Symbol('x'), Symbol('y')), Pow(Symbol('y'), Integer(2)))), StrictGreaterThan(Integer(0), Add(Pow(Symbol('x'), Integer(2)), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Integer(-10))))

	eval = post_cond.subs( { 'c':c, 'y':y, 'x':x })
	return eval



if __name__=="__main__":
	
	ip_0=int(input("enter numerator of c:\n"))
	ip_1=int(input("enter denominator of c:\n"))
	assert(ip_1!=0), ("Error denominator entered is 0")
	c=sympy.Rational(ip_0,ip_1)
	
	
	lambda_var_0 = sympy.symbols('lambda_var_0')
	
	
	if pre_condition_0(c=c)==True:
		all_vals = dict()
		all_vals['c'] = c
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
	
	
	if pre_condition_1(c=c)==True:
		all_vals = dict()
		all_vals['c'] = c
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
	
	
	if pre_condition_2(c=c)==True:
		all_vals = dict()
		all_vals['c'] = c
		all_vals['y'] = Add(Symbol('lambda_var_0'), Rational(-3, 2))
		all_vals['x'] = Integer(-3)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_2 SAT")

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_3(c=c)==True:
		all_vals = dict()
		all_vals['c'] = c
		all_vals['y'] = Rational(-3, 2)
		all_vals['x'] = Add(Symbol('lambda_var_0'), Integer(-3))
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_3 SAT")

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_4(c=c)==True:
		all_vals = dict()
		all_vals['c'] = c
		all_vals['y'] = Add(Symbol('lambda_var_0'), Rational(31, 8))
		all_vals['x'] = Integer(5)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_4 SAT")

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_5(c=c)==True:
		all_vals = dict()
		all_vals['c'] = c
		all_vals['y'] = Rational(31, 8)
		all_vals['x'] = Add(Symbol('lambda_var_0'), Integer(5))
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_5 SAT")

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_6(c=c)==True:
		all_vals = dict()
		all_vals['c'] = c
		all_vals['y'] = Add(Symbol('lambda_var_0'), Rational(-31, 8))
		all_vals['x'] = Integer(-5)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_6 SAT")

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_7(c=c)==True:
		all_vals = dict()
		all_vals['c'] = c
		all_vals['y'] = Rational(-31, 8)
		all_vals['x'] = Add(Symbol('lambda_var_0'), Integer(-5))
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_7 SAT")

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_8(c=c)==True:
		all_vals = dict()
		all_vals['c'] = c
		all_vals['y'] = Add(Symbol('lambda_var_0'), Rational(31, 8))
		all_vals['x'] = Integer(5)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_8 SAT")

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_9(c=c)==True:
		all_vals = dict()
		all_vals['c'] = c
		all_vals['y'] = Rational(31, 8)
		all_vals['x'] = Add(Symbol('lambda_var_0'), Integer(5))
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_9 SAT")

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_10(c=c)==True:
		all_vals = dict()
		all_vals['c'] = c
		all_vals['y'] = Add(Symbol('lambda_var_0'), Rational(31, 8))
		all_vals['x'] = Integer(5)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_10 SAT")

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_11(c=c)==True:
		all_vals = dict()
		all_vals['c'] = c
		all_vals['y'] = Rational(31, 8)
		all_vals['x'] = Add(Symbol('lambda_var_0'), Integer(5))
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_11 SAT")

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_12(c=c)==True:
		all_vals = dict()
		all_vals['c'] = c
		all_vals['y'] = Add(Symbol('lambda_var_0'), Rational(31, 8))
		all_vals['x'] = Integer(5)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_12 SAT")

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_13(c=c)==True:
		all_vals = dict()
		all_vals['c'] = c
		all_vals['y'] = Rational(31, 8)
		all_vals['x'] = Add(Symbol('lambda_var_0'), Integer(5))
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_13 SAT")

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_14(c=c)==True:
		all_vals = dict()
		all_vals['c'] = c
		all_vals['y'] = Add(Symbol('lambda_var_0'), Rational(31, 8))
		all_vals['x'] = Integer(5)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_14 SAT")

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_15(c=c)==True:
		all_vals = dict()
		all_vals['c'] = c
		all_vals['y'] = Rational(31, 8)
		all_vals['x'] = Add(Symbol('lambda_var_0'), Integer(5))
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_15 SAT")

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_16(c=c)==True:
		all_vals = dict()
		all_vals['c'] = c
		all_vals['y'] = Add(Symbol('lambda_var_0'), Rational(31, 8))
		all_vals['x'] = Integer(5)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_16 SAT")

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_17(c=c)==True:
		all_vals = dict()
		all_vals['c'] = c
		all_vals['y'] = Rational(31, 8)
		all_vals['x'] = Add(Symbol('lambda_var_0'), Integer(5))
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_17 SAT")

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_18(c=c)==True:
		all_vals = dict()
		all_vals['c'] = c
		all_vals['y'] = Add(Symbol('lambda_var_0'), Rational(31, 8))
		all_vals['x'] = Integer(5)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_18 SAT")

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_19(c=c)==True:
		all_vals = dict()
		all_vals['c'] = c
		all_vals['y'] = Rational(31, 8)
		all_vals['x'] = Add(Symbol('lambda_var_0'), Integer(5))
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_19 SAT")

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_20(c=c)==True:
		all_vals = dict()
		all_vals['c'] = c
		all_vals['y'] = Add(Symbol('lambda_var_0'), Rational(31, 8))
		all_vals['x'] = Integer(5)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_20 SAT")

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_21(c=c)==True:
		all_vals = dict()
		all_vals['c'] = c
		all_vals['y'] = Rational(31, 8)
		all_vals['x'] = Add(Symbol('lambda_var_0'), Integer(5))
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_21 SAT")

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_22(c=c)==True:
		all_vals = dict()
		all_vals['c'] = c
		all_vals['y'] = Add(Symbol('lambda_var_0'), Rational(31, 8))
		all_vals['x'] = Integer(5)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_22 SAT")

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass


	print("UNKNOWN")
