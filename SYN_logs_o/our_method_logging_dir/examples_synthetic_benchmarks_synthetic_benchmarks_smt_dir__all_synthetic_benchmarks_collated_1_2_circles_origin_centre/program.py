import sympy
from sympy import *
from NQS.helper_program_cav import get_lambda_val

def pre_condition_0(r1:sympy.Rational,r2:sympy.Rational):
	#Ne(2*r1 - 1, 0) & Ne(2*r1 + 1, 0) & (((r1 + r2 > 0) & (2*r1 - 1 > 0) & (-r1 + r2 < 0)) | ((r1 + r2 < 0) & (-r1 + r2 > 0) & (2*r1 + 1 < 0)))

	pre_cond = And(Unequality(Add(Mul(Integer(2), Symbol('r1')), Integer(-1)), Integer(0)), Unequality(Add(Mul(Integer(2), Symbol('r1')), Integer(1)), Integer(0)), Or(And(StrictGreaterThan(Add(Symbol('r1'), Symbol('r2')), Integer(0)), StrictGreaterThan(Add(Mul(Integer(2), Symbol('r1')), Integer(-1)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Symbol('r2')), Integer(0))), And(StrictLessThan(Add(Symbol('r1'), Symbol('r2')), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r1')), Symbol('r2')), Integer(0)), StrictLessThan(Add(Mul(Integer(2), Symbol('r1')), Integer(1)), Integer(0)))))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1(r1:sympy.Rational,r2:sympy.Rational):
	#Ne(8*r1 - 1, 0) & Ne(8*r1 + 1, 0) & (((r1 + r2 > 0) & (8*r1 - 1 > 0) & (-r1 + r2 < 0)) | ((r1 + r2 < 0) & (-r1 + r2 > 0) & (8*r1 + 1 < 0)))

	pre_cond = And(Unequality(Add(Mul(Integer(8), Symbol('r1')), Integer(-1)), Integer(0)), Unequality(Add(Mul(Integer(8), Symbol('r1')), Integer(1)), Integer(0)), Or(And(StrictGreaterThan(Add(Symbol('r1'), Symbol('r2')), Integer(0)), StrictGreaterThan(Add(Mul(Integer(8), Symbol('r1')), Integer(-1)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Symbol('r2')), Integer(0))), And(StrictLessThan(Add(Symbol('r1'), Symbol('r2')), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r1')), Symbol('r2')), Integer(0)), StrictLessThan(Add(Mul(Integer(8), Symbol('r1')), Integer(1)), Integer(0)))))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_2(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 + r2 > 0) & (r1 + r2 < 0) & (-r1 + r2 > 0) & (-r1 + r2 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('r1'), Symbol('r2')), Integer(0)), StrictLessThan(Add(Symbol('r1'), Symbol('r2')), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r1')), Symbol('r2')), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Symbol('r2')), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_3(r1:sympy.Rational,r2:sympy.Rational):
	#Ne(32*r1 - 1, 0) & Ne(32*r1 + 1, 0) & (((r1 + r2 > 0) & (32*r1 - 1 > 0) & (-r1 + r2 < 0)) | ((r1 + r2 < 0) & (-r1 + r2 > 0) & (32*r1 + 1 < 0)))

	pre_cond = And(Unequality(Add(Mul(Integer(32), Symbol('r1')), Integer(-1)), Integer(0)), Unequality(Add(Mul(Integer(32), Symbol('r1')), Integer(1)), Integer(0)), Or(And(StrictGreaterThan(Add(Symbol('r1'), Symbol('r2')), Integer(0)), StrictGreaterThan(Add(Mul(Integer(32), Symbol('r1')), Integer(-1)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Symbol('r2')), Integer(0))), And(StrictLessThan(Add(Symbol('r1'), Symbol('r2')), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r1')), Symbol('r2')), Integer(0)), StrictLessThan(Add(Mul(Integer(32), Symbol('r1')), Integer(1)), Integer(0)))))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_4(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 + r2 > 0) & (r1 + r2 < 0) & (-r1 + r2 > 0) & (-r1 + r2 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('r1'), Symbol('r2')), Integer(0)), StrictLessThan(Add(Symbol('r1'), Symbol('r2')), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r1')), Symbol('r2')), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Symbol('r2')), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_5(r1:sympy.Rational,r2:sympy.Rational):
	#Ne(64*r1 - 1, 0) & Ne(64*r1 + 1, 0) & (((r1 + r2 > 0) & (64*r1 - 1 > 0) & (-r1 + r2 < 0)) | ((r1 + r2 < 0) & (-r1 + r2 > 0) & (64*r1 + 1 < 0)))

	pre_cond = And(Unequality(Add(Mul(Integer(64), Symbol('r1')), Integer(-1)), Integer(0)), Unequality(Add(Mul(Integer(64), Symbol('r1')), Integer(1)), Integer(0)), Or(And(StrictGreaterThan(Add(Symbol('r1'), Symbol('r2')), Integer(0)), StrictGreaterThan(Add(Mul(Integer(64), Symbol('r1')), Integer(-1)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Symbol('r2')), Integer(0))), And(StrictLessThan(Add(Symbol('r1'), Symbol('r2')), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r1')), Symbol('r2')), Integer(0)), StrictLessThan(Add(Mul(Integer(64), Symbol('r1')), Integer(1)), Integer(0)))))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_6(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 + r2 > 0) & (r1 + r2 < 0) & (-r1 + r2 > 0) & (-r1 + r2 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('r1'), Symbol('r2')), Integer(0)), StrictLessThan(Add(Symbol('r1'), Symbol('r2')), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r1')), Symbol('r2')), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Symbol('r2')), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_7(r1:sympy.Rational,r2:sympy.Rational):
	#Ne(256*r1 - 1, 0) & Ne(256*r1 + 1, 0) & (((r1 + r2 > 0) & (256*r1 - 1 > 0) & (-r1 + r2 < 0)) | ((r1 + r2 < 0) & (-r1 + r2 > 0) & (256*r1 + 1 < 0)))

	pre_cond = And(Unequality(Add(Mul(Integer(256), Symbol('r1')), Integer(-1)), Integer(0)), Unequality(Add(Mul(Integer(256), Symbol('r1')), Integer(1)), Integer(0)), Or(And(StrictGreaterThan(Add(Symbol('r1'), Symbol('r2')), Integer(0)), StrictGreaterThan(Add(Mul(Integer(256), Symbol('r1')), Integer(-1)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Symbol('r2')), Integer(0))), And(StrictLessThan(Add(Symbol('r1'), Symbol('r2')), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r1')), Symbol('r2')), Integer(0)), StrictLessThan(Add(Mul(Integer(256), Symbol('r1')), Integer(1)), Integer(0)))))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_8(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 + r2 > 0) & (r1 + r2 < 0) & (-r1 + r2 > 0) & (-r1 + r2 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('r1'), Symbol('r2')), Integer(0)), StrictLessThan(Add(Symbol('r1'), Symbol('r2')), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r1')), Symbol('r2')), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Symbol('r2')), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_9(r1:sympy.Rational,r2:sympy.Rational):
	#Ne(1024*r1 - 1, 0) & Ne(1024*r1 + 1, 0) & (((r1 + r2 > 0) & (1024*r1 - 1 > 0) & (-r1 + r2 < 0)) | ((r1 + r2 < 0) & (-r1 + r2 > 0) & (1024*r1 + 1 < 0)))

	pre_cond = And(Unequality(Add(Mul(Integer(1024), Symbol('r1')), Integer(-1)), Integer(0)), Unequality(Add(Mul(Integer(1024), Symbol('r1')), Integer(1)), Integer(0)), Or(And(StrictGreaterThan(Add(Symbol('r1'), Symbol('r2')), Integer(0)), StrictGreaterThan(Add(Mul(Integer(1024), Symbol('r1')), Integer(-1)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Symbol('r2')), Integer(0))), And(StrictLessThan(Add(Symbol('r1'), Symbol('r2')), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r1')), Symbol('r2')), Integer(0)), StrictLessThan(Add(Mul(Integer(1024), Symbol('r1')), Integer(1)), Integer(0)))))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_10(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 + r2 > 0) & (r1 + r2 < 0) & (-r1 + r2 > 0) & (-r1 + r2 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('r1'), Symbol('r2')), Integer(0)), StrictLessThan(Add(Symbol('r1'), Symbol('r2')), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r1')), Symbol('r2')), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Symbol('r2')), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_11(r1:sympy.Rational,r2:sympy.Rational):
	#Ne(4096*r1 - 1, 0) & Ne(4096*r1 + 1, 0) & (((r1 + r2 > 0) & (4096*r1 - 1 > 0) & (-r1 + r2 < 0)) | ((r1 + r2 < 0) & (-r1 + r2 > 0) & (4096*r1 + 1 < 0)))

	pre_cond = And(Unequality(Add(Mul(Integer(4096), Symbol('r1')), Integer(-1)), Integer(0)), Unequality(Add(Mul(Integer(4096), Symbol('r1')), Integer(1)), Integer(0)), Or(And(StrictGreaterThan(Add(Symbol('r1'), Symbol('r2')), Integer(0)), StrictGreaterThan(Add(Mul(Integer(4096), Symbol('r1')), Integer(-1)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Symbol('r2')), Integer(0))), And(StrictLessThan(Add(Symbol('r1'), Symbol('r2')), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r1')), Symbol('r2')), Integer(0)), StrictLessThan(Add(Mul(Integer(4096), Symbol('r1')), Integer(1)), Integer(0)))))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_12(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 + r2 > 0) & (r1 + r2 < 0) & (-r1 + r2 > 0) & (-r1 + r2 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('r1'), Symbol('r2')), Integer(0)), StrictLessThan(Add(Symbol('r1'), Symbol('r2')), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r1')), Symbol('r2')), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Symbol('r2')), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_13(r1:sympy.Rational,r2:sympy.Rational):
	#Ne(16384*r1 - 1, 0) & Ne(16384*r1 + 1, 0) & (((r1 + r2 > 0) & (16384*r1 - 1 > 0) & (-r1 + r2 < 0)) | ((r1 + r2 < 0) & (-r1 + r2 > 0) & (16384*r1 + 1 < 0)))

	pre_cond = And(Unequality(Add(Mul(Integer(16384), Symbol('r1')), Integer(-1)), Integer(0)), Unequality(Add(Mul(Integer(16384), Symbol('r1')), Integer(1)), Integer(0)), Or(And(StrictGreaterThan(Add(Symbol('r1'), Symbol('r2')), Integer(0)), StrictGreaterThan(Add(Mul(Integer(16384), Symbol('r1')), Integer(-1)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Symbol('r2')), Integer(0))), And(StrictLessThan(Add(Symbol('r1'), Symbol('r2')), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r1')), Symbol('r2')), Integer(0)), StrictLessThan(Add(Mul(Integer(16384), Symbol('r1')), Integer(1)), Integer(0)))))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_14(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 + r2 > 0) & (r1 + r2 < 0) & (-r1 + r2 > 0) & (-r1 + r2 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('r1'), Symbol('r2')), Integer(0)), StrictLessThan(Add(Symbol('r1'), Symbol('r2')), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r1')), Symbol('r2')), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Symbol('r2')), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_15(r1:sympy.Rational,r2:sympy.Rational):
	#Ne(65536*r1 - 1, 0) & Ne(65536*r1 + 1, 0) & (((r1 + r2 > 0) & (65536*r1 - 1 > 0) & (-r1 + r2 < 0)) | ((r1 + r2 < 0) & (-r1 + r2 > 0) & (65536*r1 + 1 < 0)))

	pre_cond = And(Unequality(Add(Mul(Integer(65536), Symbol('r1')), Integer(-1)), Integer(0)), Unequality(Add(Mul(Integer(65536), Symbol('r1')), Integer(1)), Integer(0)), Or(And(StrictGreaterThan(Add(Symbol('r1'), Symbol('r2')), Integer(0)), StrictGreaterThan(Add(Mul(Integer(65536), Symbol('r1')), Integer(-1)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Symbol('r2')), Integer(0))), And(StrictLessThan(Add(Symbol('r1'), Symbol('r2')), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r1')), Symbol('r2')), Integer(0)), StrictLessThan(Add(Mul(Integer(65536), Symbol('r1')), Integer(1)), Integer(0)))))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_16(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 + r2 > 0) & (r1 + r2 < 0) & (-r1 + r2 > 0) & (-r1 + r2 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('r1'), Symbol('r2')), Integer(0)), StrictLessThan(Add(Symbol('r1'), Symbol('r2')), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r1')), Symbol('r2')), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Symbol('r2')), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_17(r1:sympy.Rational,r2:sympy.Rational):
	#Ne(262144*r1 - 1, 0) & Ne(262144*r1 + 1, 0) & (((r1 + r2 > 0) & (262144*r1 - 1 > 0) & (-r1 + r2 < 0)) | ((r1 + r2 < 0) & (-r1 + r2 > 0) & (262144*r1 + 1 < 0)))

	pre_cond = And(Unequality(Add(Mul(Integer(262144), Symbol('r1')), Integer(-1)), Integer(0)), Unequality(Add(Mul(Integer(262144), Symbol('r1')), Integer(1)), Integer(0)), Or(And(StrictGreaterThan(Add(Symbol('r1'), Symbol('r2')), Integer(0)), StrictGreaterThan(Add(Mul(Integer(262144), Symbol('r1')), Integer(-1)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Symbol('r2')), Integer(0))), And(StrictLessThan(Add(Symbol('r1'), Symbol('r2')), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r1')), Symbol('r2')), Integer(0)), StrictLessThan(Add(Mul(Integer(262144), Symbol('r1')), Integer(1)), Integer(0)))))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_18(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 + r2 > 0) & (r1 + r2 < 0) & (-r1 + r2 > 0) & (-r1 + r2 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('r1'), Symbol('r2')), Integer(0)), StrictLessThan(Add(Symbol('r1'), Symbol('r2')), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r1')), Symbol('r2')), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Symbol('r2')), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_19(r1:sympy.Rational,r2:sympy.Rational):
	#Ne(1048576*r1 - 1, 0) & Ne(1048576*r1 + 1, 0) & (((r1 + r2 > 0) & (1048576*r1 - 1 > 0) & (-r1 + r2 < 0)) | ((r1 + r2 < 0) & (-r1 + r2 > 0) & (1048576*r1 + 1 < 0)))

	pre_cond = And(Unequality(Add(Mul(Integer(1048576), Symbol('r1')), Integer(-1)), Integer(0)), Unequality(Add(Mul(Integer(1048576), Symbol('r1')), Integer(1)), Integer(0)), Or(And(StrictGreaterThan(Add(Symbol('r1'), Symbol('r2')), Integer(0)), StrictGreaterThan(Add(Mul(Integer(1048576), Symbol('r1')), Integer(-1)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Symbol('r2')), Integer(0))), And(StrictLessThan(Add(Symbol('r1'), Symbol('r2')), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r1')), Symbol('r2')), Integer(0)), StrictLessThan(Add(Mul(Integer(1048576), Symbol('r1')), Integer(1)), Integer(0)))))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_20(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 + r2 > 0) & (r1 + r2 < 0) & (-r1 + r2 > 0) & (-r1 + r2 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('r1'), Symbol('r2')), Integer(0)), StrictLessThan(Add(Symbol('r1'), Symbol('r2')), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r1')), Symbol('r2')), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Symbol('r2')), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_21(r1:sympy.Rational,r2:sympy.Rational):
	#Ne(4194304*r1 - 1, 0) & Ne(4194304*r1 + 1, 0) & (((r1 + r2 > 0) & (4194304*r1 - 1 > 0) & (-r1 + r2 < 0)) | ((r1 + r2 < 0) & (-r1 + r2 > 0) & (4194304*r1 + 1 < 0)))

	pre_cond = And(Unequality(Add(Mul(Integer(4194304), Symbol('r1')), Integer(-1)), Integer(0)), Unequality(Add(Mul(Integer(4194304), Symbol('r1')), Integer(1)), Integer(0)), Or(And(StrictGreaterThan(Add(Symbol('r1'), Symbol('r2')), Integer(0)), StrictGreaterThan(Add(Mul(Integer(4194304), Symbol('r1')), Integer(-1)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Symbol('r2')), Integer(0))), And(StrictLessThan(Add(Symbol('r1'), Symbol('r2')), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r1')), Symbol('r2')), Integer(0)), StrictLessThan(Add(Mul(Integer(4194304), Symbol('r1')), Integer(1)), Integer(0)))))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_22(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 + r2 > 0) & (r1 + r2 < 0) & (-r1 + r2 > 0) & (-r1 + r2 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('r1'), Symbol('r2')), Integer(0)), StrictLessThan(Add(Symbol('r1'), Symbol('r2')), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r1')), Symbol('r2')), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Symbol('r2')), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def post_condition(r1:sympy.Rational, r2:sympy.Rational, x:sympy.Rational, y:sympy.Rational):
	# (0 > -r1**2 + x**2 + y**2) & (0 > r2**2 - x**2 - y**2)

	post_cond =  And(StrictGreaterThan(Integer(0), Add(Mul(Integer(-1), Pow(Symbol('r1'), Integer(2))), Pow(Symbol('x'), Integer(2)), Pow(Symbol('y'), Integer(2)))), StrictGreaterThan(Integer(0), Add(Pow(Symbol('r2'), Integer(2)), Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))))))

	eval = post_cond.subs( { 'r1':r1, 'r2':r2, 'x':x, 'y':y })

	return eval == sympy.logic.boolalg.BooleanTrue



#return post-condition single variable
def return_post_condition_single_var(post_condition, r1:sympy.Rational=None, r2:sympy.Rational=None, x:sympy.Rational=None, y:sympy.Rational=None):
	assert r1!=None
	assert r2!=None


	if x==None:
		assert y!=None
		return lambda x: post_condition(r1=r1, r2=r2, x=x, y=y)

	if y==None:
		assert x!=None
		return lambda y: post_condition(r1=r1, r2=r2, x=x, y=y)


	return post_condition(r1=r1, r2=r2, x=x, y=y)


def get_univariate_poly( r1:sympy.Rational, r2:sympy.Rational, x:sympy.Rational, y:sympy.Rational ):


	post_cond =  And(StrictGreaterThan(Integer(0), Add(Mul(Integer(-1), Pow(Symbol('r1'), Integer(2))), Pow(Symbol('x'), Integer(2)), Pow(Symbol('y'), Integer(2)))), StrictGreaterThan(Integer(0), Add(Pow(Symbol('r2'), Integer(2)), Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))))))

	eval = post_cond.subs( { 'r1':r1, 'r2':r2, 'x':x, 'y':y })
	return eval



if __name__=="__main__":
	
	ip_0=int(input("enter numerator of r1:\n"))
	ip_1=int(input("enter denominator of r1:\n"))
	assert(ip_1!=0), ("Error denominator entered is 0")
	r1=sympy.Rational(ip_0,ip_1)
	
	
	ip_0=int(input("enter numerator of r2:\n"))
	ip_1=int(input("enter denominator of r2:\n"))
	assert(ip_1!=0), ("Error denominator entered is 0")
	r2=sympy.Rational(ip_0,ip_1)
	
	
	lambda_var_0 = sympy.symbols('lambda_var_0')
	
	
	if pre_condition_0(r1=r1,r2=r2)==True:
		all_vals = dict()
		all_vals['r1'] = r1
		all_vals['r2'] = r2
		all_vals['x'] = Add(Symbol('lambda_var_0'), Rational(1, 8))
		all_vals['y'] = Rational(1, 2)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_0 SAT")

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_1(r1=r1,r2=r2)==True:
		all_vals = dict()
		all_vals['r1'] = r1
		all_vals['r2'] = r2
		all_vals['x'] = Rational(1, 8)
		all_vals['y'] = Add(Symbol('lambda_var_0'), Rational(1, 2))
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_1 SAT")

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_2(r1=r1,r2=r2)==True:
		all_vals = dict()
		all_vals['r1'] = r1
		all_vals['r2'] = r2
		all_vals['x'] = Add(Symbol('lambda_var_0'), Rational(-1, 32))
		all_vals['y'] = Integer(0)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_2 SAT")

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_3(r1=r1,r2=r2)==True:
		all_vals = dict()
		all_vals['r1'] = r1
		all_vals['r2'] = r2
		all_vals['x'] = Rational(-1, 32)
		all_vals['y'] = Symbol('lambda_var_0')
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_3 SAT")

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_4(r1=r1,r2=r2)==True:
		all_vals = dict()
		all_vals['r1'] = r1
		all_vals['r2'] = r2
		all_vals['x'] = Add(Symbol('lambda_var_0'), Rational(-1, 64))
		all_vals['y'] = Integer(0)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_4 SAT")

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_5(r1=r1,r2=r2)==True:
		all_vals = dict()
		all_vals['r1'] = r1
		all_vals['r2'] = r2
		all_vals['x'] = Rational(-1, 64)
		all_vals['y'] = Symbol('lambda_var_0')
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_5 SAT")

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_6(r1=r1,r2=r2)==True:
		all_vals = dict()
		all_vals['r1'] = r1
		all_vals['r2'] = r2
		all_vals['x'] = Add(Symbol('lambda_var_0'), Rational(-1, 256))
		all_vals['y'] = Integer(0)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_6 SAT")

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_7(r1=r1,r2=r2)==True:
		all_vals = dict()
		all_vals['r1'] = r1
		all_vals['r2'] = r2
		all_vals['x'] = Rational(-1, 256)
		all_vals['y'] = Symbol('lambda_var_0')
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_7 SAT")

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_8(r1=r1,r2=r2)==True:
		all_vals = dict()
		all_vals['r1'] = r1
		all_vals['r2'] = r2
		all_vals['x'] = Add(Symbol('lambda_var_0'), Rational(-1, 1024))
		all_vals['y'] = Integer(0)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_8 SAT")

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_9(r1=r1,r2=r2)==True:
		all_vals = dict()
		all_vals['r1'] = r1
		all_vals['r2'] = r2
		all_vals['x'] = Rational(-1, 1024)
		all_vals['y'] = Symbol('lambda_var_0')
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_9 SAT")

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_10(r1=r1,r2=r2)==True:
		all_vals = dict()
		all_vals['r1'] = r1
		all_vals['r2'] = r2
		all_vals['x'] = Add(Symbol('lambda_var_0'), Rational(-1, 4096))
		all_vals['y'] = Integer(0)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_10 SAT")

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_11(r1=r1,r2=r2)==True:
		all_vals = dict()
		all_vals['r1'] = r1
		all_vals['r2'] = r2
		all_vals['x'] = Rational(-1, 4096)
		all_vals['y'] = Symbol('lambda_var_0')
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_11 SAT")

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_12(r1=r1,r2=r2)==True:
		all_vals = dict()
		all_vals['r1'] = r1
		all_vals['r2'] = r2
		all_vals['x'] = Add(Symbol('lambda_var_0'), Rational(-1, 16384))
		all_vals['y'] = Integer(0)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_12 SAT")

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_13(r1=r1,r2=r2)==True:
		all_vals = dict()
		all_vals['r1'] = r1
		all_vals['r2'] = r2
		all_vals['x'] = Rational(-1, 16384)
		all_vals['y'] = Symbol('lambda_var_0')
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_13 SAT")

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_14(r1=r1,r2=r2)==True:
		all_vals = dict()
		all_vals['r1'] = r1
		all_vals['r2'] = r2
		all_vals['x'] = Add(Symbol('lambda_var_0'), Rational(-1, 65536))
		all_vals['y'] = Integer(0)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_14 SAT")

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_15(r1=r1,r2=r2)==True:
		all_vals = dict()
		all_vals['r1'] = r1
		all_vals['r2'] = r2
		all_vals['x'] = Rational(-1, 65536)
		all_vals['y'] = Symbol('lambda_var_0')
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_15 SAT")

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_16(r1=r1,r2=r2)==True:
		all_vals = dict()
		all_vals['r1'] = r1
		all_vals['r2'] = r2
		all_vals['x'] = Add(Symbol('lambda_var_0'), Rational(-1, 262144))
		all_vals['y'] = Integer(0)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_16 SAT")

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_17(r1=r1,r2=r2)==True:
		all_vals = dict()
		all_vals['r1'] = r1
		all_vals['r2'] = r2
		all_vals['x'] = Rational(-1, 262144)
		all_vals['y'] = Symbol('lambda_var_0')
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_17 SAT")

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_18(r1=r1,r2=r2)==True:
		all_vals = dict()
		all_vals['r1'] = r1
		all_vals['r2'] = r2
		all_vals['x'] = Add(Symbol('lambda_var_0'), Rational(-1, 1048576))
		all_vals['y'] = Integer(0)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_18 SAT")

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_19(r1=r1,r2=r2)==True:
		all_vals = dict()
		all_vals['r1'] = r1
		all_vals['r2'] = r2
		all_vals['x'] = Rational(-1, 1048576)
		all_vals['y'] = Symbol('lambda_var_0')
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_19 SAT")

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_20(r1=r1,r2=r2)==True:
		all_vals = dict()
		all_vals['r1'] = r1
		all_vals['r2'] = r2
		all_vals['x'] = Add(Symbol('lambda_var_0'), Rational(-1, 4194304))
		all_vals['y'] = Integer(0)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_20 SAT")

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_21(r1=r1,r2=r2)==True:
		all_vals = dict()
		all_vals['r1'] = r1
		all_vals['r2'] = r2
		all_vals['x'] = Rational(-1, 4194304)
		all_vals['y'] = Symbol('lambda_var_0')
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_21 SAT")

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_22(r1=r1,r2=r2)==True:
		all_vals = dict()
		all_vals['r1'] = r1
		all_vals['r2'] = r2
		all_vals['x'] = Add(Symbol('lambda_var_0'), Rational(-1, 16777216))
		all_vals['y'] = Integer(0)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_22 SAT")

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass


	print("UNKNOWN")
