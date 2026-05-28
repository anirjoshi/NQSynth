import sympy
from sympy import *

def pre_condition_0(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 7/4) & (b + delta >= 1/2) & (delta >= b**3 - 3) & (b - delta <= 1/2) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(7, 4)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(1, 2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(1, 2)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 1) & (b + delta >= 1) & (delta >= b**3 - 3) & (b - delta <= 1) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(1)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Integer(1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Integer(1)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_2(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 1/4) & (b + delta >= 3/2) & (delta >= b**3 - 3) & (b - delta <= 3/2) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(1, 4)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(3, 2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(3, 2)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_3(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 7/64) & (b + delta >= 11/8) & (delta >= b**3 - 3) & (b - delta <= 11/8) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(7, 64)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(11, 8)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(11, 8)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_4(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 17/256) & (b + delta >= 23/16) & (delta >= b**3 - 3) & (b - delta <= 23/16) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(17, 256)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(23, 16)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(23, 16)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_5(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 23/1024) & (b + delta >= 45/32) & (delta >= b**3 - 3) & (b - delta <= 45/32) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(23, 1024)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(45, 32)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(45, 32)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_6(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 89/4096) & (b + delta >= 91/64) & (delta >= b**3 - 3) & (b - delta <= 91/64) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(89, 4096)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(91, 64)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(91, 64)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_7(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4241/262144) & (b + delta >= 727/512) & (delta >= b**3 - 3) & (b - delta <= 727/512) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4241, 262144)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(727, 512)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(727, 512)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_8(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 96961/4194304) & (b + delta >= 2913/2048) & (delta >= b**3 - 3) & (b - delta <= 2913/2048) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(96961, 4194304)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(2913, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(2913, 2048)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_9(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 1528073/67108864) & (b + delta >= 11651/8192) & (delta >= b**3 - 3) & (b - delta <= 11651/8192) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(1528073, 67108864)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(11651, 8192)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(11651, 8192)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_10(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 376193/16777216) & (b + delta >= 5825/4096) & (delta >= b**3 - 3) & (b - delta <= 5825/4096) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(376193, 16777216)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(5825, 4096)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(5825, 4096)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_11(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 1481473/67108864) & (b + delta >= 11649/8192) & (delta >= b**3 - 3) & (b - delta <= 11649/8192) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(1481473, 67108864)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(11649, 8192)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(11649, 8192)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_12(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 5879297/268435456) & (b + delta >= 23297/16384) & (delta >= b**3 - 3) & (b - delta <= 23297/16384) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(5879297, 268435456)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(23297, 16384)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(23297, 16384)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_13(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 23424001/1073741824) & (b + delta >= 46593/32768) & (delta >= b**3 - 3) & (b - delta <= 46593/32768) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(23424001, 1073741824)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(46593, 32768)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(46593, 32768)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_14(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 93509633/4294967296) & (b + delta >= 93185/65536) & (delta >= b**3 - 3) & (b - delta <= 93185/65536) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(93509633, 4294967296)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(93185, 65536)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(93185, 65536)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_15(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 373665793/17179869184) & (b + delta >= 186369/131072) & (delta >= b**3 - 3) & (b - delta <= 186369/131072) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(373665793, 17179869184)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(186369, 131072)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(186369, 131072)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_16(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 1493917697/68719476736) & (b + delta >= 372737/262144) & (delta >= b**3 - 3) & (b - delta <= 372737/262144) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(1493917697, 68719476736)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(372737, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(372737, 262144)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_17(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 5974179841/274877906944) & (b + delta >= 745473/524288) & (delta >= b**3 - 3) & (b - delta <= 745473/524288) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(5974179841, 274877906944)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(745473, 524288)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(745473, 524288)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_18(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 23893737473/1099511627776) & (b + delta >= 1490945/1048576) & (delta >= b**3 - 3) & (b - delta <= 1490945/1048576) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(23893737473, 1099511627776)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(1490945, 1048576)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(1490945, 1048576)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_19(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 95568986113/4398046511104) & (b + delta >= 2981889/2097152) & (delta >= b**3 - 3) & (b - delta <= 2981889/2097152) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(95568986113, 4398046511104)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(2981889, 2097152)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(2981889, 2097152)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_20(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 382264016897/17592186044416) & (b + delta >= 5963777/4194304) & (delta >= b**3 - 3) & (b - delta <= 5963777/4194304) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(382264016897, 17592186044416)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(5963777, 4194304)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(5963777, 4194304)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_21(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 1529032212481/70368744177664) & (b + delta >= 11927553/8388608) & (delta >= b**3 - 3) & (b - delta <= 11927553/8388608) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(1529032212481, 70368744177664)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(11927553, 8388608)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(11927553, 8388608)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_22(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 6116081139713/281474976710656) & (b + delta >= 23855105/16777216) & (delta >= b**3 - 3) & (b - delta <= 23855105/16777216) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(6116081139713, 281474976710656)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(23855105, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(23855105, 16777216)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_23(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 24464229138433/1125899906842624) & (b + delta >= 47710209/33554432) & (delta >= b**3 - 3) & (b - delta <= 47710209/33554432) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(24464229138433, 1125899906842624)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(47710209, 33554432)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(47710209, 33554432)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_24(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 97856725712897/4503599627370496) & (b + delta >= 95420417/67108864) & (delta >= b**3 - 3) & (b - delta <= 95420417/67108864) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(97856725712897, 4503599627370496)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(95420417, 67108864)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(95420417, 67108864)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_25(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 391426521169921/18014398509481984) & (b + delta >= 190840833/134217728) & (delta >= b**3 - 3) & (b - delta <= 190840833/134217728) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(391426521169921, 18014398509481984)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(190840833, 134217728)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(190840833, 134217728)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_26(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 1565705321316353/72057594037927936) & (b + delta >= 381681665/268435456) & (delta >= b**3 - 3) & (b - delta <= 381681665/268435456) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(1565705321316353, 72057594037927936)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(381681665, 268435456)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(381681665, 268435456)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_27(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 6262819758538753/288230376151711744) & (b + delta >= 763363329/536870912) & (delta >= b**3 - 3) & (b - delta <= 763363329/536870912) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(6262819758538753, 288230376151711744)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(763363329, 536870912)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(763363329, 536870912)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_28(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 25051275980701697/1152921504606846976) & (b + delta >= 1526726657/1073741824) & (delta >= b**3 - 3) & (b - delta <= 1526726657/1073741824) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(25051275980701697, 1152921504606846976)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(1526726657, 1073741824)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(1526726657, 1073741824)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_29(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 100205097815900161/4611686018427387904) & (b + delta >= 3053453313/2147483648) & (delta >= b**3 - 3) & (b - delta <= 3053453313/2147483648) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(100205097815900161, 4611686018427387904)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(3053453313, 2147483648)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(3053453313, 2147483648)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_30(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 400820379049787393/18446744073709551616) & (b + delta >= 6106906625/4294967296) & (delta >= b**3 - 3) & (b - delta <= 6106906625/4294967296) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(400820379049787393, 18446744073709551616)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(6106906625, 4294967296)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(6106906625, 4294967296)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_31(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 1603281491771523073/73786976294838206464) & (b + delta >= 12213813249/8589934592) & (delta >= b**3 - 3) & (b - delta <= 12213813249/8589934592) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(1603281491771523073, 73786976294838206464)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(12213813249, 8589934592)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(12213813249, 8589934592)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_32(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 6413125918230839297/295147905179352825856) & (b + delta >= 24427626497/17179869184) & (delta >= b**3 - 3) & (b - delta <= 24427626497/17179869184) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(6413125918230839297, 295147905179352825856)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(24427626497, 17179869184)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(24427626497, 17179869184)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_33(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 25652503575212851201/1180591620717411303424) & (b + delta >= 48855252993/34359738368) & (delta >= b**3 - 3) & (b - delta <= 48855252993/34359738368) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(25652503575212851201, 1180591620717411303424)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(48855252993, 34359738368)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(48855252993, 34359738368)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_34(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 102610014105430392833/4722366482869645213696) & (b + delta >= 97710505985/68719476736) & (delta >= b**3 - 3) & (b - delta <= 97710505985/68719476736) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(102610014105430392833, 4722366482869645213696)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(97710505985, 68719476736)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(97710505985, 68719476736)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_35(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 410440056030879547393/18889465931478580854784) & (b + delta >= 195421011969/137438953472) & (delta >= b**3 - 3) & (b - delta <= 195421011969/137438953472) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(410440056030879547393, 18889465931478580854784)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(195421011969, 137438953472)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(195421011969, 137438953472)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_36(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 1641760223341834141697/75557863725914323419136) & (b + delta >= 390842023937/274877906944) & (delta >= b**3 - 3) & (b - delta <= 390842023937/274877906944) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(1641760223341834141697, 75557863725914323419136)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(390842023937, 274877906944)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(390842023937, 274877906944)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_37(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 6567040891803968471041/302231454903657293676544) & (b + delta >= 781684047873/549755813888) & (delta >= b**3 - 3) & (b - delta <= 781684047873/549755813888) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(6567040891803968471041, 302231454903657293676544)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(781684047873, 549755813888)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(781684047873, 549755813888)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_38(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 26268163564089137692673/1208925819614629174706176) & (b + delta >= 1563368095745/1099511627776) & (delta >= b**3 - 3) & (b - delta <= 1563368095745/1099511627776) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(26268163564089137692673, 1208925819614629174706176)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(1563368095745, 1099511627776)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(1563368095745, 1099511627776)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_39(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 105072654250103078387713/4835703278458516698824704) & (b + delta >= 3126736191489/2199023255552) & (delta >= b**3 - 3) & (b - delta <= 3126736191489/2199023255552) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(105072654250103078387713, 4835703278458516698824704)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(3126736191489, 2199023255552)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(3126736191489, 2199023255552)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_40(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 420290616987905368784897/19342813113834066795298816) & (b + delta >= 6253472382977/4398046511104) & (delta >= b**3 - 3) & (b - delta <= 6253472382977/4398046511104) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(420290616987905368784897, 19342813113834066795298816)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(6253472382977, 4398046511104)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(6253472382977, 4398046511104)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_41(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 1681162467926607585607681/77371252455336267181195264) & (b + delta >= 12506944765953/8796093022208) & (delta >= b**3 - 3) & (b - delta <= 12506944765953/8796093022208) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(1681162467926607585607681, 77371252455336267181195264)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(12506944765953, 8796093022208)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(12506944765953, 8796093022208)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_42(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 6724649871656402563366913/309485009821345068724781056) & (b + delta >= 25013889531905/17592186044416) & (delta >= b**3 - 3) & (b - delta <= 25013889531905/17592186044416) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(6724649871656402563366913, 309485009821345068724781056)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(25013889531905, 17592186044416)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(25013889531905, 17592186044416)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_43(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 26898599486525554695340033/1237940039285380274899124224) & (b + delta >= 50027779063809/35184372088832) & (delta >= b**3 - 3) & (b - delta <= 50027779063809/35184372088832) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(26898599486525554695340033, 1237940039285380274899124224)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(50027779063809, 35184372088832)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(50027779063809, 35184372088832)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_44(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 107594397945902107665104897/4951760157141521099596496896) & (b + delta >= 100055558127617/70368744177664) & (delta >= b**3 - 3) & (b - delta <= 100055558127617/70368744177664) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(107594397945902107665104897, 4951760157141521099596496896)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(100055558127617, 70368744177664)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(100055558127617, 70368744177664)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_45(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 430377591783208208427909121/19807040628566084398385987584) & (b + delta >= 200111116255233/140737488355328) & (delta >= b**3 - 3) & (b - delta <= 200111116255233/140737488355328) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(430377591783208208427909121, 19807040628566084398385987584)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(200111116255233, 140737488355328)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(200111116255233, 140737488355328)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_46(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 1721510367132032389246615553/79228162514264337593543950336) & (b + delta >= 400222232510465/281474976710656) & (delta >= b**3 - 3) & (b - delta <= 400222232510465/281474976710656) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(1721510367132032389246615553, 79228162514264337593543950336)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(400222232510465, 281474976710656)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(400222232510465, 281474976710656)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_47(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 6886041468526528668056420353/316912650057057350374175801344) & (b + delta >= 800444465020929/562949953421312) & (delta >= b**3 - 3) & (b - delta <= 800444465020929/562949953421312) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(6886041468526528668056420353, 316912650057057350374175801344)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(800444465020929, 562949953421312)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(800444465020929, 562949953421312)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_48(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 27544165874102912894365597697/1267650600228229401496703205376) & (b + delta >= 1600888930041857/1125899906842624) & (delta >= b**3 - 3) & (b - delta <= 1600888930041857/1125899906842624) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(27544165874102912894365597697, 1267650600228229401496703205376)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(1600888930041857, 1125899906842624)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(1600888930041857, 1125899906842624)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_49(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 110176663496405248021742223361/5070602400912917605986812821504) & (b + delta >= 3201777860083713/2251799813685248) & (delta >= b**3 - 3) & (b - delta <= 3201777860083713/2251799813685248) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(110176663496405248021742223361, 5070602400912917605986812821504)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(3201777860083713, 2251799813685248)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(3201777860083713, 2251799813685248)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_50(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 440706653985608184975528558593/20282409603651670423947251286016) & (b + delta >= 6403555720167425/4503599627370496) & (delta >= b**3 - 3) & (b - delta <= 6403555720167425/4503599627370496) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(440706653985608184975528558593, 20282409603651670423947251286016)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(6403555720167425, 4503599627370496)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(6403555720167425, 4503599627370496)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_51(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 1762826615942407125679233564673/81129638414606681695789005144064) & (b + delta >= 12807111440334849/9007199254740992) & (delta >= b**3 - 3) & (b - delta <= 12807111440334849/9007199254740992) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(1762826615942407125679233564673, 81129638414606681695789005144064)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(12807111440334849, 9007199254740992)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(12807111440334849, 9007199254740992)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_52(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 1762826615942407125679233564673/81129638414606681695789005144064) & (b + delta >= 12807111440334849/9007199254740992) & (delta >= b**3 - 3) & (b - delta <= 12807111440334849/9007199254740992) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(1762826615942407125679233564673, 81129638414606681695789005144064)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(12807111440334849, 9007199254740992)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(12807111440334849, 9007199254740992)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_53(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 1762826615942407125679233564673/81129638414606681695789005144064) & (b + delta >= 12807111440334849/9007199254740992) & (delta >= b**3 - 3) & (b - delta <= 12807111440334849/9007199254740992) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(1762826615942407125679233564673, 81129638414606681695789005144064)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(12807111440334849, 9007199254740992)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(12807111440334849, 9007199254740992)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_54(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 1681162468727052050629697/77371252455336267181195264) & (b + delta >= 12506944765985/8796093022208) & (delta >= b**3 - 3) & (b - delta <= 12506944765985/8796093022208) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(1681162468727052050629697, 77371252455336267181195264)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(12506944765985, 8796093022208)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(12506944765985, 8796093022208)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_55(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 7051306463771216584535535780929/324518553658426726783156020576256) & (b + delta >= 25614222880669729/18014398509481984) & (delta >= b**3 - 3) & (b - delta <= 25614222880669729/18014398509481984) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(7051306463771216584535535780929, 324518553658426726783156020576256)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(25614222880669729, 18014398509481984)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(25614222880669729, 18014398509481984)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_56(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 26898599499332666135691521/1237940039285380274899124224) & (b + delta >= 50027779063937/35184372088832) & (delta >= b**3 - 3) & (b - delta <= 50027779063937/35184372088832) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(26898599499332666135691521, 1237940039285380274899124224)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(50027779063937, 35184372088832)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(50027779063937, 35184372088832)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_57(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 7051306463769577274271172919297/324518553658426726783156020576256) & (b + delta >= 25614222880669697/18014398509481984) & (delta >= b**3 - 3) & (b - delta <= 25614222880669697/18014398509481984) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(7051306463769577274271172919297, 324518553658426726783156020576256)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(25614222880669697, 18014398509481984)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(25614222880669697, 18014398509481984)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_58(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 107594397997130553426510337/4951760157141521099596496896) & (b + delta >= 100055558127873/70368744177664) & (delta >= b**3 - 3) & (b - delta <= 100055558127873/70368744177664) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(107594397997130553426510337, 4951760157141521099596496896)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(100055558127873, 70368744177664)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(100055558127873, 70368744177664)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_59(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 28205225855084763881250620444801/1298074214633706907132624082305024) & (b + delta >= 51228445761339457/36028797018963968) & (delta >= b**3 - 3) & (b - delta <= 51228445761339457/36028797018963968) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(28205225855084763881250620444801, 1298074214633706907132624082305024)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(51228445761339457, 36028797018963968)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(51228445761339457, 36028797018963968)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_60(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 430377591988121991473529857/19807040628566084398385987584) & (b + delta >= 200111116255745/140737488355328) & (delta >= b**3 - 3) & (b - delta <= 200111116255745/140737488355328) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(430377591988121991473529857, 19807040628566084398385987584)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(200111116255745, 140737488355328)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(200111116255745, 140737488355328)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_61(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 1721510367951687521429096449/79228162514264337593543950336) & (b + delta >= 400222232511489/281474976710656) & (delta >= b**3 - 3) & (b - delta <= 400222232511489/281474976710656) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(1721510367951687521429096449, 79228162514264337593543950336)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(400222232511489, 281474976710656)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(400222232511489, 281474976710656)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_62(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 26898599489727332555424833/1237940039285380274899124224) & (b + delta >= 50027779063841/35184372088832) & (delta >= b**3 - 3) & (b - delta <= 50027779063841/35184372088832) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(26898599489727332555424833, 1237940039285380274899124224)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(50027779063841, 35184372088832)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(50027779063841, 35184372088832)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_63(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 430377591834436654189265153/19807040628566084398385987584) & (b + delta >= 200111116255361/140737488355328) & (delta >= b**3 - 3) & (b - delta <= 200111116255361/140737488355328) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(430377591834436654189265153, 19807040628566084398385987584)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(200111116255361, 140737488355328)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(200111116255361, 140737488355328)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_64(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 1721510367336946172292039169/79228162514264337593543950336) & (b + delta >= 400222232510721/281474976710656) & (delta >= b**3 - 3) & (b - delta <= 400222232510721/281474976710656) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(1721510367336946172292039169, 79228162514264337593543950336)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(400222232510721, 281474976710656)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(400222232510721, 281474976710656)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_65(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 1762826615943226780811414996033/81129638414606681695789005144064) & (b + delta >= 12807111440334881/9007199254740992) & (delta >= b**3 - 3) & (b - delta <= 12807111440334881/9007199254740992) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(1762826615943226780811414996033, 81129638414606681695789005144064)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(12807111440334881, 9007199254740992)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(12807111440334881, 9007199254740992)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_66(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 6886041469346183800238113793/316912650057057350374175801344) & (b + delta >= 800444465021441/562949953421312) & (delta >= b**3 - 3) & (b - delta <= 800444465021441/562949953421312) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(6886041469346183800238113793, 316912650057057350374175801344)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(800444465021441, 562949953421312)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(800444465021441, 562949953421312)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_67(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 27544165877381533423092369409/1267650600228229401496703205376) & (b + delta >= 1600888930042881/1125899906842624) & (delta >= b**3 - 3) & (b - delta <= 1600888930042881/1125899906842624) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(27544165877381533423092369409, 1267650600228229401496703205376)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(1600888930042881, 1125899906842624)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(1600888930042881, 1125899906842624)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_68(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 110176663509519730136649306113/5070602400912917605986812821504) & (b + delta >= 3201777860085761/2251799813685248) & (delta >= b**3 - 3) & (b - delta <= 3201777860085761/2251799813685248) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(110176663509519730136649306113, 5070602400912917605986812821504)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(3201777860085761, 2251799813685248)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(3201777860085761, 2251799813685248)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_69(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 440706654038066113435156881409/20282409603651670423947251286016) & (b + delta >= 6403555720171521/4503599627370496) & (delta >= b**3 - 3) & (b - delta <= 6403555720171521/4503599627370496) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(440706654038066113435156881409, 20282409603651670423947251286016)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(6403555720171521, 4503599627370496)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(6403555720171521, 4503599627370496)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_70(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 1762826616152238839517746839553/81129638414606681695789005144064) & (b + delta >= 12807111440343041/9007199254740992) & (delta >= b**3 - 3) & (b - delta <= 12807111440343041/9007199254740992) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(1762826616152238839517746839553, 81129638414606681695789005144064)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(12807111440343041, 9007199254740992)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(12807111440343041, 9007199254740992)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_71(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 1762826616152238839517746839553/81129638414606681695789005144064) & (b + delta >= 12807111440343041/9007199254740992) & (delta >= b**3 - 3) & (b - delta <= 12807111440343041/9007199254740992) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(1762826616152238839517746839553, 81129638414606681695789005144064)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(12807111440343041, 9007199254740992)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(12807111440343041, 9007199254740992)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_72(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 1762826616152238839517746839553/81129638414606681695789005144064) & (b + delta >= 12807111440343041/9007199254740992) & (delta >= b**3 - 3) & (b - delta <= 12807111440343041/9007199254740992) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(1762826616152238839517746839553, 81129638414606681695789005144064)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(12807111440343041, 9007199254740992)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(12807111440343041, 9007199254740992)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_73(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 1762826616152238839517746839553/81129638414606681695789005144064) & (b + delta >= 12807111440343041/9007199254740992) & (delta >= b**3 - 3) & (b - delta <= 12807111440343041/9007199254740992) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(1762826616152238839517746839553, 81129638414606681695789005144064)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(12807111440343041, 9007199254740992)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(12807111440343041, 9007199254740992)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_74(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 7051306464610543439889589896257/324518553658426726783156020576256) & (b + delta >= 25614222880686113/18014398509481984) & (delta >= b**3 - 3) & (b - delta <= 25614222880686113/18014398509481984) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(7051306464610543439889589896257, 324518553658426726783156020576256)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(25614222880686113, 18014398509481984)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(25614222880686113, 18014398509481984)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_75(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 7051306464610543439889589896257/324518553658426726783156020576256) & (b + delta >= 25614222880686113/18014398509481984) & (delta >= b**3 - 3) & (b - delta <= 25614222880686113/18014398509481984) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(7051306464610543439889589896257, 324518553658426726783156020576256)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(25614222880686113, 18014398509481984)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(25614222880686113, 18014398509481984)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_76(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 7051306464610543439889589896257/324518553658426726783156020576256) & (b + delta >= 25614222880686113/18014398509481984) & (delta >= b**3 - 3) & (b - delta <= 25614222880686113/18014398509481984) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(7051306464610543439889589896257, 324518553658426726783156020576256)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(25614222880686113, 18014398509481984)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(25614222880686113, 18014398509481984)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_77(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 110176663549068090264466768961/5070602400912917605986812821504) & (b + delta >= 3201777860091937/2251799813685248) & (delta >= b**3 - 3) & (b - delta <= 3201777860091937/2251799813685248) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(110176663549068090264466768961, 5070602400912917605986812821504)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(3201777860091937, 2251799813685248)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(3201777860091937, 2251799813685248)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_78(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 440706654038066113435156881409/20282409603651670423947251286016) & (b + delta >= 6403555720171521/4503599627370496) & (delta >= b**3 - 3) & (b - delta <= 6403555720171521/4503599627370496) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(440706654038066113435156881409, 20282409603651670423947251286016)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(6403555720171521, 4503599627370496)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(6403555720171521, 4503599627370496)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_79(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 1762826616785012601562826096897/81129638414606681695789005144064) & (b + delta >= 12807111440367745/9007199254740992) & (delta >= b**3 - 3) & (b - delta <= 12807111440367745/9007199254740992) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(1762826616785012601562826096897, 81129638414606681695789005144064)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(12807111440367745, 9007199254740992)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(12807111440367745, 9007199254740992)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_80(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 6724649871656402563366913/309485009821345068724781056) & (b + delta >= 25013889531905/17592186044416) & (delta >= b**3 - 3) & (b - delta <= 25013889531905/17592186044416) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(6724649871656402563366913, 309485009821345068724781056)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(25013889531905, 17592186044416)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(25013889531905, 17592186044416)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_81(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 1762826616785012601562826096897/81129638414606681695789005144064) & (b + delta >= 12807111440367745/9007199254740992) & (delta >= b**3 - 3) & (b - delta <= 12807111440367745/9007199254740992) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(1762826616785012601562826096897, 81129638414606681695789005144064)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(12807111440367745, 9007199254740992)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(12807111440367745, 9007199254740992)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_82(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 1762826616785012601562826096897/81129638414606681695789005144064) & (b + delta >= 12807111440367745/9007199254740992) & (delta >= b**3 - 3) & (b - delta <= 12807111440367745/9007199254740992) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(1762826616785012601562826096897, 81129638414606681695789005144064)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(12807111440367745, 9007199254740992)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(12807111440367745, 9007199254740992)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_83(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 110176663549068090264466768961/5070602400912917605986812821504) & (b + delta >= 3201777860091937/2251799813685248) & (delta >= b**3 - 3) & (b - delta <= 3201777860091937/2251799813685248) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(110176663549068090264466768961, 5070602400912917605986812821504)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(3201777860091937, 2251799813685248)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(3201777860091937, 2251799813685248)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_84(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 6724649871656402563366913/309485009821345068724781056) & (b + delta >= 25013889531905/17592186044416) & (delta >= b**3 - 3) & (b - delta <= 25013889531905/17592186044416) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(6724649871656402563366913, 309485009821345068724781056)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(25013889531905, 17592186044416)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(25013889531905, 17592186044416)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_85(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 110176663549068090264466768961/5070602400912917605986812821504) & (b + delta >= 3201777860091937/2251799813685248) & (delta >= b**3 - 3) & (b - delta <= 3201777860091937/2251799813685248) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(110176663549068090264466768961, 5070602400912917605986812821504)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(3201777860091937, 2251799813685248)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(3201777860091937, 2251799813685248)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_86(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 1805134454725424068744907527035953/83076749736557242056487941267521536) & (b + delta >= 409827566090715655/288230376151711744) & (delta >= b**3 - 3) & (b - delta <= 409827566090715655/288230376151711744) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(1805134454725424068744907527035953, 83076749736557242056487941267521536)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(409827566090715655, 288230376151711744)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(409827566090715655, 288230376151711744)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_87(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 110176663549068090264466768961/5070602400912917605986812821504) & (b + delta >= 3201777860091937/2251799813685248) & (delta >= b**3 - 3) & (b - delta <= 3201777860091937/2251799813685248) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(110176663549068090264466768961, 5070602400912917605986812821504)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(3201777860091937, 2251799813685248)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(3201777860091937, 2251799813685248)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_88(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 7051306467139999177805542916609/324518553658426726783156020576256) & (b + delta >= 25614222880735489/18014398509481984) & (delta >= b**3 - 3) & (b - delta <= 25614222880735489/18014398509481984) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(7051306467139999177805542916609, 324518553658426726783156020576256)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(25614222880735489, 18014398509481984)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(25614222880735489, 18014398509481984)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_89(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 1762826616152238839517746839553/81129638414606681695789005144064) & (b + delta >= 12807111440343041/9007199254740992) & (delta >= b**3 - 3) & (b - delta <= 12807111440343041/9007199254740992) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(1762826616152238839517746839553, 81129638414606681695789005144064)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(12807111440343041, 9007199254740992)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(12807111440343041, 9007199254740992)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_90(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 7051306467139999177805542916609/324518553658426726783156020576256) & (b + delta >= 25614222880735489/18014398509481984) & (delta >= b**3 - 3) & (b - delta <= 25614222880735489/18014398509481984) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(7051306467139999177805542916609, 324518553658426726783156020576256)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(25614222880735489, 18014398509481984)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(25614222880735489, 18014398509481984)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_91(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 6262868613792833/288230376151711744) & (b + delta >= 763363361/536870912) & (delta >= b**3 - 3) & (b - delta <= 763363361/536870912) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(6262868613792833, 288230376151711744)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(763363361, 536870912)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(763363361, 536870912)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_92(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 100205879499964673/4611686018427387904) & (b + delta >= 3053453441/2147483648) & (delta >= b**3 - 3) & (b - delta <= 3053453441/2147483648) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(100205879499964673, 4611686018427387904)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(3053453441, 2147483648)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(3053453441, 2147483648)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_93(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 26898599499732888368203033/1237940039285380274899124224) & (b + delta >= 50027779063941/35184372088832) & (delta >= b**3 - 3) & (b - delta <= 50027779063941/35184372088832) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(26898599499732888368203033, 1237940039285380274899124224)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(50027779063941, 35184372088832)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(50027779063941, 35184372088832)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_94(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 1721510367977301744309832769/79228162514264337593543950336) & (b + delta >= 400222232511521/281474976710656) & (delta >= b**3 - 3) & (b - delta <= 400222232511521/281474976710656) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(1721510367977301744309832769, 79228162514264337593543950336)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(400222232511521, 281474976710656)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(400222232511521, 281474976710656)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_95(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 27544165887627222575377047809/1267650600228229401496703205376) & (b + delta >= 1600888930046081/1125899906842624) & (delta >= b**3 - 3) & (b - delta <= 1600888930046081/1125899906842624) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(27544165887627222575377047809, 1267650600228229401496703205376)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(1600888930046081, 1125899906842624)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(1600888930046081, 1125899906842624)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_96(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 1721510367157646612127286337/79228162514264337593543950336) & (b + delta >= 400222232510497/281474976710656) & (delta >= b**3 - 3) & (b - delta <= 400222232510497/281474976710656) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(1721510367157646612127286337, 79228162514264337593543950336)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(400222232510497, 281474976710656)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(400222232510497, 281474976710656)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_97(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 27544165874512740460456329473/1267650600228229401496703205376) & (b + delta >= 1600888930041985/1125899906842624) & (delta >= b**3 - 3) & (b - delta <= 1600888930041985/1125899906842624) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(27544165874512740460456329473, 1267650600228229401496703205376)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(1600888930041985, 1125899906842624)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(1600888930041985, 1125899906842624)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_98(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 110176663498044558286105149953/5070602400912917605986812821504) & (b + delta >= 3201777860083969/2251799813685248) & (delta >= b**3 - 3) & (b - delta <= 3201777860083969/2251799813685248) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(110176663498044558286105149953, 5070602400912917605986812821504)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(3201777860083969, 2251799813685248)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(3201777860083969, 2251799813685248)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_99(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 440706653992165426032980263937/20282409603651670423947251286016) & (b + delta >= 6403555720167937/4503599627370496) & (delta >= b**3 - 3) & (b - delta <= 6403555720167937/4503599627370496) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(440706653992165426032980263937, 20282409603651670423947251286016)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(6403555720167937, 4503599627370496)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(6403555720167937, 4503599627370496)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_100(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 440706653985608184975528558593/20282409603651670423947251286016) & (b + delta >= 6403555720167425/4503599627370496) & (delta >= b**3 - 3) & (b - delta <= 6403555720167425/4503599627370496) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(440706653985608184975528558593, 20282409603651670423947251286016)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(6403555720167425, 4503599627370496)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(6403555720167425, 4503599627370496)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_101(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 1762826615968636089909040384001/81129638414606681695789005144064) & (b + delta >= 12807111440335873/9007199254740992) & (delta >= b**3 - 3) & (b - delta <= 12807111440335873/9007199254740992) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(1762826615968636089909040384001, 81129638414606681695789005144064)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(12807111440335873, 9007199254740992)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(12807111440335873, 9007199254740992)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_102(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 1762826615968636089909040384001/81129638414606681695789005144064) & (b + delta >= 12807111440335873/9007199254740992) & (delta >= b**3 - 3) & (b - delta <= 12807111440335873/9007199254740992) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(1762826615968636089909040384001, 81129638414606681695789005144064)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(12807111440335873, 9007199254740992)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(12807111440335873, 9007199254740992)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_103(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 1805134454725424068744907527035953/83076749736557242056487941267521536) & (b + delta >= 409827566090715655/288230376151711744) & (delta >= b**3 - 3) & (b - delta <= 409827566090715655/288230376151711744) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(1805134454725424068744907527035953, 83076749736557242056487941267521536)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(409827566090715655, 288230376151711744)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(409827566090715655, 288230376151711744)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_104(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 1762826615942407125679233564673/81129638414606681695789005144064) & (b + delta >= 12807111440334849/9007199254740992) & (delta >= b**3 - 3) & (b - delta <= 12807111440334849/9007199254740992) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(1762826615942407125679233564673, 81129638414606681695789005144064)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(12807111440334849, 9007199254740992)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(12807111440334849, 9007199254740992)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_105(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 1762826615968687318354801727497/81129638414606681695789005144064) & (b + delta >= 12807111440335875/9007199254740992) & (delta >= b**3 - 3) & (b - delta <= 12807111440335875/9007199254740992) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(1762826615968687318354801727497, 81129638414606681695789005144064)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(12807111440335875, 9007199254740992)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(12807111440335875, 9007199254740992)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_106(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 28205225855499304464351395700961/1298074214633706907132624082305024) & (b + delta >= 51228445761343503/36028797018963968) & (delta >= b**3 - 3) & (b - delta <= 51228445761343503/36028797018963968) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(28205225855499304464351395700961, 1298074214633706907132624082305024)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(51228445761343503, 36028797018963968)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(51228445761343503, 36028797018963968)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_107(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 28205225855501148688398804067393/1298074214633706907132624082305024) & (b + delta >= 51228445761343521/36028797018963968) & (delta >= b**3 - 3) & (b - delta <= 51228445761343521/36028797018963968) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(28205225855501148688398804067393, 1298074214633706907132624082305024)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(51228445761343521, 36028797018963968)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(51228445761343521, 36028797018963968)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_108(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 28205225855501148688398804067393/1298074214633706907132624082305024) & (b + delta >= 51228445761343521/36028797018963968) & (delta >= b**3 - 3) & (b - delta <= 51228445761343521/36028797018963968) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(28205225855501148688398804067393, 1298074214633706907132624082305024)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(51228445761343521, 36028797018963968)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(51228445761343521, 36028797018963968)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_109(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 28205225855501148688398804067393/1298074214633706907132624082305024) & (b + delta >= 51228445761343521/36028797018963968) & (delta >= b**3 - 3) & (b - delta <= 51228445761343521/36028797018963968) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(28205225855501148688398804067393, 1298074214633706907132624082305024)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(51228445761343521, 36028797018963968)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(51228445761343521, 36028797018963968)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_110(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 440706654038091727658037567497/20282409603651670423947251286016) & (b + delta >= 6403555720171523/4503599627370496) & (delta >= b**3 - 3) & (b - delta <= 6403555720171523/4503599627370496) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(440706654038091727658037567497, 20282409603651670423947251286016)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(6403555720171523, 4503599627370496)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(6403555720171523, 4503599627370496)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_111(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 1762826616152341296409269583897/81129638414606681695789005144064) & (b + delta >= 12807111440343045/9007199254740992) & (delta >= b**3 - 3) & (b - delta <= 12807111440343045/9007199254740992) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(1762826616152341296409269583897, 81129638414606681695789005144064)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(12807111440343045, 9007199254740992)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(12807111440343045, 9007199254740992)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_112(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 1762826616152341296409269583897/81129638414606681695789005144064) & (b + delta >= 12807111440343045/9007199254740992) & (delta >= b**3 - 3) & (b - delta <= 12807111440343045/9007199254740992) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(1762826616152341296409269583897, 81129638414606681695789005144064)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(12807111440343045, 9007199254740992)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(12807111440343045, 9007199254740992)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_113(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 1762826616152341296409269583897/81129638414606681695789005144064) & (b + delta >= 12807111440343045/9007199254740992) & (delta >= b**3 - 3) & (b - delta <= 12807111440343045/9007199254740992) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(1762826616152341296409269583897, 81129638414606681695789005144064)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(12807111440343045, 9007199254740992)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(12807111440343045, 9007199254740992)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_114(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 1762826616152238839517746839553/81129638414606681695789005144064) & (b + delta >= 12807111440343041/9007199254740992) & (delta >= b**3 - 3) & (b - delta <= 12807111440343041/9007199254740992) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(1762826616152238839517746839553, 81129638414606681695789005144064)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(12807111440343041, 9007199254740992)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(12807111440343041, 9007199254740992)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_115(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 1762826616152392524855030956081/81129638414606681695789005144064) & (b + delta >= 12807111440343047/9007199254740992) & (delta >= b**3 - 3) & (b - delta <= 12807111440343047/9007199254740992) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(1762826616152392524855030956081, 81129638414606681695789005144064)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(12807111440343047, 9007199254740992)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(12807111440343047, 9007199254740992)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_116(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 6886041471805149196786339841/316912650057057350374175801344) & (b + delta >= 800444465022977/562949953421312) & (delta >= b**3 - 3) & (b - delta <= 800444465022977/562949953421312) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(6886041471805149196786339841, 316912650057057350374175801344)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(800444465022977, 562949953421312)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(800444465022977, 562949953421312)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_117(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 27544165887217395009285267457/1267650600228229401496703205376) & (b + delta >= 1600888930045953/1125899906842624) & (delta >= b**3 - 3) & (b - delta <= 1600888930045953/1125899906842624) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(27544165887217395009285267457, 1267650600228229401496703205376)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(1600888930045953, 1125899906842624)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(1600888930045953, 1125899906842624)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_118(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 1762826616152238839517746839553/81129638414606681695789005144064) & (b + delta >= 12807111440343041/9007199254740992) & (delta >= b**3 - 3) & (b - delta <= 12807111440343041/9007199254740992) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(1762826616152238839517746839553, 81129638414606681695789005144064)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(12807111440343041, 9007199254740992)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(12807111440343041, 9007199254740992)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_119(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 26898599486525554695340033/1237940039285380274899124224) & (b + delta >= 50027779063809/35184372088832) & (delta >= b**3 - 3) & (b - delta <= 50027779063809/35184372088832) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(26898599486525554695340033, 1237940039285380274899124224)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(50027779063809, 35184372088832)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(50027779063809, 35184372088832)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_120(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 6724649871656402563366913/309485009821345068724781056) & (b + delta >= 25013889531905/17592186044416) & (delta >= b**3 - 3) & (b - delta <= 25013889531905/17592186044416) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(6724649871656402563366913, 309485009821345068724781056)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(25013889531905, 17592186044416)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(25013889531905, 17592186044416)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_121(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 19873/1048576) & (b + delta >= 1455/1024) & (delta >= b**3 - 3) & (b - delta <= 1455/1024) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(19873, 1048576)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(1455, 1024)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(1455, 1024)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_122(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 107594397945902107665104897/4951760157141521099596496896) & (b + delta >= 100055558127617/70368744177664) & (delta >= b**3 - 3) & (b - delta <= 100055558127617/70368744177664) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(107594397945902107665104897, 4951760157141521099596496896)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(100055558127617, 70368744177664)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(100055558127617, 70368744177664)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_123(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 430377591796015319868245057/19807040628566084398385987584) & (b + delta >= 200111116255265/140737488355328) & (delta >= b**3 - 3) & (b - delta <= 200111116255265/140737488355328) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(430377591796015319868245057, 19807040628566084398385987584)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(200111116255265, 140737488355328)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(200111116255265, 140737488355328)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_124(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 112820903421995783460924265185809/5192296858534827628530496329220096) & (b + delta >= 102456891522686999/72057594037927936) & (delta >= b**3 - 3) & (b - delta <= 102456891522686999/72057594037927936) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(112820903421995783460924265185809, 5192296858534827628530496329220096)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(102456891522686999, 72057594037927936)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(102456891522686999, 72057594037927936)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_125(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 105072654250103078387713/4835703278458516698824704) & (b + delta >= 3126736191489/2199023255552) & (delta >= b**3 - 3) & (b - delta <= 3126736191489/2199023255552) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(105072654250103078387713, 4835703278458516698824704)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(3126736191489, 2199023255552)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(3126736191489, 2199023255552)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_126(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 1762826615942407125679233564673/81129638414606681695789005144064) & (b + delta >= 12807111440334849/9007199254740992) & (delta >= b**3 - 3) & (b - delta <= 12807111440334849/9007199254740992) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(1762826615942407125679233564673, 81129638414606681695789005144064)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(12807111440334849, 9007199254740992)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(12807111440334849, 9007199254740992)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_127(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 1762826615942407125679233564673/81129638414606681695789005144064) & (b + delta >= 12807111440334849/9007199254740992) & (delta >= b**3 - 3) & (b - delta <= 12807111440334849/9007199254740992) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(1762826615942407125679233564673, 81129638414606681695789005144064)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(12807111440334849, 9007199254740992)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(12807111440334849, 9007199254740992)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_128(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 110176663496405248021742223361/5070602400912917605986812821504) & (b + delta >= 3201777860083713/2251799813685248) & (delta >= b**3 - 3) & (b - delta <= 3201777860083713/2251799813685248) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(110176663496405248021742223361, 5070602400912917605986812821504)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(3201777860083713, 2251799813685248)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(3201777860083713, 2251799813685248)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_129(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 1762826616152238839517746839553/81129638414606681695789005144064) & (b + delta >= 12807111440343041/9007199254740992) & (delta >= b**3 - 3) & (b - delta <= 12807111440343041/9007199254740992) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(1762826616152238839517746839553, 81129638414606681695789005144064)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(12807111440343041, 9007199254740992)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(12807111440343041, 9007199254740992)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_130(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 6886041468731442451101794561/316912650057057350374175801344) & (b + delta >= 800444465021057/562949953421312) & (delta >= b**3 - 3) & (b - delta <= 800444465021057/562949953421312) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(6886041468731442451101794561, 316912650057057350374175801344)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(800444465021057, 562949953421312)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(800444465021057, 562949953421312)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_131(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 27544165874922568026547094017/1267650600228229401496703205376) & (b + delta >= 1600888930042113/1125899906842624) & (delta >= b**3 - 3) & (b - delta <= 1600888930042113/1125899906842624) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(27544165874922568026547094017, 1267650600228229401496703205376)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(1600888930042113, 1125899906842624)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(1600888930042113, 1125899906842624)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_132(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 1762826616152238839517746839553/81129638414606681695789005144064) & (b + delta >= 12807111440343041/9007199254740992) & (delta >= b**3 - 3) & (b - delta <= 12807111440343041/9007199254740992) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(1762826616152238839517746839553, 81129638414606681695789005144064)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(12807111440343041, 9007199254740992)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(12807111440343041, 9007199254740992)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_133(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 110176663499683868550468207617/5070602400912917605986812821504) & (b + delta >= 3201777860084225/2251799813685248) & (delta >= b**3 - 3) & (b - delta <= 3201777860084225/2251799813685248) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(110176663499683868550468207617, 5070602400912917605986812821504)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(3201777860084225, 2251799813685248)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(3201777860084225, 2251799813685248)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_134(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 1762826616152341296409269583897/81129638414606681695789005144064) & (b + delta >= 12807111440343045/9007199254740992) & (delta >= b**3 - 3) & (b - delta <= 12807111440343045/9007199254740992) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(1762826616152341296409269583897, 81129638414606681695789005144064)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(12807111440343045, 9007199254740992)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(12807111440343045, 9007199254740992)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_135(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 1762826616152341296409269583897/81129638414606681695789005144064) & (b + delta >= 12807111440343045/9007199254740992) & (delta >= b**3 - 3) & (b - delta <= 12807111440343045/9007199254740992) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(1762826616152341296409269583897, 81129638414606681695789005144064)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(12807111440343045, 9007199254740992)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(12807111440343045, 9007199254740992)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_136(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 1762826616152341296409269583897/81129638414606681695789005144064) & (b + delta >= 12807111440343045/9007199254740992) & (delta >= b**3 - 3) & (b - delta <= 12807111440343045/9007199254740992) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(1762826616152341296409269583897, 81129638414606681695789005144064)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(12807111440343045, 9007199254740992)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(12807111440343045, 9007199254740992)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_137(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 1762826616152341296409269583897/81129638414606681695789005144064) & (b + delta >= 12807111440343045/9007199254740992) & (delta >= b**3 - 3) & (b - delta <= 12807111440343045/9007199254740992) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(1762826616152341296409269583897, 81129638414606681695789005144064)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(12807111440343045, 9007199254740992)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(12807111440343045, 9007199254740992)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_138(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 1762826616152341296409269583897/81129638414606681695789005144064) & (b + delta >= 12807111440343045/9007199254740992) & (delta >= b**3 - 3) & (b - delta <= 12807111440343045/9007199254740992) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(1762826616152341296409269583897, 81129638414606681695789005144064)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(12807111440343045, 9007199254740992)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(12807111440343045, 9007199254740992)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_139(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 1762826616152341296409269583897/81129638414606681695789005144064) & (b + delta >= 12807111440343045/9007199254740992) & (delta >= b**3 - 3) & (b - delta <= 12807111440343045/9007199254740992) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(1762826616152341296409269583897, 81129638414606681695789005144064)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(12807111440343045, 9007199254740992)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(12807111440343045, 9007199254740992)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_140(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 1762826616152341296409269583897/81129638414606681695789005144064) & (b + delta >= 12807111440343045/9007199254740992) & (delta >= b**3 - 3) & (b - delta <= 12807111440343045/9007199254740992) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(1762826616152341296409269583897, 81129638414606681695789005144064)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(12807111440343045, 9007199254740992)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(12807111440343045, 9007199254740992)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_141(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 1762826616152341296409269583897/81129638414606681695789005144064) & (b + delta >= 12807111440343045/9007199254740992) & (delta >= b**3 - 3) & (b - delta <= 12807111440343045/9007199254740992) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(1762826616152341296409269583897, 81129638414606681695789005144064)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(12807111440343045, 9007199254740992)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(12807111440343045, 9007199254740992)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_142(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 1762826616152341296409269583897/81129638414606681695789005144064) & (b + delta >= 12807111440343045/9007199254740992) & (delta >= b**3 - 3) & (b - delta <= 12807111440343045/9007199254740992) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(1762826616152341296409269583897, 81129638414606681695789005144064)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(12807111440343045, 9007199254740992)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(12807111440343045, 9007199254740992)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_143(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 1762826616152341296409269583897/81129638414606681695789005144064) & (b + delta >= 12807111440343045/9007199254740992) & (delta >= b**3 - 3) & (b - delta <= 12807111440343045/9007199254740992) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(1762826616152341296409269583897, 81129638414606681695789005144064)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(12807111440343045, 9007199254740992)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(12807111440343045, 9007199254740992)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_144(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 1762826616152341296409269583897/81129638414606681695789005144064) & (b + delta >= 12807111440343045/9007199254740992) & (delta >= b**3 - 3) & (b - delta <= 12807111440343045/9007199254740992) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(1762826616152341296409269583897, 81129638414606681695789005144064)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(12807111440343045, 9007199254740992)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(12807111440343045, 9007199254740992)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_145(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 1762826616152341296409269583897/81129638414606681695789005144064) & (b + delta >= 12807111440343045/9007199254740992) & (delta >= b**3 - 3) & (b - delta <= 12807111440343045/9007199254740992) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(1762826616152341296409269583897, 81129638414606681695789005144064)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(12807111440343045, 9007199254740992)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(12807111440343045, 9007199254740992)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_146(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 1762826616152341296409269583897/81129638414606681695789005144064) & (b + delta >= 12807111440343045/9007199254740992) & (delta >= b**3 - 3) & (b - delta <= 12807111440343045/9007199254740992) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(1762826616152341296409269583897, 81129638414606681695789005144064)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(12807111440343045, 9007199254740992)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(12807111440343045, 9007199254740992)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_147(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 1762826616152341296409269583897/81129638414606681695789005144064) & (b + delta >= 12807111440343045/9007199254740992) & (delta >= b**3 - 3) & (b - delta <= 12807111440343045/9007199254740992) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(1762826616152341296409269583897, 81129638414606681695789005144064)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(12807111440343045, 9007199254740992)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(12807111440343045, 9007199254740992)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_148(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 1762826616152341296409269583897/81129638414606681695789005144064) & (b + delta >= 12807111440343045/9007199254740992) & (delta >= b**3 - 3) & (b - delta <= 12807111440343045/9007199254740992) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(1762826616152341296409269583897, 81129638414606681695789005144064)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(12807111440343045, 9007199254740992)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(12807111440343045, 9007199254740992)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_149(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 1762826616152341296409269583897/81129638414606681695789005144064) & (b + delta >= 12807111440343045/9007199254740992) & (delta >= b**3 - 3) & (b - delta <= 12807111440343045/9007199254740992) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(1762826616152341296409269583897, 81129638414606681695789005144064)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(12807111440343045, 9007199254740992)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(12807111440343045, 9007199254740992)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_150(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 1762826616152341296409269583897/81129638414606681695789005144064) & (b + delta >= 12807111440343045/9007199254740992) & (delta >= b**3 - 3) & (b - delta <= 12807111440343045/9007199254740992) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(1762826616152341296409269583897, 81129638414606681695789005144064)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(12807111440343045, 9007199254740992)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(12807111440343045, 9007199254740992)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_151(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 1762826616152341296409269583897/81129638414606681695789005144064) & (b + delta >= 12807111440343045/9007199254740992) & (delta >= b**3 - 3) & (b - delta <= 12807111440343045/9007199254740992) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(1762826616152341296409269583897, 81129638414606681695789005144064)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(12807111440343045, 9007199254740992)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(12807111440343045, 9007199254740992)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_152(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 1762826616152341296409269583897/81129638414606681695789005144064) & (b + delta >= 12807111440343045/9007199254740992) & (delta >= b**3 - 3) & (b - delta <= 12807111440343045/9007199254740992) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(1762826616152341296409269583897, 81129638414606681695789005144064)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(12807111440343045, 9007199254740992)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(12807111440343045, 9007199254740992)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_153(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 1762826616152341296409269583897/81129638414606681695789005144064) & (b + delta >= 12807111440343045/9007199254740992) & (delta >= b**3 - 3) & (b - delta <= 12807111440343045/9007199254740992) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(1762826616152341296409269583897, 81129638414606681695789005144064)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(12807111440343045, 9007199254740992)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(12807111440343045, 9007199254740992)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_154(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 1762826616152341296409269583897/81129638414606681695789005144064) & (b + delta >= 12807111440343045/9007199254740992) & (delta >= b**3 - 3) & (b - delta <= 12807111440343045/9007199254740992) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(1762826616152341296409269583897, 81129638414606681695789005144064)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(12807111440343045, 9007199254740992)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(12807111440343045, 9007199254740992)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_155(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 1762826616152341296409269583897/81129638414606681695789005144064) & (b + delta >= 12807111440343045/9007199254740992) & (delta >= b**3 - 3) & (b - delta <= 12807111440343045/9007199254740992) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(1762826616152341296409269583897, 81129638414606681695789005144064)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(12807111440343045, 9007199254740992)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(12807111440343045, 9007199254740992)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_156(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 1762826616152341296409269583897/81129638414606681695789005144064) & (b + delta >= 12807111440343045/9007199254740992) & (delta >= b**3 - 3) & (b - delta <= 12807111440343045/9007199254740992) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(1762826616152341296409269583897, 81129638414606681695789005144064)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(12807111440343045, 9007199254740992)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(12807111440343045, 9007199254740992)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_157(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 1762826616152341296409269583897/81129638414606681695789005144064) & (b + delta >= 12807111440343045/9007199254740992) & (delta >= b**3 - 3) & (b - delta <= 12807111440343045/9007199254740992) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(1762826616152341296409269583897, 81129638414606681695789005144064)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(12807111440343045, 9007199254740992)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(12807111440343045, 9007199254740992)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_158(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 1762826616152341296409269583897/81129638414606681695789005144064) & (b + delta >= 12807111440343045/9007199254740992) & (delta >= b**3 - 3) & (b - delta <= 12807111440343045/9007199254740992) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(1762826616152341296409269583897, 81129638414606681695789005144064)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(12807111440343045, 9007199254740992)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(12807111440343045, 9007199254740992)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_159(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 1762826616152341296409269583897/81129638414606681695789005144064) & (b + delta >= 12807111440343045/9007199254740992) & (delta >= b**3 - 3) & (b - delta <= 12807111440343045/9007199254740992) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(1762826616152341296409269583897, 81129638414606681695789005144064)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(12807111440343045, 9007199254740992)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(12807111440343045, 9007199254740992)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_160(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 1762826616152341296409269583897/81129638414606681695789005144064) & (b + delta >= 12807111440343045/9007199254740992) & (delta >= b**3 - 3) & (b - delta <= 12807111440343045/9007199254740992) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(1762826616152341296409269583897, 81129638414606681695789005144064)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(12807111440343045, 9007199254740992)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(12807111440343045, 9007199254740992)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_161(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 1762826616152341296409269583897/81129638414606681695789005144064) & (b + delta >= 12807111440343045/9007199254740992) & (delta >= b**3 - 3) & (b - delta <= 12807111440343045/9007199254740992) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(1762826616152341296409269583897, 81129638414606681695789005144064)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(12807111440343045, 9007199254740992)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(12807111440343045, 9007199254740992)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_162(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 1762826616152341296409269583897/81129638414606681695789005144064) & (b + delta >= 12807111440343045/9007199254740992) & (delta >= b**3 - 3) & (b - delta <= 12807111440343045/9007199254740992) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(1762826616152341296409269583897, 81129638414606681695789005144064)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(12807111440343045, 9007199254740992)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(12807111440343045, 9007199254740992)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_163(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 1762826616152341296409269583897/81129638414606681695789005144064) & (b + delta >= 12807111440343045/9007199254740992) & (delta >= b**3 - 3) & (b - delta <= 12807111440343045/9007199254740992) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(1762826616152341296409269583897, 81129638414606681695789005144064)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(12807111440343045, 9007199254740992)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(12807111440343045, 9007199254740992)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_164(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 1762826616152341296409269583897/81129638414606681695789005144064) & (b + delta >= 12807111440343045/9007199254740992) & (delta >= b**3 - 3) & (b - delta <= 12807111440343045/9007199254740992) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(1762826616152341296409269583897, 81129638414606681695789005144064)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(12807111440343045, 9007199254740992)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(12807111440343045, 9007199254740992)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_165(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 1762826616152341296409269583897/81129638414606681695789005144064) & (b + delta >= 12807111440343045/9007199254740992) & (delta >= b**3 - 3) & (b - delta <= 12807111440343045/9007199254740992) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(1762826616152341296409269583897, 81129638414606681695789005144064)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(12807111440343045, 9007199254740992)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(12807111440343045, 9007199254740992)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_166(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 1762826616152341296409269583897/81129638414606681695789005144064) & (b + delta >= 12807111440343045/9007199254740992) & (delta >= b**3 - 3) & (b - delta <= 12807111440343045/9007199254740992) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(1762826616152341296409269583897, 81129638414606681695789005144064)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(12807111440343045, 9007199254740992)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(12807111440343045, 9007199254740992)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_167(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 1762826616152341296409269583897/81129638414606681695789005144064) & (b + delta >= 12807111440343045/9007199254740992) & (delta >= b**3 - 3) & (b - delta <= 12807111440343045/9007199254740992) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(1762826616152341296409269583897, 81129638414606681695789005144064)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(12807111440343045, 9007199254740992)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(12807111440343045, 9007199254740992)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_168(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 1762826616152341296409269583897/81129638414606681695789005144064) & (b + delta >= 12807111440343045/9007199254740992) & (delta >= b**3 - 3) & (b - delta <= 12807111440343045/9007199254740992) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(1762826616152341296409269583897, 81129638414606681695789005144064)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(12807111440343045, 9007199254740992)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(12807111440343045, 9007199254740992)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_169(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 1762826616152341296409269583897/81129638414606681695789005144064) & (b + delta >= 12807111440343045/9007199254740992) & (delta >= b**3 - 3) & (b - delta <= 12807111440343045/9007199254740992) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(1762826616152341296409269583897, 81129638414606681695789005144064)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(12807111440343045, 9007199254740992)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(12807111440343045, 9007199254740992)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_170(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 1762826616152341296409269583897/81129638414606681695789005144064) & (b + delta >= 12807111440343045/9007199254740992) & (delta >= b**3 - 3) & (b - delta <= 12807111440343045/9007199254740992) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(1762826616152341296409269583897, 81129638414606681695789005144064)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(12807111440343045, 9007199254740992)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(12807111440343045, 9007199254740992)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_171(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 1762826616152341296409269583897/81129638414606681695789005144064) & (b + delta >= 12807111440343045/9007199254740992) & (delta >= b**3 - 3) & (b - delta <= 12807111440343045/9007199254740992) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(1762826616152341296409269583897, 81129638414606681695789005144064)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(12807111440343045, 9007199254740992)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(12807111440343045, 9007199254740992)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_172(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 1762826616152341296409269583897/81129638414606681695789005144064) & (b + delta >= 12807111440343045/9007199254740992) & (delta >= b**3 - 3) & (b - delta <= 12807111440343045/9007199254740992) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(1762826616152341296409269583897, 81129638414606681695789005144064)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(12807111440343045, 9007199254740992)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(12807111440343045, 9007199254740992)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_173(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 1762826616152341296409269583897/81129638414606681695789005144064) & (b + delta >= 12807111440343045/9007199254740992) & (delta >= b**3 - 3) & (b - delta <= 12807111440343045/9007199254740992) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(1762826616152341296409269583897, 81129638414606681695789005144064)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(12807111440343045, 9007199254740992)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(12807111440343045, 9007199254740992)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_174(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 1762826616152341296409269583897/81129638414606681695789005144064) & (b + delta >= 12807111440343045/9007199254740992) & (delta >= b**3 - 3) & (b - delta <= 12807111440343045/9007199254740992) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(1762826616152341296409269583897, 81129638414606681695789005144064)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(12807111440343045, 9007199254740992)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(12807111440343045, 9007199254740992)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_175(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 1762826616152341296409269583897/81129638414606681695789005144064) & (b + delta >= 12807111440343045/9007199254740992) & (delta >= b**3 - 3) & (b - delta <= 12807111440343045/9007199254740992) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(1762826616152341296409269583897, 81129638414606681695789005144064)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(12807111440343045, 9007199254740992)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(12807111440343045, 9007199254740992)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_176(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 1762826616152341296409269583897/81129638414606681695789005144064) & (b + delta >= 12807111440343045/9007199254740992) & (delta >= b**3 - 3) & (b - delta <= 12807111440343045/9007199254740992) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(1762826616152341296409269583897, 81129638414606681695789005144064)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(12807111440343045, 9007199254740992)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(12807111440343045, 9007199254740992)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_177(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 1762826616152341296409269583897/81129638414606681695789005144064) & (b + delta >= 12807111440343045/9007199254740992) & (delta >= b**3 - 3) & (b - delta <= 12807111440343045/9007199254740992) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(1762826616152341296409269583897, 81129638414606681695789005144064)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(12807111440343045, 9007199254740992)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(12807111440343045, 9007199254740992)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_178(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 1762826616152341296409269583897/81129638414606681695789005144064) & (b + delta >= 12807111440343045/9007199254740992) & (delta >= b**3 - 3) & (b - delta <= 12807111440343045/9007199254740992) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(1762826616152341296409269583897, 81129638414606681695789005144064)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(12807111440343045, 9007199254740992)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(12807111440343045, 9007199254740992)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_179(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 1762826616152341296409269583897/81129638414606681695789005144064) & (b + delta >= 12807111440343045/9007199254740992) & (delta >= b**3 - 3) & (b - delta <= 12807111440343045/9007199254740992) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(1762826616152341296409269583897, 81129638414606681695789005144064)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(12807111440343045, 9007199254740992)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(12807111440343045, 9007199254740992)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_180(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 1762826616152341296409269583897/81129638414606681695789005144064) & (b + delta >= 12807111440343045/9007199254740992) & (delta >= b**3 - 3) & (b - delta <= 12807111440343045/9007199254740992) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(1762826616152341296409269583897, 81129638414606681695789005144064)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(12807111440343045, 9007199254740992)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(12807111440343045, 9007199254740992)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_181(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 1762826616152341296409269583897/81129638414606681695789005144064) & (b + delta >= 12807111440343045/9007199254740992) & (delta >= b**3 - 3) & (b - delta <= 12807111440343045/9007199254740992) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(1762826616152341296409269583897, 81129638414606681695789005144064)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(12807111440343045, 9007199254740992)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(12807111440343045, 9007199254740992)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_182(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 1762826616152341296409269583897/81129638414606681695789005144064) & (b + delta >= 12807111440343045/9007199254740992) & (delta >= b**3 - 3) & (b - delta <= 12807111440343045/9007199254740992) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(1762826616152341296409269583897, 81129638414606681695789005144064)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(12807111440343045, 9007199254740992)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(12807111440343045, 9007199254740992)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_183(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 1721510367157646612127286337/79228162514264337593543950336) & (b + delta >= 400222232510497/281474976710656) & (delta >= b**3 - 3) & (b - delta <= 400222232510497/281474976710656) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(1721510367157646612127286337, 79228162514264337593543950336)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(400222232510497, 281474976710656)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(400222232510497, 281474976710656)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_184(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 28205225855501148688398804067393/1298074214633706907132624082305024) & (b + delta >= 51228445761343521/36028797018963968) & (delta >= b**3 - 3) & (b - delta <= 51228445761343521/36028797018963968) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(28205225855501148688398804067393, 1298074214633706907132624082305024)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(51228445761343521, 36028797018963968)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(51228445761343521, 36028797018963968)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_185(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 1721510367157646612127286337/79228162514264337593543950336) & (b + delta >= 400222232510497/281474976710656) & (delta >= b**3 - 3) & (b - delta <= 400222232510497/281474976710656) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(1721510367157646612127286337, 79228162514264337593543950336)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(400222232510497, 281474976710656)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(400222232510497, 281474976710656)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_186(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 1762826615943226780811414996033/81129638414606681695789005144064) & (b + delta >= 12807111440334881/9007199254740992) & (delta >= b**3 - 3) & (b - delta <= 12807111440334881/9007199254740992) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(1762826615943226780811414996033, 81129638414606681695789005144064)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(12807111440334881, 9007199254740992)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(12807111440334881, 9007199254740992)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_187(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 1762826615968636089909040384001/81129638414606681695789005144064) & (b + delta >= 12807111440335873/9007199254740992) & (delta >= b**3 - 3) & (b - delta <= 12807111440335873/9007199254740992) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(1762826615968636089909040384001, 81129638414606681695789005144064)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(12807111440335873, 9007199254740992)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(12807111440335873, 9007199254740992)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_188(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 110176663499696675661908544521/5070602400912917605986812821504) & (b + delta >= 3201777860084227/2251799813685248) & (delta >= b**3 - 3) & (b - delta <= 3201777860084227/2251799813685248) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(110176663499696675661908544521, 5070602400912917605986812821504)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(3201777860084227, 2251799813685248)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(3201777860084227, 2251799813685248)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_189(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 112820903421995783460924265185809/5192296858534827628530496329220096) & (b + delta >= 102456891522686999/72057594037927936) & (delta >= b**3 - 3) & (b - delta <= 102456891522686999/72057594037927936) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(112820903421995783460924265185809, 5192296858534827628530496329220096)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(102456891522686999, 72057594037927936)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(102456891522686999, 72057594037927936)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_190(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 112820903421995783460924265185809/5192296858534827628530496329220096) & (b + delta >= 102456891522686999/72057594037927936) & (delta >= b**3 - 3) & (b - delta <= 102456891522686999/72057594037927936) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(112820903421995783460924265185809, 5192296858534827628530496329220096)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(102456891522686999, 72057594037927936)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(102456891522686999, 72057594037927936)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_191(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 112820903421995783460924265185809/5192296858534827628530496329220096) & (b + delta >= 102456891522686999/72057594037927936) & (delta >= b**3 - 3) & (b - delta <= 102456891522686999/72057594037927936) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(112820903421995783460924265185809, 5192296858534827628530496329220096)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(102456891522686999, 72057594037927936)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(102456891522686999, 72057594037927936)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_192(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 7051306463771216584535535780929/324518553658426726783156020576256) & (b + delta >= 25614222880669729/18014398509481984) & (delta >= b**3 - 3) & (b - delta <= 25614222880669729/18014398509481984) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(7051306463771216584535535780929, 324518553658426726783156020576256)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(25614222880669729, 18014398509481984)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(25614222880669729, 18014398509481984)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_193(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 1762826615968636089909040384001/81129638414606681695789005144064) & (b + delta >= 12807111440335873/9007199254740992) & (delta >= b**3 - 3) & (b - delta <= 12807111440335873/9007199254740992) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(1762826615968636089909040384001, 81129638414606681695789005144064)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(12807111440335873, 9007199254740992)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(12807111440335873, 9007199254740992)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_194(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 7220537819007820303563692936453921/332306998946228968225951765070086144) & (b + delta >= 819655132181496047/576460752303423488) & (delta >= b**3 - 3) & (b - delta <= 819655132181496047/576460752303423488) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(7220537819007820303563692936453921, 332306998946228968225951765070086144)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(819655132181496047, 576460752303423488)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(819655132181496047, 576460752303423488)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_195(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 112820903421995783460924265185809/5192296858534827628530496329220096) & (b + delta >= 102456891522686999/72057594037927936) & (delta >= b**3 - 3) & (b - delta <= 102456891522686999/72057594037927936) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(112820903421995783460924265185809, 5192296858534827628530496329220096)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(102456891522686999, 72057594037927936)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(102456891522686999, 72057594037927936)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_196(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 1762826615968636089909040384001/81129638414606681695789005144064) & (b + delta >= 12807111440335873/9007199254740992) & (delta >= b**3 - 3) & (b - delta <= 12807111440335873/9007199254740992) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(1762826615968636089909040384001, 81129638414606681695789005144064)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(12807111440335873, 9007199254740992)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(12807111440335873, 9007199254740992)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_197(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 440706653998722667090432493569/20282409603651670423947251286016) & (b + delta >= 6403555720168449/4503599627370496) & (delta >= b**3 - 3) & (b - delta <= 6403555720168449/4503599627370496) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(440706653998722667090432493569, 20282409603651670423947251286016)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(6403555720168449, 4503599627370496)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(6403555720168449, 4503599627370496)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_198(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 28205225855081485260721894720577/1298074214633706907132624082305024) & (b + delta >= 51228445761339425/36028797018963968) & (delta >= b**3 - 3) & (b - delta <= 51228445761339425/36028797018963968) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(28205225855081485260721894720577, 1298074214633706907132624082305024)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(51228445761339425, 36028797018963968)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(51228445761339425, 36028797018963968)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_199(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 26898599486525554695340033/1237940039285380274899124224) & (b + delta >= 50027779063809/35184372088832) & (delta >= b**3 - 3) & (b - delta <= 50027779063809/35184372088832) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(26898599486525554695340033, 1237940039285380274899124224)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(50027779063809, 35184372088832)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(50027779063809, 35184372088832)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_200(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 110176663499683868550468207617/5070602400912917605986812821504) & (b + delta >= 3201777860084225/2251799813685248) & (delta >= b**3 - 3) & (b - delta <= 3201777860084225/2251799813685248) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(110176663499683868550468207617, 5070602400912917605986812821504)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(3201777860084225, 2251799813685248)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(3201777860084225, 2251799813685248)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_201(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 6886041468737846006821963033/316912650057057350374175801344) & (b + delta >= 800444465021061/562949953421312) & (delta >= b**3 - 3) & (b - delta <= 800444465021061/562949953421312) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(6886041468737846006821963033, 316912650057057350374175801344)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(800444465021061, 562949953421312)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(800444465021061, 562949953421312)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_202(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 1762826615994865054138849300481/81129638414606681695789005144064) & (b + delta >= 12807111440336897/9007199254740992) & (delta >= b**3 - 3) & (b - delta <= 12807111440336897/9007199254740992) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(1762826615994865054138849300481, 81129638414606681695789005144064)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(12807111440336897, 9007199254740992)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(12807111440336897, 9007199254740992)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_203(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 1762826615994865054138849300481/81129638414606681695789005144064) & (b + delta >= 12807111440336897/9007199254740992) & (delta >= b**3 - 3) & (b - delta <= 12807111440336897/9007199254740992) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(1762826615994865054138849300481, 81129638414606681695789005144064)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(12807111440336897, 9007199254740992)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(12807111440336897, 9007199254740992)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_204(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 115528605102427133842433024278850513/5316911983139663491615228241121378304) & (b + delta >= 3278620528725725239/2305843009213693952) & (delta >= b**3 - 3) & (b - delta <= 3278620528725725239/2305843009213693952) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(115528605102427133842433024278850513, 5316911983139663491615228241121378304)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(3278620528725725239, 2305843009213693952)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(3278620528725725239, 2305843009213693952)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_205(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 28205225855501148688398804067393/1298074214633706907132624082305024) & (b + delta >= 51228445761343521/36028797018963968) & (delta >= b**3 - 3) & (b - delta <= 51228445761343521/36028797018963968) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(28205225855501148688398804067393, 1298074214633706907132624082305024)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(51228445761343521, 36028797018963968)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(51228445761343521, 36028797018963968)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_206(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 26898599486525554695340033/1237940039285380274899124224) & (b + delta >= 50027779063809/35184372088832) & (delta >= b**3 - 3) & (b - delta <= 50027779063809/35184372088832) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(26898599486525554695340033, 1237940039285380274899124224)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(50027779063809, 35184372088832)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(50027779063809, 35184372088832)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_207(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 28205225855501148688398804067393/1298074214633706907132624082305024) & (b + delta >= 51228445761343521/36028797018963968) & (delta >= b**3 - 3) & (b - delta <= 51228445761343521/36028797018963968) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(28205225855501148688398804067393, 1298074214633706907132624082305024)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(51228445761343521, 36028797018963968)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(51228445761343521, 36028797018963968)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_208(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 26898599486525554695340033/1237940039285380274899124224) & (b + delta >= 50027779063809/35184372088832) & (delta >= b**3 - 3) & (b - delta <= 50027779063809/35184372088832) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(26898599486525554695340033, 1237940039285380274899124224)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(50027779063809, 35184372088832)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(50027779063809, 35184372088832)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_209(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 1762826615942407125679233564673/81129638414606681695789005144064) & (b + delta >= 12807111440334849/9007199254740992) & (delta >= b**3 - 3) & (b - delta <= 12807111440334849/9007199254740992) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(1762826615942407125679233564673, 81129638414606681695789005144064)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(12807111440334849, 9007199254740992)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(12807111440334849, 9007199254740992)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_210(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 1762826615942407125679233564673/81129638414606681695789005144064) & (b + delta >= 12807111440334849/9007199254740992) & (delta >= b**3 - 3) & (b - delta <= 12807111440334849/9007199254740992) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(1762826615942407125679233564673, 81129638414606681695789005144064)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(12807111440334849, 9007199254740992)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(12807111440334849, 9007199254740992)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_211(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 1805134454725424068744907527035953/83076749736557242056487941267521536) & (b + delta >= 409827566090715655/288230376151711744) & (delta >= b**3 - 3) & (b - delta <= 409827566090715655/288230376151711744) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(1805134454725424068744907527035953, 83076749736557242056487941267521536)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(409827566090715655, 288230376151711744)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(409827566090715655, 288230376151711744)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_212(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 1762826615942407125679233564673/81129638414606681695789005144064) & (b + delta >= 12807111440334849/9007199254740992) & (delta >= b**3 - 3) & (b - delta <= 12807111440334849/9007199254740992) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(1762826615942407125679233564673, 81129638414606681695789005144064)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(12807111440334849, 9007199254740992)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(12807111440334849, 9007199254740992)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_213(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 440706653985608184975528558593/20282409603651670423947251286016) & (b + delta >= 6403555720167425/4503599627370496) & (delta >= b**3 - 3) & (b - delta <= 6403555720167425/4503599627370496) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(440706653985608184975528558593, 20282409603651670423947251286016)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(6403555720167425, 4503599627370496)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(6403555720167425, 4503599627370496)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_214(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 1762826615942407125679233564673/81129638414606681695789005144064) & (b + delta >= 12807111440334849/9007199254740992) & (delta >= b**3 - 3) & (b - delta <= 12807111440334849/9007199254740992) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(1762826615942407125679233564673, 81129638414606681695789005144064)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(12807111440334849, 9007199254740992)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(12807111440334849, 9007199254740992)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_215(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 1762826615968636089909040384001/81129638414606681695789005144064) & (b + delta >= 12807111440335873/9007199254740992) & (delta >= b**3 - 3) & (b - delta <= 12807111440335873/9007199254740992) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(1762826615968636089909040384001, 81129638414606681695789005144064)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(12807111440335873, 9007199254740992)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(12807111440335873, 9007199254740992)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_216(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 110176663498044558286105149953/5070602400912917605986812821504) & (b + delta >= 3201777860083969/2251799813685248) & (delta >= b**3 - 3) & (b - delta <= 3201777860083969/2251799813685248) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(110176663498044558286105149953, 5070602400912917605986812821504)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(3201777860083969, 2251799813685248)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(3201777860083969, 2251799813685248)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_217(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 115528605104125105185295914627357617/5316911983139663491615228241121378304) & (b + delta >= 3278620528725984185/2305843009213693952) & (delta >= b**3 - 3) & (b - delta <= 3278620528725984185/2305843009213693952) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(115528605104125105185295914627357617, 5316911983139663491615228241121378304)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(3278620528725984185, 2305843009213693952)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(3278620528725984185, 2305843009213693952)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_218(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 112820903420325736129104533524609/5192296858534827628530496329220096) & (b + delta >= 102456891522678849/72057594037927936) & (delta >= b**3 - 3) & (b - delta <= 102456891522678849/72057594037927936) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(112820903420325736129104533524609, 5192296858534827628530496329220096)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(102456891522678849, 72057594037927936)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(102456891522678849, 72057594037927936)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_219(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 28205225855081485260721894720577/1298074214633706907132624082305024) & (b + delta >= 51228445761339425/36028797018963968) & (delta >= b**3 - 3) & (b - delta <= 51228445761339425/36028797018963968) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(28205225855081485260721894720577, 1298074214633706907132624082305024)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(51228445761339425, 36028797018963968)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(51228445761339425, 36028797018963968)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_220(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 28205225855081485260721894720577/1298074214633706907132624082305024) & (b + delta >= 51228445761339425/36028797018963968) & (delta >= b**3 - 3) & (b - delta <= 51228445761339425/36028797018963968) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(28205225855081485260721894720577, 1298074214633706907132624082305024)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(51228445761339425, 36028797018963968)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(51228445761339425, 36028797018963968)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_221(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 107594397945902107665104897/4951760157141521099596496896) & (b + delta >= 100055558127617/70368744177664) & (delta >= b**3 - 3) & (b - delta <= 100055558127617/70368744177664) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(107594397945902107665104897, 4951760157141521099596496896)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(100055558127617, 70368744177664)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(100055558127617, 70368744177664)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_222(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 7051306463771216584535535780929/324518553658426726783156020576256) & (b + delta >= 25614222880669729/18014398509481984) & (delta >= b**3 - 3) & (b - delta <= 25614222880669729/18014398509481984) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(7051306463771216584535535780929, 324518553658426726783156020576256)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(25614222880669729, 18014398509481984)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(25614222880669729, 18014398509481984)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_223(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 115528605102427133842433024278850513/5316911983139663491615228241121378304) & (b + delta >= 3278620528725725239/2305843009213693952) & (delta >= b**3 - 3) & (b - delta <= 3278620528725725239/2305843009213693952) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(115528605102427133842433024278850513, 5316911983139663491615228241121378304)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(3278620528725725239, 2305843009213693952)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(3278620528725725239, 2305843009213693952)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_224(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 115528605102427133842433024278850513/5316911983139663491615228241121378304) & (b + delta >= 3278620528725725239/2305843009213693952) & (delta >= b**3 - 3) & (b - delta <= 3278620528725725239/2305843009213693952) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(115528605102427133842433024278850513, 5316911983139663491615228241121378304)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(3278620528725725239, 2305843009213693952)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(3278620528725725239, 2305843009213693952)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_225(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 110176663499811939664871577017/5070602400912917605986812821504) & (b + delta >= 3201777860084245/2251799813685248) & (delta >= b**3 - 3) & (b - delta <= 3201777860084245/2251799813685248) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(110176663499811939664871577017, 5070602400912917605986812821504)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(3201777860084245, 2251799813685248)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(3201777860084245, 2251799813685248)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_226(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 440706653999234951548045971089/20282409603651670423947251286016) & (b + delta >= 6403555720168489/4503599627370496) & (delta >= b**3 - 3) & (b - delta <= 6403555720168489/4503599627370496) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(440706653999234951548045971089, 20282409603651670423947251286016)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(6403555720168489, 4503599627370496)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(6403555720168489, 4503599627370496)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_227(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 1681162467976635364671497/77371252455336267181195264) & (b + delta >= 12506944765955/8796093022208) & (delta >= b**3 - 3) & (b - delta <= 12506944765955/8796093022208) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(1681162467976635364671497, 77371252455336267181195264)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(12506944765955, 8796093022208)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(12506944765955, 8796093022208)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_228(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 1762826615968636089909040384001/81129638414606681695789005144064) & (b + delta >= 12807111440335873/9007199254740992) & (delta >= b**3 - 3) & (b - delta <= 12807111440335873/9007199254740992) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(1762826615968636089909040384001, 81129638414606681695789005144064)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(12807111440335873, 9007199254740992)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(12807111440335873, 9007199254740992)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_229(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 6724649871656402563366913/309485009821345068724781056) & (b + delta >= 25013889531905/17592186044416) & (delta >= b**3 - 3) & (b - delta <= 25013889531905/17592186044416) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(6724649871656402563366913, 309485009821345068724781056)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(25013889531905, 17592186044416)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(25013889531905, 17592186044416)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_230(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 6724649871656402563366913/309485009821345068724781056) & (b + delta >= 25013889531905/17592186044416) & (delta >= b**3 - 3) & (b - delta <= 25013889531905/17592186044416) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(6724649871656402563366913, 309485009821345068724781056)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(25013889531905, 17592186044416)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(25013889531905, 17592186044416)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_231(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 7051306463771216584535535780929/324518553658426726783156020576256) & (b + delta >= 25614222880669729/18014398509481984) & (delta >= b**3 - 3) & (b - delta <= 25614222880669729/18014398509481984) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(7051306463771216584535535780929, 324518553658426726783156020576256)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(25614222880669729, 18014398509481984)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(25614222880669729, 18014398509481984)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_232(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 110176663496405248021742223361/5070602400912917605986812821504) & (b + delta >= 3201777860083713/2251799813685248) & (delta >= b**3 - 3) & (b - delta <= 3201777860083713/2251799813685248) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(110176663496405248021742223361, 5070602400912917605986812821504)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(3201777860083713, 2251799813685248)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(3201777860083713, 2251799813685248)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_233(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 110176663496405248021742223361/5070602400912917605986812821504) & (b + delta >= 3201777860083713/2251799813685248) & (delta >= b**3 - 3) & (b - delta <= 3201777860083713/2251799813685248) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(110176663496405248021742223361, 5070602400912917605986812821504)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(3201777860083713, 2251799813685248)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(3201777860083713, 2251799813685248)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_234(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 306329/16777216) & (b + delta >= 5819/4096) & (delta >= b**3 - 3) & (b - delta <= 5819/4096) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(306329, 16777216)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(5819, 4096)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(5819, 4096)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_235(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 28205225855499304464351395700961/1298074214633706907132624082305024) & (b + delta >= 51228445761343503/36028797018963968) & (delta >= b**3 - 3) & (b - delta <= 51228445761343503/36028797018963968) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(28205225855499304464351395700961, 1298074214633706907132624082305024)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(51228445761343503, 36028797018963968)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(51228445761343503, 36028797018963968)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_236(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 112820903420325736129104533524609/5192296858534827628530496329220096) & (b + delta >= 102456891522678849/72057594037927936) & (delta >= b**3 - 3) & (b - delta <= 102456891522678849/72057594037927936) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(112820903420325736129104533524609, 5192296858534827628530496329220096)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(102456891522678849, 72057594037927936)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(102456891522678849, 72057594037927936)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_237(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 1805134454725424068744907527035953/83076749736557242056487941267521536) & (b + delta >= 409827566090715655/288230376151711744) & (delta >= b**3 - 3) & (b - delta <= 409827566090715655/288230376151711744) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(1805134454725424068744907527035953, 83076749736557242056487941267521536)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(409827566090715655, 288230376151711744)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(409827566090715655, 288230376151711744)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_238(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 28205225855499304464351395700961/1298074214633706907132624082305024) & (b + delta >= 51228445761343503/36028797018963968) & (delta >= b**3 - 3) & (b - delta <= 51228445761343503/36028797018963968) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(28205225855499304464351395700961, 1298074214633706907132624082305024)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(51228445761343503, 36028797018963968)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(51228445761343503, 36028797018963968)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_239(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 1805134454725424068744907527035953/83076749736557242056487941267521536) & (b + delta >= 409827566090715655/288230376151711744) & (delta >= b**3 - 3) & (b - delta <= 409827566090715655/288230376151711744) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(1805134454725424068744907527035953, 83076749736557242056487941267521536)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(409827566090715655, 288230376151711744)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(409827566090715655, 288230376151711744)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_240(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 1762826615943226780811414996033/81129638414606681695789005144064) & (b + delta >= 12807111440334881/9007199254740992) & (delta >= b**3 - 3) & (b - delta <= 12807111440334881/9007199254740992) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(1762826615943226780811414996033, 81129638414606681695789005144064)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(12807111440334881, 9007199254740992)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(12807111440334881, 9007199254740992)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_241(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 112820903421995783460924265185809/5192296858534827628530496329220096) & (b + delta >= 102456891522686999/72057594037927936) & (delta >= b**3 - 3) & (b - delta <= 102456891522686999/72057594037927936) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(112820903421995783460924265185809, 5192296858534827628530496329220096)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(102456891522686999, 72057594037927936)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(102456891522686999, 72057594037927936)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_242(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 107594397945902107665104897/4951760157141521099596496896) & (b + delta >= 100055558127617/70368744177664) & (delta >= b**3 - 3) & (b - delta <= 100055558127617/70368744177664) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(107594397945902107665104897, 4951760157141521099596496896)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(100055558127617, 70368744177664)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(100055558127617, 70368744177664)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_243(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 1805134454725424068744907527035953/83076749736557242056487941267521536) & (b + delta >= 409827566090715655/288230376151711744) & (delta >= b**3 - 3) & (b - delta <= 409827566090715655/288230376151711744) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(1805134454725424068744907527035953, 83076749736557242056487941267521536)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(409827566090715655, 288230376151711744)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(409827566090715655, 288230376151711744)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_244(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 7051306463772855894799898644609/324518553658426726783156020576256) & (b + delta >= 25614222880669761/18014398509481984) & (delta >= b**3 - 3) & (b - delta <= 25614222880669761/18014398509481984) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(7051306463772855894799898644609, 324518553658426726783156020576256)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(25614222880669761, 18014398509481984)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(25614222880669761, 18014398509481984)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_245(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 451283613681462367439627422538801/20769187434139310514121985316880384) & (b + delta >= 204913783045358087/144115188075855872) & (delta >= b**3 - 3) & (b - delta <= 204913783045358087/144115188075855872) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(451283613681462367439627422538801, 20769187434139310514121985316880384)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(204913783045358087, 144115188075855872)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(204913783045358087, 144115188075855872)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_246(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 1721510367157646612127286337/79228162514264337593543950336) & (b + delta >= 400222232510497/281474976710656) & (delta >= b**3 - 3) & (b - delta <= 400222232510497/281474976710656) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(1721510367157646612127286337, 79228162514264337593543950336)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(400222232510497, 281474976710656)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(400222232510497, 281474976710656)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_247(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 7051306464609518870974362452137/324518553658426726783156020576256) & (b + delta >= 25614222880686093/18014398509481984) & (delta >= b**3 - 3) & (b - delta <= 25614222880686093/18014398509481984) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(7051306464609518870974362452137, 324518553658426726783156020576256)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(25614222880686093, 18014398509481984)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(25614222880686093, 18014398509481984)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_248(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 7051306463771216584535535780929/324518553658426726783156020576256) & (b + delta >= 25614222880669729/18014398509481984) & (delta >= b**3 - 3) & (b - delta <= 25614222880669729/18014398509481984) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(7051306463771216584535535780929, 324518553658426726783156020576256)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(25614222880669729, 18014398509481984)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(25614222880669729, 18014398509481984)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_249(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 110176663496405248021742223361/5070602400912917605986812821504) & (b + delta >= 3201777860083713/2251799813685248) & (delta >= b**3 - 3) & (b - delta <= 3201777860083713/2251799813685248) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(110176663496405248021742223361, 5070602400912917605986812821504)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(3201777860083713, 2251799813685248)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(3201777860083713, 2251799813685248)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_250(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 28205225855078206640193168998401/1298074214633706907132624082305024) & (b + delta >= 51228445761339393/36028797018963968) & (delta >= b**3 - 3) & (b - delta <= 51228445761339393/36028797018963968) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(28205225855078206640193168998401, 1298074214633706907132624082305024)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(51228445761339393, 36028797018963968)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(51228445761339393, 36028797018963968)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_251(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 1762826615996914191969303210401/81129638414606681695789005144064) & (b + delta >= 12807111440336977/9007199254740992) & (delta >= b**3 - 3) & (b - delta <= 12807111440336977/9007199254740992) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(1762826615996914191969303210401, 81129638414606681695789005144064)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(12807111440336977, 9007199254740992)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(12807111440336977, 9007199254740992)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_252(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 1762826615994865054138849300481/81129638414606681695789005144064) & (b + delta >= 12807111440336897/9007199254740992) & (delta >= b**3 - 3) & (b - delta <= 12807111440336897/9007199254740992) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(1762826615994865054138849300481, 81129638414606681695789005144064)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(12807111440336897, 9007199254740992)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(12807111440336897, 9007199254740992)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_253(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 28205225855081485260721894720577/1298074214633706907132624082305024) & (b + delta >= 51228445761339425/36028797018963968) & (delta >= b**3 - 3) & (b - delta <= 51228445761339425/36028797018963968) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(28205225855081485260721894720577, 1298074214633706907132624082305024)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(51228445761339425, 36028797018963968)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(51228445761339425, 36028797018963968)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_254(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 430377591783208208427909121/19807040628566084398385987584) & (b + delta >= 200111116255233/140737488355328) & (delta >= b**3 - 3) & (b - delta <= 200111116255233/140737488355328) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(430377591783208208427909121, 19807040628566084398385987584)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(200111116255233, 140737488355328)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(200111116255233, 140737488355328)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_255(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 28205225855078206640193168998401/1298074214633706907132624082305024) & (b + delta >= 51228445761339393/36028797018963968) & (delta >= b**3 - 3) & (b - delta <= 51228445761339393/36028797018963968) & (delta >= 3 - b**3)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(28205225855078206640193168998401, 1298074214633706907132624082305024)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(51228445761339393, 36028797018963968)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(3)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(51228445761339393, 36028797018963968)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def post_condition(b:sympy.Rational, delta:sympy.Rational, a:sympy.Rational):
	# (0 <= delta) & (-a + b <= delta) & (a - b <= delta) & (a**2 - 2 <= delta) & (b**3 - 3 <= delta) & (2 - a**2 <= delta) & (3 - b**3 <= delta)

	post_cond =  And(LessThan(Integer(0), Symbol('delta')), LessThan(Add(Mul(Integer(-1), Symbol('a')), Symbol('b')), Symbol('delta')), LessThan(Add(Symbol('a'), Mul(Integer(-1), Symbol('b'))), Symbol('delta')), LessThan(Add(Pow(Symbol('a'), Integer(2)), Integer(-2)), Symbol('delta')), LessThan(Add(Pow(Symbol('b'), Integer(3)), Integer(-3)), Symbol('delta')), LessThan(Add(Integer(2), Mul(Integer(-1), Pow(Symbol('a'), Integer(2)))), Symbol('delta')), LessThan(Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(3)))), Symbol('delta')))

	eval = post_cond.subs( { 'b':b, 'delta':delta, 'a':a })

	return eval == sympy.logic.boolalg.BooleanTrue





if __name__=="__main__":
	
	ip_0=int(input("enter integer numerator of b:\n"))
	ip_1=int(input("enter integer denominator of b:\n"))
	assert(ip_1!=0), ("Error denominator entered is 0")
	b=sympy.Rational(ip_0,ip_1)
	
	
	ip_0=int(input("enter integer numerator of delta:\n"))
	ip_1=int(input("enter integer denominator of delta:\n"))
	assert(ip_1!=0), ("Error denominator entered is 0")
	delta=sympy.Rational(ip_0,ip_1)
	
	
	
	
	if pre_condition_0(b=b,delta=delta)==True:
		print("pre_condition_0 SAT")
		print('delta = 4')
		print('b = 1/8')
		print('a = 1/2')
		exit(0)
	
	
	if pre_condition_1(b=b,delta=delta)==True:
		print("pre_condition_1 SAT")
		print('delta = 1')
		print('b = 3/2')
		print('a = 1')
		exit(0)
	
	
	if pre_condition_2(b=b,delta=delta)==True:
		print("pre_condition_2 SAT")
		print('delta = 7/16')
		print('b = 3/2')
		print('a = 3/2')
		exit(0)
	
	
	if pre_condition_3(b=b,delta=delta)==True:
		print("pre_condition_3 SAT")
		print('delta = 1/8')
		print('b = 23/16')
		print('a = 11/8')
		exit(0)
	
	
	if pre_condition_4(b=b,delta=delta)==True:
		print("pre_condition_4 SAT")
		print('delta = 3/32')
		print('b = 23/16')
		print('a = 23/16')
		exit(0)
	
	
	if pre_condition_5(b=b,delta=delta)==True:
		print("pre_condition_5 SAT")
		print('delta = 1/16')
		print('b = 23/16')
		print('a = 45/32')
		exit(0)
	
	
	if pre_condition_6(b=b,delta=delta)==True:
		print("pre_condition_6 SAT")
		print('delta = 45/2048')
		print('b = 369/256')
		print('a = 91/64')
		exit(0)
	
	
	if pre_condition_7(b=b,delta=delta)==True:
		print("pre_condition_7 SAT")
		print('delta = 177/8192')
		print('b = 369/256')
		print('a = 727/512')
		exit(0)
	
	
	if pre_condition_8(b=b,delta=delta)==True:
		print("pre_condition_8 SAT")
		print('delta = 95/4096')
		print('b = 185/128')
		print('a = 2913/2048')
		exit(0)
	
	
	if pre_condition_9(b=b,delta=delta)==True:
		print("pre_condition_9 SAT")
		print('delta = 757/32768')
		print('b = 185/128')
		print('a = 11651/8192')
		exit(0)
	
	
	if pre_condition_10(b=b,delta=delta)==True:
		print("pre_condition_10 SAT")
		print('delta = 735/32768')
		print('b = 1479/1024')
		print('a = 5825/4096')
		exit(0)
	
	
	if pre_condition_11(b=b,delta=delta)==True:
		print("pre_condition_11 SAT")
		print('delta = 367/16384')
		print('b = 1479/1024')
		print('a = 11649/8192')
		exit(0)
	
	
	if pre_condition_12(b=b,delta=delta)==True:
		print("pre_condition_12 SAT")
		print('delta = 719/32768')
		print('b = 2957/2048')
		print('a = 23297/16384')
		exit(0)
	
	
	if pre_condition_13(b=b,delta=delta)==True:
		print("pre_condition_13 SAT")
		print('delta = 1431/65536')
		print('b = 11827/8192')
		print('a = 46593/32768')
		exit(0)
	
	
	if pre_condition_14(b=b,delta=delta)==True:
		print("pre_condition_14 SAT")
		print('delta = 2855/131072')
		print('b = 23653/16384')
		print('a = 93185/65536')
		exit(0)
	
	
	if pre_condition_15(b=b,delta=delta)==True:
		print("pre_condition_15 SAT")
		print('delta = 5703/262144')
		print('b = 47305/32768')
		print('a = 186369/131072')
		exit(0)
	
	
	if pre_condition_16(b=b,delta=delta)==True:
		print("pre_condition_16 SAT")
		print('delta = 11399/524288')
		print('b = 94609/65536')
		print('a = 372737/262144')
		exit(0)
	
	
	if pre_condition_17(b=b,delta=delta)==True:
		print("pre_condition_17 SAT")
		print('delta = 22791/1048576')
		print('b = 189217/131072')
		print('a = 745473/524288')
		exit(0)
	
	
	if pre_condition_18(b=b,delta=delta)==True:
		print("pre_condition_18 SAT")
		print('delta = 45575/2097152')
		print('b = 378433/262144')
		print('a = 1490945/1048576')
		exit(0)
	
	
	if pre_condition_19(b=b,delta=delta)==True:
		print("pre_condition_19 SAT")
		print('delta = 91143/4194304')
		print('b = 756865/524288')
		print('a = 2981889/2097152')
		exit(0)
	
	
	if pre_condition_20(b=b,delta=delta)==True:
		print("pre_condition_20 SAT")
		print('delta = 182279/8388608')
		print('b = 1513729/1048576')
		print('a = 5963777/4194304')
		exit(0)
	
	
	if pre_condition_21(b=b,delta=delta)==True:
		print("pre_condition_21 SAT")
		print('delta = 364551/16777216')
		print('b = 3027457/2097152')
		print('a = 11927553/8388608')
		exit(0)
	
	
	if pre_condition_22(b=b,delta=delta)==True:
		print("pre_condition_22 SAT")
		print('delta = 729095/33554432')
		print('b = 6054913/4194304')
		print('a = 23855105/16777216')
		exit(0)
	
	
	if pre_condition_23(b=b,delta=delta)==True:
		print("pre_condition_23 SAT")
		print('delta = 1458183/67108864')
		print('b = 12109825/8388608')
		print('a = 47710209/33554432')
		exit(0)
	
	
	if pre_condition_24(b=b,delta=delta)==True:
		print("pre_condition_24 SAT")
		print('delta = 2916359/134217728')
		print('b = 24219649/16777216')
		print('a = 95420417/67108864')
		exit(0)
	
	
	if pre_condition_25(b=b,delta=delta)==True:
		print("pre_condition_25 SAT")
		print('delta = 5832711/268435456')
		print('b = 48439297/33554432')
		print('a = 190840833/134217728')
		exit(0)
	
	
	if pre_condition_26(b=b,delta=delta)==True:
		print("pre_condition_26 SAT")
		print('delta = 11665415/536870912')
		print('b = 96878593/67108864')
		print('a = 381681665/268435456')
		exit(0)
	
	
	if pre_condition_27(b=b,delta=delta)==True:
		print("pre_condition_27 SAT")
		print('delta = 23330823/1073741824')
		print('b = 193757185/134217728')
		print('a = 763363329/536870912')
		exit(0)
	
	
	if pre_condition_28(b=b,delta=delta)==True:
		print("pre_condition_28 SAT")
		print('delta = 46661639/2147483648')
		print('b = 387514369/268435456')
		print('a = 1526726657/1073741824')
		exit(0)
	
	
	if pre_condition_29(b=b,delta=delta)==True:
		print("pre_condition_29 SAT")
		print('delta = 93323271/4294967296')
		print('b = 775028737/536870912')
		print('a = 3053453313/2147483648')
		exit(0)
	
	
	if pre_condition_30(b=b,delta=delta)==True:
		print("pre_condition_30 SAT")
		print('delta = 186646535/8589934592')
		print('b = 1550057473/1073741824')
		print('a = 6106906625/4294967296')
		exit(0)
	
	
	if pre_condition_31(b=b,delta=delta)==True:
		print("pre_condition_31 SAT")
		print('delta = 373293063/17179869184')
		print('b = 3100114945/2147483648')
		print('a = 12213813249/8589934592')
		exit(0)
	
	
	if pre_condition_32(b=b,delta=delta)==True:
		print("pre_condition_32 SAT")
		print('delta = 746586119/34359738368')
		print('b = 6200229889/4294967296')
		print('a = 24427626497/17179869184')
		exit(0)
	
	
	if pre_condition_33(b=b,delta=delta)==True:
		print("pre_condition_33 SAT")
		print('delta = 1493172231/68719476736')
		print('b = 12400459777/8589934592')
		print('a = 48855252993/34359738368')
		exit(0)
	
	
	if pre_condition_34(b=b,delta=delta)==True:
		print("pre_condition_34 SAT")
		print('delta = 2986344455/137438953472')
		print('b = 24800919553/17179869184')
		print('a = 97710505985/68719476736')
		exit(0)
	
	
	if pre_condition_35(b=b,delta=delta)==True:
		print("pre_condition_35 SAT")
		print('delta = 5972688903/274877906944')
		print('b = 49601839105/34359738368')
		print('a = 195421011969/137438953472')
		exit(0)
	
	
	if pre_condition_36(b=b,delta=delta)==True:
		print("pre_condition_36 SAT")
		print('delta = 11945377799/549755813888')
		print('b = 99203678209/68719476736')
		print('a = 390842023937/274877906944')
		exit(0)
	
	
	if pre_condition_37(b=b,delta=delta)==True:
		print("pre_condition_37 SAT")
		print('delta = 23890755591/1099511627776')
		print('b = 198407356417/137438953472')
		print('a = 781684047873/549755813888')
		exit(0)
	
	
	if pre_condition_38(b=b,delta=delta)==True:
		print("pre_condition_38 SAT")
		print('delta = 47781511175/2199023255552')
		print('b = 396814712833/274877906944')
		print('a = 1563368095745/1099511627776')
		exit(0)
	
	
	if pre_condition_39(b=b,delta=delta)==True:
		print("pre_condition_39 SAT")
		print('delta = 95563022343/4398046511104')
		print('b = 793629425665/549755813888')
		print('a = 3126736191489/2199023255552')
		exit(0)
	
	
	if pre_condition_40(b=b,delta=delta)==True:
		print("pre_condition_40 SAT")
		print('delta = 191126044679/8796093022208')
		print('b = 1587258851329/1099511627776')
		print('a = 6253472382977/4398046511104')
		exit(0)
	
	
	if pre_condition_41(b=b,delta=delta)==True:
		print("pre_condition_41 SAT")
		print('delta = 382252089351/17592186044416')
		print('b = 3174517702657/2199023255552')
		print('a = 12506944765953/8796093022208')
		exit(0)
	
	
	if pre_condition_42(b=b,delta=delta)==True:
		print("pre_condition_42 SAT")
		print('delta = 764504178695/35184372088832')
		print('b = 6349035405313/4398046511104')
		print('a = 25013889531905/17592186044416')
		exit(0)
	
	
	if pre_condition_43(b=b,delta=delta)==True:
		print("pre_condition_43 SAT")
		print('delta = 1529008357383/70368744177664')
		print('b = 12698070810625/8796093022208')
		print('a = 50027779063809/35184372088832')
		exit(0)
	
	
	if pre_condition_44(b=b,delta=delta)==True:
		print("pre_condition_44 SAT")
		print('delta = 3058016714759/140737488355328')
		print('b = 25396141621249/17592186044416')
		print('a = 100055558127617/70368744177664')
		exit(0)
	
	
	if pre_condition_45(b=b,delta=delta)==True:
		print("pre_condition_45 SAT")
		print('delta = 6116033429511/281474976710656')
		print('b = 50792283242497/35184372088832')
		print('a = 200111116255233/140737488355328')
		exit(0)
	
	
	if pre_condition_46(b=b,delta=delta)==True:
		print("pre_condition_46 SAT")
		print('delta = 12232066859015/562949953421312')
		print('b = 101584566484993/70368744177664')
		print('a = 400222232510465/281474976710656')
		exit(0)
	
	
	if pre_condition_47(b=b,delta=delta)==True:
		print("pre_condition_47 SAT")
		print('delta = 24464133718023/1125899906842624')
		print('b = 203169132969985/140737488355328')
		print('a = 800444465020929/562949953421312')
		exit(0)
	
	
	if pre_condition_48(b=b,delta=delta)==True:
		print("pre_condition_48 SAT")
		print('delta = 48928267436039/2251799813685248')
		print('b = 406338265939969/281474976710656')
		print('a = 1600888930041857/1125899906842624')
		exit(0)
	
	
	if pre_condition_49(b=b,delta=delta)==True:
		print("pre_condition_49 SAT")
		print('delta = 97856534872071/4503599627370496')
		print('b = 812676531879937/562949953421312')
		print('a = 3201777860083713/2251799813685248')
		exit(0)
	
	
	if pre_condition_50(b=b,delta=delta)==True:
		print("pre_condition_50 SAT")
		print('delta = 195713069744135/9007199254740992')
		print('b = 1625353063759873/1125899906842624')
		print('a = 6403555720167425/4503599627370496')
		exit(0)
	
	
	if pre_condition_51(b=b,delta=delta)==True:
		print("pre_condition_51 SAT")
		print('delta = 391426139488263/18014398509481984')
		print('b = 3250706127519745/2251799813685248')
		print('a = 12807111440334849/9007199254740992')
		exit(0)
	
	
	if pre_condition_52(b=b,delta=delta)==True:
		print("pre_condition_52 SAT")
		print('delta = 391426139488263/18014398509481984')
		print('b = 3250706127519745/2251799813685248')
		print('a = 12807111440334849/9007199254740992')
		exit(0)
	
	
	if pre_condition_53(b=b,delta=delta)==True:
		print("pre_condition_53 SAT")
		print('delta = 391426139488263/18014398509481984')
		print('b = 3250706127519745/2251799813685248')
		print('a = 12807111440334849/9007199254740992')
		exit(0)
	
	
	if pre_condition_54(b=b,delta=delta)==True:
		print("pre_condition_54 SAT")
		print('delta = 382252089535/17592186044416')
		print('b = 99203678209/68719476736')
		print('a = 12506944765985/8796093022208')
		exit(0)
	
	
	if pre_condition_55(b=b,delta=delta)==True:
		print("pre_condition_55 SAT")
		print('delta = 782852278976703/36028797018963968')
		print('b = 203169132969985/140737488355328')
		print('a = 25614222880669729/18014398509481984')
		exit(0)
	
	
	if pre_condition_56(b=b,delta=delta)==True:
		print("pre_condition_56 SAT")
		print('delta = 1529008358111/70368744177664')
		print('b = 3174517702687/2199023255552')
		print('a = 50027779063937/35184372088832')
		exit(0)
	
	
	if pre_condition_57(b=b,delta=delta)==True:
		print("pre_condition_57 SAT")
		print('delta = 782852278976519/36028797018963968')
		print('b = 6501412255039489/4503599627370496')
		print('a = 25614222880669697/18014398509481984')
		exit(0)
	
	
	if pre_condition_58(b=b,delta=delta)==True:
		print("pre_condition_58 SAT")
		print('delta = 3058016716215/140737488355328')
		print('b = 25396141621495/17592186044416')
		print('a = 100055558127873/70368744177664')
		exit(0)
	
	
	if pre_condition_59(b=b,delta=delta)==True:
		print("pre_condition_59 SAT")
		print('delta = 6262818231813593/288230376151711744')
		print('b = 13002824510079039/9007199254740992')
		print('a = 51228445761339457/36028797018963968')
		exit(0)
	
	
	if pre_condition_60(b=b,delta=delta)==True:
		print("pre_condition_60 SAT")
		print('delta = 6116033432423/281474976710656')
		print('b = 50792283242989/35184372088832')
		print('a = 200111116255745/140737488355328')
		exit(0)
	
	
	if pre_condition_61(b=b,delta=delta)==True:
		print("pre_condition_61 SAT")
		print('delta = 12232066864839/562949953421312')
		print('b = 101584566485977/70368744177664')
		print('a = 400222232511489/281474976710656')
		exit(0)
	
	
	if pre_condition_62(b=b,delta=delta)==True:
		print("pre_condition_62 SAT")
		print('delta = 1529008357567/70368744177664')
		print('b = 396814712833/274877906944')
		print('a = 50027779063841/35184372088832')
		exit(0)
	
	
	if pre_condition_63(b=b,delta=delta)==True:
		print("pre_condition_63 SAT")
		print('delta = 6116033430239/281474976710656')
		print('b = 12698070810655/8796093022208')
		print('a = 200111116255361/140737488355328')
		exit(0)
	
	
	if pre_condition_64(b=b,delta=delta)==True:
		print("pre_condition_64 SAT")
		print('delta = 12232066860471/562949953421312')
		print('b = 101584566485239/70368744177664')
		print('a = 400222232510721/281474976710656')
		exit(0)
	
	
	if pre_condition_65(b=b,delta=delta)==True:
		print("pre_condition_65 SAT")
		print('delta = 391426139488447/18014398509481984')
		print('b = 101584566484993/70368744177664')
		print('a = 12807111440334881/9007199254740992')
		exit(0)
	
	
	if pre_condition_66(b=b,delta=delta)==True:
		print("pre_condition_66 SAT")
		print('delta = 24464133720935/1125899906842624')
		print('b = 203169132970477/140737488355328')
		print('a = 800444465021441/562949953421312')
		exit(0)
	
	
	if pre_condition_67(b=b,delta=delta)==True:
		print("pre_condition_67 SAT")
		print('delta = 48928267441863/2251799813685248')
		print('b = 406338265940953/281474976710656')
		print('a = 1600888930042881/1125899906842624')
		exit(0)
	
	
	if pre_condition_68(b=b,delta=delta)==True:
		print("pre_condition_68 SAT")
		print('delta = 97856534883719/4503599627370496')
		print('b = 812676531881905/562949953421312')
		print('a = 3201777860085761/2251799813685248')
		exit(0)
	
	
	if pre_condition_69(b=b,delta=delta)==True:
		print("pre_condition_69 SAT")
		print('delta = 195713069767431/9007199254740992')
		print('b = 1625353063763809/1125899906842624')
		print('a = 6403555720171521/4503599627370496')
		exit(0)
	
	
	if pre_condition_70(b=b,delta=delta)==True:
		print("pre_condition_70 SAT")
		print('delta = 391426139534855/18014398509481984')
		print('b = 3250706127527617/2251799813685248')
		print('a = 12807111440343041/9007199254740992')
		exit(0)
	
	
	if pre_condition_71(b=b,delta=delta)==True:
		print("pre_condition_71 SAT")
		print('delta = 391426139534855/18014398509481984')
		print('b = 3250706127527617/2251799813685248')
		print('a = 12807111440343041/9007199254740992')
		exit(0)
	
	
	if pre_condition_72(b=b,delta=delta)==True:
		print("pre_condition_72 SAT")
		print('delta = 391426139534855/18014398509481984')
		print('b = 3250706127527617/2251799813685248')
		print('a = 12807111440343041/9007199254740992')
		exit(0)
	
	
	if pre_condition_73(b=b,delta=delta)==True:
		print("pre_condition_73 SAT")
		print('delta = 391426139534855/18014398509481984')
		print('b = 3250706127527617/2251799813685248')
		print('a = 12807111440343041/9007199254740992')
		exit(0)
	
	
	if pre_condition_74(b=b,delta=delta)==True:
		print("pre_condition_74 SAT")
		print('delta = 1565704558139773/72057594037927936')
		print('b = 203169132970477/140737488355328')
		print('a = 25614222880686113/18014398509481984')
		exit(0)
	
	
	if pre_condition_75(b=b,delta=delta)==True:
		print("pre_condition_75 SAT")
		print('delta = 1565704558139773/72057594037927936')
		print('b = 203169132970477/140737488355328')
		print('a = 25614222880686113/18014398509481984')
		exit(0)
	
	
	if pre_condition_76(b=b,delta=delta)==True:
		print("pre_condition_76 SAT")
		print('delta = 1565704558139773/72057594037927936')
		print('b = 203169132970477/140737488355328')
		print('a = 25614222880686113/18014398509481984')
		exit(0)
	
	
	if pre_condition_77(b=b,delta=delta)==True:
		print("pre_condition_77 SAT")
		print('delta = 97856534918847/4503599627370496')
		print('b = 25396141621495/17592186044416')
		print('a = 3201777860091937/2251799813685248')
		exit(0)
	
	
	if pre_condition_78(b=b,delta=delta)==True:
		print("pre_condition_78 SAT")
		print('delta = 1565704558139441/72057594037927936')
		print('b = 1625353063763809/1125899906842624')
		print('a = 6403555720171521/4503599627370496')
		exit(0)
	
	
	if pre_condition_79(b=b,delta=delta)==True:
		print("pre_condition_79 SAT")
		print('delta = 391426139675359/18014398509481984')
		print('b = 812676531887839/562949953421312')
		print('a = 12807111440367745/9007199254740992')
		exit(0)
	
	
	if pre_condition_80(b=b,delta=delta)==True:
		print("pre_condition_80 SAT")
		print('delta = 782852278982657/36028797018963968')
		print('b = 6349035405313/4398046511104')
		print('a = 25013889531905/17592186044416')
		exit(0)
	
	
	if pre_condition_81(b=b,delta=delta)==True:
		print("pre_condition_81 SAT")
		print('delta = 391426139675359/18014398509481984')
		print('b = 812676531887839/562949953421312')
		print('a = 12807111440367745/9007199254740992')
		exit(0)
	
	
	if pre_condition_82(b=b,delta=delta)==True:
		print("pre_condition_82 SAT")
		print('delta = 391426139675359/18014398509481984')
		print('b = 812676531887839/562949953421312')
		print('a = 12807111440367745/9007199254740992')
		exit(0)
	
	
	if pre_condition_83(b=b,delta=delta)==True:
		print("pre_condition_83 SAT")
		print('delta = 782852279350769/36028797018963968')
		print('b = 25396141621495/17592186044416')
		print('a = 3201777860091937/2251799813685248')
		exit(0)
	
	
	if pre_condition_84(b=b,delta=delta)==True:
		print("pre_condition_84 SAT")
		print('delta = 782852278982657/36028797018963968')
		print('b = 6349035405313/4398046511104')
		print('a = 25013889531905/17592186044416')
		exit(0)
	
	
	if pre_condition_85(b=b,delta=delta)==True:
		print("pre_condition_85 SAT")
		print('delta = 782852279350769/36028797018963968')
		print('b = 25396141621495/17592186044416')
		print('a = 3201777860091937/2251799813685248')
		exit(0)
	
	
	if pre_condition_86(b=b,delta=delta)==True:
		print("pre_condition_86 SAT")
		print('delta = 50102545854508585/2305843009213693952')
		print('b = 104022596080632307/72057594037927936')
		print('a = 409827566090715655/288230376151711744')
		exit(0)
	
	
	if pre_condition_87(b=b,delta=delta)==True:
		print("pre_condition_87 SAT")
		print('delta = 782852279350769/36028797018963968')
		print('b = 25396141621495/17592186044416')
		print('a = 3201777860091937/2251799813685248')
		exit(0)
	
	
	if pre_condition_88(b=b,delta=delta)==True:
		print("pre_condition_88 SAT")
		print('delta = 782852279350711/36028797018963968')
		print('b = 6501412255102711/4503599627370496')
		print('a = 25614222880735489/18014398509481984')
		exit(0)
	
	
	if pre_condition_89(b=b,delta=delta)==True:
		print("pre_condition_89 SAT")
		print('delta = 391426139534855/18014398509481984')
		print('b = 3250706127527617/2251799813685248')
		print('a = 12807111440343041/9007199254740992')
		exit(0)
	
	
	if pre_condition_90(b=b,delta=delta)==True:
		print("pre_condition_90 SAT")
		print('delta = 782852279350711/36028797018963968')
		print('b = 6501412255102711/4503599627370496')
		print('a = 25614222880735489/18014398509481984')
		exit(0)
	
	
	if pre_condition_91(b=b,delta=delta)==True:
		print("pre_condition_91 SAT")
		print('delta = 23331007/1073741824')
		print('b = 6054913/4194304')
		print('a = 763363361/536870912')
		exit(0)
	
	
	if pre_condition_92(b=b,delta=delta)==True:
		print("pre_condition_92 SAT")
		print('delta = 93323999/4294967296')
		print('b = 193757215/134217728')
		print('a = 3053453441/2147483648')
		exit(0)
	
	
	if pre_condition_93(b=b,delta=delta)==True:
		print("pre_condition_93 SAT")
		print('delta = 1529008358135/70368744177664')
		print('b = 99203678209/68719476736')
		print('a = 50027779063941/35184372088832')
		exit(0)
	
	
	if pre_condition_94(b=b,delta=delta)==True:
		print("pre_condition_94 SAT")
		print('delta = 12232066865023/562949953421312')
		print('b = 12698070810751/8796093022208')
		print('a = 400222232511521/281474976710656')
		exit(0)
	
	
	if pre_condition_95(b=b,delta=delta)==True:
		print("pre_condition_95 SAT")
		print('delta = 48928267460063/2251799813685248')
		print('b = 101584566486007/70368744177664')
		print('a = 1600888930046081/1125899906842624')
		exit(0)
	
	
	if pre_condition_96(b=b,delta=delta)==True:
		print("pre_condition_96 SAT")
		print('delta = 12232066859199/562949953421312')
		print('b = 3174517702657/2199023255552')
		print('a = 400222232510497/281474976710656')
		exit(0)
	
	
	if pre_condition_97(b=b,delta=delta)==True:
		print("pre_condition_97 SAT")
		print('delta = 48928267436767/2251799813685248')
		print('b = 101584566485023/70368744177664')
		print('a = 1600888930041985/1125899906842624')
		exit(0)
	
	
	if pre_condition_98(b=b,delta=delta)==True:
		print("pre_condition_98 SAT")
		print('delta = 97856534873527/4503599627370496')
		print('b = 812676531880183/562949953421312')
		print('a = 3201777860083969/2251799813685248')
		exit(0)
	
	
	if pre_condition_99(b=b,delta=delta)==True:
		print("pre_condition_99 SAT")
		print('delta = 195713069747047/9007199254740992')
		print('b = 1625353063760365/1125899906842624')
		print('a = 6403555720167937/4503599627370496')
		exit(0)
	
	
	if pre_condition_100(b=b,delta=delta)==True:
		print("pre_condition_100 SAT")
		print('delta = 1565704557953073/72057594037927936')
		print('b = 1625353063759873/1125899906842624')
		print('a = 6403555720167425/4503599627370496')
		exit(0)
	
	
	if pre_condition_101(b=b,delta=delta)==True:
		print("pre_condition_101 SAT")
		print('delta = 391426139494087/18014398509481984')
		print('b = 3250706127520729/2251799813685248')
		print('a = 12807111440335873/9007199254740992')
		exit(0)
	
	
	if pre_condition_102(b=b,delta=delta)==True:
		print("pre_condition_102 SAT")
		print('delta = 391426139494087/18014398509481984')
		print('b = 3250706127520729/2251799813685248')
		print('a = 12807111440335873/9007199254740992')
		exit(0)
	
	
	if pre_condition_103(b=b,delta=delta)==True:
		print("pre_condition_103 SAT")
		print('delta = 50102545854508585/2305843009213693952')
		print('b = 104022596080632307/72057594037927936')
		print('a = 409827566090715655/288230376151711744')
		exit(0)
	
	
	if pre_condition_104(b=b,delta=delta)==True:
		print("pre_condition_104 SAT")
		print('delta = 391426139488263/18014398509481984')
		print('b = 3250706127519745/2251799813685248')
		print('a = 12807111440334849/9007199254740992')
		exit(0)
	
	
	if pre_condition_105(b=b,delta=delta)==True:
		print("pre_condition_105 SAT")
		print('delta = 1565704557976393/72057594037927936')
		print('b = 3250706127520731/2251799813685248')
		print('a = 12807111440335875/9007199254740992')
		exit(0)
	
	
	if pre_condition_106(b=b,delta=delta)==True:
		print("pre_condition_106 SAT")
		print('delta = 12525636463811281/576460752303423488')
		print('b = 13002824510082927/9007199254740992')
		print('a = 51228445761343503/36028797018963968')
		exit(0)
	
	
	if pre_condition_107(b=b,delta=delta)==True:
		print("pre_condition_107 SAT")
		print('delta = 12525636463812081/576460752303423488')
		print('b = 101584566485023/70368744177664')
		print('a = 51228445761343521/36028797018963968')
		exit(0)
	
	
	if pre_condition_108(b=b,delta=delta)==True:
		print("pre_condition_108 SAT")
		print('delta = 12525636463812081/576460752303423488')
		print('b = 101584566485023/70368744177664')
		print('a = 51228445761343521/36028797018963968')
		exit(0)
	
	
	if pre_condition_109(b=b,delta=delta)==True:
		print("pre_condition_109 SAT")
		print('delta = 12525636463812081/576460752303423488')
		print('b = 101584566485023/70368744177664')
		print('a = 51228445761343521/36028797018963968')
		exit(0)
	
	
	if pre_condition_110(b=b,delta=delta)==True:
		print("pre_condition_110 SAT")
		print('delta = 195713069767443/9007199254740992')
		print('b = 1625353063763811/1125899906842624')
		print('a = 6403555720171523/4503599627370496')
		exit(0)
	
	
	if pre_condition_111(b=b,delta=delta)==True:
		print("pre_condition_111 SAT")
		print('delta = 782852279069757/36028797018963968')
		print('b = 3250706127527621/2251799813685248')
		print('a = 12807111440343045/9007199254740992')
		exit(0)
	
	
	if pre_condition_112(b=b,delta=delta)==True:
		print("pre_condition_112 SAT")
		print('delta = 782852279069757/36028797018963968')
		print('b = 3250706127527621/2251799813685248')
		print('a = 12807111440343045/9007199254740992')
		exit(0)
	
	
	if pre_condition_113(b=b,delta=delta)==True:
		print("pre_condition_113 SAT")
		print('delta = 782852279069757/36028797018963968')
		print('b = 3250706127527621/2251799813685248')
		print('a = 12807111440343045/9007199254740992')
		exit(0)
	
	
	if pre_condition_114(b=b,delta=delta)==True:
		print("pre_condition_114 SAT")
		print('delta = 391426139534855/18014398509481984')
		print('b = 3250706127527617/2251799813685248')
		print('a = 12807111440343041/9007199254740992')
		exit(0)
	
	
	if pre_condition_115(b=b,delta=delta)==True:
		print("pre_condition_115 SAT")
		print('delta = 391426139534891/18014398509481984')
		print('b = 3250706127527623/2251799813685248')
		print('a = 12807111440343047/9007199254740992')
		exit(0)
	
	
	if pre_condition_116(b=b,delta=delta)==True:
		print("pre_condition_116 SAT")
		print('delta = 24464133729671/1125899906842624')
		print('b = 203169132971953/140737488355328')
		print('a = 800444465022977/562949953421312')
		exit(0)
	
	
	if pre_condition_117(b=b,delta=delta)==True:
		print("pre_condition_117 SAT")
		print('delta = 48928267459335/2251799813685248')
		print('b = 406338265943905/281474976710656')
		print('a = 1600888930045953/1125899906842624')
		exit(0)
	
	
	if pre_condition_118(b=b,delta=delta)==True:
		print("pre_condition_118 SAT")
		print('delta = 391426139534855/18014398509481984')
		print('b = 3250706127527617/2251799813685248')
		print('a = 12807111440343041/9007199254740992')
		exit(0)
	
	
	if pre_condition_119(b=b,delta=delta)==True:
		print("pre_condition_119 SAT")
		print('delta = 1565704557959169/72057594037927936')
		print('b = 12698070810625/8796093022208')
		print('a = 50027779063809/35184372088832')
		exit(0)
	
	
	if pre_condition_120(b=b,delta=delta)==True:
		print("pre_condition_120 SAT")
		print('delta = 782852278982657/36028797018963968')
		print('b = 6349035405313/4398046511104')
		print('a = 25013889531905/17592186044416')
		exit(0)
	
	
	if pre_condition_121(b=b,delta=delta)==True:
		print("pre_condition_121 SAT")
		print('delta = 43/2048')
		print('b = 369/256')
		print('a = 1455/1024')
		exit(0)
	
	
	if pre_condition_122(b=b,delta=delta)==True:
		print("pre_condition_122 SAT")
		print('delta = 3131409115912193/144115188075855872')
		print('b = 25396141621249/17592186044416')
		print('a = 100055558127617/70368744177664')
		exit(0)
	
	
	if pre_condition_123(b=b,delta=delta)==True:
		print("pre_condition_123 SAT")
		print('delta = 6116033429695/281474976710656')
		print('b = 1587258851329/1099511627776')
		print('a = 200111116255265/140737488355328')
		exit(0)
	
	
	if pre_condition_124(b=b,delta=delta)==True:
		print("pre_condition_124 SAT")
		print('delta = 100205091710488667/4611686018427387904')
		print('b = 13002824510082923/9007199254740992')
		print('a = 102456891522686999/72057594037927936')
		exit(0)
	
	
	if pre_condition_125(b=b,delta=delta)==True:
		print("pre_condition_125 SAT")
		print('delta = 782852279025665/36028797018963968')
		print('b = 793629425665/549755813888')
		print('a = 3126736191489/2199023255552')
		exit(0)
	
	
	if pre_condition_126(b=b,delta=delta)==True:
		print("pre_condition_126 SAT")
		print('delta = 391426139488263/18014398509481984')
		print('b = 3250706127519745/2251799813685248')
		print('a = 12807111440334849/9007199254740992')
		exit(0)
	
	
	if pre_condition_127(b=b,delta=delta)==True:
		print("pre_condition_127 SAT")
		print('delta = 391426139488263/18014398509481984')
		print('b = 3250706127519745/2251799813685248')
		print('a = 12807111440334849/9007199254740992')
		exit(0)
	
	
	if pre_condition_128(b=b,delta=delta)==True:
		print("pre_condition_128 SAT")
		print('delta = 782852278976561/36028797018963968')
		print('b = 812676531879937/562949953421312')
		print('a = 3201777860083713/2251799813685248')
		exit(0)
	
	
	if pre_condition_129(b=b,delta=delta)==True:
		print("pre_condition_129 SAT")
		print('delta = 391426139534855/18014398509481984')
		print('b = 3250706127527617/2251799813685248')
		print('a = 12807111440343041/9007199254740992')
		exit(0)
	
	
	if pre_condition_130(b=b,delta=delta)==True:
		print("pre_condition_130 SAT")
		print('delta = 24464133718751/1125899906842624')
		print('b = 50792283242527/35184372088832')
		print('a = 800444465021057/562949953421312')
		exit(0)
	
	
	if pre_condition_131(b=b,delta=delta)==True:
		print("pre_condition_131 SAT")
		print('delta = 48928267437495/2251799813685248')
		print('b = 406338265940215/281474976710656')
		print('a = 1600888930042113/1125899906842624')
		exit(0)
	
	
	if pre_condition_132(b=b,delta=delta)==True:
		print("pre_condition_132 SAT")
		print('delta = 391426139534855/18014398509481984')
		print('b = 3250706127527617/2251799813685248')
		print('a = 12807111440343041/9007199254740992')
		exit(0)
	
	
	if pre_condition_133(b=b,delta=delta)==True:
		print("pre_condition_133 SAT")
		print('delta = 97856534874983/4503599627370496')
		print('b = 812676531880429/562949953421312')
		print('a = 3201777860084225/2251799813685248')
		exit(0)
	
	
	if pre_condition_134(b=b,delta=delta)==True:
		print("pre_condition_134 SAT")
		print('delta = 782852279069757/36028797018963968')
		print('b = 3250706127527621/2251799813685248')
		print('a = 12807111440343045/9007199254740992')
		exit(0)
	
	
	if pre_condition_135(b=b,delta=delta)==True:
		print("pre_condition_135 SAT")
		print('delta = 782852279069757/36028797018963968')
		print('b = 3250706127527621/2251799813685248')
		print('a = 12807111440343045/9007199254740992')
		exit(0)
	
	
	if pre_condition_136(b=b,delta=delta)==True:
		print("pre_condition_136 SAT")
		print('delta = 782852279069757/36028797018963968')
		print('b = 3250706127527621/2251799813685248')
		print('a = 12807111440343045/9007199254740992')
		exit(0)
	
	
	if pre_condition_137(b=b,delta=delta)==True:
		print("pre_condition_137 SAT")
		print('delta = 782852279069757/36028797018963968')
		print('b = 3250706127527621/2251799813685248')
		print('a = 12807111440343045/9007199254740992')
		exit(0)
	
	
	if pre_condition_138(b=b,delta=delta)==True:
		print("pre_condition_138 SAT")
		print('delta = 782852279069757/36028797018963968')
		print('b = 3250706127527621/2251799813685248')
		print('a = 12807111440343045/9007199254740992')
		exit(0)
	
	
	if pre_condition_139(b=b,delta=delta)==True:
		print("pre_condition_139 SAT")
		print('delta = 782852279069757/36028797018963968')
		print('b = 3250706127527621/2251799813685248')
		print('a = 12807111440343045/9007199254740992')
		exit(0)
	
	
	if pre_condition_140(b=b,delta=delta)==True:
		print("pre_condition_140 SAT")
		print('delta = 782852279069757/36028797018963968')
		print('b = 3250706127527621/2251799813685248')
		print('a = 12807111440343045/9007199254740992')
		exit(0)
	
	
	if pre_condition_141(b=b,delta=delta)==True:
		print("pre_condition_141 SAT")
		print('delta = 782852279069757/36028797018963968')
		print('b = 3250706127527621/2251799813685248')
		print('a = 12807111440343045/9007199254740992')
		exit(0)
	
	
	if pre_condition_142(b=b,delta=delta)==True:
		print("pre_condition_142 SAT")
		print('delta = 782852279069757/36028797018963968')
		print('b = 3250706127527621/2251799813685248')
		print('a = 12807111440343045/9007199254740992')
		exit(0)
	
	
	if pre_condition_143(b=b,delta=delta)==True:
		print("pre_condition_143 SAT")
		print('delta = 782852279069757/36028797018963968')
		print('b = 3250706127527621/2251799813685248')
		print('a = 12807111440343045/9007199254740992')
		exit(0)
	
	
	if pre_condition_144(b=b,delta=delta)==True:
		print("pre_condition_144 SAT")
		print('delta = 782852279069757/36028797018963968')
		print('b = 3250706127527621/2251799813685248')
		print('a = 12807111440343045/9007199254740992')
		exit(0)
	
	
	if pre_condition_145(b=b,delta=delta)==True:
		print("pre_condition_145 SAT")
		print('delta = 782852279069757/36028797018963968')
		print('b = 3250706127527621/2251799813685248')
		print('a = 12807111440343045/9007199254740992')
		exit(0)
	
	
	if pre_condition_146(b=b,delta=delta)==True:
		print("pre_condition_146 SAT")
		print('delta = 782852279069757/36028797018963968')
		print('b = 3250706127527621/2251799813685248')
		print('a = 12807111440343045/9007199254740992')
		exit(0)
	
	
	if pre_condition_147(b=b,delta=delta)==True:
		print("pre_condition_147 SAT")
		print('delta = 782852279069757/36028797018963968')
		print('b = 3250706127527621/2251799813685248')
		print('a = 12807111440343045/9007199254740992')
		exit(0)
	
	
	if pre_condition_148(b=b,delta=delta)==True:
		print("pre_condition_148 SAT")
		print('delta = 782852279069757/36028797018963968')
		print('b = 3250706127527621/2251799813685248')
		print('a = 12807111440343045/9007199254740992')
		exit(0)
	
	
	if pre_condition_149(b=b,delta=delta)==True:
		print("pre_condition_149 SAT")
		print('delta = 782852279069757/36028797018963968')
		print('b = 3250706127527621/2251799813685248')
		print('a = 12807111440343045/9007199254740992')
		exit(0)
	
	
	if pre_condition_150(b=b,delta=delta)==True:
		print("pre_condition_150 SAT")
		print('delta = 782852279069757/36028797018963968')
		print('b = 3250706127527621/2251799813685248')
		print('a = 12807111440343045/9007199254740992')
		exit(0)
	
	
	if pre_condition_151(b=b,delta=delta)==True:
		print("pre_condition_151 SAT")
		print('delta = 782852279069757/36028797018963968')
		print('b = 3250706127527621/2251799813685248')
		print('a = 12807111440343045/9007199254740992')
		exit(0)
	
	
	if pre_condition_152(b=b,delta=delta)==True:
		print("pre_condition_152 SAT")
		print('delta = 782852279069757/36028797018963968')
		print('b = 3250706127527621/2251799813685248')
		print('a = 12807111440343045/9007199254740992')
		exit(0)
	
	
	if pre_condition_153(b=b,delta=delta)==True:
		print("pre_condition_153 SAT")
		print('delta = 782852279069757/36028797018963968')
		print('b = 3250706127527621/2251799813685248')
		print('a = 12807111440343045/9007199254740992')
		exit(0)
	
	
	if pre_condition_154(b=b,delta=delta)==True:
		print("pre_condition_154 SAT")
		print('delta = 782852279069757/36028797018963968')
		print('b = 3250706127527621/2251799813685248')
		print('a = 12807111440343045/9007199254740992')
		exit(0)
	
	
	if pre_condition_155(b=b,delta=delta)==True:
		print("pre_condition_155 SAT")
		print('delta = 782852279069757/36028797018963968')
		print('b = 3250706127527621/2251799813685248')
		print('a = 12807111440343045/9007199254740992')
		exit(0)
	
	
	if pre_condition_156(b=b,delta=delta)==True:
		print("pre_condition_156 SAT")
		print('delta = 782852279069757/36028797018963968')
		print('b = 3250706127527621/2251799813685248')
		print('a = 12807111440343045/9007199254740992')
		exit(0)
	
	
	if pre_condition_157(b=b,delta=delta)==True:
		print("pre_condition_157 SAT")
		print('delta = 782852279069757/36028797018963968')
		print('b = 3250706127527621/2251799813685248')
		print('a = 12807111440343045/9007199254740992')
		exit(0)
	
	
	if pre_condition_158(b=b,delta=delta)==True:
		print("pre_condition_158 SAT")
		print('delta = 782852279069757/36028797018963968')
		print('b = 3250706127527621/2251799813685248')
		print('a = 12807111440343045/9007199254740992')
		exit(0)
	
	
	if pre_condition_159(b=b,delta=delta)==True:
		print("pre_condition_159 SAT")
		print('delta = 782852279069757/36028797018963968')
		print('b = 3250706127527621/2251799813685248')
		print('a = 12807111440343045/9007199254740992')
		exit(0)
	
	
	if pre_condition_160(b=b,delta=delta)==True:
		print("pre_condition_160 SAT")
		print('delta = 782852279069757/36028797018963968')
		print('b = 3250706127527621/2251799813685248')
		print('a = 12807111440343045/9007199254740992')
		exit(0)
	
	
	if pre_condition_161(b=b,delta=delta)==True:
		print("pre_condition_161 SAT")
		print('delta = 782852279069757/36028797018963968')
		print('b = 3250706127527621/2251799813685248')
		print('a = 12807111440343045/9007199254740992')
		exit(0)
	
	
	if pre_condition_162(b=b,delta=delta)==True:
		print("pre_condition_162 SAT")
		print('delta = 782852279069757/36028797018963968')
		print('b = 3250706127527621/2251799813685248')
		print('a = 12807111440343045/9007199254740992')
		exit(0)
	
	
	if pre_condition_163(b=b,delta=delta)==True:
		print("pre_condition_163 SAT")
		print('delta = 782852279069757/36028797018963968')
		print('b = 3250706127527621/2251799813685248')
		print('a = 12807111440343045/9007199254740992')
		exit(0)
	
	
	if pre_condition_164(b=b,delta=delta)==True:
		print("pre_condition_164 SAT")
		print('delta = 782852279069757/36028797018963968')
		print('b = 3250706127527621/2251799813685248')
		print('a = 12807111440343045/9007199254740992')
		exit(0)
	
	
	if pre_condition_165(b=b,delta=delta)==True:
		print("pre_condition_165 SAT")
		print('delta = 782852279069757/36028797018963968')
		print('b = 3250706127527621/2251799813685248')
		print('a = 12807111440343045/9007199254740992')
		exit(0)
	
	
	if pre_condition_166(b=b,delta=delta)==True:
		print("pre_condition_166 SAT")
		print('delta = 782852279069757/36028797018963968')
		print('b = 3250706127527621/2251799813685248')
		print('a = 12807111440343045/9007199254740992')
		exit(0)
	
	
	if pre_condition_167(b=b,delta=delta)==True:
		print("pre_condition_167 SAT")
		print('delta = 782852279069757/36028797018963968')
		print('b = 3250706127527621/2251799813685248')
		print('a = 12807111440343045/9007199254740992')
		exit(0)
	
	
	if pre_condition_168(b=b,delta=delta)==True:
		print("pre_condition_168 SAT")
		print('delta = 782852279069757/36028797018963968')
		print('b = 3250706127527621/2251799813685248')
		print('a = 12807111440343045/9007199254740992')
		exit(0)
	
	
	if pre_condition_169(b=b,delta=delta)==True:
		print("pre_condition_169 SAT")
		print('delta = 782852279069757/36028797018963968')
		print('b = 3250706127527621/2251799813685248')
		print('a = 12807111440343045/9007199254740992')
		exit(0)
	
	
	if pre_condition_170(b=b,delta=delta)==True:
		print("pre_condition_170 SAT")
		print('delta = 782852279069757/36028797018963968')
		print('b = 3250706127527621/2251799813685248')
		print('a = 12807111440343045/9007199254740992')
		exit(0)
	
	
	if pre_condition_171(b=b,delta=delta)==True:
		print("pre_condition_171 SAT")
		print('delta = 782852279069757/36028797018963968')
		print('b = 3250706127527621/2251799813685248')
		print('a = 12807111440343045/9007199254740992')
		exit(0)
	
	
	if pre_condition_172(b=b,delta=delta)==True:
		print("pre_condition_172 SAT")
		print('delta = 782852279069757/36028797018963968')
		print('b = 3250706127527621/2251799813685248')
		print('a = 12807111440343045/9007199254740992')
		exit(0)
	
	
	if pre_condition_173(b=b,delta=delta)==True:
		print("pre_condition_173 SAT")
		print('delta = 782852279069757/36028797018963968')
		print('b = 3250706127527621/2251799813685248')
		print('a = 12807111440343045/9007199254740992')
		exit(0)
	
	
	if pre_condition_174(b=b,delta=delta)==True:
		print("pre_condition_174 SAT")
		print('delta = 782852279069757/36028797018963968')
		print('b = 3250706127527621/2251799813685248')
		print('a = 12807111440343045/9007199254740992')
		exit(0)
	
	
	if pre_condition_175(b=b,delta=delta)==True:
		print("pre_condition_175 SAT")
		print('delta = 782852279069757/36028797018963968')
		print('b = 3250706127527621/2251799813685248')
		print('a = 12807111440343045/9007199254740992')
		exit(0)
	
	
	if pre_condition_176(b=b,delta=delta)==True:
		print("pre_condition_176 SAT")
		print('delta = 782852279069757/36028797018963968')
		print('b = 3250706127527621/2251799813685248')
		print('a = 12807111440343045/9007199254740992')
		exit(0)
	
	
	if pre_condition_177(b=b,delta=delta)==True:
		print("pre_condition_177 SAT")
		print('delta = 782852279069757/36028797018963968')
		print('b = 3250706127527621/2251799813685248')
		print('a = 12807111440343045/9007199254740992')
		exit(0)
	
	
	if pre_condition_178(b=b,delta=delta)==True:
		print("pre_condition_178 SAT")
		print('delta = 782852279069757/36028797018963968')
		print('b = 3250706127527621/2251799813685248')
		print('a = 12807111440343045/9007199254740992')
		exit(0)
	
	
	if pre_condition_179(b=b,delta=delta)==True:
		print("pre_condition_179 SAT")
		print('delta = 782852279069757/36028797018963968')
		print('b = 3250706127527621/2251799813685248')
		print('a = 12807111440343045/9007199254740992')
		exit(0)
	
	
	if pre_condition_180(b=b,delta=delta)==True:
		print("pre_condition_180 SAT")
		print('delta = 782852279069757/36028797018963968')
		print('b = 3250706127527621/2251799813685248')
		print('a = 12807111440343045/9007199254740992')
		exit(0)
	
	
	if pre_condition_181(b=b,delta=delta)==True:
		print("pre_condition_181 SAT")
		print('delta = 782852279069757/36028797018963968')
		print('b = 3250706127527621/2251799813685248')
		print('a = 12807111440343045/9007199254740992')
		exit(0)
	
	
	if pre_condition_182(b=b,delta=delta)==True:
		print("pre_condition_182 SAT")
		print('delta = 782852279069757/36028797018963968')
		print('b = 3250706127527621/2251799813685248')
		print('a = 12807111440343045/9007199254740992')
		exit(0)
	
	
	if pre_condition_183(b=b,delta=delta)==True:
		print("pre_condition_183 SAT")
		print('delta = 782852278988673/36028797018963968')
		print('b = 3174517702657/2199023255552')
		print('a = 400222232510497/281474976710656')
		exit(0)
	
	
	if pre_condition_184(b=b,delta=delta)==True:
		print("pre_condition_184 SAT")
		print('delta = 12525636463812081/576460752303423488')
		print('b = 101584566485023/70368744177664')
		print('a = 51228445761343521/36028797018963968')
		exit(0)
	
	
	if pre_condition_185(b=b,delta=delta)==True:
		print("pre_condition_185 SAT")
		print('delta = 782852278988673/36028797018963968')
		print('b = 3174517702657/2199023255552')
		print('a = 400222232510497/281474976710656')
		exit(0)
	
	
	if pre_condition_186(b=b,delta=delta)==True:
		print("pre_condition_186 SAT")
		print('delta = 391426139488447/18014398509481984')
		print('b = 101584566484993/70368744177664')
		print('a = 12807111440334881/9007199254740992')
		exit(0)
	
	
	if pre_condition_187(b=b,delta=delta)==True:
		print("pre_condition_187 SAT")
		print('delta = 391426139494087/18014398509481984')
		print('b = 3250706127520729/2251799813685248')
		print('a = 12807111440335873/9007199254740992')
		exit(0)
	
	
	if pre_condition_188(b=b,delta=delta)==True:
		print("pre_condition_188 SAT")
		print('delta = 97856534874995/4503599627370496')
		print('b = 812676531880431/562949953421312')
		print('a = 3201777860084227/2251799813685248')
		exit(0)
	
	
	if pre_condition_189(b=b,delta=delta)==True:
		print("pre_condition_189 SAT")
		print('delta = 100205091710488667/4611686018427387904')
		print('b = 13002824510082923/9007199254740992')
		print('a = 102456891522686999/72057594037927936')
		exit(0)
	
	
	if pre_condition_190(b=b,delta=delta)==True:
		print("pre_condition_190 SAT")
		print('delta = 100205091710488667/4611686018427387904')
		print('b = 13002824510082923/9007199254740992')
		print('a = 102456891522686999/72057594037927936')
		exit(0)
	
	
	if pre_condition_191(b=b,delta=delta)==True:
		print("pre_condition_191 SAT")
		print('delta = 100205091710488667/4611686018427387904')
		print('b = 13002824510082923/9007199254740992')
		print('a = 102456891522686999/72057594037927936')
		exit(0)
	
	
	if pre_condition_192(b=b,delta=delta)==True:
		print("pre_condition_192 SAT")
		print('delta = 782852278976703/36028797018963968')
		print('b = 203169132969985/140737488355328')
		print('a = 25614222880669729/18014398509481984')
		exit(0)
	
	
	if pre_condition_193(b=b,delta=delta)==True:
		print("pre_condition_193 SAT")
		print('delta = 391426139494087/18014398509481984')
		print('b = 3250706127520729/2251799813685248')
		print('a = 12807111440335873/9007199254740992')
		exit(0)
	
	
	if pre_condition_194(b=b,delta=delta)==True:
		print("pre_condition_194 SAT")
		print('delta = 25051272927622483/1152921504606846976')
		print('b = 104022596080663411/72057594037927936')
		print('a = 819655132181496047/576460752303423488')
		exit(0)
	
	
	if pre_condition_195(b=b,delta=delta)==True:
		print("pre_condition_195 SAT")
		print('delta = 100205091710488667/4611686018427387904')
		print('b = 13002824510082923/9007199254740992')
		print('a = 102456891522686999/72057594037927936')
		exit(0)
	
	
	if pre_condition_196(b=b,delta=delta)==True:
		print("pre_condition_196 SAT")
		print('delta = 391426139494087/18014398509481984')
		print('b = 3250706127520729/2251799813685248')
		print('a = 12807111440335873/9007199254740992')
		exit(0)
	
	
	if pre_condition_197(b=b,delta=delta)==True:
		print("pre_condition_197 SAT")
		print('delta = 195713069749959/9007199254740992')
		print('b = 1625353063760857/1125899906842624')
		print('a = 6403555720168449/4503599627370496')
		exit(0)
	
	
	if pre_condition_198(b=b,delta=delta)==True:
		print("pre_condition_198 SAT")
		print('delta = 1565704557953215/72057594037927936')
		print('b = 406338265939969/281474976710656')
		print('a = 51228445761339425/36028797018963968')
		exit(0)
	
	
	if pre_condition_199(b=b,delta=delta)==True:
		print("pre_condition_199 SAT")
		print('delta = 1565704557959169/72057594037927936')
		print('b = 12698070810625/8796093022208')
		print('a = 50027779063809/35184372088832')
		exit(0)
	
	
	if pre_condition_200(b=b,delta=delta)==True:
		print("pre_condition_200 SAT")
		print('delta = 1565704557999713/72057594037927936')
		print('b = 812676531880429/562949953421312')
		print('a = 3201777860084225/2251799813685248')
		exit(0)
	
	
	if pre_condition_201(b=b,delta=delta)==True:
		print("pre_condition_201 SAT")
		print('delta = 24464133718775/1125899906842624')
		print('b = 1587258851329/1099511627776')
		print('a = 800444465021061/562949953421312')
		exit(0)
	
	
	if pre_condition_202(b=b,delta=delta)==True:
		print("pre_condition_202 SAT")
		print('delta = 391426139499911/18014398509481984')
		print('b = 3250706127521713/2251799813685248')
		print('a = 12807111440336897/9007199254740992')
		exit(0)
	
	
	if pre_condition_203(b=b,delta=delta)==True:
		print("pre_condition_203 SAT")
		print('delta = 391426139499911/18014398509481984')
		print('b = 3250706127521713/2251799813685248')
		print('a = 12807111440336897/9007199254740992')
		exit(0)
	
	
	if pre_condition_204(b=b,delta=delta)==True:
		print("pre_condition_204 SAT")
		print('delta = 200410183418034293/9223372036854775808')
		print('b = 832180768645058453/576460752303423488')
		print('a = 3278620528725725239/2305843009213693952')
		exit(0)
	
	
	if pre_condition_205(b=b,delta=delta)==True:
		print("pre_condition_205 SAT")
		print('delta = 12525636463812081/576460752303423488')
		print('b = 101584566485023/70368744177664')
		print('a = 51228445761343521/36028797018963968')
		exit(0)
	
	
	if pre_condition_206(b=b,delta=delta)==True:
		print("pre_condition_206 SAT")
		print('delta = 1565704557959169/72057594037927936')
		print('b = 12698070810625/8796093022208')
		print('a = 50027779063809/35184372088832')
		exit(0)
	
	
	if pre_condition_207(b=b,delta=delta)==True:
		print("pre_condition_207 SAT")
		print('delta = 12525636463812081/576460752303423488')
		print('b = 101584566485023/70368744177664')
		print('a = 51228445761343521/36028797018963968')
		exit(0)
	
	
	if pre_condition_208(b=b,delta=delta)==True:
		print("pre_condition_208 SAT")
		print('delta = 1565704557959169/72057594037927936')
		print('b = 12698070810625/8796093022208')
		print('a = 50027779063809/35184372088832')
		exit(0)
	
	
	if pre_condition_209(b=b,delta=delta)==True:
		print("pre_condition_209 SAT")
		print('delta = 391426139488263/18014398509481984')
		print('b = 3250706127519745/2251799813685248')
		print('a = 12807111440334849/9007199254740992')
		exit(0)
	
	
	if pre_condition_210(b=b,delta=delta)==True:
		print("pre_condition_210 SAT")
		print('delta = 391426139488263/18014398509481984')
		print('b = 3250706127519745/2251799813685248')
		print('a = 12807111440334849/9007199254740992')
		exit(0)
	
	
	if pre_condition_211(b=b,delta=delta)==True:
		print("pre_condition_211 SAT")
		print('delta = 50102545854508585/2305843009213693952')
		print('b = 104022596080632307/72057594037927936')
		print('a = 409827566090715655/288230376151711744')
		exit(0)
	
	
	if pre_condition_212(b=b,delta=delta)==True:
		print("pre_condition_212 SAT")
		print('delta = 391426139488263/18014398509481984')
		print('b = 3250706127519745/2251799813685248')
		print('a = 12807111440334849/9007199254740992')
		exit(0)
	
	
	if pre_condition_213(b=b,delta=delta)==True:
		print("pre_condition_213 SAT")
		print('delta = 1565704557953073/72057594037927936')
		print('b = 1625353063759873/1125899906842624')
		print('a = 6403555720167425/4503599627370496')
		exit(0)
	
	
	if pre_condition_214(b=b,delta=delta)==True:
		print("pre_condition_214 SAT")
		print('delta = 391426139488263/18014398509481984')
		print('b = 3250706127519745/2251799813685248')
		print('a = 12807111440334849/9007199254740992')
		exit(0)
	
	
	if pre_condition_215(b=b,delta=delta)==True:
		print("pre_condition_215 SAT")
		print('delta = 391426139494087/18014398509481984')
		print('b = 3250706127520729/2251799813685248')
		print('a = 12807111440335873/9007199254740992')
		exit(0)
	
	
	if pre_condition_216(b=b,delta=delta)==True:
		print("pre_condition_216 SAT")
		print('delta = 782852278988209/36028797018963968')
		print('b = 812676531880183/562949953421312')
		print('a = 3201777860083969/2251799813685248')
		exit(0)
	
	
	if pre_condition_217(b=b,delta=delta)==True:
		print("pre_condition_217 SAT")
		print('delta = 200410183420979805/9223372036854775808')
		print('b = 208045192161326821/144115188075855872')
		print('a = 3278620528725984185/2305843009213693952')
		exit(0)
	
	
	if pre_condition_218(b=b,delta=delta)==True:
		print("pre_condition_218 SAT")
		print('delta = 12525636463625689/576460752303423488')
		print('b = 26005649020158015/18014398509481984')
		print('a = 102456891522678849/72057594037927936')
		exit(0)
	
	
	if pre_condition_219(b=b,delta=delta)==True:
		print("pre_condition_219 SAT")
		print('delta = 1565704557953215/72057594037927936')
		print('b = 406338265939969/281474976710656')
		print('a = 51228445761339425/36028797018963968')
		exit(0)
	
	
	if pre_condition_220(b=b,delta=delta)==True:
		print("pre_condition_220 SAT")
		print('delta = 1565704557953215/72057594037927936')
		print('b = 406338265939969/281474976710656')
		print('a = 51228445761339425/36028797018963968')
		exit(0)
	
	
	if pre_condition_221(b=b,delta=delta)==True:
		print("pre_condition_221 SAT")
		print('delta = 3131409115912193/144115188075855872')
		print('b = 25396141621249/17592186044416')
		print('a = 100055558127617/70368744177664')
		exit(0)
	
	
	if pre_condition_222(b=b,delta=delta)==True:
		print("pre_condition_222 SAT")
		print('delta = 782852278976703/36028797018963968')
		print('b = 203169132969985/140737488355328')
		print('a = 25614222880669729/18014398509481984')
		exit(0)
	
	
	if pre_condition_223(b=b,delta=delta)==True:
		print("pre_condition_223 SAT")
		print('delta = 200410183418034293/9223372036854775808')
		print('b = 832180768645058453/576460752303423488')
		print('a = 3278620528725725239/2305843009213693952')
		exit(0)
	
	
	if pre_condition_224(b=b,delta=delta)==True:
		print("pre_condition_224 SAT")
		print('delta = 200410183418034293/9223372036854775808')
		print('b = 832180768645058453/576460752303423488')
		print('a = 3278620528725725239/2305843009213693952')
		exit(0)
	
	
	if pre_condition_225(b=b,delta=delta)==True:
		print("pre_condition_225 SAT")
		print('delta = 195713069750191/9007199254740992')
		print('b = 1587258851329/1099511627776')
		print('a = 3201777860084245/2251799813685248')
		exit(0)
	
	
	if pre_condition_226(b=b,delta=delta)==True:
		print("pre_condition_226 SAT")
		print('delta = 391426139500381/18014398509481984')
		print('b = 1587258851329/1099511627776')
		print('a = 6403555720168489/4503599627370496')
		exit(0)
	
	
	if pre_condition_227(b=b,delta=delta)==True:
		print("pre_condition_227 SAT")
		print('delta = 382252089363/17592186044416')
		print('b = 3174517702659/2199023255552')
		print('a = 12506944765955/8796093022208')
		exit(0)
	
	
	if pre_condition_228(b=b,delta=delta)==True:
		print("pre_condition_228 SAT")
		print('delta = 391426139494087/18014398509481984')
		print('b = 3250706127520729/2251799813685248')
		print('a = 12807111440335873/9007199254740992')
		exit(0)
	
	
	if pre_condition_229(b=b,delta=delta)==True:
		print("pre_condition_229 SAT")
		print('delta = 782852278982657/36028797018963968')
		print('b = 6349035405313/4398046511104')
		print('a = 25013889531905/17592186044416')
		exit(0)
	
	
	if pre_condition_230(b=b,delta=delta)==True:
		print("pre_condition_230 SAT")
		print('delta = 782852278982657/36028797018963968')
		print('b = 6349035405313/4398046511104')
		print('a = 25013889531905/17592186044416')
		exit(0)
	
	
	if pre_condition_231(b=b,delta=delta)==True:
		print("pre_condition_231 SAT")
		print('delta = 782852278976703/36028797018963968')
		print('b = 203169132969985/140737488355328')
		print('a = 25614222880669729/18014398509481984')
		exit(0)
	
	
	if pre_condition_232(b=b,delta=delta)==True:
		print("pre_condition_232 SAT")
		print('delta = 782852278976561/36028797018963968')
		print('b = 812676531879937/562949953421312')
		print('a = 3201777860083713/2251799813685248')
		exit(0)
	
	
	if pre_condition_233(b=b,delta=delta)==True:
		print("pre_condition_233 SAT")
		print('delta = 782852278976561/36028797018963968')
		print('b = 812676531879937/562949953421312')
		print('a = 3201777860083713/2251799813685248')
		exit(0)
	
	
	if pre_condition_234(b=b,delta=delta)==True:
		print("pre_condition_234 SAT")
		print('delta = 155/8192')
		print('b = 737/512')
		print('a = 5819/4096')
		exit(0)
	
	
	if pre_condition_235(b=b,delta=delta)==True:
		print("pre_condition_235 SAT")
		print('delta = 12525636463811281/576460752303423488')
		print('b = 13002824510082927/9007199254740992')
		print('a = 51228445761343503/36028797018963968')
		exit(0)
	
	
	if pre_condition_236(b=b,delta=delta)==True:
		print("pre_condition_236 SAT")
		print('delta = 12525636463625689/576460752303423488')
		print('b = 26005649020158015/18014398509481984')
		print('a = 102456891522678849/72057594037927936')
		exit(0)
	
	
	if pre_condition_237(b=b,delta=delta)==True:
		print("pre_condition_237 SAT")
		print('delta = 50102545854508585/2305843009213693952')
		print('b = 104022596080632307/72057594037927936')
		print('a = 409827566090715655/288230376151711744')
		exit(0)
	
	
	if pre_condition_238(b=b,delta=delta)==True:
		print("pre_condition_238 SAT")
		print('delta = 12525636463811281/576460752303423488')
		print('b = 13002824510082927/9007199254740992')
		print('a = 51228445761343503/36028797018963968')
		exit(0)
	
	
	if pre_condition_239(b=b,delta=delta)==True:
		print("pre_condition_239 SAT")
		print('delta = 50102545854508585/2305843009213693952')
		print('b = 104022596080632307/72057594037927936')
		print('a = 409827566090715655/288230376151711744')
		exit(0)
	
	
	if pre_condition_240(b=b,delta=delta)==True:
		print("pre_condition_240 SAT")
		print('delta = 391426139488447/18014398509481984')
		print('b = 101584566484993/70368744177664')
		print('a = 12807111440334881/9007199254740992')
		exit(0)
	
	
	if pre_condition_241(b=b,delta=delta)==True:
		print("pre_condition_241 SAT")
		print('delta = 100205091710488667/4611686018427387904')
		print('b = 13002824510082923/9007199254740992')
		print('a = 102456891522686999/72057594037927936')
		exit(0)
	
	
	if pre_condition_242(b=b,delta=delta)==True:
		print("pre_condition_242 SAT")
		print('delta = 3131409115912193/144115188075855872')
		print('b = 25396141621249/17592186044416')
		print('a = 100055558127617/70368744177664')
		exit(0)
	
	
	if pre_condition_243(b=b,delta=delta)==True:
		print("pre_condition_243 SAT")
		print('delta = 50102545854508585/2305843009213693952')
		print('b = 104022596080632307/72057594037927936')
		print('a = 409827566090715655/288230376151711744')
		exit(0)
	
	
	if pre_condition_244(b=b,delta=delta)==True:
		print("pre_condition_244 SAT")
		print('delta = 3131409115907545/144115188075855872')
		print('b = 6501412255039551/4503599627370496')
		print('a = 25614222880669761/18014398509481984')
		exit(0)
	
	
	if pre_condition_245(b=b,delta=delta)==True:
		print("pre_condition_245 SAT")
		print('delta = 25051272927260201/1152921504606846976')
		print('b = 52011298040316403/36028797018963968')
		print('a = 204913783045358087/144115188075855872')
		exit(0)
	
	
	if pre_condition_246(b=b,delta=delta)==True:
		print("pre_condition_246 SAT")
		print('delta = 782852278988673/36028797018963968')
		print('b = 3174517702657/2199023255552')
		print('a = 400222232510497/281474976710656')
		exit(0)
	
	
	if pre_condition_247(b=b,delta=delta)==True:
		print("pre_condition_247 SAT")
		print('delta = 1565704558139549/72057594037927936')
		print('b = 6501412255055245/4503599627370496')
		print('a = 25614222880686093/18014398509481984')
		exit(0)
	
	
	if pre_condition_248(b=b,delta=delta)==True:
		print("pre_condition_248 SAT")
		print('delta = 782852278976703/36028797018963968')
		print('b = 203169132969985/140737488355328')
		print('a = 25614222880669729/18014398509481984')
		exit(0)
	
	
	if pre_condition_249(b=b,delta=delta)==True:
		print("pre_condition_249 SAT")
		print('delta = 782852278976561/36028797018963968')
		print('b = 812676531879937/562949953421312')
		print('a = 3201777860083713/2251799813685248')
		exit(0)
	
	
	if pre_condition_250(b=b,delta=delta)==True:
		print("pre_condition_250 SAT")
		print('delta = 1565704557953031/72057594037927936')
		print('b = 13002824510078977/9007199254740992')
		print('a = 51228445761339393/36028797018963968')
		exit(0)
	
	
	if pre_condition_251(b=b,delta=delta)==True:
		print("pre_condition_251 SAT")
		print('delta = 391426139500367/18014398509481984')
		print('b = 1625353063760895/1125899906842624')
		print('a = 12807111440336977/9007199254740992')
		exit(0)
	
	
	if pre_condition_252(b=b,delta=delta)==True:
		print("pre_condition_252 SAT")
		print('delta = 391426139499911/18014398509481984')
		print('b = 3250706127521713/2251799813685248')
		print('a = 12807111440336897/9007199254740992')
		exit(0)
	
	
	if pre_condition_253(b=b,delta=delta)==True:
		print("pre_condition_253 SAT")
		print('delta = 1565704557953215/72057594037927936')
		print('b = 406338265939969/281474976710656')
		print('a = 51228445761339425/36028797018963968')
		exit(0)
	
	
	if pre_condition_254(b=b,delta=delta)==True:
		print("pre_condition_254 SAT")
		print('delta = 391426139488641/18014398509481984')
		print('b = 50792283242497/35184372088832')
		print('a = 200111116255233/140737488355328')
		exit(0)
	
	
	if pre_condition_255(b=b,delta=delta)==True:
		print("pre_condition_255 SAT")
		print('delta = 1565704557953031/72057594037927936')
		print('b = 13002824510078977/9007199254740992')
		print('a = 51228445761339393/36028797018963968')
		exit(0)


	print("UNKNOWN")
	exit(0)
