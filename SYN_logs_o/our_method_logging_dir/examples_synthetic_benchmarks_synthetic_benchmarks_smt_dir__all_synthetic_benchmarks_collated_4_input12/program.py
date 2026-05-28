import sympy
from sympy import *
from NQS.helper_program_cav import get_lambda_val

def pre_condition_0(x:sympy.Rational):
	#(x**3 + 2*x**2 + 2*x + 2 >= 0) & ((x - 1 < 0) | (x**12 - x**11 + x**10 - x**9 - 5*x**8 + 3*x**7 - x**6 + 14*x**4 - 8*x**3 - 4 <= 0))

	pre_cond = And(GreaterThan(Add(Pow(Symbol('x'), Integer(3)), Mul(Integer(2), Pow(Symbol('x'), Integer(2))), Mul(Integer(2), Symbol('x')), Integer(2)), Integer(0)), Or(StrictLessThan(Add(Symbol('x'), Integer(-1)), Integer(0)), LessThan(Add(Pow(Symbol('x'), Integer(12)), Mul(Integer(-1), Pow(Symbol('x'), Integer(11))), Pow(Symbol('x'), Integer(10)), Mul(Integer(-1), Pow(Symbol('x'), Integer(9))), Mul(Integer(-1), Integer(5), Pow(Symbol('x'), Integer(8))), Mul(Integer(3), Pow(Symbol('x'), Integer(7))), Mul(Integer(-1), Pow(Symbol('x'), Integer(6))), Mul(Integer(14), Pow(Symbol('x'), Integer(4))), Mul(Integer(-1), Integer(8), Pow(Symbol('x'), Integer(3))), Integer(-4)), Integer(0))))

	eval = pre_cond.subs( { 'x':x })

	if eval==True:
		assert eval!=False
		return True
	return False


def post_condition(x:sympy.Rational, y:sympy.Rational):
	# (0 >= x**2 + y**2 - 8) & (0 >= x**3 + y**4 - 2) & (0 >= x**4 + y**3 - 2)

	post_cond =  And(GreaterThan(Integer(0), Add(Pow(Symbol('x'), Integer(2)), Pow(Symbol('y'), Integer(2)), Integer(-8))), GreaterThan(Integer(0), Add(Pow(Symbol('x'), Integer(3)), Pow(Symbol('y'), Integer(4)), Integer(-2))), GreaterThan(Integer(0), Add(Pow(Symbol('x'), Integer(4)), Pow(Symbol('y'), Integer(3)), Integer(-2))))

	eval = post_cond.subs( { 'x':x, 'y':y })

	return eval == sympy.logic.boolalg.BooleanTrue



#return post-condition single variable
def return_post_condition_single_var(post_condition, x:sympy.Rational=None, y:sympy.Rational=None):
	assert x!=None


	if y==None:
		return lambda y: post_condition(x=x, y=y)


	return post_condition(x=x, y=y)


def get_univariate_poly( x:sympy.Rational, y:sympy.Rational ):


	post_cond =  And(GreaterThan(Integer(0), Add(Pow(Symbol('x'), Integer(2)), Pow(Symbol('y'), Integer(2)), Integer(-8))), GreaterThan(Integer(0), Add(Pow(Symbol('x'), Integer(3)), Pow(Symbol('y'), Integer(4)), Integer(-2))), GreaterThan(Integer(0), Add(Pow(Symbol('x'), Integer(4)), Pow(Symbol('y'), Integer(3)), Integer(-2))))

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
		all_vals['y'] = Add(Symbol('lambda_var_0'), Integer(-1))
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_0 SAT")

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass


	print("Weakest pre-condition UNSAT")
