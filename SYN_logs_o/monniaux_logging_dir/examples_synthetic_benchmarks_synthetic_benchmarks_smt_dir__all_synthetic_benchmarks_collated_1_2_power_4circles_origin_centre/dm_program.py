import sympy
from sympy import *

def pre_condition_0(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 - y**4 > 0) & (r2 - y**4 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('r1'), Mul(Integer(-1), Pow(Symbol('y'), Integer(4)))), Integer(0)), StrictLessThan(Add(Symbol('r2'), Mul(Integer(-1), Pow(Symbol('y'), Integer(4)))), Integer(0)))

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
	#(-r2 + y**4 + 1 > 0) & (-r1 + y**4 + 1 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(4)), Integer(1)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(4)), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_3(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 1) & (r2 < 1)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Integer(1)), StrictLessThan(Symbol('r2'), Integer(1)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_4(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**4 + 1/16 > 0) & (-r1 + y**4 + 1/16 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(4)), Rational(1, 16)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(4)), Rational(1, 16)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_5(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 1/16) & (r2 < 1/16)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(1, 16)), StrictLessThan(Symbol('r2'), Rational(1, 16)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_6(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**4 + 81/256 > 0) & (-r1 + y**4 + 81/256 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(4)), Rational(81, 256)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(4)), Rational(81, 256)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_7(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 1297/4096) & (r2 < 1297/4096)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(1297, 4096)), StrictLessThan(Symbol('r2'), Rational(1297, 4096)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_8(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**4 + 625/4096 > 0) & (-r1 + y**4 + 625/4096 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(4)), Rational(625, 4096)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(4)), Rational(625, 4096)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_9(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 881/4096) & (r2 < 881/4096)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(881, 4096)), StrictLessThan(Symbol('r2'), Rational(881, 4096)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_10(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**4 + 6561/65536 > 0) & (-r1 + y**4 + 6561/65536 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(4)), Rational(6561, 65536)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(4)), Rational(6561, 65536)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_11(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 16561/65536) & (r2 < 16561/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(16561, 65536)), StrictLessThan(Symbol('r2'), Rational(16561, 65536)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_12(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**4 + 130321/1048576 > 0) & (-r1 + y**4 + 130321/1048576 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(4)), Rational(130321, 1048576)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(4)), Rational(130321, 1048576)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_13(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 290321/1048576) & (r2 < 290321/1048576)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(290321, 1048576)), StrictLessThan(Symbol('r2'), Rational(290321, 1048576)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_14(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**4 + 130321/1048576 > 0) & (-r1 + y**4 + 130321/1048576 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(4)), Rational(130321, 1048576)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(4)), Rational(130321, 1048576)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_15(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 4398577/16777216) & (r2 < 4398577/16777216)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(4398577, 16777216)), StrictLessThan(Symbol('r2'), Rational(4398577, 16777216)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_16(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**4 + 38950081/268435456 > 0) & (-r1 + y**4 + 38950081/268435456 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(4)), Rational(38950081, 268435456)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(4)), Rational(38950081, 268435456)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_17(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 72312257/268435456) & (r2 < 72312257/268435456)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(72312257, 268435456)), StrictLessThan(Symbol('r2'), Rational(72312257, 268435456)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_18(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**4 + 639128961/4294967296 > 0) & (-r1 + y**4 + 639128961/4294967296 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(4)), Rational(639128961, 4294967296)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(4)), Rational(639128961, 4294967296)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_19(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 1145378961/4294967296) & (r2 < 1145378961/4294967296)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(1145378961, 4294967296)), StrictLessThan(Symbol('r2'), Rational(1145378961, 4294967296)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_20(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**4 + 639128961/4294967296 > 0) & (-r1 + y**4 + 639128961/4294967296 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(4)), Rational(639128961, 4294967296)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(4)), Rational(639128961, 4294967296)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_21(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 1145378961/4294967296) & (r2 < 1145378961/4294967296)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(1145378961, 4294967296)), StrictLessThan(Symbol('r2'), Rational(1145378961, 4294967296)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_22(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**4 + 639128961/4294967296 > 0) & (-r1 + y**4 + 639128961/4294967296 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(4)), Rational(639128961, 4294967296)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(4)), Rational(639128961, 4294967296)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_23(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 1145378961/4294967296) & (r2 < 1145378961/4294967296)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(1145378961, 4294967296)), StrictLessThan(Symbol('r2'), Rational(1145378961, 4294967296)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_24(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**4 + 639128961/4294967296 > 0) & (-r1 + y**4 + 639128961/4294967296 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(4)), Rational(639128961, 4294967296)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(4)), Rational(639128961, 4294967296)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_25(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 1145378961/4294967296) & (r2 < 1145378961/4294967296)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(1145378961, 4294967296)), StrictLessThan(Symbol('r2'), Rational(1145378961, 4294967296)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_26(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**4 + 639128961/4294967296 > 0) & (-r1 + y**4 + 639128961/4294967296 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(4)), Rational(639128961, 4294967296)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(4)), Rational(639128961, 4294967296)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_27(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 1145378961/4294967296) & (r2 < 1145378961/4294967296)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(1145378961, 4294967296)), StrictLessThan(Symbol('r2'), Rational(1145378961, 4294967296)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_28(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**4 + 639128961/4294967296 > 0) & (-r1 + y**4 + 639128961/4294967296 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(4)), Rational(639128961, 4294967296)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(4)), Rational(639128961, 4294967296)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_29(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 1145378961/4294967296) & (r2 < 1145378961/4294967296)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(1145378961, 4294967296)), StrictLessThan(Symbol('r2'), Rational(1145378961, 4294967296)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_30(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**4 + 639128961/4294967296 > 0) & (-r1 + y**4 + 639128961/4294967296 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(4)), Rational(639128961, 4294967296)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(4)), Rational(639128961, 4294967296)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_31(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 1145378961/4294967296) & (r2 < 1145378961/4294967296)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(1145378961, 4294967296)), StrictLessThan(Symbol('r2'), Rational(1145378961, 4294967296)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_32(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**4 + 639128961/4294967296 > 0) & (-r1 + y**4 + 639128961/4294967296 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(4)), Rational(639128961, 4294967296)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(4)), Rational(639128961, 4294967296)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_33(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 1145378961/4294967296) & (r2 < 1145378961/4294967296)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(1145378961, 4294967296)), StrictLessThan(Symbol('r2'), Rational(1145378961, 4294967296)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_34(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**4 + 639128961/4294967296 > 0) & (-r1 + y**4 + 639128961/4294967296 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(4)), Rational(639128961, 4294967296)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(4)), Rational(639128961, 4294967296)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_35(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 1145378961/4294967296) & (r2 < 1145378961/4294967296)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(1145378961, 4294967296)), StrictLessThan(Symbol('r2'), Rational(1145378961, 4294967296)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_36(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**4 + 639128961/4294967296 > 0) & (-r1 + y**4 + 639128961/4294967296 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(4)), Rational(639128961, 4294967296)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(4)), Rational(639128961, 4294967296)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_37(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 1145378961/4294967296) & (r2 < 1145378961/4294967296)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(1145378961, 4294967296)), StrictLessThan(Symbol('r2'), Rational(1145378961, 4294967296)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_38(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**4 + 639128961/4294967296 > 0) & (-r1 + y**4 + 639128961/4294967296 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(4)), Rational(639128961, 4294967296)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(4)), Rational(639128961, 4294967296)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_39(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 1145378961/4294967296) & (r2 < 1145378961/4294967296)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(1145378961, 4294967296)), StrictLessThan(Symbol('r2'), Rational(1145378961, 4294967296)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_40(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**4 + 639128961/4294967296 > 0) & (-r1 + y**4 + 639128961/4294967296 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(4)), Rational(639128961, 4294967296)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(4)), Rational(639128961, 4294967296)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_41(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 1145378961/4294967296) & (r2 < 1145378961/4294967296)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(1145378961, 4294967296)), StrictLessThan(Symbol('r2'), Rational(1145378961, 4294967296)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_42(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**4 + 639128961/4294967296 > 0) & (-r1 + y**4 + 639128961/4294967296 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(4)), Rational(639128961, 4294967296)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(4)), Rational(639128961, 4294967296)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_43(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 1145378961/4294967296) & (r2 < 1145378961/4294967296)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(1145378961, 4294967296)), StrictLessThan(Symbol('r2'), Rational(1145378961, 4294967296)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_44(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**4 + 639128961/4294967296 > 0) & (-r1 + y**4 + 639128961/4294967296 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(4)), Rational(639128961, 4294967296)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(4)), Rational(639128961, 4294967296)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_45(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 1145378961/4294967296) & (r2 < 1145378961/4294967296)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(1145378961, 4294967296)), StrictLessThan(Symbol('r2'), Rational(1145378961, 4294967296)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_46(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**4 + 639128961/4294967296 > 0) & (-r1 + y**4 + 639128961/4294967296 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(4)), Rational(639128961, 4294967296)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(4)), Rational(639128961, 4294967296)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_47(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 1145378961/4294967296) & (r2 < 1145378961/4294967296)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(1145378961, 4294967296)), StrictLessThan(Symbol('r2'), Rational(1145378961, 4294967296)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_48(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**4 + 639128961/4294967296 > 0) & (-r1 + y**4 + 639128961/4294967296 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(4)), Rational(639128961, 4294967296)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(4)), Rational(639128961, 4294967296)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_49(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 1145378961/4294967296) & (r2 < 1145378961/4294967296)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(1145378961, 4294967296)), StrictLessThan(Symbol('r2'), Rational(1145378961, 4294967296)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_50(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**4 + 639128961/4294967296 > 0) & (-r1 + y**4 + 639128961/4294967296 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(4)), Rational(639128961, 4294967296)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(4)), Rational(639128961, 4294967296)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_51(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 1145378961/4294967296) & (r2 < 1145378961/4294967296)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(1145378961, 4294967296)), StrictLessThan(Symbol('r2'), Rational(1145378961, 4294967296)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_52(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**4 + 639128961/4294967296 > 0) & (-r1 + y**4 + 639128961/4294967296 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(4)), Rational(639128961, 4294967296)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(4)), Rational(639128961, 4294967296)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_53(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 1145378961/4294967296) & (r2 < 1145378961/4294967296)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(1145378961, 4294967296)), StrictLessThan(Symbol('r2'), Rational(1145378961, 4294967296)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_54(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**4 + 639128961/4294967296 > 0) & (-r1 + y**4 + 639128961/4294967296 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(4)), Rational(639128961, 4294967296)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(4)), Rational(639128961, 4294967296)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_55(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 1145378961/4294967296) & (r2 < 1145378961/4294967296)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(1145378961, 4294967296)), StrictLessThan(Symbol('r2'), Rational(1145378961, 4294967296)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_56(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**4 + 639128961/4294967296 > 0) & (-r1 + y**4 + 639128961/4294967296 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(4)), Rational(639128961, 4294967296)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(4)), Rational(639128961, 4294967296)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_57(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 1145378961/4294967296) & (r2 < 1145378961/4294967296)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(1145378961, 4294967296)), StrictLessThan(Symbol('r2'), Rational(1145378961, 4294967296)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_58(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**4 + 639128961/4294967296 > 0) & (-r1 + y**4 + 639128961/4294967296 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(4)), Rational(639128961, 4294967296)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(4)), Rational(639128961, 4294967296)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_59(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 1145378961/4294967296) & (r2 < 1145378961/4294967296)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(1145378961, 4294967296)), StrictLessThan(Symbol('r2'), Rational(1145378961, 4294967296)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_60(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**4 + 639128961/4294967296 > 0) & (-r1 + y**4 + 639128961/4294967296 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(4)), Rational(639128961, 4294967296)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(4)), Rational(639128961, 4294967296)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_61(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 1145378961/4294967296) & (r2 < 1145378961/4294967296)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(1145378961, 4294967296)), StrictLessThan(Symbol('r2'), Rational(1145378961, 4294967296)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_62(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**4 + 639128961/4294967296 > 0) & (-r1 + y**4 + 639128961/4294967296 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(4)), Rational(639128961, 4294967296)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(4)), Rational(639128961, 4294967296)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_63(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 1145378961/4294967296) & (r2 < 1145378961/4294967296)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(1145378961, 4294967296)), StrictLessThan(Symbol('r2'), Rational(1145378961, 4294967296)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_64(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**4 + 639128961/4294967296 > 0) & (-r1 + y**4 + 639128961/4294967296 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(4)), Rational(639128961, 4294967296)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(4)), Rational(639128961, 4294967296)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_65(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 1145378961/4294967296) & (r2 < 1145378961/4294967296)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(1145378961, 4294967296)), StrictLessThan(Symbol('r2'), Rational(1145378961, 4294967296)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_66(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**4 + 639128961/4294967296 > 0) & (-r1 + y**4 + 639128961/4294967296 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(4)), Rational(639128961, 4294967296)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(4)), Rational(639128961, 4294967296)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_67(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 1145378961/4294967296) & (r2 < 1145378961/4294967296)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(1145378961, 4294967296)), StrictLessThan(Symbol('r2'), Rational(1145378961, 4294967296)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_68(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**4 + 639128961/4294967296 > 0) & (-r1 + y**4 + 639128961/4294967296 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(4)), Rational(639128961, 4294967296)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(4)), Rational(639128961, 4294967296)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_69(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 1145378961/4294967296) & (r2 < 1145378961/4294967296)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(1145378961, 4294967296)), StrictLessThan(Symbol('r2'), Rational(1145378961, 4294967296)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_70(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**4 + 639128961/4294967296 > 0) & (-r1 + y**4 + 639128961/4294967296 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(4)), Rational(639128961, 4294967296)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(4)), Rational(639128961, 4294967296)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_71(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 1145378961/4294967296) & (r2 < 1145378961/4294967296)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(1145378961, 4294967296)), StrictLessThan(Symbol('r2'), Rational(1145378961, 4294967296)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_72(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**4 + 639128961/4294967296 > 0) & (-r1 + y**4 + 639128961/4294967296 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(4)), Rational(639128961, 4294967296)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(4)), Rational(639128961, 4294967296)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_73(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 1145378961/4294967296) & (r2 < 1145378961/4294967296)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(1145378961, 4294967296)), StrictLessThan(Symbol('r2'), Rational(1145378961, 4294967296)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_74(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**4 + 639128961/4294967296 > 0) & (-r1 + y**4 + 639128961/4294967296 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(4)), Rational(639128961, 4294967296)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(4)), Rational(639128961, 4294967296)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_75(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 1145378961/4294967296) & (r2 < 1145378961/4294967296)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(1145378961, 4294967296)), StrictLessThan(Symbol('r2'), Rational(1145378961, 4294967296)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_76(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**4 + 639128961/4294967296 > 0) & (-r1 + y**4 + 639128961/4294967296 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(4)), Rational(639128961, 4294967296)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(4)), Rational(639128961, 4294967296)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_77(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 1145378961/4294967296) & (r2 < 1145378961/4294967296)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(1145378961, 4294967296)), StrictLessThan(Symbol('r2'), Rational(1145378961, 4294967296)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_78(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**4 + 639128961/4294967296 > 0) & (-r1 + y**4 + 639128961/4294967296 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(4)), Rational(639128961, 4294967296)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(4)), Rational(639128961, 4294967296)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_79(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 1145378961/4294967296) & (r2 < 1145378961/4294967296)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(1145378961, 4294967296)), StrictLessThan(Symbol('r2'), Rational(1145378961, 4294967296)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_80(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**4 + 639128961/4294967296 > 0) & (-r1 + y**4 + 639128961/4294967296 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(4)), Rational(639128961, 4294967296)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(4)), Rational(639128961, 4294967296)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_81(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 1145378961/4294967296) & (r2 < 1145378961/4294967296)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(1145378961, 4294967296)), StrictLessThan(Symbol('r2'), Rational(1145378961, 4294967296)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_82(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**4 + 639128961/4294967296 > 0) & (-r1 + y**4 + 639128961/4294967296 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(4)), Rational(639128961, 4294967296)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(4)), Rational(639128961, 4294967296)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_83(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 1145378961/4294967296) & (r2 < 1145378961/4294967296)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(1145378961, 4294967296)), StrictLessThan(Symbol('r2'), Rational(1145378961, 4294967296)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_84(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**4 + 639128961/4294967296 > 0) & (-r1 + y**4 + 639128961/4294967296 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(4)), Rational(639128961, 4294967296)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(4)), Rational(639128961, 4294967296)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_85(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 1145378961/4294967296) & (r2 < 1145378961/4294967296)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(1145378961, 4294967296)), StrictLessThan(Symbol('r2'), Rational(1145378961, 4294967296)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_86(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**4 + 639128961/4294967296 > 0) & (-r1 + y**4 + 639128961/4294967296 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(4)), Rational(639128961, 4294967296)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(4)), Rational(639128961, 4294967296)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_87(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 1145378961/4294967296) & (r2 < 1145378961/4294967296)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(1145378961, 4294967296)), StrictLessThan(Symbol('r2'), Rational(1145378961, 4294967296)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_88(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**4 + 639128961/4294967296 > 0) & (-r1 + y**4 + 639128961/4294967296 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(4)), Rational(639128961, 4294967296)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(4)), Rational(639128961, 4294967296)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_89(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 1145378961/4294967296) & (r2 < 1145378961/4294967296)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(1145378961, 4294967296)), StrictLessThan(Symbol('r2'), Rational(1145378961, 4294967296)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_90(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**4 + 639128961/4294967296 > 0) & (-r1 + y**4 + 639128961/4294967296 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(4)), Rational(639128961, 4294967296)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(4)), Rational(639128961, 4294967296)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_91(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 1145378961/4294967296) & (r2 < 1145378961/4294967296)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(1145378961, 4294967296)), StrictLessThan(Symbol('r2'), Rational(1145378961, 4294967296)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_92(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**4 + 639128961/4294967296 > 0) & (-r1 + y**4 + 639128961/4294967296 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(4)), Rational(639128961, 4294967296)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(4)), Rational(639128961, 4294967296)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_93(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 1145378961/4294967296) & (r2 < 1145378961/4294967296)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(1145378961, 4294967296)), StrictLessThan(Symbol('r2'), Rational(1145378961, 4294967296)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_94(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**4 + 639128961/4294967296 > 0) & (-r1 + y**4 + 639128961/4294967296 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(4)), Rational(639128961, 4294967296)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(4)), Rational(639128961, 4294967296)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_95(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 1145378961/4294967296) & (r2 < 1145378961/4294967296)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(1145378961, 4294967296)), StrictLessThan(Symbol('r2'), Rational(1145378961, 4294967296)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_96(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**4 + 639128961/4294967296 > 0) & (-r1 + y**4 + 639128961/4294967296 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(4)), Rational(639128961, 4294967296)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(4)), Rational(639128961, 4294967296)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_97(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 1145378961/4294967296) & (r2 < 1145378961/4294967296)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(1145378961, 4294967296)), StrictLessThan(Symbol('r2'), Rational(1145378961, 4294967296)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_98(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**4 + 639128961/4294967296 > 0) & (-r1 + y**4 + 639128961/4294967296 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(4)), Rational(639128961, 4294967296)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(4)), Rational(639128961, 4294967296)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_99(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 1145378961/4294967296) & (r2 < 1145378961/4294967296)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(1145378961, 4294967296)), StrictLessThan(Symbol('r2'), Rational(1145378961, 4294967296)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_100(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**4 + 639128961/4294967296 > 0) & (-r1 + y**4 + 639128961/4294967296 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(4)), Rational(639128961, 4294967296)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(4)), Rational(639128961, 4294967296)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_101(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 1145378961/4294967296) & (r2 < 1145378961/4294967296)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(1145378961, 4294967296)), StrictLessThan(Symbol('r2'), Rational(1145378961, 4294967296)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_102(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**4 + 639128961/4294967296 > 0) & (-r1 + y**4 + 639128961/4294967296 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(4)), Rational(639128961, 4294967296)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(4)), Rational(639128961, 4294967296)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_103(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 1145378961/4294967296) & (r2 < 1145378961/4294967296)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(1145378961, 4294967296)), StrictLessThan(Symbol('r2'), Rational(1145378961, 4294967296)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_104(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**4 + 639128961/4294967296 > 0) & (-r1 + y**4 + 639128961/4294967296 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(4)), Rational(639128961, 4294967296)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(4)), Rational(639128961, 4294967296)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_105(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 1145378961/4294967296) & (r2 < 1145378961/4294967296)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(1145378961, 4294967296)), StrictLessThan(Symbol('r2'), Rational(1145378961, 4294967296)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_106(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**4 + 639128961/4294967296 > 0) & (-r1 + y**4 + 639128961/4294967296 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(4)), Rational(639128961, 4294967296)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(4)), Rational(639128961, 4294967296)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_107(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 1145378961/4294967296) & (r2 < 1145378961/4294967296)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(1145378961, 4294967296)), StrictLessThan(Symbol('r2'), Rational(1145378961, 4294967296)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_108(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**4 + 639128961/4294967296 > 0) & (-r1 + y**4 + 639128961/4294967296 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(4)), Rational(639128961, 4294967296)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(4)), Rational(639128961, 4294967296)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_109(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 1145378961/4294967296) & (r2 < 1145378961/4294967296)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(1145378961, 4294967296)), StrictLessThan(Symbol('r2'), Rational(1145378961, 4294967296)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_110(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**4 + 639128961/4294967296 > 0) & (-r1 + y**4 + 639128961/4294967296 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(4)), Rational(639128961, 4294967296)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(4)), Rational(639128961, 4294967296)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_111(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 1145378961/4294967296) & (r2 < 1145378961/4294967296)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(1145378961, 4294967296)), StrictLessThan(Symbol('r2'), Rational(1145378961, 4294967296)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_112(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**4 + 639128961/4294967296 > 0) & (-r1 + y**4 + 639128961/4294967296 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(4)), Rational(639128961, 4294967296)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(4)), Rational(639128961, 4294967296)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_113(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 1145378961/4294967296) & (r2 < 1145378961/4294967296)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(1145378961, 4294967296)), StrictLessThan(Symbol('r2'), Rational(1145378961, 4294967296)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_114(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**4 + 639128961/4294967296 > 0) & (-r1 + y**4 + 639128961/4294967296 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(4)), Rational(639128961, 4294967296)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(4)), Rational(639128961, 4294967296)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_115(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 1145378961/4294967296) & (r2 < 1145378961/4294967296)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(1145378961, 4294967296)), StrictLessThan(Symbol('r2'), Rational(1145378961, 4294967296)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_116(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**4 + 639128961/4294967296 > 0) & (-r1 + y**4 + 639128961/4294967296 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(4)), Rational(639128961, 4294967296)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(4)), Rational(639128961, 4294967296)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_117(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 1145378961/4294967296) & (r2 < 1145378961/4294967296)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(1145378961, 4294967296)), StrictLessThan(Symbol('r2'), Rational(1145378961, 4294967296)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_118(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**4 + 639128961/4294967296 > 0) & (-r1 + y**4 + 639128961/4294967296 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(4)), Rational(639128961, 4294967296)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(4)), Rational(639128961, 4294967296)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_119(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 1145378961/4294967296) & (r2 < 1145378961/4294967296)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(1145378961, 4294967296)), StrictLessThan(Symbol('r2'), Rational(1145378961, 4294967296)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_120(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**4 + 639128961/4294967296 > 0) & (-r1 + y**4 + 639128961/4294967296 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(4)), Rational(639128961, 4294967296)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(4)), Rational(639128961, 4294967296)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_121(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 1145378961/4294967296) & (r2 < 1145378961/4294967296)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(1145378961, 4294967296)), StrictLessThan(Symbol('r2'), Rational(1145378961, 4294967296)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_122(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**4 + 639128961/4294967296 > 0) & (-r1 + y**4 + 639128961/4294967296 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(4)), Rational(639128961, 4294967296)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(4)), Rational(639128961, 4294967296)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_123(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 1145378961/4294967296) & (r2 < 1145378961/4294967296)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(1145378961, 4294967296)), StrictLessThan(Symbol('r2'), Rational(1145378961, 4294967296)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_124(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**4 + 639128961/4294967296 > 0) & (-r1 + y**4 + 639128961/4294967296 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(4)), Rational(639128961, 4294967296)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(4)), Rational(639128961, 4294967296)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_125(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 1145378961/4294967296) & (r2 < 1145378961/4294967296)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(1145378961, 4294967296)), StrictLessThan(Symbol('r2'), Rational(1145378961, 4294967296)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_126(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**4 + 639128961/4294967296 > 0) & (-r1 + y**4 + 639128961/4294967296 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(4)), Rational(639128961, 4294967296)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(4)), Rational(639128961, 4294967296)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_127(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 1145378961/4294967296) & (r2 < 1145378961/4294967296)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(1145378961, 4294967296)), StrictLessThan(Symbol('r2'), Rational(1145378961, 4294967296)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_128(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**4 + 639128961/4294967296 > 0) & (-r1 + y**4 + 639128961/4294967296 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(4)), Rational(639128961, 4294967296)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(4)), Rational(639128961, 4294967296)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_129(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 1145378961/4294967296) & (r2 < 1145378961/4294967296)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(1145378961, 4294967296)), StrictLessThan(Symbol('r2'), Rational(1145378961, 4294967296)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_130(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**4 + 639128961/4294967296 > 0) & (-r1 + y**4 + 639128961/4294967296 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(4)), Rational(639128961, 4294967296)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(4)), Rational(639128961, 4294967296)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_131(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 1145378961/4294967296) & (r2 < 1145378961/4294967296)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(1145378961, 4294967296)), StrictLessThan(Symbol('r2'), Rational(1145378961, 4294967296)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_132(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**4 + 639128961/4294967296 > 0) & (-r1 + y**4 + 639128961/4294967296 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(4)), Rational(639128961, 4294967296)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(4)), Rational(639128961, 4294967296)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_133(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 1145378961/4294967296) & (r2 < 1145378961/4294967296)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(1145378961, 4294967296)), StrictLessThan(Symbol('r2'), Rational(1145378961, 4294967296)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_134(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**4 + 639128961/4294967296 > 0) & (-r1 + y**4 + 639128961/4294967296 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(4)), Rational(639128961, 4294967296)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(4)), Rational(639128961, 4294967296)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_135(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 1145378961/4294967296) & (r2 < 1145378961/4294967296)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(1145378961, 4294967296)), StrictLessThan(Symbol('r2'), Rational(1145378961, 4294967296)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_136(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**4 + 639128961/4294967296 > 0) & (-r1 + y**4 + 639128961/4294967296 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(4)), Rational(639128961, 4294967296)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(4)), Rational(639128961, 4294967296)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_137(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 1145378961/4294967296) & (r2 < 1145378961/4294967296)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(1145378961, 4294967296)), StrictLessThan(Symbol('r2'), Rational(1145378961, 4294967296)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_138(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**4 + 639128961/4294967296 > 0) & (-r1 + y**4 + 639128961/4294967296 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(4)), Rational(639128961, 4294967296)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(4)), Rational(639128961, 4294967296)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_139(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 1145378961/4294967296) & (r2 < 1145378961/4294967296)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(1145378961, 4294967296)), StrictLessThan(Symbol('r2'), Rational(1145378961, 4294967296)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_140(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**4 + 639128961/4294967296 > 0) & (-r1 + y**4 + 639128961/4294967296 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(4)), Rational(639128961, 4294967296)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(4)), Rational(639128961, 4294967296)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_141(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 1145378961/4294967296) & (r2 < 1145378961/4294967296)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(1145378961, 4294967296)), StrictLessThan(Symbol('r2'), Rational(1145378961, 4294967296)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_142(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**4 + 639128961/4294967296 > 0) & (-r1 + y**4 + 639128961/4294967296 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(4)), Rational(639128961, 4294967296)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(4)), Rational(639128961, 4294967296)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_143(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 1145378961/4294967296) & (r2 < 1145378961/4294967296)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(1145378961, 4294967296)), StrictLessThan(Symbol('r2'), Rational(1145378961, 4294967296)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_144(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**4 + 639128961/4294967296 > 0) & (-r1 + y**4 + 639128961/4294967296 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(4)), Rational(639128961, 4294967296)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(4)), Rational(639128961, 4294967296)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_145(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 1145378961/4294967296) & (r2 < 1145378961/4294967296)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(1145378961, 4294967296)), StrictLessThan(Symbol('r2'), Rational(1145378961, 4294967296)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_146(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**4 + 639128961/4294967296 > 0) & (-r1 + y**4 + 639128961/4294967296 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(4)), Rational(639128961, 4294967296)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(4)), Rational(639128961, 4294967296)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_147(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 1145378961/4294967296) & (r2 < 1145378961/4294967296)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(1145378961, 4294967296)), StrictLessThan(Symbol('r2'), Rational(1145378961, 4294967296)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_148(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**4 + 639128961/4294967296 > 0) & (-r1 + y**4 + 639128961/4294967296 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(4)), Rational(639128961, 4294967296)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(4)), Rational(639128961, 4294967296)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_149(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 1145378961/4294967296) & (r2 < 1145378961/4294967296)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(1145378961, 4294967296)), StrictLessThan(Symbol('r2'), Rational(1145378961, 4294967296)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_150(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**4 + 639128961/4294967296 > 0) & (-r1 + y**4 + 639128961/4294967296 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(4)), Rational(639128961, 4294967296)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(4)), Rational(639128961, 4294967296)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_151(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 1145378961/4294967296) & (r2 < 1145378961/4294967296)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(1145378961, 4294967296)), StrictLessThan(Symbol('r2'), Rational(1145378961, 4294967296)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_152(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**4 + 639128961/4294967296 > 0) & (-r1 + y**4 + 639128961/4294967296 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(4)), Rational(639128961, 4294967296)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(4)), Rational(639128961, 4294967296)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_153(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 1145378961/4294967296) & (r2 < 1145378961/4294967296)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(1145378961, 4294967296)), StrictLessThan(Symbol('r2'), Rational(1145378961, 4294967296)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_154(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**4 + 639128961/4294967296 > 0) & (-r1 + y**4 + 639128961/4294967296 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(4)), Rational(639128961, 4294967296)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(4)), Rational(639128961, 4294967296)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_155(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 1145378961/4294967296) & (r2 < 1145378961/4294967296)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(1145378961, 4294967296)), StrictLessThan(Symbol('r2'), Rational(1145378961, 4294967296)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_156(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**4 + 639128961/4294967296 > 0) & (-r1 + y**4 + 639128961/4294967296 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(4)), Rational(639128961, 4294967296)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(4)), Rational(639128961, 4294967296)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_157(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 1145378961/4294967296) & (r2 < 1145378961/4294967296)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(1145378961, 4294967296)), StrictLessThan(Symbol('r2'), Rational(1145378961, 4294967296)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_158(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**4 + 639128961/4294967296 > 0) & (-r1 + y**4 + 639128961/4294967296 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(4)), Rational(639128961, 4294967296)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(4)), Rational(639128961, 4294967296)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_159(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 1145378961/4294967296) & (r2 < 1145378961/4294967296)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(1145378961, 4294967296)), StrictLessThan(Symbol('r2'), Rational(1145378961, 4294967296)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_160(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**4 + 639128961/4294967296 > 0) & (-r1 + y**4 + 639128961/4294967296 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(4)), Rational(639128961, 4294967296)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(4)), Rational(639128961, 4294967296)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_161(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 1145378961/4294967296) & (r2 < 1145378961/4294967296)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(1145378961, 4294967296)), StrictLessThan(Symbol('r2'), Rational(1145378961, 4294967296)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_162(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**4 + 639128961/4294967296 > 0) & (-r1 + y**4 + 639128961/4294967296 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(4)), Rational(639128961, 4294967296)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(4)), Rational(639128961, 4294967296)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_163(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 1145378961/4294967296) & (r2 < 1145378961/4294967296)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(1145378961, 4294967296)), StrictLessThan(Symbol('r2'), Rational(1145378961, 4294967296)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_164(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**4 + 639128961/4294967296 > 0) & (-r1 + y**4 + 639128961/4294967296 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(4)), Rational(639128961, 4294967296)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(4)), Rational(639128961, 4294967296)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_165(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 1145378961/4294967296) & (r2 < 1145378961/4294967296)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(1145378961, 4294967296)), StrictLessThan(Symbol('r2'), Rational(1145378961, 4294967296)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_166(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**4 + 639128961/4294967296 > 0) & (-r1 + y**4 + 639128961/4294967296 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(4)), Rational(639128961, 4294967296)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(4)), Rational(639128961, 4294967296)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_167(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 1145378961/4294967296) & (r2 < 1145378961/4294967296)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(1145378961, 4294967296)), StrictLessThan(Symbol('r2'), Rational(1145378961, 4294967296)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_168(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**4 + 639128961/4294967296 > 0) & (-r1 + y**4 + 639128961/4294967296 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(4)), Rational(639128961, 4294967296)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(4)), Rational(639128961, 4294967296)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_169(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 1145378961/4294967296) & (r2 < 1145378961/4294967296)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(1145378961, 4294967296)), StrictLessThan(Symbol('r2'), Rational(1145378961, 4294967296)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_170(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**4 + 639128961/4294967296 > 0) & (-r1 + y**4 + 639128961/4294967296 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(4)), Rational(639128961, 4294967296)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(4)), Rational(639128961, 4294967296)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_171(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 1145378961/4294967296) & (r2 < 1145378961/4294967296)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(1145378961, 4294967296)), StrictLessThan(Symbol('r2'), Rational(1145378961, 4294967296)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_172(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**4 + 639128961/4294967296 > 0) & (-r1 + y**4 + 639128961/4294967296 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(4)), Rational(639128961, 4294967296)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(4)), Rational(639128961, 4294967296)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_173(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 1145378961/4294967296) & (r2 < 1145378961/4294967296)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(1145378961, 4294967296)), StrictLessThan(Symbol('r2'), Rational(1145378961, 4294967296)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_174(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**4 + 639128961/4294967296 > 0) & (-r1 + y**4 + 639128961/4294967296 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(4)), Rational(639128961, 4294967296)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(4)), Rational(639128961, 4294967296)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_175(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 1145378961/4294967296) & (r2 < 1145378961/4294967296)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(1145378961, 4294967296)), StrictLessThan(Symbol('r2'), Rational(1145378961, 4294967296)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_176(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**4 + 639128961/4294967296 > 0) & (-r1 + y**4 + 639128961/4294967296 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(4)), Rational(639128961, 4294967296)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(4)), Rational(639128961, 4294967296)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_177(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 1145378961/4294967296) & (r2 < 1145378961/4294967296)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(1145378961, 4294967296)), StrictLessThan(Symbol('r2'), Rational(1145378961, 4294967296)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_178(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**4 + 639128961/4294967296 > 0) & (-r1 + y**4 + 639128961/4294967296 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(4)), Rational(639128961, 4294967296)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(4)), Rational(639128961, 4294967296)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_179(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 1145378961/4294967296) & (r2 < 1145378961/4294967296)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(1145378961, 4294967296)), StrictLessThan(Symbol('r2'), Rational(1145378961, 4294967296)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_180(r1:sympy.Rational,r2:sympy.Rational):
	#(-r2 + y**4 + 639128961/4294967296 > 0) & (-r1 + y**4 + 639128961/4294967296 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('r2')), Pow(Symbol('y'), Integer(4)), Rational(639128961, 4294967296)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('r1')), Pow(Symbol('y'), Integer(4)), Rational(639128961, 4294967296)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_181(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 1145378961/4294967296) & (r2 < 1145378961/4294967296)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(1145378961, 4294967296)), StrictLessThan(Symbol('r2'), Rational(1145378961, 4294967296)))