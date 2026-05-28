import sympy
from sympy import *
from NQS.helper_program_cav import get_lambda_val

def pre_condition_0(a:sympy.Rational,b:sympy.Rational):
	#(b + 1 > 0) & (b - 1 < 0) & (((a >= 0) & (a - 1 < 0)) | ((a < 0) & (a + 1 > 0)) | (a**2 - 2*a + b**2 < 0) | (a**2 + 2*a + b**2 < 0))

	pre_cond = And(StrictGreaterThan(Add(Symbol('b'), Integer(1)), Integer(0)), StrictLessThan(Add(Symbol('b'), Integer(-1)), Integer(0)), Or(And(GreaterThan(Symbol('a'), Integer(0)), StrictLessThan(Add(Symbol('a'), Integer(-1)), Integer(0))), And(StrictLessThan(Symbol('a'), Integer(0)), StrictGreaterThan(Add(Symbol('a'), Integer(1)), Integer(0))), StrictLessThan(Add(Pow(Symbol('a'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('a')), Pow(Symbol('b'), Integer(2))), Integer(0)), StrictLessThan(Add(Pow(Symbol('a'), Integer(2)), Mul(Integer(2), Symbol('a')), Pow(Symbol('b'), Integer(2))), Integer(0))))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1(a:sympy.Rational,b:sympy.Rational):
	#(8*a + 7 > 0) & (8*a - 9 < 0) & ((131072*a**6 - 98304*a**5 + 393216*a**4*b**2 - 362496*a**4 - 196608*a**3*b**2 + 191488*a**3 + 393216*a**2*b**4 - 749568*a**2*b**2 + 749952*a**2 - 98304*a*b**4 + 193536*a*b**2 - 193536*a + 131072*b**6 - 387072*b**4 + 249984*b**2 - 512001 < 0) | (4194304*a**8 - 4194304*a**7 + 16777216*a**6*b**2 - 14942208*a**6 - 12582912*a**5*b**2 + 12124160*a**5 + 25165824*a**4*b**4 - 46399488*a**4*b**2 + 12918784*a**4 - 12582912*a**3*b**4 + 24510464*a**3*b**2 - 7741440*a**3 + 16777216*a**2*b**6 - 47972352*a**2*b**4 + 95993856*a**2*b**2 + 1507968*a**2 - 4194304*a*b**6 + 12386304*a*b**4 - 24772608*a*b**2 - 127008*a + 4194304*b**8 - 16515072*b**6 + 15998976*b**4 - 65536128*b**2 + 3969 < 0))

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(8), Symbol('a')), Integer(7)), Integer(0)), StrictLessThan(Add(Mul(Integer(8), Symbol('a')), Integer(-9)), Integer(0)), Or(StrictLessThan(Add(Mul(Integer(131072), Pow(Symbol('a'), Integer(6))), Mul(Integer(-1), Integer(98304), Pow(Symbol('a'), Integer(5))), Mul(Integer(393216), Pow(Symbol('a'), Integer(4)), Pow(Symbol('b'), Integer(2))), Mul(Integer(-1), Integer(362496), Pow(Symbol('a'), Integer(4))), Mul(Integer(-1), Integer(196608), Pow(Symbol('a'), Integer(3)), Pow(Symbol('b'), Integer(2))), Mul(Integer(191488), Pow(Symbol('a'), Integer(3))), Mul(Integer(393216), Pow(Symbol('a'), Integer(2)), Pow(Symbol('b'), Integer(4))), Mul(Integer(-1), Integer(749568), Pow(Symbol('a'), Integer(2)), Pow(Symbol('b'), Integer(2))), Mul(Integer(749952), Pow(Symbol('a'), Integer(2))), Mul(Integer(-1), Integer(98304), Symbol('a'), Pow(Symbol('b'), Integer(4))), Mul(Integer(193536), Symbol('a'), Pow(Symbol('b'), Integer(2))), Mul(Integer(-1), Integer(193536), Symbol('a')), Mul(Integer(131072), Pow(Symbol('b'), Integer(6))), Mul(Integer(-1), Integer(387072), Pow(Symbol('b'), Integer(4))), Mul(Integer(249984), Pow(Symbol('b'), Integer(2))), Integer(-512001)), Integer(0)), StrictLessThan(Add(Mul(Integer(4194304), Pow(Symbol('a'), Integer(8))), Mul(Integer(-1), Integer(4194304), Pow(Symbol('a'), Integer(7))), Mul(Integer(16777216), Pow(Symbol('a'), Integer(6)), Pow(Symbol('b'), Integer(2))), Mul(Integer(-1), Integer(14942208), Pow(Symbol('a'), Integer(6))), Mul(Integer(-1), Integer(12582912), Pow(Symbol('a'), Integer(5)), Pow(Symbol('b'), Integer(2))), Mul(Integer(12124160), Pow(Symbol('a'), Integer(5))), Mul(Integer(25165824), Pow(Symbol('a'), Integer(4)), Pow(Symbol('b'), Integer(4))), Mul(Integer(-1), Integer(46399488), Pow(Symbol('a'), Integer(4)), Pow(Symbol('b'), Integer(2))), Mul(Integer(12918784), Pow(Symbol('a'), Integer(4))), Mul(Integer(-1), Integer(12582912), Pow(Symbol('a'), Integer(3)), Pow(Symbol('b'), Integer(4))), Mul(Integer(24510464), Pow(Symbol('a'), Integer(3)), Pow(Symbol('b'), Integer(2))), Mul(Integer(-1), Integer(7741440), Pow(Symbol('a'), Integer(3))), Mul(Integer(16777216), Pow(Symbol('a'), Integer(2)), Pow(Symbol('b'), Integer(6))), Mul(Integer(-1), Integer(47972352), Pow(Symbol('a'), Integer(2)), Pow(Symbol('b'), Integer(4))), Mul(Integer(95993856), Pow(Symbol('a'), Integer(2)), Pow(Symbol('b'), Integer(2))), Mul(Integer(1507968), Pow(Symbol('a'), Integer(2))), Mul(Integer(-1), Integer(4194304), Symbol('a'), Pow(Symbol('b'), Integer(6))), Mul(Integer(12386304), Symbol('a'), Pow(Symbol('b'), Integer(4))), Mul(Integer(-1), Integer(24772608), Symbol('a'), Pow(Symbol('b'), Integer(2))), Mul(Integer(-1), Integer(127008), Symbol('a')), Mul(Integer(4194304), Pow(Symbol('b'), Integer(8))), Mul(Integer(-1), Integer(16515072), Pow(Symbol('b'), Integer(6))), Mul(Integer(15998976), Pow(Symbol('b'), Integer(4))), Mul(Integer(-1), Integer(65536128), Pow(Symbol('b'), Integer(2))), Integer(3969)), Integer(0))))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_2(a:sympy.Rational,b:sympy.Rational):
	#(2*b + 3 > 0) & (2*b - 1 < 0) & ((16*a**4 - 15 < 0) | (64*a**8 + 256*a**6*b**2 + 256*a**6*b - 192*a**6 + 384*a**4*b**4 + 768*a**4*b**3 - 192*a**4*b**2 - 576*a**4*b + 96*a**4 + 256*a**2*b**6 + 768*a**2*b**5 + 192*a**2*b**4 - 896*a**2*b**3 + 576*a**2*b**2 + 1152*a**2*b - 648*a**2 + 64*b**8 + 256*b**7 + 192*b**6 - 320*b**5 - 416*b**4 + 168*b**2 + 72*b + 9 < 0))

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(2), Symbol('b')), Integer(3)), Integer(0)), StrictLessThan(Add(Mul(Integer(2), Symbol('b')), Integer(-1)), Integer(0)), Or(StrictLessThan(Add(Mul(Integer(16), Pow(Symbol('a'), Integer(4))), Integer(-15)), Integer(0)), StrictLessThan(Add(Mul(Integer(64), Pow(Symbol('a'), Integer(8))), Mul(Integer(256), Pow(Symbol('a'), Integer(6)), Pow(Symbol('b'), Integer(2))), Mul(Integer(256), Pow(Symbol('a'), Integer(6)), Symbol('b')), Mul(Integer(-1), Integer(192), Pow(Symbol('a'), Integer(6))), Mul(Integer(384), Pow(Symbol('a'), Integer(4)), Pow(Symbol('b'), Integer(4))), Mul(Integer(768), Pow(Symbol('a'), Integer(4)), Pow(Symbol('b'), Integer(3))), Mul(Integer(-1), Integer(192), Pow(Symbol('a'), Integer(4)), Pow(Symbol('b'), Integer(2))), Mul(Integer(-1), Integer(576), Pow(Symbol('a'), Integer(4)), Symbol('b')), Mul(Integer(96), Pow(Symbol('a'), Integer(4))), Mul(Integer(256), Pow(Symbol('a'), Integer(2)), Pow(Symbol('b'), Integer(6))), Mul(Integer(768), Pow(Symbol('a'), Integer(2)), Pow(Symbol('b'), Integer(5))), Mul(Integer(192), Pow(Symbol('a'), Integer(2)), Pow(Symbol('b'), Integer(4))), Mul(Integer(-1), Integer(896), Pow(Symbol('a'), Integer(2)), Pow(Symbol('b'), Integer(3))), Mul(Integer(576), Pow(Symbol('a'), Integer(2)), Pow(Symbol('b'), Integer(2))), Mul(Integer(1152), Pow(Symbol('a'), Integer(2)), Symbol('b')), Mul(Integer(-1), Integer(648), Pow(Symbol('a'), Integer(2))), Mul(Integer(64), Pow(Symbol('b'), Integer(8))), Mul(Integer(256), Pow(Symbol('b'), Integer(7))), Mul(Integer(192), Pow(Symbol('b'), Integer(6))), Mul(Integer(-1), Integer(320), Pow(Symbol('b'), Integer(5))), Mul(Integer(-1), Integer(416), Pow(Symbol('b'), Integer(4))), Mul(Integer(168), Pow(Symbol('b'), Integer(2))), Mul(Integer(72), Symbol('b')), Integer(9)), Integer(0))))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_3(a:sympy.Rational,b:sympy.Rational):
	#(4*a + 1 > 0) & (4*a - 7 < 0) & ((2048*a**6 - 9216*a**5 + 6144*a**4*b**2 + 11136*a**4 - 18432*a**3*b**2 + 1152*a**3 + 6144*a**2*b**4 + 8448*a**2*b**2 - 672*a**2 - 9216*a*b**4 + 8064*a*b**2 - 8064*a + 2048*b**6 - 2688*b**4 - 224*b**2 - 2009 < 0) | (16384*a**8 - 98304*a**7 + 65536*a**6*b**2 + 192512*a**6 - 294912*a**5*b**2 - 92160*a**5 + 98304*a**4*b**4 + 356352*a**4*b**2 - 114176*a**4 - 294912*a**3*b**4 + 36864*a**3*b**2 + 107520*a**3 + 65536*a**2*b**6 + 135168*a**2*b**4 - 21504*a**2*b**2 + 6048*a**2 - 98304*a*b**6 + 129024*a*b**4 - 258048*a*b**2 - 21168*a + 16384*b**8 - 28672*b**6 - 3584*b**4 - 64288*b**2 + 3969 < 0))

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(4), Symbol('a')), Integer(1)), Integer(0)), StrictLessThan(Add(Mul(Integer(4), Symbol('a')), Integer(-7)), Integer(0)), Or(StrictLessThan(Add(Mul(Integer(2048), Pow(Symbol('a'), Integer(6))), Mul(Integer(-1), Integer(9216), Pow(Symbol('a'), Integer(5))), Mul(Integer(6144), Pow(Symbol('a'), Integer(4)), Pow(Symbol('b'), Integer(2))), Mul(Integer(11136), Pow(Symbol('a'), Integer(4))), Mul(Integer(-1), Integer(18432), Pow(Symbol('a'), Integer(3)), Pow(Symbol('b'), Integer(2))), Mul(Integer(1152), Pow(Symbol('a'), Integer(3))), Mul(Integer(6144), Pow(Symbol('a'), Integer(2)), Pow(Symbol('b'), Integer(4))), Mul(Integer(8448), Pow(Symbol('a'), Integer(2)), Pow(Symbol('b'), Integer(2))), Mul(Integer(-1), Integer(672), Pow(Symbol('a'), Integer(2))), Mul(Integer(-1), Integer(9216), Symbol('a'), Pow(Symbol('b'), Integer(4))), Mul(Integer(8064), Symbol('a'), Pow(Symbol('b'), Integer(2))), Mul(Integer(-1), Integer(8064), Symbol('a')), Mul(Integer(2048), Pow(Symbol('b'), Integer(6))), Mul(Integer(-1), Integer(2688), Pow(Symbol('b'), Integer(4))), Mul(Integer(-1), Integer(224), Pow(Symbol('b'), Integer(2))), Integer(-2009)), Integer(0)), StrictLessThan(Add(Mul(Integer(16384), Pow(Symbol('a'), Integer(8))), Mul(Integer(-1), Integer(98304), Pow(Symbol('a'), Integer(7))), Mul(Integer(65536), Pow(Symbol('a'), Integer(6)), Pow(Symbol('b'), Integer(2))), Mul(Integer(192512), Pow(Symbol('a'), Integer(6))), Mul(Integer(-1), Integer(294912), Pow(Symbol('a'), Integer(5)), Pow(Symbol('b'), Integer(2))), Mul(Integer(-1), Integer(92160), Pow(Symbol('a'), Integer(5))), Mul(Integer(98304), Pow(Symbol('a'), Integer(4)), Pow(Symbol('b'), Integer(4))), Mul(Integer(356352), Pow(Symbol('a'), Integer(4)), Pow(Symbol('b'), Integer(2))), Mul(Integer(-1), Integer(114176), Pow(Symbol('a'), Integer(4))), Mul(Integer(-1), Integer(294912), Pow(Symbol('a'), Integer(3)), Pow(Symbol('b'), Integer(4))), Mul(Integer(36864), Pow(Symbol('a'), Integer(3)), Pow(Symbol('b'), Integer(2))), Mul(Integer(107520), Pow(Symbol('a'), Integer(3))), Mul(Integer(65536), Pow(Symbol('a'), Integer(2)), Pow(Symbol('b'), Integer(6))), Mul(Integer(135168), Pow(Symbol('a'), Integer(2)), Pow(Symbol('b'), Integer(4))), Mul(Integer(-1), Integer(21504), Pow(Symbol('a'), Integer(2)), Pow(Symbol('b'), Integer(2))), Mul(Integer(6048), Pow(Symbol('a'), Integer(2))), Mul(Integer(-1), Integer(98304), Symbol('a'), Pow(Symbol('b'), Integer(6))), Mul(Integer(129024), Symbol('a'), Pow(Symbol('b'), Integer(4))), Mul(Integer(-1), Integer(258048), Symbol('a'), Pow(Symbol('b'), Integer(2))), Mul(Integer(-1), Integer(21168), Symbol('a')), Mul(Integer(16384), Pow(Symbol('b'), Integer(8))), Mul(Integer(-1), Integer(28672), Pow(Symbol('b'), Integer(6))), Mul(Integer(-1), Integer(3584), Pow(Symbol('b'), Integer(4))), Mul(Integer(-1), Integer(64288), Pow(Symbol('b'), Integer(2))), Integer(3969)), Integer(0))))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def post_condition(a:sympy.Rational, b:sympy.Rational, x:sympy.Rational, y:sympy.Rational):
	# (0 > x**4 + y**4 - 1) & (0 > a**2 - 2*a*x + b**2 - 2*b*y + x**2 + y**2 - 1)

	post_cond =  And(StrictGreaterThan(Integer(0), Add(Pow(Symbol('x'), Integer(4)), Pow(Symbol('y'), Integer(4)), Integer(-1))), StrictGreaterThan(Integer(0), Add(Pow(Symbol('a'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('a'), Symbol('x')), Pow(Symbol('b'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('b'), Symbol('y')), Pow(Symbol('x'), Integer(2)), Pow(Symbol('y'), Integer(2)), Integer(-1))))

	eval = post_cond.subs( { 'a':a, 'b':b, 'x':x, 'y':y })

	return eval == sympy.logic.boolalg.BooleanTrue



#return post-condition single variable
def return_post_condition_single_var(post_condition, a:sympy.Rational=None, b:sympy.Rational=None, x:sympy.Rational=None, y:sympy.Rational=None):
	assert a!=None
	assert b!=None


	if x==None:
		assert y!=None
		return lambda x: post_condition(a=a, b=b, x=x, y=y)

	if y==None:
		assert x!=None
		return lambda y: post_condition(a=a, b=b, x=x, y=y)


	return post_condition(a=a, b=b, x=x, y=y)


def get_univariate_poly( a:sympy.Rational, b:sympy.Rational, x:sympy.Rational, y:sympy.Rational ):


	post_cond =  And(StrictGreaterThan(Integer(0), Add(Pow(Symbol('x'), Integer(4)), Pow(Symbol('y'), Integer(4)), Integer(-1))), StrictGreaterThan(Integer(0), Add(Pow(Symbol('a'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('a'), Symbol('x')), Pow(Symbol('b'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('b'), Symbol('y')), Pow(Symbol('x'), Integer(2)), Pow(Symbol('y'), Integer(2)), Integer(-1))))

	eval = post_cond.subs( { 'a':a, 'b':b, 'x':x, 'y':y })
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
	
	
	lambda_var_0 = sympy.symbols('lambda_var_0')
	
	
	if pre_condition_0(a=a,b=b)==True:
		all_vals = dict()
		all_vals['a'] = a
		all_vals['b'] = b
		all_vals['x'] = Add(Symbol('lambda_var_0'), Rational(1, 8))
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
	
	
	if pre_condition_1(a=a,b=b)==True:
		all_vals = dict()
		all_vals['a'] = a
		all_vals['b'] = b
		all_vals['x'] = Rational(1, 8)
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
	
	
	if pre_condition_2(a=a,b=b)==True:
		all_vals = dict()
		all_vals['a'] = a
		all_vals['b'] = b
		all_vals['x'] = Add(Symbol('lambda_var_0'), Rational(3, 4))
		all_vals['y'] = Rational(-1, 2)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_2 SAT")

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_3(a=a,b=b)==True:
		all_vals = dict()
		all_vals['a'] = a
		all_vals['b'] = b
		all_vals['x'] = Rational(3, 4)
		all_vals['y'] = Add(Symbol('lambda_var_0'), Rational(-1, 2))
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
