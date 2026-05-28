import sympy
from sympy import *

def pre_condition_0(r1:sympy.Rational,r2:sympy.Rational):
	#(r2 < -2*y) & (r1 + y**2 - 1 > 0)

	pre_cond = And(StrictLessThan(Symbol('r2'), Mul(Integer(-1), Integer(2), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Integer(-1)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 1) & (r2 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Integer(1)), StrictLessThan(Symbol('r2'), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_2(r1:sympy.Rational,r2:sympy.Rational):
	#(4*r2 < -11*y) & (r1 + y**2 - 7/4 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(4), Symbol('r2')), Mul(Integer(-1), Integer(11), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-7, 4)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_3(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > 3/4) & (r2 < 11/4)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(3, 4)), StrictLessThan(Symbol('r2'), Rational(11, 4)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_4(r1:sympy.Rational,r2:sympy.Rational):
	#(r2 < -3*y) & (r1 + y**2 - 2 > 0)

	pre_cond = And(StrictLessThan(Symbol('r2'), Mul(Integer(-1), Integer(3), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Integer(-2)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_5(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -2) & (r2 < 6)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Integer(-2)), StrictLessThan(Symbol('r2'), Integer(6)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_6(r1:sympy.Rational,r2:sympy.Rational):
	#(32*r2 < -91*y) & (r1 + y**2 - 59/32 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(32), Symbol('r2')), Mul(Integer(-1), Integer(91), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-59, 32)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_7(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -69/32) & (r2 < 91/16)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-69, 32)), StrictLessThan(Symbol('r2'), Rational(91, 16)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_8(r1:sympy.Rational,r2:sympy.Rational):
	#(64*r2 < -187*y) & (r1 + y**2 - 123/64 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(64), Symbol('r2')), Mul(Integer(-1), Integer(187), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-123, 64)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_9(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -453/64) & (r2 < 561/64)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-453, 64)), StrictLessThan(Symbol('r2'), Rational(561, 64)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_10(r1:sympy.Rational,r2:sympy.Rational):
	#(64*r2 < -189*y) & (r1 + y**2 - 125/64 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(64), Symbol('r2')), Mul(Integer(-1), Integer(189), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-125, 64)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_11(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -899/64) & (r2 < 189/16)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-899, 64)), StrictLessThan(Symbol('r2'), Rational(189, 16)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_12(r1:sympy.Rational,r2:sympy.Rational):
	#(2*r2 < -3*y) & (r1 + y**2 - 1/2 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(2), Symbol('r2')), Mul(Integer(-1), Integer(3), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-1, 2)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_13(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -31/2) & (r2 < -6)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-31, 2)), StrictLessThan(Symbol('r2'), Integer(-6)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_14(r1:sympy.Rational,r2:sympy.Rational):
	#(8*r2 < -9*y) & (r1 + y**2 - 1/8 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(8), Symbol('r2')), Mul(Integer(-1), Integer(9), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-1, 8)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_15(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -127/8) & (r2 < -9/2)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-127, 8)), StrictLessThan(Symbol('r2'), Rational(-9, 2)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_16(r1:sympy.Rational,r2:sympy.Rational):
	#(32*r2 < -33*y) & (r1 + y**2 - 1/32 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(32), Symbol('r2')), Mul(Integer(-1), Integer(33), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-1, 32)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_17(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -511/32) & (r2 < -33/8)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-511, 32)), StrictLessThan(Symbol('r2'), Rational(-33, 8)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_18(r1:sympy.Rational,r2:sympy.Rational):
	#(128*r2 < -129*y) & (r1 + y**2 - 1/128 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(128), Symbol('r2')), Mul(Integer(-1), Integer(129), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-1, 128)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_19(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -2047/128) & (r2 < -129/32)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-2047, 128)), StrictLessThan(Symbol('r2'), Rational(-129, 32)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_20(r1:sympy.Rational,r2:sympy.Rational):
	#(512*r2 < -513*y) & (r1 + y**2 - 1/512 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(512), Symbol('r2')), Mul(Integer(-1), Integer(513), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-1, 512)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_21(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -8191/512) & (r2 < -513/128)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-8191, 512)), StrictLessThan(Symbol('r2'), Rational(-513, 128)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_22(r1:sympy.Rational,r2:sympy.Rational):
	#(2048*r2 < -2049*y) & (r1 + y**2 - 1/2048 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(2048), Symbol('r2')), Mul(Integer(-1), Integer(2049), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-1, 2048)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_23(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -32767/2048) & (r2 < -2049/512)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-32767, 2048)), StrictLessThan(Symbol('r2'), Rational(-2049, 512)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_24(r1:sympy.Rational,r2:sympy.Rational):
	#(8192*r2 < -8193*y) & (r1 + y**2 - 1/8192 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(8192), Symbol('r2')), Mul(Integer(-1), Integer(8193), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-1, 8192)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_25(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -131071/8192) & (r2 < -8193/2048)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-131071, 8192)), StrictLessThan(Symbol('r2'), Rational(-8193, 2048)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_26(r1:sympy.Rational,r2:sympy.Rational):
	#(32768*r2 < -32769*y) & (r1 + y**2 - 1/32768 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(32768), Symbol('r2')), Mul(Integer(-1), Integer(32769), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-1, 32768)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_27(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -524287/32768) & (r2 < -32769/8192)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-524287, 32768)), StrictLessThan(Symbol('r2'), Rational(-32769, 8192)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_28(r1:sympy.Rational,r2:sympy.Rational):
	#(131072*r2 < -131073*y) & (r1 + y**2 - 1/131072 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(131072), Symbol('r2')), Mul(Integer(-1), Integer(131073), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-1, 131072)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_29(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -2097151/131072) & (r2 < -131073/32768)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-2097151, 131072)), StrictLessThan(Symbol('r2'), Rational(-131073, 32768)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_30(r1:sympy.Rational,r2:sympy.Rational):
	#(524288*r2 < -524289*y) & (r1 + y**2 - 1/524288 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(524288), Symbol('r2')), Mul(Integer(-1), Integer(524289), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-1, 524288)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_31(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -8388607/524288) & (r2 < -524289/131072)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-8388607, 524288)), StrictLessThan(Symbol('r2'), Rational(-524289, 131072)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_32(r1:sympy.Rational,r2:sympy.Rational):
	#(2097152*r2 < -2097153*y) & (r1 + y**2 - 1/2097152 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(2097152), Symbol('r2')), Mul(Integer(-1), Integer(2097153), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-1, 2097152)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_33(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -33554431/2097152) & (r2 < -2097153/524288)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-33554431, 2097152)), StrictLessThan(Symbol('r2'), Rational(-2097153, 524288)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_34(r1:sympy.Rational,r2:sympy.Rational):
	#(8388608*r2 < -8388609*y) & (r1 + y**2 - 1/8388608 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(8388608), Symbol('r2')), Mul(Integer(-1), Integer(8388609), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-1, 8388608)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_35(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -134217727/8388608) & (r2 < -8388609/2097152)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-134217727, 8388608)), StrictLessThan(Symbol('r2'), Rational(-8388609, 2097152)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_36(r1:sympy.Rational,r2:sympy.Rational):
	#(33554432*r2 < -33554433*y) & (r1 + y**2 - 1/33554432 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(33554432), Symbol('r2')), Mul(Integer(-1), Integer(33554433), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-1, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_37(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -536870911/33554432) & (r2 < -33554433/8388608)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-536870911, 33554432)), StrictLessThan(Symbol('r2'), Rational(-33554433, 8388608)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_38(r1:sympy.Rational,r2:sympy.Rational):
	#(134217728*r2 < -134217729*y) & (r1 + y**2 - 1/134217728 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(134217728), Symbol('r2')), Mul(Integer(-1), Integer(134217729), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-1, 134217728)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_39(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -2147483647/134217728) & (r2 < -134217729/33554432)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-2147483647, 134217728)), StrictLessThan(Symbol('r2'), Rational(-134217729, 33554432)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_40(r1:sympy.Rational,r2:sympy.Rational):
	#(536870912*r2 < -536870913*y) & (r1 + y**2 - 1/536870912 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(536870912), Symbol('r2')), Mul(Integer(-1), Integer(536870913), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-1, 536870912)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_41(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -8589934591/536870912) & (r2 < -536870913/134217728)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-8589934591, 536870912)), StrictLessThan(Symbol('r2'), Rational(-536870913, 134217728)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_42(r1:sympy.Rational,r2:sympy.Rational):
	#(2147483648*r2 < -2147483649*y) & (r1 + y**2 - 1/2147483648 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(2147483648), Symbol('r2')), Mul(Integer(-1), Integer(2147483649), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-1, 2147483648)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_43(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -34359738367/2147483648) & (r2 < -2147483649/536870912)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-34359738367, 2147483648)), StrictLessThan(Symbol('r2'), Rational(-2147483649, 536870912)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_44(r1:sympy.Rational,r2:sympy.Rational):
	#(8589934592*r2 < -8589934593*y) & (r1 + y**2 - 1/8589934592 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(8589934592), Symbol('r2')), Mul(Integer(-1), Integer(8589934593), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-1, 8589934592)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_45(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -137438953471/8589934592) & (r2 < -8589934593/2147483648)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-137438953471, 8589934592)), StrictLessThan(Symbol('r2'), Rational(-8589934593, 2147483648)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_46(r1:sympy.Rational,r2:sympy.Rational):
	#(17179869184*r2 < -17179869185*y) & (r1 + y**2 - 1/17179869184 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(17179869184), Symbol('r2')), Mul(Integer(-1), Integer(17179869185), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-1, 17179869184)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_47(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -18889465935807905175847123403810752178230856860321879/1180591620992289210384000000000000000000000000000000) & (r2 < -13743895349599999012911257/3435973837200000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-18889465935807905175847123403810752178230856860321879, 1180591620992289210384000000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-13743895349599999012911257, 3435973837200000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_48(r1:sympy.Rational,r2:sympy.Rational):
	#(34359738368*r2 < -34359738369*y) & (r1 + y**2 - 1/34359738368 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(34359738368), Symbol('r2')), Mul(Integer(-1), Integer(34359738369), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-1, 34359738368)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_49(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -549755813887/34359738368) & (r2 < -34359738369/8589934592)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-549755813887, 34359738368)), StrictLessThan(Symbol('r2'), Rational(-34359738369, 8589934592)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_50(r1:sympy.Rational,r2:sympy.Rational):
	#(250000000000000000000000000*r2 < -250000000003637978807091713*y) & (r1 + y**2 - 3637978807091713/250000000000000000000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(250000000000000000000000000), Symbol('r2')), Mul(Integer(-1), Integer(250000000003637978807091713), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-3637978807091713, 250000000000000000000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_51(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -295147905196264212084914677631998495175057957936089/18446744078004518912250000000000000000000000000000) & (r2 < -4294967296187499654399123235204836917250939078858721/1073741824125000000000000000000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-295147905196264212084914677631998495175057957936089, 18446744078004518912250000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-4294967296187499654399123235204836917250939078858721, 1073741824125000000000000000000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_52(r1:sympy.Rational,r2:sympy.Rational):
	#(17179869184499998617589217000000000000*r2 < -17179869184718748301480487470777672191*y) & (r1 + y**2 - 218749683891270470777672191/17179869184499998617589217000000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(17179869184499998617589217000000000000), Symbol('r2')), Mul(Integer(-1), Integer(17179869184718748301480487470777672191), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-218749683891270470777672191, 17179869184499998617589217000000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_53(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -5070602401351603020285900137467287471749991400512918683977403584751526481313/316912650140067673211333309885284932978169208250000000000000000000000000000) & (r2 < -1999999999850842671192908287/500000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-5070602401351603020285900137467287471749991400512918683977403584751526481313, 316912650140067673211333309885284932978169208250000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1999999999850842671192908287, 500000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_54(r1:sympy.Rational,r2:sympy.Rational):
	#(17179869184499998617589217000000000000*r2 < -17179869184718748301480487470777672191*y) & (r1 + y**2 - 218749683891270470777672191/17179869184499998617589217000000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(17179869184499998617589217000000000000), Symbol('r2')), Mul(Integer(-1), Integer(17179869184718748301480487470777672191), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-218749683891270470777672191, 17179869184499998617589217000000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_55(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -5070602401333156168748174479359636251571774261969758845630752089437488671513/316912650140067673211333309885284932978169208250000000000000000000000000000) & (r2 < -34359738366374993474269138334641895644481421749710421/8589934592249999308794608500000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-5070602401333156168748174479359636251571774261969758845630752089437488671513, 316912650140067673211333309885284932978169208250000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-34359738366374993474269138334641895644481421749710421, 8589934592249999308794608500000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_56(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_57(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_58(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_59(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_60(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_61(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_62(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_63(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_64(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_65(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_66(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_67(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_68(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_69(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_70(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_71(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_72(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_73(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_74(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_75(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_76(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_77(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_78(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_79(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_80(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_81(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_82(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_83(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_84(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_85(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_86(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_87(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_88(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_89(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_90(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_91(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_92(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_93(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_94(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_95(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_96(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_97(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_98(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_99(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_100(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_101(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_102(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_103(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_104(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_105(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_106(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_107(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_108(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_109(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_110(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_111(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_112(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_113(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_114(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_115(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_116(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_117(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_118(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_119(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_120(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_121(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_122(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_123(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_124(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_125(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_126(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_127(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_128(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_129(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_130(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_131(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_132(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_133(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_134(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_135(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_136(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_137(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_138(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_139(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_140(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_141(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_142(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_143(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_144(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_145(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_146(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_147(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_148(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_149(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_150(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_151(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_152(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_153(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_154(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_155(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_156(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_157(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_158(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_159(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_160(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_161(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_162(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_163(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_164(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_165(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_166(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_167(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_168(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_169(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_170(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_171(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_172(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_173(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_174(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_175(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_176(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_177(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_178(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_179(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_180(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_181(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_182(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_183(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_184(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_185(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_186(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_187(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_188(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_189(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_190(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_191(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_192(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_193(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_194(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_195(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_196(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_197(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_198(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_199(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_200(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_201(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_202(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_203(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_204(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_205(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_206(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_207(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_208(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_209(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_210(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_211(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_212(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_213(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_214(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_215(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_216(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_217(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_218(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_219(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_220(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_221(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_222(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_223(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_224(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_225(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_226(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_227(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_228(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_229(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_230(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_231(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_232(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_233(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_234(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_235(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_236(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_237(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_238(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_239(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_240(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_241(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_242(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_243(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_244(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_245(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_246(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_247(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_248(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_249(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_250(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_251(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_252(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_253(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_254(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_255(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_256(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_257(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_258(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_259(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_260(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_261(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_262(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_263(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_264(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_265(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_266(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_267(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_268(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_269(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_270(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_271(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_272(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_273(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_274(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_275(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_276(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_277(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_278(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_279(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_280(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_281(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_282(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_283(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_284(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_285(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_286(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_287(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_288(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_289(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_290(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_291(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_292(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_293(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_294(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_295(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_296(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_297(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_298(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_299(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_300(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_301(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_302(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_303(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_304(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_305(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_306(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_307(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_308(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_309(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_310(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_311(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_312(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_313(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_314(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_315(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_316(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_317(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_318(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_319(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_320(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_321(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_322(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_323(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_324(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_325(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_326(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_327(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_328(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_329(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_330(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_331(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_332(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_333(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_334(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_335(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_336(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_337(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_338(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_339(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_340(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_341(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_342(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_343(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_344(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_345(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_346(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_347(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_348(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_349(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_350(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_351(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_352(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_353(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_354(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_355(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_356(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_357(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_358(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_359(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_360(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_361(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_362(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_363(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_364(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_365(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_366(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_367(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_368(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_369(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_370(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_371(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_372(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_373(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_374(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_375(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_376(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_377(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_378(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_379(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_380(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_381(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_382(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_383(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_384(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_385(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_386(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_387(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_388(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_389(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_390(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_391(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_392(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_393(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_394(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_395(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_396(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_397(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_398(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_399(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_400(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_401(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_402(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_403(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_404(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_405(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_406(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_407(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_408(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_409(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_410(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_411(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_412(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_413(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_414(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_415(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_416(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_417(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_418(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_419(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_420(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_421(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_422(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_423(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_424(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_425(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_426(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_427(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_428(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_429(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_430(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_431(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_432(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_433(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_434(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_435(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_436(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_437(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_438(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_439(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_440(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_441(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_442(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_443(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_444(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_445(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_446(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_447(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_448(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_449(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_450(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_451(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_452(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_453(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_454(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_455(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_456(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_457(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_458(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_459(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_460(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_461(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_462(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_463(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_464(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_465(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_466(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_467(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_468(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_469(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_470(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_471(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_472(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_473(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_474(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_475(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_476(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_477(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_478(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_479(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_480(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_481(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_482(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_483(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_484(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_485(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_486(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_487(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_488(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_489(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_490(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_491(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_492(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_493(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_494(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_495(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_496(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_497(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_498(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_499(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_500(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_501(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_502(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_503(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_504(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_505(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_506(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_507(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_508(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_509(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_510(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_511(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_512(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_513(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_514(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_515(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_516(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_517(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_518(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_519(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_520(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_521(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_522(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_523(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_524(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_525(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_526(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_527(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_528(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_529(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_530(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_531(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_532(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_533(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_534(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_535(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_536(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_537(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_538(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_539(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_540(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_541(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_542(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_543(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_544(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_545(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_546(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_547(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_548(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_549(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_550(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_551(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_552(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_553(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_554(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_555(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_556(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_557(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_558(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_559(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_560(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_561(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_562(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_563(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_564(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_565(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_566(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_567(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_568(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_569(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_570(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_571(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_572(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_573(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_574(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_575(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_576(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_577(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_578(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_579(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_580(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_581(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_582(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_583(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_584(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_585(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_586(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_587(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_588(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_589(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_590(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_591(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_592(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_593(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_594(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_595(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_596(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_597(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_598(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_599(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_600(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_601(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_602(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_603(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_604(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_605(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_606(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_607(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_608(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_609(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_610(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_611(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_612(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_613(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_614(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_615(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_616(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_617(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_618(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_619(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_620(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_621(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_622(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_623(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_624(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_625(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_626(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_627(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_628(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_629(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_630(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_631(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_632(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_633(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_634(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_635(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_636(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_637(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_638(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_639(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_640(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_641(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_642(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_643(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_644(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_645(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_646(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_647(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_648(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_649(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_650(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_651(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_652(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_653(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_654(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_655(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_656(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_657(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_658(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_659(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_660(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_661(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('r1'), Rational(-87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979, 5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000)), StrictLessThan(Symbol('r2'), Rational(-1717986918318749655508927106705009102952214960570811, 429496729612499965439730425000000000000000000000000)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_662(r1:sympy.Rational,r2:sympy.Rational):
	#(14757395259799788675068890471671072484764265712080550000000000*r2 < -14757395259987693066362965974200759939829129715779340434964923*y) & (r1 + y**2 - 187904391294075502529687455064864003698790434964923/14757395259799788675068890471671072484764265712080550000000000 > 0)

	pre_cond = And(StrictLessThan(Mul(Integer(14757395259799788675068890471671072484764265712080550000000000), Symbol('r2')), Mul(Integer(-1), Integer(14757395259987693066362965974200759939829129715779340434964923), Symbol('y'))), StrictGreaterThan(Add(Symbol('r1'), Pow(Symbol('y'), Integer(2)), Rational(-187904391294075502529687455064864003698790434964923, 14757395259799788675068890471671072484764265712080550000000000)), Integer(0)))

	eval = pre_cond.subs( { 'r1':r1, 'r2':r2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_663(r1:sympy.Rational,r2:sympy.Rational):
	#(r1 > -87112285941356727181498415369688793387228407350755753452600768665739325927355046345045727528597452979/5444517872309674211633922454958403264019606128755247559003429515407634750000000000000000000000000000) & (r2 < -1717986918318749655508927106705009102952214960570811/429496729612499965439730425000000000000000000000000)