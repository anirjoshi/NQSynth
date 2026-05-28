import sympy
from sympy import *

def pre_condition_0(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 - y**12 > 0) & (r2 - y**12 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('r1'), Mul(Integer(-1), Pow(Symbol('y'), Integer(12)))), Integer(0)), StrictLessThan(Add(Symbol('r2'), Mul(Integer(-1), Pow(Symbol('y'), Integer(12)))), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 0) & (r2 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Integer(0)), StrictLessThan(Symbol('r2'), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_2(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 1/4096 > 0) & (-r1 + y**12 + 1/4096 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(1, 4096)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(1, 4096)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_3(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 16777217/68719476736) & (r2 < 16777217/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(16777217, 68719476736)), StrictLessThan(Symbol('r2'), Rational(16777217, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_4(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 1 > 0) & (-r1 + y**12 + 1 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Integer(1)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_5(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 68719476737/68719476736) & (r2 < 68719476737/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(68719476737, 68719476736)), StrictLessThan(Symbol('r2'), Rational(68719476737, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_6(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 4096 > 0) & (-r1 + y**12 + 4096 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Integer(4096)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Integer(4096)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_7(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 281474976710657/68719476736) & (r2 < 281474976710657/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(281474976710657, 68719476736)), StrictLessThan(Symbol('r2'), Rational(281474976710657, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_8(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441 > 0) & (-r1 + y**12 + 531441 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Integer(531441)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Integer(531441)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_9(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 36520347436056577/68719476736) & (r2 < 36520347436056577/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(36520347436056577, 68719476736)), StrictLessThan(Symbol('r2'), Rational(36520347436056577, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_10(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_11(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_12(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_13(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_14(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_15(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_16(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_17(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_18(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_19(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_20(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_21(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_22(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_23(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_24(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_25(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_26(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_27(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_28(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_29(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_30(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_31(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_32(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_33(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_34(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_35(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_36(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_37(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_38(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_39(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_40(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_41(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_42(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_43(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_44(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_45(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_46(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_47(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_48(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_49(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_50(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_51(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_52(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_53(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_54(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_55(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_56(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_57(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_58(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_59(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_60(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_61(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_62(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_63(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_64(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_65(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_66(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_67(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_68(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_69(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_70(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_71(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_72(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_73(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_74(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_75(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_76(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_77(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_78(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_79(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_80(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_81(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_82(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_83(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_84(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_85(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_86(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_87(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_88(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_89(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_90(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_91(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_92(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_93(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_94(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_95(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_96(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_97(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_98(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_99(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_100(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_101(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_102(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_103(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_104(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_105(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_106(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_107(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_108(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_109(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_110(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_111(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_112(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_113(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_114(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_115(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_116(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_117(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_118(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_119(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_120(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_121(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_122(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_123(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_124(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_125(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_126(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_127(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_128(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_129(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_130(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_131(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_132(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_133(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_134(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_135(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_136(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_137(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_138(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_139(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_140(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_141(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_142(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_143(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_144(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_145(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_146(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_147(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_148(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_149(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_150(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_151(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_152(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_153(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_154(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_155(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_156(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_157(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_158(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_159(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_160(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_161(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_162(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_163(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_164(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_165(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_166(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_167(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_168(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_169(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_170(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_171(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_172(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_173(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_174(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_175(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_176(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_177(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_178(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_179(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_180(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_181(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_182(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_183(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_184(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_185(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_186(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_187(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_188(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_189(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_190(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_191(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_192(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_193(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_194(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_195(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_196(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_197(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_198(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_199(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_200(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_201(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_202(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_203(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_204(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_205(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_206(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_207(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_208(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_209(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_210(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_211(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_212(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_213(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_214(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_215(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_216(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_217(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_218(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_219(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_220(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_221(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_222(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_223(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_224(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_225(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_226(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_227(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_228(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_229(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_230(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_231(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_232(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_233(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_234(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_235(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_236(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_237(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_238(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_239(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_240(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_241(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_242(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_243(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_244(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_245(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_246(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_247(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_248(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_249(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_250(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_251(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_252(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_253(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_254(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_255(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_256(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_257(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_258(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_259(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_260(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_261(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_262(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_263(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_264(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_265(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_266(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_267(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_268(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_269(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_270(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_271(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_272(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_273(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_274(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_275(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_276(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_277(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_278(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_279(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_280(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_281(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_282(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_283(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_284(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_285(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_286(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_287(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_288(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_289(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_290(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_291(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_292(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_293(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_294(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_295(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_296(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_297(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_298(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_299(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_300(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_301(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_302(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_303(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_304(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_305(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_306(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_307(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_308(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_309(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_310(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_311(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_312(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_313(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_314(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_315(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_316(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_317(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_318(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_319(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_320(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_321(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_322(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_323(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_324(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_325(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_326(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_327(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_328(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_329(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_330(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_331(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_332(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_333(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_334(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_335(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_336(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_337(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_338(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_339(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_340(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_341(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_342(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_343(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_344(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_345(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_346(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_347(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_348(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_349(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_350(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_351(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_352(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_353(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_354(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_355(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_356(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_357(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_358(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_359(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_360(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_361(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_362(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_363(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_364(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_365(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_366(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_367(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_368(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_369(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_370(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_371(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_372(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_373(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_374(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_375(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_376(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_377(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_378(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_379(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_380(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_381(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_382(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_383(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_384(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_385(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_386(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_387(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_388(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_389(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_390(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_391(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_392(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_393(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_394(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_395(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_396(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_397(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_398(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_399(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_400(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_401(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_402(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_403(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_404(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_405(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_406(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_407(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_408(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_409(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_410(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_411(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_412(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_413(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_414(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_415(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_416(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_417(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_418(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_419(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_420(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_421(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_422(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_423(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_424(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_425(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_426(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_427(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_428(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_429(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_430(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_431(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_432(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_433(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_434(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_435(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_436(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_437(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_438(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_439(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_440(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_441(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_442(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_443(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_444(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_445(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_446(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_447(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_448(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_449(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_450(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_451(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_452(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_453(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_454(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_455(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_456(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_457(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_458(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_459(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_460(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_461(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_462(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_463(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_464(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_465(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_466(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_467(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_468(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_469(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_470(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_471(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_472(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_473(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_474(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_475(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_476(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_477(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_478(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_479(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_480(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_481(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_482(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_483(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_484(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_485(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_486(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_487(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_488(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_489(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_490(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_491(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_492(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_493(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_494(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_495(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_496(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_497(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_498(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_499(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_500(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_501(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_502(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_503(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_504(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_505(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_506(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_507(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_508(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_509(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_510(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_511(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_512(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_513(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_514(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_515(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_516(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_517(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_518(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_519(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_520(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_521(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_522(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_523(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_524(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_525(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_526(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_527(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_528(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_529(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_530(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_531(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_532(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_533(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_534(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_535(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_536(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_537(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_538(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_539(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_540(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_541(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_542(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_543(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_544(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_545(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_546(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_547(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_548(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_549(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_550(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_551(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_552(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_553(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_554(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_555(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_556(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_557(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_558(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_559(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_560(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_561(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_562(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_563(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_564(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_565(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_566(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_567(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_568(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_569(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_570(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_571(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_572(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_573(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_574(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_575(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_576(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_577(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_578(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_579(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_580(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_581(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_582(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_583(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_584(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_585(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_586(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_587(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_588(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_589(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_590(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_591(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_592(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_593(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_594(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_595(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_596(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_597(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_598(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_599(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_600(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_601(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_602(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_603(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_604(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_605(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_606(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_607(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_608(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_609(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_610(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_611(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_612(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_613(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_614(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_615(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_616(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(12)), Rational(531441, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_617(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 2176782337/68719476736) & (r2 < 2176782337/68719476736)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(2176782337, 68719476736)), StrictLessThan(Symbol('r2'), Rational(2176782337, 68719476736)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_618(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**12 + 531441/16777216 > 0) & (-r1 + y**12 + 531441/16777216 < 0)