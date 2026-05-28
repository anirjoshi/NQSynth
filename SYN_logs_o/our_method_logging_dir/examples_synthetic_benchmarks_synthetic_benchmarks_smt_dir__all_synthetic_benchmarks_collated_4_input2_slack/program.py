import sympy
from sympy import *
from NQS.helper_program_cav import get_lambda_val

def pre_condition_0(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + d2 > 0) & (d1 + x > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('d2')), Integer(0)), StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Integer(0)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def post_condition(x:sympy.Rational, d1:sympy.Rational, d2:sympy.Rational, y:sympy.Rational):
	# (0 > -d1 - x + y**2) & (0 > -d2 + x - y**2)

	post_cond =  And(StrictGreaterThan(Integer(0), Add(Mul(Integer(-1), Symbol('d1')), Mul(Integer(-1), Symbol('x')), Pow(Symbol('y'), Integer(2)))), StrictGreaterThan(Integer(0), Add(Mul(Integer(-1), Symbol('d2')), Symbol('x'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))))))

	eval = post_cond.subs( { 'x':x, 'd1':d1, 'd2':d2, 'y':y })

	return eval == sympy.logic.boolalg.BooleanTrue



#return post-condition single variable
def return_post_condition_single_var(post_condition, x:sympy.Rational=None, d1:sympy.Rational=None, d2:sympy.Rational=None, y:sympy.Rational=None):
	assert x!=None
	assert d1!=None
	assert d2!=None


	if y==None:
		return lambda y: post_condition(x=x, d1=d1, d2=d2, y=y)


	return post_condition(x=x, d1=d1, d2=d2, y=y)


def get_univariate_poly( x:sympy.Rational, d1:sympy.Rational, d2:sympy.Rational, y:sympy.Rational ):


	post_cond =  And(StrictGreaterThan(Integer(0), Add(Mul(Integer(-1), Symbol('d1')), Mul(Integer(-1), Symbol('x')), Pow(Symbol('y'), Integer(2)))), StrictGreaterThan(Integer(0), Add(Mul(Integer(-1), Symbol('d2')), Symbol('x'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))))))

	eval = post_cond.subs( { 'x':x, 'd1':d1, 'd2':d2, 'y':y })
	return eval



if __name__=="__main__":
	
	ip_0=int(input("enter numerator of x:\n"))
	ip_1=int(input("enter denominator of x:\n"))
	assert(ip_1!=0), ("Error denominator entered is 0")
	x=sympy.Rational(ip_0,ip_1)
	
	
	ip_0=int(input("enter numerator of d1:\n"))
	ip_1=int(input("enter denominator of d1:\n"))
	assert(ip_1!=0), ("Error denominator entered is 0")
	d1=sympy.Rational(ip_0,ip_1)
	
	
	ip_0=int(input("enter numerator of d2:\n"))
	ip_1=int(input("enter denominator of d2:\n"))
	assert(ip_1!=0), ("Error denominator entered is 0")
	d2=sympy.Rational(ip_0,ip_1)
	
	
	lambda_var_0 = sympy.symbols('lambda_var_0')
	
	
	if pre_condition_0(x=x,d1=d1,d2=d2)==True:
		all_vals = dict()
		all_vals['x'] = x
		all_vals['d1'] = d1
		all_vals['d2'] = d2
		all_vals['y'] = Symbol('lambda_var_0')
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_0 SAT")

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass


	print("Weakest pre-condition UNSAT")
