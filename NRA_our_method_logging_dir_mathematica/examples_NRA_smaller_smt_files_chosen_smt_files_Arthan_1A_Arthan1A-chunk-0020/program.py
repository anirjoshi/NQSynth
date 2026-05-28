import sympy
from sympy import *
from NQS.helper_program_cav import get_lambda_val

def pre_condition_0(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 1/8) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi - 2*skoS > 0)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Rational(1, 8)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Add(Symbol('pi'), Mul(Integer(-1), Integer(2), Symbol('skoS'))), Integer(0)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi - 2*skoS > 0)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Add(Symbol('pi'), Mul(Integer(-1), Integer(2), Symbol('skoS'))), Integer(0)))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def post_condition(delta:sympy.Rational, skoS:sympy.Rational, pi:sympy.Rational, skoCOSS:sympy.Rational, skoSINS:sympy.Rational):
	# (0 <= delta) & (0 <= skoCOSS) & (0 <= skoS) & (skoSINS <= skoS) & (31415927/10000000 > pi) & (pi > 15707963/5000000) & (pi/2 > skoS) & (skoCOSS**2 + skoSINS**2 - 1 <= delta) & (-skoCOSS**2 - skoSINS**2 + 1 <= delta)

	post_cond =  And(LessThan(Integer(0), Symbol('delta')), LessThan(Integer(0), Symbol('skoCOSS')), LessThan(Integer(0), Symbol('skoS')), LessThan(Symbol('skoSINS'), Symbol('skoS')), StrictGreaterThan(Rational(31415927, 10000000), Symbol('pi')), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Mul(Rational(1, 2), Symbol('pi')), Symbol('skoS')), LessThan(Add(Pow(Symbol('skoCOSS'), Integer(2)), Pow(Symbol('skoSINS'), Integer(2)), Integer(-1)), Symbol('delta')), LessThan(Add(Mul(Integer(-1), Pow(Symbol('skoCOSS'), Integer(2))), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(1)), Symbol('delta')))

	eval = post_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi, 'skoCOSS':skoCOSS, 'skoSINS':skoSINS })

	return eval == sympy.logic.boolalg.BooleanTrue



#return post-condition single variable
def return_post_condition_single_var(post_condition, delta:sympy.Rational=None, skoS:sympy.Rational=None, pi:sympy.Rational=None, skoCOSS:sympy.Rational=None, skoSINS:sympy.Rational=None):
	assert delta!=None
	assert skoS!=None
	assert pi!=None


	if skoCOSS==None:
		assert skoSINS!=None
		return lambda skoCOSS: post_condition(delta=delta, skoS=skoS, pi=pi, skoCOSS=skoCOSS, skoSINS=skoSINS)

	if skoSINS==None:
		assert skoCOSS!=None
		return lambda skoSINS: post_condition(delta=delta, skoS=skoS, pi=pi, skoCOSS=skoCOSS, skoSINS=skoSINS)


	return post_condition(delta=delta, skoS=skoS, pi=pi, skoCOSS=skoCOSS, skoSINS=skoSINS)


def get_univariate_poly( delta:sympy.Rational, skoS:sympy.Rational, pi:sympy.Rational, skoCOSS:sympy.Rational, skoSINS:sympy.Rational ):


	post_cond =  And(LessThan(Integer(0), Symbol('delta')), LessThan(Integer(0), Symbol('skoCOSS')), LessThan(Integer(0), Symbol('skoS')), LessThan(Symbol('skoSINS'), Symbol('skoS')), StrictGreaterThan(Rational(31415927, 10000000), Symbol('pi')), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Mul(Rational(1, 2), Symbol('pi')), Symbol('skoS')), LessThan(Add(Pow(Symbol('skoCOSS'), Integer(2)), Pow(Symbol('skoSINS'), Integer(2)), Integer(-1)), Symbol('delta')), LessThan(Add(Mul(Integer(-1), Pow(Symbol('skoCOSS'), Integer(2))), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(1)), Symbol('delta')))

	eval = post_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi, 'skoCOSS':skoCOSS, 'skoSINS':skoSINS })
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
	
	
	ip_0=int(input("enter numerator of pi:\n"))
	ip_1=int(input("enter denominator of pi:\n"))
	assert(ip_1!=0), ("Error denominator entered is 0")
	pi=sympy.Rational(ip_0,ip_1)
	
	
	lambda_var_0 = sympy.symbols('lambda_var_0')
	
	
	if pre_condition_0(delta=delta,skoS=skoS,pi=pi)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoS'] = skoS
		all_vals['pi'] = pi
		all_vals['skoCOSS'] = Add(Symbol('lambda_var_0'), Integer(1))
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
	
	
	if pre_condition_1(delta=delta,skoS=skoS,pi=pi)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoS'] = skoS
		all_vals['pi'] = pi
		all_vals['skoCOSS'] = Integer(1)
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
