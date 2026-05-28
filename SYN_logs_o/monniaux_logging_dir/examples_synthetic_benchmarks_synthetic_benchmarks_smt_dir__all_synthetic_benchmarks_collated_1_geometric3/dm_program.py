import sympy
from sympy import *

def pre_condition_0(c:sympy.Rational):
	#(y**2 < 63/64) & (c + y**2 - 47/64 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(63, 64)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-47, 64)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1(c:sympy.Rational):
	#c < 47/64

	pre_cond = StrictLessThan(Symbol('c'), Rational(47, 64))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_2(c:sympy.Rational):
	#(y**2 < 3/4) & (c + y**2 - 11/4 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(3, 4)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-11, 4)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_3(c:sympy.Rational):
	#c < 11/4

	pre_cond = StrictLessThan(Symbol('c'), Rational(11, 4))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_4(c:sympy.Rational):
	#(y**2 < 7/16) & (c + y**2 - 63/16 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(7, 16)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-63, 16)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_5(c:sympy.Rational):
	#c < 63/16

	pre_cond = StrictLessThan(Symbol('c'), Rational(63, 16))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_6(c:sympy.Rational):
	#(y**2 < 15/64) & (c + y**2 - 287/64 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(15, 64)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-287, 64)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_7(c:sympy.Rational):
	#c < 287/64

	pre_cond = StrictLessThan(Symbol('c'), Rational(287, 64))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_8(c:sympy.Rational):
	#(y**2 < 31/256) & (c + y**2 - 1215/256 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(31, 256)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1215, 256)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_9(c:sympy.Rational):
	#c < 1215/256

	pre_cond = StrictLessThan(Symbol('c'), Rational(1215, 256))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_10(c:sympy.Rational):
	#(y**2 < 63/1024) & (c + y**2 - 4991/1024 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(63, 1024)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-4991, 1024)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_11(c:sympy.Rational):
	#c < 4991/1024

	pre_cond = StrictLessThan(Symbol('c'), Rational(4991, 1024))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_12(c:sympy.Rational):
	#(y**2 < 127/4096) & (c + y**2 - 20223/4096 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(127, 4096)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-20223, 4096)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_13(c:sympy.Rational):
	#c < 20223/4096

	pre_cond = StrictLessThan(Symbol('c'), Rational(20223, 4096))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_14(c:sympy.Rational):
	#(y**2 < 255/16384) & (c + y**2 - 81407/16384 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(255, 16384)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-81407, 16384)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_15(c:sympy.Rational):
	#c < 81407/16384

	pre_cond = StrictLessThan(Symbol('c'), Rational(81407, 16384))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_16(c:sympy.Rational):
	#(y**2 < 511/65536) & (c + y**2 - 326655/65536 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(511, 65536)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-326655, 65536)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_17(c:sympy.Rational):
	#c < 326655/65536

	pre_cond = StrictLessThan(Symbol('c'), Rational(326655, 65536))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_18(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_19(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_20(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_21(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_22(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_23(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_24(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_25(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_26(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_27(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_28(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_29(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_30(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_31(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_32(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_33(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_34(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_35(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_36(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_37(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_38(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_39(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_40(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_41(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_42(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_43(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_44(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_45(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_46(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_47(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_48(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_49(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_50(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_51(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_52(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_53(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_54(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_55(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_56(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_57(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_58(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_59(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_60(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_61(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_62(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_63(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_64(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_65(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_66(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_67(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_68(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_69(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_70(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_71(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_72(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_73(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_74(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_75(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_76(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_77(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_78(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_79(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_80(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_81(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_82(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_83(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_84(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_85(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_86(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_87(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_88(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_89(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_90(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_91(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_92(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_93(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_94(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_95(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_96(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_97(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_98(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_99(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_100(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_101(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_102(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_103(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_104(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_105(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_106(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_107(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_108(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_109(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_110(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_111(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_112(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_113(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_114(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_115(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_116(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_117(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_118(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_119(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_120(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_121(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_122(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_123(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_124(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_125(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_126(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_127(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_128(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_129(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_130(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_131(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_132(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_133(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_134(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_135(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_136(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_137(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_138(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_139(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_140(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_141(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_142(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_143(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_144(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_145(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_146(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_147(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_148(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_149(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_150(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_151(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_152(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_153(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_154(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_155(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_156(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_157(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_158(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_159(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_160(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_161(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_162(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_163(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_164(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_165(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_166(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_167(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_168(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_169(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_170(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_171(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_172(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_173(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_174(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_175(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_176(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_177(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_178(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_179(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_180(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_181(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_182(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_183(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_184(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_185(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_186(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_187(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_188(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_189(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_190(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_191(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_192(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_193(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_194(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_195(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_196(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_197(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_198(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_199(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_200(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_201(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_202(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_203(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_204(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_205(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_206(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_207(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_208(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_209(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_210(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_211(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_212(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_213(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_214(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_215(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_216(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_217(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_218(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_219(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_220(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_221(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_222(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_223(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_224(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_225(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_226(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_227(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_228(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_229(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_230(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_231(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_232(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_233(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_234(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_235(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_236(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_237(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_238(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_239(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_240(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_241(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_242(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_243(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_244(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_245(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_246(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_247(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_248(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_249(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_250(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_251(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_252(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_253(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_254(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_255(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_256(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_257(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_258(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_259(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_260(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_261(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_262(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_263(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_264(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_265(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_266(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_267(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_268(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_269(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_270(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_271(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_272(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_273(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_274(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_275(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_276(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_277(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_278(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_279(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_280(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_281(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_282(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_283(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_284(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_285(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_286(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_287(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_288(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_289(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_290(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_291(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_292(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_293(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_294(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_295(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_296(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_297(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_298(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_299(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_300(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_301(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_302(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_303(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_304(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_305(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_306(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_307(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_308(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_309(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_310(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_311(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_312(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_313(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_314(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_315(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_316(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_317(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_318(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_319(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_320(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_321(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_322(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_323(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_324(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_325(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_326(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_327(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_328(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_329(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_330(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_331(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_332(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_333(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_334(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_335(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_336(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_337(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_338(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_339(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_340(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_341(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_342(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_343(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_344(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_345(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_346(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_347(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_348(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_349(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_350(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_351(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_352(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_353(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_354(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_355(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_356(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_357(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_358(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_359(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_360(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_361(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_362(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_363(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_364(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_365(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_366(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_367(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_368(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_369(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_370(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_371(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_372(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_373(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_374(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_375(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_376(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_377(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_378(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_379(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_380(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_381(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_382(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_383(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_384(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_385(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_386(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_387(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_388(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_389(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_390(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_391(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_392(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_393(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_394(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_395(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_396(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_397(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_398(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_399(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_400(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_401(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_402(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_403(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_404(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_405(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_406(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_407(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_408(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_409(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_410(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_411(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_412(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_413(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_414(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_415(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_416(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_417(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_418(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_419(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_420(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_421(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_422(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_423(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_424(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_425(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_426(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_427(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_428(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_429(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_430(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_431(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_432(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_433(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_434(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_435(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_436(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_437(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_438(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_439(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_440(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_441(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_442(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_443(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_444(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_445(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_446(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_447(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_448(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_449(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_450(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_451(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_452(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_453(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_454(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_455(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_456(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_457(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_458(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_459(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_460(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_461(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_462(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_463(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_464(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_465(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_466(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_467(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_468(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_469(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_470(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_471(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_472(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_473(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_474(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_475(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_476(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_477(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_478(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_479(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_480(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_481(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_482(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_483(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_484(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_485(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_486(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_487(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_488(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_489(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_490(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_491(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_492(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_493(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_494(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_495(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_496(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_497(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_498(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_499(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_500(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_501(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_502(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_503(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_504(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_505(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_506(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_507(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_508(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_509(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_510(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_511(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_512(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_513(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_514(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_515(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_516(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_517(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_518(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_519(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_520(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_521(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_522(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_523(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_524(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_525(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_526(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_527(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_528(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_529(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_530(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_531(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_532(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_533(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_534(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_535(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_536(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_537(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_538(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_539(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_540(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_541(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_542(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_543(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_544(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_545(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_546(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_547(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_548(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_549(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_550(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_551(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_552(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_553(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_554(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_555(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_556(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_557(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_558(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_559(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_560(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_561(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_562(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_563(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_564(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_565(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_566(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_567(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_568(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_569(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_570(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_571(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_572(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_573(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_574(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_575(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_576(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_577(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_578(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_579(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_580(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_581(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_582(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_583(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_584(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_585(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_586(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_587(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_588(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_589(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_590(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_591(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_592(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_593(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_594(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_595(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_596(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_597(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_598(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_599(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_600(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_601(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_602(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_603(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_604(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_605(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_606(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_607(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_608(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_609(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_610(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_611(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_612(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_613(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_614(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_615(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_616(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_617(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_618(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_619(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_620(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_621(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_622(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_623(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_624(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_625(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_626(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_627(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_628(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_629(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_630(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_631(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_632(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_633(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_634(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_635(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_636(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_637(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_638(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_639(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_640(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_641(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_642(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_643(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_644(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_645(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_646(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_647(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_648(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_649(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_650(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_651(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_652(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_653(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_654(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_655(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_656(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_657(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_658(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_659(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_660(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_661(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_662(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_663(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_664(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_665(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_666(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_667(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_668(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_669(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_670(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_671(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_672(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_673(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_674(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_675(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_676(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_677(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_678(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_679(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_680(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_681(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_682(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_683(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_684(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_685(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_686(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_687(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_688(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_689(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_690(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_691(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_692(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_693(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_694(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_695(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_696(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_697(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_698(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_699(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_700(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_701(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_702(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_703(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_704(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_705(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_706(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_707(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_708(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_709(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_710(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_711(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_712(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_713(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_714(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_715(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_716(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_717(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_718(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_719(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_720(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_721(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_722(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_723(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_724(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_725(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_726(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_727(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_728(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_729(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_730(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_731(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_732(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_733(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_734(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_735(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_736(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_737(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_738(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_739(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_740(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_741(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_742(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_743(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_744(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_745(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_746(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_747(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_748(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_749(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_750(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_751(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_752(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_753(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_754(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_755(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_756(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_757(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_758(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_759(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_760(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_761(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_762(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_763(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_764(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_765(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_766(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_767(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_768(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_769(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_770(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_771(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_772(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_773(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_774(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_775(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_776(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_777(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_778(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_779(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_780(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_781(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_782(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_783(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_784(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_785(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_786(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_787(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_788(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_789(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_790(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_791(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_792(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_793(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_794(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_795(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_796(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_797(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_798(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_799(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_800(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_801(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_802(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_803(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_804(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_805(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_806(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_807(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_808(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_809(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_810(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_811(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_812(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_813(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_814(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_815(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_816(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_817(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_818(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_819(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_820(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_821(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_822(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_823(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_824(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_825(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_826(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_827(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_828(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_829(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_830(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_831(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_832(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_833(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_834(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_835(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_836(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_837(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_838(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_839(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_840(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_841(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_842(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_843(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_844(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_845(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_846(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_847(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_848(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_849(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_850(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_851(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_852(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_853(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_854(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_855(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_856(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_857(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_858(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_859(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_860(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_861(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_862(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_863(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_864(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_865(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_866(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_867(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_868(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_869(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_870(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_871(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_872(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_873(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_874(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_875(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_876(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_877(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_878(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_879(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_880(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_881(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_882(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_883(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_884(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_885(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_886(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_887(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_888(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_889(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_890(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_891(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_892(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_893(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_894(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_895(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_896(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_897(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_898(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_899(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_900(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_901(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_902(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_903(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_904(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_905(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_906(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_907(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_908(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_909(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_910(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_911(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_912(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_913(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_914(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_915(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_916(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_917(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_918(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_919(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_920(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_921(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_922(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_923(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_924(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_925(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_926(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_927(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_928(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_929(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_930(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_931(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_932(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_933(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_934(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_935(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_936(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_937(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_938(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_939(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_940(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_941(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_942(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_943(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_944(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_945(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_946(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_947(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_948(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_949(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_950(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_951(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_952(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_953(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_954(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_955(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_956(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_957(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_958(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_959(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_960(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_961(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_962(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_963(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_964(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_965(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_966(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_967(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_968(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_969(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_970(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_971(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_972(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_973(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_974(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_975(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_976(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_977(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_978(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_979(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_980(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_981(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_982(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_983(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_984(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_985(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_986(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_987(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_988(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_989(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_990(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_991(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_992(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_993(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_994(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_995(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_996(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_997(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_998(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_999(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1000(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1001(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1002(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1003(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1004(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1005(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1006(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1007(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1008(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1009(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1010(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1011(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1012(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1013(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1014(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1015(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1016(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1017(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1018(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1019(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1020(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1021(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1022(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1023(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1024(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1025(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1026(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1027(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1028(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1029(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1030(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1031(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1032(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1033(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1034(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1035(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1036(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1037(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1038(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1039(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1040(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1041(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1042(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1043(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1044(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1045(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1046(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1047(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1048(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1049(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1050(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1051(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1052(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1053(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1054(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1055(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1056(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1057(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1058(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1059(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1060(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1061(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1062(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1063(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1064(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1065(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1066(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1067(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1068(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1069(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1070(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1071(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1072(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1073(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1074(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1075(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1076(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1077(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1078(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1079(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1080(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1081(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1082(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1083(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1084(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1085(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1086(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1087(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1088(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1089(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1090(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1091(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1092(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1093(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1094(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1095(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1096(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1097(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1098(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1099(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1100(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1101(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1102(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1103(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1104(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1105(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1106(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1107(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1108(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1109(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1110(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1111(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1112(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1113(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1114(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1115(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1116(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1117(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1118(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1119(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1120(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1121(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1122(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1123(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1124(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1125(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1126(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1127(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1128(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1129(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1130(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1131(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1132(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1133(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1134(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1135(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1136(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1137(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1138(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1139(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1140(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1141(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1142(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1143(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1144(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1145(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1146(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1147(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1148(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1149(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1150(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1151(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1152(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1153(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1154(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1155(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1156(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1157(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1158(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1159(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1160(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1161(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1162(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1163(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1164(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1165(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1166(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1167(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1168(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1169(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1170(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1171(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1172(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1173(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1174(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1175(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1176(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1177(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1178(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1179(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1180(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1181(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1182(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1183(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1184(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1185(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1186(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1187(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1188(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1189(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1190(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1191(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1192(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1193(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1194(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1195(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1196(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1197(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1198(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1199(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1200(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1201(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1202(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1203(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1204(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1205(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1206(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1207(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1208(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1209(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1210(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1211(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1212(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1213(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1214(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1215(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1216(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1217(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1218(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1219(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1220(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1221(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1222(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1223(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1224(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1225(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1226(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1227(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1228(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1229(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1230(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1231(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1232(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1233(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1234(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1235(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1236(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1237(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1238(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1239(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1240(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1241(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1242(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1243(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1244(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1245(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1246(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1247(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1248(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1249(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1250(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1251(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1252(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1253(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1254(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1255(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1256(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1257(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1258(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1259(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1260(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1261(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1262(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1263(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1264(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1265(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1266(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1267(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1268(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1269(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1270(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1271(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1272(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1273(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1274(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1275(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1276(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1277(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1278(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1279(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1280(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1281(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1282(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1283(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1284(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1285(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1286(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1287(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1288(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1289(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1290(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1291(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1292(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1293(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1294(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1295(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1296(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1297(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1298(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1299(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1300(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1301(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1302(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1303(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1304(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1305(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1306(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1307(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1308(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1309(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1310(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1311(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1312(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1313(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1314(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1315(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1316(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1317(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1318(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1319(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1320(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1321(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1322(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1323(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1324(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1325(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1326(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1327(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1328(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1329(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1330(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1331(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1332(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1333(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1334(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1335(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1336(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1337(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1338(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1339(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1340(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1341(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1342(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1343(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1344(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1345(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1346(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1347(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1348(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1349(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1350(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1351(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1352(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1353(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1354(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1355(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1356(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1357(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1358(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1359(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1360(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1361(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1362(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1363(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1364(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1365(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1366(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1367(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1368(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1369(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1370(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1371(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1372(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1373(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1374(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1375(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1376(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1377(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1378(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1379(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1380(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1381(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1382(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1383(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1384(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1385(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1386(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1387(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1388(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1389(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1390(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1391(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1392(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1393(c:sympy.Rational):
	#c < 1308671/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1308671, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1394(c:sympy.Rational):
	#(y**2 < 1023/262144) & (c + y**2 - 1308671/262144 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(2)), Rational(1023, 262144)), StrictLessThan(Add(Symbol('c'), Pow(Symbol('y'), Integer(2)), Rational(-1308671, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def post_condition(c:sympy.Rational, x:sympy.Rational, y:sympy.Rational):
	# (0 > x**2 + y**2 - 1) & (0 > c + x**2 - 6*x + y**2)

	post_cond =  And(StrictGreaterThan(Integer(0), Add(Pow(Symbol('x'), Integer(2)), Pow(Symbol('y'), Integer(2)), Integer(-1))), StrictGreaterThan(Integer(0), Add(Symbol('c'), Pow(Symbol('x'), Integer(2)), Mul(Integer(-1), Integer(6), Symbol('x')), Pow(Symbol('y'), Integer(2)))))

	eval = post_cond.subs( { 'c':c, 'x':x, 'y':y })

	return eval == sympy.logic.boolalg.BooleanTrue





if __name__=="__main__":
	
	ip_0=int(input("enter integer numerator of c:\n"))
	ip_1=int(input("enter integer denominator of c:\n"))
	assert(ip_1!=0), ("Error denominator entered is 0")
	c=sympy.Rational(ip_0,ip_1)
	
	
	
	
	if pre_condition_0(c=c)==True:
		print("pre_condition_0 SAT")
		print('x = 1/8')
		print('y = 0')
		print('c = -17/64')
		exit(0)
	
	
	if pre_condition_1(c=c)==True:
		print("pre_condition_1 SAT")
		print('x = 1/8')
		print('y = 0')
		print('c = -17/64')
		exit(0)
	
	
	if pre_condition_2(c=c)==True:
		print("pre_condition_2 SAT")
		print('x = 1/2')
		print('y = 0')
		print('c = 1')
		exit(0)
	
	
	if pre_condition_3(c=c)==True:
		print("pre_condition_3 SAT")
		print('x = 1/2')
		print('y = 0')
		print('c = 1')
		exit(0)
	
	
	if pre_condition_4(c=c)==True:
		print("pre_condition_4 SAT")
		print('x = 3/4')
		print('y = 0')
		print('c = 3')
		exit(0)
	
	
	if pre_condition_5(c=c)==True:
		print("pre_condition_5 SAT")
		print('x = 3/4')
		print('y = 0')
		print('c = 3')
		exit(0)
	
	
	if pre_condition_6(c=c)==True:
		print("pre_condition_6 SAT")
		print('x = 7/8')
		print('y = 0')
		print('c = 4')
		exit(0)
	
	
	if pre_condition_7(c=c)==True:
		print("pre_condition_7 SAT")
		print('x = 7/8')
		print('y = 0')
		print('c = 4')
		exit(0)
	
	
	if pre_condition_8(c=c)==True:
		print("pre_condition_8 SAT")
		print('x = 15/16')
		print('y = 0')
		print('c = 9/2')
		exit(0)
	
	
	if pre_condition_9(c=c)==True:
		print("pre_condition_9 SAT")
		print('x = 15/16')
		print('y = 0')
		print('c = 9/2')
		exit(0)
	
	
	if pre_condition_10(c=c)==True:
		print("pre_condition_10 SAT")
		print('x = 31/32')
		print('y = 0')
		print('c = 19/4')
		exit(0)
	
	
	if pre_condition_11(c=c)==True:
		print("pre_condition_11 SAT")
		print('x = 31/32')
		print('y = 0')
		print('c = 19/4')
		exit(0)
	
	
	if pre_condition_12(c=c)==True:
		print("pre_condition_12 SAT")
		print('x = 63/64')
		print('y = 0')
		print('c = 39/8')
		exit(0)
	
	
	if pre_condition_13(c=c)==True:
		print("pre_condition_13 SAT")
		print('x = 63/64')
		print('y = 0')
		print('c = 39/8')
		exit(0)
	
	
	if pre_condition_14(c=c)==True:
		print("pre_condition_14 SAT")
		print('x = 127/128')
		print('y = 0')
		print('c = 79/16')
		exit(0)
	
	
	if pre_condition_15(c=c)==True:
		print("pre_condition_15 SAT")
		print('x = 127/128')
		print('y = 0')
		print('c = 79/16')
		exit(0)
	
	
	if pre_condition_16(c=c)==True:
		print("pre_condition_16 SAT")
		print('x = 255/256')
		print('y = 0')
		print('c = 159/32')
		exit(0)
	
	
	if pre_condition_17(c=c)==True:
		print("pre_condition_17 SAT")
		print('x = 255/256')
		print('y = 0')
		print('c = 159/32')
		exit(0)
	
	
	if pre_condition_18(c=c)==True:
		print("pre_condition_18 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 319/64')
		exit(0)
	
	
	if pre_condition_19(c=c)==True:
		print("pre_condition_19 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 319/64')
		exit(0)
	
	
	if pre_condition_20(c=c)==True:
		print("pre_condition_20 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_21(c=c)==True:
		print("pre_condition_21 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_22(c=c)==True:
		print("pre_condition_22 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_23(c=c)==True:
		print("pre_condition_23 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_24(c=c)==True:
		print("pre_condition_24 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_25(c=c)==True:
		print("pre_condition_25 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_26(c=c)==True:
		print("pre_condition_26 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_27(c=c)==True:
		print("pre_condition_27 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_28(c=c)==True:
		print("pre_condition_28 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_29(c=c)==True:
		print("pre_condition_29 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_30(c=c)==True:
		print("pre_condition_30 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_31(c=c)==True:
		print("pre_condition_31 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_32(c=c)==True:
		print("pre_condition_32 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_33(c=c)==True:
		print("pre_condition_33 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_34(c=c)==True:
		print("pre_condition_34 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_35(c=c)==True:
		print("pre_condition_35 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_36(c=c)==True:
		print("pre_condition_36 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_37(c=c)==True:
		print("pre_condition_37 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_38(c=c)==True:
		print("pre_condition_38 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_39(c=c)==True:
		print("pre_condition_39 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_40(c=c)==True:
		print("pre_condition_40 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_41(c=c)==True:
		print("pre_condition_41 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_42(c=c)==True:
		print("pre_condition_42 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_43(c=c)==True:
		print("pre_condition_43 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_44(c=c)==True:
		print("pre_condition_44 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_45(c=c)==True:
		print("pre_condition_45 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_46(c=c)==True:
		print("pre_condition_46 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_47(c=c)==True:
		print("pre_condition_47 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_48(c=c)==True:
		print("pre_condition_48 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_49(c=c)==True:
		print("pre_condition_49 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_50(c=c)==True:
		print("pre_condition_50 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_51(c=c)==True:
		print("pre_condition_51 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_52(c=c)==True:
		print("pre_condition_52 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_53(c=c)==True:
		print("pre_condition_53 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_54(c=c)==True:
		print("pre_condition_54 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_55(c=c)==True:
		print("pre_condition_55 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_56(c=c)==True:
		print("pre_condition_56 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_57(c=c)==True:
		print("pre_condition_57 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_58(c=c)==True:
		print("pre_condition_58 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_59(c=c)==True:
		print("pre_condition_59 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_60(c=c)==True:
		print("pre_condition_60 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_61(c=c)==True:
		print("pre_condition_61 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_62(c=c)==True:
		print("pre_condition_62 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_63(c=c)==True:
		print("pre_condition_63 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_64(c=c)==True:
		print("pre_condition_64 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_65(c=c)==True:
		print("pre_condition_65 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_66(c=c)==True:
		print("pre_condition_66 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_67(c=c)==True:
		print("pre_condition_67 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_68(c=c)==True:
		print("pre_condition_68 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_69(c=c)==True:
		print("pre_condition_69 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_70(c=c)==True:
		print("pre_condition_70 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_71(c=c)==True:
		print("pre_condition_71 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_72(c=c)==True:
		print("pre_condition_72 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_73(c=c)==True:
		print("pre_condition_73 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_74(c=c)==True:
		print("pre_condition_74 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_75(c=c)==True:
		print("pre_condition_75 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_76(c=c)==True:
		print("pre_condition_76 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_77(c=c)==True:
		print("pre_condition_77 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_78(c=c)==True:
		print("pre_condition_78 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_79(c=c)==True:
		print("pre_condition_79 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_80(c=c)==True:
		print("pre_condition_80 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_81(c=c)==True:
		print("pre_condition_81 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_82(c=c)==True:
		print("pre_condition_82 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_83(c=c)==True:
		print("pre_condition_83 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_84(c=c)==True:
		print("pre_condition_84 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_85(c=c)==True:
		print("pre_condition_85 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_86(c=c)==True:
		print("pre_condition_86 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_87(c=c)==True:
		print("pre_condition_87 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_88(c=c)==True:
		print("pre_condition_88 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_89(c=c)==True:
		print("pre_condition_89 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_90(c=c)==True:
		print("pre_condition_90 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_91(c=c)==True:
		print("pre_condition_91 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_92(c=c)==True:
		print("pre_condition_92 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_93(c=c)==True:
		print("pre_condition_93 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_94(c=c)==True:
		print("pre_condition_94 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_95(c=c)==True:
		print("pre_condition_95 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_96(c=c)==True:
		print("pre_condition_96 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_97(c=c)==True:
		print("pre_condition_97 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_98(c=c)==True:
		print("pre_condition_98 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_99(c=c)==True:
		print("pre_condition_99 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_100(c=c)==True:
		print("pre_condition_100 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_101(c=c)==True:
		print("pre_condition_101 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_102(c=c)==True:
		print("pre_condition_102 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_103(c=c)==True:
		print("pre_condition_103 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_104(c=c)==True:
		print("pre_condition_104 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_105(c=c)==True:
		print("pre_condition_105 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_106(c=c)==True:
		print("pre_condition_106 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_107(c=c)==True:
		print("pre_condition_107 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_108(c=c)==True:
		print("pre_condition_108 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_109(c=c)==True:
		print("pre_condition_109 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_110(c=c)==True:
		print("pre_condition_110 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_111(c=c)==True:
		print("pre_condition_111 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_112(c=c)==True:
		print("pre_condition_112 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_113(c=c)==True:
		print("pre_condition_113 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_114(c=c)==True:
		print("pre_condition_114 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_115(c=c)==True:
		print("pre_condition_115 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_116(c=c)==True:
		print("pre_condition_116 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_117(c=c)==True:
		print("pre_condition_117 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_118(c=c)==True:
		print("pre_condition_118 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_119(c=c)==True:
		print("pre_condition_119 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_120(c=c)==True:
		print("pre_condition_120 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_121(c=c)==True:
		print("pre_condition_121 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_122(c=c)==True:
		print("pre_condition_122 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_123(c=c)==True:
		print("pre_condition_123 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_124(c=c)==True:
		print("pre_condition_124 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_125(c=c)==True:
		print("pre_condition_125 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_126(c=c)==True:
		print("pre_condition_126 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_127(c=c)==True:
		print("pre_condition_127 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_128(c=c)==True:
		print("pre_condition_128 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_129(c=c)==True:
		print("pre_condition_129 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_130(c=c)==True:
		print("pre_condition_130 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_131(c=c)==True:
		print("pre_condition_131 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_132(c=c)==True:
		print("pre_condition_132 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_133(c=c)==True:
		print("pre_condition_133 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_134(c=c)==True:
		print("pre_condition_134 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_135(c=c)==True:
		print("pre_condition_135 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_136(c=c)==True:
		print("pre_condition_136 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_137(c=c)==True:
		print("pre_condition_137 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_138(c=c)==True:
		print("pre_condition_138 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_139(c=c)==True:
		print("pre_condition_139 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_140(c=c)==True:
		print("pre_condition_140 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_141(c=c)==True:
		print("pre_condition_141 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_142(c=c)==True:
		print("pre_condition_142 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_143(c=c)==True:
		print("pre_condition_143 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_144(c=c)==True:
		print("pre_condition_144 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_145(c=c)==True:
		print("pre_condition_145 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_146(c=c)==True:
		print("pre_condition_146 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_147(c=c)==True:
		print("pre_condition_147 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_148(c=c)==True:
		print("pre_condition_148 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_149(c=c)==True:
		print("pre_condition_149 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_150(c=c)==True:
		print("pre_condition_150 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_151(c=c)==True:
		print("pre_condition_151 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_152(c=c)==True:
		print("pre_condition_152 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_153(c=c)==True:
		print("pre_condition_153 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_154(c=c)==True:
		print("pre_condition_154 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_155(c=c)==True:
		print("pre_condition_155 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_156(c=c)==True:
		print("pre_condition_156 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_157(c=c)==True:
		print("pre_condition_157 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_158(c=c)==True:
		print("pre_condition_158 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_159(c=c)==True:
		print("pre_condition_159 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_160(c=c)==True:
		print("pre_condition_160 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_161(c=c)==True:
		print("pre_condition_161 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_162(c=c)==True:
		print("pre_condition_162 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_163(c=c)==True:
		print("pre_condition_163 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_164(c=c)==True:
		print("pre_condition_164 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_165(c=c)==True:
		print("pre_condition_165 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_166(c=c)==True:
		print("pre_condition_166 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_167(c=c)==True:
		print("pre_condition_167 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_168(c=c)==True:
		print("pre_condition_168 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_169(c=c)==True:
		print("pre_condition_169 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_170(c=c)==True:
		print("pre_condition_170 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_171(c=c)==True:
		print("pre_condition_171 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_172(c=c)==True:
		print("pre_condition_172 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_173(c=c)==True:
		print("pre_condition_173 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_174(c=c)==True:
		print("pre_condition_174 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_175(c=c)==True:
		print("pre_condition_175 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_176(c=c)==True:
		print("pre_condition_176 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_177(c=c)==True:
		print("pre_condition_177 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_178(c=c)==True:
		print("pre_condition_178 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_179(c=c)==True:
		print("pre_condition_179 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_180(c=c)==True:
		print("pre_condition_180 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_181(c=c)==True:
		print("pre_condition_181 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_182(c=c)==True:
		print("pre_condition_182 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_183(c=c)==True:
		print("pre_condition_183 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_184(c=c)==True:
		print("pre_condition_184 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_185(c=c)==True:
		print("pre_condition_185 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_186(c=c)==True:
		print("pre_condition_186 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_187(c=c)==True:
		print("pre_condition_187 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_188(c=c)==True:
		print("pre_condition_188 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_189(c=c)==True:
		print("pre_condition_189 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_190(c=c)==True:
		print("pre_condition_190 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_191(c=c)==True:
		print("pre_condition_191 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_192(c=c)==True:
		print("pre_condition_192 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_193(c=c)==True:
		print("pre_condition_193 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_194(c=c)==True:
		print("pre_condition_194 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_195(c=c)==True:
		print("pre_condition_195 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_196(c=c)==True:
		print("pre_condition_196 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_197(c=c)==True:
		print("pre_condition_197 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_198(c=c)==True:
		print("pre_condition_198 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_199(c=c)==True:
		print("pre_condition_199 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_200(c=c)==True:
		print("pre_condition_200 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_201(c=c)==True:
		print("pre_condition_201 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_202(c=c)==True:
		print("pre_condition_202 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_203(c=c)==True:
		print("pre_condition_203 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_204(c=c)==True:
		print("pre_condition_204 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_205(c=c)==True:
		print("pre_condition_205 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_206(c=c)==True:
		print("pre_condition_206 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_207(c=c)==True:
		print("pre_condition_207 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_208(c=c)==True:
		print("pre_condition_208 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_209(c=c)==True:
		print("pre_condition_209 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_210(c=c)==True:
		print("pre_condition_210 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_211(c=c)==True:
		print("pre_condition_211 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_212(c=c)==True:
		print("pre_condition_212 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_213(c=c)==True:
		print("pre_condition_213 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_214(c=c)==True:
		print("pre_condition_214 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_215(c=c)==True:
		print("pre_condition_215 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_216(c=c)==True:
		print("pre_condition_216 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_217(c=c)==True:
		print("pre_condition_217 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_218(c=c)==True:
		print("pre_condition_218 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_219(c=c)==True:
		print("pre_condition_219 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_220(c=c)==True:
		print("pre_condition_220 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_221(c=c)==True:
		print("pre_condition_221 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_222(c=c)==True:
		print("pre_condition_222 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_223(c=c)==True:
		print("pre_condition_223 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_224(c=c)==True:
		print("pre_condition_224 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_225(c=c)==True:
		print("pre_condition_225 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_226(c=c)==True:
		print("pre_condition_226 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_227(c=c)==True:
		print("pre_condition_227 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_228(c=c)==True:
		print("pre_condition_228 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_229(c=c)==True:
		print("pre_condition_229 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_230(c=c)==True:
		print("pre_condition_230 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_231(c=c)==True:
		print("pre_condition_231 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_232(c=c)==True:
		print("pre_condition_232 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_233(c=c)==True:
		print("pre_condition_233 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_234(c=c)==True:
		print("pre_condition_234 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_235(c=c)==True:
		print("pre_condition_235 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_236(c=c)==True:
		print("pre_condition_236 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_237(c=c)==True:
		print("pre_condition_237 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_238(c=c)==True:
		print("pre_condition_238 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_239(c=c)==True:
		print("pre_condition_239 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_240(c=c)==True:
		print("pre_condition_240 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_241(c=c)==True:
		print("pre_condition_241 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_242(c=c)==True:
		print("pre_condition_242 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_243(c=c)==True:
		print("pre_condition_243 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_244(c=c)==True:
		print("pre_condition_244 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_245(c=c)==True:
		print("pre_condition_245 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_246(c=c)==True:
		print("pre_condition_246 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_247(c=c)==True:
		print("pre_condition_247 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_248(c=c)==True:
		print("pre_condition_248 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_249(c=c)==True:
		print("pre_condition_249 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_250(c=c)==True:
		print("pre_condition_250 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_251(c=c)==True:
		print("pre_condition_251 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_252(c=c)==True:
		print("pre_condition_252 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_253(c=c)==True:
		print("pre_condition_253 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_254(c=c)==True:
		print("pre_condition_254 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_255(c=c)==True:
		print("pre_condition_255 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_256(c=c)==True:
		print("pre_condition_256 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_257(c=c)==True:
		print("pre_condition_257 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_258(c=c)==True:
		print("pre_condition_258 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_259(c=c)==True:
		print("pre_condition_259 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_260(c=c)==True:
		print("pre_condition_260 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_261(c=c)==True:
		print("pre_condition_261 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_262(c=c)==True:
		print("pre_condition_262 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_263(c=c)==True:
		print("pre_condition_263 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_264(c=c)==True:
		print("pre_condition_264 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_265(c=c)==True:
		print("pre_condition_265 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_266(c=c)==True:
		print("pre_condition_266 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_267(c=c)==True:
		print("pre_condition_267 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_268(c=c)==True:
		print("pre_condition_268 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_269(c=c)==True:
		print("pre_condition_269 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_270(c=c)==True:
		print("pre_condition_270 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_271(c=c)==True:
		print("pre_condition_271 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_272(c=c)==True:
		print("pre_condition_272 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_273(c=c)==True:
		print("pre_condition_273 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_274(c=c)==True:
		print("pre_condition_274 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_275(c=c)==True:
		print("pre_condition_275 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_276(c=c)==True:
		print("pre_condition_276 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_277(c=c)==True:
		print("pre_condition_277 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_278(c=c)==True:
		print("pre_condition_278 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_279(c=c)==True:
		print("pre_condition_279 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_280(c=c)==True:
		print("pre_condition_280 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_281(c=c)==True:
		print("pre_condition_281 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_282(c=c)==True:
		print("pre_condition_282 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_283(c=c)==True:
		print("pre_condition_283 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_284(c=c)==True:
		print("pre_condition_284 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_285(c=c)==True:
		print("pre_condition_285 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_286(c=c)==True:
		print("pre_condition_286 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_287(c=c)==True:
		print("pre_condition_287 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_288(c=c)==True:
		print("pre_condition_288 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_289(c=c)==True:
		print("pre_condition_289 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_290(c=c)==True:
		print("pre_condition_290 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_291(c=c)==True:
		print("pre_condition_291 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_292(c=c)==True:
		print("pre_condition_292 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_293(c=c)==True:
		print("pre_condition_293 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_294(c=c)==True:
		print("pre_condition_294 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_295(c=c)==True:
		print("pre_condition_295 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_296(c=c)==True:
		print("pre_condition_296 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_297(c=c)==True:
		print("pre_condition_297 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_298(c=c)==True:
		print("pre_condition_298 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_299(c=c)==True:
		print("pre_condition_299 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_300(c=c)==True:
		print("pre_condition_300 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_301(c=c)==True:
		print("pre_condition_301 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_302(c=c)==True:
		print("pre_condition_302 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_303(c=c)==True:
		print("pre_condition_303 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_304(c=c)==True:
		print("pre_condition_304 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_305(c=c)==True:
		print("pre_condition_305 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_306(c=c)==True:
		print("pre_condition_306 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_307(c=c)==True:
		print("pre_condition_307 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_308(c=c)==True:
		print("pre_condition_308 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_309(c=c)==True:
		print("pre_condition_309 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_310(c=c)==True:
		print("pre_condition_310 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_311(c=c)==True:
		print("pre_condition_311 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_312(c=c)==True:
		print("pre_condition_312 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_313(c=c)==True:
		print("pre_condition_313 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_314(c=c)==True:
		print("pre_condition_314 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_315(c=c)==True:
		print("pre_condition_315 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_316(c=c)==True:
		print("pre_condition_316 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_317(c=c)==True:
		print("pre_condition_317 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_318(c=c)==True:
		print("pre_condition_318 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_319(c=c)==True:
		print("pre_condition_319 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_320(c=c)==True:
		print("pre_condition_320 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_321(c=c)==True:
		print("pre_condition_321 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_322(c=c)==True:
		print("pre_condition_322 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_323(c=c)==True:
		print("pre_condition_323 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_324(c=c)==True:
		print("pre_condition_324 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_325(c=c)==True:
		print("pre_condition_325 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_326(c=c)==True:
		print("pre_condition_326 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_327(c=c)==True:
		print("pre_condition_327 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_328(c=c)==True:
		print("pre_condition_328 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_329(c=c)==True:
		print("pre_condition_329 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_330(c=c)==True:
		print("pre_condition_330 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_331(c=c)==True:
		print("pre_condition_331 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_332(c=c)==True:
		print("pre_condition_332 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_333(c=c)==True:
		print("pre_condition_333 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_334(c=c)==True:
		print("pre_condition_334 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_335(c=c)==True:
		print("pre_condition_335 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_336(c=c)==True:
		print("pre_condition_336 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_337(c=c)==True:
		print("pre_condition_337 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_338(c=c)==True:
		print("pre_condition_338 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_339(c=c)==True:
		print("pre_condition_339 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_340(c=c)==True:
		print("pre_condition_340 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_341(c=c)==True:
		print("pre_condition_341 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_342(c=c)==True:
		print("pre_condition_342 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_343(c=c)==True:
		print("pre_condition_343 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_344(c=c)==True:
		print("pre_condition_344 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_345(c=c)==True:
		print("pre_condition_345 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_346(c=c)==True:
		print("pre_condition_346 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_347(c=c)==True:
		print("pre_condition_347 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_348(c=c)==True:
		print("pre_condition_348 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_349(c=c)==True:
		print("pre_condition_349 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_350(c=c)==True:
		print("pre_condition_350 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_351(c=c)==True:
		print("pre_condition_351 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_352(c=c)==True:
		print("pre_condition_352 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_353(c=c)==True:
		print("pre_condition_353 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_354(c=c)==True:
		print("pre_condition_354 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_355(c=c)==True:
		print("pre_condition_355 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_356(c=c)==True:
		print("pre_condition_356 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_357(c=c)==True:
		print("pre_condition_357 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_358(c=c)==True:
		print("pre_condition_358 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_359(c=c)==True:
		print("pre_condition_359 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_360(c=c)==True:
		print("pre_condition_360 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_361(c=c)==True:
		print("pre_condition_361 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_362(c=c)==True:
		print("pre_condition_362 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_363(c=c)==True:
		print("pre_condition_363 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_364(c=c)==True:
		print("pre_condition_364 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_365(c=c)==True:
		print("pre_condition_365 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_366(c=c)==True:
		print("pre_condition_366 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_367(c=c)==True:
		print("pre_condition_367 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_368(c=c)==True:
		print("pre_condition_368 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_369(c=c)==True:
		print("pre_condition_369 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_370(c=c)==True:
		print("pre_condition_370 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_371(c=c)==True:
		print("pre_condition_371 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_372(c=c)==True:
		print("pre_condition_372 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_373(c=c)==True:
		print("pre_condition_373 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_374(c=c)==True:
		print("pre_condition_374 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_375(c=c)==True:
		print("pre_condition_375 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_376(c=c)==True:
		print("pre_condition_376 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_377(c=c)==True:
		print("pre_condition_377 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_378(c=c)==True:
		print("pre_condition_378 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_379(c=c)==True:
		print("pre_condition_379 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_380(c=c)==True:
		print("pre_condition_380 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_381(c=c)==True:
		print("pre_condition_381 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_382(c=c)==True:
		print("pre_condition_382 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_383(c=c)==True:
		print("pre_condition_383 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_384(c=c)==True:
		print("pre_condition_384 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_385(c=c)==True:
		print("pre_condition_385 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_386(c=c)==True:
		print("pre_condition_386 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_387(c=c)==True:
		print("pre_condition_387 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_388(c=c)==True:
		print("pre_condition_388 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_389(c=c)==True:
		print("pre_condition_389 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_390(c=c)==True:
		print("pre_condition_390 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_391(c=c)==True:
		print("pre_condition_391 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_392(c=c)==True:
		print("pre_condition_392 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_393(c=c)==True:
		print("pre_condition_393 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_394(c=c)==True:
		print("pre_condition_394 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_395(c=c)==True:
		print("pre_condition_395 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_396(c=c)==True:
		print("pre_condition_396 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_397(c=c)==True:
		print("pre_condition_397 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_398(c=c)==True:
		print("pre_condition_398 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_399(c=c)==True:
		print("pre_condition_399 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_400(c=c)==True:
		print("pre_condition_400 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_401(c=c)==True:
		print("pre_condition_401 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_402(c=c)==True:
		print("pre_condition_402 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_403(c=c)==True:
		print("pre_condition_403 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_404(c=c)==True:
		print("pre_condition_404 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_405(c=c)==True:
		print("pre_condition_405 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_406(c=c)==True:
		print("pre_condition_406 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_407(c=c)==True:
		print("pre_condition_407 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_408(c=c)==True:
		print("pre_condition_408 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_409(c=c)==True:
		print("pre_condition_409 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_410(c=c)==True:
		print("pre_condition_410 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_411(c=c)==True:
		print("pre_condition_411 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_412(c=c)==True:
		print("pre_condition_412 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_413(c=c)==True:
		print("pre_condition_413 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_414(c=c)==True:
		print("pre_condition_414 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_415(c=c)==True:
		print("pre_condition_415 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_416(c=c)==True:
		print("pre_condition_416 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_417(c=c)==True:
		print("pre_condition_417 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_418(c=c)==True:
		print("pre_condition_418 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_419(c=c)==True:
		print("pre_condition_419 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_420(c=c)==True:
		print("pre_condition_420 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_421(c=c)==True:
		print("pre_condition_421 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_422(c=c)==True:
		print("pre_condition_422 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_423(c=c)==True:
		print("pre_condition_423 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_424(c=c)==True:
		print("pre_condition_424 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_425(c=c)==True:
		print("pre_condition_425 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_426(c=c)==True:
		print("pre_condition_426 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_427(c=c)==True:
		print("pre_condition_427 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_428(c=c)==True:
		print("pre_condition_428 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_429(c=c)==True:
		print("pre_condition_429 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_430(c=c)==True:
		print("pre_condition_430 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_431(c=c)==True:
		print("pre_condition_431 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_432(c=c)==True:
		print("pre_condition_432 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_433(c=c)==True:
		print("pre_condition_433 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_434(c=c)==True:
		print("pre_condition_434 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_435(c=c)==True:
		print("pre_condition_435 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_436(c=c)==True:
		print("pre_condition_436 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_437(c=c)==True:
		print("pre_condition_437 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_438(c=c)==True:
		print("pre_condition_438 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_439(c=c)==True:
		print("pre_condition_439 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_440(c=c)==True:
		print("pre_condition_440 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_441(c=c)==True:
		print("pre_condition_441 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_442(c=c)==True:
		print("pre_condition_442 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_443(c=c)==True:
		print("pre_condition_443 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_444(c=c)==True:
		print("pre_condition_444 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_445(c=c)==True:
		print("pre_condition_445 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_446(c=c)==True:
		print("pre_condition_446 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_447(c=c)==True:
		print("pre_condition_447 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_448(c=c)==True:
		print("pre_condition_448 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_449(c=c)==True:
		print("pre_condition_449 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_450(c=c)==True:
		print("pre_condition_450 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_451(c=c)==True:
		print("pre_condition_451 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_452(c=c)==True:
		print("pre_condition_452 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_453(c=c)==True:
		print("pre_condition_453 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_454(c=c)==True:
		print("pre_condition_454 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_455(c=c)==True:
		print("pre_condition_455 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_456(c=c)==True:
		print("pre_condition_456 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_457(c=c)==True:
		print("pre_condition_457 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_458(c=c)==True:
		print("pre_condition_458 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_459(c=c)==True:
		print("pre_condition_459 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_460(c=c)==True:
		print("pre_condition_460 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_461(c=c)==True:
		print("pre_condition_461 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_462(c=c)==True:
		print("pre_condition_462 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_463(c=c)==True:
		print("pre_condition_463 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_464(c=c)==True:
		print("pre_condition_464 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_465(c=c)==True:
		print("pre_condition_465 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_466(c=c)==True:
		print("pre_condition_466 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_467(c=c)==True:
		print("pre_condition_467 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_468(c=c)==True:
		print("pre_condition_468 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_469(c=c)==True:
		print("pre_condition_469 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_470(c=c)==True:
		print("pre_condition_470 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_471(c=c)==True:
		print("pre_condition_471 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_472(c=c)==True:
		print("pre_condition_472 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_473(c=c)==True:
		print("pre_condition_473 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_474(c=c)==True:
		print("pre_condition_474 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_475(c=c)==True:
		print("pre_condition_475 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_476(c=c)==True:
		print("pre_condition_476 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_477(c=c)==True:
		print("pre_condition_477 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_478(c=c)==True:
		print("pre_condition_478 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_479(c=c)==True:
		print("pre_condition_479 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_480(c=c)==True:
		print("pre_condition_480 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_481(c=c)==True:
		print("pre_condition_481 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_482(c=c)==True:
		print("pre_condition_482 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_483(c=c)==True:
		print("pre_condition_483 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_484(c=c)==True:
		print("pre_condition_484 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_485(c=c)==True:
		print("pre_condition_485 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_486(c=c)==True:
		print("pre_condition_486 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_487(c=c)==True:
		print("pre_condition_487 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_488(c=c)==True:
		print("pre_condition_488 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_489(c=c)==True:
		print("pre_condition_489 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_490(c=c)==True:
		print("pre_condition_490 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_491(c=c)==True:
		print("pre_condition_491 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_492(c=c)==True:
		print("pre_condition_492 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_493(c=c)==True:
		print("pre_condition_493 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_494(c=c)==True:
		print("pre_condition_494 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_495(c=c)==True:
		print("pre_condition_495 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_496(c=c)==True:
		print("pre_condition_496 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_497(c=c)==True:
		print("pre_condition_497 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_498(c=c)==True:
		print("pre_condition_498 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_499(c=c)==True:
		print("pre_condition_499 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_500(c=c)==True:
		print("pre_condition_500 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_501(c=c)==True:
		print("pre_condition_501 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_502(c=c)==True:
		print("pre_condition_502 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_503(c=c)==True:
		print("pre_condition_503 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_504(c=c)==True:
		print("pre_condition_504 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_505(c=c)==True:
		print("pre_condition_505 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_506(c=c)==True:
		print("pre_condition_506 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_507(c=c)==True:
		print("pre_condition_507 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_508(c=c)==True:
		print("pre_condition_508 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_509(c=c)==True:
		print("pre_condition_509 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_510(c=c)==True:
		print("pre_condition_510 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_511(c=c)==True:
		print("pre_condition_511 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_512(c=c)==True:
		print("pre_condition_512 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_513(c=c)==True:
		print("pre_condition_513 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_514(c=c)==True:
		print("pre_condition_514 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_515(c=c)==True:
		print("pre_condition_515 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_516(c=c)==True:
		print("pre_condition_516 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_517(c=c)==True:
		print("pre_condition_517 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_518(c=c)==True:
		print("pre_condition_518 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_519(c=c)==True:
		print("pre_condition_519 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_520(c=c)==True:
		print("pre_condition_520 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_521(c=c)==True:
		print("pre_condition_521 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_522(c=c)==True:
		print("pre_condition_522 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_523(c=c)==True:
		print("pre_condition_523 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_524(c=c)==True:
		print("pre_condition_524 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_525(c=c)==True:
		print("pre_condition_525 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_526(c=c)==True:
		print("pre_condition_526 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_527(c=c)==True:
		print("pre_condition_527 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_528(c=c)==True:
		print("pre_condition_528 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_529(c=c)==True:
		print("pre_condition_529 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_530(c=c)==True:
		print("pre_condition_530 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_531(c=c)==True:
		print("pre_condition_531 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_532(c=c)==True:
		print("pre_condition_532 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_533(c=c)==True:
		print("pre_condition_533 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_534(c=c)==True:
		print("pre_condition_534 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_535(c=c)==True:
		print("pre_condition_535 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_536(c=c)==True:
		print("pre_condition_536 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_537(c=c)==True:
		print("pre_condition_537 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_538(c=c)==True:
		print("pre_condition_538 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_539(c=c)==True:
		print("pre_condition_539 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_540(c=c)==True:
		print("pre_condition_540 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_541(c=c)==True:
		print("pre_condition_541 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_542(c=c)==True:
		print("pre_condition_542 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_543(c=c)==True:
		print("pre_condition_543 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_544(c=c)==True:
		print("pre_condition_544 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_545(c=c)==True:
		print("pre_condition_545 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_546(c=c)==True:
		print("pre_condition_546 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_547(c=c)==True:
		print("pre_condition_547 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_548(c=c)==True:
		print("pre_condition_548 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_549(c=c)==True:
		print("pre_condition_549 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_550(c=c)==True:
		print("pre_condition_550 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_551(c=c)==True:
		print("pre_condition_551 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_552(c=c)==True:
		print("pre_condition_552 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_553(c=c)==True:
		print("pre_condition_553 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_554(c=c)==True:
		print("pre_condition_554 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_555(c=c)==True:
		print("pre_condition_555 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_556(c=c)==True:
		print("pre_condition_556 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_557(c=c)==True:
		print("pre_condition_557 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_558(c=c)==True:
		print("pre_condition_558 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_559(c=c)==True:
		print("pre_condition_559 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_560(c=c)==True:
		print("pre_condition_560 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_561(c=c)==True:
		print("pre_condition_561 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_562(c=c)==True:
		print("pre_condition_562 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_563(c=c)==True:
		print("pre_condition_563 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_564(c=c)==True:
		print("pre_condition_564 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_565(c=c)==True:
		print("pre_condition_565 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_566(c=c)==True:
		print("pre_condition_566 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_567(c=c)==True:
		print("pre_condition_567 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_568(c=c)==True:
		print("pre_condition_568 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_569(c=c)==True:
		print("pre_condition_569 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_570(c=c)==True:
		print("pre_condition_570 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_571(c=c)==True:
		print("pre_condition_571 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_572(c=c)==True:
		print("pre_condition_572 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_573(c=c)==True:
		print("pre_condition_573 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_574(c=c)==True:
		print("pre_condition_574 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_575(c=c)==True:
		print("pre_condition_575 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_576(c=c)==True:
		print("pre_condition_576 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_577(c=c)==True:
		print("pre_condition_577 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_578(c=c)==True:
		print("pre_condition_578 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_579(c=c)==True:
		print("pre_condition_579 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_580(c=c)==True:
		print("pre_condition_580 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_581(c=c)==True:
		print("pre_condition_581 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_582(c=c)==True:
		print("pre_condition_582 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_583(c=c)==True:
		print("pre_condition_583 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_584(c=c)==True:
		print("pre_condition_584 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_585(c=c)==True:
		print("pre_condition_585 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_586(c=c)==True:
		print("pre_condition_586 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_587(c=c)==True:
		print("pre_condition_587 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_588(c=c)==True:
		print("pre_condition_588 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_589(c=c)==True:
		print("pre_condition_589 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_590(c=c)==True:
		print("pre_condition_590 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_591(c=c)==True:
		print("pre_condition_591 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_592(c=c)==True:
		print("pre_condition_592 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_593(c=c)==True:
		print("pre_condition_593 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_594(c=c)==True:
		print("pre_condition_594 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_595(c=c)==True:
		print("pre_condition_595 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_596(c=c)==True:
		print("pre_condition_596 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_597(c=c)==True:
		print("pre_condition_597 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_598(c=c)==True:
		print("pre_condition_598 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_599(c=c)==True:
		print("pre_condition_599 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_600(c=c)==True:
		print("pre_condition_600 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_601(c=c)==True:
		print("pre_condition_601 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_602(c=c)==True:
		print("pre_condition_602 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_603(c=c)==True:
		print("pre_condition_603 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_604(c=c)==True:
		print("pre_condition_604 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_605(c=c)==True:
		print("pre_condition_605 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_606(c=c)==True:
		print("pre_condition_606 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_607(c=c)==True:
		print("pre_condition_607 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_608(c=c)==True:
		print("pre_condition_608 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_609(c=c)==True:
		print("pre_condition_609 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_610(c=c)==True:
		print("pre_condition_610 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_611(c=c)==True:
		print("pre_condition_611 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_612(c=c)==True:
		print("pre_condition_612 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_613(c=c)==True:
		print("pre_condition_613 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_614(c=c)==True:
		print("pre_condition_614 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_615(c=c)==True:
		print("pre_condition_615 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_616(c=c)==True:
		print("pre_condition_616 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_617(c=c)==True:
		print("pre_condition_617 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_618(c=c)==True:
		print("pre_condition_618 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_619(c=c)==True:
		print("pre_condition_619 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_620(c=c)==True:
		print("pre_condition_620 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_621(c=c)==True:
		print("pre_condition_621 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_622(c=c)==True:
		print("pre_condition_622 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_623(c=c)==True:
		print("pre_condition_623 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_624(c=c)==True:
		print("pre_condition_624 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_625(c=c)==True:
		print("pre_condition_625 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_626(c=c)==True:
		print("pre_condition_626 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_627(c=c)==True:
		print("pre_condition_627 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_628(c=c)==True:
		print("pre_condition_628 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_629(c=c)==True:
		print("pre_condition_629 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_630(c=c)==True:
		print("pre_condition_630 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_631(c=c)==True:
		print("pre_condition_631 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_632(c=c)==True:
		print("pre_condition_632 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_633(c=c)==True:
		print("pre_condition_633 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_634(c=c)==True:
		print("pre_condition_634 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_635(c=c)==True:
		print("pre_condition_635 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_636(c=c)==True:
		print("pre_condition_636 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_637(c=c)==True:
		print("pre_condition_637 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_638(c=c)==True:
		print("pre_condition_638 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_639(c=c)==True:
		print("pre_condition_639 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_640(c=c)==True:
		print("pre_condition_640 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_641(c=c)==True:
		print("pre_condition_641 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_642(c=c)==True:
		print("pre_condition_642 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_643(c=c)==True:
		print("pre_condition_643 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_644(c=c)==True:
		print("pre_condition_644 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_645(c=c)==True:
		print("pre_condition_645 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_646(c=c)==True:
		print("pre_condition_646 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_647(c=c)==True:
		print("pre_condition_647 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_648(c=c)==True:
		print("pre_condition_648 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_649(c=c)==True:
		print("pre_condition_649 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_650(c=c)==True:
		print("pre_condition_650 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_651(c=c)==True:
		print("pre_condition_651 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_652(c=c)==True:
		print("pre_condition_652 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_653(c=c)==True:
		print("pre_condition_653 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_654(c=c)==True:
		print("pre_condition_654 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_655(c=c)==True:
		print("pre_condition_655 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_656(c=c)==True:
		print("pre_condition_656 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_657(c=c)==True:
		print("pre_condition_657 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_658(c=c)==True:
		print("pre_condition_658 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_659(c=c)==True:
		print("pre_condition_659 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_660(c=c)==True:
		print("pre_condition_660 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_661(c=c)==True:
		print("pre_condition_661 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_662(c=c)==True:
		print("pre_condition_662 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_663(c=c)==True:
		print("pre_condition_663 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_664(c=c)==True:
		print("pre_condition_664 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_665(c=c)==True:
		print("pre_condition_665 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_666(c=c)==True:
		print("pre_condition_666 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_667(c=c)==True:
		print("pre_condition_667 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_668(c=c)==True:
		print("pre_condition_668 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_669(c=c)==True:
		print("pre_condition_669 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_670(c=c)==True:
		print("pre_condition_670 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_671(c=c)==True:
		print("pre_condition_671 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_672(c=c)==True:
		print("pre_condition_672 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_673(c=c)==True:
		print("pre_condition_673 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_674(c=c)==True:
		print("pre_condition_674 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_675(c=c)==True:
		print("pre_condition_675 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_676(c=c)==True:
		print("pre_condition_676 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_677(c=c)==True:
		print("pre_condition_677 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_678(c=c)==True:
		print("pre_condition_678 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_679(c=c)==True:
		print("pre_condition_679 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_680(c=c)==True:
		print("pre_condition_680 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_681(c=c)==True:
		print("pre_condition_681 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_682(c=c)==True:
		print("pre_condition_682 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_683(c=c)==True:
		print("pre_condition_683 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_684(c=c)==True:
		print("pre_condition_684 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_685(c=c)==True:
		print("pre_condition_685 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_686(c=c)==True:
		print("pre_condition_686 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_687(c=c)==True:
		print("pre_condition_687 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_688(c=c)==True:
		print("pre_condition_688 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_689(c=c)==True:
		print("pre_condition_689 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_690(c=c)==True:
		print("pre_condition_690 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_691(c=c)==True:
		print("pre_condition_691 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_692(c=c)==True:
		print("pre_condition_692 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_693(c=c)==True:
		print("pre_condition_693 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_694(c=c)==True:
		print("pre_condition_694 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_695(c=c)==True:
		print("pre_condition_695 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_696(c=c)==True:
		print("pre_condition_696 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_697(c=c)==True:
		print("pre_condition_697 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_698(c=c)==True:
		print("pre_condition_698 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_699(c=c)==True:
		print("pre_condition_699 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_700(c=c)==True:
		print("pre_condition_700 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_701(c=c)==True:
		print("pre_condition_701 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_702(c=c)==True:
		print("pre_condition_702 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_703(c=c)==True:
		print("pre_condition_703 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_704(c=c)==True:
		print("pre_condition_704 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_705(c=c)==True:
		print("pre_condition_705 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_706(c=c)==True:
		print("pre_condition_706 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_707(c=c)==True:
		print("pre_condition_707 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_708(c=c)==True:
		print("pre_condition_708 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_709(c=c)==True:
		print("pre_condition_709 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_710(c=c)==True:
		print("pre_condition_710 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_711(c=c)==True:
		print("pre_condition_711 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_712(c=c)==True:
		print("pre_condition_712 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_713(c=c)==True:
		print("pre_condition_713 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_714(c=c)==True:
		print("pre_condition_714 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_715(c=c)==True:
		print("pre_condition_715 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_716(c=c)==True:
		print("pre_condition_716 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_717(c=c)==True:
		print("pre_condition_717 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_718(c=c)==True:
		print("pre_condition_718 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_719(c=c)==True:
		print("pre_condition_719 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_720(c=c)==True:
		print("pre_condition_720 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_721(c=c)==True:
		print("pre_condition_721 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_722(c=c)==True:
		print("pre_condition_722 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_723(c=c)==True:
		print("pre_condition_723 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_724(c=c)==True:
		print("pre_condition_724 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_725(c=c)==True:
		print("pre_condition_725 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_726(c=c)==True:
		print("pre_condition_726 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_727(c=c)==True:
		print("pre_condition_727 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_728(c=c)==True:
		print("pre_condition_728 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_729(c=c)==True:
		print("pre_condition_729 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_730(c=c)==True:
		print("pre_condition_730 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_731(c=c)==True:
		print("pre_condition_731 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_732(c=c)==True:
		print("pre_condition_732 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_733(c=c)==True:
		print("pre_condition_733 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_734(c=c)==True:
		print("pre_condition_734 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_735(c=c)==True:
		print("pre_condition_735 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_736(c=c)==True:
		print("pre_condition_736 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_737(c=c)==True:
		print("pre_condition_737 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_738(c=c)==True:
		print("pre_condition_738 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_739(c=c)==True:
		print("pre_condition_739 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_740(c=c)==True:
		print("pre_condition_740 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_741(c=c)==True:
		print("pre_condition_741 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_742(c=c)==True:
		print("pre_condition_742 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_743(c=c)==True:
		print("pre_condition_743 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_744(c=c)==True:
		print("pre_condition_744 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_745(c=c)==True:
		print("pre_condition_745 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_746(c=c)==True:
		print("pre_condition_746 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_747(c=c)==True:
		print("pre_condition_747 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_748(c=c)==True:
		print("pre_condition_748 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_749(c=c)==True:
		print("pre_condition_749 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_750(c=c)==True:
		print("pre_condition_750 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_751(c=c)==True:
		print("pre_condition_751 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_752(c=c)==True:
		print("pre_condition_752 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_753(c=c)==True:
		print("pre_condition_753 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_754(c=c)==True:
		print("pre_condition_754 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_755(c=c)==True:
		print("pre_condition_755 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_756(c=c)==True:
		print("pre_condition_756 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_757(c=c)==True:
		print("pre_condition_757 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_758(c=c)==True:
		print("pre_condition_758 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_759(c=c)==True:
		print("pre_condition_759 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_760(c=c)==True:
		print("pre_condition_760 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_761(c=c)==True:
		print("pre_condition_761 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_762(c=c)==True:
		print("pre_condition_762 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_763(c=c)==True:
		print("pre_condition_763 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_764(c=c)==True:
		print("pre_condition_764 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_765(c=c)==True:
		print("pre_condition_765 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_766(c=c)==True:
		print("pre_condition_766 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_767(c=c)==True:
		print("pre_condition_767 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_768(c=c)==True:
		print("pre_condition_768 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_769(c=c)==True:
		print("pre_condition_769 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_770(c=c)==True:
		print("pre_condition_770 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_771(c=c)==True:
		print("pre_condition_771 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_772(c=c)==True:
		print("pre_condition_772 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_773(c=c)==True:
		print("pre_condition_773 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_774(c=c)==True:
		print("pre_condition_774 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_775(c=c)==True:
		print("pre_condition_775 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_776(c=c)==True:
		print("pre_condition_776 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_777(c=c)==True:
		print("pre_condition_777 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_778(c=c)==True:
		print("pre_condition_778 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_779(c=c)==True:
		print("pre_condition_779 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_780(c=c)==True:
		print("pre_condition_780 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_781(c=c)==True:
		print("pre_condition_781 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_782(c=c)==True:
		print("pre_condition_782 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_783(c=c)==True:
		print("pre_condition_783 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_784(c=c)==True:
		print("pre_condition_784 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_785(c=c)==True:
		print("pre_condition_785 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_786(c=c)==True:
		print("pre_condition_786 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_787(c=c)==True:
		print("pre_condition_787 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_788(c=c)==True:
		print("pre_condition_788 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_789(c=c)==True:
		print("pre_condition_789 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_790(c=c)==True:
		print("pre_condition_790 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_791(c=c)==True:
		print("pre_condition_791 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_792(c=c)==True:
		print("pre_condition_792 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_793(c=c)==True:
		print("pre_condition_793 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_794(c=c)==True:
		print("pre_condition_794 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_795(c=c)==True:
		print("pre_condition_795 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_796(c=c)==True:
		print("pre_condition_796 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_797(c=c)==True:
		print("pre_condition_797 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_798(c=c)==True:
		print("pre_condition_798 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_799(c=c)==True:
		print("pre_condition_799 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_800(c=c)==True:
		print("pre_condition_800 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_801(c=c)==True:
		print("pre_condition_801 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_802(c=c)==True:
		print("pre_condition_802 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_803(c=c)==True:
		print("pre_condition_803 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_804(c=c)==True:
		print("pre_condition_804 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_805(c=c)==True:
		print("pre_condition_805 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_806(c=c)==True:
		print("pre_condition_806 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_807(c=c)==True:
		print("pre_condition_807 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_808(c=c)==True:
		print("pre_condition_808 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_809(c=c)==True:
		print("pre_condition_809 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_810(c=c)==True:
		print("pre_condition_810 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_811(c=c)==True:
		print("pre_condition_811 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_812(c=c)==True:
		print("pre_condition_812 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_813(c=c)==True:
		print("pre_condition_813 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_814(c=c)==True:
		print("pre_condition_814 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_815(c=c)==True:
		print("pre_condition_815 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_816(c=c)==True:
		print("pre_condition_816 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_817(c=c)==True:
		print("pre_condition_817 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_818(c=c)==True:
		print("pre_condition_818 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_819(c=c)==True:
		print("pre_condition_819 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_820(c=c)==True:
		print("pre_condition_820 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_821(c=c)==True:
		print("pre_condition_821 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_822(c=c)==True:
		print("pre_condition_822 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_823(c=c)==True:
		print("pre_condition_823 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_824(c=c)==True:
		print("pre_condition_824 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_825(c=c)==True:
		print("pre_condition_825 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_826(c=c)==True:
		print("pre_condition_826 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_827(c=c)==True:
		print("pre_condition_827 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_828(c=c)==True:
		print("pre_condition_828 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_829(c=c)==True:
		print("pre_condition_829 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_830(c=c)==True:
		print("pre_condition_830 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_831(c=c)==True:
		print("pre_condition_831 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_832(c=c)==True:
		print("pre_condition_832 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_833(c=c)==True:
		print("pre_condition_833 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_834(c=c)==True:
		print("pre_condition_834 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_835(c=c)==True:
		print("pre_condition_835 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_836(c=c)==True:
		print("pre_condition_836 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_837(c=c)==True:
		print("pre_condition_837 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_838(c=c)==True:
		print("pre_condition_838 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_839(c=c)==True:
		print("pre_condition_839 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_840(c=c)==True:
		print("pre_condition_840 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_841(c=c)==True:
		print("pre_condition_841 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_842(c=c)==True:
		print("pre_condition_842 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_843(c=c)==True:
		print("pre_condition_843 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_844(c=c)==True:
		print("pre_condition_844 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_845(c=c)==True:
		print("pre_condition_845 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_846(c=c)==True:
		print("pre_condition_846 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_847(c=c)==True:
		print("pre_condition_847 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_848(c=c)==True:
		print("pre_condition_848 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_849(c=c)==True:
		print("pre_condition_849 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_850(c=c)==True:
		print("pre_condition_850 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_851(c=c)==True:
		print("pre_condition_851 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_852(c=c)==True:
		print("pre_condition_852 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_853(c=c)==True:
		print("pre_condition_853 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_854(c=c)==True:
		print("pre_condition_854 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_855(c=c)==True:
		print("pre_condition_855 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_856(c=c)==True:
		print("pre_condition_856 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_857(c=c)==True:
		print("pre_condition_857 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_858(c=c)==True:
		print("pre_condition_858 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_859(c=c)==True:
		print("pre_condition_859 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_860(c=c)==True:
		print("pre_condition_860 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_861(c=c)==True:
		print("pre_condition_861 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_862(c=c)==True:
		print("pre_condition_862 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_863(c=c)==True:
		print("pre_condition_863 SAT")
		print('x = 511/512')
		print('y = 0')
		print('c = 22482796584894463/4503599627370496')
		exit(0)
	
	
	if pre_condition_864(c=c)==True:
		print("pre_condition_864 SAT")