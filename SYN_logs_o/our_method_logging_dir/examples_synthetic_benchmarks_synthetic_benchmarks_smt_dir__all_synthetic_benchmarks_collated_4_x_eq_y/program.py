import sympy
from sympy import *
from NQS.helper_program_cav import get_lambda_val

def pre_condition_0(y:sympy.Rational):
	#True

	pre_cond = true

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def post_condition(y:sympy.Rational, x:sympy.Rational):
	# (0 >= -x + y) & (0 >= x - y)

	post_cond =  And(GreaterThan(Integer(0), Add(Mul(Integer(-1), Symbol('x')), Symbol('y'))), GreaterThan(Integer(0), Add(Symbol('x'), Mul(Integer(-1), Symbol('y')))))

	eval = post_cond.subs( { 'y':y, 'x':x })

	return eval == sympy.logic.boolalg.BooleanTrue



#return post-condition single variable
def return_post_condition_single_var(post_condition, y:sympy.Rational=None, x:sympy.Rational=None):
	assert y!=None


	if x==None:
		return lambda x: post_condition(y=y, x=x)


	return post_condition(y=y, x=x)


def get_univariate_poly( y:sympy.Rational, x:sympy.Rational ):


	post_cond =  And(GreaterThan(Integer(0), Add(Mul(Integer(-1), Symbol('x')), Symbol('y'))), GreaterThan(Integer(0), Add(Symbol('x'), Mul(Integer(-1), Symbol('y')))))

	eval = post_cond.subs( { 'y':y, 'x':x })
	return eval



if __name__=="__main__":
	
	ip_0=int(input("enter numerator of y:\n"))
	ip_1=int(input("enter denominator of y:\n"))
	assert(ip_1!=0), ("Error denominator entered is 0")
	y=sympy.Rational(ip_0,ip_1)
	
	
	lambda_var_0 = sympy.symbols('lambda_var_0')
	
	
	if pre_condition_0(y=y)==True:
		all_vals = dict()
		all_vals['y'] = y
		all_vals['x'] = Symbol('lambda_var_0')
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_0 SAT")

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass


	print("Weakest pre-condition UNSAT")
