import sympy
from sympy import *
from NQS.helper_program_cav import get_lambda_val

def pre_condition_0(r2:sympy.Rational):
	#r2 - 1 > 0

	pre_cond = StrictGreaterThan(Add(Symbol('r2'), Integer(-1)), Integer(0))

	eval = pre_cond.subs( { 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1(r2:sympy.Rational):
	#268435456*r2**3 + 524288000*r2**2 + 251854848*r2 - 77629185 > 0

	pre_cond = StrictGreaterThan(Add(Mul(Integer(268435456), Pow(Symbol('r2'), Integer(3))), Mul(Integer(524288000), Pow(Symbol('r2'), Integer(2))), Mul(Integer(251854848), Symbol('r2')), Integer(-77629185)), Integer(0))

	eval = pre_cond.subs( { 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_2(r2:sympy.Rational):
	#262144*r2 - 47961 > 0

	pre_cond = StrictGreaterThan(Add(Mul(Integer(262144), Symbol('r2')), Integer(-47961)), Integer(0))

	eval = pre_cond.subs( { 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_3(r2:sympy.Rational):
	#68719476736*r2**3 + 136633647104*r2**2 + 67648880640*r2 - 17851489281 > 0

	pre_cond = StrictGreaterThan(Add(Mul(Integer(68719476736), Pow(Symbol('r2'), Integer(3))), Mul(Integer(136633647104), Pow(Symbol('r2'), Integer(2))), Mul(Integer(67648880640), Symbol('r2')), Integer(-17851489281)), Integer(0))

	eval = pre_cond.subs( { 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_4(r2:sympy.Rational):
	#67108864*r2 - 12117361 > 0

	pre_cond = StrictGreaterThan(Add(Mul(Integer(67108864), Symbol('r2')), Integer(-12117361)), Integer(0))

	eval = pre_cond.subs( { 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_5(r2:sympy.Rational):
	#17592186044416*r2**3 + 35132832481280*r2**2 + 17523516899328*r2 - 4441004601345 > 0

	pre_cond = StrictGreaterThan(Add(Mul(Integer(17592186044416), Pow(Symbol('r2'), Integer(3))), Mul(Integer(35132832481280), Pow(Symbol('r2'), Integer(2))), Mul(Integer(17523516899328), Symbol('r2')), Integer(-4441004601345)), Integer(0))

	eval = pre_cond.subs( { 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_6(r2:sympy.Rational):
	#268435456*r2 - 48288601 > 0

	pre_cond = StrictGreaterThan(Add(Mul(Integer(268435456), Symbol('r2')), Integer(-48288601)), Integer(0))

	eval = pre_cond.subs( { 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_7(r2:sympy.Rational):
	#4503599627370496*r2**3 + 9003900719857664*r2**2 + 4499202386165760*r2 - 1128648820244481 > 0

	pre_cond = StrictGreaterThan(Add(Mul(Integer(4503599627370496), Pow(Symbol('r2'), Integer(3))), Mul(Integer(9003900719857664), Pow(Symbol('r2'), Integer(2))), Mul(Integer(4499202386165760), Symbol('r2')), Integer(-1128648820244481)), Integer(0))

	eval = pre_cond.subs( { 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_8(r2:sympy.Rational):
	#67108864*r2 - 12061729 > 0

	pre_cond = StrictGreaterThan(Add(Mul(Integer(67108864), Symbol('r2')), Integer(-12061729)), Integer(0))

	eval = pre_cond.subs( { 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_9(r2:sympy.Rational):
	#1152921504606846976*r2**3 + 2305631902981160960*r2**2 + 1152640042515038208*r2 - 288406300160098305 > 0

	pre_cond = StrictGreaterThan(Add(Mul(Integer(1152921504606846976), Pow(Symbol('r2'), Integer(3))), Mul(Integer(2305631902981160960), Pow(Symbol('r2'), Integer(2))), Mul(Integer(1152640042515038208), Symbol('r2')), Integer(-288406300160098305)), Integer(0))

	eval = pre_cond.subs( { 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_10(r2:sympy.Rational):
	#4294967296*r2 - 771672841 > 0

	pre_cond = StrictGreaterThan(Add(Mul(Integer(4294967296), Symbol('r2')), Integer(-771672841)), Integer(0))

	eval = pre_cond.subs( { 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_11(r2:sympy.Rational):
	#295147905179352825856*r2**3 + 590282299559823540224*r2**2 + 295129890987001774080*r2 - 73798235328268206081 > 0

	pre_cond = StrictGreaterThan(Add(Mul(Integer(295147905179352825856), Pow(Symbol('r2'), Integer(3))), Mul(Integer(590282299559823540224), Pow(Symbol('r2'), Integer(2))), Mul(Integer(295129890987001774080), Symbol('r2')), Integer(-73798235328268206081)), Integer(0))

	eval = pre_cond.subs( { 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_12(r2:sympy.Rational):
	#1073741824*r2 - 192904321 > 0

	pre_cond = StrictGreaterThan(Add(Mul(Integer(1073741824), Symbol('r2')), Integer(-192904321)), Integer(0))

	eval = pre_cond.subs( { 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_13(r2:sympy.Rational):
	#75557863725914323419136*r2**3 + 151114862760700191703040*r2**2 + 75556710807708251455488*r2 - 18890186507968723288065 > 0

	pre_cond = StrictGreaterThan(Add(Mul(Integer(75557863725914323419136), Pow(Symbol('r2'), Integer(3))), Mul(Integer(151114862760700191703040), Pow(Symbol('r2'), Integer(2))), Mul(Integer(75556710807708251455488), Symbol('r2')), Integer(-18890186507968723288065)), Integer(0))

	eval = pre_cond.subs( { 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_14(r2:sympy.Rational):
	#68719476736*r2 - 12345654321 > 0

	pre_cond = StrictGreaterThan(Add(Mul(Integer(68719476736), Symbol('r2')), Integer(-12345654321)), Integer(0))

	eval = pre_cond.subs( { 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_15(r2:sympy.Rational):
	#19342813113834066795298816*r2**3 + 38685570887435912461942784*r2**2 + 19342739326910548515225600*r2 - 4835749395327497095086081 > 0

	pre_cond = StrictGreaterThan(Add(Mul(Integer(19342813113834066795298816), Pow(Symbol('r2'), Integer(3))), Mul(Integer(38685570887435912461942784), Pow(Symbol('r2'), Integer(2))), Mul(Integer(19342739326910548515225600), Symbol('r2')), Integer(-4835749395327497095086081)), Integer(0))

	eval = pre_cond.subs( { 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_16(r2:sympy.Rational):
	#17592186044416*r2 - 3160476839529 > 0

	pre_cond = StrictGreaterThan(Add(Mul(Integer(17592186044416), Symbol('r2')), Integer(-3160476839529)), Integer(0))

	eval = pre_cond.subs( { 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_17(r2:sympy.Rational):
	#4951760157141521099596496896*r2**3 + 9903516772508180046959083520*r2**2 + 4951755434775882654881415168*r2 - 1237942990764572806033178625 > 0

	pre_cond = StrictGreaterThan(Add(Mul(Integer(4951760157141521099596496896), Pow(Symbol('r2'), Integer(3))), Mul(Integer(9903516772508180046959083520), Pow(Symbol('r2'), Integer(2))), Mul(Integer(4951755434775882654881415168), Symbol('r2')), Integer(-1237942990764572806033178625)), Integer(0))

	eval = pre_cond.subs( { 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_18(r2:sympy.Rational):
	#1099511627776*r2 - 197529580249 > 0

	pre_cond = StrictGreaterThan(Add(Mul(Integer(1099511627776), Symbol('r2')), Integer(-197529580249)), Integer(0))

	eval = pre_cond.subs( { 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_19(r2:sympy.Rational):
	#1267650600228229401496703205376*r2**3 + 2535300973782867625250436153344*r2**2 + 1267650297996788008638291640320*r2 - 316912838951718916960267796481 > 0

	pre_cond = StrictGreaterThan(Add(Mul(Integer(1267650600228229401496703205376), Pow(Symbol('r2'), Integer(3))), Mul(Integer(2535300973782867625250436153344), Pow(Symbol('r2'), Integer(2))), Mul(Integer(1267650297996788008638291640320), Symbol('r2')), Integer(-316912838951718916960267796481)), Integer(0))

	eval = pre_cond.subs( { 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_20(r2:sympy.Rational):
	#281474976710656*r2 - 50567558321569 > 0

	pre_cond = StrictGreaterThan(Add(Mul(Integer(281474976710656), Symbol('r2')), Integer(-50567558321569)), Integer(0))

	eval = pre_cond.subs( { 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_21(r2:sympy.Rational):
	#324518553658426726783156020576256*r2**3 + 649037092809743618190761944678400*r2**2 + 324518534315613829121871339061248*r2 - 81129650503864913870879650217985 > 0

	pre_cond = StrictGreaterThan(Add(Mul(Integer(324518553658426726783156020576256), Pow(Symbol('r2'), Integer(3))), Mul(Integer(649037092809743618190761944678400), Pow(Symbol('r2'), Integer(2))), Mul(Integer(324518534315613829121871339061248), Symbol('r2')), Integer(-81129650503864913870879650217985)), Integer(0))

	eval = pre_cond.subs( { 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_22(r2:sympy.Rational):
	#4611686018427387904*r2 - 828498830029630321 > 0

	pre_cond = StrictGreaterThan(Add(Mul(Integer(4611686018427387904), Symbol('r2')), Integer(-828498830029630321)), Integer(0))

	eval = pre_cond.subs( { 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_23(r2:sympy.Rational):
	#83076749736557242056487941267521536*r2**3 + 166153498544659454648940676360699904*r2**2 + 83076748498617206229872180188938240*r2 - 20769188207851835643945416948449281 > 0

	pre_cond = StrictGreaterThan(Add(Mul(Integer(83076749736557242056487941267521536), Pow(Symbol('r2'), Integer(3))), Mul(Integer(166153498544659454648940676360699904), Pow(Symbol('r2'), Integer(2))), Mul(Integer(83076748498617206229872180188938240), Symbol('r2')), Integer(-20769188207851835643945416948449281)), Integer(0))

	eval = pre_cond.subs( { 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def post_condition(r2:sympy.Rational, x:sympy.Rational, y:sympy.Rational):
	# (0 > -r2 + x**2 + y**2) & (0 > x**4 + 6*x**2 - 4*y**3 - 4*y + 2)

	post_cond =  And(StrictGreaterThan(Integer(0), Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('x'), Integer(2)), Pow(Symbol('y'), Integer(2)))), StrictGreaterThan(Integer(0), Add(Pow(Symbol('x'), Integer(4)), Mul(Integer(6), Pow(Symbol('x'), Integer(2))), Mul(Integer(-1), Integer(4), Pow(Symbol('y'), Integer(3))), Mul(Integer(-1), Integer(4), Symbol('y')), Integer(2))))

	eval = post_cond.subs( { 'r2':r2, 'x':x, 'y':y })

	return eval == sympy.logic.boolalg.BooleanTrue



#return post-condition single variable
def return_post_condition_single_var(post_condition, r2:sympy.Rational=None, x:sympy.Rational=None, y:sympy.Rational=None):
	assert r2!=None


	if x==None:
		assert y!=None
		return lambda x: post_condition(r2=r2, x=x, y=y)

	if y==None:
		assert x!=None
		return lambda y: post_condition(r2=r2, x=x, y=y)


	return post_condition(r2=r2, x=x, y=y)


def get_univariate_poly( r2:sympy.Rational, x:sympy.Rational, y:sympy.Rational ):


	post_cond =  And(StrictGreaterThan(Integer(0), Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('x'), Integer(2)), Pow(Symbol('y'), Integer(2)))), StrictGreaterThan(Integer(0), Add(Pow(Symbol('x'), Integer(4)), Mul(Integer(6), Pow(Symbol('x'), Integer(2))), Mul(Integer(-1), Integer(4), Pow(Symbol('y'), Integer(3))), Mul(Integer(-1), Integer(4), Symbol('y')), Integer(2))))

	eval = post_cond.subs( { 'r2':r2, 'x':x, 'y':y })
	return eval



if __name__=="__main__":
	
	ip_0=int(input("enter numerator of r2:\n"))
	ip_1=int(input("enter denominator of r2:\n"))
	assert(ip_1!=0), ("Error denominator entered is 0")
	r2=sympy.Rational(ip_0,ip_1)
	
	
	lambda_var_0 = sympy.symbols('lambda_var_0')
	
	
	if pre_condition_0(r2=r2)==True:
		all_vals = dict()
		all_vals['r2'] = r2
		all_vals['x'] = Add(Symbol('lambda_var_0'), Rational(1, 8))
		all_vals['y'] = Integer(1)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_0 SAT")

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_1(r2=r2)==True:
		all_vals = dict()
		all_vals['r2'] = r2
		all_vals['x'] = Rational(1, 8)
		all_vals['y'] = Add(Symbol('lambda_var_0'), Integer(1))
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_1 SAT")

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_2(r2=r2)==True:
		all_vals = dict()
		all_vals['r2'] = r2
		all_vals['x'] = Add(Symbol('lambda_var_0'), Rational(-1, 16))
		all_vals['y'] = Rational(219, 512)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_2 SAT")

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_3(r2=r2)==True:
		all_vals = dict()
		all_vals['r2'] = r2
		all_vals['x'] = Rational(-1, 16)
		all_vals['y'] = Add(Symbol('lambda_var_0'), Rational(219, 512))
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_3 SAT")

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_4(r2=r2)==True:
		all_vals = dict()
		all_vals['r2'] = r2
		all_vals['x'] = Add(Symbol('lambda_var_0'), Rational(-1, 32))
		all_vals['y'] = Rational(3481, 8192)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_4 SAT")

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_5(r2=r2)==True:
		all_vals = dict()
		all_vals['r2'] = r2
		all_vals['x'] = Rational(-1, 32)
		all_vals['y'] = Add(Symbol('lambda_var_0'), Rational(3481, 8192))
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_5 SAT")

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_6(r2=r2)==True:
		all_vals = dict()
		all_vals['r2'] = r2
		all_vals['x'] = Add(Symbol('lambda_var_0'), Rational(-1, 64))
		all_vals['y'] = Rational(6949, 16384)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_6 SAT")

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_7(r2=r2)==True:
		all_vals = dict()
		all_vals['r2'] = r2
		all_vals['x'] = Rational(-1, 64)
		all_vals['y'] = Add(Symbol('lambda_var_0'), Rational(6949, 16384))
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_7 SAT")

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_8(r2=r2)==True:
		all_vals = dict()
		all_vals['r2'] = r2
		all_vals['x'] = Add(Symbol('lambda_var_0'), Rational(-1, 128))
		all_vals['y'] = Rational(3473, 8192)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_8 SAT")

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_9(r2=r2)==True:
		all_vals = dict()
		all_vals['r2'] = r2
		all_vals['x'] = Rational(-1, 128)
		all_vals['y'] = Add(Symbol('lambda_var_0'), Rational(3473, 8192))
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_9 SAT")

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_10(r2=r2)==True:
		all_vals = dict()
		all_vals['r2'] = r2
		all_vals['x'] = Add(Symbol('lambda_var_0'), Rational(-1, 256))
		all_vals['y'] = Rational(27779, 65536)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_10 SAT")

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_11(r2=r2)==True:
		all_vals = dict()
		all_vals['r2'] = r2
		all_vals['x'] = Rational(-1, 256)
		all_vals['y'] = Add(Symbol('lambda_var_0'), Rational(27779, 65536))
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_11 SAT")

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_12(r2=r2)==True:
		all_vals = dict()
		all_vals['r2'] = r2
		all_vals['x'] = Add(Symbol('lambda_var_0'), Rational(-1, 512))
		all_vals['y'] = Rational(13889, 32768)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_12 SAT")

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_13(r2=r2)==True:
		all_vals = dict()
		all_vals['r2'] = r2
		all_vals['x'] = Rational(-1, 512)
		all_vals['y'] = Add(Symbol('lambda_var_0'), Rational(13889, 32768))
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_13 SAT")

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_14(r2=r2)==True:
		all_vals = dict()
		all_vals['r2'] = r2
		all_vals['x'] = Add(Symbol('lambda_var_0'), Rational(-1, 1024))
		all_vals['y'] = Rational(111111, 262144)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_14 SAT")

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_15(r2=r2)==True:
		all_vals = dict()
		all_vals['r2'] = r2
		all_vals['x'] = Rational(-1, 1024)
		all_vals['y'] = Add(Symbol('lambda_var_0'), Rational(111111, 262144))
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_15 SAT")

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_16(r2=r2)==True:
		all_vals = dict()
		all_vals['r2'] = r2
		all_vals['x'] = Add(Symbol('lambda_var_0'), Rational(-1, 2048))
		all_vals['y'] = Rational(1777773, 4194304)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_16 SAT")

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_17(r2=r2)==True:
		all_vals = dict()
		all_vals['r2'] = r2
		all_vals['x'] = Rational(-1, 2048)
		all_vals['y'] = Add(Symbol('lambda_var_0'), Rational(1777773, 4194304))
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_17 SAT")

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_18(r2=r2)==True:
		all_vals = dict()
		all_vals['r2'] = r2
		all_vals['x'] = Add(Symbol('lambda_var_0'), Rational(-1, 4096))
		all_vals['y'] = Rational(444443, 1048576)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_18 SAT")

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_19(r2=r2)==True:
		all_vals = dict()
		all_vals['r2'] = r2
		all_vals['x'] = Rational(-1, 4096)
		all_vals['y'] = Add(Symbol('lambda_var_0'), Rational(444443, 1048576))
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_19 SAT")

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_20(r2=r2)==True:
		all_vals = dict()
		all_vals['r2'] = r2
		all_vals['x'] = Add(Symbol('lambda_var_0'), Rational(-1, 8192))
		all_vals['y'] = Rational(7111087, 16777216)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_20 SAT")

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_21(r2=r2)==True:
		all_vals = dict()
		all_vals['r2'] = r2
		all_vals['x'] = Rational(-1, 8192)
		all_vals['y'] = Add(Symbol('lambda_var_0'), Rational(7111087, 16777216))
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_21 SAT")

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_22(r2=r2)==True:
		all_vals = dict()
		all_vals['r2'] = r2
		all_vals['x'] = Add(Symbol('lambda_var_0'), Rational(-1, 16384))
		all_vals['y'] = Rational(910219111, 2147483648)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_22 SAT")

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_23(r2=r2)==True:
		all_vals = dict()
		all_vals['r2'] = r2
		all_vals['x'] = Rational(-1, 16384)
		all_vals['y'] = Add(Symbol('lambda_var_0'), Rational(910219111, 2147483648))
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_23 SAT")

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass


	print("UNKNOWN")
