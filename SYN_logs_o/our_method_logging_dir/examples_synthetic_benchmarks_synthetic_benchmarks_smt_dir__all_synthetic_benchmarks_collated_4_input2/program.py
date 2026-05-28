import sympy
from sympy import *
from NQS.helper_program_cav import get_lambda_val

def pre_condition_0(x:sympy.Rational):
	#x >= 0

	pre_cond = GreaterThan(Symbol('x'), Integer(0))

	eval = pre_cond.subs( { 'x':x })

	if eval==True:
		assert eval!=False
		return True
	return False


def post_condition(x:sympy.Rational, y:sympy.Rational):
	# (0 >= -x + y**2) & (0 >= x - y**2)

	post_cond =  And(GreaterThan(Integer(0), Add(Mul(Integer(-1), Symbol('x')), Pow(Symbol('y'), Integer(2)))), GreaterThan(Integer(0), Add(Symbol('x'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))))))

	eval = post_cond.subs( { 'x':x, 'y':y })

	return eval == sympy.logic.boolalg.BooleanTrue



#return post-condition single variable
def return_post_condition_single_var(post_condition, x:sympy.Rational=None, y:sympy.Rational=None):
	assert x!=None


	if y==None:
		return lambda y: post_condition(x=x, y=y)


	return post_condition(x=x, y=y)


def get_univariate_poly( x:sympy.Rational, y:sympy.Rational ):


	post_cond =  And(GreaterThan(Integer(0), Add(Mul(Integer(-1), Symbol('x')), Pow(Symbol('y'), Integer(2)))), GreaterThan(Integer(0), Add(Symbol('x'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))))))

	eval = post_cond.subs( { 'x':x, 'y':y })
	return eval



if __name__=="__main__":
	
	ip_0=int(input("enter numerator of x:\n"))
	ip_1=int(input("enter denominator of x:\n"))
	assert(ip_1!=0), ("Error denominator entered is 0")
	x=sympy.Rational(ip_0,ip_1)
	
	
	lambda_var_0 = sympy.symbols('lambda_var_0')
	
	
	if pre_condition_0(x=x)==True:
		all_vals = dict()
		all_vals['x'] = x
		all_vals['y'] = Add(Symbol('lambda_var_0'), Rational(1, 8))
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_0 SAT")

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass


	print("Weakest pre-condition UNSAT")
