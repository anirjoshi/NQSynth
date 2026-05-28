import sympy
from sympy import *
from NQS.helper_program_cav import get_lambda_val

def pre_condition_0(a:sympy.Rational,r:sympy.Rational):
	#36*r - 1 > 0

	pre_cond = StrictGreaterThan(Add(Mul(Integer(36), Symbol('r')), Integer(-1)), Integer(0))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1(a:sympy.Rational,r:sympy.Rational):
	#9*r - 1 > 0

	pre_cond = StrictGreaterThan(Add(Mul(Integer(9), Symbol('r')), Integer(-1)), Integer(0))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_2(a:sympy.Rational,r:sympy.Rational):
	#(64*r - 1 > 0) & ((a + 512 < 0) | (-a**2 - 1024*a + 9437184*r - 409600 > 0))

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(64), Symbol('r')), Integer(-1)), Integer(0)), Or(StrictLessThan(Add(Symbol('a'), Integer(512)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('a'), Integer(2))), Mul(Integer(-1), Integer(1024), Symbol('a')), Mul(Integer(9437184), Symbol('r')), Integer(-409600)), Integer(0))))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_3(a:sympy.Rational,r:sympy.Rational):
	#16777216*a**2*r**3 - 196608*a**2*r**2 + 768*a**2*r - a**2 - 6553600 > 0

	pre_cond = StrictGreaterThan(Add(Mul(Integer(16777216), Pow(Symbol('a'), Integer(2)), Pow(Symbol('r'), Integer(3))), Mul(Integer(-1), Integer(196608), Pow(Symbol('a'), Integer(2)), Pow(Symbol('r'), Integer(2))), Mul(Integer(768), Pow(Symbol('a'), Integer(2)), Symbol('r')), Mul(Integer(-1), Pow(Symbol('a'), Integer(2))), Integer(-6553600)), Integer(0))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_4(a:sympy.Rational,r:sympy.Rational):
	#(4096*r - 49 > 0) & ((343*a - 262144 > 0) | (-117649*a**2 + 179830784*a + 2473901162496*r - 98314485760 > 0))

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(4096), Symbol('r')), Integer(-49)), Integer(0)), Or(StrictGreaterThan(Add(Mul(Integer(343), Symbol('a')), Integer(-262144)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Integer(117649), Pow(Symbol('a'), Integer(2))), Mul(Integer(179830784), Symbol('a')), Mul(Integer(2473901162496), Symbol('r')), Integer(-98314485760)), Integer(0))))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_5(a:sympy.Rational,r:sympy.Rational):
	#19342813113834066795298816*a**2*r**3 - 212299182031086915944448*a**2*r**2 + 776704374657093992448*a**2*r - 947200518061237441*a**2 - 7850807744635654566313984 > 0

	pre_cond = StrictGreaterThan(Add(Mul(Integer(19342813113834066795298816), Pow(Symbol('a'), Integer(2)), Pow(Symbol('r'), Integer(3))), Mul(Integer(-1), Integer(212299182031086915944448), Pow(Symbol('a'), Integer(2)), Pow(Symbol('r'), Integer(2))), Mul(Integer(776704374657093992448), Pow(Symbol('a'), Integer(2)), Symbol('r')), Mul(Integer(-1), Integer(947200518061237441), Pow(Symbol('a'), Integer(2))), Integer(-7850807744635654566313984)), Integer(0))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_6(a:sympy.Rational,r:sympy.Rational):
	#(16384*r - 225 > 0) & ((3375*a + 2097152 < 0) | (-11390625*a**2 - 14155776000*a + 158329674399744*r - 6572373704704 > 0))

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(16384), Symbol('r')), Integer(-225)), Integer(0)), Or(StrictLessThan(Add(Mul(Integer(3375), Symbol('a')), Integer(2097152)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Integer(11390625), Pow(Symbol('a'), Integer(2))), Mul(Integer(-1), Integer(14155776000), Symbol('a')), Mul(Integer(158329674399744), Symbol('r')), Integer(-6572373704704)), Integer(0))))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_7(a:sympy.Rational,r:sympy.Rational):
	#4398046511104*a**2*r**3 - 20132659200*a**2*r**2 + 30720000*a**2*r - 15625*a**2 - 2578054119424 > 0

	pre_cond = StrictGreaterThan(Add(Mul(Integer(4398046511104), Pow(Symbol('a'), Integer(2)), Pow(Symbol('r'), Integer(3))), Mul(Integer(-1), Integer(20132659200), Pow(Symbol('a'), Integer(2)), Pow(Symbol('r'), Integer(2))), Mul(Integer(30720000), Pow(Symbol('a'), Integer(2)), Symbol('r')), Mul(Integer(-1), Integer(15625), Pow(Symbol('a'), Integer(2))), Integer(-2578054119424)), Integer(0))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_8(a:sympy.Rational,r:sympy.Rational):
	#(16384*r - 1 > 0) & ((a + 2097152 < 0) | (-a**2 - 4194304*a + 158329674399744*r - 4407710187520 > 0))

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(16384), Symbol('r')), Integer(-1)), Integer(0)), Or(StrictLessThan(Add(Symbol('a'), Integer(2097152)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('a'), Integer(2))), Mul(Integer(-1), Integer(4194304), Symbol('a')), Mul(Integer(158329674399744), Symbol('r')), Integer(-4407710187520)), Integer(0))))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_9(a:sympy.Rational,r:sympy.Rational):
	#68719476736*a**2*r**3 - 50331648*a**2*r**2 + 12288*a**2*r - a**2 - 56438554624 > 0

	pre_cond = StrictGreaterThan(Add(Mul(Integer(68719476736), Pow(Symbol('a'), Integer(2)), Pow(Symbol('r'), Integer(3))), Mul(Integer(-1), Integer(50331648), Pow(Symbol('a'), Integer(2)), Pow(Symbol('r'), Integer(2))), Mul(Integer(12288), Pow(Symbol('a'), Integer(2)), Symbol('r')), Mul(Integer(-1), Pow(Symbol('a'), Integer(2))), Integer(-56438554624)), Integer(0))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_10(a:sympy.Rational,r:sympy.Rational):
	#(1048576*r - 7921 > 0) & ((704969*a + 1073741824 < 0) | (-496981290961*a**2 - 1513909399846912*a + 41505174165846491136*r - 1466453842336940032 > 0))

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(1048576), Symbol('r')), Integer(-7921)), Integer(0)), Or(StrictLessThan(Add(Mul(Integer(704969), Symbol('a')), Integer(1073741824)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Integer(496981290961), Pow(Symbol('a'), Integer(2))), Mul(Integer(-1), Integer(1513909399846912), Symbol('a')), Mul(Integer(41505174165846491136), Symbol('r')), Integer(-1466453842336940032)), Integer(0))))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_11(a:sympy.Rational,r:sympy.Rational):
	#5070602400912917605986812821504*a**2*r**3 - 3930882217501718170180780032*a**2*r**2 + 1015779045969584562634752*a**2*r - 87495801462998035849*a**2 - 4139645613982577134324311654400 > 0

	pre_cond = StrictGreaterThan(Add(Mul(Integer(5070602400912917605986812821504), Pow(Symbol('a'), Integer(2)), Pow(Symbol('r'), Integer(3))), Mul(Integer(-1), Integer(3930882217501718170180780032), Pow(Symbol('a'), Integer(2)), Pow(Symbol('r'), Integer(2))), Mul(Integer(1015779045969584562634752), Pow(Symbol('a'), Integer(2)), Symbol('r')), Mul(Integer(-1), Integer(87495801462998035849), Pow(Symbol('a'), Integer(2))), Integer(-4139645613982577134324311654400)), Integer(0))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_12(a:sympy.Rational,r:sympy.Rational):
	#(262144*r - 961 > 0) & ((29791*a + 134217728 < 0) | (-887503681*a**2 - 7996960669696*a + 648518346341351424*r - 20391817526640640 > 0))

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(262144), Symbol('r')), Integer(-961)), Integer(0)), Or(StrictLessThan(Add(Mul(Integer(29791), Symbol('a')), Integer(134217728)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Integer(887503681), Pow(Symbol('a'), Integer(2))), Mul(Integer(-1), Integer(7996960669696), Symbol('a')), Mul(Integer(648518346341351424), Symbol('r')), Integer(-20391817526640640)), Integer(0))))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_13(a:sympy.Rational,r:sympy.Rational):
	#19342813113834066795298816*a**2*r**3 - 13837003610321187766272*a**2*r**2 + 3299462661493751808*a**2*r - 262254607552729*a**2 - 15924580996659860331298816 > 0

	pre_cond = StrictGreaterThan(Add(Mul(Integer(19342813113834066795298816), Pow(Symbol('a'), Integer(2)), Pow(Symbol('r'), Integer(3))), Mul(Integer(-1), Integer(13837003610321187766272), Pow(Symbol('a'), Integer(2)), Pow(Symbol('r'), Integer(2))), Mul(Integer(3299462661493751808), Pow(Symbol('a'), Integer(2)), Symbol('r')), Mul(Integer(-1), Integer(262254607552729), Pow(Symbol('a'), Integer(2))), Integer(-15924580996659860331298816)), Integer(0))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_14(a:sympy.Rational,r:sympy.Rational):
	#(65536*r - 121 > 0) & ((1331*a + 16777216 < 0) | (-1771561*a**2 - 44660948992*a + 10133099161583616*r - 300183854252032 > 0))

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(65536), Symbol('r')), Integer(-121)), Integer(0)), Or(StrictLessThan(Add(Mul(Integer(1331), Symbol('a')), Integer(16777216)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Integer(1771561), Pow(Symbol('a'), Integer(2))), Mul(Integer(-1), Integer(44660948992), Symbol('a')), Mul(Integer(10133099161583616), Symbol('r')), Integer(-300183854252032)), Integer(0))))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_15(a:sympy.Rational,r:sympy.Rational):
	#4398046511104*a**2*r**3 - 805306368*a**2*r**2 + 49152*a**2*r - a**2 - 3995393327104 > 0

	pre_cond = StrictGreaterThan(Add(Mul(Integer(4398046511104), Pow(Symbol('a'), Integer(2)), Pow(Symbol('r'), Integer(3))), Mul(Integer(-1), Integer(805306368), Pow(Symbol('a'), Integer(2)), Pow(Symbol('r'), Integer(2))), Mul(Integer(49152), Pow(Symbol('a'), Integer(2)), Symbol('r')), Mul(Integer(-1), Pow(Symbol('a'), Integer(2))), Integer(-3995393327104)), Integer(0))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_16(a:sympy.Rational,r:sympy.Rational):
	#(4194304*r - 3969 > 0) & ((250047*a + 8589934592 < 0) | (-62523502209*a**2 - 4295774749851648*a + 2656331146614175432704*r - 76300618205608542208 > 0))

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(4194304), Symbol('r')), Integer(-3969)), Integer(0)), Or(StrictLessThan(Add(Mul(Integer(250047), Symbol('a')), Integer(8589934592)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Integer(62523502209), Pow(Symbol('a'), Integer(2))), Mul(Integer(-1), Integer(4295774749851648), Symbol('a')), Mul(Integer(2656331146614175432704), Symbol('r')), Integer(-76300618205608542208)), Integer(0))))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_17(a:sympy.Rational,r:sympy.Rational):
	#281474976710656*a**2*r**3 - 12884901888*a**2*r**2 + 196608*a**2*r - a**2 - 268435456000000 > 0

	pre_cond = StrictGreaterThan(Add(Mul(Integer(281474976710656), Pow(Symbol('a'), Integer(2)), Pow(Symbol('r'), Integer(3))), Mul(Integer(-1), Integer(12884901888), Pow(Symbol('a'), Integer(2)), Pow(Symbol('r'), Integer(2))), Mul(Integer(196608), Pow(Symbol('a'), Integer(2)), Symbol('r')), Mul(Integer(-1), Pow(Symbol('a'), Integer(2))), Integer(-268435456000000)), Integer(0))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_18(a:sympy.Rational,r:sympy.Rational):
	#(4194304*r - 2025 > 0) & ((91125*a + 8589934592 < 0) | (-8303765625*a**2 - 1565515579392000*a + 2656331146614175432704*r - 75069446657476132864 > 0))

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(4194304), Symbol('r')), Integer(-2025)), Integer(0)), Or(StrictLessThan(Add(Mul(Integer(91125), Symbol('a')), Integer(8589934592)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Integer(8303765625), Pow(Symbol('a'), Integer(2))), Mul(Integer(-1), Integer(1565515579392000), Symbol('a')), Mul(Integer(2656331146614175432704), Symbol('r')), Integer(-75069446657476132864)), Integer(0))))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_19(a:sympy.Rational,r:sympy.Rational):
	#18014398509481984*a**2*r**3 - 206158430208*a**2*r**2 + 786432*a**2*r - a**2 - 17594659945578496 > 0

	pre_cond = StrictGreaterThan(Add(Mul(Integer(18014398509481984), Pow(Symbol('a'), Integer(2)), Pow(Symbol('r'), Integer(3))), Mul(Integer(-1), Integer(206158430208), Pow(Symbol('a'), Integer(2)), Pow(Symbol('r'), Integer(2))), Mul(Integer(786432), Pow(Symbol('a'), Integer(2)), Symbol('r')), Mul(Integer(-1), Pow(Symbol('a'), Integer(2))), Integer(-17594659945578496)), Integer(0))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_20(a:sympy.Rational,r:sympy.Rational):
	#(268435456*r - 65025 > 0) & ((16581375*a + 4398046511104 < 0) | (-274941996890625*a**2 - 145851316936114176000*a + 696341272098026404630757376*r - 19511492735717452300681216 > 0))

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(268435456), Symbol('r')), Integer(-65025)), Integer(0)), Or(StrictLessThan(Add(Mul(Integer(16581375), Symbol('a')), Integer(4398046511104)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Integer(274941996890625), Pow(Symbol('a'), Integer(2))), Mul(Integer(-1), Integer(145851316936114176000), Symbol('a')), Mul(Integer(696341272098026404630757376), Symbol('r')), Integer(-19511492735717452300681216)), Integer(0))))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_21(a:sympy.Rational,r:sympy.Rational):
	#1152921504606846976*a**2*r**3 - 3298534883328*a**2*r**2 + 3145728*a**2*r - a**2 - 1139450288143335424 > 0

	pre_cond = StrictGreaterThan(Add(Mul(Integer(1152921504606846976), Pow(Symbol('a'), Integer(2)), Pow(Symbol('r'), Integer(3))), Mul(Integer(-1), Integer(3298534883328), Pow(Symbol('a'), Integer(2)), Pow(Symbol('r'), Integer(2))), Mul(Integer(3145728), Pow(Symbol('a'), Integer(2)), Symbol('r')), Mul(Integer(-1), Pow(Symbol('a'), Integer(2))), Integer(-1139450288143335424)), Integer(0))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def post_condition(a:sympy.Rational, r:sympy.Rational, x:sympy.Rational, y:sympy.Rational):
	# (0 > -r + x**2 + y**2) & (0 > a*y**3 - 6*x + 1)

	post_cond =  And(StrictGreaterThan(Integer(0), Add(Mul(Integer(-1), Symbol('r')), Pow(Symbol('x'), Integer(2)), Pow(Symbol('y'), Integer(2)))), StrictGreaterThan(Integer(0), Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Mul(Integer(-1), Integer(6), Symbol('x')), Integer(1))))

	eval = post_cond.subs( { 'a':a, 'r':r, 'x':x, 'y':y })

	return eval == sympy.logic.boolalg.BooleanTrue



#return post-condition single variable
def return_post_condition_single_var(post_condition, a:sympy.Rational=None, r:sympy.Rational=None, x:sympy.Rational=None, y:sympy.Rational=None):
	assert a!=None
	assert r!=None


	if x==None:
		assert y!=None
		return lambda x: post_condition(a=a, r=r, x=x, y=y)

	if y==None:
		assert x!=None
		return lambda y: post_condition(a=a, r=r, x=x, y=y)


	return post_condition(a=a, r=r, x=x, y=y)


def get_univariate_poly( a:sympy.Rational, r:sympy.Rational, x:sympy.Rational, y:sympy.Rational ):


	post_cond =  And(StrictGreaterThan(Integer(0), Add(Mul(Integer(-1), Symbol('r')), Pow(Symbol('x'), Integer(2)), Pow(Symbol('y'), Integer(2)))), StrictGreaterThan(Integer(0), Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Mul(Integer(-1), Integer(6), Symbol('x')), Integer(1))))

	eval = post_cond.subs( { 'a':a, 'r':r, 'x':x, 'y':y })
	return eval



if __name__=="__main__":
	
	ip_0=int(input("enter numerator of a:\n"))
	ip_1=int(input("enter denominator of a:\n"))
	assert(ip_1!=0), ("Error denominator entered is 0")
	a=sympy.Rational(ip_0,ip_1)
	
	
	ip_0=int(input("enter numerator of r:\n"))
	ip_1=int(input("enter denominator of r:\n"))
	assert(ip_1!=0), ("Error denominator entered is 0")
	r=sympy.Rational(ip_0,ip_1)
	
	
	lambda_var_0 = sympy.symbols('lambda_var_0')
	
	
	if pre_condition_0(a=a,r=r)==True:
		all_vals = dict()
		all_vals['a'] = a
		all_vals['r'] = r
		all_vals['x'] = Add(Symbol('lambda_var_0'), Rational(1, 3))
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
	
	
	if pre_condition_1(a=a,r=r)==True:
		all_vals = dict()
		all_vals['a'] = a
		all_vals['r'] = r
		all_vals['x'] = Rational(1, 3)
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
	
	
	if pre_condition_2(a=a,r=r)==True:
		all_vals = dict()
		all_vals['a'] = a
		all_vals['r'] = r
		all_vals['x'] = Add(Symbol('lambda_var_0'), Rational(1, 16))
		all_vals['y'] = Rational(1, 8)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_2 SAT")

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_3(a=a,r=r)==True:
		all_vals = dict()
		all_vals['a'] = a
		all_vals['r'] = r
		all_vals['x'] = Rational(1, 16)
		all_vals['y'] = Add(Symbol('lambda_var_0'), Rational(1, 8))
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_3 SAT")

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_4(a=a,r=r)==True:
		all_vals = dict()
		all_vals['a'] = a
		all_vals['r'] = r
		all_vals['x'] = Add(Symbol('lambda_var_0'), Rational(991, 16384))
		all_vals['y'] = Rational(-7, 64)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_4 SAT")

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_5(a=a,r=r)==True:
		all_vals = dict()
		all_vals['a'] = a
		all_vals['r'] = r
		all_vals['x'] = Rational(991, 16384)
		all_vals['y'] = Add(Symbol('lambda_var_0'), Rational(-7, 64))
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_5 SAT")

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_6(a=a,r=r)==True:
		all_vals = dict()
		all_vals['a'] = a
		all_vals['r'] = r
		all_vals['x'] = Add(Symbol('lambda_var_0'), Rational(5, 128))
		all_vals['y'] = Rational(15, 128)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_6 SAT")

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_7(a=a,r=r)==True:
		all_vals = dict()
		all_vals['a'] = a
		all_vals['r'] = r
		all_vals['x'] = Rational(5, 128)
		all_vals['y'] = Add(Symbol('lambda_var_0'), Rational(15, 128))
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_7 SAT")

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_8(a=a,r=r)==True:
		all_vals = dict()
		all_vals['a'] = a
		all_vals['r'] = r
		all_vals['x'] = Add(Symbol('lambda_var_0'), Rational(1, 64))
		all_vals['y'] = Rational(1, 128)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_8 SAT")

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_9(a=a,r=r)==True:
		all_vals = dict()
		all_vals['a'] = a
		all_vals['r'] = r
		all_vals['x'] = Rational(1, 64)
		all_vals['y'] = Add(Symbol('lambda_var_0'), Rational(1, 128))
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_9 SAT")

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_10(a=a,r=r)==True:
		all_vals = dict()
		all_vals['a'] = a
		all_vals['r'] = r
		all_vals['x'] = Add(Symbol('lambda_var_0'), Rational(2107, 131072))
		all_vals['y'] = Rational(89, 1024)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_10 SAT")

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_11(a=a,r=r)==True:
		all_vals = dict()
		all_vals['a'] = a
		all_vals['r'] = r
		all_vals['x'] = Rational(2107, 131072)
		all_vals['y'] = Add(Symbol('lambda_var_0'), Rational(89, 1024))
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_11 SAT")

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_12(a=a,r=r)==True:
		all_vals = dict()
		all_vals['a'] = a
		all_vals['r'] = r
		all_vals['x'] = Add(Symbol('lambda_var_0'), Rational(253, 16384))
		all_vals['y'] = Rational(31, 512)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_12 SAT")

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_13(a=a,r=r)==True:
		all_vals = dict()
		all_vals['a'] = a
		all_vals['r'] = r
		all_vals['x'] = Rational(253, 16384)
		all_vals['y'] = Add(Symbol('lambda_var_0'), Rational(31, 512))
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_13 SAT")

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_14(a=a,r=r)==True:
		all_vals = dict()
		all_vals['a'] = a
		all_vals['r'] = r
		all_vals['x'] = Add(Symbol('lambda_var_0'), Rational(1, 128))
		all_vals['y'] = Rational(11, 256)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_14 SAT")

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_15(a=a,r=r)==True:
		all_vals = dict()
		all_vals['a'] = a
		all_vals['r'] = r
		all_vals['x'] = Rational(1, 128)
		all_vals['y'] = Add(Symbol('lambda_var_0'), Rational(11, 256))
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_15 SAT")

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_16(a=a,r=r)==True:
		all_vals = dict()
		all_vals['a'] = a
		all_vals['r'] = r
		all_vals['x'] = Add(Symbol('lambda_var_0'), Rational(1, 256))
		all_vals['y'] = Rational(63, 2048)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_16 SAT")

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_17(a=a,r=r)==True:
		all_vals = dict()
		all_vals['a'] = a
		all_vals['r'] = r
		all_vals['x'] = Rational(1, 256)
		all_vals['y'] = Add(Symbol('lambda_var_0'), Rational(63, 2048))
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_17 SAT")

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_18(a=a,r=r)==True:
		all_vals = dict()
		all_vals['a'] = a
		all_vals['r'] = r
		all_vals['x'] = Add(Symbol('lambda_var_0'), Rational(1, 512))
		all_vals['y'] = Rational(45, 2048)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_18 SAT")

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_19(a=a,r=r)==True:
		all_vals = dict()
		all_vals['a'] = a
		all_vals['r'] = r
		all_vals['x'] = Rational(1, 512)
		all_vals['y'] = Add(Symbol('lambda_var_0'), Rational(45, 2048))
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_19 SAT")

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_20(a=a,r=r)==True:
		all_vals = dict()
		all_vals['a'] = a
		all_vals['r'] = r
		all_vals['x'] = Add(Symbol('lambda_var_0'), Rational(1, 1024))
		all_vals['y'] = Rational(255, 16384)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_20 SAT")

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_21(a=a,r=r)==True:
		all_vals = dict()
		all_vals['a'] = a
		all_vals['r'] = r
		all_vals['x'] = Rational(1, 1024)
		all_vals['y'] = Add(Symbol('lambda_var_0'), Rational(255, 16384))
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_21 SAT")

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass


	print("UNKNOWN")
