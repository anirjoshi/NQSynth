import sympy
from sympy import *
from NQS.helper_program_cav import get_lambda_val

def pre_condition_0(delta:sympy.Rational,skoX:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoX > 0) & (skoX - 1 < 0) & (5000000*pi - 15707963 > 0) & (10000000*pi - 31415927 < 0)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Add(Symbol('skoX'), Integer(-1)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(5000000), Symbol('pi')), Integer(-15707963)), Integer(0)), StrictLessThan(Add(Mul(Integer(10000000), Symbol('pi')), Integer(-31415927)), Integer(0)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def post_condition(delta:sympy.Rational, skoX:sympy.Rational, pi:sympy.Rational, skoSM:sympy.Rational):
	# (0 <= delta) & (1 > skoX) & (31415927/10000000 > pi) & (pi > 15707963/5000000) & (skoX > 0) & ~((skoSM**2 + skoX - 1 <= delta) & (-skoSM**2 - skoX + 1 <= delta))

	post_cond =  And(LessThan(Integer(0), Symbol('delta')), StrictGreaterThan(Integer(1), Symbol('skoX')), StrictGreaterThan(Rational(31415927, 10000000), Symbol('pi')), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), Not(And(LessThan(Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1)), Symbol('delta')), LessThan(Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1)), Symbol('delta')))))

	eval = post_cond.subs( { 'delta':delta, 'skoX':skoX, 'pi':pi, 'skoSM':skoSM })

	return eval == sympy.logic.boolalg.BooleanTrue



#return post-condition single variable
def return_post_condition_single_var(post_condition, delta:sympy.Rational=None, skoX:sympy.Rational=None, pi:sympy.Rational=None, skoSM:sympy.Rational=None):
	assert delta!=None
	assert skoX!=None
	assert pi!=None


	if skoSM==None:
		return lambda skoSM: post_condition(delta=delta, skoX=skoX, pi=pi, skoSM=skoSM)


	return post_condition(delta=delta, skoX=skoX, pi=pi, skoSM=skoSM)


def get_univariate_poly( delta:sympy.Rational, skoX:sympy.Rational, pi:sympy.Rational, skoSM:sympy.Rational ):


	post_cond =  And(LessThan(Integer(0), Symbol('delta')), StrictGreaterThan(Integer(1), Symbol('skoX')), StrictGreaterThan(Rational(31415927, 10000000), Symbol('pi')), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), Not(And(LessThan(Add(Pow(Symbol('skoSM'), Integer(2)), Symbol('skoX'), Integer(-1)), Symbol('delta')), LessThan(Add(Mul(Integer(-1), Pow(Symbol('skoSM'), Integer(2))), Mul(Integer(-1), Symbol('skoX')), Integer(1)), Symbol('delta')))))

	eval = post_cond.subs( { 'delta':delta, 'skoX':skoX, 'pi':pi, 'skoSM':skoSM })
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
	
	
	ip_0=int(input("enter numerator of pi:\n"))
	ip_1=int(input("enter denominator of pi:\n"))
	assert(ip_1!=0), ("Error denominator entered is 0")
	pi=sympy.Rational(ip_0,ip_1)
	
	
	lambda_var_0 = sympy.symbols('lambda_var_0')
	
	
	if pre_condition_0(delta=delta,skoX=skoX,pi=pi)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['skoX'] = skoX
		all_vals['pi'] = pi
		all_vals['skoSM'] = Add(Symbol('lambda_var_0'), Rational(1, 8))
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_0 SAT")

			print("skoSM=", all_vals["skoSM"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass


	print("Weakest pre-condition UNSAT")
