import sympy
from sympy import *
from NQS.helper_program_cav import get_lambda_val

def pre_condition_0(z:sympy.Rational):
	#(z > 0) & (16*z - 1 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Integer(0)), StrictLessThan(Add(Mul(Integer(16), Symbol('z')), Integer(-1)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1(z:sympy.Rational):
	#(z > 0) & (8*z - 1 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Integer(0)), StrictLessThan(Add(Mul(Integer(8), Symbol('z')), Integer(-1)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_2(z:sympy.Rational):
	#(z > 0) & (4*z - 1 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Integer(0)), StrictLessThan(Add(Mul(Integer(4), Symbol('z')), Integer(-1)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_3(z:sympy.Rational):
	#(z > 0) & (z - 2 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Integer(0)), StrictLessThan(Add(Symbol('z'), Integer(-2)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_4(z:sympy.Rational):
	#(z > 0) & (z - 4 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Integer(0)), StrictLessThan(Add(Symbol('z'), Integer(-4)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_5(z:sympy.Rational):
	#(z > 0) & (z - 72 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Integer(0)), StrictLessThan(Add(Symbol('z'), Integer(-72)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_6(z:sympy.Rational):
	#(z > 0) & (4*z - 289 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Integer(0)), StrictLessThan(Add(Mul(Integer(4), Symbol('z')), Integer(-289)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_7(z:sympy.Rational):
	#(z > 0) & (z - 578 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Integer(0)), StrictLessThan(Add(Symbol('z'), Integer(-578)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_8(z:sympy.Rational):
	#(z > 0) & (z - 1156 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Integer(0)), StrictLessThan(Add(Symbol('z'), Integer(-1156)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_9(z:sympy.Rational):
	#(z > 0) & (z - 800 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Integer(0)), StrictLessThan(Add(Symbol('z'), Integer(-800)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_10(z:sympy.Rational):
	#(z > 0) & (4*z - 4761 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Integer(0)), StrictLessThan(Add(Mul(Integer(4), Symbol('z')), Integer(-4761)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_11(z:sympy.Rational):
	#(z > 0) & (z - 10368 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Integer(0)), StrictLessThan(Add(Symbol('z'), Integer(-10368)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_12(z:sympy.Rational):
	#(z > 0) & (z - 10404 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Integer(0)), StrictLessThan(Add(Symbol('z'), Integer(-10404)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_13(z:sympy.Rational):
	#(z > 0) & (z - 84872 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Integer(0)), StrictLessThan(Add(Symbol('z'), Integer(-84872)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_14(z:sympy.Rational):
	#(z > 0) & (4*z - 339889 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Integer(0)), StrictLessThan(Add(Mul(Integer(4), Symbol('z')), Integer(-339889)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_15(z:sympy.Rational):
	#(z > 0) & (z - 686792 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Integer(0)), StrictLessThan(Add(Symbol('z'), Integer(-686792)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_16(z:sympy.Rational):
	#(z > 0) & (4*z - 6996025 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Integer(0)), StrictLessThan(Add(Mul(Integer(4), Symbol('z')), Integer(-6996025)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_17(z:sympy.Rational):
	#(z > 0) & (z - 691488 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Integer(0)), StrictLessThan(Add(Symbol('z'), Integer(-691488)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_18(z:sympy.Rational):
	#(z > 0) & (z - 1750329 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Integer(0)), StrictLessThan(Add(Symbol('z'), Integer(-1750329)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_19(z:sympy.Rational):
	#(z > 0) & (z - 14023808 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Integer(0)), StrictLessThan(Add(Symbol('z'), Integer(-14023808)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_20(z:sympy.Rational):
	#(z > 0) & (z - 35545444 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Integer(0)), StrictLessThan(Add(Symbol('z'), Integer(-35545444)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_21(z:sympy.Rational):
	#(z > 0) & (z - 14045000 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Integer(0)), StrictLessThan(Add(Symbol('z'), Integer(-14045000)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_22(z:sympy.Rational):
	#(z > 0) & (4*z - 359898841 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Integer(0)), StrictLessThan(Add(Mul(Integer(4), Symbol('z')), Integer(-359898841)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_23(z:sympy.Rational):
	#(z > 0) & (z - 35549312 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Integer(0)), StrictLessThan(Add(Symbol('z'), Integer(-35549312)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def post_condition(z:sympy.Rational, y:sympy.Rational, x:sympy.Rational):
	# (0 > -x*y + y**2 + z) & (0 > x**2 - y**2 - 10*z)

	post_cond =  And(StrictGreaterThan(Integer(0), Add(Mul(Integer(-1), Symbol('x'), Symbol('y')), Pow(Symbol('y'), Integer(2)), Symbol('z'))), StrictGreaterThan(Integer(0), Add(Pow(Symbol('x'), Integer(2)), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Mul(Integer(-1), Integer(10), Symbol('z')))))

	eval = post_cond.subs( { 'z':z, 'y':y, 'x':x })

	return eval == sympy.logic.boolalg.BooleanTrue



#return post-condition single variable
def return_post_condition_single_var(post_condition, z:sympy.Rational=None, y:sympy.Rational=None, x:sympy.Rational=None):
	assert z!=None


	if y==None:
		assert x!=None
		return lambda y: post_condition(z=z, y=y, x=x)

	if x==None:
		assert y!=None
		return lambda x: post_condition(z=z, y=y, x=x)


	return post_condition(z=z, y=y, x=x)


def get_univariate_poly( z:sympy.Rational, y:sympy.Rational, x:sympy.Rational ):


	post_cond =  And(StrictGreaterThan(Integer(0), Add(Mul(Integer(-1), Symbol('x'), Symbol('y')), Pow(Symbol('y'), Integer(2)), Symbol('z'))), StrictGreaterThan(Integer(0), Add(Pow(Symbol('x'), Integer(2)), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Mul(Integer(-1), Integer(10), Symbol('z')))))

	eval = post_cond.subs( { 'z':z, 'y':y, 'x':x })
	return eval



if __name__=="__main__":
	
	ip_0=int(input("enter numerator of z:\n"))
	ip_1=int(input("enter denominator of z:\n"))
	assert(ip_1!=0), ("Error denominator entered is 0")
	z=sympy.Rational(ip_0,ip_1)
	
	
	lambda_var_0 = sympy.symbols('lambda_var_0')
	
	
	if pre_condition_0(z=z)==True:
		all_vals = dict()
		all_vals['z'] = z
		all_vals['y'] = Add(Symbol('lambda_var_0'), Rational(1, 8))
		all_vals['x'] = Rational(1, 2)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_0 SAT")

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_1(z=z)==True:
		all_vals = dict()
		all_vals['z'] = z
		all_vals['y'] = Rational(1, 8)
		all_vals['x'] = Add(Symbol('lambda_var_0'), Rational(1, 2))
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_1 SAT")

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_2(z=z)==True:
		all_vals = dict()
		all_vals['z'] = z
		all_vals['y'] = Add(Symbol('lambda_var_0'), Rational(-1, 2))
		all_vals['x'] = Integer(-1)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_2 SAT")

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_3(z=z)==True:
		all_vals = dict()
		all_vals['z'] = z
		all_vals['y'] = Rational(-1, 2)
		all_vals['x'] = Add(Symbol('lambda_var_0'), Integer(-1))
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_3 SAT")

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_4(z=z)==True:
		all_vals = dict()
		all_vals['z'] = z
		all_vals['y'] = Add(Symbol('lambda_var_0'), Integer(3))
		all_vals['x'] = Integer(4)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_4 SAT")

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_5(z=z)==True:
		all_vals = dict()
		all_vals['z'] = z
		all_vals['y'] = Integer(3)
		all_vals['x'] = Add(Symbol('lambda_var_0'), Integer(4))
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_5 SAT")

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_6(z=z)==True:
		all_vals = dict()
		all_vals['z'] = z
		all_vals['y'] = Add(Symbol('lambda_var_0'), Rational(-17, 2))
		all_vals['x'] = Integer(-17)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_6 SAT")

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_7(z=z)==True:
		all_vals = dict()
		all_vals['z'] = z
		all_vals['y'] = Rational(-17, 2)
		all_vals['x'] = Add(Symbol('lambda_var_0'), Integer(-17))
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_7 SAT")

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_8(z=z)==True:
		all_vals = dict()
		all_vals['z'] = z
		all_vals['y'] = Add(Symbol('lambda_var_0'), Integer(10))
		all_vals['x'] = Integer(68)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_8 SAT")

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_9(z=z)==True:
		all_vals = dict()
		all_vals['z'] = z
		all_vals['y'] = Integer(10)
		all_vals['x'] = Add(Symbol('lambda_var_0'), Integer(68))
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_9 SAT")

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_10(z=z)==True:
		all_vals = dict()
		all_vals['z'] = z
		all_vals['y'] = Add(Symbol('lambda_var_0'), Integer(36))
		all_vals['x'] = Integer(69)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_10 SAT")

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_11(z=z)==True:
		all_vals = dict()
		all_vals['z'] = z
		all_vals['y'] = Integer(36)
		all_vals['x'] = Add(Symbol('lambda_var_0'), Integer(69))
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_11 SAT")

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_12(z=z)==True:
		all_vals = dict()
		all_vals['z'] = z
		all_vals['y'] = Add(Symbol('lambda_var_0'), Integer(-103))
		all_vals['x'] = Integer(-204)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_12 SAT")

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_13(z=z)==True:
		all_vals = dict()
		all_vals['z'] = z
		all_vals['y'] = Integer(-103)
		all_vals['x'] = Add(Symbol('lambda_var_0'), Integer(-204))
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_13 SAT")

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_14(z=z)==True:
		all_vals = dict()
		all_vals['z'] = z
		all_vals['y'] = Add(Symbol('lambda_var_0'), Integer(-293))
		all_vals['x'] = Integer(-583)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_14 SAT")

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_15(z=z)==True:
		all_vals = dict()
		all_vals['z'] = z
		all_vals['y'] = Integer(-293)
		all_vals['x'] = Add(Symbol('lambda_var_0'), Integer(-583))
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_15 SAT")

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_16(z=z)==True:
		all_vals = dict()
		all_vals['z'] = z
		all_vals['y'] = Add(Symbol('lambda_var_0'), Integer(-294))
		all_vals['x'] = Integer(-2645)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_16 SAT")

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_17(z=z)==True:
		all_vals = dict()
		all_vals['z'] = z
		all_vals['y'] = Integer(-294)
		all_vals['x'] = Add(Symbol('lambda_var_0'), Integer(-2645))
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_17 SAT")

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_18(z=z)==True:
		all_vals = dict()
		all_vals['z'] = z
		all_vals['y'] = Add(Symbol('lambda_var_0'), Integer(-1324))
		all_vals['x'] = Integer(-2646)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_18 SAT")

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_19(z=z)==True:
		all_vals = dict()
		all_vals['z'] = z
		all_vals['y'] = Integer(-1324)
		all_vals['x'] = Add(Symbol('lambda_var_0'), Integer(-2646))
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_19 SAT")

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_20(z=z)==True:
		all_vals = dict()
		all_vals['z'] = z
		all_vals['y'] = Add(Symbol('lambda_var_0'), Integer(-1325))
		all_vals['x'] = Integer(-11924)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_20 SAT")

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_21(z=z)==True:
		all_vals = dict()
		all_vals['z'] = z
		all_vals['y'] = Integer(-1325)
		all_vals['x'] = Add(Symbol('lambda_var_0'), Integer(-11924))
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_21 SAT")

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_22(z=z)==True:
		all_vals = dict()
		all_vals['z'] = z
		all_vals['y'] = Add(Symbol('lambda_var_0'), Integer(-2108))
		all_vals['x'] = Integer(-18971)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_22 SAT")

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_23(z=z)==True:
		all_vals = dict()
		all_vals['z'] = z
		all_vals['y'] = Integer(-2108)
		all_vals['x'] = Add(Symbol('lambda_var_0'), Integer(-18971))
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_23 SAT")

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass


	print("UNKNOWN")
