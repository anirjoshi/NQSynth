import sympy
from sympy import *
from NQS.helper_program_cav import get_lambda_val

def pre_condition_0(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX - 1 < 0) & Ne(delta + skoS2**2 - 2, 0) & Ne(-delta + skoS2**2 - 2, 0) & ((delta + skoS2**2 - 2 < 0) | (-delta + skoS2**2 - 2 > 0))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Add(Symbol('skoX'), Integer(-1)), Integer(0)), Unequality(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2)), Integer(-2)), Integer(0)), Unequality(Add(Mul(Integer(-1), Symbol('delta')), Pow(Symbol('skoS2'), Integer(2)), Integer(-2)), Integer(0)), Or(StrictLessThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2)), Integer(-2)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('delta')), Pow(Symbol('skoS2'), Integer(2)), Integer(-2)), Integer(0))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX - 1 < 0) & Ne(delta + skoS2**2 - 2, 0) & Ne(-delta + skoS2**2 - 2, 0) & ((delta + skoS2**2 - 2 < 0) | (-delta + skoS2**2 - 2 > 0))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Add(Symbol('skoX'), Integer(-1)), Integer(0)), Unequality(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2)), Integer(-2)), Integer(0)), Unequality(Add(Mul(Integer(-1), Symbol('delta')), Pow(Symbol('skoS2'), Integer(2)), Integer(-2)), Integer(0)), Or(StrictLessThan(Add(Symbol('delta'), Pow(Symbol('skoS2'), Integer(2)), Integer(-2)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('delta')), Pow(Symbol('skoS2'), Integer(2)), Integer(-2)), Integer(0))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def post_condition(delta:sympy.Rational, skoX:sympy.Rational, skoS2:sympy.Rational, skoSP:sympy.Rational, skoSM:sympy.Rational):
	# (0 <= delta) & (1 > skoX) & (skoS2 > 0) & (skoSM > 0) & (skoSP > 0) & (skoX > 0) & ~((skoS2**2 - 2 <= delta) & (2 - skoS2**2 <= delta))

	post_cond =  And(LessThan(Integer(0), Symbol('delta')), StrictGreaterThan(Integer(1), Symbol('skoX')), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoSP'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), Not(And(LessThan(Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2)), Symbol('delta')), LessThan(Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2)))), Symbol('delta')))))

	eval = post_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'skoSP':skoSP, 'skoSM':skoSM })

	return eval == sympy.logic.boolalg.BooleanTrue



#return post-condition single variable
def return_post_condition_single_var(post_condition, delta:sympy.Rational=None, skoX:sympy.Rational=None, skoS2:sympy.Rational=None, skoSP:sympy.Rational=None, skoSM:sympy.Rational=None):
	assert delta!=None
	assert skoX!=None
	assert skoS2!=None


	if skoSP==None:
		assert skoSM!=None
		return lambda skoSP: post_condition(delta=delta, skoX=skoX, skoS2=skoS2, skoSP=skoSP, skoSM=skoSM)

	if skoSM==None:
		assert skoSP!=None
		return lambda skoSM: post_condition(delta=delta, skoX=skoX, skoS2=skoS2, skoSP=skoSP, skoSM=skoSM)


	return post_condition(delta=delta, skoX=skoX, skoS2=skoS2, skoSP=skoSP, skoSM=skoSM)


def get_univariate_poly( delta:sympy.Rational, skoX:sympy.Rational, skoS2:sympy.Rational, skoSP:sympy.Rational, skoSM:sympy.Rational ):


	post_cond =  And(LessThan(Integer(0), Symbol('delta')), StrictGreaterThan(Integer(1), Symbol('skoX')), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoSP'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), Not(And(LessThan(Add(Pow(Symbol('skoS2'), Integer(2)), Integer(-2)), Symbol('delta')), LessThan(Add(Integer(2), Mul(Integer(-1), Pow(Symbol('skoS2'), Integer(2)))), Symbol('delta')))))

	eval = post_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'skoSP':skoSP, 'skoSM':skoSM })
	return eval



if __name__=="__main__":
	
	ip_0=int(input("enter numerator of delta:\n"))
	ip_1=int(input("enter denominator of delta:\n"))
	assert(ip_1!=0), ("Error denominator entered is 0")
	delta=sympy.Rational(ip_0,ip_1)
	
	
	ip_0=int(input("enter numerator of skoX:\n"))
	ip_1=int(input("enter denominator of skoX:\n"))
	assert(ip_1!=0), ("Error denominator entered is 0")
	skoX=sympy.Rational(ip_0,ip_1)
	
	
	ip_0=int(input("enter numerator of skoS2:\n"))
	ip_1=int(input("enter denominator of skoS2:\n"))
	assert(ip_1!=0), ("Error denominator entered is 0")
	skoS2=sympy.Rational(ip_0,ip_1)
	
	
	lambda_var_0 = sympy.symbols('lambda_var_0')
	
	
	if pre_condition_0(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoX'] = skoX
		all_vals['skoS2'] = skoS2
		all_vals['skoSP'] = Add(Symbol('lambda_var_0'), Integer(1))
		all_vals['skoSM'] = Integer(1)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_0 SAT")

			print("skoSP=", all_vals["skoSP"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSM=", all_vals["skoSM"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_1(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoX'] = skoX
		all_vals['skoS2'] = skoS2
		all_vals['skoSP'] = Integer(1)
		all_vals['skoSM'] = Add(Symbol('lambda_var_0'), Integer(1))
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_1 SAT")

			print("skoSP=", all_vals["skoSP"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSM=", all_vals["skoSM"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass


	print("Weakest pre-condition UNSAT")
