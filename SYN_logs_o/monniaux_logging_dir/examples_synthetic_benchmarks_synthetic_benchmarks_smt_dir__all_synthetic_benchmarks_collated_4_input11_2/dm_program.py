import sympy
from sympy import *

def pre_condition_0(c:sympy.Rational,d:sympy.Rational):
	#(d > -y) & (c - y**2 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('d'), Mul(Integer(-1), Symbol('y'))), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2)))), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1(c:sympy.Rational,d:sympy.Rational):
	#(c > 0) & (d > 0)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Integer(0)), StrictGreaterThan(Symbol('d'), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_2(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 1) & (c - y**2 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Integer(1)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_3(c:sympy.Rational,d:sympy.Rational):
	#(c > 3) & (d > -1)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Integer(3)), StrictGreaterThan(Symbol('d'), Integer(-1)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_4(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 1/16) & (c - y**2 + 1/16 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(1, 16)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(1, 16)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_5(c:sympy.Rational,d:sympy.Rational):
	#(c > -3/64) & (d > -1/16)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-3, 64)), StrictGreaterThan(Symbol('d'), Rational(-1, 16)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_6(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 49/1024) & (c - y**2 + 49/1024 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(49, 1024)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(49, 1024)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_7(c:sympy.Rational,d:sympy.Rational):
	#(c > -49/1024) & (d > 49/1024)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-49, 1024)), StrictGreaterThan(Symbol('d'), Rational(49, 1024)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_8(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 225/4096) & (c - y**2 + 225/4096 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(225, 4096)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(225, 4096)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_9(c:sympy.Rational,d:sympy.Rational):
	#(c > -209/4096) & (d > 481/4096)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-209, 4096)), StrictGreaterThan(Symbol('d'), Rational(481, 4096)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_10(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 841/16384) & (c - y**2 + 841/16384 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(841, 16384)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(841, 16384)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_11(c:sympy.Rational,d:sympy.Rational):
	#(c > -841/16384) & (d > 841/16384)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-841, 16384)), StrictGreaterThan(Symbol('d'), Rational(841, 16384)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_12(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 12769/262144) & (c - y**2 + 12769/262144 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(12769, 262144)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(12769, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_13(c:sympy.Rational,d:sympy.Rational):
	#(c > -399/8192) & (d > 13281/262144)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-399, 8192)), StrictGreaterThan(Symbol('d'), Rational(13281, 262144)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_14(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_15(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_16(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_17(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_18(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_19(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_20(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_21(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_22(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_23(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_24(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_25(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_26(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_27(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_28(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_29(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_30(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_31(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_32(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_33(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_34(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_35(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_36(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_37(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_38(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_39(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_40(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_41(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_42(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_43(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_44(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_45(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_46(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_47(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_48(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_49(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_50(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_51(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_52(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_53(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_54(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_55(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_56(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_57(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_58(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_59(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_60(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_61(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_62(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_63(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_64(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_65(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_66(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_67(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_68(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_69(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_70(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_71(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_72(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_73(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_74(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_75(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_76(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_77(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_78(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_79(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_80(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_81(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_82(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_83(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_84(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_85(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_86(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_87(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_88(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_89(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_90(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_91(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_92(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_93(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_94(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_95(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_96(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_97(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_98(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_99(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_100(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_101(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_102(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_103(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_104(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_105(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_106(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_107(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_108(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_109(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_110(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_111(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_112(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_113(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_114(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_115(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_116(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_117(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_118(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_119(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_120(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_121(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_122(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_123(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_124(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_125(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_126(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_127(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_128(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_129(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_130(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_131(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_132(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_133(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_134(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_135(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_136(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_137(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_138(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_139(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_140(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_141(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_142(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_143(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_144(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_145(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_146(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_147(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_148(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_149(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_150(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_151(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_152(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_153(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_154(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_155(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_156(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_157(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_158(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_159(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_160(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_161(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_162(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_163(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_164(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_165(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_166(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_167(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_168(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_169(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_170(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_171(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_172(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_173(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_174(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_175(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_176(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_177(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_178(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_179(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_180(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_181(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_182(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_183(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_184(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_185(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_186(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_187(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_188(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_189(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_190(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_191(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_192(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_193(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_194(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_195(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_196(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_197(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_198(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_199(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_200(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_201(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_202(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_203(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_204(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_205(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_206(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_207(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_208(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_209(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_210(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_211(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_212(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_213(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_214(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_215(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_216(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_217(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_218(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_219(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_220(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_221(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_222(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_223(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_224(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_225(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_226(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_227(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_228(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_229(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_230(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_231(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_232(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_233(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_234(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_235(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_236(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_237(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_238(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_239(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_240(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_241(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_242(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_243(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_244(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_245(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_246(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_247(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_248(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_249(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_250(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_251(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_252(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_253(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_254(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_255(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_256(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_257(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_258(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_259(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_260(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_261(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_262(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_263(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_264(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_265(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_266(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_267(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_268(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_269(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_270(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_271(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_272(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_273(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_274(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_275(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_276(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_277(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_278(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_279(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_280(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_281(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_282(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_283(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_284(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_285(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_286(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_287(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_288(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_289(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_290(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_291(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_292(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_293(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_294(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_295(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_296(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_297(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_298(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_299(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_300(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_301(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_302(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_303(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_304(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_305(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_306(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_307(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_308(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_309(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_310(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_311(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_312(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_313(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_314(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_315(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_316(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_317(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_318(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_319(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_320(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_321(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_322(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_323(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_324(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_325(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_326(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_327(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_328(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_329(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_330(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_331(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_332(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_333(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_334(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_335(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_336(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_337(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_338(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_339(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_340(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_341(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_342(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_343(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_344(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_345(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_346(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_347(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_348(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_349(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_350(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_351(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_352(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_353(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_354(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_355(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_356(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_357(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_358(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_359(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_360(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_361(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_362(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_363(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_364(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_365(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_366(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_367(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_368(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_369(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_370(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_371(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_372(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_373(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_374(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_375(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_376(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_377(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_378(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_379(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_380(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_381(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_382(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_383(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_384(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_385(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_386(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_387(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_388(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_389(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_390(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_391(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_392(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_393(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_394(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_395(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_396(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_397(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_398(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_399(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_400(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_401(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_402(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_403(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_404(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_405(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_406(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_407(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_408(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_409(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_410(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_411(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_412(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_413(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_414(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_415(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_416(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_417(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_418(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_419(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_420(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_421(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_422(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_423(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_424(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_425(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_426(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_427(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_428(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_429(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_430(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_431(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_432(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_433(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_434(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_435(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_436(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_437(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_438(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_439(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_440(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_441(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_442(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_443(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_444(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_445(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_446(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_447(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_448(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_449(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_450(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_451(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_452(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_453(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_454(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_455(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_456(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_457(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_458(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_459(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_460(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_461(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_462(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_463(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_464(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_465(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_466(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_467(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_468(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_469(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_470(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_471(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_472(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_473(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_474(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_475(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_476(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_477(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_478(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_479(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_480(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_481(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_482(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_483(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_484(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_485(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_486(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_487(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_488(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_489(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_490(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_491(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_492(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_493(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_494(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_495(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_496(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_497(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_498(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_499(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_500(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_501(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_502(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_503(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_504(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_505(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_506(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_507(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_508(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_509(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_510(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_511(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_512(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_513(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_514(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_515(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_516(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_517(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_518(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_519(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_520(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_521(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_522(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_523(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_524(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_525(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_526(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_527(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_528(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_529(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_530(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_531(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_532(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_533(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_534(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_535(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_536(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_537(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_538(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_539(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_540(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_541(c:sympy.Rational,d:sympy.Rational):
	#(c > -836771329/17179869184) & (d > 836771329/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('c'), Rational(-836771329, 17179869184)), StrictGreaterThan(Symbol('d'), Rational(836771329, 17179869184)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_542(c:sympy.Rational,d:sympy.Rational):
	#(d + y > 836771329/17179869184) & (c - y**2 + 836771329/17179869184 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('d'), Symbol('y')), Rational(836771329, 17179869184)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(836771329, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'c':c, 'd':d })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_543(c:sympy.Rational,d:sympy.Rational):