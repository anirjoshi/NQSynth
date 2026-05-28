import sympy
from sympy import *

def pre_condition_0(z:sympy.Rational):
	#(x - 8*z > 1/8) & (-x**2 + 10*z + 1/64 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('x'), Mul(Integer(-1), Integer(8), Symbol('z'))), Rational(1, 8)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Rational(1, 64)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1(z:sympy.Rational):
	#(z > 3/128) & (z < 3/64)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(3, 128)), StrictLessThan(Symbol('z'), Rational(3, 64)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_2(z:sympy.Rational):
	#(x + 2*z < -1/2) & (-x**2 + 10*z + 1/4 > 0)

	pre_cond = And(StrictLessThan(Add(Symbol('x'), Mul(Integer(2), Symbol('z'))), Rational(-1, 2)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Rational(1, 4)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_3(z:sympy.Rational):
	#(z > 3/40) & (z < 1/4)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(3, 40)), StrictLessThan(Symbol('z'), Rational(1, 4)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_4(z:sympy.Rational):
	#(x - 4*z > 1/4) & (-x**2 + 10*z + 1/16 > 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('x'), Mul(Integer(-1), Integer(4), Symbol('z'))), Rational(1, 4)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Rational(1, 16)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_5(z:sympy.Rational):
	#(z > 3/160) & (z < 1/16)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(3, 160)), StrictLessThan(Symbol('z'), Rational(1, 16)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_6(z:sympy.Rational):
	#(x + 4*z < -1/4) & (-x**2 + 10*z + 1/16 > 0)

	pre_cond = And(StrictLessThan(Add(Symbol('x'), Mul(Integer(4), Symbol('z'))), Rational(-1, 4)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Rational(1, 16)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_7(z:sympy.Rational):
	#(z > 21/640) & (z < 3/32)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(21, 640)), StrictLessThan(Symbol('z'), Rational(3, 32)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_8(z:sympy.Rational):
	#(x + z < -1) & (-x**2 + 10*z + 1 > 0)

	pre_cond = And(StrictLessThan(Add(Symbol('x'), Symbol('z')), Integer(-1)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_9(z:sympy.Rational):
	#(z > 12/5) & (z < 4)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(12, 5)), StrictLessThan(Symbol('z'), Integer(4)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_10(z:sympy.Rational):
	#(2*x + z < -4) & (-x**2 + 10*z + 4 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(2), Symbol('x')), Symbol('z')), Integer(-4)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(4)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_11(z:sympy.Rational):
	#(z > 77/10) & (z < 14)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(77, 10)), StrictLessThan(Symbol('z'), Integer(14)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_12(z:sympy.Rational):
	#(4*x + z < -16) & (-x**2 + 10*z + 16 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(4), Symbol('x')), Symbol('z')), Integer(-16)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(16)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_13(z:sympy.Rational):
	#(z > 69/2) & (z < 60)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(69, 2)), StrictLessThan(Symbol('z'), Integer(60)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_14(z:sympy.Rational):
	#(5*x + z < -25) & (-x**2 + 10*z + 25 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(5), Symbol('x')), Symbol('z')), Integer(-25)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(25)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_15(z:sympy.Rational):
	#(z > 1271/10) & (z < 155)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(1271, 10)), StrictLessThan(Symbol('z'), Integer(155)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_16(z:sympy.Rational):
	#(6*x + z < -36) & (-x**2 + 10*z + 36 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(6), Symbol('x')), Symbol('z')), Integer(-36)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(36)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_17(z:sympy.Rational):
	#(z > 1989/10) & (z < 234)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(1989, 10)), StrictLessThan(Symbol('z'), Integer(234)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_18(z:sympy.Rational):
	#(7*x + z < -49) & (-x**2 + 10*z + 49 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(7), Symbol('x')), Symbol('z')), Integer(-49)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(49)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_19(z:sympy.Rational):
	#(z > 2867/10) & (z < 329)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(2867, 10)), StrictLessThan(Symbol('z'), Integer(329)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_20(z:sympy.Rational):
	#(8*x + z < -64) & (-x**2 + 10*z + 64 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(8), Symbol('x')), Symbol('z')), Integer(-64)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(64)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_21(z:sympy.Rational):
	#(z > 781/2) & (z < 440)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(781, 2)), StrictLessThan(Symbol('z'), Integer(440)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_22(z:sympy.Rational):
	#(9*x + z < -81) & (-x**2 + 10*z + 81 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(9), Symbol('x')), Symbol('z')), Integer(-81)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(81)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_23(z:sympy.Rational):
	#(z > 496) & (z < 558)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Integer(496)), StrictLessThan(Symbol('z'), Integer(558)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_24(z:sympy.Rational):
	#(10*x + z < -100) & (-x**2 + 10*z + 100 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(10), Symbol('x')), Symbol('z')), Integer(-100)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(100)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_25(z:sympy.Rational):
	#(z > 630) & (z < 700)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Integer(630)), StrictLessThan(Symbol('z'), Integer(700)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_26(z:sympy.Rational):
	#(11*x + z < -121) & (-x**2 + 10*z + 121 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(11), Symbol('x')), Symbol('z')), Integer(-121)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(121)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_27(z:sympy.Rational):
	#(z > 780) & (z < 858)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Integer(780)), StrictLessThan(Symbol('z'), Integer(858)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_28(z:sympy.Rational):
	#(12*x + z < -144) & (-x**2 + 10*z + 144 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(12), Symbol('x')), Symbol('z')), Integer(-144)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(144)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_29(z:sympy.Rational):
	#(z > 946) & (z < 1032)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Integer(946)), StrictLessThan(Symbol('z'), Integer(1032)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_30(z:sympy.Rational):
	#(13*x + z < -169) & (-x**2 + 10*z + 169 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(13), Symbol('x')), Symbol('z')), Integer(-169)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(169)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_31(z:sympy.Rational):
	#(z > 1128) & (z < 1222)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Integer(1128)), StrictLessThan(Symbol('z'), Integer(1222)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_32(z:sympy.Rational):
	#(14*x + z < -196) & (-x**2 + 10*z + 196 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(14), Symbol('x')), Symbol('z')), Integer(-196)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(196)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_33(z:sympy.Rational):
	#(z > 1326) & (z < 1428)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Integer(1326)), StrictLessThan(Symbol('z'), Integer(1428)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_34(z:sympy.Rational):
	#(15*x + z < -225) & (-x**2 + 10*z + 225 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(15), Symbol('x')), Symbol('z')), Integer(-225)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(225)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_35(z:sympy.Rational):
	#(z > 1540) & (z < 1650)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Integer(1540)), StrictLessThan(Symbol('z'), Integer(1650)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_36(z:sympy.Rational):
	#(16*x + z < -256) & (-x**2 + 10*z + 256 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(16), Symbol('x')), Symbol('z')), Integer(-256)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(256)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_37(z:sympy.Rational):
	#(z > 1770) & (z < 1888)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Integer(1770)), StrictLessThan(Symbol('z'), Integer(1888)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_38(z:sympy.Rational):
	#(17*x + z < -289) & (-x**2 + 10*z + 289 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(17), Symbol('x')), Symbol('z')), Integer(-289)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(289)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_39(z:sympy.Rational):
	#(z > 3975/2) & (z < 2125)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(3975, 2)), StrictLessThan(Symbol('z'), Integer(2125)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_40(z:sympy.Rational):
	#(18*x + z < -324) & (-x**2 + 10*z + 324 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(18), Symbol('x')), Symbol('z')), Integer(-324)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(324)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_41(z:sympy.Rational):
	#(z > 22477/10) & (z < 2394)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(22477, 10)), StrictLessThan(Symbol('z'), Integer(2394)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_42(z:sympy.Rational):
	#(19*x + z < -361) & (-x**2 + 10*z + 361 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(19), Symbol('x')), Symbol('z')), Integer(-361)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(361)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_43(z:sympy.Rational):
	#(z > 25239/10) & (z < 2679)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(25239, 10)), StrictLessThan(Symbol('z'), Integer(2679)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_44(z:sympy.Rational):
	#(20*x + z < -400) & (-x**2 + 10*z + 400 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(20), Symbol('x')), Symbol('z')), Integer(-400)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(400)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_45(z:sympy.Rational):
	#(z > 28161/10) & (z < 2980)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(28161, 10)), StrictLessThan(Symbol('z'), Integer(2980)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_46(z:sympy.Rational):
	#(21*x + z < -441) & (-x**2 + 10*z + 441 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(21), Symbol('x')), Symbol('z')), Integer(-441)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(441)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_47(z:sympy.Rational):
	#(z > 31243/10) & (z < 3297)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(31243, 10)), StrictLessThan(Symbol('z'), Integer(3297)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_48(z:sympy.Rational):
	#(22*x + z < -484) & (-x**2 + 10*z + 484 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(22), Symbol('x')), Symbol('z')), Integer(-484)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(484)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_49(z:sympy.Rational):
	#(z > 6897/2) & (z < 3630)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(6897, 2)), StrictLessThan(Symbol('z'), Integer(3630)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_50(z:sympy.Rational):
	#(23*x + z < -529) & (-x**2 + 10*z + 529 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(23), Symbol('x')), Symbol('z')), Integer(-529)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(529)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_51(z:sympy.Rational):
	#(z > 3296) & (z < 3680)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Integer(3296)), StrictLessThan(Symbol('z'), Integer(3680)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_52(z:sympy.Rational):
	#(24*x + z < -576) & (-x**2 + 10*z + 576 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(24), Symbol('x')), Symbol('z')), Integer(-576)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(576)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_53(z:sympy.Rational):
	#(z > 42273/10) & (z < 4392)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(42273, 10)), StrictLessThan(Symbol('z'), Integer(4392)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_54(z:sympy.Rational):
	#(25*x + z < -625) & (-x**2 + 10*z + 625 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(25), Symbol('x')), Symbol('z')), Integer(-625)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(625)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_55(z:sympy.Rational):
	#(z > 46031/10) & (z < 4775)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(46031, 10)), StrictLessThan(Symbol('z'), Integer(4775)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_56(z:sympy.Rational):
	#(26*x + z < -676) & (-x**2 + 10*z + 676 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(26), Symbol('x')), Symbol('z')), Integer(-676)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(676)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_57(z:sympy.Rational):
	#(z > 22134/5) & (z < 4836)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(22134, 5)), StrictLessThan(Symbol('z'), Integer(4836)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_58(z:sympy.Rational):
	#(27*x + z < -729) & (-x**2 + 10*z + 729 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(27), Symbol('x')), Symbol('z')), Integer(-729)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(729)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_59(z:sympy.Rational):
	#(z > 8843/2) & (z < 4995)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(8843, 2)), StrictLessThan(Symbol('z'), Integer(4995)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_60(z:sympy.Rational):
	#(28*x + z < -784) & (-x**2 + 10*z + 784 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(28), Symbol('x')), Symbol('z')), Integer(-784)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(784)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_61(z:sympy.Rational):
	#(z > 4416) & (z < 5152)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Integer(4416)), StrictLessThan(Symbol('z'), Integer(5152)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_62(z:sympy.Rational):
	#(29*x + z < -841) & (-x**2 + 10*z + 841 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(29), Symbol('x')), Symbol('z')), Integer(-841)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(841)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_63(z:sympy.Rational):
	#(z > 44103/10) & (z < 5307)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(44103, 10)), StrictLessThan(Symbol('z'), Integer(5307)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_64(z:sympy.Rational):
	#(30*x + z < -900) & (-x**2 + 10*z + 900 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(30), Symbol('x')), Symbol('z')), Integer(-900)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(900)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_65(z:sympy.Rational):
	#(z > 22022/5) & (z < 5460)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(22022, 5)), StrictLessThan(Symbol('z'), Integer(5460)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_66(z:sympy.Rational):
	#(31*x + z < -961) & (-x**2 + 10*z + 961 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(31), Symbol('x')), Symbol('z')), Integer(-961)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(961)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_67(z:sympy.Rational):
	#(z > 43983/10) & (z < 5611)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(43983, 10)), StrictLessThan(Symbol('z'), Integer(5611)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_68(z:sympy.Rational):
	#(32*x + z < -1024) & (-x**2 + 10*z + 1024 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(32), Symbol('x')), Symbol('z')), Integer(-1024)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(1024)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_69(z:sympy.Rational):
	#(z > 4392) & (z < 5760)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Integer(4392)), StrictLessThan(Symbol('z'), Integer(5760)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_70(z:sympy.Rational):
	#(39*x + z < -1521) & (-x**2 + 10*z + 1521 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(39), Symbol('x')), Symbol('z')), Integer(-1521)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(1521)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_71(z:sympy.Rational):
	#(z > 21924/5) & (z < 6786)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(21924, 5)), StrictLessThan(Symbol('z'), Integer(6786)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_72(z:sympy.Rational):
	#(40*x + z < -1600) & (-x**2 + 10*z + 1600 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(40), Symbol('x')), Symbol('z')), Integer(-1600)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(1600)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_73(z:sympy.Rational):
	#(z > 34048/5) & (z < 8960)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(34048, 5)), StrictLessThan(Symbol('z'), Integer(8960)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_74(z:sympy.Rational):
	#(41*x + z < -1681) & (-x**2 + 10*z + 1681 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(41), Symbol('x')), Symbol('z')), Integer(-1681)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(1681)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_75(z:sympy.Rational):
	#(z > 13603/2) & (z < 9143)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(13603, 2)), StrictLessThan(Symbol('z'), Integer(9143)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_76(z:sympy.Rational):
	#(42*x + z < -1764) & (-x**2 + 10*z + 1764 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(42), Symbol('x')), Symbol('z')), Integer(-1764)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(1764)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_77(z:sympy.Rational):
	#(z > 33966/5) & (z < 9324)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(33966, 5)), StrictLessThan(Symbol('z'), Integer(9324)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_78(z:sympy.Rational):
	#(43*x + z < -1849) & (-x**2 + 10*z + 1849 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(43), Symbol('x')), Symbol('z')), Integer(-1849)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(1849)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_79(z:sympy.Rational):
	#(z > 67847/10) & (z < 9503)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(67847, 10)), StrictLessThan(Symbol('z'), Integer(9503)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_80(z:sympy.Rational):
	#(44*x + z < -1936) & (-x**2 + 10*z + 1936 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(44), Symbol('x')), Symbol('z')), Integer(-1936)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(1936)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_81(z:sympy.Rational):
	#(z > 147833/10) & (z < 15092)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(147833, 10)), StrictLessThan(Symbol('z'), Integer(15092)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_82(z:sympy.Rational):
	#(45*x + z < -2025) & (-x**2 + 10*z + 2025 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(45), Symbol('x')), Symbol('z')), Integer(-2025)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(2025)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_83(z:sympy.Rational):
	#(z > 95319/10) & (z < 12015)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(95319, 10)), StrictLessThan(Symbol('z'), Integer(12015)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_84(z:sympy.Rational):
	#(46*x + z < -2116) & (-x**2 + 10*z + 2116 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(46), Symbol('x')), Symbol('z')), Integer(-2116)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(2116)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_85(z:sympy.Rational):
	#(z > 47614/5) & (z < 12236)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(47614, 5)), StrictLessThan(Symbol('z'), Integer(12236)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_86(z:sympy.Rational):
	#(47*x + z < -2209) & (-x**2 + 10*z + 2209 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(47), Symbol('x')), Symbol('z')), Integer(-2209)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(2209)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_87(z:sympy.Rational):
	#(z > 19027/2) & (z < 12455)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(19027, 2)), StrictLessThan(Symbol('z'), Integer(12455)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_88(z:sympy.Rational):
	#(48*x + z < -2304) & (-x**2 + 10*z + 2304 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(48), Symbol('x')), Symbol('z')), Integer(-2304)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(2304)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_89(z:sympy.Rational):
	#(z > 9504) & (z < 12672)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Integer(9504)), StrictLessThan(Symbol('z'), Integer(12672)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_90(z:sympy.Rational):
	#(49*x + z < -2401) & (-x**2 + 10*z + 2401 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(49), Symbol('x')), Symbol('z')), Integer(-2401)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(2401)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_91(z:sympy.Rational):
	#(z > 94943/10) & (z < 12887)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(94943, 10)), StrictLessThan(Symbol('z'), Integer(12887)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_92(z:sympy.Rational):
	#(50*x + z < -2500) & (-x**2 + 10*z + 2500 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(50), Symbol('x')), Symbol('z')), Integer(-2500)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(2500)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_93(z:sympy.Rational):
	#(z > 129269/10) & (z < 15650)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(129269, 10)), StrictLessThan(Symbol('z'), Integer(15650)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_94(z:sympy.Rational):
	#(51*x + z < -2601) & (-x**2 + 10*z + 2601 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(51), Symbol('x')), Symbol('z')), Integer(-2601)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(2601)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_95(z:sympy.Rational):
	#(z > 64584/5) & (z < 15912)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(64584, 5)), StrictLessThan(Symbol('z'), Integer(15912)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_96(z:sympy.Rational):
	#(52*x + z < -2704) & (-x**2 + 10*z + 2704 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(52), Symbol('x')), Symbol('z')), Integer(-2704)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(2704)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_97(z:sympy.Rational):
	#(z > 25813/2) & (z < 16172)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(25813, 2)), StrictLessThan(Symbol('z'), Integer(16172)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_98(z:sympy.Rational):
	#(53*x + z < -2809) & (-x**2 + 10*z + 2809 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(53), Symbol('x')), Symbol('z')), Integer(-2809)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(2809)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_99(z:sympy.Rational):
	#(z > 12896) & (z < 16430)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Integer(12896)), StrictLessThan(Symbol('z'), Integer(16430)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_100(z:sympy.Rational):
	#(54*x + z < -2916) & (-x**2 + 10*z + 2916 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(54), Symbol('x')), Symbol('z')), Integer(-2916)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(2916)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_101(z:sympy.Rational):
	#(z > 128853/10) & (z < 16686)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(128853, 10)), StrictLessThan(Symbol('z'), Integer(16686)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_102(z:sympy.Rational):
	#(55*x + z < -3025) & (-x**2 + 10*z + 3025 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(55), Symbol('x')), Symbol('z')), Integer(-3025)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(3025)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_103(z:sympy.Rational):
	#(z > 233171/10) & (z < 23705)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(233171, 10)), StrictLessThan(Symbol('z'), Integer(23705)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_104(z:sympy.Rational):
	#(56*x + z < -3136) & (-x**2 + 10*z + 3136 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(56), Symbol('x')), Symbol('z')), Integer(-3136)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(3136)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_105(z:sympy.Rational):
	#(z > 167433/10) & (z < 19992)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(167433, 10)), StrictLessThan(Symbol('z'), Integer(19992)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_106(z:sympy.Rational):
	#(57*x + z < -3249) & (-x**2 + 10*z + 3249 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(57), Symbol('x')), Symbol('z')), Integer(-3249)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(3249)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_107(z:sympy.Rational):
	#(z > 16732) & (z < 20292)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Integer(16732)), StrictLessThan(Symbol('z'), Integer(20292)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_108(z:sympy.Rational):
	#(58*x + z < -3364) & (-x**2 + 10*z + 3364 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(58), Symbol('x')), Symbol('z')), Integer(-3364)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(3364)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_109(z:sympy.Rational):
	#(z > 33441/2) & (z < 20590)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(33441, 2)), StrictLessThan(Symbol('z'), Integer(20590)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_110(z:sympy.Rational):
	#(59*x + z < -3481) & (-x**2 + 10*z + 3481 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(59), Symbol('x')), Symbol('z')), Integer(-3481)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(3481)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_111(z:sympy.Rational):
	#(z > 83544/5) & (z < 20886)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(83544, 5)), StrictLessThan(Symbol('z'), Integer(20886)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_112(z:sympy.Rational):
	#(60*x + z < -3600) & (-x**2 + 10*z + 3600 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(60), Symbol('x')), Symbol('z')), Integer(-3600)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(3600)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_113(z:sympy.Rational):
	#(z > 166969/10) & (z < 21180)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(166969, 10)), StrictLessThan(Symbol('z'), Integer(21180)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_114(z:sympy.Rational):
	#(61*x + z < -3721) & (-x**2 + 10*z + 3721 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(61), Symbol('x')), Symbol('z')), Integer(-3721)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(3721)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_115(z:sympy.Rational):
	#(z > 83424/5) & (z < 21472)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(83424, 5)), StrictLessThan(Symbol('z'), Integer(21472)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_116(z:sympy.Rational):
	#(62*x + z < -3844) & (-x**2 + 10*z + 3844 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(62), Symbol('x')), Symbol('z')), Integer(-3844)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(3844)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_117(z:sympy.Rational):
	#(z > 21518) & (z < 25172)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Integer(21518)), StrictLessThan(Symbol('z'), Integer(25172)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_118(z:sympy.Rational):
	#(63*x + z < -3969) & (-x**2 + 10*z + 3969 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(63), Symbol('x')), Symbol('z')), Integer(-3969)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(3969)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_119(z:sympy.Rational):
	#(z > 43011/2) & (z < 25515)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(43011, 2)), StrictLessThan(Symbol('z'), Integer(25515)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_120(z:sympy.Rational):
	#(64*x + z < -4096) & (-x**2 + 10*z + 4096 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(64), Symbol('x')), Symbol('z')), Integer(-4096)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(4096)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_121(z:sympy.Rational):
	#(z > 107464/5) & (z < 25856)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(107464, 5)), StrictLessThan(Symbol('z'), Integer(25856)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_122(z:sympy.Rational):
	#(65*x + z < -4225) & (-x**2 + 10*z + 4225 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(65), Symbol('x')), Symbol('z')), Integer(-4225)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(4225)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_123(z:sympy.Rational):
	#(z > 214799/10) & (z < 26195)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(214799, 10)), StrictLessThan(Symbol('z'), Integer(26195)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_124(z:sympy.Rational):
	#(66*x + z < -4356) & (-x**2 + 10*z + 4356 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(66), Symbol('x')), Symbol('z')), Integer(-4356)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(4356)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_125(z:sympy.Rational):
	#(z > 107334/5) & (z < 26532)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(107334, 5)), StrictLessThan(Symbol('z'), Integer(26532)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_126(z:sympy.Rational):
	#(67*x + z < -4489) & (-x**2 + 10*z + 4489 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(67), Symbol('x')), Symbol('z')), Integer(-4489)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(4489)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_127(z:sympy.Rational):
	#(z > 348347/10) & (z < 35309)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(348347, 10)), StrictLessThan(Symbol('z'), Integer(35309)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_128(z:sympy.Rational):
	#(68*x + z < -4624) & (-x**2 + 10*z + 4624 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(68), Symbol('x')), Symbol('z')), Integer(-4624)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(4624)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_129(z:sympy.Rational):
	#(z > 132888/5) & (z < 30736)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(132888, 5)), StrictLessThan(Symbol('z'), Integer(30736)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_130(z:sympy.Rational):
	#(69*x + z < -4761) & (-x**2 + 10*z + 4761 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(69), Symbol('x')), Symbol('z')), Integer(-4761)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(4761)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_131(z:sympy.Rational):
	#(z > 265639/10) & (z < 31119)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(265639, 10)), StrictLessThan(Symbol('z'), Integer(31119)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_132(z:sympy.Rational):
	#(70*x + z < -4900) & (-x**2 + 10*z + 4900 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(70), Symbol('x')), Symbol('z')), Integer(-4900)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(4900)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_133(z:sympy.Rational):
	#(z > 26550) & (z < 31500)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Integer(26550)), StrictLessThan(Symbol('z'), Integer(31500)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_134(z:sympy.Rational):
	#(71*x + z < -5041) & (-x**2 + 10*z + 5041 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(71), Symbol('x')), Symbol('z')), Integer(-5041)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(5041)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_135(z:sympy.Rational):
	#(z > 265359/10) & (z < 31879)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(265359, 10)), StrictLessThan(Symbol('z'), Integer(31879)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_136(z:sympy.Rational):
	#(72*x + z < -5184) & (-x**2 + 10*z + 5184 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(72), Symbol('x')), Symbol('z')), Integer(-5184)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(5184)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_137(z:sympy.Rational):
	#(z > 132608/5) & (z < 32256)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(132608, 5)), StrictLessThan(Symbol('z'), Integer(32256)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_138(z:sympy.Rational):
	#(73*x + z < -5329) & (-x**2 + 10*z + 5329 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(73), Symbol('x')), Symbol('z')), Integer(-5329)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(5329)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_139(z:sympy.Rational):
	#(z > 32300) & (z < 36500)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Integer(32300)), StrictLessThan(Symbol('z'), Integer(36500)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_140(z:sympy.Rational):
	#(74*x + z < -5476) & (-x**2 + 10*z + 5476 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(74), Symbol('x')), Symbol('z')), Integer(-5476)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(5476)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_141(z:sympy.Rational):
	#(z > 322853/10) & (z < 36926)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(322853, 10)), StrictLessThan(Symbol('z'), Integer(36926)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_142(z:sympy.Rational):
	#(75*x + z < -5625) & (-x**2 + 10*z + 5625 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(75), Symbol('x')), Symbol('z')), Integer(-5625)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(5625)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_143(z:sympy.Rational):
	#(z > 437931/10) & (z < 44325)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(437931, 10)), StrictLessThan(Symbol('z'), Integer(44325)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_144(z:sympy.Rational):
	#(76*x + z < -5776) & (-x**2 + 10*z + 5776 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(76), Symbol('x')), Symbol('z')), Integer(-5776)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(5776)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_145(z:sympy.Rational):
	#(z > 221562/5) & (z < 45144)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(221562, 5)), StrictLessThan(Symbol('z'), Integer(45144)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_146(z:sympy.Rational):
	#(77*x + z < -5929) & (-x**2 + 10*z + 5929 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(77), Symbol('x')), Symbol('z')), Integer(-5929)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(5929)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_147(z:sympy.Rational):
	#(z > 461927/10) & (z < 46739)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(461927, 10)), StrictLessThan(Symbol('z'), Integer(46739)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_148(z:sympy.Rational):
	#(78*x + z < -6084) & (-x**2 + 10*z + 6084 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(78), Symbol('x')), Symbol('z')), Integer(-6084)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(6084)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_149(z:sympy.Rational):
	#(z > 46726) & (z < 47580)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Integer(46726)), StrictLessThan(Symbol('z'), Integer(47580)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_150(z:sympy.Rational):
	#(79*x + z < -6241) & (-x**2 + 10*z + 6241 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(79), Symbol('x')), Symbol('z')), Integer(-6241)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(6241)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_151(z:sympy.Rational):
	#(z > 486563/10) & (z < 49217)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(486563, 10)), StrictLessThan(Symbol('z'), Integer(49217)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_152(z:sympy.Rational):
	#(80*x + z < -6400) & (-x**2 + 10*z + 6400 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(80), Symbol('x')), Symbol('z')), Integer(-6400)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(6400)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_153(z:sympy.Rational):
	#(z > 499121/10) & (z < 50480)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(499121, 10)), StrictLessThan(Symbol('z'), Integer(50480)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_154(z:sympy.Rational):
	#(81*x + z < -6561) & (-x**2 + 10*z + 6561 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(81), Symbol('x')), Symbol('z')), Integer(-6561)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(6561)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_155(z:sympy.Rational):
	#(z > 252332/5) & (z < 51354)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(252332, 5)), StrictLessThan(Symbol('z'), Integer(51354)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_156(z:sympy.Rational):
	#(82*x + z < -6724) & (-x**2 + 10*z + 6724 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(82), Symbol('x')), Symbol('z')), Integer(-6724)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(6724)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_157(z:sympy.Rational):
	#(z > 524717/10) & (z < 53054)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(524717, 10)), StrictLessThan(Symbol('z'), Integer(53054)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_158(z:sympy.Rational):
	#(83*x + z < -6889) & (-x**2 + 10*z + 6889 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(83), Symbol('x')), Symbol('z')), Integer(-6889)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(6889)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_159(z:sympy.Rational):
	#(z > 53628) & (z < 54282)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Integer(53628)), StrictLessThan(Symbol('z'), Integer(54282)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_160(z:sympy.Rational):
	#(84*x + z < -7056) & (-x**2 + 10*z + 7056 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(84), Symbol('x')), Symbol('z')), Integer(-7056)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(7056)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_161(z:sympy.Rational):
	#(z > 54946) & (z < 55608)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Integer(54946)), StrictLessThan(Symbol('z'), Integer(55608)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_162(z:sympy.Rational):
	#(85*x + z < -7225) & (-x**2 + 10*z + 7225 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(85), Symbol('x')), Symbol('z')), Integer(-7225)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(7225)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_163(z:sympy.Rational):
	#(z > 56280) & (z < 56950)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Integer(56280)), StrictLessThan(Symbol('z'), Integer(56950)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_164(z:sympy.Rational):
	#(86*x + z < -7396) & (-x**2 + 10*z + 7396 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(86), Symbol('x')), Symbol('z')), Integer(-7396)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(7396)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_165(z:sympy.Rational):
	#(z > 57630) & (z < 58308)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Integer(57630)), StrictLessThan(Symbol('z'), Integer(58308)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_166(z:sympy.Rational):
	#(87*x + z < -7569) & (-x**2 + 10*z + 7569 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(87), Symbol('x')), Symbol('z')), Integer(-7569)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(7569)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_167(z:sympy.Rational):
	#(z > 117683/2) & (z < 59595)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(117683, 2)), StrictLessThan(Symbol('z'), Integer(59595)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_168(z:sympy.Rational):
	#(88*x + z < -7744) & (-x**2 + 10*z + 7744 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(88), Symbol('x')), Symbol('z')), Integer(-7744)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(7744)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_169(z:sympy.Rational):
	#(z > 602217/10) & (z < 60984)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(602217, 10)), StrictLessThan(Symbol('z'), Integer(60984)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_170(z:sympy.Rational):
	#(89*x + z < -7921) & (-x**2 + 10*z + 7921 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(89), Symbol('x')), Symbol('z')), Integer(-7921)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(7921)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_171(z:sympy.Rational):
	#(z > 616179/10) & (z < 62389)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(616179, 10)), StrictLessThan(Symbol('z'), Integer(62389)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_172(z:sympy.Rational):
	#(90*x + z < -8100) & (-x**2 + 10*z + 8100 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(90), Symbol('x')), Symbol('z')), Integer(-8100)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(8100)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_173(z:sympy.Rational):
	#(z > 630301/10) & (z < 63810)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(630301, 10)), StrictLessThan(Symbol('z'), Integer(63810)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_174(z:sympy.Rational):
	#(91*x + z < -8281) & (-x**2 + 10*z + 8281 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(91), Symbol('x')), Symbol('z')), Integer(-8281)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(8281)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_175(z:sympy.Rational):
	#(z > 321484/5) & (z < 65156)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(321484, 5)), StrictLessThan(Symbol('z'), Integer(65156)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_176(z:sympy.Rational):
	#(92*x + z < -8464) & (-x**2 + 10*z + 8464 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(92), Symbol('x')), Symbol('z')), Integer(-8464)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(8464)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_177(z:sympy.Rational):
	#(z > 328696/5) & (z < 66608)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(328696, 5)), StrictLessThan(Symbol('z'), Integer(66608)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_178(z:sympy.Rational):
	#(93*x + z < -8649) & (-x**2 + 10*z + 8649 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(93), Symbol('x')), Symbol('z')), Integer(-8649)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(8649)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_179(z:sympy.Rational):
	#(z > 335988/5) & (z < 68076)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(335988, 5)), StrictLessThan(Symbol('z'), Integer(68076)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_180(z:sympy.Rational):
	#(94*x + z < -8836) & (-x**2 + 10*z + 8836 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(94), Symbol('x')), Symbol('z')), Integer(-8836)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(8836)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_181(z:sympy.Rational):
	#(z > 68672) & (z < 69560)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Integer(68672)), StrictLessThan(Symbol('z'), Integer(69560)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_182(z:sympy.Rational):
	#(95*x + z < -9025) & (-x**2 + 10*z + 9025 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(95), Symbol('x')), Symbol('z')), Integer(-9025)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(9025)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_183(z:sympy.Rational):
	#(z > 350812/5) & (z < 71060)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(350812, 5)), StrictLessThan(Symbol('z'), Integer(71060)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_184(z:sympy.Rational):
	#(96*x + z < -9216) & (-x**2 + 10*z + 9216 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(96), Symbol('x')), Symbol('z')), Integer(-9216)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(9216)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_185(z:sympy.Rational):
	#(z > 142997/2) & (z < 72480)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(142997, 2)), StrictLessThan(Symbol('z'), Integer(72480)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_186(z:sympy.Rational):
	#(97*x + z < -9409) & (-x**2 + 10*z + 9409 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(97), Symbol('x')), Symbol('z')), Integer(-9409)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(9409)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_187(z:sympy.Rational):
	#(z > 730191/10) & (z < 74011)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(730191, 10)), StrictLessThan(Symbol('z'), Integer(74011)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_188(z:sympy.Rational):
	#(98*x + z < -9604) & (-x**2 + 10*z + 9604 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(98), Symbol('x')), Symbol('z')), Integer(-9604)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(9604)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_189(z:sympy.Rational):
	#(z > 745557/10) & (z < 75558)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(745557, 10)), StrictLessThan(Symbol('z'), Integer(75558)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_190(z:sympy.Rational):
	#(99*x + z < -9801) & (-x**2 + 10*z + 9801 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(99), Symbol('x')), Symbol('z')), Integer(-9801)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(9801)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_191(z:sympy.Rational):
	#(z > 761083/10) & (z < 77121)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(761083, 10)), StrictLessThan(Symbol('z'), Integer(77121)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_192(z:sympy.Rational):
	#(100*x + z < -10000) & (-x**2 + 10*z + 10000 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(100), Symbol('x')), Symbol('z')), Integer(-10000)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(10000)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_193(z:sympy.Rational):
	#(z > 776769/10) & (z < 78700)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(776769, 10)), StrictLessThan(Symbol('z'), Integer(78700)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_194(z:sympy.Rational):
	#(101*x + z < -10201) & (-x**2 + 10*z + 10201 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(101), Symbol('x')), Symbol('z')), Integer(-10201)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(10201)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_195(z:sympy.Rational):
	#(z > 395412/5) & (z < 80194)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(395412, 5)), StrictLessThan(Symbol('z'), Integer(80194)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_196(z:sympy.Rational):
	#(102*x + z < -10404) & (-x**2 + 10*z + 10404 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(102), Symbol('x')), Symbol('z')), Integer(-10404)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(10404)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_197(z:sympy.Rational):
	#(z > 403406/5) & (z < 81804)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(403406, 5)), StrictLessThan(Symbol('z'), Integer(81804)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_198(z:sympy.Rational):
	#(103*x + z < -10609) & (-x**2 + 10*z + 10609 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(103), Symbol('x')), Symbol('z')), Integer(-10609)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(10609)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_199(z:sympy.Rational):
	#(z > 82296) & (z < 83430)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Integer(82296)), StrictLessThan(Symbol('z'), Integer(83430)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_200(z:sympy.Rational):
	#(104*x + z < -10816) & (-x**2 + 10*z + 10816 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(104), Symbol('x')), Symbol('z')), Integer(-10816)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(10816)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_201(z:sympy.Rational):
	#(z > 419634/5) & (z < 85072)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(419634, 5)), StrictLessThan(Symbol('z'), Integer(85072)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_202(z:sympy.Rational):
	#(105*x + z < -11025) & (-x**2 + 10*z + 11025 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(105), Symbol('x')), Symbol('z')), Integer(-11025)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(11025)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_203(z:sympy.Rational):
	#(z > 427868/5) & (z < 86730)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(427868, 5)), StrictLessThan(Symbol('z'), Integer(86730)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_204(z:sympy.Rational):
	#(106*x + z < -11236) & (-x**2 + 10*z + 11236 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(106), Symbol('x')), Symbol('z')), Integer(-11236)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(11236)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_205(z:sympy.Rational):
	#(z > 174097/2) & (z < 88298)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(174097, 2)), StrictLessThan(Symbol('z'), Integer(88298)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_206(z:sympy.Rational):
	#(107*x + z < -11449) & (-x**2 + 10*z + 11449 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(107), Symbol('x')), Symbol('z')), Integer(-11449)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(11449)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_207(z:sympy.Rational):
	#(z > 177451/2) & (z < 89987)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(177451, 2)), StrictLessThan(Symbol('z'), Integer(89987)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_208(z:sympy.Rational):
	#(108*x + z < -11664) & (-x**2 + 10*z + 11664 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(108), Symbol('x')), Symbol('z')), Integer(-11664)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(11664)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_209(z:sympy.Rational):
	#(z > 180837/2) & (z < 91692)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(180837, 2)), StrictLessThan(Symbol('z'), Integer(91692)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_210(z:sympy.Rational):
	#(109*x + z < -11881) & (-x**2 + 10*z + 11881 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(109), Symbol('x')), Symbol('z')), Integer(-11881)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(11881)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_211(z:sympy.Rational):
	#(z > 184255/2) & (z < 93413)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(184255, 2)), StrictLessThan(Symbol('z'), Integer(93413)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_212(z:sympy.Rational):
	#(110*x + z < -12100) & (-x**2 + 10*z + 12100 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(110), Symbol('x')), Symbol('z')), Integer(-12100)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(12100)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_213(z:sympy.Rational):
	#(z > 187705/2) & (z < 95150)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(187705, 2)), StrictLessThan(Symbol('z'), Integer(95150)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_214(z:sympy.Rational):
	#(111*x + z < -12321) & (-x**2 + 10*z + 12321 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(111), Symbol('x')), Symbol('z')), Integer(-12321)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(12321)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_215(z:sympy.Rational):
	#(z > 476984/5) & (z < 96792)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(476984, 5)), StrictLessThan(Symbol('z'), Integer(96792)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_216(z:sympy.Rational):
	#(112*x + z < -12544) & (-x**2 + 10*z + 12544 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(112), Symbol('x')), Symbol('z')), Integer(-12544)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(12544)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_217(z:sympy.Rational):
	#(z > 97152) & (z < 98560)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Integer(97152)), StrictLessThan(Symbol('z'), Integer(98560)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_218(z:sympy.Rational):
	#(113*x + z < -12769) & (-x**2 + 10*z + 12769 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(113), Symbol('x')), Symbol('z')), Integer(-12769)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(12769)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_219(z:sympy.Rational):
	#(z > 494616/5) & (z < 100344)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(494616, 5)), StrictLessThan(Symbol('z'), Integer(100344)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_220(z:sympy.Rational):
	#(114*x + z < -12996) & (-x**2 + 10*z + 12996 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(114), Symbol('x')), Symbol('z')), Integer(-12996)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(12996)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_221(z:sympy.Rational):
	#(z > 503552/5) & (z < 102144)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(503552, 5)), StrictLessThan(Symbol('z'), Integer(102144)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_222(z:sympy.Rational):
	#(115*x + z < -13225) & (-x**2 + 10*z + 13225 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(115), Symbol('x')), Symbol('z')), Integer(-13225)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(13225)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_223(z:sympy.Rational):
	#(z > 512568/5) & (z < 103960)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(512568, 5)), StrictLessThan(Symbol('z'), Integer(103960)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_224(z:sympy.Rational):
	#(116*x + z < -13456) & (-x**2 + 10*z + 13456 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(116), Symbol('x')), Symbol('z')), Integer(-13456)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(13456)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_225(z:sympy.Rational):
	#(z > 521664/5) & (z < 105792)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(521664, 5)), StrictLessThan(Symbol('z'), Integer(105792)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_226(z:sympy.Rational):
	#(117*x + z < -13689) & (-x**2 + 10*z + 13689 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(117), Symbol('x')), Symbol('z')), Integer(-13689)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(13689)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_227(z:sympy.Rational):
	#(z > 1059607/10) & (z < 107523)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(1059607, 10)), StrictLessThan(Symbol('z'), Integer(107523)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_228(z:sympy.Rational):
	#(118*x + z < -13924) & (-x**2 + 10*z + 13924 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(118), Symbol('x')), Symbol('z')), Integer(-13924)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(13924)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_229(z:sympy.Rational):
	#(z > 1078101/10) & (z < 109386)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(1078101, 10)), StrictLessThan(Symbol('z'), Integer(109386)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_230(z:sympy.Rational):
	#(119*x + z < -14161) & (-x**2 + 10*z + 14161 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(119), Symbol('x')), Symbol('z')), Integer(-14161)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(14161)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_231(z:sympy.Rational):
	#(z > 219351/2) & (z < 111265)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(219351, 2)), StrictLessThan(Symbol('z'), Integer(111265)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_232(z:sympy.Rational):
	#(120*x + z < -14400) & (-x**2 + 10*z + 14400 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(120), Symbol('x')), Symbol('z')), Integer(-14400)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(14400)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_233(z:sympy.Rational):
	#(z > 1115569/10) & (z < 113160)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(1115569, 10)), StrictLessThan(Symbol('z'), Integer(113160)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_234(z:sympy.Rational):
	#(121*x + z < -14641) & (-x**2 + 10*z + 14641 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(121), Symbol('x')), Symbol('z')), Integer(-14641)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(14641)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_235(z:sympy.Rational):
	#(z > 1134543/10) & (z < 115071)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(1134543, 10)), StrictLessThan(Symbol('z'), Integer(115071)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_236(z:sympy.Rational):
	#(122*x + z < -14884) & (-x**2 + 10*z + 14884 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(122), Symbol('x')), Symbol('z')), Integer(-14884)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(14884)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_237(z:sympy.Rational):
	#(z > 575758/5) & (z < 116876)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(575758, 5)), StrictLessThan(Symbol('z'), Integer(116876)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_238(z:sympy.Rational):
	#(123*x + z < -15129) & (-x**2 + 10*z + 15129 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(123), Symbol('x')), Symbol('z')), Integer(-15129)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(15129)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_239(z:sympy.Rational):
	#(z > 585396/5) & (z < 118818)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(585396, 5)), StrictLessThan(Symbol('z'), Integer(118818)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_240(z:sympy.Rational):
	#(124*x + z < -15376) & (-x**2 + 10*z + 15376 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(124), Symbol('x')), Symbol('z')), Integer(-15376)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(15376)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_241(z:sympy.Rational):
	#(z > 595114/5) & (z < 120776)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(595114, 5)), StrictLessThan(Symbol('z'), Integer(120776)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_242(z:sympy.Rational):
	#(125*x + z < -15625) & (-x**2 + 10*z + 15625 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(125), Symbol('x')), Symbol('z')), Integer(-15625)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(15625)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_243(z:sympy.Rational):
	#(z > 604912/5) & (z < 122750)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(604912, 5)), StrictLessThan(Symbol('z'), Integer(122750)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_244(z:sympy.Rational):
	#(126*x + z < -15876) & (-x**2 + 10*z + 15876 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(126), Symbol('x')), Symbol('z')), Integer(-15876)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(15876)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_245(z:sympy.Rational):
	#(z > 122958) & (z < 124740)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Integer(122958)), StrictLessThan(Symbol('z'), Integer(124740)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_246(z:sympy.Rational):
	#(127*x + z < -16129) & (-x**2 + 10*z + 16129 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(127), Symbol('x')), Symbol('z')), Integer(-16129)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(16129)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_247(z:sympy.Rational):
	#(z > 624748/5) & (z < 126746)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(624748, 5)), StrictLessThan(Symbol('z'), Integer(126746)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_248(z:sympy.Rational):
	#(128*x + z < -16384) & (-x**2 + 10*z + 16384 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(128), Symbol('x')), Symbol('z')), Integer(-16384)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(16384)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_249(z:sympy.Rational):
	#(z > 253461/2) & (z < 128640)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(253461, 2)), StrictLessThan(Symbol('z'), Integer(128640)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_250(z:sympy.Rational):
	#(129*x + z < -16641) & (-x**2 + 10*z + 16641 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(129), Symbol('x')), Symbol('z')), Integer(-16641)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(16641)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_251(z:sympy.Rational):
	#(z > 1287523/10) & (z < 130677)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(1287523, 10)), StrictLessThan(Symbol('z'), Integer(130677)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_252(z:sympy.Rational):
	#(130*x + z < -16900) & (-x**2 + 10*z + 16900 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(130), Symbol('x')), Symbol('z')), Integer(-16900)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(16900)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_253(z:sympy.Rational):
	#(z > 1307901/10) & (z < 132730)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(1307901, 10)), StrictLessThan(Symbol('z'), Integer(132730)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_254(z:sympy.Rational):
	#(131*x + z < -17161) & (-x**2 + 10*z + 17161 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(131), Symbol('x')), Symbol('z')), Integer(-17161)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(17161)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_255(z:sympy.Rational):
	#(z > 1328439/10) & (z < 134799)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(1328439, 10)), StrictLessThan(Symbol('z'), Integer(134799)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_256(z:sympy.Rational):
	#(132*x + z < -17424) & (-x**2 + 10*z + 17424 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(132), Symbol('x')), Symbol('z')), Integer(-17424)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(17424)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_257(z:sympy.Rational):
	#(z > 1349137/10) & (z < 136884)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(1349137, 10)), StrictLessThan(Symbol('z'), Integer(136884)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_258(z:sympy.Rational):
	#(133*x + z < -17689) & (-x**2 + 10*z + 17689 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(133), Symbol('x')), Symbol('z')), Integer(-17689)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(17689)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_259(z:sympy.Rational):
	#(z > 273999/2) & (z < 138985)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(273999, 2)), StrictLessThan(Symbol('z'), Integer(138985)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_260(z:sympy.Rational):
	#(134*x + z < -17956) & (-x**2 + 10*z + 17956 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(134), Symbol('x')), Symbol('z')), Integer(-17956)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(17956)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_261(z:sympy.Rational):
	#(z > 138864) & (z < 140968)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Integer(138864)), StrictLessThan(Symbol('z'), Integer(140968)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_262(z:sympy.Rational):
	#(135*x + z < -18225) & (-x**2 + 10*z + 18225 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(135), Symbol('x')), Symbol('z')), Integer(-18225)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(18225)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_263(z:sympy.Rational):
	#(z > 140980) & (z < 143100)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Integer(140980)), StrictLessThan(Symbol('z'), Integer(143100)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_264(z:sympy.Rational):
	#(136*x + z < -18496) & (-x**2 + 10*z + 18496 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(136), Symbol('x')), Symbol('z')), Integer(-18496)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(18496)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_265(z:sympy.Rational):
	#(z > 143112) & (z < 145248)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Integer(143112)), StrictLessThan(Symbol('z'), Integer(145248)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_266(z:sympy.Rational):
	#(137*x + z < -18769) & (-x**2 + 10*z + 18769 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(137), Symbol('x')), Symbol('z')), Integer(-18769)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(18769)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_267(z:sympy.Rational):
	#(z > 145260) & (z < 147412)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Integer(145260)), StrictLessThan(Symbol('z'), Integer(147412)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_268(z:sympy.Rational):
	#(138*x + z < -19044) & (-x**2 + 10*z + 19044 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(138), Symbol('x')), Symbol('z')), Integer(-19044)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(19044)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_269(z:sympy.Rational):
	#(z > 147424) & (z < 149592)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Integer(147424)), StrictLessThan(Symbol('z'), Integer(149592)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_270(z:sympy.Rational):
	#(139*x + z < -19321) & (-x**2 + 10*z + 19321 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(139), Symbol('x')), Symbol('z')), Integer(-19321)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(19321)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_271(z:sympy.Rational):
	#(z > 1493579/10) & (z < 151649)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(1493579, 10)), StrictLessThan(Symbol('z'), Integer(151649)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_272(z:sympy.Rational):
	#(140*x + z < -19600) & (-x**2 + 10*z + 19600 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(140), Symbol('x')), Symbol('z')), Integer(-19600)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(19600)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_273(z:sympy.Rational):
	#(z > 1515521/10) & (z < 153860)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(1515521, 10)), StrictLessThan(Symbol('z'), Integer(153860)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_274(z:sympy.Rational):
	#(141*x + z < -19881) & (-x**2 + 10*z + 19881 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(141), Symbol('x')), Symbol('z')), Integer(-19881)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(19881)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_275(z:sympy.Rational):
	#(z > 1537623/10) & (z < 156087)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(1537623, 10)), StrictLessThan(Symbol('z'), Integer(156087)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_276(z:sympy.Rational):
	#(142*x + z < -20164) & (-x**2 + 10*z + 20164 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(142), Symbol('x')), Symbol('z')), Integer(-20164)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(20164)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_277(z:sympy.Rational):
	#(z > 311977/2) & (z < 158330)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(311977, 2)), StrictLessThan(Symbol('z'), Integer(158330)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_278(z:sympy.Rational):
	#(143*x + z < -20449) & (-x**2 + 10*z + 20449 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(143), Symbol('x')), Symbol('z')), Integer(-20449)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(20449)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_279(z:sympy.Rational):
	#(z > 1582307/10) & (z < 160589)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(1582307, 10)), StrictLessThan(Symbol('z'), Integer(160589)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_280(z:sympy.Rational):
	#(144*x + z < -20736) & (-x**2 + 10*z + 20736 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(144), Symbol('x')), Symbol('z')), Integer(-20736)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(20736)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_281(z:sympy.Rational):
	#(z > 1604889/10) & (z < 162864)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(1604889, 10)), StrictLessThan(Symbol('z'), Integer(162864)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_282(z:sympy.Rational):
	#(145*x + z < -21025) & (-x**2 + 10*z + 21025 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(145), Symbol('x')), Symbol('z')), Integer(-21025)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(21025)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_283(z:sympy.Rational):
	#(z > 1627631/10) & (z < 165155)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(1627631, 10)), StrictLessThan(Symbol('z'), Integer(165155)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_284(z:sympy.Rational):
	#(146*x + z < -21316) & (-x**2 + 10*z + 21316 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(146), Symbol('x')), Symbol('z')), Integer(-21316)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(21316)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_285(z:sympy.Rational):
	#(z > 823974/5) & (z < 167316)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(823974, 5)), StrictLessThan(Symbol('z'), Integer(167316)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_286(z:sympy.Rational):
	#(147*x + z < -21609) & (-x**2 + 10*z + 21609 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(147), Symbol('x')), Symbol('z')), Integer(-21609)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(21609)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_287(z:sympy.Rational):
	#(z > 835496/5) & (z < 169638)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(835496, 5)), StrictLessThan(Symbol('z'), Integer(169638)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_288(z:sympy.Rational):
	#(148*x + z < -21904) & (-x**2 + 10*z + 21904 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(148), Symbol('x')), Symbol('z')), Integer(-21904)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(21904)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_289(z:sympy.Rational):
	#(z > 847098/5) & (z < 171976)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(847098, 5)), StrictLessThan(Symbol('z'), Integer(171976)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_290(z:sympy.Rational):
	#(149*x + z < -22201) & (-x**2 + 10*z + 22201 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(149), Symbol('x')), Symbol('z')), Integer(-22201)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(22201)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_291(z:sympy.Rational):
	#(z > 171756) & (z < 174330)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Integer(171756)), StrictLessThan(Symbol('z'), Integer(174330)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_292(z:sympy.Rational):
	#(150*x + z < -22500) & (-x**2 + 10*z + 22500 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(150), Symbol('x')), Symbol('z')), Integer(-22500)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(22500)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_293(z:sympy.Rational):
	#(z > 870542/5) & (z < 176700)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(870542, 5)), StrictLessThan(Symbol('z'), Integer(176700)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_294(z:sympy.Rational):
	#(151*x + z < -22801) & (-x**2 + 10*z + 22801 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(151), Symbol('x')), Symbol('z')), Integer(-22801)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(22801)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_295(z:sympy.Rational):
	#(z > 882384/5) & (z < 179086)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(882384, 5)), StrictLessThan(Symbol('z'), Integer(179086)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_296(z:sympy.Rational):
	#(152*x + z < -23104) & (-x**2 + 10*z + 23104 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(152), Symbol('x')), Symbol('z')), Integer(-23104)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(23104)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_297(z:sympy.Rational):
	#(z > 1785921/10) & (z < 181336)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(1785921, 10)), StrictLessThan(Symbol('z'), Integer(181336)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_298(z:sympy.Rational):
	#(153*x + z < -23409) & (-x**2 + 10*z + 23409 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(153), Symbol('x')), Symbol('z')), Integer(-23409)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(23409)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_299(z:sympy.Rational):
	#(z > 1809907/10) & (z < 183753)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(1809907, 10)), StrictLessThan(Symbol('z'), Integer(183753)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_300(z:sympy.Rational):
	#(154*x + z < -23716) & (-x**2 + 10*z + 23716 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(154), Symbol('x')), Symbol('z')), Integer(-23716)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(23716)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_301(z:sympy.Rational):
	#(z > 1834053/10) & (z < 186186)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(1834053, 10)), StrictLessThan(Symbol('z'), Integer(186186)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_302(z:sympy.Rational):
	#(155*x + z < -24025) & (-x**2 + 10*z + 24025 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(155), Symbol('x')), Symbol('z')), Integer(-24025)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(24025)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_303(z:sympy.Rational):
	#(z > 1858359/10) & (z < 188635)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(1858359, 10)), StrictLessThan(Symbol('z'), Integer(188635)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_304(z:sympy.Rational):
	#(156*x + z < -24336) & (-x**2 + 10*z + 24336 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(156), Symbol('x')), Symbol('z')), Integer(-24336)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(24336)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_305(z:sympy.Rational):
	#(z > 376565/2) & (z < 191100)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(376565, 2)), StrictLessThan(Symbol('z'), Integer(191100)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_306(z:sympy.Rational):
	#(157*x + z < -24649) & (-x**2 + 10*z + 24649 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(157), Symbol('x')), Symbol('z')), Integer(-24649)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(24649)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_307(z:sympy.Rational):
	#(z > 1907451/10) & (z < 193581)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(1907451, 10)), StrictLessThan(Symbol('z'), Integer(193581)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_308(z:sympy.Rational):
	#(158*x + z < -24964) & (-x**2 + 10*z + 24964 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(158), Symbol('x')), Symbol('z')), Integer(-24964)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(24964)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_309(z:sympy.Rational):
	#(z > 192944) & (z < 195920)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Integer(192944)), StrictLessThan(Symbol('z'), Integer(195920)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_310(z:sympy.Rational):
	#(159*x + z < -25281) & (-x**2 + 10*z + 25281 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(159), Symbol('x')), Symbol('z')), Integer(-25281)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(25281)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_311(z:sympy.Rational):
	#(z > 977184/5) & (z < 198432)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(977184, 5)), StrictLessThan(Symbol('z'), Integer(198432)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_312(z:sympy.Rational):
	#(160*x + z < -25600) & (-x**2 + 10*z + 25600 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(160), Symbol('x')), Symbol('z')), Integer(-25600)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(25600)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_313(z:sympy.Rational):
	#(z > 989728/5) & (z < 200960)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(989728, 5)), StrictLessThan(Symbol('z'), Integer(200960)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_314(z:sympy.Rational):
	#(161*x + z < -25921) & (-x**2 + 10*z + 25921 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(161), Symbol('x')), Symbol('z')), Integer(-25921)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(25921)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_315(z:sympy.Rational):
	#(z > 1002352/5) & (z < 203504)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(1002352, 5)), StrictLessThan(Symbol('z'), Integer(203504)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_316(z:sympy.Rational):
	#(162*x + z < -26244) & (-x**2 + 10*z + 26244 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(162), Symbol('x')), Symbol('z')), Integer(-26244)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(26244)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_317(z:sympy.Rational):
	#(z > 1015056/5) & (z < 206064)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(1015056, 5)), StrictLessThan(Symbol('z'), Integer(206064)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_318(z:sympy.Rational):
	#(163*x + z < -26569) & (-x**2 + 10*z + 26569 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(163), Symbol('x')), Symbol('z')), Integer(-26569)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(26569)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_319(z:sympy.Rational):
	#(z > 205568) & (z < 208640)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Integer(205568)), StrictLessThan(Symbol('z'), Integer(208640)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_320(z:sympy.Rational):
	#(164*x + z < -26896) & (-x**2 + 10*z + 26896 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(164), Symbol('x')), Symbol('z')), Integer(-26896)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(26896)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_321(z:sympy.Rational):
	#(z > 415701/2) & (z < 211068)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(415701, 2)), StrictLessThan(Symbol('z'), Integer(211068)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_322(z:sympy.Rational):
	#(165*x + z < -27225) & (-x**2 + 10*z + 27225 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(165), Symbol('x')), Symbol('z')), Integer(-27225)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(27225)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_323(z:sympy.Rational):
	#(z > 420875/2) & (z < 213675)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(420875, 2)), StrictLessThan(Symbol('z'), Integer(213675)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_324(z:sympy.Rational):
	#(166*x + z < -27556) & (-x**2 + 10*z + 27556 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(166), Symbol('x')), Symbol('z')), Integer(-27556)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(27556)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_325(z:sympy.Rational):
	#(z > 426081/2) & (z < 216298)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(426081, 2)), StrictLessThan(Symbol('z'), Integer(216298)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_326(z:sympy.Rational):
	#(167*x + z < -27889) & (-x**2 + 10*z + 27889 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(167), Symbol('x')), Symbol('z')), Integer(-27889)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(27889)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_327(z:sympy.Rational):
	#(z > 431319/2) & (z < 218937)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(431319, 2)), StrictLessThan(Symbol('z'), Integer(218937)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_328(z:sympy.Rational):
	#(168*x + z < -28224) & (-x**2 + 10*z + 28224 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(168), Symbol('x')), Symbol('z')), Integer(-28224)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(28224)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_329(z:sympy.Rational):
	#(z > 436589/2) & (z < 221592)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(436589, 2)), StrictLessThan(Symbol('z'), Integer(221592)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_330(z:sympy.Rational):
	#(169*x + z < -28561) & (-x**2 + 10*z + 28561 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(169), Symbol('x')), Symbol('z')), Integer(-28561)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(28561)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_331(z:sympy.Rational):
	#(z > 441891/2) & (z < 224263)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(441891, 2)), StrictLessThan(Symbol('z'), Integer(224263)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_332(z:sympy.Rational):
	#(170*x + z < -28900) & (-x**2 + 10*z + 28900 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(170), Symbol('x')), Symbol('z')), Integer(-28900)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(28900)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_333(z:sympy.Rational):
	#(z > 447225/2) & (z < 226950)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(447225, 2)), StrictLessThan(Symbol('z'), Integer(226950)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_334(z:sympy.Rational):
	#(171*x + z < -29241) & (-x**2 + 10*z + 29241 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(171), Symbol('x')), Symbol('z')), Integer(-29241)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(29241)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_335(z:sympy.Rational):
	#(z > 1129964/5) & (z < 229482)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(1129964, 5)), StrictLessThan(Symbol('z'), Integer(229482)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_336(z:sympy.Rational):
	#(172*x + z < -29584) & (-x**2 + 10*z + 29584 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(172), Symbol('x')), Symbol('z')), Integer(-29584)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(29584)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_337(z:sympy.Rational):
	#(z > 228690) & (z < 232200)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Integer(228690)), StrictLessThan(Symbol('z'), Integer(232200)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_338(z:sympy.Rational):
	#(173*x + z < -29929) & (-x**2 + 10*z + 29929 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(173), Symbol('x')), Symbol('z')), Integer(-29929)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(29929)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_339(z:sympy.Rational):
	#(z > 1157016/5) & (z < 234934)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(1157016, 5)), StrictLessThan(Symbol('z'), Integer(234934)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_340(z:sympy.Rational):
	#(174*x + z < -30276) & (-x**2 + 10*z + 30276 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(174), Symbol('x')), Symbol('z')), Integer(-30276)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(30276)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_341(z:sympy.Rational):
	#(z > 1170662/5) & (z < 237684)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(1170662, 5)), StrictLessThan(Symbol('z'), Integer(237684)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_342(z:sympy.Rational):
	#(175*x + z < -30625) & (-x**2 + 10*z + 30625 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(175), Symbol('x')), Symbol('z')), Integer(-30625)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(30625)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_343(z:sympy.Rational):
	#(z > 1184388/5) & (z < 240450)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(1184388, 5)), StrictLessThan(Symbol('z'), Integer(240450)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_344(z:sympy.Rational):
	#(176*x + z < -30976) & (-x**2 + 10*z + 30976 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(176), Symbol('x')), Symbol('z')), Integer(-30976)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(30976)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_345(z:sympy.Rational):
	#(z > 1198194/5) & (z < 243232)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(1198194, 5)), StrictLessThan(Symbol('z'), Integer(243232)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_346(z:sympy.Rational):
	#(177*x + z < -31329) & (-x**2 + 10*z + 31329 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(177), Symbol('x')), Symbol('z')), Integer(-31329)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(31329)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_347(z:sympy.Rational):
	#(z > 2421027/10) & (z < 245853)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(2421027, 10)), StrictLessThan(Symbol('z'), Integer(245853)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_348(z:sympy.Rational):
	#(178*x + z < -31684) & (-x**2 + 10*z + 31684 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(178), Symbol('x')), Symbol('z')), Integer(-31684)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(31684)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_349(z:sympy.Rational):
	#(z > 2448941/10) & (z < 248666)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(2448941, 10)), StrictLessThan(Symbol('z'), Integer(248666)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_350(z:sympy.Rational):
	#(179*x + z < -32041) & (-x**2 + 10*z + 32041 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(179), Symbol('x')), Symbol('z')), Integer(-32041)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(32041)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_351(z:sympy.Rational):
	#(z > 495403/2) & (z < 251495)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(495403, 2)), StrictLessThan(Symbol('z'), Integer(251495)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_352(z:sympy.Rational):
	#(180*x + z < -32400) & (-x**2 + 10*z + 32400 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(180), Symbol('x')), Symbol('z')), Integer(-32400)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(32400)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_353(z:sympy.Rational):
	#(z > 2505249/10) & (z < 254340)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(2505249, 10)), StrictLessThan(Symbol('z'), Integer(254340)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_354(z:sympy.Rational):
	#(181*x + z < -32761) & (-x**2 + 10*z + 32761 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(181), Symbol('x')), Symbol('z')), Integer(-32761)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(32761)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_355(z:sympy.Rational):
	#(z > 2533643/10) & (z < 257201)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(2533643, 10)), StrictLessThan(Symbol('z'), Integer(257201)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_356(z:sympy.Rational):
	#(182*x + z < -33124) & (-x**2 + 10*z + 33124 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(182), Symbol('x')), Symbol('z')), Integer(-33124)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(33124)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_357(z:sympy.Rational):
	#(z > 2562197/10) & (z < 260078)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(2562197, 10)), StrictLessThan(Symbol('z'), Integer(260078)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_358(z:sympy.Rational):
	#(183*x + z < -33489) & (-x**2 + 10*z + 33489 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(183), Symbol('x')), Symbol('z')), Integer(-33489)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(33489)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_359(z:sympy.Rational):
	#(z > 2590911/10) & (z < 262971)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(2590911, 10)), StrictLessThan(Symbol('z'), Integer(262971)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_360(z:sympy.Rational):
	#(184*x + z < -33856) & (-x**2 + 10*z + 33856 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(184), Symbol('x')), Symbol('z')), Integer(-33856)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(33856)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_361(z:sympy.Rational):
	#(z > 1308264/5) & (z < 265696)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(1308264, 5)), StrictLessThan(Symbol('z'), Integer(265696)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_362(z:sympy.Rational):
	#(185*x + z < -34225) & (-x**2 + 10*z + 34225 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(185), Symbol('x')), Symbol('z')), Integer(-34225)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(34225)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_363(z:sympy.Rational):
	#(z > 1322772/5) & (z < 268620)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(1322772, 5)), StrictLessThan(Symbol('z'), Integer(268620)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_364(z:sympy.Rational):
	#(186*x + z < -34596) & (-x**2 + 10*z + 34596 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(186), Symbol('x')), Symbol('z')), Integer(-34596)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(34596)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_365(z:sympy.Rational):
	#(z > 267472) & (z < 271560)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Integer(267472)), StrictLessThan(Symbol('z'), Integer(271560)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_366(z:sympy.Rational):
	#(187*x + z < -34969) & (-x**2 + 10*z + 34969 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(187), Symbol('x')), Symbol('z')), Integer(-34969)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(34969)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_367(z:sympy.Rational):
	#(z > 1352028/5) & (z < 274516)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(1352028, 5)), StrictLessThan(Symbol('z'), Integer(274516)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_368(z:sympy.Rational):
	#(188*x + z < -35344) & (-x**2 + 10*z + 35344 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(188), Symbol('x')), Symbol('z')), Integer(-35344)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(35344)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_369(z:sympy.Rational):
	#(z > 1366776/5) & (z < 277488)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(1366776, 5)), StrictLessThan(Symbol('z'), Integer(277488)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_370(z:sympy.Rational):
	#(189*x + z < -35721) & (-x**2 + 10*z + 35721 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(189), Symbol('x')), Symbol('z')), Integer(-35721)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(35721)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_371(z:sympy.Rational):
	#(z > 1381604/5) & (z < 280476)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(1381604, 5)), StrictLessThan(Symbol('z'), Integer(280476)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_372(z:sympy.Rational):
	#(190*x + z < -36100) & (-x**2 + 10*z + 36100 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(190), Symbol('x')), Symbol('z')), Integer(-36100)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(36100)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_373(z:sympy.Rational):
	#(z > 1396512/5) & (z < 283480)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(1396512, 5)), StrictLessThan(Symbol('z'), Integer(283480)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_374(z:sympy.Rational):
	#(191*x + z < -36481) & (-x**2 + 10*z + 36481 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(191), Symbol('x')), Symbol('z')), Integer(-36481)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(36481)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_375(z:sympy.Rational):
	#(z > 2819619/10) & (z < 286309)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(2819619, 10)), StrictLessThan(Symbol('z'), Integer(286309)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_376(z:sympy.Rational):
	#(192*x + z < -36864) & (-x**2 + 10*z + 36864 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(192), Symbol('x')), Symbol('z')), Integer(-36864)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(36864)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_377(z:sympy.Rational):
	#(z > 2849737/10) & (z < 289344)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(2849737, 10)), StrictLessThan(Symbol('z'), Integer(289344)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_378(z:sympy.Rational):
	#(193*x + z < -37249) & (-x**2 + 10*z + 37249 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(193), Symbol('x')), Symbol('z')), Integer(-37249)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(37249)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_379(z:sympy.Rational):
	#(z > 576003/2) & (z < 292395)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(576003, 2)), StrictLessThan(Symbol('z'), Integer(292395)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_380(z:sympy.Rational):
	#(194*x + z < -37636) & (-x**2 + 10*z + 37636 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(194), Symbol('x')), Symbol('z')), Integer(-37636)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(37636)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_381(z:sympy.Rational):
	#(z > 2910453/10) & (z < 295462)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(2910453, 10)), StrictLessThan(Symbol('z'), Integer(295462)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_382(z:sympy.Rational):
	#(195*x + z < -38025) & (-x**2 + 10*z + 38025 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(195), Symbol('x')), Symbol('z')), Integer(-38025)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(38025)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_383(z:sympy.Rational):
	#(z > 2941051/10) & (z < 298545)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(2941051, 10)), StrictLessThan(Symbol('z'), Integer(298545)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_384(z:sympy.Rational):
	#(196*x + z < -38416) & (-x**2 + 10*z + 38416 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(196), Symbol('x')), Symbol('z')), Integer(-38416)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(38416)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_385(z:sympy.Rational):
	#(z > 2971809/10) & (z < 301644)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(2971809, 10)), StrictLessThan(Symbol('z'), Integer(301644)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_386(z:sympy.Rational):
	#(197*x + z < -38809) & (-x**2 + 10*z + 38809 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(197), Symbol('x')), Symbol('z')), Integer(-38809)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(38809)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_387(z:sympy.Rational):
	#(z > 3002727/10) & (z < 304759)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(3002727, 10)), StrictLessThan(Symbol('z'), Integer(304759)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_388(z:sympy.Rational):
	#(198*x + z < -39204) & (-x**2 + 10*z + 39204 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(198), Symbol('x')), Symbol('z')), Integer(-39204)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(39204)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_389(z:sympy.Rational):
	#(z > 303030) & (z < 307692)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Integer(303030)), StrictLessThan(Symbol('z'), Integer(307692)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_390(z:sympy.Rational):
	#(199*x + z < -39601) & (-x**2 + 10*z + 39601 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(199), Symbol('x')), Symbol('z')), Integer(-39601)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(39601)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_391(z:sympy.Rational):
	#(z > 306152) & (z < 310838)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Integer(306152)), StrictLessThan(Symbol('z'), Integer(310838)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_392(z:sympy.Rational):
	#(200*x + z < -40000) & (-x**2 + 10*z + 40000 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(200), Symbol('x')), Symbol('z')), Integer(-40000)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(40000)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_393(z:sympy.Rational):
	#(z > 309290) & (z < 314000)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Integer(309290)), StrictLessThan(Symbol('z'), Integer(314000)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_394(z:sympy.Rational):
	#(201*x + z < -40401) & (-x**2 + 10*z + 40401 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(201), Symbol('x')), Symbol('z')), Integer(-40401)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(40401)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_395(z:sympy.Rational):
	#(z > 312444) & (z < 317178)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Integer(312444)), StrictLessThan(Symbol('z'), Integer(317178)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_396(z:sympy.Rational):
	#(202*x + z < -40804) & (-x**2 + 10*z + 40804 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(202), Symbol('x')), Symbol('z')), Integer(-40804)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(40804)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_397(z:sympy.Rational):
	#(z > 315614) & (z < 320372)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Integer(315614)), StrictLessThan(Symbol('z'), Integer(320372)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_398(z:sympy.Rational):
	#(203*x + z < -41209) & (-x**2 + 10*z + 41209 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(203), Symbol('x')), Symbol('z')), Integer(-41209)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(41209)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_399(z:sympy.Rational):
	#(z > 318800) & (z < 323582)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Integer(318800)), StrictLessThan(Symbol('z'), Integer(323582)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_400(z:sympy.Rational):
	#(204*x + z < -41616) & (-x**2 + 10*z + 41616 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(204), Symbol('x')), Symbol('z')), Integer(-41616)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(41616)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_401(z:sympy.Rational):
	#(z > 3216409/10) & (z < 326604)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(3216409, 10)), StrictLessThan(Symbol('z'), Integer(326604)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_402(z:sympy.Rational):
	#(205*x + z < -42025) & (-x**2 + 10*z + 42025 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(205), Symbol('x')), Symbol('z')), Integer(-42025)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(42025)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_403(z:sympy.Rational):
	#(z > 3248571/10) & (z < 329845)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(3248571, 10)), StrictLessThan(Symbol('z'), Integer(329845)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_404(z:sympy.Rational):
	#(206*x + z < -42436) & (-x**2 + 10*z + 42436 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(206), Symbol('x')), Symbol('z')), Integer(-42436)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(42436)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_405(z:sympy.Rational):
	#(z > 3280893/10) & (z < 333102)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(3280893, 10)), StrictLessThan(Symbol('z'), Integer(333102)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_406(z:sympy.Rational):
	#(207*x + z < -42849) & (-x**2 + 10*z + 42849 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(207), Symbol('x')), Symbol('z')), Integer(-42849)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(42849)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_407(z:sympy.Rational):
	#(z > 662675/2) & (z < 336375)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(662675, 2)), StrictLessThan(Symbol('z'), Integer(336375)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_408(z:sympy.Rational):
	#(208*x + z < -43264) & (-x**2 + 10*z + 43264 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(208), Symbol('x')), Symbol('z')), Integer(-43264)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(43264)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_409(z:sympy.Rational):
	#(z > 3346017/10) & (z < 339664)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(3346017, 10)), StrictLessThan(Symbol('z'), Integer(339664)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_410(z:sympy.Rational):
	#(209*x + z < -43681) & (-x**2 + 10*z + 43681 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(209), Symbol('x')), Symbol('z')), Integer(-43681)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(43681)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_411(z:sympy.Rational):
	#(z > 3378819/10) & (z < 342969)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(3378819, 10)), StrictLessThan(Symbol('z'), Integer(342969)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_412(z:sympy.Rational):
	#(210*x + z < -44100) & (-x**2 + 10*z + 44100 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(210), Symbol('x')), Symbol('z')), Integer(-44100)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(44100)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_413(z:sympy.Rational):
	#(z > 3411781/10) & (z < 346290)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(3411781, 10)), StrictLessThan(Symbol('z'), Integer(346290)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_414(z:sympy.Rational):
	#(211*x + z < -44521) & (-x**2 + 10*z + 44521 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(211), Symbol('x')), Symbol('z')), Integer(-44521)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(44521)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_415(z:sympy.Rational):
	#(z > 1720584/5) & (z < 349416)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(1720584, 5)), StrictLessThan(Symbol('z'), Integer(349416)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_416(z:sympy.Rational):
	#(212*x + z < -44944) & (-x**2 + 10*z + 44944 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(212), Symbol('x')), Symbol('z')), Integer(-44944)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(44944)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_417(z:sympy.Rational):
	#(z > 1737216/5) & (z < 352768)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(1737216, 5)), StrictLessThan(Symbol('z'), Integer(352768)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_418(z:sympy.Rational):
	#(213*x + z < -45369) & (-x**2 + 10*z + 45369 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(213), Symbol('x')), Symbol('z')), Integer(-45369)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(45369)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_419(z:sympy.Rational):
	#(z > 1753928/5) & (z < 356136)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(1753928, 5)), StrictLessThan(Symbol('z'), Integer(356136)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_420(z:sympy.Rational):
	#(214*x + z < -45796) & (-x**2 + 10*z + 45796 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(214), Symbol('x')), Symbol('z')), Integer(-45796)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(45796)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_421(z:sympy.Rational):
	#(z > 354144) & (z < 359520)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Integer(354144)), StrictLessThan(Symbol('z'), Integer(359520)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_422(z:sympy.Rational):
	#(215*x + z < -46225) & (-x**2 + 10*z + 46225 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(215), Symbol('x')), Symbol('z')), Integer(-46225)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(46225)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_423(z:sympy.Rational):
	#(z > 1787592/5) & (z < 362920)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(1787592, 5)), StrictLessThan(Symbol('z'), Integer(362920)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_424(z:sympy.Rational):
	#(216*x + z < -46656) & (-x**2 + 10*z + 46656 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(216), Symbol('x')), Symbol('z')), Integer(-46656)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(46656)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_425(z:sympy.Rational):
	#(z > 1804544/5) & (z < 366336)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(1804544, 5)), StrictLessThan(Symbol('z'), Integer(366336)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_426(z:sympy.Rational):
	#(217*x + z < -47089) & (-x**2 + 10*z + 47089 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(217), Symbol('x')), Symbol('z')), Integer(-47089)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(47089)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_427(z:sympy.Rational):
	#(z > 1821576/5) & (z < 369768)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(1821576, 5)), StrictLessThan(Symbol('z'), Integer(369768)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_428(z:sympy.Rational):
	#(218*x + z < -47524) & (-x**2 + 10*z + 47524 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(218), Symbol('x')), Symbol('z')), Integer(-47524)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(47524)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_429(z:sympy.Rational):
	#(z > 3673517/10) & (z < 372998)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(3673517, 10)), StrictLessThan(Symbol('z'), Integer(372998)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_430(z:sympy.Rational):
	#(219*x + z < -47961) & (-x**2 + 10*z + 47961 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(219), Symbol('x')), Symbol('z')), Integer(-47961)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(47961)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_431(z:sympy.Rational):
	#(z > 3707883/10) & (z < 376461)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(3707883, 10)), StrictLessThan(Symbol('z'), Integer(376461)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_432(z:sympy.Rational):
	#(220*x + z < -48400) & (-x**2 + 10*z + 48400 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(220), Symbol('x')), Symbol('z')), Integer(-48400)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(48400)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_433(z:sympy.Rational):
	#(z > 3742409/10) & (z < 379940)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(3742409, 10)), StrictLessThan(Symbol('z'), Integer(379940)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_434(z:sympy.Rational):
	#(221*x + z < -48841) & (-x**2 + 10*z + 48841 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(221), Symbol('x')), Symbol('z')), Integer(-48841)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(48841)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_435(z:sympy.Rational):
	#(z > 755419/2) & (z < 383435)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(755419, 2)), StrictLessThan(Symbol('z'), Integer(383435)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_436(z:sympy.Rational):
	#(222*x + z < -49284) & (-x**2 + 10*z + 49284 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(222), Symbol('x')), Symbol('z')), Integer(-49284)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(49284)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_437(z:sympy.Rational):
	#(z > 3811941/10) & (z < 386946)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(3811941, 10)), StrictLessThan(Symbol('z'), Integer(386946)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_438(z:sympy.Rational):
	#(223*x + z < -49729) & (-x**2 + 10*z + 49729 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(223), Symbol('x')), Symbol('z')), Integer(-49729)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(49729)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_439(z:sympy.Rational):
	#(z > 3846947/10) & (z < 390473)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(3846947, 10)), StrictLessThan(Symbol('z'), Integer(390473)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_440(z:sympy.Rational):
	#(224*x + z < -50176) & (-x**2 + 10*z + 50176 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(224), Symbol('x')), Symbol('z')), Integer(-50176)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(50176)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_441(z:sympy.Rational):
	#(z > 3882113/10) & (z < 394016)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(3882113, 10)), StrictLessThan(Symbol('z'), Integer(394016)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_442(z:sympy.Rational):
	#(225*x + z < -50625) & (-x**2 + 10*z + 50625 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(225), Symbol('x')), Symbol('z')), Integer(-50625)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(50625)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_443(z:sympy.Rational):
	#(z > 1956728/5) & (z < 397350)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(1956728, 5)), StrictLessThan(Symbol('z'), Integer(397350)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_444(z:sympy.Rational):
	#(226*x + z < -51076) & (-x**2 + 10*z + 51076 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(226), Symbol('x')), Symbol('z')), Integer(-51076)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(51076)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_445(z:sympy.Rational):
	#(z > 1974462/5) & (z < 400924)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(1974462, 5)), StrictLessThan(Symbol('z'), Integer(400924)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_446(z:sympy.Rational):
	#(227*x + z < -51529) & (-x**2 + 10*z + 51529 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(227), Symbol('x')), Symbol('z')), Integer(-51529)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(51529)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_447(z:sympy.Rational):
	#(z > 1992276/5) & (z < 404514)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(1992276, 5)), StrictLessThan(Symbol('z'), Integer(404514)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_448(z:sympy.Rational):
	#(228*x + z < -51984) & (-x**2 + 10*z + 51984 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(228), Symbol('x')), Symbol('z')), Integer(-51984)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(51984)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_449(z:sympy.Rational):
	#(z > 402034) & (z < 408120)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Integer(402034)), StrictLessThan(Symbol('z'), Integer(408120)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_450(z:sympy.Rational):
	#(229*x + z < -52441) & (-x**2 + 10*z + 52441 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(229), Symbol('x')), Symbol('z')), Integer(-52441)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(52441)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_451(z:sympy.Rational):
	#(z > 2028144/5) & (z < 411742)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(2028144, 5)), StrictLessThan(Symbol('z'), Integer(411742)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_452(z:sympy.Rational):
	#(230*x + z < -52900) & (-x**2 + 10*z + 52900 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(230), Symbol('x')), Symbol('z')), Integer(-52900)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(52900)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_453(z:sympy.Rational):
	#(z > 2046198/5) & (z < 415380)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(2046198, 5)), StrictLessThan(Symbol('z'), Integer(415380)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_454(z:sympy.Rational):
	#(231*x + z < -53361) & (-x**2 + 10*z + 53361 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(231), Symbol('x')), Symbol('z')), Integer(-53361)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(53361)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_455(z:sympy.Rational):
	#(z > 2064332/5) & (z < 419034)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(2064332, 5)), StrictLessThan(Symbol('z'), Integer(419034)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_456(z:sympy.Rational):
	#(232*x + z < -53824) & (-x**2 + 10*z + 53824 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(232), Symbol('x')), Symbol('z')), Integer(-53824)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(53824)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_457(z:sympy.Rational):
	#(z > 832197/2) & (z < 422472)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(832197, 2)), StrictLessThan(Symbol('z'), Integer(422472)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_458(z:sympy.Rational):
	#(233*x + z < -54289) & (-x**2 + 10*z + 54289 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(233), Symbol('x')), Symbol('z')), Integer(-54289)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(54289)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_459(z:sympy.Rational):
	#(z > 839511/2) & (z < 426157)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(839511, 2)), StrictLessThan(Symbol('z'), Integer(426157)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_460(z:sympy.Rational):
	#(234*x + z < -54756) & (-x**2 + 10*z + 54756 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(234), Symbol('x')), Symbol('z')), Integer(-54756)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(54756)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_461(z:sympy.Rational):
	#(z > 846857/2) & (z < 429858)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(846857, 2)), StrictLessThan(Symbol('z'), Integer(429858)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_462(z:sympy.Rational):
	#(235*x + z < -55225) & (-x**2 + 10*z + 55225 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(235), Symbol('x')), Symbol('z')), Integer(-55225)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(55225)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_463(z:sympy.Rational):
	#(z > 854235/2) & (z < 433575)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(854235, 2)), StrictLessThan(Symbol('z'), Integer(433575)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_464(z:sympy.Rational):
	#(236*x + z < -55696) & (-x**2 + 10*z + 55696 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(236), Symbol('x')), Symbol('z')), Integer(-55696)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(55696)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_465(z:sympy.Rational):
	#(z > 861645/2) & (z < 437308)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(861645, 2)), StrictLessThan(Symbol('z'), Integer(437308)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_466(z:sympy.Rational):
	#(237*x + z < -56169) & (-x**2 + 10*z + 56169 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(237), Symbol('x')), Symbol('z')), Integer(-56169)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(56169)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_467(z:sympy.Rational):
	#(z > 869087/2) & (z < 441057)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(869087, 2)), StrictLessThan(Symbol('z'), Integer(441057)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_468(z:sympy.Rational):
	#(238*x + z < -56644) & (-x**2 + 10*z + 56644 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(238), Symbol('x')), Symbol('z')), Integer(-56644)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(56644)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_469(z:sympy.Rational):
	#(z > 876561/2) & (z < 444822)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(876561, 2)), StrictLessThan(Symbol('z'), Integer(444822)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_470(z:sympy.Rational):
	#(239*x + z < -57121) & (-x**2 + 10*z + 57121 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(239), Symbol('x')), Symbol('z')), Integer(-57121)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(57121)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_471(z:sympy.Rational):
	#(z > 2208052/5) & (z < 448364)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(2208052, 5)), StrictLessThan(Symbol('z'), Integer(448364)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_472(z:sympy.Rational):
	#(240*x + z < -57600) & (-x**2 + 10*z + 57600 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(240), Symbol('x')), Symbol('z')), Integer(-57600)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(57600)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_473(z:sympy.Rational):
	#(z > 2226888/5) & (z < 452160)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(2226888, 5)), StrictLessThan(Symbol('z'), Integer(452160)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_474(z:sympy.Rational):
	#(241*x + z < -58081) & (-x**2 + 10*z + 58081 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(241), Symbol('x')), Symbol('z')), Integer(-58081)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(58081)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_475(z:sympy.Rational):
	#(z > 2245804/5) & (z < 455972)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(2245804, 5)), StrictLessThan(Symbol('z'), Integer(455972)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_476(z:sympy.Rational):
	#(242*x + z < -58564) & (-x**2 + 10*z + 58564 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(242), Symbol('x')), Symbol('z')), Integer(-58564)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(58564)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_477(z:sympy.Rational):
	#(z > 452960) & (z < 459800)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Integer(452960)), StrictLessThan(Symbol('z'), Integer(459800)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_478(z:sympy.Rational):
	#(243*x + z < -59049) & (-x**2 + 10*z + 59049 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(243), Symbol('x')), Symbol('z')), Integer(-59049)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(59049)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_479(z:sympy.Rational):
	#(z > 2283876/5) & (z < 463644)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(2283876, 5)), StrictLessThan(Symbol('z'), Integer(463644)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_480(z:sympy.Rational):
	#(244*x + z < -59536) & (-x**2 + 10*z + 59536 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(244), Symbol('x')), Symbol('z')), Integer(-59536)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(59536)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_481(z:sympy.Rational):
	#(z > 2303032/5) & (z < 467504)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(2303032, 5)), StrictLessThan(Symbol('z'), Integer(467504)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_482(z:sympy.Rational):
	#(245*x + z < -60025) & (-x**2 + 10*z + 60025 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(245), Symbol('x')), Symbol('z')), Integer(-60025)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(60025)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_483(z:sympy.Rational):
	#(z > 2322268/5) & (z < 471380)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(2322268, 5)), StrictLessThan(Symbol('z'), Integer(471380)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_484(z:sympy.Rational):
	#(246*x + z < -60516) & (-x**2 + 10*z + 60516 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(246), Symbol('x')), Symbol('z')), Integer(-60516)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(60516)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_485(z:sympy.Rational):
	#(z > 2341584/5) & (z < 475272)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(2341584, 5)), StrictLessThan(Symbol('z'), Integer(475272)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_486(z:sympy.Rational):
	#(247*x + z < -61009) & (-x**2 + 10*z + 61009 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(247), Symbol('x')), Symbol('z')), Integer(-61009)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(61009)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_487(z:sympy.Rational):
	#(z > 4717587/10) & (z < 478933)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(4717587, 10)), StrictLessThan(Symbol('z'), Integer(478933)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_488(z:sympy.Rational):
	#(248*x + z < -61504) & (-x**2 + 10*z + 61504 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(248), Symbol('x')), Symbol('z')), Integer(-61504)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(61504)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_489(z:sympy.Rational):
	#(z > 4756521/10) & (z < 482856)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(4756521, 10)), StrictLessThan(Symbol('z'), Integer(482856)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_490(z:sympy.Rational):
	#(249*x + z < -62001) & (-x**2 + 10*z + 62001 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(249), Symbol('x')), Symbol('z')), Integer(-62001)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(62001)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_491(z:sympy.Rational):
	#(z > 959123/2) & (z < 486795)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(959123, 2)), StrictLessThan(Symbol('z'), Integer(486795)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_492(z:sympy.Rational):
	#(250*x + z < -62500) & (-x**2 + 10*z + 62500 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(250), Symbol('x')), Symbol('z')), Integer(-62500)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(62500)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_493(z:sympy.Rational):
	#(z > 4834869/10) & (z < 490750)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(4834869, 10)), StrictLessThan(Symbol('z'), Integer(490750)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_494(z:sympy.Rational):
	#(251*x + z < -63001) & (-x**2 + 10*z + 63001 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(251), Symbol('x')), Symbol('z')), Integer(-63001)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(63001)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_495(z:sympy.Rational):
	#(z > 4874283/10) & (z < 494721)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(4874283, 10)), StrictLessThan(Symbol('z'), Integer(494721)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_496(z:sympy.Rational):
	#(252*x + z < -63504) & (-x**2 + 10*z + 63504 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(252), Symbol('x')), Symbol('z')), Integer(-63504)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(63504)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_497(z:sympy.Rational):
	#(z > 4913857/10) & (z < 498708)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(4913857, 10)), StrictLessThan(Symbol('z'), Integer(498708)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_498(z:sympy.Rational):
	#(253*x + z < -64009) & (-x**2 + 10*z + 64009 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(253), Symbol('x')), Symbol('z')), Integer(-64009)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(64009)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_499(z:sympy.Rational):
	#(z > 4953591/10) & (z < 502711)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(4953591, 10)), StrictLessThan(Symbol('z'), Integer(502711)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_500(z:sympy.Rational):
	#(254*x + z < -64516) & (-x**2 + 10*z + 64516 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(254), Symbol('x')), Symbol('z')), Integer(-64516)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(64516)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_501(z:sympy.Rational):
	#(z > 2494494/5) & (z < 506476)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(2494494, 5)), StrictLessThan(Symbol('z'), Integer(506476)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_502(z:sympy.Rational):
	#(255*x + z < -65025) & (-x**2 + 10*z + 65025 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(255), Symbol('x')), Symbol('z')), Integer(-65025)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(65025)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_503(z:sympy.Rational):
	#(z > 2514512/5) & (z < 510510)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(2514512, 5)), StrictLessThan(Symbol('z'), Integer(510510)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_504(z:sympy.Rational):
	#(256*x + z < -65536) & (-x**2 + 10*z + 65536 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(256), Symbol('x')), Symbol('z')), Integer(-65536)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(65536)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_505(z:sympy.Rational):
	#(z > 506922) & (z < 514560)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Integer(506922)), StrictLessThan(Symbol('z'), Integer(514560)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_506(z:sympy.Rational):
	#(257*x + z < -66049) & (-x**2 + 10*z + 66049 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(257), Symbol('x')), Symbol('z')), Integer(-66049)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(66049)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_507(z:sympy.Rational):
	#(z > 2554788/5) & (z < 518626)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(2554788, 5)), StrictLessThan(Symbol('z'), Integer(518626)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_508(z:sympy.Rational):
	#(258*x + z < -66564) & (-x**2 + 10*z + 66564 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(258), Symbol('x')), Symbol('z')), Integer(-66564)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(66564)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_509(z:sympy.Rational):
	#(z > 2575046/5) & (z < 522708)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(2575046, 5)), StrictLessThan(Symbol('z'), Integer(522708)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_510(z:sympy.Rational):
	#(259*x + z < -67081) & (-x**2 + 10*z + 67081 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(259), Symbol('x')), Symbol('z')), Integer(-67081)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(67081)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_511(z:sympy.Rational):
	#(z > 2595384/5) & (z < 526806)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(2595384, 5)), StrictLessThan(Symbol('z'), Integer(526806)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_512(z:sympy.Rational):
	#(260*x + z < -67600) & (-x**2 + 10*z + 67600 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(260), Symbol('x')), Symbol('z')), Integer(-67600)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(67600)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_513(z:sympy.Rational):
	#(z > 2615802/5) & (z < 530920)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(2615802, 5)), StrictLessThan(Symbol('z'), Integer(530920)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_514(z:sympy.Rational):
	#(261*x + z < -68121) & (-x**2 + 10*z + 68121 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(261), Symbol('x')), Symbol('z')), Integer(-68121)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(68121)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_515(z:sympy.Rational):
	#(z > 5267979/10) & (z < 534789)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(5267979, 10)), StrictLessThan(Symbol('z'), Integer(534789)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_516(z:sympy.Rational):
	#(262*x + z < -68644) & (-x**2 + 10*z + 68644 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(262), Symbol('x')), Symbol('z')), Integer(-68644)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(68644)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_517(z:sympy.Rational):
	#(z > 5309117/10) & (z < 538934)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(5309117, 10)), StrictLessThan(Symbol('z'), Integer(538934)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_518(z:sympy.Rational):
	#(263*x + z < -69169) & (-x**2 + 10*z + 69169 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(263), Symbol('x')), Symbol('z')), Integer(-69169)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(69169)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_519(z:sympy.Rational):
	#(z > 1070083/2) & (z < 543095)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(1070083, 2)), StrictLessThan(Symbol('z'), Integer(543095)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_520(z:sympy.Rational):
	#(264*x + z < -69696) & (-x**2 + 10*z + 69696 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(264), Symbol('x')), Symbol('z')), Integer(-69696)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(69696)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_521(z:sympy.Rational):
	#(z > 5391873/10) & (z < 547272)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(5391873, 10)), StrictLessThan(Symbol('z'), Integer(547272)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_522(z:sympy.Rational):
	#(265*x + z < -70225) & (-x**2 + 10*z + 70225 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(265), Symbol('x')), Symbol('z')), Integer(-70225)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(70225)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_523(z:sympy.Rational):
	#(z > 5433491/10) & (z < 551465)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(5433491, 10)), StrictLessThan(Symbol('z'), Integer(551465)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_524(z:sympy.Rational):
	#(266*x + z < -70756) & (-x**2 + 10*z + 70756 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(266), Symbol('x')), Symbol('z')), Integer(-70756)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(70756)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_525(z:sympy.Rational):
	#(z > 5475269/10) & (z < 555674)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(5475269, 10)), StrictLessThan(Symbol('z'), Integer(555674)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_526(z:sympy.Rational):
	#(267*x + z < -71289) & (-x**2 + 10*z + 71289 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(267), Symbol('x')), Symbol('z')), Integer(-71289)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(71289)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_527(z:sympy.Rational):
	#(z > 5517207/10) & (z < 559899)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(5517207, 10)), StrictLessThan(Symbol('z'), Integer(559899)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_528(z:sympy.Rational):
	#(268*x + z < -71824) & (-x**2 + 10*z + 71824 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(268), Symbol('x')), Symbol('z')), Integer(-71824)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(71824)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_529(z:sympy.Rational):
	#(z > 555456) & (z < 563872)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Integer(555456)), StrictLessThan(Symbol('z'), Integer(563872)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_530(z:sympy.Rational):
	#(269*x + z < -72361) & (-x**2 + 10*z + 72361 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(269), Symbol('x')), Symbol('z')), Integer(-72361)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(72361)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_531(z:sympy.Rational):
	#(z > 559680) & (z < 568128)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Integer(559680)), StrictLessThan(Symbol('z'), Integer(568128)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_532(z:sympy.Rational):
	#(270*x + z < -72900) & (-x**2 + 10*z + 72900 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(270), Symbol('x')), Symbol('z')), Integer(-72900)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(72900)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_533(z:sympy.Rational):
	#(z > 563920) & (z < 572400)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Integer(563920)), StrictLessThan(Symbol('z'), Integer(572400)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_534(z:sympy.Rational):
	#(271*x + z < -73441) & (-x**2 + 10*z + 73441 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(271), Symbol('x')), Symbol('z')), Integer(-73441)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(73441)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_535(z:sympy.Rational):
	#(z > 568176) & (z < 576688)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Integer(568176)), StrictLessThan(Symbol('z'), Integer(576688)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_536(z:sympy.Rational):
	#(272*x + z < -73984) & (-x**2 + 10*z + 73984 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(272), Symbol('x')), Symbol('z')), Integer(-73984)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(73984)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_537(z:sympy.Rational):
	#(z > 572448) & (z < 580992)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Integer(572448)), StrictLessThan(Symbol('z'), Integer(580992)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_538(z:sympy.Rational):
	#(273*x + z < -74529) & (-x**2 + 10*z + 74529 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(273), Symbol('x')), Symbol('z')), Integer(-74529)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(74529)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_539(z:sympy.Rational):
	#(z > 576736) & (z < 585312)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Integer(576736)), StrictLessThan(Symbol('z'), Integer(585312)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_540(z:sympy.Rational):
	#(274*x + z < -75076) & (-x**2 + 10*z + 75076 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(274), Symbol('x')), Symbol('z')), Integer(-75076)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(75076)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_541(z:sympy.Rational):
	#(z > 581040) & (z < 589648)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Integer(581040)), StrictLessThan(Symbol('z'), Integer(589648)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_542(z:sympy.Rational):
	#(275*x + z < -75625) & (-x**2 + 10*z + 75625 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(275), Symbol('x')), Symbol('z')), Integer(-75625)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(75625)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_543(z:sympy.Rational):
	#(z > 5848731/10) & (z < 593725)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(5848731, 10)), StrictLessThan(Symbol('z'), Integer(593725)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_544(z:sympy.Rational):
	#(276*x + z < -76176) & (-x**2 + 10*z + 76176 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(276), Symbol('x')), Symbol('z')), Integer(-76176)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(76176)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_545(z:sympy.Rational):
	#(z > 5892073/10) & (z < 598092)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(5892073, 10)), StrictLessThan(Symbol('z'), Integer(598092)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_546(z:sympy.Rational):
	#(277*x + z < -76729) & (-x**2 + 10*z + 76729 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(277), Symbol('x')), Symbol('z')), Integer(-76729)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(76729)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_547(z:sympy.Rational):
	#(z > 1187115/2) & (z < 602475)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(1187115, 2)), StrictLessThan(Symbol('z'), Integer(602475)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_548(z:sympy.Rational):
	#(278*x + z < -77284) & (-x**2 + 10*z + 77284 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(278), Symbol('x')), Symbol('z')), Integer(-77284)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(77284)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_549(z:sympy.Rational):
	#(z > 5979237/10) & (z < 606874)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(5979237, 10)), StrictLessThan(Symbol('z'), Integer(606874)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_550(z:sympy.Rational):
	#(279*x + z < -77841) & (-x**2 + 10*z + 77841 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(279), Symbol('x')), Symbol('z')), Integer(-77841)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(77841)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_551(z:sympy.Rational):
	#(z > 6023059/10) & (z < 611289)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(6023059, 10)), StrictLessThan(Symbol('z'), Integer(611289)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_552(z:sympy.Rational):
	#(280*x + z < -78400) & (-x**2 + 10*z + 78400 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(280), Symbol('x')), Symbol('z')), Integer(-78400)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(78400)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_553(z:sympy.Rational):
	#(z > 6067041/10) & (z < 615720)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(6067041, 10)), StrictLessThan(Symbol('z'), Integer(615720)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_554(z:sympy.Rational):
	#(281*x + z < -78961) & (-x**2 + 10*z + 78961 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(281), Symbol('x')), Symbol('z')), Integer(-78961)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(78961)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_555(z:sympy.Rational):
	#(z > 6111183/10) & (z < 620167)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(6111183, 10)), StrictLessThan(Symbol('z'), Integer(620167)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_556(z:sympy.Rational):
	#(282*x + z < -79524) & (-x**2 + 10*z + 79524 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(282), Symbol('x')), Symbol('z')), Integer(-79524)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(79524)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_557(z:sympy.Rational):
	#(z > 1231097/2) & (z < 624630)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(1231097, 2)), StrictLessThan(Symbol('z'), Integer(624630)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_558(z:sympy.Rational):
	#(283*x + z < -80089) & (-x**2 + 10*z + 80089 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(283), Symbol('x')), Symbol('z')), Integer(-80089)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(80089)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_559(z:sympy.Rational):
	#(z > 3097468/5) & (z < 628826)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(3097468, 5)), StrictLessThan(Symbol('z'), Integer(628826)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_560(z:sympy.Rational):
	#(284*x + z < -80656) & (-x**2 + 10*z + 80656 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(284), Symbol('x')), Symbol('z')), Integer(-80656)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(80656)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_561(z:sympy.Rational):
	#(z > 623954) & (z < 633320)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Integer(623954)), StrictLessThan(Symbol('z'), Integer(633320)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_562(z:sympy.Rational):
	#(285*x + z < -81225) & (-x**2 + 10*z + 81225 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(285), Symbol('x')), Symbol('z')), Integer(-81225)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(81225)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_563(z:sympy.Rational):
	#(z > 3142152/5) & (z < 637830)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(3142152, 5)), StrictLessThan(Symbol('z'), Integer(637830)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_564(z:sympy.Rational):
	#(286*x + z < -81796) & (-x**2 + 10*z + 81796 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(286), Symbol('x')), Symbol('z')), Integer(-81796)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(81796)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_565(z:sympy.Rational):
	#(z > 3164614/5) & (z < 642356)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(3164614, 5)), StrictLessThan(Symbol('z'), Integer(642356)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_566(z:sympy.Rational):
	#(287*x + z < -82369) & (-x**2 + 10*z + 82369 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(287), Symbol('x')), Symbol('z')), Integer(-82369)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(82369)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_567(z:sympy.Rational):
	#(z > 3187156/5) & (z < 646898)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(3187156, 5)), StrictLessThan(Symbol('z'), Integer(646898)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_568(z:sympy.Rational):
	#(288*x + z < -82944) & (-x**2 + 10*z + 82944 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(288), Symbol('x')), Symbol('z')), Integer(-82944)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(82944)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_569(z:sympy.Rational):
	#(z > 3209778/5) & (z < 651456)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(3209778, 5)), StrictLessThan(Symbol('z'), Integer(651456)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_570(z:sympy.Rational):
	#(289*x + z < -83521) & (-x**2 + 10*z + 83521 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(289), Symbol('x')), Symbol('z')), Integer(-83521)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(83521)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_571(z:sympy.Rational):
	#(z > 646496) & (z < 656030)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Integer(646496)), StrictLessThan(Symbol('z'), Integer(656030)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_572(z:sympy.Rational):
	#(290*x + z < -84100) & (-x**2 + 10*z + 84100 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(290), Symbol('x')), Symbol('z')), Integer(-84100)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(84100)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_573(z:sympy.Rational):
	#(z > 6505389/10) & (z < 660330)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(6505389, 10)), StrictLessThan(Symbol('z'), Integer(660330)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_574(z:sympy.Rational):
	#(291*x + z < -84681) & (-x**2 + 10*z + 84681 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(291), Symbol('x')), Symbol('z')), Integer(-84681)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(84681)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_575(z:sympy.Rational):
	#(z > 1310219/2) & (z < 664935)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(1310219, 2)), StrictLessThan(Symbol('z'), Integer(664935)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_576(z:sympy.Rational):
	#(292*x + z < -85264) & (-x**2 + 10*z + 85264 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(292), Symbol('x')), Symbol('z')), Integer(-85264)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(85264)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_577(z:sympy.Rational):
	#(z > 6596961/10) & (z < 669556)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(6596961, 10)), StrictLessThan(Symbol('z'), Integer(669556)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_578(z:sympy.Rational):
	#(293*x + z < -85849) & (-x**2 + 10*z + 85849 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(293), Symbol('x')), Symbol('z')), Integer(-85849)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(85849)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_579(z:sympy.Rational):
	#(z > 6642987/10) & (z < 674193)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(6642987, 10)), StrictLessThan(Symbol('z'), Integer(674193)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_580(z:sympy.Rational):
	#(294*x + z < -86436) & (-x**2 + 10*z + 86436 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(294), Symbol('x')), Symbol('z')), Integer(-86436)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(86436)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_581(z:sympy.Rational):
	#(z > 6689173/10) & (z < 678846)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(6689173, 10)), StrictLessThan(Symbol('z'), Integer(678846)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_582(z:sympy.Rational):
	#(295*x + z < -87025) & (-x**2 + 10*z + 87025 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(295), Symbol('x')), Symbol('z')), Integer(-87025)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(87025)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_583(z:sympy.Rational):
	#(z > 6735519/10) & (z < 683515)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(6735519, 10)), StrictLessThan(Symbol('z'), Integer(683515)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_584(z:sympy.Rational):
	#(296*x + z < -87616) & (-x**2 + 10*z + 87616 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(296), Symbol('x')), Symbol('z')), Integer(-87616)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(87616)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_585(z:sympy.Rational):
	#(z > 1356405/2) & (z < 688200)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(1356405, 2)), StrictLessThan(Symbol('z'), Integer(688200)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_586(z:sympy.Rational):
	#(297*x + z < -88209) & (-x**2 + 10*z + 88209 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(297), Symbol('x')), Symbol('z')), Integer(-88209)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(88209)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_587(z:sympy.Rational):
	#(z > 3411716/5) & (z < 692604)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(3411716, 5)), StrictLessThan(Symbol('z'), Integer(692604)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_588(z:sympy.Rational):
	#(298*x + z < -88804) & (-x**2 + 10*z + 88804 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(298), Symbol('x')), Symbol('z')), Integer(-88804)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(88804)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_589(z:sympy.Rational):
	#(z > 687024) & (z < 697320)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Integer(687024)), StrictLessThan(Symbol('z'), Integer(697320)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_590(z:sympy.Rational):
	#(299*x + z < -89401) & (-x**2 + 10*z + 89401 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(299), Symbol('x')), Symbol('z')), Integer(-89401)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(89401)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_591(z:sympy.Rational):
	#(z > 3458604/5) & (z < 702052)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(3458604, 5)), StrictLessThan(Symbol('z'), Integer(702052)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_592(z:sympy.Rational):
	#(300*x + z < -90000) & (-x**2 + 10*z + 90000 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(300), Symbol('x')), Symbol('z')), Integer(-90000)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(90000)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_593(z:sympy.Rational):
	#(z > 3482168/5) & (z < 706800)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(3482168, 5)), StrictLessThan(Symbol('z'), Integer(706800)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_594(z:sympy.Rational):
	#(301*x + z < -90601) & (-x**2 + 10*z + 90601 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(301), Symbol('x')), Symbol('z')), Integer(-90601)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(90601)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_595(z:sympy.Rational):
	#(z > 3505812/5) & (z < 711564)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(3505812, 5)), StrictLessThan(Symbol('z'), Integer(711564)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_596(z:sympy.Rational):
	#(302*x + z < -91204) & (-x**2 + 10*z + 91204 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(302), Symbol('x')), Symbol('z')), Integer(-91204)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(91204)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_597(z:sympy.Rational):
	#(z > 3529536/5) & (z < 716344)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(3529536, 5)), StrictLessThan(Symbol('z'), Integer(716344)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_598(z:sympy.Rational):
	#(303*x + z < -91809) & (-x**2 + 10*z + 91809 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(303), Symbol('x')), Symbol('z')), Integer(-91809)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(91809)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_599(z:sympy.Rational):
	#(z > 710668) & (z < 721140)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Integer(710668)), StrictLessThan(Symbol('z'), Integer(721140)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_600(z:sympy.Rational):
	#(304*x + z < -92416) & (-x**2 + 10*z + 92416 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(304), Symbol('x')), Symbol('z')), Integer(-92416)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(92416)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_601(z:sympy.Rational):
	#(z > 3577224/5) & (z < 725952)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(3577224, 5)), StrictLessThan(Symbol('z'), Integer(725952)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_602(z:sympy.Rational):
	#(305*x + z < -93025) & (-x**2 + 10*z + 93025 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(305), Symbol('x')), Symbol('z')), Integer(-93025)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(93025)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_603(z:sympy.Rational):
	#(z > 1439395/2) & (z < 730475)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(1439395, 2)), StrictLessThan(Symbol('z'), Integer(730475)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_604(z:sympy.Rational):
	#(306*x + z < -93636) & (-x**2 + 10*z + 93636 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(306), Symbol('x')), Symbol('z')), Integer(-93636)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(93636)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_605(z:sympy.Rational):
	#(z > 1449009/2) & (z < 735318)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(1449009, 2)), StrictLessThan(Symbol('z'), Integer(735318)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_606(z:sympy.Rational):
	#(307*x + z < -94249) & (-x**2 + 10*z + 94249 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(307), Symbol('x')), Symbol('z')), Integer(-94249)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(94249)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_607(z:sympy.Rational):
	#(z > 1458655/2) & (z < 740177)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(1458655, 2)), StrictLessThan(Symbol('z'), Integer(740177)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_608(z:sympy.Rational):
	#(308*x + z < -94864) & (-x**2 + 10*z + 94864 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(308), Symbol('x')), Symbol('z')), Integer(-94864)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(94864)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_609(z:sympy.Rational):
	#(z > 1468333/2) & (z < 745052)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(1468333, 2)), StrictLessThan(Symbol('z'), Integer(745052)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_610(z:sympy.Rational):
	#(309*x + z < -95481) & (-x**2 + 10*z + 95481 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(309), Symbol('x')), Symbol('z')), Integer(-95481)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(95481)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_611(z:sympy.Rational):
	#(z > 1478043/2) & (z < 749943)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(1478043, 2)), StrictLessThan(Symbol('z'), Integer(749943)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_612(z:sympy.Rational):
	#(310*x + z < -96100) & (-x**2 + 10*z + 96100 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(310), Symbol('x')), Symbol('z')), Integer(-96100)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(96100)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_613(z:sympy.Rational):
	#(z > 1487785/2) & (z < 754850)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(1487785, 2)), StrictLessThan(Symbol('z'), Integer(754850)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_614(z:sympy.Rational):
	#(311*x + z < -96721) & (-x**2 + 10*z + 96721 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(311), Symbol('x')), Symbol('z')), Integer(-96721)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(96721)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_615(z:sympy.Rational):
	#(z > 1497559/2) & (z < 759773)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(1497559, 2)), StrictLessThan(Symbol('z'), Integer(759773)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_616(z:sympy.Rational):
	#(312*x + z < -97344) & (-x**2 + 10*z + 97344 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(312), Symbol('x')), Symbol('z')), Integer(-97344)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(97344)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_617(z:sympy.Rational):
	#(z > 753130) & (z < 764400)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Integer(753130)), StrictLessThan(Symbol('z'), Integer(764400)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_618(z:sympy.Rational):
	#(313*x + z < -97969) & (-x**2 + 10*z + 97969 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(313), Symbol('x')), Symbol('z')), Integer(-97969)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(97969)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_619(z:sympy.Rational):
	#(z > 3790236/5) & (z < 769354)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(3790236, 5)), StrictLessThan(Symbol('z'), Integer(769354)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_620(z:sympy.Rational):
	#(314*x + z < -98596) & (-x**2 + 10*z + 98596 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(314), Symbol('x')), Symbol('z')), Integer(-98596)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(98596)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_621(z:sympy.Rational):
	#(z > 3814902/5) & (z < 774324)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(3814902, 5)), StrictLessThan(Symbol('z'), Integer(774324)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_622(z:sympy.Rational):
	#(315*x + z < -99225) & (-x**2 + 10*z + 99225 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(315), Symbol('x')), Symbol('z')), Integer(-99225)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(99225)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_623(z:sympy.Rational):
	#(z > 3839648/5) & (z < 779310)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(3839648, 5)), StrictLessThan(Symbol('z'), Integer(779310)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_624(z:sympy.Rational):
	#(316*x + z < -99856) & (-x**2 + 10*z + 99856 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(316), Symbol('x')), Symbol('z')), Integer(-99856)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(99856)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_625(z:sympy.Rational):
	#(z > 3864474/5) & (z < 784312)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(3864474, 5)), StrictLessThan(Symbol('z'), Integer(784312)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_626(z:sympy.Rational):
	#(317*x + z < -100489) & (-x**2 + 10*z + 100489 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(317), Symbol('x')), Symbol('z')), Integer(-100489)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(100489)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_627(z:sympy.Rational):
	#(z > 777876) & (z < 789330)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Integer(777876)), StrictLessThan(Symbol('z'), Integer(789330)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_628(z:sympy.Rational):
	#(318*x + z < -101124) & (-x**2 + 10*z + 101124 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(318), Symbol('x')), Symbol('z')), Integer(-101124)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(101124)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_629(z:sympy.Rational):
	#(z > 3914366/5) & (z < 794364)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(3914366, 5)), StrictLessThan(Symbol('z'), Integer(794364)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_630(z:sympy.Rational):
	#(319*x + z < -101761) & (-x**2 + 10*z + 101761 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(319), Symbol('x')), Symbol('z')), Integer(-101761)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(101761)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_631(z:sympy.Rational):
	#(z > 3939432/5) & (z < 799414)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(3939432, 5)), StrictLessThan(Symbol('z'), Integer(799414)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_632(z:sympy.Rational):
	#(320*x + z < -102400) & (-x**2 + 10*z + 102400 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(320), Symbol('x')), Symbol('z')), Integer(-102400)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(102400)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_633(z:sympy.Rational):
	#(z > 7923489/10) & (z < 804160)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(7923489, 10)), StrictLessThan(Symbol('z'), Integer(804160)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_634(z:sympy.Rational):
	#(321*x + z < -103041) & (-x**2 + 10*z + 103041 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(321), Symbol('x')), Symbol('z')), Integer(-103041)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(103041)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_635(z:sympy.Rational):
	#(z > 7973923/10) & (z < 809241)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(7973923, 10)), StrictLessThan(Symbol('z'), Integer(809241)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_636(z:sympy.Rational):
	#(322*x + z < -103684) & (-x**2 + 10*z + 103684 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(322), Symbol('x')), Symbol('z')), Integer(-103684)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(103684)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_637(z:sympy.Rational):
	#(z > 8024517/10) & (z < 814338)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(8024517, 10)), StrictLessThan(Symbol('z'), Integer(814338)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_638(z:sympy.Rational):
	#(323*x + z < -104329) & (-x**2 + 10*z + 104329 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(323), Symbol('x')), Symbol('z')), Integer(-104329)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(104329)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_639(z:sympy.Rational):
	#(z > 8075271/10) & (z < 819451)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(8075271, 10)), StrictLessThan(Symbol('z'), Integer(819451)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_640(z:sympy.Rational):
	#(324*x + z < -104976) & (-x**2 + 10*z + 104976 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(324), Symbol('x')), Symbol('z')), Integer(-104976)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(104976)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_641(z:sympy.Rational):
	#(z > 1625237/2) & (z < 824580)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(1625237, 2)), StrictLessThan(Symbol('z'), Integer(824580)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_642(z:sympy.Rational):
	#(325*x + z < -105625) & (-x**2 + 10*z + 105625 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(325), Symbol('x')), Symbol('z')), Integer(-105625)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(105625)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_643(z:sympy.Rational):
	#(z > 8177259/10) & (z < 829725)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(8177259, 10)), StrictLessThan(Symbol('z'), Integer(829725)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_644(z:sympy.Rational):
	#(326*x + z < -106276) & (-x**2 + 10*z + 106276 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(326), Symbol('x')), Symbol('z')), Integer(-106276)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(106276)), Integer(0)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_645(z:sympy.Rational):
	#(z > 8228493/10) & (z < 834886)

	pre_cond = And(StrictGreaterThan(Symbol('z'), Rational(8228493, 10)), StrictLessThan(Symbol('z'), Integer(834886)))

	eval = pre_cond.subs( { 'z':z })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_646(z:sympy.Rational):
	#(327*x + z < -106929) & (-x**2 + 10*z + 106929 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(327), Symbol('x')), Symbol('z')), Integer(-106929)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(10), Symbol('z')), Integer(106929)), Integer(0)))