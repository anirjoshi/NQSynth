import sympy
from sympy import *
from NQS.helper_program_cav import get_lambda_val

def pre_condition_0(c:sympy.Rational):
	#(2*c + 1 < 0) & ((2*c**3 + 3*c**2 - 9*c + 3 < 0) | (c**4 + 2*c**3 - 9*c**2 + 6*c + 13 < 0))

	pre_cond = And(StrictLessThan(Add(Mul(Integer(2), Symbol('c')), Integer(1)), Integer(0)), Or(StrictLessThan(Add(Mul(Integer(2), Pow(Symbol('c'), Integer(3))), Mul(Integer(3), Pow(Symbol('c'), Integer(2))), Mul(Integer(-1), Integer(9), Symbol('c')), Integer(3)), Integer(0)), StrictLessThan(Add(Pow(Symbol('c'), Integer(4)), Mul(Integer(2), Pow(Symbol('c'), Integer(3))), Mul(Integer(-1), Integer(9), Pow(Symbol('c'), Integer(2))), Mul(Integer(6), Symbol('c')), Integer(13)), Integer(0))))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1(c:sympy.Rational):
	#64*c + 161 < 0

	pre_cond = StrictLessThan(Add(Mul(Integer(64), Symbol('c')), Integer(161)), Integer(0))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_2(c:sympy.Rational):
	#(2*c + 5 < 0) & (c**2 + 5*c + 3 < 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(2), Symbol('c')), Integer(5)), Integer(0)), StrictLessThan(Add(Pow(Symbol('c'), Integer(2)), Mul(Integer(5), Symbol('c')), Integer(3)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_3(c:sympy.Rational):
	#256*c + 185 < 0

	pre_cond = StrictLessThan(Add(Mul(Integer(256), Symbol('c')), Integer(185)), Integer(0))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_4(c:sympy.Rational):
	#(2*c + 5 < 0) & (c**2 + 5*c + 3 < 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(2), Symbol('c')), Integer(5)), Integer(0)), StrictLessThan(Add(Pow(Symbol('c'), Integer(2)), Mul(Integer(5), Symbol('c')), Integer(3)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_5(c:sympy.Rational):
	#64*c + 45 < 0

	pre_cond = StrictLessThan(Add(Mul(Integer(64), Symbol('c')), Integer(45)), Integer(0))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_6(c:sympy.Rational):
	#(2*c + 5 < 0) & (c**2 + 5*c + 3 < 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(2), Symbol('c')), Integer(5)), Integer(0)), StrictLessThan(Add(Pow(Symbol('c'), Integer(2)), Mul(Integer(5), Symbol('c')), Integer(3)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_7(c:sympy.Rational):
	#512*c + 357 < 0

	pre_cond = StrictLessThan(Add(Mul(Integer(512), Symbol('c')), Integer(357)), Integer(0))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_8(c:sympy.Rational):
	#(2*c + 5 < 0) & (c**2 + 5*c + 3 < 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(2), Symbol('c')), Integer(5)), Integer(0)), StrictLessThan(Add(Pow(Symbol('c'), Integer(2)), Mul(Integer(5), Symbol('c')), Integer(3)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_9(c:sympy.Rational):
	#131072*c + 91387 < 0

	pre_cond = StrictLessThan(Add(Mul(Integer(131072), Symbol('c')), Integer(91387)), Integer(0))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_10(c:sympy.Rational):
	#(2*c + 5 < 0) & (c**2 + 5*c + 3 < 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(2), Symbol('c')), Integer(5)), Integer(0)), StrictLessThan(Add(Pow(Symbol('c'), Integer(2)), Mul(Integer(5), Symbol('c')), Integer(3)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_11(c:sympy.Rational):
	#1048576*c + 731093 < 0

	pre_cond = StrictLessThan(Add(Mul(Integer(1048576), Symbol('c')), Integer(731093)), Integer(0))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_12(c:sympy.Rational):
	#(2*c + 5 < 0) & (c**2 + 5*c + 3 < 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(2), Symbol('c')), Integer(5)), Integer(0)), StrictLessThan(Add(Pow(Symbol('c'), Integer(2)), Mul(Integer(5), Symbol('c')), Integer(3)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_13(c:sympy.Rational):
	#67108864*c + 46789935 < 0

	pre_cond = StrictLessThan(Add(Mul(Integer(67108864), Symbol('c')), Integer(46789935)), Integer(0))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_14(c:sympy.Rational):
	#(2*c + 5 < 0) & (c**2 + 5*c + 3 < 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(2), Symbol('c')), Integer(5)), Integer(0)), StrictLessThan(Add(Pow(Symbol('c'), Integer(2)), Mul(Integer(5), Symbol('c')), Integer(3)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_15(c:sympy.Rational):
	#2147483648*c + 1497277917 < 0

	pre_cond = StrictLessThan(Add(Mul(Integer(2147483648), Symbol('c')), Integer(1497277917)), Integer(0))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_16(c:sympy.Rational):
	#(2*c + 5 < 0) & (c**2 + 5*c + 3 < 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(2), Symbol('c')), Integer(5)), Integer(0)), StrictLessThan(Add(Pow(Symbol('c'), Integer(2)), Mul(Integer(5), Symbol('c')), Integer(3)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_17(c:sympy.Rational):
	#274877906944*c + 191651573371 < 0

	pre_cond = StrictLessThan(Add(Mul(Integer(274877906944), Symbol('c')), Integer(191651573371)), Integer(0))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_18(c:sympy.Rational):
	#(2*c + 5 < 0) & (c**2 + 5*c + 3 < 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(2), Symbol('c')), Integer(5)), Integer(0)), StrictLessThan(Add(Pow(Symbol('c'), Integer(2)), Mul(Integer(5), Symbol('c')), Integer(3)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_19(c:sympy.Rational):
	#2199023255552*c + 1533212586965 < 0

	pre_cond = StrictLessThan(Add(Mul(Integer(2199023255552), Symbol('c')), Integer(1533212586965)), Integer(0))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_20(c:sympy.Rational):
	#(2*c + 5 < 0) & (c**2 + 5*c + 3 < 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(2), Symbol('c')), Integer(5)), Integer(0)), StrictLessThan(Add(Pow(Symbol('c'), Integer(2)), Mul(Integer(5), Symbol('c')), Integer(3)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_21(c:sympy.Rational):
	#77371252455336267181195264*c + 53945122151049237200458985 < 0

	pre_cond = StrictLessThan(Add(Mul(Integer(77371252455336267181195264), Symbol('c')), Integer(53945122151049237200458985)), Integer(0))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_22(c:sympy.Rational):
	#(2*c + 5 < 0) & (c**2 + 5*c + 3 < 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(2), Symbol('c')), Integer(5)), Integer(0)), StrictLessThan(Add(Pow(Symbol('c'), Integer(2)), Mul(Integer(5), Symbol('c')), Integer(3)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def post_condition(c:sympy.Rational, x:sympy.Rational, y:sympy.Rational):
	# (0 > -c**2 + x**2 + y**2) & (0 > c + x**2 - 4*x + y**2 + 3)

	post_cond =  And(StrictGreaterThan(Integer(0), Add(Mul(Integer(-1), Pow(Symbol('c'), Integer(2))), Pow(Symbol('x'), Integer(2)), Pow(Symbol('y'), Integer(2)))), StrictGreaterThan(Integer(0), Add(Symbol('c'), Pow(Symbol('x'), Integer(2)), Mul(Integer(-1), Integer(4), Symbol('x')), Pow(Symbol('y'), Integer(2)), Integer(3))))

	eval = post_cond.subs( { 'c':c, 'x':x, 'y':y })

	return eval == sympy.logic.boolalg.BooleanTrue



#return post-condition single variable
def return_post_condition_single_var(post_condition, c:sympy.Rational=None, x:sympy.Rational=None, y:sympy.Rational=None):
	assert c!=None


	if x==None:
		assert y!=None
		return lambda x: post_condition(c=c, x=x, y=y)

	if y==None:
		assert x!=None
		return lambda y: post_condition(c=c, x=x, y=y)


	return post_condition(c=c, x=x, y=y)


def get_univariate_poly( c:sympy.Rational, x:sympy.Rational, y:sympy.Rational ):


	post_cond =  And(StrictGreaterThan(Integer(0), Add(Mul(Integer(-1), Pow(Symbol('c'), Integer(2))), Pow(Symbol('x'), Integer(2)), Pow(Symbol('y'), Integer(2)))), StrictGreaterThan(Integer(0), Add(Symbol('c'), Pow(Symbol('x'), Integer(2)), Mul(Integer(-1), Integer(4), Symbol('x')), Pow(Symbol('y'), Integer(2)), Integer(3))))

	eval = post_cond.subs( { 'c':c, 'x':x, 'y':y })
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
	
	
	if pre_condition_1(c=c)==True:
		all_vals = dict()
		all_vals['c'] = c
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
	
	
	if pre_condition_2(c=c)==True:
		all_vals = dict()
		all_vals['c'] = c
		all_vals['x'] = Add(Symbol('lambda_var_0'), Rational(11, 16))
		all_vals['y'] = Integer(0)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_2 SAT")

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_3(c=c)==True:
		all_vals = dict()
		all_vals['c'] = c
		all_vals['x'] = Rational(11, 16)
		all_vals['y'] = Symbol('lambda_var_0')
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_3 SAT")

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_4(c=c)==True:
		all_vals = dict()
		all_vals['c'] = c
		all_vals['x'] = Add(Symbol('lambda_var_0'), Rational(45, 64))
		all_vals['y'] = Integer(0)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_4 SAT")

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_5(c=c)==True:
		all_vals = dict()
		all_vals['c'] = c
		all_vals['x'] = Rational(45, 64)
		all_vals['y'] = Symbol('lambda_var_0')
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_5 SAT")

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_6(c=c)==True:
		all_vals = dict()
		all_vals['c'] = c
		all_vals['x'] = Add(Symbol('lambda_var_0'), Rational(357, 512))
		all_vals['y'] = Integer(0)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_6 SAT")

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_7(c=c)==True:
		all_vals = dict()
		all_vals['c'] = c
		all_vals['x'] = Rational(357, 512)
		all_vals['y'] = Symbol('lambda_var_0')
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_7 SAT")

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_8(c=c)==True:
		all_vals = dict()
		all_vals['c'] = c
		all_vals['x'] = Add(Symbol('lambda_var_0'), Rational(91387, 131072))
		all_vals['y'] = Integer(0)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_8 SAT")

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_9(c=c)==True:
		all_vals = dict()
		all_vals['c'] = c
		all_vals['x'] = Rational(91387, 131072)
		all_vals['y'] = Symbol('lambda_var_0')
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_9 SAT")

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_10(c=c)==True:
		all_vals = dict()
		all_vals['c'] = c
		all_vals['x'] = Add(Symbol('lambda_var_0'), Rational(731093, 1048576))
		all_vals['y'] = Integer(0)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_10 SAT")

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_11(c=c)==True:
		all_vals = dict()
		all_vals['c'] = c
		all_vals['x'] = Rational(731093, 1048576)
		all_vals['y'] = Symbol('lambda_var_0')
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_11 SAT")

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_12(c=c)==True:
		all_vals = dict()
		all_vals['c'] = c
		all_vals['x'] = Add(Symbol('lambda_var_0'), Rational(46789935, 67108864))
		all_vals['y'] = Integer(0)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_12 SAT")

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_13(c=c)==True:
		all_vals = dict()
		all_vals['c'] = c
		all_vals['x'] = Rational(46789935, 67108864)
		all_vals['y'] = Symbol('lambda_var_0')
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_13 SAT")

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_14(c=c)==True:
		all_vals = dict()
		all_vals['c'] = c
		all_vals['x'] = Add(Symbol('lambda_var_0'), Rational(1497277917, 2147483648))
		all_vals['y'] = Integer(0)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_14 SAT")

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_15(c=c)==True:
		all_vals = dict()
		all_vals['c'] = c
		all_vals['x'] = Rational(1497277917, 2147483648)
		all_vals['y'] = Symbol('lambda_var_0')
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_15 SAT")

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_16(c=c)==True:
		all_vals = dict()
		all_vals['c'] = c
		all_vals['x'] = Add(Symbol('lambda_var_0'), Rational(191651573371, 274877906944))
		all_vals['y'] = Integer(0)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_16 SAT")

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_17(c=c)==True:
		all_vals = dict()
		all_vals['c'] = c
		all_vals['x'] = Rational(191651573371, 274877906944)
		all_vals['y'] = Symbol('lambda_var_0')
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_17 SAT")

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_18(c=c)==True:
		all_vals = dict()
		all_vals['c'] = c
		all_vals['x'] = Add(Symbol('lambda_var_0'), Rational(1533212586965, 2199023255552))
		all_vals['y'] = Integer(0)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_18 SAT")

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_19(c=c)==True:
		all_vals = dict()
		all_vals['c'] = c
		all_vals['x'] = Rational(1533212586965, 2199023255552)
		all_vals['y'] = Symbol('lambda_var_0')
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_19 SAT")

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_20(c=c)==True:
		all_vals = dict()
		all_vals['c'] = c
		all_vals['x'] = Add(Symbol('lambda_var_0'), Rational(6132850347859, 8796093022208))
		all_vals['y'] = Integer(0)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_20 SAT")

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_21(c=c)==True:
		all_vals = dict()
		all_vals['c'] = c
		all_vals['x'] = Rational(6132850347859, 8796093022208)
		all_vals['y'] = Symbol('lambda_var_0')
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_21 SAT")

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_22(c=c)==True:
		all_vals = dict()
		all_vals['c'] = c
		all_vals['x'] = Add(Symbol('lambda_var_0'), Rational(196251211131489, 281474976710656))
		all_vals['y'] = Integer(0)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_22 SAT")

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass


	print("UNKNOWN")
