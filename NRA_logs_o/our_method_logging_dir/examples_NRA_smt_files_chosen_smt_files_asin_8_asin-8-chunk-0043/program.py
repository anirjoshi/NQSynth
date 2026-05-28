import sympy
from sympy import *
from NQS.helper_program_cav import get_lambda_val

def pre_condition_0(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoX > 0) & (skoX - 1 < 0) & (5000000*pi - 15707963 > 0) & (10000000*pi - 31415927 < 0) & Ne(2*skoS2 + 1, 0) & Ne(20*pi*skoS2 + 10*pi + 1, 0) & ((2*skoS2 + 1 > 0) | (20*pi*skoS2 + 10*pi + 1 < 0))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Add(Symbol('skoX'), Integer(-1)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(5000000), Symbol('pi')), Integer(-15707963)), Integer(0)), StrictLessThan(Add(Mul(Integer(10000000), Symbol('pi')), Integer(-31415927)), Integer(0)), Unequality(Add(Mul(Integer(2), Symbol('skoS2')), Integer(1)), Integer(0)), Unequality(Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(1)), Integer(0)), Or(StrictGreaterThan(Add(Mul(Integer(2), Symbol('skoS2')), Integer(1)), Integer(0)), StrictLessThan(Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(1)), Integer(0))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoX > 0) & (skoX - 1 < 0) & (5000000*pi - 15707963 > 0) & (2*skoS2 + 1 > 0) & (10000000*pi - 31415927 < 0)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Add(Symbol('skoX'), Integer(-1)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(5000000), Symbol('pi')), Integer(-15707963)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(2), Symbol('skoS2')), Integer(1)), Integer(0)), StrictLessThan(Add(Mul(Integer(10000000), Symbol('pi')), Integer(-31415927)), Integer(0)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_2(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoX > 0) & (skoX - 1 < 0) & (5000000*pi - 15707963 > 0) & (10000000*pi - 31415927 < 0) & (2*skoS2 + 1 < 0)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Add(Symbol('skoX'), Integer(-1)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(5000000), Symbol('pi')), Integer(-15707963)), Integer(0)), StrictLessThan(Add(Mul(Integer(10000000), Symbol('pi')), Integer(-31415927)), Integer(0)), StrictLessThan(Add(Mul(Integer(2), Symbol('skoS2')), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_3(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoX > 0) & (skoX - 1 < 0) & (5000000*pi - 15707963 > 0) & (10000000*pi - 31415927 < 0) & Ne(2*skoS2 + 1, 0) & Ne(20*pi*skoS2 + 10*pi - 1, 0) & ((2*skoS2 + 1 < 0) | (20*pi*skoS2 + 10*pi - 1 > 0))

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Add(Symbol('skoX'), Integer(-1)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(5000000), Symbol('pi')), Integer(-15707963)), Integer(0)), StrictLessThan(Add(Mul(Integer(10000000), Symbol('pi')), Integer(-31415927)), Integer(0)), Unequality(Add(Mul(Integer(2), Symbol('skoS2')), Integer(1)), Integer(0)), Unequality(Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1)), Integer(0)), Or(StrictLessThan(Add(Mul(Integer(2), Symbol('skoS2')), Integer(1)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1)), Integer(0))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def post_condition(delta:sympy.Rational, skoX:sympy.Rational, skoS2:sympy.Rational, pi:sympy.Rational, skoSP:sympy.Rational, skoSM:sympy.Rational):
	# (0 <= delta) & (1 > skoX) & (31415927/10000000 > pi) & (pi > 15707963/5000000) & (skoX > 0) & (skoX*(-skoSM - skoSP - 4) > 0) & (skoSP*(pi*skoS2 + pi/2 + 1/20) > skoSM*(pi*skoS2 + pi/2 - 1/20) - 1/5)

	post_cond =  And(LessThan(Integer(0), Symbol('delta')), StrictGreaterThan(Integer(1), Symbol('skoX')), StrictGreaterThan(Rational(31415927, 10000000), Symbol('pi')), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictGreaterThan(Mul(Symbol('skoX'), Add(Mul(Integer(-1), Symbol('skoSM')), Mul(Integer(-1), Symbol('skoSP')), Integer(-4))), Integer(0)), StrictGreaterThan(Mul(Symbol('skoSP'), Add(Mul(Symbol('pi'), Symbol('skoS2')), Mul(Rational(1, 2), Symbol('pi')), Rational(1, 20))), Add(Mul(Symbol('skoSM'), Add(Mul(Symbol('pi'), Symbol('skoS2')), Mul(Rational(1, 2), Symbol('pi')), Rational(-1, 20))), Rational(-1, 5))))

	eval = post_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi, 'skoSP':skoSP, 'skoSM':skoSM })

	return eval == sympy.logic.boolalg.BooleanTrue



#return post-condition single variable
def return_post_condition_single_var(post_condition, delta:sympy.Rational=None, skoX:sympy.Rational=None, skoS2:sympy.Rational=None, pi:sympy.Rational=None, skoSP:sympy.Rational=None, skoSM:sympy.Rational=None):
	assert delta!=None
	assert skoX!=None
	assert skoS2!=None
	assert pi!=None


	if skoSP==None:
		assert skoSM!=None
		return lambda skoSP: post_condition(delta=delta, skoX=skoX, skoS2=skoS2, pi=pi, skoSP=skoSP, skoSM=skoSM)

	if skoSM==None:
		assert skoSP!=None
		return lambda skoSM: post_condition(delta=delta, skoX=skoX, skoS2=skoS2, pi=pi, skoSP=skoSP, skoSM=skoSM)


	return post_condition(delta=delta, skoX=skoX, skoS2=skoS2, pi=pi, skoSP=skoSP, skoSM=skoSM)


def get_univariate_poly( delta:sympy.Rational, skoX:sympy.Rational, skoS2:sympy.Rational, pi:sympy.Rational, skoSP:sympy.Rational, skoSM:sympy.Rational ):


	post_cond =  And(LessThan(Integer(0), Symbol('delta')), StrictGreaterThan(Integer(1), Symbol('skoX')), StrictGreaterThan(Rational(31415927, 10000000), Symbol('pi')), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictGreaterThan(Mul(Symbol('skoX'), Add(Mul(Integer(-1), Symbol('skoSM')), Mul(Integer(-1), Symbol('skoSP')), Integer(-4))), Integer(0)), StrictGreaterThan(Mul(Symbol('skoSP'), Add(Mul(Symbol('pi'), Symbol('skoS2')), Mul(Rational(1, 2), Symbol('pi')), Rational(1, 20))), Add(Mul(Symbol('skoSM'), Add(Mul(Symbol('pi'), Symbol('skoS2')), Mul(Rational(1, 2), Symbol('pi')), Rational(-1, 20))), Rational(-1, 5))))

	eval = post_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi, 'skoSP':skoSP, 'skoSM':skoSM })
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
	
	
	ip_0=int(input("enter numerator of pi:\n"))
	ip_1=int(input("enter denominator of pi:\n"))
	assert(ip_1!=0), ("Error denominator entered is 0")
	pi=sympy.Rational(ip_0,ip_1)
	
	
	lambda_var_0 = sympy.symbols('lambda_var_0')
	
	
	if pre_condition_0(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoX'] = skoX
		all_vals['skoS2'] = skoS2
		all_vals['pi'] = pi
		all_vals['skoSP'] = Add(Symbol('lambda_var_0'), Rational(1, 8))
		all_vals['skoSM'] = Integer(-6)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_0 SAT")

			print("skoSP=", all_vals["skoSP"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSM=", all_vals["skoSM"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_1(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoX'] = skoX
		all_vals['skoS2'] = skoS2
		all_vals['pi'] = pi
		all_vals['skoSP'] = Rational(1, 8)
		all_vals['skoSM'] = Add(Symbol('lambda_var_0'), Integer(-6))
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_1 SAT")

			print("skoSP=", all_vals["skoSP"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSM=", all_vals["skoSM"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_2(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoX'] = skoX
		all_vals['skoS2'] = skoS2
		all_vals['pi'] = pi
		all_vals['skoSP'] = Add(Symbol('lambda_var_0'), Integer(-3))
		all_vals['skoSM'] = Rational(-3, 2)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_2 SAT")

			print("skoSP=", all_vals["skoSP"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSM=", all_vals["skoSM"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_3(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoX'] = skoX
		all_vals['skoS2'] = skoS2
		all_vals['pi'] = pi
		all_vals['skoSP'] = Integer(-3)
		all_vals['skoSM'] = Add(Symbol('lambda_var_0'), Rational(-3, 2))
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_3 SAT")

			print("skoSP=", all_vals["skoSP"].subs( { 'lambda_var_0':lambda_val } ))

			print("skoSM=", all_vals["skoSM"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass


	print("Weakest pre-condition UNSAT")
