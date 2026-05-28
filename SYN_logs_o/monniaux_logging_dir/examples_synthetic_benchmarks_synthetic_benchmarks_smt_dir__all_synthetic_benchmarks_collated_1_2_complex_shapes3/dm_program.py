import sympy
from sympy import *

def pre_condition_0(a:sympy.Rational,r:sympy.Rational):
	#(r > 0) & (a*y**3 + 1 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Integer(0)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1(a:sympy.Rational,r:sympy.Rational):
	#(r > 0) & (a < -512)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Integer(0)), StrictLessThan(Symbol('a'), Integer(-512)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_2(a:sympy.Rational,r:sympy.Rational):
	#(r > 1/9) & (a*y**3 - 1 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(1, 9)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Integer(-1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_3(a:sympy.Rational,r:sympy.Rational):
	#r > 1/9

	pre_cond = StrictGreaterThan(Symbol('r'), Rational(1, 9))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_4(a:sympy.Rational,r:sympy.Rational):
	#(r > 1/16) & (a*y**3 - 1/2 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(1, 16)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-1, 2)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_5(a:sympy.Rational,r:sympy.Rational):
	#(r > 1/16) & (a < 256)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(1, 16)), StrictLessThan(Symbol('a'), Integer(256)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_6(a:sympy.Rational,r:sympy.Rational):
	#(r > 25/256) & (a*y**3 - 7/8 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(25, 256)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-7, 8)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_7(a:sympy.Rational,r:sympy.Rational):
	#(r > 25/256) & (a < 448)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(25, 256)), StrictLessThan(Symbol('a'), Integer(448)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_8(a:sympy.Rational,r:sympy.Rational):
	#(r > 81/1024) & (a*y**3 - 11/16 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(81, 1024)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-11, 16)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_9(a:sympy.Rational,r:sympy.Rational):
	#(r > 81/1024) & (a < 352)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(81, 1024)), StrictLessThan(Symbol('a'), Integer(352)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_10(a:sympy.Rational,r:sympy.Rational):
	#(r > 289/4096) & (a*y**3 - 19/32 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(289, 4096)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-19, 32)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_11(a:sympy.Rational,r:sympy.Rational):
	#(r > 289/4096) & (a < 304)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(289, 4096)), StrictLessThan(Symbol('a'), Integer(304)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_12(a:sympy.Rational,r:sympy.Rational):
	#(r > 1089/16384) & (a*y**3 - 35/64 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(1089, 16384)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-35, 64)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_13(a:sympy.Rational,r:sympy.Rational):
	#(r > 1089/16384) & (a < 280)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(1089, 16384)), StrictLessThan(Symbol('a'), Integer(280)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_14(a:sympy.Rational,r:sympy.Rational):
	#(r > 4225/65536) & (a*y**3 - 67/128 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(4225, 65536)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-67, 128)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_15(a:sympy.Rational,r:sympy.Rational):
	#(r > 4225/65536) & (a < 268)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(4225, 65536)), StrictLessThan(Symbol('a'), Integer(268)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_16(a:sympy.Rational,r:sympy.Rational):
	#(r > 17161/262144) & (a*y**3 - 137/256 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(17161, 262144)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-137, 256)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_17(a:sympy.Rational,r:sympy.Rational):
	#(r > 17161/262144) & (a < 274)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(17161, 262144)), StrictLessThan(Symbol('a'), Integer(274)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_18(a:sympy.Rational,r:sympy.Rational):
	#(r > 69169/1048576) & (a*y**3 - 277/512 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(69169, 1048576)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-277, 512)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_19(a:sympy.Rational,r:sympy.Rational):
	#(r > 69169/1048576) & (a < 277)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(69169, 1048576)), StrictLessThan(Symbol('a'), Integer(277)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_20(a:sympy.Rational,r:sympy.Rational):
	#(r > 277729/4194304) & (a*y**3 - 557/1024 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(277729, 4194304)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-557, 1024)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_21(a:sympy.Rational,r:sympy.Rational):
	#(r > 277729/4194304) & (a < 557/2)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(277729, 4194304)), StrictLessThan(Symbol('a'), Rational(557, 2)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_22(a:sympy.Rational,r:sympy.Rational):
	#(r > 1113025/16777216) & (a*y**3 - 1117/2048 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(1113025, 16777216)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-1117, 2048)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_23(a:sympy.Rational,r:sympy.Rational):
	#(r > 1113025/16777216) & (a < 1117/4)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(1113025, 16777216)), StrictLessThan(Symbol('a'), Rational(1117, 4)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_24(a:sympy.Rational,r:sympy.Rational):
	#(r > 4456321/67108864) & (a*y**3 - 2237/4096 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(4456321, 67108864)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-2237, 4096)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_25(a:sympy.Rational,r:sympy.Rational):
	#(r > 4456321/67108864) & (a < 2237/8)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(4456321, 67108864)), StrictLessThan(Symbol('a'), Rational(2237, 8)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_26(a:sympy.Rational,r:sympy.Rational):
	#(r > 17833729/268435456) & (a*y**3 - 4477/8192 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(17833729, 268435456)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-4477, 8192)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_27(a:sympy.Rational,r:sympy.Rational):
	#(r > 17833729/268435456) & (a < 4477/16)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(17833729, 268435456)), StrictLessThan(Symbol('a'), Rational(4477, 16)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_28(a:sympy.Rational,r:sympy.Rational):
	#(r > 71351809/1073741824) & (a*y**3 - 8957/16384 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(71351809, 1073741824)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-8957, 16384)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_29(a:sympy.Rational,r:sympy.Rational):
	#(r > 71351809/1073741824) & (a < 8957/32)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(71351809, 1073741824)), StrictLessThan(Symbol('a'), Rational(8957, 32)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_30(a:sympy.Rational,r:sympy.Rational):
	#(r > 285441025/4294967296) & (a*y**3 - 17917/32768 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(285441025, 4294967296)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-17917, 32768)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_31(a:sympy.Rational,r:sympy.Rational):
	#(r > 285441025/4294967296) & (a < 17917/64)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(285441025, 4294967296)), StrictLessThan(Symbol('a'), Rational(17917, 64)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_32(a:sympy.Rational,r:sympy.Rational):
	#(r > 1141831681/17179869184) & (a*y**3 - 35837/65536 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(1141831681, 17179869184)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-35837, 65536)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_33(a:sympy.Rational,r:sympy.Rational):
	#(r > 1141831681/17179869184) & (a < 35837/128)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(1141831681, 17179869184)), StrictLessThan(Symbol('a'), Rational(35837, 128)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_34(a:sympy.Rational,r:sympy.Rational):
	#(r > 4567461889/68719476736) & (a*y**3 - 71677/131072 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(4567461889, 68719476736)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-71677, 131072)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_35(a:sympy.Rational,r:sympy.Rational):
	#(r > 4567461889/68719476736) & (a < 71677/256)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(4567461889, 68719476736)), StrictLessThan(Symbol('a'), Rational(71677, 256)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_36(a:sympy.Rational,r:sympy.Rational):
	#(r > 18270117889/274877906944) & (a*y**3 - 143357/262144 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(18270117889, 274877906944)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-143357, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_37(a:sympy.Rational,r:sympy.Rational):
	#(r > 18270117889/274877906944) & (a < 143357/512)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(18270117889, 274877906944)), StrictLessThan(Symbol('a'), Rational(143357, 512)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_38(a:sympy.Rational,r:sympy.Rational):
	#(r > 73081012225/1099511627776) & (a*y**3 - 286717/524288 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(73081012225, 1099511627776)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-286717, 524288)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_39(a:sympy.Rational,r:sympy.Rational):
	#(r > 73081012225/1099511627776) & (a < 286717/1024)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(73081012225, 1099511627776)), StrictLessThan(Symbol('a'), Rational(286717, 1024)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_40(a:sympy.Rational,r:sympy.Rational):
	#(r > 292325130241/4398046511104) & (a*y**3 - 573437/1048576 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(292325130241, 4398046511104)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-573437, 1048576)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_41(a:sympy.Rational,r:sympy.Rational):
	#(r > 292325130241/4398046511104) & (a < 573437/2048)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(292325130241, 4398046511104)), StrictLessThan(Symbol('a'), Rational(573437, 2048)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_42(a:sympy.Rational,r:sympy.Rational):
	#(r > 1169302683649/17592186044416) & (a*y**3 - 1146877/2097152 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(1169302683649, 17592186044416)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-1146877, 2097152)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_43(a:sympy.Rational,r:sympy.Rational):
	#(r > 1169302683649/17592186044416) & (a < 1146877/4096)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(1169302683649, 17592186044416)), StrictLessThan(Symbol('a'), Rational(1146877, 4096)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_44(a:sympy.Rational,r:sympy.Rational):
	#(r > 4677215059969/70368744177664) & (a*y**3 - 2293757/4194304 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(4677215059969, 70368744177664)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-2293757, 4194304)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_45(a:sympy.Rational,r:sympy.Rational):
	#(r > 4677215059969/70368744177664) & (a < 2293757/8192)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(4677215059969, 70368744177664)), StrictLessThan(Symbol('a'), Rational(2293757, 8192)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_46(a:sympy.Rational,r:sympy.Rational):
	#(r > 18708868890625/281474976710656) & (a*y**3 - 4587517/8388608 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(18708868890625, 281474976710656)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-4587517, 8388608)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_47(a:sympy.Rational,r:sympy.Rational):
	#(r > 18708868890625/281474976710656) & (a < 4587517/16384)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(18708868890625, 281474976710656)), StrictLessThan(Symbol('a'), Rational(4587517, 16384)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_48(a:sympy.Rational,r:sympy.Rational):
	#(r > 74835492864001/1125899906842624) & (a*y**3 - 9175037/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(74835492864001, 1125899906842624)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-9175037, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_49(a:sympy.Rational,r:sympy.Rational):
	#(r > 74835492864001/1125899906842624) & (a < 9175037/32768)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(74835492864001, 1125899906842624)), StrictLessThan(Symbol('a'), Rational(9175037, 32768)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_50(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_51(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_52(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_53(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_54(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_55(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_56(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_57(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_58(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_59(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_60(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_61(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_62(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_63(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_64(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_65(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_66(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_67(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_68(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_69(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_70(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_71(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_72(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_73(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_74(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_75(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_76(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_77(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_78(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_79(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_80(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_81(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_82(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_83(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_84(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_85(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_86(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_87(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_88(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_89(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_90(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_91(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_92(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_93(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_94(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_95(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_96(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_97(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_98(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_99(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_100(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_101(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_102(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_103(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_104(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_105(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_106(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_107(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_108(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_109(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_110(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_111(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_112(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_113(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_114(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_115(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_116(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_117(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_118(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_119(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_120(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_121(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_122(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_123(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_124(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_125(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_126(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_127(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_128(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_129(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_130(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_131(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_132(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_133(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_134(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_135(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_136(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_137(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_138(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_139(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_140(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_141(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_142(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_143(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_144(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_145(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_146(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_147(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_148(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_149(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_150(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_151(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_152(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_153(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_154(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_155(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_156(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_157(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_158(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_159(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_160(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_161(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_162(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_163(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_164(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_165(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_166(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_167(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_168(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_169(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_170(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_171(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_172(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_173(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_174(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_175(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_176(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_177(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_178(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_179(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_180(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_181(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_182(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_183(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_184(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_185(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_186(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_187(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_188(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_189(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_190(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_191(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_192(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_193(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_194(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_195(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_196(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_197(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_198(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_199(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_200(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_201(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_202(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_203(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_204(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_205(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_206(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_207(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_208(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_209(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_210(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_211(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_212(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_213(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_214(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_215(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_216(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_217(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_218(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_219(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_220(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_221(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_222(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_223(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_224(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_225(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_226(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_227(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_228(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_229(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_230(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_231(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_232(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_233(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_234(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_235(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_236(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_237(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_238(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_239(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_240(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_241(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_242(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_243(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_244(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_245(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_246(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_247(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_248(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_249(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_250(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_251(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_252(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_253(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_254(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_255(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_256(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_257(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_258(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_259(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_260(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_261(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_262(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_263(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_264(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_265(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_266(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_267(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_268(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_269(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_270(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_271(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_272(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_273(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_274(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_275(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_276(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_277(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_278(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_279(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_280(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_281(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_282(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_283(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_284(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_285(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_286(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_287(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_288(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_289(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_290(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_291(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_292(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_293(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_294(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_295(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_296(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_297(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_298(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_299(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_300(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_301(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_302(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_303(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_304(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_305(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_306(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_307(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_308(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_309(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_310(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_311(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_312(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_313(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_314(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_315(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_316(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_317(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_318(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_319(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_320(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_321(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_322(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_323(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_324(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_325(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_326(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_327(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_328(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_329(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_330(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_331(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_332(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_333(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_334(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_335(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_336(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_337(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_338(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_339(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_340(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_341(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_342(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_343(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_344(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_345(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_346(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_347(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_348(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_349(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_350(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_351(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_352(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_353(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_354(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_355(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_356(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_357(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_358(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_359(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_360(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_361(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_362(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_363(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_364(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_365(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_366(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_367(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_368(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_369(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_370(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_371(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_372(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_373(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_374(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_375(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_376(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_377(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_378(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_379(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_380(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_381(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_382(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_383(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_384(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_385(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_386(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_387(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_388(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_389(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_390(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_391(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_392(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_393(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_394(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_395(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_396(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_397(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_398(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_399(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_400(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_401(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_402(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_403(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_404(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_405(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_406(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_407(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_408(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_409(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_410(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_411(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_412(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_413(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_414(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_415(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_416(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_417(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_418(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_419(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_420(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_421(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_422(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_423(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_424(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_425(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_426(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_427(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_428(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_429(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_430(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_431(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_432(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_433(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_434(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_435(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_436(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_437(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_438(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_439(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_440(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_441(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_442(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_443(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_444(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_445(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_446(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_447(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_448(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_449(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_450(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_451(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_452(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_453(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_454(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_455(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_456(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_457(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_458(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_459(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_460(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_461(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_462(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_463(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_464(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_465(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_466(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_467(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_468(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_469(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_470(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_471(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_472(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_473(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_474(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_475(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_476(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_477(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_478(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_479(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_480(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_481(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_482(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_483(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_484(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_485(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_486(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_487(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_488(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_489(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_490(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_491(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_492(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_493(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_494(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_495(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_496(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_497(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_498(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_499(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_500(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_501(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_502(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_503(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_504(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_505(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_506(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_507(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_508(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_509(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_510(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_511(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_512(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_513(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_514(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_515(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_516(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_517(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_518(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_519(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_520(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_521(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_522(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_523(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_524(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_525(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_526(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_527(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_528(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_529(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_530(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_531(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_532(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_533(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_534(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_535(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_536(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_537(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_538(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_539(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_540(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_541(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_542(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_543(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_544(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_545(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_546(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_547(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_548(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_549(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_550(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_551(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_552(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_553(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_554(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_555(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_556(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_557(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_558(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_559(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_560(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_561(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_562(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_563(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_564(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_565(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_566(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_567(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_568(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_569(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_570(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_571(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_572(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_573(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_574(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_575(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_576(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_577(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_578(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_579(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_580(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_581(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_582(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_583(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_584(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_585(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_586(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_587(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_588(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_589(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_590(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_591(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_592(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_593(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_594(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_595(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_596(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_597(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_598(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_599(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_600(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_601(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_602(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_603(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_604(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_605(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_606(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_607(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_608(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_609(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_610(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_611(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_612(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_613(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_614(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_615(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_616(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_617(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_618(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_619(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_620(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_621(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_622(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_623(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_624(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_625(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_626(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_627(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_628(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_629(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_630(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_631(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_632(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_633(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_634(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_635(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_636(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_637(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_638(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_639(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_640(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_641(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_642(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_643(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_644(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_645(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_646(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_647(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_648(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_649(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_650(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_651(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_652(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_653(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_654(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_655(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_656(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_657(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_658(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_659(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_660(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_661(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_662(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_663(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_664(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_665(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_666(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_667(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_668(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_669(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_670(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_671(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_672(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_673(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_674(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_675(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_676(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_677(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_678(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_679(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_680(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_681(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_682(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_683(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_684(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_685(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_686(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_687(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_688(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_689(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_690(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_691(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_692(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_693(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_694(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_695(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_696(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_697(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_698(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_699(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_700(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_701(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_702(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_703(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_704(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_705(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_706(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_707(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_708(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_709(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_710(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_711(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_712(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_713(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_714(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_715(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_716(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_717(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_718(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_719(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_720(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_721(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_722(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_723(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_724(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_725(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_726(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_727(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_728(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_729(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_730(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_731(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_732(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_733(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_734(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_735(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_736(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_737(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_738(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_739(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_740(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_741(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_742(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_743(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_744(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_745(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_746(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_747(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_748(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_749(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_750(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_751(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_752(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_753(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_754(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_755(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_756(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_757(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_758(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_759(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_760(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_761(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_762(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_763(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_764(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_765(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_766(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_767(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_768(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_769(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_770(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_771(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_772(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_773(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_774(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_775(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_776(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_777(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_778(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_779(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_780(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_781(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_782(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_783(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_784(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_785(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_786(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_787(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_788(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_789(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_790(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_791(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_792(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_793(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_794(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_795(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_796(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_797(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_798(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_799(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_800(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_801(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_802(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_803(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_804(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_805(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_806(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_807(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_808(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_809(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_810(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_811(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_812(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_813(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_814(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_815(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_816(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_817(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_818(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_819(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_820(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_821(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_822(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_823(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_824(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_825(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_826(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_827(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_828(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_829(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_830(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_831(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_832(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_833(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_834(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_835(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_836(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_837(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_838(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_839(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_840(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_841(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_842(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_843(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_844(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_845(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_846(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_847(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_848(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_849(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_850(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_851(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_852(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_853(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_854(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_855(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_856(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_857(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_858(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_859(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_860(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_861(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_862(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_863(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_864(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_865(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_866(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_867(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_868(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_869(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_870(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_871(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_872(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_873(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_874(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_875(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_876(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_877(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_878(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_879(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_880(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_881(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_882(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_883(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_884(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_885(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_886(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_887(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_888(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_889(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_890(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_891(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_892(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_893(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_894(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_895(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_896(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_897(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_898(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_899(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_900(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_901(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_902(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_903(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_904(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_905(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_906(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_907(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_908(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_909(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_910(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_911(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_912(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_913(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_914(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_915(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_916(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_917(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_918(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_919(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_920(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_921(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_922(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_923(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_924(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_925(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_926(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_927(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_928(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_929(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_930(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_931(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_932(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_933(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_934(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_935(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_936(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_937(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_938(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_939(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_940(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_941(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_942(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_943(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_944(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_945(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_946(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_947(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_948(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_949(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_950(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_951(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_952(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_953(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_954(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_955(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_956(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_957(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_958(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_959(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_960(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_961(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_962(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_963(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_964(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_965(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_966(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_967(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_968(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_969(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_970(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_971(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_972(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_973(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_974(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_975(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_976(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_977(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_978(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_979(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_980(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_981(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_982(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_983(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_984(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_985(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_986(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_987(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_988(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_989(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_990(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_991(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_992(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_993(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_994(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_995(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_996(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_997(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_998(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_999(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1000(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1001(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1002(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1003(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1004(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1005(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1006(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1007(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1008(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1009(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1010(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1011(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1012(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1013(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1014(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1015(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1016(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1017(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1018(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1019(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1020(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1021(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1022(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1023(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1024(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1025(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1026(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1027(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1028(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1029(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1030(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1031(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1032(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1033(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1034(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1035(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1036(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1037(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1038(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1039(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1040(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1041(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1042(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1043(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1044(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1045(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1046(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1047(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1048(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1049(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1050(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1051(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1052(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1053(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1054(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1055(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1056(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1057(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1058(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1059(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1060(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1061(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1062(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1063(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1064(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1065(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1066(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1067(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1068(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1069(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1070(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1071(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1072(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1073(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1074(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1075(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1076(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1077(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1078(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1079(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1080(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1081(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1082(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1083(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1084(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1085(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1086(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1087(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1088(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1089(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1090(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1091(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1092(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1093(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1094(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1095(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1096(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1097(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1098(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1099(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1100(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1101(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1102(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1103(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1104(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1105(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1106(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1107(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1108(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1109(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1110(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1111(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1112(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1113(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1114(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1115(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1116(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1117(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1118(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1119(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1120(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1121(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1122(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1123(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1124(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1125(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1126(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1127(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1128(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1129(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1130(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1131(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1132(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1133(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1134(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1135(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1136(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1137(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1138(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1139(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1140(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1141(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1142(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1143(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1144(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1145(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1146(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1147(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1148(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1149(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1150(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1151(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1152(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1153(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1154(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1155(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1156(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1157(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1158(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1159(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1160(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1161(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1162(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1163(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1164(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1165(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1166(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1167(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1168(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1169(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1170(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1171(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1172(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1173(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1174(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1175(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1176(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1177(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1178(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1179(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1180(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1181(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1182(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1183(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a < 18350077/65536)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Symbol('a'), Rational(18350077, 65536)))

	eval = pre_cond.subs( { 'a':a, 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1184(a:sympy.Rational,r:sympy.Rational):
	#(r > 299342006059009/4503599627370496) & (a*y**3 - 18350077/33554432 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('r'), Rational(299342006059009, 4503599627370496)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(3))), Rational(-18350077, 33554432)), Integer(0)))