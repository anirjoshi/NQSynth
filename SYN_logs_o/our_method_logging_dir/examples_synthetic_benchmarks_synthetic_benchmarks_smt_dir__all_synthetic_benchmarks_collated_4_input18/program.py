import sympy
from sympy import *
from NQS.helper_program_cav import get_lambda_val

def pre_condition_0(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#c > 0

	pre_cond = StrictGreaterThan(Symbol('c'), Integer(0))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#b > 0

	pre_cond = StrictGreaterThan(Symbol('b'), Integer(0))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_2(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#a > 0

	pre_cond = StrictGreaterThan(Symbol('a'), Integer(0))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_3(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#c + 1 > 0

	pre_cond = StrictGreaterThan(Add(Symbol('c'), Integer(1)), Integer(0))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_4(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#b + 2 > 0

	pre_cond = StrictGreaterThan(Add(Symbol('b'), Integer(2)), Integer(0))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_5(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#a + 1 > 0

	pre_cond = StrictGreaterThan(Add(Symbol('a'), Integer(1)), Integer(0))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_6(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#c + 8 > 0

	pre_cond = StrictGreaterThan(Add(Symbol('c'), Integer(8)), Integer(0))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_7(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#b + 16 > 0

	pre_cond = StrictGreaterThan(Add(Symbol('b'), Integer(16)), Integer(0))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_8(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#a + 8 > 0

	pre_cond = StrictGreaterThan(Add(Symbol('a'), Integer(8)), Integer(0))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_9(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#c + 27 > 0

	pre_cond = StrictGreaterThan(Add(Symbol('c'), Integer(27)), Integer(0))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_10(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#b + 54 > 0

	pre_cond = StrictGreaterThan(Add(Symbol('b'), Integer(54)), Integer(0))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_11(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#a + 27 > 0

	pre_cond = StrictGreaterThan(Add(Symbol('a'), Integer(27)), Integer(0))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_12(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#c + 64 > 0

	pre_cond = StrictGreaterThan(Add(Symbol('c'), Integer(64)), Integer(0))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_13(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#b + 128 > 0

	pre_cond = StrictGreaterThan(Add(Symbol('b'), Integer(128)), Integer(0))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_14(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#a + 64 > 0

	pre_cond = StrictGreaterThan(Add(Symbol('a'), Integer(64)), Integer(0))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_15(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#c + 125 > 0

	pre_cond = StrictGreaterThan(Add(Symbol('c'), Integer(125)), Integer(0))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_16(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#b + 250 > 0

	pre_cond = StrictGreaterThan(Add(Symbol('b'), Integer(250)), Integer(0))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_17(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#a + 125 > 0

	pre_cond = StrictGreaterThan(Add(Symbol('a'), Integer(125)), Integer(0))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_18(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#c + 216 > 0

	pre_cond = StrictGreaterThan(Add(Symbol('c'), Integer(216)), Integer(0))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_19(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#b + 728 > 0

	pre_cond = StrictGreaterThan(Add(Symbol('b'), Integer(728)), Integer(0))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_20(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#a + 512 > 0

	pre_cond = StrictGreaterThan(Add(Symbol('a'), Integer(512)), Integer(0))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_21(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#c + 343 > 0

	pre_cond = StrictGreaterThan(Add(Symbol('c'), Integer(343)), Integer(0))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def post_condition(a:sympy.Rational, b:sympy.Rational, c:sympy.Rational, x:sympy.Rational, y:sympy.Rational, z:sympy.Rational):
	# (0 > -a + x**3 + y**3) & (0 > -b + x**3 + z**3) & (0 > -c + y**3 + z**3)

	post_cond =  And(StrictGreaterThan(Integer(0), Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('x'), Integer(3)), Pow(Symbol('y'), Integer(3)))), StrictGreaterThan(Integer(0), Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('x'), Integer(3)), Pow(Symbol('z'), Integer(3)))), StrictGreaterThan(Integer(0), Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3)))))

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


	post_cond =  And(StrictGreaterThan(Integer(0), Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('x'), Integer(3)), Pow(Symbol('y'), Integer(3)))), StrictGreaterThan(Integer(0), Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('x'), Integer(3)), Pow(Symbol('z'), Integer(3)))), StrictGreaterThan(Integer(0), Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3)))))

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
	
	
	if pre_condition_3(a=a,b=b,c=c)==True:
		all_vals = dict()
		all_vals['a'] = a
		all_vals['b'] = b
		all_vals['c'] = c
		all_vals['x'] = Add(Symbol('lambda_var_0'), Integer(-1))
		all_vals['y'] = Integer(0)
		all_vals['z'] = Integer(-1)
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
	
	
	if pre_condition_4(a=a,b=b,c=c)==True:
		all_vals = dict()
		all_vals['a'] = a
		all_vals['b'] = b
		all_vals['c'] = c
		all_vals['x'] = Integer(-1)
		all_vals['y'] = Symbol('lambda_var_0')
		all_vals['z'] = Integer(-1)
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
	
	
	if pre_condition_5(a=a,b=b,c=c)==True:
		all_vals = dict()
		all_vals['a'] = a
		all_vals['b'] = b
		all_vals['c'] = c
		all_vals['x'] = Integer(-1)
		all_vals['y'] = Integer(0)
		all_vals['z'] = Add(Symbol('lambda_var_0'), Integer(-1))
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
	
	
	if pre_condition_6(a=a,b=b,c=c)==True:
		all_vals = dict()
		all_vals['a'] = a
		all_vals['b'] = b
		all_vals['c'] = c
		all_vals['x'] = Add(Symbol('lambda_var_0'), Integer(-2))
		all_vals['y'] = Integer(0)
		all_vals['z'] = Integer(-2)
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
	
	
	if pre_condition_7(a=a,b=b,c=c)==True:
		all_vals = dict()
		all_vals['a'] = a
		all_vals['b'] = b
		all_vals['c'] = c
		all_vals['x'] = Integer(-2)
		all_vals['y'] = Symbol('lambda_var_0')
		all_vals['z'] = Integer(-2)
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
	
	
	if pre_condition_8(a=a,b=b,c=c)==True:
		all_vals = dict()
		all_vals['a'] = a
		all_vals['b'] = b
		all_vals['c'] = c
		all_vals['x'] = Integer(-2)
		all_vals['y'] = Integer(0)
		all_vals['z'] = Add(Symbol('lambda_var_0'), Integer(-2))
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
	
	
	if pre_condition_9(a=a,b=b,c=c)==True:
		all_vals = dict()
		all_vals['a'] = a
		all_vals['b'] = b
		all_vals['c'] = c
		all_vals['x'] = Add(Symbol('lambda_var_0'), Integer(-3))
		all_vals['y'] = Integer(0)
		all_vals['z'] = Integer(-3)
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
	
	
	if pre_condition_10(a=a,b=b,c=c)==True:
		all_vals = dict()
		all_vals['a'] = a
		all_vals['b'] = b
		all_vals['c'] = c
		all_vals['x'] = Integer(-3)
		all_vals['y'] = Symbol('lambda_var_0')
		all_vals['z'] = Integer(-3)
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
	
	
	if pre_condition_11(a=a,b=b,c=c)==True:
		all_vals = dict()
		all_vals['a'] = a
		all_vals['b'] = b
		all_vals['c'] = c
		all_vals['x'] = Integer(-3)
		all_vals['y'] = Integer(0)
		all_vals['z'] = Add(Symbol('lambda_var_0'), Integer(-3))
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
	
	
	if pre_condition_12(a=a,b=b,c=c)==True:
		all_vals = dict()
		all_vals['a'] = a
		all_vals['b'] = b
		all_vals['c'] = c
		all_vals['x'] = Add(Symbol('lambda_var_0'), Integer(-4))
		all_vals['y'] = Integer(0)
		all_vals['z'] = Integer(-4)
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
	
	
	if pre_condition_13(a=a,b=b,c=c)==True:
		all_vals = dict()
		all_vals['a'] = a
		all_vals['b'] = b
		all_vals['c'] = c
		all_vals['x'] = Integer(-4)
		all_vals['y'] = Symbol('lambda_var_0')
		all_vals['z'] = Integer(-4)
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
	
	
	if pre_condition_14(a=a,b=b,c=c)==True:
		all_vals = dict()
		all_vals['a'] = a
		all_vals['b'] = b
		all_vals['c'] = c
		all_vals['x'] = Integer(-4)
		all_vals['y'] = Integer(0)
		all_vals['z'] = Add(Symbol('lambda_var_0'), Integer(-4))
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
	
	
	if pre_condition_15(a=a,b=b,c=c)==True:
		all_vals = dict()
		all_vals['a'] = a
		all_vals['b'] = b
		all_vals['c'] = c
		all_vals['x'] = Add(Symbol('lambda_var_0'), Integer(-5))
		all_vals['y'] = Integer(0)
		all_vals['z'] = Integer(-5)
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
	
	
	if pre_condition_16(a=a,b=b,c=c)==True:
		all_vals = dict()
		all_vals['a'] = a
		all_vals['b'] = b
		all_vals['c'] = c
		all_vals['x'] = Integer(-5)
		all_vals['y'] = Symbol('lambda_var_0')
		all_vals['z'] = Integer(-5)
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
	
	
	if pre_condition_17(a=a,b=b,c=c)==True:
		all_vals = dict()
		all_vals['a'] = a
		all_vals['b'] = b
		all_vals['c'] = c
		all_vals['x'] = Integer(-5)
		all_vals['y'] = Integer(0)
		all_vals['z'] = Add(Symbol('lambda_var_0'), Integer(-5))
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
	
	
	if pre_condition_18(a=a,b=b,c=c)==True:
		all_vals = dict()
		all_vals['a'] = a
		all_vals['b'] = b
		all_vals['c'] = c
		all_vals['x'] = Add(Symbol('lambda_var_0'), Integer(-8))
		all_vals['y'] = Integer(0)
		all_vals['z'] = Integer(-6)
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
	
	
	if pre_condition_19(a=a,b=b,c=c)==True:
		all_vals = dict()
		all_vals['a'] = a
		all_vals['b'] = b
		all_vals['c'] = c
		all_vals['x'] = Integer(-8)
		all_vals['y'] = Symbol('lambda_var_0')
		all_vals['z'] = Integer(-6)
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
	
	
	if pre_condition_20(a=a,b=b,c=c)==True:
		all_vals = dict()
		all_vals['a'] = a
		all_vals['b'] = b
		all_vals['c'] = c
		all_vals['x'] = Integer(-8)
		all_vals['y'] = Integer(0)
		all_vals['z'] = Add(Symbol('lambda_var_0'), Integer(-6))
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
	
	
	if pre_condition_21(a=a,b=b,c=c)==True:
		all_vals = dict()
		all_vals['a'] = a
		all_vals['b'] = b
		all_vals['c'] = c
		all_vals['x'] = Add(Symbol('lambda_var_0'), Integer(-16))
		all_vals['y'] = Integer(0)
		all_vals['z'] = Integer(-7)
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


	print("UNKNOWN")
