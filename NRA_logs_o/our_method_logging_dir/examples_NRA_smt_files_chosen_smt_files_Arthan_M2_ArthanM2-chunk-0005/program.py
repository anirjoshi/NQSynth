import sympy
from sympy import *
from NQS.helper_program_cav import get_lambda_val

def pre_condition_0(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM - 2 >= 0) & (-delta + skoSINS**2 - 1 <= 0)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Add(Symbol('skoM'), Integer(-2)), Integer(0)), LessThan(Add(Mul(Integer(-1), Symbol('delta')), Pow(Symbol('skoSINS'), Integer(2)), Integer(-1)), Integer(0)))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1(delta:sympy.Rational,skoSINS:sympy.Rational,skoM:sympy.Rational):
	#(delta >= 0) & (skoM - 2 >= 0) & (64*delta + 64*skoSINS**2 - 63 >= 0) & (-64*delta + 64*skoSINS**2 - 63 <= 0)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Add(Symbol('skoM'), Integer(-2)), Integer(0)), GreaterThan(Add(Mul(Integer(64), Symbol('delta')), Mul(Integer(64), Pow(Symbol('skoSINS'), Integer(2))), Integer(-63)), Integer(0)), LessThan(Add(Mul(Integer(-1), Integer(64), Symbol('delta')), Mul(Integer(64), Pow(Symbol('skoSINS'), Integer(2))), Integer(-63)), Integer(0)))

	eval = pre_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM })

	if eval==True:
		assert eval!=False
		return True
	return False


def post_condition(delta:sympy.Rational, skoSINS:sympy.Rational, skoM:sympy.Rational, skoCOSS:sympy.Rational, skoS:sympy.Rational):
	# (0 <= delta) & (2 <= skoM) & (2 <= skoS) & (skoCOSS**2 + skoSINS**2 - 1 <= delta) & (-skoCOSS**2 - skoSINS**2 + 1 <= delta)

	post_cond =  And(LessThan(Integer(0), Symbol('delta')), LessThan(Integer(2), Symbol('skoM')), LessThan(Integer(2), Symbol('skoS')), LessThan(Add(Pow(Symbol('skoCOSS'), Integer(2)), Pow(Symbol('skoSINS'), Integer(2)), Integer(-1)), Symbol('delta')), LessThan(Add(Mul(Integer(-1), Pow(Symbol('skoCOSS'), Integer(2))), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(1)), Symbol('delta')))

	eval = post_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM, 'skoCOSS':skoCOSS, 'skoS':skoS })

	return eval == sympy.logic.boolalg.BooleanTrue



#return post-condition single variable
def return_post_condition_single_var(post_condition, delta:sympy.Rational=None, skoSINS:sympy.Rational=None, skoM:sympy.Rational=None, skoCOSS:sympy.Rational=None, skoS:sympy.Rational=None):
	assert delta!=None
	assert skoSINS!=None
	assert skoM!=None


	if skoCOSS==None:
		assert skoS!=None
		return lambda skoCOSS: post_condition(delta=delta, skoSINS=skoSINS, skoM=skoM, skoCOSS=skoCOSS, skoS=skoS)

	if skoS==None:
		assert skoCOSS!=None
		return lambda skoS: post_condition(delta=delta, skoSINS=skoSINS, skoM=skoM, skoCOSS=skoCOSS, skoS=skoS)


	return post_condition(delta=delta, skoSINS=skoSINS, skoM=skoM, skoCOSS=skoCOSS, skoS=skoS)


def get_univariate_poly( delta:sympy.Rational, skoSINS:sympy.Rational, skoM:sympy.Rational, skoCOSS:sympy.Rational, skoS:sympy.Rational ):


	post_cond =  And(LessThan(Integer(0), Symbol('delta')), LessThan(Integer(2), Symbol('skoM')), LessThan(Integer(2), Symbol('skoS')), LessThan(Add(Pow(Symbol('skoCOSS'), Integer(2)), Pow(Symbol('skoSINS'), Integer(2)), Integer(-1)), Symbol('delta')), LessThan(Add(Mul(Integer(-1), Pow(Symbol('skoCOSS'), Integer(2))), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(1)), Symbol('delta')))

	eval = post_cond.subs( { 'delta':delta, 'skoSINS':skoSINS, 'skoM':skoM, 'skoCOSS':skoCOSS, 'skoS':skoS })
	return eval



if __name__=="__main__":
	
	ip_0=int(input("enter numerator of delta:\n"))
	ip_1=int(input("enter denominator of delta:\n"))
	assert(ip_1!=0), ("Error denominator entered is 0")
	delta=sympy.Rational(ip_0,ip_1)
	
	
	ip_0=int(input("enter numerator of skoSINS:\n"))
	ip_1=int(input("enter denominator of skoSINS:\n"))
	assert(ip_1!=0), ("Error denominator entered is 0")
	skoSINS=sympy.Rational(ip_0,ip_1)
	
	
	ip_0=int(input("enter numerator of skoM:\n"))
	ip_1=int(input("enter denominator of skoM:\n"))
	assert(ip_1!=0), ("Error denominator entered is 0")
	skoM=sympy.Rational(ip_0,ip_1)
	
	
	lambda_var_0 = sympy.symbols('lambda_var_0')
	
	
	if pre_condition_0(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoSINS'] = skoSINS
		all_vals['skoM'] = skoM
		all_vals['skoCOSS'] = Add(Symbol('lambda_var_0'), Rational(1, 8))
		all_vals['skoS'] = Integer(2)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_0 SAT")

			print("skoCOSS=", all_vals["skoCOSS"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoS=", all_vals["skoS"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_1(delta=delta,skoSINS=skoSINS,skoM=skoM)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoSINS'] = skoSINS
		all_vals['skoM'] = skoM
		all_vals['skoCOSS'] = Rational(1, 8)
		all_vals['skoS'] = Add(Symbol('lambda_var_0'), Integer(2))
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_1 SAT")

			print("skoCOSS=", all_vals["skoCOSS"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoS=", all_vals["skoS"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass


	print("Weakest pre-condition UNSAT")
