import sympy
from sympy import *
from NQS.helper_program_cav import get_lambda_val

def pre_condition_0(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta - 99 >= 0) & (100*skoS - 217 > 0) & (skoS**2 + skoS - 9 >= 0) & ((delta - 136 > 0) | (delta**2*skoS + delta**2 - 34*delta*skoS**3 - 78*delta*skoS**2 - 163*delta*skoS - 119*delta + 48*skoS**5 + 140*skoS**4 + 2344*skoS**3 + 5484*skoS**2 + 10340*skoS + 6460 > 0) | (delta**2*skoS**2 + 2*delta**2*skoS + delta**2 - 17*delta*skoS**4 - 52*delta*skoS**3 - 163*delta*skoS**2 - 238*delta*skoS - 191*delta + 16*skoS**6 + 56*skoS**5 + 1172*skoS**4 + 3656*skoS**3 + 10340*skoS**2 + 12920*skoS + 13204 <= 0))

	pre_cond = And(GreaterThan(Add(Symbol('delta'), Integer(-99)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(100), Symbol('skoS')), Integer(-217)), Integer(0)), GreaterThan(Add(Pow(Symbol('skoS'), Integer(2)), Symbol('skoS'), Integer(-9)), Integer(0)), Or(StrictGreaterThan(Add(Symbol('delta'), Integer(-136)), Integer(0)), StrictGreaterThan(Add(Mul(Pow(Symbol('delta'), Integer(2)), Symbol('skoS')), Pow(Symbol('delta'), Integer(2)), Mul(Integer(-1), Integer(34), Symbol('delta'), Pow(Symbol('skoS'), Integer(3))), Mul(Integer(-1), Integer(78), Symbol('delta'), Pow(Symbol('skoS'), Integer(2))), Mul(Integer(-1), Integer(163), Symbol('delta'), Symbol('skoS')), Mul(Integer(-1), Integer(119), Symbol('delta')), Mul(Integer(48), Pow(Symbol('skoS'), Integer(5))), Mul(Integer(140), Pow(Symbol('skoS'), Integer(4))), Mul(Integer(2344), Pow(Symbol('skoS'), Integer(3))), Mul(Integer(5484), Pow(Symbol('skoS'), Integer(2))), Mul(Integer(10340), Symbol('skoS')), Integer(6460)), Integer(0)), LessThan(Add(Mul(Pow(Symbol('delta'), Integer(2)), Pow(Symbol('skoS'), Integer(2))), Mul(Integer(2), Pow(Symbol('delta'), Integer(2)), Symbol('skoS')), Pow(Symbol('delta'), Integer(2)), Mul(Integer(-1), Integer(17), Symbol('delta'), Pow(Symbol('skoS'), Integer(4))), Mul(Integer(-1), Integer(52), Symbol('delta'), Pow(Symbol('skoS'), Integer(3))), Mul(Integer(-1), Integer(163), Symbol('delta'), Pow(Symbol('skoS'), Integer(2))), Mul(Integer(-1), Integer(238), Symbol('delta'), Symbol('skoS')), Mul(Integer(-1), Integer(191), Symbol('delta')), Mul(Integer(16), Pow(Symbol('skoS'), Integer(6))), Mul(Integer(56), Pow(Symbol('skoS'), Integer(5))), Mul(Integer(1172), Pow(Symbol('skoS'), Integer(4))), Mul(Integer(3656), Pow(Symbol('skoS'), Integer(3))), Mul(Integer(10340), Pow(Symbol('skoS'), Integer(2))), Mul(Integer(12920), Symbol('skoS')), Integer(13204)), Integer(0))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def post_condition(delta:sympy.Rational, skoS:sympy.Rational, skoCOSS:sympy.Rational, skoSINS:sympy.Rational):
	# (0 <= delta) & (217/100 <= skoS) & (skoCOSS**2 + skoSINS**2 - 1 <= delta) & (-skoCOSS**2 - skoSINS**2 + 1 <= delta) & (skoSINS*(-2*skoCOSS + skoS*(skoS*(skoS + 2) - 4) + skoSINS*(skoS + 1) - 3) <= skoCOSS*(-2*skoCOSS - 2) + skoS*(skoCOSS*(-2*skoCOSS - 10) + skoS*(-6*skoCOSS - 2*skoS - 6)) + 2)

	post_cond =  And(LessThan(Integer(0), Symbol('delta')), LessThan(Rational(217, 100), Symbol('skoS')), LessThan(Add(Pow(Symbol('skoCOSS'), Integer(2)), Pow(Symbol('skoSINS'), Integer(2)), Integer(-1)), Symbol('delta')), LessThan(Add(Mul(Integer(-1), Pow(Symbol('skoCOSS'), Integer(2))), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(1)), Symbol('delta')), LessThan(Mul(Symbol('skoSINS'), Add(Mul(Integer(-1), Integer(2), Symbol('skoCOSS')), Mul(Symbol('skoS'), Add(Mul(Symbol('skoS'), Add(Symbol('skoS'), Integer(2))), Integer(-4))), Mul(Symbol('skoSINS'), Add(Symbol('skoS'), Integer(1))), Integer(-3))), Add(Mul(Symbol('skoCOSS'), Add(Mul(Integer(-1), Integer(2), Symbol('skoCOSS')), Integer(-2))), Mul(Symbol('skoS'), Add(Mul(Symbol('skoCOSS'), Add(Mul(Integer(-1), Integer(2), Symbol('skoCOSS')), Integer(-10))), Mul(Symbol('skoS'), Add(Mul(Integer(-1), Integer(6), Symbol('skoCOSS')), Mul(Integer(-1), Integer(2), Symbol('skoS')), Integer(-6))))), Integer(2))))

	eval = post_cond.subs( { 'delta':delta, 'skoS':skoS, 'skoCOSS':skoCOSS, 'skoSINS':skoSINS })

	return eval == sympy.logic.boolalg.BooleanTrue



#return post-condition single variable
def return_post_condition_single_var(post_condition, delta:sympy.Rational=None, skoS:sympy.Rational=None, skoCOSS:sympy.Rational=None, skoSINS:sympy.Rational=None):
	assert delta!=None
	assert skoS!=None


	if skoCOSS==None:
		assert skoSINS!=None
		return lambda skoCOSS: post_condition(delta=delta, skoS=skoS, skoCOSS=skoCOSS, skoSINS=skoSINS)

	if skoSINS==None:
		assert skoCOSS!=None
		return lambda skoSINS: post_condition(delta=delta, skoS=skoS, skoCOSS=skoCOSS, skoSINS=skoSINS)


	return post_condition(delta=delta, skoS=skoS, skoCOSS=skoCOSS, skoSINS=skoSINS)


def get_univariate_poly( delta:sympy.Rational, skoS:sympy.Rational, skoCOSS:sympy.Rational, skoSINS:sympy.Rational ):


	post_cond =  And(LessThan(Integer(0), Symbol('delta')), LessThan(Rational(217, 100), Symbol('skoS')), LessThan(Add(Pow(Symbol('skoCOSS'), Integer(2)), Pow(Symbol('skoSINS'), Integer(2)), Integer(-1)), Symbol('delta')), LessThan(Add(Mul(Integer(-1), Pow(Symbol('skoCOSS'), Integer(2))), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(1)), Symbol('delta')), LessThan(Mul(Symbol('skoSINS'), Add(Mul(Integer(-1), Integer(2), Symbol('skoCOSS')), Mul(Symbol('skoS'), Add(Mul(Symbol('skoS'), Add(Symbol('skoS'), Integer(2))), Integer(-4))), Mul(Symbol('skoSINS'), Add(Symbol('skoS'), Integer(1))), Integer(-3))), Add(Mul(Symbol('skoCOSS'), Add(Mul(Integer(-1), Integer(2), Symbol('skoCOSS')), Integer(-2))), Mul(Symbol('skoS'), Add(Mul(Symbol('skoCOSS'), Add(Mul(Integer(-1), Integer(2), Symbol('skoCOSS')), Integer(-10))), Mul(Symbol('skoS'), Add(Mul(Integer(-1), Integer(6), Symbol('skoCOSS')), Mul(Integer(-1), Integer(2), Symbol('skoS')), Integer(-6))))), Integer(2))))

	eval = post_cond.subs( { 'delta':delta, 'skoS':skoS, 'skoCOSS':skoCOSS, 'skoSINS':skoSINS })
	return eval



if __name__=="__main__":
	
	ip_0=int(input("enter numerator of delta:\n"))
	ip_1=int(input("enter denominator of delta:\n"))
	assert(ip_1!=0), ("Error denominator entered is 0")
	delta=sympy.Rational(ip_0,ip_1)
	
	
	ip_0=int(input("enter numerator of skoS:\n"))
	ip_1=int(input("enter denominator of skoS:\n"))
	assert(ip_1!=0), ("Error denominator entered is 0")
	skoS=sympy.Rational(ip_0,ip_1)
	
	
	lambda_var_0 = sympy.symbols('lambda_var_0')
	
	
	if pre_condition_0(delta=delta,skoS=skoS)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoS'] = skoS
		all_vals['skoCOSS'] = Add(Symbol('lambda_var_0'), Rational(1, 8))
		all_vals['skoSINS'] = Integer(-10)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_0 SAT")

			print("skoCOSS=", all_vals["skoCOSS"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSINS=", all_vals["skoSINS"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass


	print("UNKNOWN")
