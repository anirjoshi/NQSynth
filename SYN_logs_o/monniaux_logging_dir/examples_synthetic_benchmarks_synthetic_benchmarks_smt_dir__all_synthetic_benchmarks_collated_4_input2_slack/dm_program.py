import sympy
from sympy import *

def pre_condition_0(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d2 > x) & (d1 > -x)

	pre_cond = And(StrictGreaterThan(Symbol('d2'), Symbol('x')), StrictGreaterThan(Symbol('d1'), Mul(Integer(-1), Symbol('x'))))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1) & (d2 - x > -1)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Integer(1)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Integer(-1)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_2(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/4) & (d2 - x > -1/4)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 4)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 4)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_3(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16) & (d2 - x > -1/16)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_4(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/64) & (d2 - x > -1/64)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 64)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 64)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_5(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/256) & (d2 - x > -1/256)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 256)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 256)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_6(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/1024) & (d2 - x > -1/1024)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 1024)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 1024)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_7(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/4096) & (d2 - x > -1/4096)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 4096)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 4096)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_8(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16384) & (d2 - x > -1/16384)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16384)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16384)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_9(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/65536) & (d2 - x > -1/65536)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 65536)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 65536)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_10(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/262144) & (d2 - x > -1/262144)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 262144)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 262144)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_11(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/1048576) & (d2 - x > -1/1048576)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 1048576)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 1048576)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_12(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/4194304) & (d2 - x > -1/4194304)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 4194304)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 4194304)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_13(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_14(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_15(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_16(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_17(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_18(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_19(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_20(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_21(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_22(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_23(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_24(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_25(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_26(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_27(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_28(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_29(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_30(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_31(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_32(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_33(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_34(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_35(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_36(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_37(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_38(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_39(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_40(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_41(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_42(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_43(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_44(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_45(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_46(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_47(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_48(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_49(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_50(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_51(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_52(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_53(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_54(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_55(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_56(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_57(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_58(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_59(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_60(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_61(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_62(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_63(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_64(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_65(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_66(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_67(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_68(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_69(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_70(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_71(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_72(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_73(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_74(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_75(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_76(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_77(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_78(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_79(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_80(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_81(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_82(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_83(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_84(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_85(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_86(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_87(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_88(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_89(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_90(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_91(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_92(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_93(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_94(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_95(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_96(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_97(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_98(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_99(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_100(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_101(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_102(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_103(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_104(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_105(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_106(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_107(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_108(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_109(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_110(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_111(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_112(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_113(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_114(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_115(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_116(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_117(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_118(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_119(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_120(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_121(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_122(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_123(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_124(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_125(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_126(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_127(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_128(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_129(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_130(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_131(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_132(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_133(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_134(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_135(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_136(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_137(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_138(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_139(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_140(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_141(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_142(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_143(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_144(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_145(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_146(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_147(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_148(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_149(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_150(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_151(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_152(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_153(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_154(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_155(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_156(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_157(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_158(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_159(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_160(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_161(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_162(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_163(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_164(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_165(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_166(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_167(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_168(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_169(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_170(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_171(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_172(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_173(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_174(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_175(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_176(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_177(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_178(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_179(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_180(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_181(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_182(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_183(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_184(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_185(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_186(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_187(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_188(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_189(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_190(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_191(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_192(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_193(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_194(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_195(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_196(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_197(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_198(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_199(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_200(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_201(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_202(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_203(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_204(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_205(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_206(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_207(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_208(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_209(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_210(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_211(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_212(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_213(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_214(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_215(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_216(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_217(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_218(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_219(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_220(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_221(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_222(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_223(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_224(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_225(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_226(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_227(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_228(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_229(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_230(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_231(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_232(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_233(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_234(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_235(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_236(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_237(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_238(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_239(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_240(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_241(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_242(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_243(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_244(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_245(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_246(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_247(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_248(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_249(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_250(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_251(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_252(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_253(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_254(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_255(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_256(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_257(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_258(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_259(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_260(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_261(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_262(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_263(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_264(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_265(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_266(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_267(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_268(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_269(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_270(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_271(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_272(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_273(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_274(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_275(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_276(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_277(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_278(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_279(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_280(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_281(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_282(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_283(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_284(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_285(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_286(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_287(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_288(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_289(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_290(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_291(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_292(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_293(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_294(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_295(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_296(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_297(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_298(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_299(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_300(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_301(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_302(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_303(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_304(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_305(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_306(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_307(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_308(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_309(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_310(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_311(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_312(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_313(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_314(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_315(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_316(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_317(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_318(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_319(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_320(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_321(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_322(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_323(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_324(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_325(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_326(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_327(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_328(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_329(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_330(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_331(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_332(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_333(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_334(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_335(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_336(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_337(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_338(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_339(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_340(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_341(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_342(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_343(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_344(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_345(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_346(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_347(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_348(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_349(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_350(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_351(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_352(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_353(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_354(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_355(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_356(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_357(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_358(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_359(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_360(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_361(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_362(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_363(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_364(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_365(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_366(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_367(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_368(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_369(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_370(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_371(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_372(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_373(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_374(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_375(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_376(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_377(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_378(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_379(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_380(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_381(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_382(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_383(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_384(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_385(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_386(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_387(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_388(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_389(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_390(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_391(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_392(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_393(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_394(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_395(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_396(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_397(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_398(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_399(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_400(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_401(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_402(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_403(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_404(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_405(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_406(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_407(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_408(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_409(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_410(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_411(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_412(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_413(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_414(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_415(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_416(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_417(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_418(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_419(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_420(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_421(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_422(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_423(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_424(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_425(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_426(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_427(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_428(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_429(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_430(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_431(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_432(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_433(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_434(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_435(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_436(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_437(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_438(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_439(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_440(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_441(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_442(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_443(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_444(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_445(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_446(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_447(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_448(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_449(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_450(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_451(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_452(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_453(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_454(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_455(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_456(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_457(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_458(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_459(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_460(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_461(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_462(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_463(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_464(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_465(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_466(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_467(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_468(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_469(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_470(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_471(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_472(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_473(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_474(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_475(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_476(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_477(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_478(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_479(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_480(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_481(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_482(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_483(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_484(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_485(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_486(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_487(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_488(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_489(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_490(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_491(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_492(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_493(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_494(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_495(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_496(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_497(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_498(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_499(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_500(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_501(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_502(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_503(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_504(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_505(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_506(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_507(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_508(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_509(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_510(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_511(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_512(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_513(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_514(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_515(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_516(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_517(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_518(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_519(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_520(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_521(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_522(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_523(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_524(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_525(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_526(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_527(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_528(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_529(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_530(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_531(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_532(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_533(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_534(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_535(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_536(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_537(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_538(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_539(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_540(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_541(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_542(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_543(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_544(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_545(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_546(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_547(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_548(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_549(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_550(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_551(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_552(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_553(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_554(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_555(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_556(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_557(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_558(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_559(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_560(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_561(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_562(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_563(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_564(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_565(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_566(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_567(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_568(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_569(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_570(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_571(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_572(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_573(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_574(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_575(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_576(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_577(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_578(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_579(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_580(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_581(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_582(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_583(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_584(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_585(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_586(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_587(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_588(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_589(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_590(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_591(x:sympy.Rational,d1:sympy.Rational,d2:sympy.Rational):
	#(d1 + x > 1/16777216) & (d2 - x > -1/16777216)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d1'), Symbol('x')), Rational(1, 16777216)), StrictGreaterThan(Add(Symbol('d2'), Mul(Integer(-1), Symbol('x'))), Rational(-1, 16777216)))

	eval = pre_cond.subs( { 'x':x, 'd1':d1, 'd2':d2 })

	if eval==True:
		assert eval!=False
		return True
	return False


