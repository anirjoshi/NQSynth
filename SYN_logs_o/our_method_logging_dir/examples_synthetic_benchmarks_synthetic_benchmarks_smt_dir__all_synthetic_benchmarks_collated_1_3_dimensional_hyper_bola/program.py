import sympy
from sympy import *
from NQS.helper_program_cav import get_lambda_val

def pre_condition_0(a:sympy.Rational):
	#(a - 1 < 0) & ((4*a + 5 > 0) | (a**4 + 2*a**3 - 7*a**2 + 4*a + 4 < 0))

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Integer(-1)), Integer(0)), Or(StrictGreaterThan(Add(Mul(Integer(4), Symbol('a')), Integer(5)), Integer(0)), StrictLessThan(Add(Pow(Symbol('a'), Integer(4)), Mul(Integer(2), Pow(Symbol('a'), Integer(3))), Mul(Integer(-1), Integer(7), Pow(Symbol('a'), Integer(2))), Mul(Integer(4), Symbol('a')), Integer(4)), Integer(0))))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1(a:sympy.Rational):
	#(2*a + 3 > 0) & (4*a - 3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(2), Symbol('a')), Integer(3)), Integer(0)), StrictLessThan(Add(Mul(Integer(4), Symbol('a')), Integer(-3)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_2(a:sympy.Rational):
	#4*a**2 - 4*a - 11 < 0

	pre_cond = StrictLessThan(Add(Mul(Integer(4), Pow(Symbol('a'), Integer(2))), Mul(Integer(-1), Integer(4), Symbol('a')), Integer(-11)), Integer(0))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_3(a:sympy.Rational):
	#(6*a**2 + 6*a - 23 < 0) & (a**4 + 2*a**3 - 23*a**2 - 12*a + 36 < 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(6), Pow(Symbol('a'), Integer(2))), Mul(Integer(6), Symbol('a')), Integer(-23)), Integer(0)), StrictLessThan(Add(Pow(Symbol('a'), Integer(4)), Mul(Integer(2), Pow(Symbol('a'), Integer(3))), Mul(Integer(-1), Integer(23), Pow(Symbol('a'), Integer(2))), Mul(Integer(-1), Integer(12), Symbol('a')), Integer(36)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_4(a:sympy.Rational):
	#(a > 0) & (a - 4 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(0)), StrictLessThan(Add(Symbol('a'), Integer(-4)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_5(a:sympy.Rational):
	#a**2 - 4*a + 1 < 0

	pre_cond = StrictLessThan(Add(Pow(Symbol('a'), Integer(2)), Mul(Integer(-1), Integer(4), Symbol('a')), Integer(1)), Integer(0))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_6(a:sympy.Rational):
	#(a**2 - 3*a - 11 < 0) & (a**2 + 5*a - 11 < 0)

	pre_cond = And(StrictLessThan(Add(Pow(Symbol('a'), Integer(2)), Mul(Integer(-1), Integer(3), Symbol('a')), Integer(-11)), Integer(0)), StrictLessThan(Add(Pow(Symbol('a'), Integer(2)), Mul(Integer(5), Symbol('a')), Integer(-11)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_7(a:sympy.Rational):
	#(8*a - 9 > 0) & (8*a - 41 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(8), Symbol('a')), Integer(-9)), Integer(0)), StrictLessThan(Add(Mul(Integer(8), Symbol('a')), Integer(-41)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_8(a:sympy.Rational):
	#(8*a - 9 > 0) & (8*a - 41 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(8), Symbol('a')), Integer(-9)), Integer(0)), StrictLessThan(Add(Mul(Integer(8), Symbol('a')), Integer(-41)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_9(a:sympy.Rational):
	#(a**2 - 3*a - 44 < 0) & (a**2 + 5*a - 44 < 0)

	pre_cond = And(StrictLessThan(Add(Pow(Symbol('a'), Integer(2)), Mul(Integer(-1), Integer(3), Symbol('a')), Integer(-44)), Integer(0)), StrictLessThan(Add(Pow(Symbol('a'), Integer(2)), Mul(Integer(5), Symbol('a')), Integer(-44)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_10(a:sympy.Rational):
	#(a - 4 > 0) & (a - 8 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Integer(-4)), Integer(0)), StrictLessThan(Add(Symbol('a'), Integer(-8)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_11(a:sympy.Rational):
	#(a - 4 > 0) & (a - 8 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Integer(-4)), Integer(0)), StrictLessThan(Add(Symbol('a'), Integer(-8)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_12(a:sympy.Rational):
	#(a**2 - 3*a - 76 < 0) & (a**2 + 5*a - 76 < 0)

	pre_cond = And(StrictLessThan(Add(Pow(Symbol('a'), Integer(2)), Mul(Integer(-1), Integer(3), Symbol('a')), Integer(-76)), Integer(0)), StrictLessThan(Add(Pow(Symbol('a'), Integer(2)), Mul(Integer(5), Symbol('a')), Integer(-76)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_13(a:sympy.Rational):
	#(a - 6 > 0) & (a - 10 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Integer(-6)), Integer(0)), StrictLessThan(Add(Symbol('a'), Integer(-10)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_14(a:sympy.Rational):
	#(a - 6 > 0) & (a - 10 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Integer(-6)), Integer(0)), StrictLessThan(Add(Symbol('a'), Integer(-10)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_15(a:sympy.Rational):
	#(a**2 - 3*a - 116 < 0) & (a**2 + 5*a - 116 < 0)

	pre_cond = And(StrictLessThan(Add(Pow(Symbol('a'), Integer(2)), Mul(Integer(-1), Integer(3), Symbol('a')), Integer(-116)), Integer(0)), StrictLessThan(Add(Pow(Symbol('a'), Integer(2)), Mul(Integer(5), Symbol('a')), Integer(-116)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_16(a:sympy.Rational):
	#(a - 8 > 0) & (a - 12 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Integer(-8)), Integer(0)), StrictLessThan(Add(Symbol('a'), Integer(-12)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_17(a:sympy.Rational):
	#(a - 8 > 0) & (a - 12 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Integer(-8)), Integer(0)), StrictLessThan(Add(Symbol('a'), Integer(-12)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_18(a:sympy.Rational):
	#(a**2 - 3*a - 164 < 0) & (a**2 + 5*a - 164 < 0)

	pre_cond = And(StrictLessThan(Add(Pow(Symbol('a'), Integer(2)), Mul(Integer(-1), Integer(3), Symbol('a')), Integer(-164)), Integer(0)), StrictLessThan(Add(Pow(Symbol('a'), Integer(2)), Mul(Integer(5), Symbol('a')), Integer(-164)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_19(a:sympy.Rational):
	#(a - 10 > 0) & (a - 14 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Integer(-10)), Integer(0)), StrictLessThan(Add(Symbol('a'), Integer(-14)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_20(a:sympy.Rational):
	#(a - 10 > 0) & (a - 14 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Integer(-10)), Integer(0)), StrictLessThan(Add(Symbol('a'), Integer(-14)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_21(a:sympy.Rational):
	#(a**2 - 3*a - 220 < 0) & (a**2 + 5*a - 220 < 0)

	pre_cond = And(StrictLessThan(Add(Pow(Symbol('a'), Integer(2)), Mul(Integer(-1), Integer(3), Symbol('a')), Integer(-220)), Integer(0)), StrictLessThan(Add(Pow(Symbol('a'), Integer(2)), Mul(Integer(5), Symbol('a')), Integer(-220)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_22(a:sympy.Rational):
	#(a - 12 > 0) & (a - 16 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Integer(-12)), Integer(0)), StrictLessThan(Add(Symbol('a'), Integer(-16)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_23(a:sympy.Rational):
	#(a - 12 > 0) & (a - 16 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Integer(-12)), Integer(0)), StrictLessThan(Add(Symbol('a'), Integer(-16)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def post_condition(a:sympy.Rational, x:sympy.Rational, y:sympy.Rational, z:sympy.Rational):
	# (0 > a + x**2 + y**2 - z**2) & (0 > a**2 - 2*a*x + x**2 + y**2 - 2*y - 3)

	post_cond =  And(StrictGreaterThan(Integer(0), Add(Symbol('a'), Pow(Symbol('x'), Integer(2)), Pow(Symbol('y'), Integer(2)), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))))), StrictGreaterThan(Integer(0), Add(Pow(Symbol('a'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('a'), Symbol('x')), Pow(Symbol('x'), Integer(2)), Pow(Symbol('y'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('y')), Integer(-3))))

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


	post_cond =  And(StrictGreaterThan(Integer(0), Add(Symbol('a'), Pow(Symbol('x'), Integer(2)), Pow(Symbol('y'), Integer(2)), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))))), StrictGreaterThan(Integer(0), Add(Pow(Symbol('a'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('a'), Symbol('x')), Pow(Symbol('x'), Integer(2)), Pow(Symbol('y'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('y')), Integer(-3))))

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
		all_vals['y'] = Integer(0)
		all_vals['z'] = Integer(-1)
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
		all_vals['y'] = Symbol('lambda_var_0')
		all_vals['z'] = Integer(-1)
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
		all_vals['y'] = Integer(0)
		all_vals['z'] = Add(Symbol('lambda_var_0'), Integer(-1))
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
	
	
	if pre_condition_3(a=a)==True:
		all_vals = dict()
		all_vals['a'] = a
		all_vals['x'] = Add(Symbol('lambda_var_0'), Integer(2))
		all_vals['y'] = Integer(0)
		all_vals['z'] = Integer(-3)
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
	
	
	if pre_condition_4(a=a)==True:
		all_vals = dict()
		all_vals['a'] = a
		all_vals['x'] = Integer(2)
		all_vals['y'] = Symbol('lambda_var_0')
		all_vals['z'] = Integer(-3)
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
	
	
	if pre_condition_5(a=a)==True:
		all_vals = dict()
		all_vals['a'] = a
		all_vals['x'] = Integer(2)
		all_vals['y'] = Integer(0)
		all_vals['z'] = Add(Symbol('lambda_var_0'), Integer(-3))
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
	
	
	if pre_condition_6(a=a)==True:
		all_vals = dict()
		all_vals['a'] = a
		all_vals['x'] = Add(Symbol('lambda_var_0'), Rational(25, 8))
		all_vals['y'] = Integer(1)
		all_vals['z'] = Integer(-4)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_6 SAT")

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("z=", all_vals["z"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_7(a=a)==True:
		all_vals = dict()
		all_vals['a'] = a
		all_vals['x'] = Rational(25, 8)
		all_vals['y'] = Add(Symbol('lambda_var_0'), Integer(1))
		all_vals['z'] = Integer(-4)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_7 SAT")

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("z=", all_vals["z"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_8(a=a)==True:
		all_vals = dict()
		all_vals['a'] = a
		all_vals['x'] = Rational(25, 8)
		all_vals['y'] = Integer(1)
		all_vals['z'] = Add(Symbol('lambda_var_0'), Integer(-4))
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_8 SAT")

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("z=", all_vals["z"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_9(a=a)==True:
		all_vals = dict()
		all_vals['a'] = a
		all_vals['x'] = Add(Symbol('lambda_var_0'), Integer(6))
		all_vals['y'] = Integer(1)
		all_vals['z'] = Integer(-7)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_9 SAT")

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("z=", all_vals["z"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_10(a=a)==True:
		all_vals = dict()
		all_vals['a'] = a
		all_vals['x'] = Integer(6)
		all_vals['y'] = Add(Symbol('lambda_var_0'), Integer(1))
		all_vals['z'] = Integer(-7)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_10 SAT")

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("z=", all_vals["z"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_11(a=a)==True:
		all_vals = dict()
		all_vals['a'] = a
		all_vals['x'] = Integer(6)
		all_vals['y'] = Integer(1)
		all_vals['z'] = Add(Symbol('lambda_var_0'), Integer(-7))
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_11 SAT")

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("z=", all_vals["z"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_12(a=a)==True:
		all_vals = dict()
		all_vals['a'] = a
		all_vals['x'] = Add(Symbol('lambda_var_0'), Integer(8))
		all_vals['y'] = Integer(1)
		all_vals['z'] = Integer(-9)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_12 SAT")

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("z=", all_vals["z"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_13(a=a)==True:
		all_vals = dict()
		all_vals['a'] = a
		all_vals['x'] = Integer(8)
		all_vals['y'] = Add(Symbol('lambda_var_0'), Integer(1))
		all_vals['z'] = Integer(-9)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_13 SAT")

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("z=", all_vals["z"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_14(a=a)==True:
		all_vals = dict()
		all_vals['a'] = a
		all_vals['x'] = Integer(8)
		all_vals['y'] = Integer(1)
		all_vals['z'] = Add(Symbol('lambda_var_0'), Integer(-9))
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_14 SAT")

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("z=", all_vals["z"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_15(a=a)==True:
		all_vals = dict()
		all_vals['a'] = a
		all_vals['x'] = Add(Symbol('lambda_var_0'), Integer(10))
		all_vals['y'] = Integer(1)
		all_vals['z'] = Integer(-11)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_15 SAT")

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("z=", all_vals["z"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_16(a=a)==True:
		all_vals = dict()
		all_vals['a'] = a
		all_vals['x'] = Integer(10)
		all_vals['y'] = Add(Symbol('lambda_var_0'), Integer(1))
		all_vals['z'] = Integer(-11)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_16 SAT")

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("z=", all_vals["z"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_17(a=a)==True:
		all_vals = dict()
		all_vals['a'] = a
		all_vals['x'] = Integer(10)
		all_vals['y'] = Integer(1)
		all_vals['z'] = Add(Symbol('lambda_var_0'), Integer(-11))
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_17 SAT")

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("z=", all_vals["z"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_18(a=a)==True:
		all_vals = dict()
		all_vals['a'] = a
		all_vals['x'] = Add(Symbol('lambda_var_0'), Integer(12))
		all_vals['y'] = Integer(1)
		all_vals['z'] = Integer(-13)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_18 SAT")

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("z=", all_vals["z"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_19(a=a)==True:
		all_vals = dict()
		all_vals['a'] = a
		all_vals['x'] = Integer(12)
		all_vals['y'] = Add(Symbol('lambda_var_0'), Integer(1))
		all_vals['z'] = Integer(-13)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_19 SAT")

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("z=", all_vals["z"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_20(a=a)==True:
		all_vals = dict()
		all_vals['a'] = a
		all_vals['x'] = Integer(12)
		all_vals['y'] = Integer(1)
		all_vals['z'] = Add(Symbol('lambda_var_0'), Integer(-13))
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_20 SAT")

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("z=", all_vals["z"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_21(a=a)==True:
		all_vals = dict()
		all_vals['a'] = a
		all_vals['x'] = Add(Symbol('lambda_var_0'), Integer(14))
		all_vals['y'] = Integer(1)
		all_vals['z'] = Integer(-15)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_21 SAT")

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("z=", all_vals["z"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_22(a=a)==True:
		all_vals = dict()
		all_vals['a'] = a
		all_vals['x'] = Integer(14)
		all_vals['y'] = Add(Symbol('lambda_var_0'), Integer(1))
		all_vals['z'] = Integer(-15)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_22 SAT")

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("z=", all_vals["z"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_23(a=a)==True:
		all_vals = dict()
		all_vals['a'] = a
		all_vals['x'] = Integer(14)
		all_vals['y'] = Integer(1)
		all_vals['z'] = Add(Symbol('lambda_var_0'), Integer(-15))
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_23 SAT")

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("z=", all_vals["z"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass


	print("UNKNOWN")
