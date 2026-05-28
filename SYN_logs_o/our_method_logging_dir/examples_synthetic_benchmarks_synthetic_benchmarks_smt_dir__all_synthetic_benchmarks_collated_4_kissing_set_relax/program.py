import sympy
from sympy import *
from NQS.helper_program_cav import get_lambda_val

def pre_condition_0(d:sympy.Rational,x_5_0:sympy.Rational,x_5_1:sympy.Rational):
	#(d - 1 > 0) & (-d + x50**2 + x51**2 - 1 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Integer(-1)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('d')), Pow(Symbol('x50'), Integer(2)), Pow(Symbol('x51'), Integer(2)), Integer(-1)), Integer(0)))

	eval = pre_cond.subs( { 'd':d, 'x_5_0':x_5_0, 'x_5_1':x_5_1 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1(d:sympy.Rational,x_5_0:sympy.Rational,x_5_1:sympy.Rational):
	#(d - 1 > 0) & (-d + x50**2 + x51**2 - 1 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Integer(-1)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('d')), Pow(Symbol('x50'), Integer(2)), Pow(Symbol('x51'), Integer(2)), Integer(-1)), Integer(0)))

	eval = pre_cond.subs( { 'd':d, 'x_5_0':x_5_0, 'x_5_1':x_5_1 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_2(d:sympy.Rational,x_5_0:sympy.Rational,x_5_1:sympy.Rational):
	#(d - 1 > 0) & (-d + x50**2 + x51**2 - 1 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Integer(-1)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('d')), Pow(Symbol('x50'), Integer(2)), Pow(Symbol('x51'), Integer(2)), Integer(-1)), Integer(0)))

	eval = pre_cond.subs( { 'd':d, 'x_5_0':x_5_0, 'x_5_1':x_5_1 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_3(d:sympy.Rational,x_5_0:sympy.Rational,x_5_1:sympy.Rational):
	#(d - 1 > 0) & (-d + x50**2 + x51**2 - 1 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Integer(-1)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('d')), Pow(Symbol('x50'), Integer(2)), Pow(Symbol('x51'), Integer(2)), Integer(-1)), Integer(0)))

	eval = pre_cond.subs( { 'd':d, 'x_5_0':x_5_0, 'x_5_1':x_5_1 })

	if eval==True:
		assert eval!=False
		return True
	return False


def post_condition(d:sympy.Rational, x_5_0:sympy.Rational, x_5_1:sympy.Rational, x_0_0:sympy.Rational, x_0_1:sympy.Rational, x_1_0:sympy.Rational, x_1_1:sympy.Rational, x_2_0:sympy.Rational, x_2_1:sympy.Rational, x_3_0:sympy.Rational, x_3_1:sympy.Rational, x_4_0:sympy.Rational, x_4_1:sympy.Rational):
	# (0 > -d) & (0 > -d + x_0_0**2 + x_0_1**2 - 1) & (0 > -d + x_1_0**2 + x_1_1**2 - 1) & (0 > -d + x_2_0**2 + x_2_1**2 - 1) & (0 > -d + x_3_0**2 + x_3_1**2 - 1) & (0 > -d + x_4_0**2 + x_4_1**2 - 1) & (0 > -d + x_5_0**2 + x_5_1**2 - 1) & (0 > -d - x_0_0**2 + 2*x_0_0*x_1_0 - x_0_1**2 + 2*x_0_1*x_1_1 - x_1_0**2 - x_1_1**2 + 1) & (0 > -d - x_0_0**2 + 2*x_0_0*x_2_0 - x_0_1**2 + 2*x_0_1*x_2_1 - x_2_0**2 - x_2_1**2 + 1) & (0 > -d - x_0_0**2 + 2*x_0_0*x_3_0 - x_0_1**2 + 2*x_0_1*x_3_1 - x_3_0**2 - x_3_1**2 + 1) & (0 > -d - x_0_0**2 + 2*x_0_0*x_4_0 - x_0_1**2 + 2*x_0_1*x_4_1 - x_4_0**2 - x_4_1**2 + 1) & (0 > -d - x_0_0**2 + 2*x_0_0*x_5_0 - x_0_1**2 + 2*x_0_1*x_5_1 - x_5_0**2 - x_5_1**2 + 1) & (0 > -d - x_1_0**2 + 2*x_1_0*x_2_0 - x_1_1**2 + 2*x_1_1*x_2_1 - x_2_0**2 - x_2_1**2 + 1) & (0 > -d - x_1_0**2 + 2*x_1_0*x_3_0 - x_1_1**2 + 2*x_1_1*x_3_1 - x_3_0**2 - x_3_1**2 + 1) & (0 > -d - x_1_0**2 + 2*x_1_0*x_4_0 - x_1_1**2 + 2*x_1_1*x_4_1 - x_4_0**2 - x_4_1**2 + 1) & (0 > -d - x_1_0**2 + 2*x_1_0*x_5_0 - x_1_1**2 + 2*x_1_1*x_5_1 - x_5_0**2 - x_5_1**2 + 1) & (0 > -d - x_2_0**2 + 2*x_2_0*x_3_0 - x_2_1**2 + 2*x_2_1*x_3_1 - x_3_0**2 - x_3_1**2 + 1) & (0 > -d - x_2_0**2 + 2*x_2_0*x_4_0 - x_2_1**2 + 2*x_2_1*x_4_1 - x_4_0**2 - x_4_1**2 + 1) & (0 > -d - x_2_0**2 + 2*x_2_0*x_5_0 - x_2_1**2 + 2*x_2_1*x_5_1 - x_5_0**2 - x_5_1**2 + 1) & (0 > -d - x_3_0**2 + 2*x_3_0*x_4_0 - x_3_1**2 + 2*x_3_1*x_4_1 - x_4_0**2 - x_4_1**2 + 1) & (0 > -d - x_3_0**2 + 2*x_3_0*x_5_0 - x_3_1**2 + 2*x_3_1*x_5_1 - x_5_0**2 - x_5_1**2 + 1) & (0 > -d - x_4_0**2 + 2*x_4_0*x_5_0 - x_4_1**2 + 2*x_4_1*x_5_1 - x_5_0**2 - x_5_1**2 + 1)

	post_cond =  And(StrictGreaterThan(Integer(0), Mul(Integer(-1), Symbol('d'))), StrictGreaterThan(Integer(0), Add(Mul(Integer(-1), Symbol('d')), Pow(Symbol('x_0_0'), Integer(2)), Pow(Symbol('x_0_1'), Integer(2)), Integer(-1))), StrictGreaterThan(Integer(0), Add(Mul(Integer(-1), Symbol('d')), Pow(Symbol('x_1_0'), Integer(2)), Pow(Symbol('x_1_1'), Integer(2)), Integer(-1))), StrictGreaterThan(Integer(0), Add(Mul(Integer(-1), Symbol('d')), Pow(Symbol('x_2_0'), Integer(2)), Pow(Symbol('x_2_1'), Integer(2)), Integer(-1))), StrictGreaterThan(Integer(0), Add(Mul(Integer(-1), Symbol('d')), Pow(Symbol('x_3_0'), Integer(2)), Pow(Symbol('x_3_1'), Integer(2)), Integer(-1))), StrictGreaterThan(Integer(0), Add(Mul(Integer(-1), Symbol('d')), Pow(Symbol('x_4_0'), Integer(2)), Pow(Symbol('x_4_1'), Integer(2)), Integer(-1))), StrictGreaterThan(Integer(0), Add(Mul(Integer(-1), Symbol('d')), Pow(Symbol('x_5_0'), Integer(2)), Pow(Symbol('x_5_1'), Integer(2)), Integer(-1))), StrictGreaterThan(Integer(0), Add(Mul(Integer(-1), Symbol('d')), Mul(Integer(-1), Pow(Symbol('x_0_0'), Integer(2))), Mul(Integer(2), Symbol('x_0_0'), Symbol('x_1_0')), Mul(Integer(-1), Pow(Symbol('x_0_1'), Integer(2))), Mul(Integer(2), Symbol('x_0_1'), Symbol('x_1_1')), Mul(Integer(-1), Pow(Symbol('x_1_0'), Integer(2))), Mul(Integer(-1), Pow(Symbol('x_1_1'), Integer(2))), Integer(1))), StrictGreaterThan(Integer(0), Add(Mul(Integer(-1), Symbol('d')), Mul(Integer(-1), Pow(Symbol('x_0_0'), Integer(2))), Mul(Integer(2), Symbol('x_0_0'), Symbol('x_2_0')), Mul(Integer(-1), Pow(Symbol('x_0_1'), Integer(2))), Mul(Integer(2), Symbol('x_0_1'), Symbol('x_2_1')), Mul(Integer(-1), Pow(Symbol('x_2_0'), Integer(2))), Mul(Integer(-1), Pow(Symbol('x_2_1'), Integer(2))), Integer(1))), StrictGreaterThan(Integer(0), Add(Mul(Integer(-1), Symbol('d')), Mul(Integer(-1), Pow(Symbol('x_0_0'), Integer(2))), Mul(Integer(2), Symbol('x_0_0'), Symbol('x_3_0')), Mul(Integer(-1), Pow(Symbol('x_0_1'), Integer(2))), Mul(Integer(2), Symbol('x_0_1'), Symbol('x_3_1')), Mul(Integer(-1), Pow(Symbol('x_3_0'), Integer(2))), Mul(Integer(-1), Pow(Symbol('x_3_1'), Integer(2))), Integer(1))), StrictGreaterThan(Integer(0), Add(Mul(Integer(-1), Symbol('d')), Mul(Integer(-1), Pow(Symbol('x_0_0'), Integer(2))), Mul(Integer(2), Symbol('x_0_0'), Symbol('x_4_0')), Mul(Integer(-1), Pow(Symbol('x_0_1'), Integer(2))), Mul(Integer(2), Symbol('x_0_1'), Symbol('x_4_1')), Mul(Integer(-1), Pow(Symbol('x_4_0'), Integer(2))), Mul(Integer(-1), Pow(Symbol('x_4_1'), Integer(2))), Integer(1))), StrictGreaterThan(Integer(0), Add(Mul(Integer(-1), Symbol('d')), Mul(Integer(-1), Pow(Symbol('x_0_0'), Integer(2))), Mul(Integer(2), Symbol('x_0_0'), Symbol('x_5_0')), Mul(Integer(-1), Pow(Symbol('x_0_1'), Integer(2))), Mul(Integer(2), Symbol('x_0_1'), Symbol('x_5_1')), Mul(Integer(-1), Pow(Symbol('x_5_0'), Integer(2))), Mul(Integer(-1), Pow(Symbol('x_5_1'), Integer(2))), Integer(1))), StrictGreaterThan(Integer(0), Add(Mul(Integer(-1), Symbol('d')), Mul(Integer(-1), Pow(Symbol('x_1_0'), Integer(2))), Mul(Integer(2), Symbol('x_1_0'), Symbol('x_2_0')), Mul(Integer(-1), Pow(Symbol('x_1_1'), Integer(2))), Mul(Integer(2), Symbol('x_1_1'), Symbol('x_2_1')), Mul(Integer(-1), Pow(Symbol('x_2_0'), Integer(2))), Mul(Integer(-1), Pow(Symbol('x_2_1'), Integer(2))), Integer(1))), StrictGreaterThan(Integer(0), Add(Mul(Integer(-1), Symbol('d')), Mul(Integer(-1), Pow(Symbol('x_1_0'), Integer(2))), Mul(Integer(2), Symbol('x_1_0'), Symbol('x_3_0')), Mul(Integer(-1), Pow(Symbol('x_1_1'), Integer(2))), Mul(Integer(2), Symbol('x_1_1'), Symbol('x_3_1')), Mul(Integer(-1), Pow(Symbol('x_3_0'), Integer(2))), Mul(Integer(-1), Pow(Symbol('x_3_1'), Integer(2))), Integer(1))), StrictGreaterThan(Integer(0), Add(Mul(Integer(-1), Symbol('d')), Mul(Integer(-1), Pow(Symbol('x_1_0'), Integer(2))), Mul(Integer(2), Symbol('x_1_0'), Symbol('x_4_0')), Mul(Integer(-1), Pow(Symbol('x_1_1'), Integer(2))), Mul(Integer(2), Symbol('x_1_1'), Symbol('x_4_1')), Mul(Integer(-1), Pow(Symbol('x_4_0'), Integer(2))), Mul(Integer(-1), Pow(Symbol('x_4_1'), Integer(2))), Integer(1))), StrictGreaterThan(Integer(0), Add(Mul(Integer(-1), Symbol('d')), Mul(Integer(-1), Pow(Symbol('x_1_0'), Integer(2))), Mul(Integer(2), Symbol('x_1_0'), Symbol('x_5_0')), Mul(Integer(-1), Pow(Symbol('x_1_1'), Integer(2))), Mul(Integer(2), Symbol('x_1_1'), Symbol('x_5_1')), Mul(Integer(-1), Pow(Symbol('x_5_0'), Integer(2))), Mul(Integer(-1), Pow(Symbol('x_5_1'), Integer(2))), Integer(1))), StrictGreaterThan(Integer(0), Add(Mul(Integer(-1), Symbol('d')), Mul(Integer(-1), Pow(Symbol('x_2_0'), Integer(2))), Mul(Integer(2), Symbol('x_2_0'), Symbol('x_3_0')), Mul(Integer(-1), Pow(Symbol('x_2_1'), Integer(2))), Mul(Integer(2), Symbol('x_2_1'), Symbol('x_3_1')), Mul(Integer(-1), Pow(Symbol('x_3_0'), Integer(2))), Mul(Integer(-1), Pow(Symbol('x_3_1'), Integer(2))), Integer(1))), StrictGreaterThan(Integer(0), Add(Mul(Integer(-1), Symbol('d')), Mul(Integer(-1), Pow(Symbol('x_2_0'), Integer(2))), Mul(Integer(2), Symbol('x_2_0'), Symbol('x_4_0')), Mul(Integer(-1), Pow(Symbol('x_2_1'), Integer(2))), Mul(Integer(2), Symbol('x_2_1'), Symbol('x_4_1')), Mul(Integer(-1), Pow(Symbol('x_4_0'), Integer(2))), Mul(Integer(-1), Pow(Symbol('x_4_1'), Integer(2))), Integer(1))), StrictGreaterThan(Integer(0), Add(Mul(Integer(-1), Symbol('d')), Mul(Integer(-1), Pow(Symbol('x_2_0'), Integer(2))), Mul(Integer(2), Symbol('x_2_0'), Symbol('x_5_0')), Mul(Integer(-1), Pow(Symbol('x_2_1'), Integer(2))), Mul(Integer(2), Symbol('x_2_1'), Symbol('x_5_1')), Mul(Integer(-1), Pow(Symbol('x_5_0'), Integer(2))), Mul(Integer(-1), Pow(Symbol('x_5_1'), Integer(2))), Integer(1))), StrictGreaterThan(Integer(0), Add(Mul(Integer(-1), Symbol('d')), Mul(Integer(-1), Pow(Symbol('x_3_0'), Integer(2))), Mul(Integer(2), Symbol('x_3_0'), Symbol('x_4_0')), Mul(Integer(-1), Pow(Symbol('x_3_1'), Integer(2))), Mul(Integer(2), Symbol('x_3_1'), Symbol('x_4_1')), Mul(Integer(-1), Pow(Symbol('x_4_0'), Integer(2))), Mul(Integer(-1), Pow(Symbol('x_4_1'), Integer(2))), Integer(1))), StrictGreaterThan(Integer(0), Add(Mul(Integer(-1), Symbol('d')), Mul(Integer(-1), Pow(Symbol('x_3_0'), Integer(2))), Mul(Integer(2), Symbol('x_3_0'), Symbol('x_5_0')), Mul(Integer(-1), Pow(Symbol('x_3_1'), Integer(2))), Mul(Integer(2), Symbol('x_3_1'), Symbol('x_5_1')), Mul(Integer(-1), Pow(Symbol('x_5_0'), Integer(2))), Mul(Integer(-1), Pow(Symbol('x_5_1'), Integer(2))), Integer(1))), StrictGreaterThan(Integer(0), Add(Mul(Integer(-1), Symbol('d')), Mul(Integer(-1), Pow(Symbol('x_4_0'), Integer(2))), Mul(Integer(2), Symbol('x_4_0'), Symbol('x_5_0')), Mul(Integer(-1), Pow(Symbol('x_4_1'), Integer(2))), Mul(Integer(2), Symbol('x_4_1'), Symbol('x_5_1')), Mul(Integer(-1), Pow(Symbol('x_5_0'), Integer(2))), Mul(Integer(-1), Pow(Symbol('x_5_1'), Integer(2))), Integer(1))))

	eval = post_cond.subs( { 'd':d, 'x_5_0':x_5_0, 'x_5_1':x_5_1, 'x_0_0':x_0_0, 'x_0_1':x_0_1, 'x_1_0':x_1_0, 'x_1_1':x_1_1, 'x_2_0':x_2_0, 'x_2_1':x_2_1, 'x_3_0':x_3_0, 'x_3_1':x_3_1, 'x_4_0':x_4_0, 'x_4_1':x_4_1 })

	return eval == sympy.logic.boolalg.BooleanTrue



#return post-condition single variable
def return_post_condition_single_var(post_condition, d:sympy.Rational=None, x_5_0:sympy.Rational=None, x_5_1:sympy.Rational=None, x_0_0:sympy.Rational=None, x_0_1:sympy.Rational=None, x_1_0:sympy.Rational=None, x_1_1:sympy.Rational=None, x_2_0:sympy.Rational=None, x_2_1:sympy.Rational=None, x_3_0:sympy.Rational=None, x_3_1:sympy.Rational=None, x_4_0:sympy.Rational=None, x_4_1:sympy.Rational=None):
	assert d!=None
	assert x_5_0!=None
	assert x_5_1!=None


	if x_0_0==None:
		assert x_0_1!=None
		assert x_1_0!=None
		assert x_1_1!=None
		assert x_2_0!=None
		assert x_2_1!=None
		assert x_3_0!=None
		assert x_3_1!=None
		assert x_4_0!=None
		assert x_4_1!=None
		return lambda x_0_0: post_condition(d=d, x_5_0=x_5_0, x_5_1=x_5_1, x_0_0=x_0_0, x_0_1=x_0_1, x_1_0=x_1_0, x_1_1=x_1_1, x_2_0=x_2_0, x_2_1=x_2_1, x_3_0=x_3_0, x_3_1=x_3_1, x_4_0=x_4_0, x_4_1=x_4_1)

	if x_0_1==None:
		assert x_0_0!=None
		assert x_1_0!=None
		assert x_1_1!=None
		assert x_2_0!=None
		assert x_2_1!=None
		assert x_3_0!=None
		assert x_3_1!=None
		assert x_4_0!=None
		assert x_4_1!=None
		return lambda x_0_1: post_condition(d=d, x_5_0=x_5_0, x_5_1=x_5_1, x_0_0=x_0_0, x_0_1=x_0_1, x_1_0=x_1_0, x_1_1=x_1_1, x_2_0=x_2_0, x_2_1=x_2_1, x_3_0=x_3_0, x_3_1=x_3_1, x_4_0=x_4_0, x_4_1=x_4_1)

	if x_1_0==None:
		assert x_0_0!=None
		assert x_0_1!=None
		assert x_1_1!=None
		assert x_2_0!=None
		assert x_2_1!=None
		assert x_3_0!=None
		assert x_3_1!=None
		assert x_4_0!=None
		assert x_4_1!=None
		return lambda x_1_0: post_condition(d=d, x_5_0=x_5_0, x_5_1=x_5_1, x_0_0=x_0_0, x_0_1=x_0_1, x_1_0=x_1_0, x_1_1=x_1_1, x_2_0=x_2_0, x_2_1=x_2_1, x_3_0=x_3_0, x_3_1=x_3_1, x_4_0=x_4_0, x_4_1=x_4_1)

	if x_1_1==None:
		assert x_0_0!=None
		assert x_0_1!=None
		assert x_1_0!=None
		assert x_2_0!=None
		assert x_2_1!=None
		assert x_3_0!=None
		assert x_3_1!=None
		assert x_4_0!=None
		assert x_4_1!=None
		return lambda x_1_1: post_condition(d=d, x_5_0=x_5_0, x_5_1=x_5_1, x_0_0=x_0_0, x_0_1=x_0_1, x_1_0=x_1_0, x_1_1=x_1_1, x_2_0=x_2_0, x_2_1=x_2_1, x_3_0=x_3_0, x_3_1=x_3_1, x_4_0=x_4_0, x_4_1=x_4_1)

	if x_2_0==None:
		assert x_0_0!=None
		assert x_0_1!=None
		assert x_1_0!=None
		assert x_1_1!=None
		assert x_2_1!=None
		assert x_3_0!=None
		assert x_3_1!=None
		assert x_4_0!=None
		assert x_4_1!=None
		return lambda x_2_0: post_condition(d=d, x_5_0=x_5_0, x_5_1=x_5_1, x_0_0=x_0_0, x_0_1=x_0_1, x_1_0=x_1_0, x_1_1=x_1_1, x_2_0=x_2_0, x_2_1=x_2_1, x_3_0=x_3_0, x_3_1=x_3_1, x_4_0=x_4_0, x_4_1=x_4_1)

	if x_2_1==None:
		assert x_0_0!=None
		assert x_0_1!=None
		assert x_1_0!=None
		assert x_1_1!=None
		assert x_2_0!=None
		assert x_3_0!=None
		assert x_3_1!=None
		assert x_4_0!=None
		assert x_4_1!=None
		return lambda x_2_1: post_condition(d=d, x_5_0=x_5_0, x_5_1=x_5_1, x_0_0=x_0_0, x_0_1=x_0_1, x_1_0=x_1_0, x_1_1=x_1_1, x_2_0=x_2_0, x_2_1=x_2_1, x_3_0=x_3_0, x_3_1=x_3_1, x_4_0=x_4_0, x_4_1=x_4_1)

	if x_3_0==None:
		assert x_0_0!=None
		assert x_0_1!=None
		assert x_1_0!=None
		assert x_1_1!=None
		assert x_2_0!=None
		assert x_2_1!=None
		assert x_3_1!=None
		assert x_4_0!=None
		assert x_4_1!=None
		return lambda x_3_0: post_condition(d=d, x_5_0=x_5_0, x_5_1=x_5_1, x_0_0=x_0_0, x_0_1=x_0_1, x_1_0=x_1_0, x_1_1=x_1_1, x_2_0=x_2_0, x_2_1=x_2_1, x_3_0=x_3_0, x_3_1=x_3_1, x_4_0=x_4_0, x_4_1=x_4_1)

	if x_3_1==None:
		assert x_0_0!=None
		assert x_0_1!=None
		assert x_1_0!=None
		assert x_1_1!=None
		assert x_2_0!=None
		assert x_2_1!=None
		assert x_3_0!=None
		assert x_4_0!=None
		assert x_4_1!=None
		return lambda x_3_1: post_condition(d=d, x_5_0=x_5_0, x_5_1=x_5_1, x_0_0=x_0_0, x_0_1=x_0_1, x_1_0=x_1_0, x_1_1=x_1_1, x_2_0=x_2_0, x_2_1=x_2_1, x_3_0=x_3_0, x_3_1=x_3_1, x_4_0=x_4_0, x_4_1=x_4_1)

	if x_4_0==None:
		assert x_0_0!=None
		assert x_0_1!=None
		assert x_1_0!=None
		assert x_1_1!=None
		assert x_2_0!=None
		assert x_2_1!=None
		assert x_3_0!=None
		assert x_3_1!=None
		assert x_4_1!=None
		return lambda x_4_0: post_condition(d=d, x_5_0=x_5_0, x_5_1=x_5_1, x_0_0=x_0_0, x_0_1=x_0_1, x_1_0=x_1_0, x_1_1=x_1_1, x_2_0=x_2_0, x_2_1=x_2_1, x_3_0=x_3_0, x_3_1=x_3_1, x_4_0=x_4_0, x_4_1=x_4_1)

	if x_4_1==None:
		assert x_0_0!=None
		assert x_0_1!=None
		assert x_1_0!=None
		assert x_1_1!=None
		assert x_2_0!=None
		assert x_2_1!=None
		assert x_3_0!=None
		assert x_3_1!=None
		assert x_4_0!=None
		return lambda x_4_1: post_condition(d=d, x_5_0=x_5_0, x_5_1=x_5_1, x_0_0=x_0_0, x_0_1=x_0_1, x_1_0=x_1_0, x_1_1=x_1_1, x_2_0=x_2_0, x_2_1=x_2_1, x_3_0=x_3_0, x_3_1=x_3_1, x_4_0=x_4_0, x_4_1=x_4_1)


	return post_condition(d=d, x_5_0=x_5_0, x_5_1=x_5_1, x_0_0=x_0_0, x_0_1=x_0_1, x_1_0=x_1_0, x_1_1=x_1_1, x_2_0=x_2_0, x_2_1=x_2_1, x_3_0=x_3_0, x_3_1=x_3_1, x_4_0=x_4_0, x_4_1=x_4_1)


def get_univariate_poly( d:sympy.Rational, x_5_0:sympy.Rational, x_5_1:sympy.Rational, x_0_0:sympy.Rational, x_0_1:sympy.Rational, x_1_0:sympy.Rational, x_1_1:sympy.Rational, x_2_0:sympy.Rational, x_2_1:sympy.Rational, x_3_0:sympy.Rational, x_3_1:sympy.Rational, x_4_0:sympy.Rational, x_4_1:sympy.Rational ):


	post_cond =  And(StrictGreaterThan(Integer(0), Mul(Integer(-1), Symbol('d'))), StrictGreaterThan(Integer(0), Add(Mul(Integer(-1), Symbol('d')), Pow(Symbol('x_0_0'), Integer(2)), Pow(Symbol('x_0_1'), Integer(2)), Integer(-1))), StrictGreaterThan(Integer(0), Add(Mul(Integer(-1), Symbol('d')), Pow(Symbol('x_1_0'), Integer(2)), Pow(Symbol('x_1_1'), Integer(2)), Integer(-1))), StrictGreaterThan(Integer(0), Add(Mul(Integer(-1), Symbol('d')), Pow(Symbol('x_2_0'), Integer(2)), Pow(Symbol('x_2_1'), Integer(2)), Integer(-1))), StrictGreaterThan(Integer(0), Add(Mul(Integer(-1), Symbol('d')), Pow(Symbol('x_3_0'), Integer(2)), Pow(Symbol('x_3_1'), Integer(2)), Integer(-1))), StrictGreaterThan(Integer(0), Add(Mul(Integer(-1), Symbol('d')), Pow(Symbol('x_4_0'), Integer(2)), Pow(Symbol('x_4_1'), Integer(2)), Integer(-1))), StrictGreaterThan(Integer(0), Add(Mul(Integer(-1), Symbol('d')), Pow(Symbol('x_5_0'), Integer(2)), Pow(Symbol('x_5_1'), Integer(2)), Integer(-1))), StrictGreaterThan(Integer(0), Add(Mul(Integer(-1), Symbol('d')), Mul(Integer(-1), Pow(Symbol('x_0_0'), Integer(2))), Mul(Integer(2), Symbol('x_0_0'), Symbol('x_1_0')), Mul(Integer(-1), Pow(Symbol('x_0_1'), Integer(2))), Mul(Integer(2), Symbol('x_0_1'), Symbol('x_1_1')), Mul(Integer(-1), Pow(Symbol('x_1_0'), Integer(2))), Mul(Integer(-1), Pow(Symbol('x_1_1'), Integer(2))), Integer(1))), StrictGreaterThan(Integer(0), Add(Mul(Integer(-1), Symbol('d')), Mul(Integer(-1), Pow(Symbol('x_0_0'), Integer(2))), Mul(Integer(2), Symbol('x_0_0'), Symbol('x_2_0')), Mul(Integer(-1), Pow(Symbol('x_0_1'), Integer(2))), Mul(Integer(2), Symbol('x_0_1'), Symbol('x_2_1')), Mul(Integer(-1), Pow(Symbol('x_2_0'), Integer(2))), Mul(Integer(-1), Pow(Symbol('x_2_1'), Integer(2))), Integer(1))), StrictGreaterThan(Integer(0), Add(Mul(Integer(-1), Symbol('d')), Mul(Integer(-1), Pow(Symbol('x_0_0'), Integer(2))), Mul(Integer(2), Symbol('x_0_0'), Symbol('x_3_0')), Mul(Integer(-1), Pow(Symbol('x_0_1'), Integer(2))), Mul(Integer(2), Symbol('x_0_1'), Symbol('x_3_1')), Mul(Integer(-1), Pow(Symbol('x_3_0'), Integer(2))), Mul(Integer(-1), Pow(Symbol('x_3_1'), Integer(2))), Integer(1))), StrictGreaterThan(Integer(0), Add(Mul(Integer(-1), Symbol('d')), Mul(Integer(-1), Pow(Symbol('x_0_0'), Integer(2))), Mul(Integer(2), Symbol('x_0_0'), Symbol('x_4_0')), Mul(Integer(-1), Pow(Symbol('x_0_1'), Integer(2))), Mul(Integer(2), Symbol('x_0_1'), Symbol('x_4_1')), Mul(Integer(-1), Pow(Symbol('x_4_0'), Integer(2))), Mul(Integer(-1), Pow(Symbol('x_4_1'), Integer(2))), Integer(1))), StrictGreaterThan(Integer(0), Add(Mul(Integer(-1), Symbol('d')), Mul(Integer(-1), Pow(Symbol('x_0_0'), Integer(2))), Mul(Integer(2), Symbol('x_0_0'), Symbol('x_5_0')), Mul(Integer(-1), Pow(Symbol('x_0_1'), Integer(2))), Mul(Integer(2), Symbol('x_0_1'), Symbol('x_5_1')), Mul(Integer(-1), Pow(Symbol('x_5_0'), Integer(2))), Mul(Integer(-1), Pow(Symbol('x_5_1'), Integer(2))), Integer(1))), StrictGreaterThan(Integer(0), Add(Mul(Integer(-1), Symbol('d')), Mul(Integer(-1), Pow(Symbol('x_1_0'), Integer(2))), Mul(Integer(2), Symbol('x_1_0'), Symbol('x_2_0')), Mul(Integer(-1), Pow(Symbol('x_1_1'), Integer(2))), Mul(Integer(2), Symbol('x_1_1'), Symbol('x_2_1')), Mul(Integer(-1), Pow(Symbol('x_2_0'), Integer(2))), Mul(Integer(-1), Pow(Symbol('x_2_1'), Integer(2))), Integer(1))), StrictGreaterThan(Integer(0), Add(Mul(Integer(-1), Symbol('d')), Mul(Integer(-1), Pow(Symbol('x_1_0'), Integer(2))), Mul(Integer(2), Symbol('x_1_0'), Symbol('x_3_0')), Mul(Integer(-1), Pow(Symbol('x_1_1'), Integer(2))), Mul(Integer(2), Symbol('x_1_1'), Symbol('x_3_1')), Mul(Integer(-1), Pow(Symbol('x_3_0'), Integer(2))), Mul(Integer(-1), Pow(Symbol('x_3_1'), Integer(2))), Integer(1))), StrictGreaterThan(Integer(0), Add(Mul(Integer(-1), Symbol('d')), Mul(Integer(-1), Pow(Symbol('x_1_0'), Integer(2))), Mul(Integer(2), Symbol('x_1_0'), Symbol('x_4_0')), Mul(Integer(-1), Pow(Symbol('x_1_1'), Integer(2))), Mul(Integer(2), Symbol('x_1_1'), Symbol('x_4_1')), Mul(Integer(-1), Pow(Symbol('x_4_0'), Integer(2))), Mul(Integer(-1), Pow(Symbol('x_4_1'), Integer(2))), Integer(1))), StrictGreaterThan(Integer(0), Add(Mul(Integer(-1), Symbol('d')), Mul(Integer(-1), Pow(Symbol('x_1_0'), Integer(2))), Mul(Integer(2), Symbol('x_1_0'), Symbol('x_5_0')), Mul(Integer(-1), Pow(Symbol('x_1_1'), Integer(2))), Mul(Integer(2), Symbol('x_1_1'), Symbol('x_5_1')), Mul(Integer(-1), Pow(Symbol('x_5_0'), Integer(2))), Mul(Integer(-1), Pow(Symbol('x_5_1'), Integer(2))), Integer(1))), StrictGreaterThan(Integer(0), Add(Mul(Integer(-1), Symbol('d')), Mul(Integer(-1), Pow(Symbol('x_2_0'), Integer(2))), Mul(Integer(2), Symbol('x_2_0'), Symbol('x_3_0')), Mul(Integer(-1), Pow(Symbol('x_2_1'), Integer(2))), Mul(Integer(2), Symbol('x_2_1'), Symbol('x_3_1')), Mul(Integer(-1), Pow(Symbol('x_3_0'), Integer(2))), Mul(Integer(-1), Pow(Symbol('x_3_1'), Integer(2))), Integer(1))), StrictGreaterThan(Integer(0), Add(Mul(Integer(-1), Symbol('d')), Mul(Integer(-1), Pow(Symbol('x_2_0'), Integer(2))), Mul(Integer(2), Symbol('x_2_0'), Symbol('x_4_0')), Mul(Integer(-1), Pow(Symbol('x_2_1'), Integer(2))), Mul(Integer(2), Symbol('x_2_1'), Symbol('x_4_1')), Mul(Integer(-1), Pow(Symbol('x_4_0'), Integer(2))), Mul(Integer(-1), Pow(Symbol('x_4_1'), Integer(2))), Integer(1))), StrictGreaterThan(Integer(0), Add(Mul(Integer(-1), Symbol('d')), Mul(Integer(-1), Pow(Symbol('x_2_0'), Integer(2))), Mul(Integer(2), Symbol('x_2_0'), Symbol('x_5_0')), Mul(Integer(-1), Pow(Symbol('x_2_1'), Integer(2))), Mul(Integer(2), Symbol('x_2_1'), Symbol('x_5_1')), Mul(Integer(-1), Pow(Symbol('x_5_0'), Integer(2))), Mul(Integer(-1), Pow(Symbol('x_5_1'), Integer(2))), Integer(1))), StrictGreaterThan(Integer(0), Add(Mul(Integer(-1), Symbol('d')), Mul(Integer(-1), Pow(Symbol('x_3_0'), Integer(2))), Mul(Integer(2), Symbol('x_3_0'), Symbol('x_4_0')), Mul(Integer(-1), Pow(Symbol('x_3_1'), Integer(2))), Mul(Integer(2), Symbol('x_3_1'), Symbol('x_4_1')), Mul(Integer(-1), Pow(Symbol('x_4_0'), Integer(2))), Mul(Integer(-1), Pow(Symbol('x_4_1'), Integer(2))), Integer(1))), StrictGreaterThan(Integer(0), Add(Mul(Integer(-1), Symbol('d')), Mul(Integer(-1), Pow(Symbol('x_3_0'), Integer(2))), Mul(Integer(2), Symbol('x_3_0'), Symbol('x_5_0')), Mul(Integer(-1), Pow(Symbol('x_3_1'), Integer(2))), Mul(Integer(2), Symbol('x_3_1'), Symbol('x_5_1')), Mul(Integer(-1), Pow(Symbol('x_5_0'), Integer(2))), Mul(Integer(-1), Pow(Symbol('x_5_1'), Integer(2))), Integer(1))), StrictGreaterThan(Integer(0), Add(Mul(Integer(-1), Symbol('d')), Mul(Integer(-1), Pow(Symbol('x_4_0'), Integer(2))), Mul(Integer(2), Symbol('x_4_0'), Symbol('x_5_0')), Mul(Integer(-1), Pow(Symbol('x_4_1'), Integer(2))), Mul(Integer(2), Symbol('x_4_1'), Symbol('x_5_1')), Mul(Integer(-1), Pow(Symbol('x_5_0'), Integer(2))), Mul(Integer(-1), Pow(Symbol('x_5_1'), Integer(2))), Integer(1))))

	eval = post_cond.subs( { 'd':d, 'x_5_0':x_5_0, 'x_5_1':x_5_1, 'x_0_0':x_0_0, 'x_0_1':x_0_1, 'x_1_0':x_1_0, 'x_1_1':x_1_1, 'x_2_0':x_2_0, 'x_2_1':x_2_1, 'x_3_0':x_3_0, 'x_3_1':x_3_1, 'x_4_0':x_4_0, 'x_4_1':x_4_1 })
	return eval



if __name__=="__main__":
	
	ip_0=int(input("enter numerator of d:\n"))
	ip_1=int(input("enter denominator of d:\n"))
	assert(ip_1!=0), ("Error denominator entered is 0")
	d=sympy.Rational(ip_0,ip_1)
	
	
	ip_0=int(input("enter numerator of x_5_0:\n"))
	ip_1=int(input("enter denominator of x_5_0:\n"))
	assert(ip_1!=0), ("Error denominator entered is 0")
	x_5_0=sympy.Rational(ip_0,ip_1)
	
	
	ip_0=int(input("enter numerator of x_5_1:\n"))
	ip_1=int(input("enter denominator of x_5_1:\n"))
	assert(ip_1!=0), ("Error denominator entered is 0")
	x_5_1=sympy.Rational(ip_0,ip_1)
	
	
	lambda_var_0 = sympy.symbols('lambda_var_0')
	
	
	if pre_condition_0(d=d,x_5_0=x_5_0,x_5_1=x_5_1)==True:
		all_vals = dict()
		all_vals['d'] = d
		all_vals['x_5_0'] = x_5_0
		all_vals['x_5_1'] = x_5_1
		all_vals['x_0_0'] = Add(Symbol('lambda_var_0'), Rational(1, 8))
		all_vals['x_0_1'] = Rational(1, 2)
		all_vals['x_1_0'] = Rational(-1, 2)
		all_vals['x_1_1'] = Rational(-1, 2)
		all_vals['x_2_0'] = Integer(1)
		all_vals['x_2_1'] = Integer(-1)
		all_vals['x_3_0'] = Rational(1, 2)
		all_vals['x_3_1'] = Rational(-1, 2)
		all_vals['x_4_0'] = Rational(-1, 2)
		all_vals['x_4_1'] = Integer(-1)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_0 SAT")

			print("x_0_0=", all_vals["x_0_0"].subs( { 'lambda_var_0':lambda_val } ))

			print("x_0_1=", all_vals["x_0_1"].subs( { 'lambda_var_0':lambda_val } ))

			print("x_1_0=", all_vals["x_1_0"].subs( { 'lambda_var_0':lambda_val } ))

			print("x_1_1=", all_vals["x_1_1"].subs( { 'lambda_var_0':lambda_val } ))

			print("x_2_0=", all_vals["x_2_0"].subs( { 'lambda_var_0':lambda_val } ))

			print("x_2_1=", all_vals["x_2_1"].subs( { 'lambda_var_0':lambda_val } ))

			print("x_3_0=", all_vals["x_3_0"].subs( { 'lambda_var_0':lambda_val } ))

			print("x_3_1=", all_vals["x_3_1"].subs( { 'lambda_var_0':lambda_val } ))

			print("x_4_0=", all_vals["x_4_0"].subs( { 'lambda_var_0':lambda_val } ))

			print("x_4_1=", all_vals["x_4_1"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_1(d=d,x_5_0=x_5_0,x_5_1=x_5_1)==True:
		all_vals = dict()
		all_vals['d'] = d
		all_vals['x_5_0'] = x_5_0
		all_vals['x_5_1'] = x_5_1
		all_vals['x_0_0'] = Rational(1, 8)
		all_vals['x_0_1'] = Add(Symbol('lambda_var_0'), Rational(1, 2))
		all_vals['x_1_0'] = Rational(-1, 2)
		all_vals['x_1_1'] = Rational(-1, 2)
		all_vals['x_2_0'] = Integer(1)
		all_vals['x_2_1'] = Integer(-1)
		all_vals['x_3_0'] = Rational(1, 2)
		all_vals['x_3_1'] = Rational(-1, 2)
		all_vals['x_4_0'] = Rational(-1, 2)
		all_vals['x_4_1'] = Integer(-1)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_1 SAT")

			print("x_0_0=", all_vals["x_0_0"].subs( { 'lambda_var_0':lambda_val } ))

			print("x_0_1=", all_vals["x_0_1"].subs( { 'lambda_var_0':lambda_val } ))

			print("x_1_0=", all_vals["x_1_0"].subs( { 'lambda_var_0':lambda_val } ))

			print("x_1_1=", all_vals["x_1_1"].subs( { 'lambda_var_0':lambda_val } ))

			print("x_2_0=", all_vals["x_2_0"].subs( { 'lambda_var_0':lambda_val } ))

			print("x_2_1=", all_vals["x_2_1"].subs( { 'lambda_var_0':lambda_val } ))

			print("x_3_0=", all_vals["x_3_0"].subs( { 'lambda_var_0':lambda_val } ))

			print("x_3_1=", all_vals["x_3_1"].subs( { 'lambda_var_0':lambda_val } ))

			print("x_4_0=", all_vals["x_4_0"].subs( { 'lambda_var_0':lambda_val } ))

			print("x_4_1=", all_vals["x_4_1"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_2(d=d,x_5_0=x_5_0,x_5_1=x_5_1)==True:
		all_vals = dict()
		all_vals['d'] = d
		all_vals['x_5_0'] = x_5_0
		all_vals['x_5_1'] = x_5_1
		all_vals['x_0_0'] = Rational(1, 8)
		all_vals['x_0_1'] = Rational(1, 2)
		all_vals['x_1_0'] = Add(Symbol('lambda_var_0'), Rational(-1, 2))
		all_vals['x_1_1'] = Rational(-1, 2)
		all_vals['x_2_0'] = Integer(1)
		all_vals['x_2_1'] = Integer(-1)
		all_vals['x_3_0'] = Rational(1, 2)
		all_vals['x_3_1'] = Rational(-1, 2)
		all_vals['x_4_0'] = Rational(-1, 2)
		all_vals['x_4_1'] = Integer(-1)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_2 SAT")

			print("x_0_0=", all_vals["x_0_0"].subs( { 'lambda_var_0':lambda_val } ))

			print("x_0_1=", all_vals["x_0_1"].subs( { 'lambda_var_0':lambda_val } ))

			print("x_1_0=", all_vals["x_1_0"].subs( { 'lambda_var_0':lambda_val } ))

			print("x_1_1=", all_vals["x_1_1"].subs( { 'lambda_var_0':lambda_val } ))

			print("x_2_0=", all_vals["x_2_0"].subs( { 'lambda_var_0':lambda_val } ))

			print("x_2_1=", all_vals["x_2_1"].subs( { 'lambda_var_0':lambda_val } ))

			print("x_3_0=", all_vals["x_3_0"].subs( { 'lambda_var_0':lambda_val } ))

			print("x_3_1=", all_vals["x_3_1"].subs( { 'lambda_var_0':lambda_val } ))

			print("x_4_0=", all_vals["x_4_0"].subs( { 'lambda_var_0':lambda_val } ))

			print("x_4_1=", all_vals["x_4_1"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_3(d=d,x_5_0=x_5_0,x_5_1=x_5_1)==True:
		all_vals = dict()
		all_vals['d'] = d
		all_vals['x_5_0'] = x_5_0
		all_vals['x_5_1'] = x_5_1
		all_vals['x_0_0'] = Rational(1, 8)
		all_vals['x_0_1'] = Rational(1, 2)
		all_vals['x_1_0'] = Rational(-1, 2)
		all_vals['x_1_1'] = Add(Symbol('lambda_var_0'), Rational(-1, 2))
		all_vals['x_2_0'] = Integer(1)
		all_vals['x_2_1'] = Integer(-1)
		all_vals['x_3_0'] = Rational(1, 2)
		all_vals['x_3_1'] = Rational(-1, 2)
		all_vals['x_4_0'] = Rational(-1, 2)
		all_vals['x_4_1'] = Integer(-1)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_3 SAT")

			print("x_0_0=", all_vals["x_0_0"].subs( { 'lambda_var_0':lambda_val } ))

			print("x_0_1=", all_vals["x_0_1"].subs( { 'lambda_var_0':lambda_val } ))

			print("x_1_0=", all_vals["x_1_0"].subs( { 'lambda_var_0':lambda_val } ))

			print("x_1_1=", all_vals["x_1_1"].subs( { 'lambda_var_0':lambda_val } ))

			print("x_2_0=", all_vals["x_2_0"].subs( { 'lambda_var_0':lambda_val } ))

			print("x_2_1=", all_vals["x_2_1"].subs( { 'lambda_var_0':lambda_val } ))

			print("x_3_0=", all_vals["x_3_0"].subs( { 'lambda_var_0':lambda_val } ))

			print("x_3_1=", all_vals["x_3_1"].subs( { 'lambda_var_0':lambda_val } ))

			print("x_4_0=", all_vals["x_4_0"].subs( { 'lambda_var_0':lambda_val } ))

			print("x_4_1=", all_vals["x_4_1"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass


	print("UNKNOWN")
