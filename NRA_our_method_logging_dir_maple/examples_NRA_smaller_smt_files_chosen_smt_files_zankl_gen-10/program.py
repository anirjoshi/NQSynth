import sympy
from sympy import *
from NQS.helper_program_cav import get_lambda_val

def pre_condition_0(delta:sympy.Rational):
	#((delta < 2) & (-delta <= 0)) | (Eq(delta - 2, 0) & (-delta <= 0)) | (Eq(delta + 2, 0) & (-delta <= 0)) | ((-delta <= 0) & (-delta < 2)) | ((delta < 2) & (-delta <= 0) & (-delta < 0) & ((delta < 2) | Eq(delta - 2, 0))) | ((-delta <= 0) & (-delta < 2) & ((-delta < 0) | (Eq(delta, 0) & Eq(delta + 2, 0)))) | ((delta < 2) & Eq(delta - 2, 0) & (-delta <= 0) & ((-delta < 0) | (Eq(delta, 0) & (delta < 2))))

	pre_cond = Or(And(StrictLessThan(Symbol('delta'), Integer(2)), LessThan(Mul(Integer(-1), Symbol('delta')), Integer(0))), And(Equality(Add(Symbol('delta'), Integer(-2)), Integer(0)), LessThan(Mul(Integer(-1), Symbol('delta')), Integer(0))), And(Equality(Add(Symbol('delta'), Integer(2)), Integer(0)), LessThan(Mul(Integer(-1), Symbol('delta')), Integer(0))), And(LessThan(Mul(Integer(-1), Symbol('delta')), Integer(0)), StrictLessThan(Mul(Integer(-1), Symbol('delta')), Integer(2))), And(StrictLessThan(Symbol('delta'), Integer(2)), LessThan(Mul(Integer(-1), Symbol('delta')), Integer(0)), StrictLessThan(Mul(Integer(-1), Symbol('delta')), Integer(0)), Or(StrictLessThan(Symbol('delta'), Integer(2)), Equality(Add(Symbol('delta'), Integer(-2)), Integer(0)))), And(LessThan(Mul(Integer(-1), Symbol('delta')), Integer(0)), StrictLessThan(Mul(Integer(-1), Symbol('delta')), Integer(2)), Or(StrictLessThan(Mul(Integer(-1), Symbol('delta')), Integer(0)), And(Equality(Symbol('delta'), Integer(0)), Equality(Add(Symbol('delta'), Integer(2)), Integer(0))))), And(StrictLessThan(Symbol('delta'), Integer(2)), Equality(Add(Symbol('delta'), Integer(-2)), Integer(0)), LessThan(Mul(Integer(-1), Symbol('delta')), Integer(0)), Or(StrictLessThan(Mul(Integer(-1), Symbol('delta')), Integer(0)), And(Equality(Symbol('delta'), Integer(0)), StrictLessThan(Symbol('delta'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def post_condition(delta:sympy.Rational, a:sympy.Rational):
	# (0 <= delta) & (2 - 4*a**2 <= delta) & (4*a**2 - 2 <= delta)

	post_cond =  And(LessThan(Integer(0), Symbol('delta')), LessThan(Add(Integer(2), Mul(Integer(-1), Integer(4), Pow(Symbol('a'), Integer(2)))), Symbol('delta')), LessThan(Add(Mul(Integer(4), Pow(Symbol('a'), Integer(2))), Integer(-2)), Symbol('delta')))

	eval = post_cond.subs( { 'delta':delta, 'a':a })

	return eval == sympy.logic.boolalg.BooleanTrue



#return post-condition single variable
def return_post_condition_single_var(post_condition, delta:sympy.Rational=None, a:sympy.Rational=None):
	assert delta!=None


	if a==None:
		return lambda a: post_condition(delta=delta, a=a)


	return post_condition(delta=delta, a=a)


def get_univariate_poly( delta:sympy.Rational, a:sympy.Rational ):


	post_cond =  And(LessThan(Integer(0), Symbol('delta')), LessThan(Add(Integer(2), Mul(Integer(-1), Integer(4), Pow(Symbol('a'), Integer(2)))), Symbol('delta')), LessThan(Add(Mul(Integer(4), Pow(Symbol('a'), Integer(2))), Integer(-2)), Symbol('delta')))

	eval = post_cond.subs( { 'delta':delta, 'a':a })
	return eval



if __name__=="__main__":
	
	ip_0=int(input("enter numerator of delta:\n"))
	ip_1=int(input("enter denominator of delta:\n"))
	assert(ip_1!=0), ("Error denominator entered is 0")
	delta=sympy.Rational(ip_0,ip_1)
	
	
	lambda_var_0 = sympy.symbols('lambda_var_0')
	
	
	if pre_condition_0(delta=delta)==True:
		all_vals = dict()
		all_vals['delta'] = delta
		all_vals['a'] = Add(Symbol('lambda_var_0'), Rational(1, 8))
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_0 SAT")

			print("a=", all_vals["a"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass


	print("Weakest pre-condition UNSAT")
