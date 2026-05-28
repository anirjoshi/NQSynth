import sympy
from sympy import *
from NQS.helper_program_cav import get_lambda_val

def pre_condition_0(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (20*skoS - 9 >= 0)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Add(Mul(Integer(20), Symbol('skoS')), Integer(-9)), Integer(0)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1(delta:sympy.Rational,skoS:sympy.Rational):
	#(delta >= 0) & (20*skoS - 9 >= 0)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Add(Mul(Integer(20), Symbol('skoS')), Integer(-9)), Integer(0)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS })

	if eval==True:
		assert eval!=False
		return True
	return False


def post_condition(delta:sympy.Rational, skoS:sympy.Rational, skoCOSS:sympy.Rational, skoSINS:sympy.Rational):
	# (0 <= delta) & (9/20 <= skoS) & (skoSINS*(-skoCOSS/2 + skoS*(skoS*(skoS/2 + 3/2) - 3/2) + skoSINS*(skoS/4 + 1/4) - 5/2) > skoCOSS*(-skoCOSS/2 - 3) + skoS*(skoCOSS*(-skoCOSS/2 - 6) + skoS*(-3*skoCOSS - 2*skoS - 6) - 6) - 2)

	post_cond =  And(LessThan(Integer(0), Symbol('delta')), LessThan(Rational(9, 20), Symbol('skoS')), StrictGreaterThan(Mul(Symbol('skoSINS'), Add(Mul(Integer(-1), Rational(1, 2), Symbol('skoCOSS')), Mul(Symbol('skoS'), Add(Mul(Symbol('skoS'), Add(Mul(Rational(1, 2), Symbol('skoS')), Rational(3, 2))), Rational(-3, 2))), Mul(Symbol('skoSINS'), Add(Mul(Rational(1, 4), Symbol('skoS')), Rational(1, 4))), Rational(-5, 2))), Add(Mul(Symbol('skoCOSS'), Add(Mul(Integer(-1), Rational(1, 2), Symbol('skoCOSS')), Integer(-3))), Mul(Symbol('skoS'), Add(Mul(Symbol('skoCOSS'), Add(Mul(Integer(-1), Rational(1, 2), Symbol('skoCOSS')), Integer(-6))), Mul(Symbol('skoS'), Add(Mul(Integer(-1), Integer(3), Symbol('skoCOSS')), Mul(Integer(-1), Integer(2), Symbol('skoS')), Integer(-6))), Integer(-6))), Integer(-2))))

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


	post_cond =  And(LessThan(Integer(0), Symbol('delta')), LessThan(Rational(9, 20), Symbol('skoS')), StrictGreaterThan(Mul(Symbol('skoSINS'), Add(Mul(Integer(-1), Rational(1, 2), Symbol('skoCOSS')), Mul(Symbol('skoS'), Add(Mul(Symbol('skoS'), Add(Mul(Rational(1, 2), Symbol('skoS')), Rational(3, 2))), Rational(-3, 2))), Mul(Symbol('skoSINS'), Add(Mul(Rational(1, 4), Symbol('skoS')), Rational(1, 4))), Rational(-5, 2))), Add(Mul(Symbol('skoCOSS'), Add(Mul(Integer(-1), Rational(1, 2), Symbol('skoCOSS')), Integer(-3))), Mul(Symbol('skoS'), Add(Mul(Symbol('skoCOSS'), Add(Mul(Integer(-1), Rational(1, 2), Symbol('skoCOSS')), Integer(-6))), Mul(Symbol('skoS'), Add(Mul(Integer(-1), Integer(3), Symbol('skoCOSS')), Mul(Integer(-1), Integer(2), Symbol('skoS')), Integer(-6))), Integer(-6))), Integer(-2))))

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
		all_vals['skoCOSS'] = Add(Symbol('lambda_var_0'), Integer(-2))
		all_vals['skoSINS'] = Rational(1, 8)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_0 SAT")

			print("skoCOSS=", all_vals["skoCOSS"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSINS=", all_vals["skoSINS"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_1(delta=delta,skoS=skoS)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoS'] = skoS
		all_vals['skoCOSS'] = Integer(-2)
		all_vals['skoSINS'] = Add(Symbol('lambda_var_0'), Rational(1, 8))
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_1 SAT")

			print("skoCOSS=", all_vals["skoCOSS"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSINS=", all_vals["skoSINS"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass


	print("Weakest pre-condition UNSAT")
