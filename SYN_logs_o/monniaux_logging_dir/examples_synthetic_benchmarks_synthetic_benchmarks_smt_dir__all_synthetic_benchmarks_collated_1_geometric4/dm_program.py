import sympy
from sympy import *

def pre_condition_0(c:sympy.Rational):
	#(x**2 < 41/4) & (2*c - x < -1/2)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(41, 4)), StrictLessThan(Add(Mul(Integer(2), Symbol('c')), Mul(Integer(-1), Symbol('x'))), Rational(-1, 2)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1(c:sympy.Rational):
	#c < -3/16

	pre_cond = StrictLessThan(Symbol('c'), Rational(-3, 16))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_2(c:sympy.Rational):
	#(x**2 < 641/64) & (8*c - x < -1/8)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(641, 64)), StrictLessThan(Add(Mul(Integer(8), Symbol('c')), Mul(Integer(-1), Symbol('x'))), Rational(-1, 8)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_3(c:sympy.Rational):
	#c < -9/64

	pre_cond = StrictLessThan(Symbol('c'), Rational(-9, 64))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_4(c:sympy.Rational):
	#(x**2 < 19) & (c - 3*x < -9)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Integer(19)), StrictLessThan(Add(Symbol('c'), Mul(Integer(-1), Integer(3), Symbol('x'))), Integer(-9)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_5(c:sympy.Rational):
	#c < 3

	pre_cond = StrictLessThan(Symbol('c'), Integer(3))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_6(c:sympy.Rational):
	#(x**2 < 26) & (c + 4*x < -16)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Integer(26)), StrictLessThan(Add(Symbol('c'), Mul(Integer(4), Symbol('x'))), Integer(-16)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_7(c:sympy.Rational):
	#c < 4

	pre_cond = StrictLessThan(Symbol('c'), Integer(4))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_8(c:sympy.Rational):
	#(x**2 < 2321/64) & (8*c + 41*x < -1681/8)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(2321, 64)), StrictLessThan(Add(Mul(Integer(8), Symbol('c')), Mul(Integer(41), Symbol('x'))), Rational(-1681, 8)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_9(c:sympy.Rational):
	#c < 287/64

	pre_cond = StrictLessThan(Symbol('c'), Rational(287, 64))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_10(c:sympy.Rational):
	#(x**2 < 785/16) & (4*c + 25*x < -625/4)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(785, 16)), StrictLessThan(Add(Mul(Integer(4), Symbol('c')), Mul(Integer(25), Symbol('x'))), Rational(-625, 4)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_11(c:sympy.Rational):
	#c < 75/16

	pre_cond = StrictLessThan(Symbol('c'), Rational(75, 16))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_12(c:sympy.Rational):
	#(x**2 < 262801/4096) & (64*c + 471*x < -221841/64)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(262801, 4096)), StrictLessThan(Add(Mul(Integer(64), Symbol('c')), Mul(Integer(471), Symbol('x'))), Rational(-221841, 64)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_13(c:sympy.Rational):
	#c < 19311/4096

	pre_cond = StrictLessThan(Symbol('c'), Rational(19311, 4096))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_14(c:sympy.Rational):
	#(x**2 < 20785/256) & (16*c + 135*x < -18225/16)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(20785, 256)), StrictLessThan(Add(Mul(Integer(16), Symbol('c')), Mul(Integer(135), Symbol('x'))), Rational(-18225, 16)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_15(c:sympy.Rational):
	#c < 1215/256

	pre_cond = StrictLessThan(Symbol('c'), Rational(1215, 256))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_16(c:sympy.Rational):
	#(x**2 < 401/4) & (2*c + 19*x < -361/2)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(401, 4)), StrictLessThan(Add(Mul(Integer(2), Symbol('c')), Mul(Integer(19), Symbol('x'))), Rational(-361, 2)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_17(c:sympy.Rational):
	#c < 19/4

	pre_cond = StrictLessThan(Symbol('c'), Rational(19, 4))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_18(c:sympy.Rational):
	#(x**2 < 496585/4096) & (64*c + 675*x < -455625/64)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(496585, 4096)), StrictLessThan(Add(Mul(Integer(64), Symbol('c')), Mul(Integer(675), Symbol('x'))), Rational(-455625, 64)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_19(c:sympy.Rational):
	#c < 19575/4096

	pre_cond = StrictLessThan(Symbol('c'), Rational(19575, 4096))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_20(c:sympy.Rational):
	#(x**2 < 590041/4096) & (64*c + 741*x < -549081/64)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(590041, 4096)), StrictLessThan(Add(Mul(Integer(64), Symbol('c')), Mul(Integer(741), Symbol('x'))), Rational(-549081, 64)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_21(c:sympy.Rational):
	#c < 20007/4096

	pre_cond = StrictLessThan(Symbol('c'), Rational(20007, 4096))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_22(c:sympy.Rational):
	#(x**2 < 44314289/262144) & (512*c + 6457*x < -41692849/512)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(44314289, 262144)), StrictLessThan(Add(Mul(Integer(512), Symbol('c')), Mul(Integer(6457), Symbol('x'))), Rational(-41692849, 512)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_23(c:sympy.Rational):
	#c < 1284943/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1284943, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_24(c:sympy.Rational):
	#(x**2 < 803089/4096) & (64*c + 873*x < -762129/64)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(803089, 4096)), StrictLessThan(Add(Mul(Integer(64), Symbol('c')), Mul(Integer(873), Symbol('x'))), Rational(-762129, 64)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_25(c:sympy.Rational):
	#c < 20079/4096

	pre_cond = StrictLessThan(Symbol('c'), Rational(20079, 4096))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_26(c:sympy.Rational):
	#(x**2 < 3686969/16384) & (128*c + 1877*x < -3523129/128)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(3686969, 16384)), StrictLessThan(Add(Mul(Integer(128), Symbol('c')), Mul(Integer(1877), Symbol('x'))), Rational(-3523129, 128)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_27(c:sympy.Rational):
	#c < 80711/16384

	pre_cond = StrictLessThan(Symbol('c'), Rational(80711, 16384))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_28(c:sympy.Rational):
	#(x**2 < 67118401/262144) & (512*c + 8031*x < -64496961/512)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(67118401, 262144)), StrictLessThan(Add(Mul(Integer(512), Symbol('c')), Mul(Integer(8031), Symbol('x'))), Rational(-64496961, 512)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_29(c:sympy.Rational):
	#c < 1292991/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1292991, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_30(c:sympy.Rational):
	#(x**2 < 303066785/1048576) & (1024*c + 17105*x < -292581025/1024)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(303066785, 1048576)), StrictLessThan(Add(Mul(Integer(1024), Symbol('c')), Mul(Integer(17105), Symbol('x'))), Rational(-292581025, 1024)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_31(c:sympy.Rational):
	#c < 5182815/1048576

	pre_cond = StrictLessThan(Symbol('c'), Rational(5182815, 1048576))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_32(c:sympy.Rational):
	#(x**2 < 84940769/262144) & (512*c + 9073*x < -82319329/512)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(84940769, 262144)), StrictLessThan(Add(Mul(Integer(512), Symbol('c')), Mul(Integer(9073), Symbol('x'))), Rational(-82319329, 512)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_33(c:sympy.Rational):
	#c < 1297439/262144

	pre_cond = StrictLessThan(Symbol('c'), Rational(1297439, 262144))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_34(c:sympy.Rational):
	#(x**2 < 378549985/1048576) & (1024*c + 19185*x < -368064225/1024)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(378549985, 1048576)), StrictLessThan(Add(Mul(Integer(1024), Symbol('c')), Mul(Integer(19185), Symbol('x'))), Rational(-368064225, 1024)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_35(c:sympy.Rational):
	#c < 5199135/1048576

	pre_cond = StrictLessThan(Symbol('c'), Rational(5199135, 1048576))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_36(c:sympy.Rational):
	#(x**2 < 1677741065/4194304) & (2048*c + 40445*x < -1635798025/2048)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(1677741065, 4194304)), StrictLessThan(Add(Mul(Integer(2048), Symbol('c')), Mul(Integer(40445), Symbol('x'))), Rational(-1635798025, 2048)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_37(c:sympy.Rational):
	#c < 20829175/4194304

	pre_cond = StrictLessThan(Symbol('c'), Rational(20829175, 4194304))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_38(c:sympy.Rational):
	#(x**2 < 462430841/1048576) & (1024*c + 21259*x < -451945081/1024)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(462430841, 1048576)), StrictLessThan(Add(Mul(Integer(1024), Symbol('c')), Mul(Integer(21259), Symbol('x'))), Rational(-451945081, 1024)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_39(c:sympy.Rational):
	#c < 5208455/1048576

	pre_cond = StrictLessThan(Symbol('c'), Rational(5208455, 1048576))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_40(c:sympy.Rational):
	#(x**2 < 8120309489/16777216) & (4096*c + 89177*x < -7952537329/4096)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(8120309489, 16777216)), StrictLessThan(Add(Mul(Integer(4096), Symbol('c')), Mul(Integer(89177), Symbol('x'))), Rational(-7952537329, 4096)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_41(c:sympy.Rational):
	#c < 83380495/16777216

	pre_cond = StrictLessThan(Symbol('c'), Rational(83380495, 16777216))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_42(c:sympy.Rational):
	#(x**2 < 2218818689/4194304) & (2048*c + 46657*x < -2176875649/2048)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(2218818689, 4194304)), StrictLessThan(Add(Mul(Integer(2048), Symbol('c')), Mul(Integer(46657), Symbol('x'))), Rational(-2176875649, 2048)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_43(c:sympy.Rational):
	#c < 20855679/4194304

	pre_cond = StrictLessThan(Symbol('c'), Rational(20855679, 4194304))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_44(c:sympy.Rational):
	#(x**2 < 9663689969/16777216) & (4096*c + 97447*x < -9495917809/4096)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(9663689969, 16777216)), StrictLessThan(Add(Mul(Integer(4096), Symbol('c')), Mul(Integer(97447), Symbol('x'))), Rational(-9495917809, 4096)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_45(c:sympy.Rational):
	#c < 83512079/16777216

	pre_cond = StrictLessThan(Symbol('c'), Rational(83512079, 16777216))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_46(c:sympy.Rational):
	#(x**2 < 41943042665/67108864) & (8192*c + 203155*x < -41271954025/8192)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(41943042665, 67108864)), StrictLessThan(Add(Mul(Integer(8192), Symbol('c')), Mul(Integer(203155), Symbol('x'))), Rational(-41271954025, 8192)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_47(c:sympy.Rational):
	#c < 334189975/67108864

	pre_cond = StrictLessThan(Symbol('c'), Rational(334189975, 67108864))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_48(c:sympy.Rational):
	#(x**2 < 45365699561/67108864) & (8192*c + 211411*x < -44694610921/8192)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(45365699561, 67108864)), StrictLessThan(Add(Mul(Integer(8192), Symbol('c')), Mul(Integer(211411), Symbol('x'))), Rational(-44694610921, 8192)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_49(c:sympy.Rational):
	#c < 334240791/67108864

	pre_cond = StrictLessThan(Symbol('c'), Rational(334240791, 67108864))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_50(c:sympy.Rational):
	#(x**2 < 12230620721/16777216) & (4096*c + 109831*x < -12062848561/4096)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(12230620721, 16777216)), StrictLessThan(Add(Mul(Integer(4096), Symbol('c')), Mul(Integer(109831), Symbol('x'))), Rational(-12062848561, 4096)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_51(c:sympy.Rational):
	#c < 83581391/16777216

	pre_cond = StrictLessThan(Symbol('c'), Rational(83581391, 16777216))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_52(c:sympy.Rational):
	#(x**2 < 52613600921/67108864) & (8192*c + 227909*x < -51942512281/8192)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(52613600921, 67108864)), StrictLessThan(Add(Mul(Integer(8192), Symbol('c')), Mul(Integer(227909), Symbol('x'))), Rational(-51942512281, 8192)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_53(c:sympy.Rational):
	#c < 334342503/67108864

	pre_cond = StrictLessThan(Symbol('c'), Rational(334342503, 67108864))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_54(c:sympy.Rational):
	#(x**2 < 881857121/1048576) & (1024*c + 29519*x < -871371361/1024)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(881857121, 1048576)), StrictLessThan(Add(Mul(Integer(1024), Symbol('c')), Mul(Integer(29519), Symbol('x'))), Rational(-871371361, 1024)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_55(c:sympy.Rational):
	#c < 5224863/1048576

	pre_cond = StrictLessThan(Symbol('c'), Rational(5224863, 1048576))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_56(c:sympy.Rational):
	#(x**2 < 60398049521/67108864) & (8192*c + 244391*x < -59726960881/8192)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(60398049521, 67108864)), StrictLessThan(Add(Mul(Integer(8192), Symbol('c')), Mul(Integer(244391), Symbol('x'))), Rational(-59726960881, 8192)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_57(c:sympy.Rational):
	#c < 334571279/67108864

	pre_cond = StrictLessThan(Symbol('c'), Rational(334571279, 67108864))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_58(c:sympy.Rational):
	#(x**2 < 257966969585/268435456) & (16384*c + 505255*x < -255282615025/16384)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(257966969585, 268435456)), StrictLessThan(Add(Mul(Integer(16384), Symbol('c')), Mul(Integer(505255), Symbol('x'))), Rational(-255282615025, 16384)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_59(c:sympy.Rational):
	#c < 1338420495/268435456

	pre_cond = StrictLessThan(Symbol('c'), Rational(1338420495, 268435456))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_60(c:sympy.Rational):
	#(x**2 < 68719549961/67108864) & (8192*c + 260861*x < -68048461321/8192)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(68719549961, 67108864)), StrictLessThan(Add(Mul(Integer(8192), Symbol('c')), Mul(Integer(260861), Symbol('x'))), Rational(-68048461321, 8192)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_61(c:sympy.Rational):
	#c < 334684663/67108864

	pre_cond = StrictLessThan(Symbol('c'), Rational(334684663, 67108864))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_62(c:sympy.Rational):
	#(x**2 < 4567599569/4194304) & (2048*c + 67273*x < -4525656529/2048)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(4567599569, 4194304)), StrictLessThan(Add(Mul(Integer(2048), Symbol('c')), Mul(Integer(67273), Symbol('x'))), Rational(-4525656529, 2048)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_63(c:sympy.Rational):
	#c < 20921903/4194304

	pre_cond = StrictLessThan(Symbol('c'), Rational(20921903, 4194304))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_64(c:sympy.Rational):
	#(x**2 < 1241246192329/1073741824) & (32768*c + 1109283*x < -1230508774089/32768)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(1241246192329, 1073741824)), StrictLessThan(Add(Mul(Integer(32768), Symbol('c')), Mul(Integer(1109283), Symbol('x'))), Rational(-1230508774089, 32768)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_65(c:sympy.Rational):
	#c < 5356727607/1073741824

	pre_cond = StrictLessThan(Symbol('c'), Rational(5356727607, 1073741824))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_66(c:sympy.Rational):
	#(x**2 < 328833853585/268435456) & (16384*c + 571095*x < -326149499025/16384)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(328833853585, 268435456)), StrictLessThan(Add(Mul(Integer(16384), Symbol('c')), Mul(Integer(571095), Symbol('x'))), Rational(-326149499025, 16384)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_67(c:sympy.Rational):
	#c < 1339217775/268435456

	pre_cond = StrictLessThan(Symbol('c'), Rational(1339217775, 268435456))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_68(c:sympy.Rational):
	#(x**2 < 1391571576161/1073741824) & (32768*c + 1175089*x < -1380834157921/32768)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(1391571576161, 1073741824)), StrictLessThan(Add(Mul(Integer(32768), Symbol('c')), Mul(Integer(1175089), Symbol('x'))), Rational(-1380834157921, 32768)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_69(c:sympy.Rational):
	#c < 5357230751/1073741824

	pre_cond = StrictLessThan(Symbol('c'), Rational(5357230751, 1073741824))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_70(c:sympy.Rational):
	#(x**2 < 91872068665/67108864) & (8192*c + 301995*x < -91200980025/8192)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(91872068665, 67108864)), StrictLessThan(Add(Mul(Integer(8192), Symbol('c')), Mul(Integer(301995), Symbol('x'))), Rational(-91200980025, 8192)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_71(c:sympy.Rational):
	#c < 334912455/67108864

	pre_cond = StrictLessThan(Symbol('c'), Rational(334912455, 67108864))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_72(c:sympy.Rational):
	#(x**2 < 1550483366465/1073741824) & (32768*c + 1240865*x < -1539745948225/32768)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(1550483366465, 1073741824)), StrictLessThan(Add(Mul(Integer(32768), Symbol('c')), Mul(Integer(1240865), Symbol('x'))), Rational(-1539745948225, 32768)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_73(c:sympy.Rational):
	#c < 5359295935/1073741824

	pre_cond = StrictLessThan(Symbol('c'), Rational(5359295935, 1073741824))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_74(c:sympy.Rational):
	#(x**2 < 26130589322369/17179869184) & (131072*c + 5094977*x < -25958790630529/131072)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(26130589322369, 17179869184)), StrictLessThan(Add(Mul(Integer(131072), Symbol('c')), Mul(Integer(5094977), Symbol('x'))), Rational(-25958790630529, 131072)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_75(c:sympy.Rational):
	#c < 85753557887/17179869184

	pre_cond = StrictLessThan(Symbol('c'), Rational(85753557887, 17179869184))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_76(c:sympy.Rational):
	#(x**2 < 429497004041/268435456) & (16384*c + 653309*x < -426812649481/16384)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(429497004041, 268435456)), StrictLessThan(Add(Mul(Integer(16384), Symbol('c')), Mul(Integer(653309), Symbol('x'))), Rational(-426812649481, 16384)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_77(c:sympy.Rational):
	#c < 1339936759/268435456

	pre_cond = StrictLessThan(Symbol('c'), Rational(1339936759, 268435456))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_78(c:sympy.Rational):
	#(x**2 < 451240040609/268435456) & (16384*c + 669743*x < -448555686049/16384)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(451240040609, 268435456)), StrictLessThan(Add(Mul(Integer(16384), Symbol('c')), Mul(Integer(669743), Symbol('x'))), Rational(-448555686049, 16384)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_79(c:sympy.Rational):
	#c < 1340155743/268435456

	pre_cond = StrictLessThan(Symbol('c'), Rational(1340155743, 268435456))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_80(c:sympy.Rational):
	#(x**2 < 30305300073041/17179869184) & (131072*c + 5489399*x < -30133501381201/131072)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(30305300073041, 17179869184)), StrictLessThan(Add(Mul(Integer(131072), Symbol('c')), Mul(Integer(5489399), Symbol('x'))), Rational(-30133501381201, 131072)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_81(c:sympy.Rational):
	#c < 85771859375/17179869184

	pre_cond = StrictLessThan(Symbol('c'), Rational(85771859375, 17179869184))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_82(c:sympy.Rational):
	#(x**2 < 1985349751921/1073741824) & (32768*c + 1405209*x < -1974612333681/32768)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(1985349751921, 1073741824)), StrictLessThan(Add(Mul(Integer(32768), Symbol('c')), Mul(Integer(1405209), Symbol('x'))), Rational(-1974612333681, 32768)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_83(c:sympy.Rational):
	#c < 5360872335/1073741824

	pre_cond = StrictLessThan(Symbol('c'), Rational(5360872335, 1073741824))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_84(c:sympy.Rational):
	#(x**2 < 8120177681/4194304) & (2048*c + 89879*x < -8078234641/2048)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(8120177681, 4194304)), StrictLessThan(Add(Mul(Integer(2048), Symbol('c')), Mul(Integer(89879), Symbol('x'))), Rational(-8078234641, 2048)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_85(c:sympy.Rational):
	#c < 20941807/4194304

	pre_cond = StrictLessThan(Symbol('c'), Rational(20941807, 4194304))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_86(c:sympy.Rational):
	#(x**2 < 2174328355465/1073741824) & (32768*c + 1470915*x < -2163590937225/32768)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(2174328355465, 1073741824)), StrictLessThan(Add(Mul(Integer(32768), Symbol('c')), Mul(Integer(1470915), Symbol('x'))), Rational(-2163590937225, 32768)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_87(c:sympy.Rational):
	#c < 5361485175/1073741824

	pre_cond = StrictLessThan(Symbol('c'), Rational(5361485175, 1073741824))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_88(c:sympy.Rational):
	#(x**2 < 9088156298585/4294967296) & (65536*c + 3007525*x < -9045206625625/65536)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(9088156298585, 4294967296)), StrictLessThan(Add(Mul(Integer(65536), Symbol('c')), Mul(Integer(3007525), Symbol('x'))), Rational(-9045206625625, 65536)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_89(c:sympy.Rational):
	#c < 21446660775/4294967296

	pre_cond = StrictLessThan(Symbol('c'), Rational(21446660775, 4294967296))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_90(c:sympy.Rational):
	#(x**2 < 9487587816329/4294967296) & (65536*c + 3073213*x < -9444638143369/65536)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(9487587816329, 4294967296)), StrictLessThan(Add(Mul(Integer(65536), Symbol('c')), Mul(Integer(3073213), Symbol('x'))), Rational(-9444638143369, 65536)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_91(c:sympy.Rational):
	#c < 21447953527/4294967296

	pre_cond = StrictLessThan(Symbol('c'), Rational(21447953527, 4294967296))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_92(c:sympy.Rational):
	#(x**2 < 2473901304049/1073741824) & (32768*c + 1569447*x < -2463163885809/32768)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(2473901304049, 1073741824)), StrictLessThan(Add(Mul(Integer(32768), Symbol('c')), Mul(Integer(1569447), Symbol('x'))), Rational(-2463163885809, 32768)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_93(c:sympy.Rational):
	#c < 5362800399/1073741824

	pre_cond = StrictLessThan(Symbol('c'), Rational(5362800399, 1073741824))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_94(c:sympy.Rational):
	#(x**2 < 2578054639465/1073741824) & (32768*c + 1602285*x < -2567317221225/32768)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(2578054639465, 1073741824)), StrictLessThan(Add(Mul(Integer(32768), Symbol('c')), Mul(Integer(1602285), Symbol('x'))), Rational(-2567317221225, 32768)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_95(c:sympy.Rational):
	#c < 5362847895/1073741824

	pre_cond = StrictLessThan(Symbol('c'), Rational(5362847895, 1073741824))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_96(c:sympy.Rational):
	#(x**2 < 10485761065/4194304) & (2048*c + 102195*x < -10443818025/2048)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(10485761065, 4194304)), StrictLessThan(Add(Mul(Integer(2048), Symbol('c')), Mul(Integer(102195), Symbol('x'))), Rational(-10443818025, 2048)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_97(c:sympy.Rational):
	#c < 20949975/4194304

	pre_cond = StrictLessThan(Symbol('c'), Rational(20949975, 4194304))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_98(c:sympy.Rational):
	#(x**2 < 11171211841985/4294967296) & (65536*c + 3335905*x < -11128262169025/65536)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(11171211841985, 4294967296)), StrictLessThan(Add(Mul(Integer(65536), Symbol('c')), Mul(Integer(3335905), Symbol('x'))), Rational(-11128262169025, 65536)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_99(c:sympy.Rational):
	#c < 21453205055/4294967296

	pre_cond = StrictLessThan(Symbol('c'), Rational(21453205055, 4294967296))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_100(c:sympy.Rational):
	#(x**2 < 11613594122185/4294967296) & (65536*c + 3401565*x < -11570644449225/65536)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(11613594122185, 4294967296)), StrictLessThan(Add(Mul(Integer(65536), Symbol('c')), Mul(Integer(3401565), Symbol('x'))), Rational(-11570644449225, 65536)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_101(c:sympy.Rational):
	#c < 21453670455/4294967296

	pre_cond = StrictLessThan(Symbol('c'), Rational(21453670455, 4294967296))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_102(c:sympy.Rational):
	#(x**2 < 754035262585/268435456) & (16384*c + 866805*x < -751350908025/16384)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(754035262585, 268435456)), StrictLessThan(Add(Mul(Integer(16384), Symbol('c')), Mul(Integer(866805), Symbol('x'))), Rational(-751350908025, 16384)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_103(c:sympy.Rational):
	#c < 1340947335/268435456

	pre_cond = StrictLessThan(Symbol('c'), Rational(1340947335, 268435456))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_104(c:sympy.Rational):
	#(x**2 < 200386006546649/68719476736) & (262144*c + 14131483*x < -199698811779289/262144)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(200386006546649, 68719476736)), StrictLessThan(Add(Mul(Integer(262144), Symbol('c')), Mul(Integer(14131483), Symbol('x'))), Rational(-199698811779289, 262144)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_105(c:sympy.Rational):
	#c < 343296116519/68719476736

	pre_cond = StrictLessThan(Symbol('c'), Rational(343296116519, 68719476736))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_106(c:sympy.Rational):
	#(x**2 < 51969111483065/17179869184) & (131072*c + 7197035*x < -51797312791225/131072)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(51969111483065, 17179869184)), StrictLessThan(Add(Mul(Integer(131072), Symbol('c')), Mul(Integer(7197035), Symbol('x'))), Rational(-51797312791225, 131072)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_107(c:sympy.Rational):
	#c < 85824642375/17179869184

	pre_cond = StrictLessThan(Symbol('c'), Rational(85824642375, 17179869184))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_108(c:sympy.Rational):
	#(x**2 < 13153338065/4194304) & (2048*c + 114505*x < -13111395025/2048)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(13153338065, 4194304)), StrictLessThan(Add(Mul(Integer(2048), Symbol('c')), Mul(Integer(114505), Symbol('x'))), Rational(-13111395025, 2048)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_109(c:sympy.Rational):
	#c < 20954415/4194304

	pre_cond = StrictLessThan(Symbol('c'), Rational(20954415, 4194304))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_110(c:sympy.Rational):
	#(x**2 < 13954350253361/4294967296) & (65536*c + 3729799*x < -13911400580401/65536)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(13954350253361, 4294967296)), StrictLessThan(Add(Mul(Integer(65536), Symbol('c')), Mul(Integer(3729799), Symbol('x'))), Rational(-13911400580401, 65536)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_111(c:sympy.Rational):
	#c < 21457533647/4294967296

	pre_cond = StrictLessThan(Symbol('c'), Rational(21457533647, 4294967296))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_112(c:sympy.Rational):
	#(x**2 < 231172333104529/68719476736) & (262144*c + 15181737*x < -230485138337169/262144)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(231172333104529, 68719476736)), StrictLessThan(Add(Mul(Integer(262144), Symbol('c')), Mul(Integer(15181737), Symbol('x'))), Rational(-230485138337169, 262144)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_113(c:sympy.Rational):
	#c < 343334982255/68719476736

	pre_cond = StrictLessThan(Symbol('c'), Rational(343334982255, 68719476736))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_114(c:sympy.Rational):
	#(x**2 < 239212516157585/68719476736) & (262144*c + 15444265*x < -238525321390225/262144)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(239212516157585, 68719476736)), StrictLessThan(Add(Mul(Integer(262144), Symbol('c')), Mul(Integer(15444265), Symbol('x'))), Rational(-238525321390225, 262144)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_115(c:sympy.Rational):
	#c < 343341455215/68719476736

	pre_cond = StrictLessThan(Symbol('c'), Rational(343341455215, 68719476736))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_116(c:sympy.Rational):
	#(x**2 < 15461883295985/4294967296) & (65536*c + 3926695*x < -15418933623025/65536)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(15461883295985, 4294967296)), StrictLessThan(Add(Mul(Integer(65536), Symbol('c')), Mul(Integer(3926695), Symbol('x'))), Rational(-15418933623025, 65536)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_117(c:sympy.Rational):
	#c < 21459388175/4294967296

	pre_cond = StrictLessThan(Symbol('c'), Rational(21459388175, 4294967296))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_118(c:sympy.Rational):
	#(x**2 < 255705194301449/68719476736) & (262144*c + 15969283*x < -255017999534089/262144)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(255705194301449, 68719476736)), StrictLessThan(Add(Mul(Integer(262144), Symbol('c')), Mul(Integer(15969283), Symbol('x'))), Rational(-255017999534089, 262144)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_119(c:sympy.Rational):
	#c < 343355553783/68719476736

	pre_cond = StrictLessThan(Symbol('c'), Rational(343355553783, 68719476736))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_120(c:sympy.Rational):
	#(x**2 < 66039420488609/17179869184) & (131072*c + 8115887*x < -65867621796769/131072)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(66039420488609, 17179869184)), StrictLessThan(Add(Mul(Integer(131072), Symbol('c')), Mul(Integer(8115887), Symbol('x'))), Rational(-65867621796769, 131072)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_121(c:sympy.Rational):
	#c < 85841736799/17179869184

	pre_cond = StrictLessThan(Symbol('c'), Rational(85841736799, 17179869184))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_122(c:sympy.Rational):
	#(x**2 < 68186902445969/17179869184) & (131072*c + 8247127*x < -68015103754129/131072)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(68186902445969, 17179869184)), StrictLessThan(Add(Mul(Integer(131072), Symbol('c')), Mul(Integer(8247127), Symbol('x'))), Rational(-68015103754129, 131072)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_123(c:sympy.Rational):
	#c < 85844344943/17179869184

	pre_cond = StrictLessThan(Symbol('c'), Rational(85844344943, 17179869184))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_124(c:sympy.Rational):
	#(x**2 < 17592187123721/4294967296) & (65536*c + 4189181*x < -17549237450761/65536)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(17592187123721, 4294967296)), StrictLessThan(Add(Mul(Integer(65536), Symbol('c')), Mul(Integer(4189181), Symbol('x'))), Rational(-17549237450761, 65536)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_125(c:sympy.Rational):
	#c < 21461174263/4294967296

	pre_cond = StrictLessThan(Symbol('c'), Rational(21461174263, 4294967296))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_126(c:sympy.Rational):
	#(x**2 < 1134139917161/268435456) & (16384*c + 1063699*x < -1131455562601/16384)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(1134139917161, 268435456)), StrictLessThan(Add(Mul(Integer(16384), Symbol('c')), Mul(Integer(1063699), Symbol('x'))), Rational(-1131455562601, 16384)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_127(c:sympy.Rational):
	#c < 1341324439/268435456

	pre_cond = StrictLessThan(Symbol('c'), Rational(1341324439, 268435456))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_128(c:sympy.Rational):
	#(x**2 < 74835517119329/17179869184) & (131072*c + 8640817*x < -74663718427489/131072)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(74835517119329, 17179869184)), StrictLessThan(Add(Mul(Integer(131072), Symbol('c')), Mul(Integer(8640817), Symbol('x'))), Rational(-74663718427489, 131072)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_129(c:sympy.Rational):
	#c < 85846516895/17179869184

	pre_cond = StrictLessThan(Symbol('c'), Rational(85846516895, 17179869184))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_130(c:sympy.Rational):
	#(x**2 < 308481762372985/68719476736) & (262144*c + 17544075*x < -307794567605625/262144)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(308481762372985, 68719476736)), StrictLessThan(Add(Mul(Integer(262144), Symbol('c')), Mul(Integer(17544075), Symbol('x'))), Rational(-307794567605625, 262144)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_131(c:sympy.Rational):
	#c < 343390179975/68719476736

	pre_cond = StrictLessThan(Symbol('c'), Rational(343390179975, 68719476736))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_132(c:sympy.Rational):
	#(x**2 < 317758886308409/68719476736) & (262144*c + 17806507*x < -317071691541049/262144)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(317758886308409, 68719476736)), StrictLessThan(Add(Mul(Integer(262144), Symbol('c')), Mul(Integer(17806507), Symbol('x'))), Rational(-317071691541049, 262144)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_133(c:sympy.Rational):
	#c < 343398487495/68719476736

	pre_cond = StrictLessThan(Symbol('c'), Rational(343398487495, 68719476736))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_134(c:sympy.Rational):
	#(x**2 < 327173462250121/68719476736) & (262144*c + 18068931*x < -326486267482761/262144)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(327173462250121, 68719476736)), StrictLessThan(Add(Mul(Integer(262144), Symbol('c')), Mul(Integer(18068931), Symbol('x'))), Rational(-326486267482761, 262144)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_135(c:sympy.Rational):
	#c < 343400033655/68719476736

	pre_cond = StrictLessThan(Symbol('c'), Rational(343400033655, 68719476736))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_136(c:sympy.Rational):
	#(x**2 < 84181360234769/17179869184) & (131072*c + 9165673*x < -84009561542929/131072)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(84181360234769, 17179869184)), StrictLessThan(Add(Mul(Integer(131072), Symbol('c')), Mul(Integer(9165673), Symbol('x'))), Rational(-84009561542929, 131072)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_137(c:sympy.Rational):
	#c < 85854858991/17179869184

	pre_cond = StrictLessThan(Symbol('c'), Rational(85854858991, 17179869184))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_138(c:sympy.Rational):
	#(x**2 < 86603720644969/17179869184) & (131072*c + 9296877*x < -86431921953129/131072)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(86603720644969, 17179869184)), StrictLessThan(Add(Mul(Integer(131072), Symbol('c')), Mul(Integer(9296877), Symbol('x'))), Rational(-86431921953129, 131072)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_139(c:sympy.Rational):
	#c < 85856659095/17179869184

	pre_cond = StrictLessThan(Symbol('c'), Rational(85856659095, 17179869184))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_140(c:sympy.Rational):
	#(x**2 < 356241776151385/68719476736) & (262144*c + 18856155*x < -355554581384025/262144)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(356241776151385, 68719476736)), StrictLessThan(Add(Mul(Integer(262144), Symbol('c')), Mul(Integer(18856155), Symbol('x'))), Rational(-355554581384025, 262144)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_141(c:sympy.Rational):
	#c < 343427151015/68719476736

	pre_cond = StrictLessThan(Symbol('c'), Rational(343427151015, 68719476736))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_142(c:sympy.Rational):
	#(x**2 < 5859297617175785/1099511627776) & (1048576*c + 76474195*x < -5848302500898025/1048576)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(5859297617175785, 1099511627776)), StrictLessThan(Add(Mul(Integer(1048576), Symbol('c')), Mul(Integer(76474195), Symbol('x'))), Rational(-5848302500898025, 1048576)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_143(c:sympy.Rational):
	#c < 5494900333335/1099511627776

	pre_cond = StrictLessThan(Symbol('c'), Rational(5494900333335, 1099511627776))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_144(c:sympy.Rational):
	#(x**2 < 1505231422490081/274877906944) & (524288*c + 38761871*x < -1502482643420641/524288)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(1505231422490081, 274877906944)), StrictLessThan(Add(Mul(Integer(524288), Symbol('c')), Mul(Integer(38761871), Symbol('x'))), Rational(-1502482643420641, 524288)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_145(c:sympy.Rational):
	#c < 1373759470111/274877906944

	pre_cond = StrictLessThan(Symbol('c'), Rational(1373759470111, 274877906944))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_146(c:sympy.Rational):
	#(x**2 < 24159191140201/4294967296) & (65536*c + 4910829*x < -24116241467241/65536)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(24159191140201, 4294967296)), StrictLessThan(Add(Mul(Integer(65536), Symbol('c')), Mul(Integer(4910829), Symbol('x'))), Rational(-24116241467241, 65536)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_147(c:sympy.Rational):
	#c < 21465233559/4294967296

	pre_cond = StrictLessThan(Symbol('c'), Rational(21465233559, 4294967296))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_148(c:sympy.Rational):
	#(x**2 < 6350779185540881/1099511627776) & (1048576*c + 79622761*x < -6339784069263121/1048576)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(6350779185540881, 1099511627776)), StrictLessThan(Add(Mul(Integer(1048576), Symbol('c')), Mul(Integer(79622761), Symbol('x'))), Rational(-6339784069263121, 1048576)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_149(c:sympy.Rational):
	#c < 5495164850415/1099511627776

	pre_cond = StrictLessThan(Symbol('c'), Rational(5495164850415, 1099511627776))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_150(c:sympy.Rational):
	#(x**2 < 1629751113707129/274877906944) & (524288*c + 40336117*x < -1627002334637689/524288)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(1629751113707129, 274877906944)), StrictLessThan(Add(Mul(Integer(524288), Symbol('c')), Mul(Integer(40336117), Symbol('x'))), Rational(-1627002334637689, 524288)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_151(c:sympy.Rational):
	#c < 1373807808903/274877906944

	pre_cond = StrictLessThan(Symbol('c'), Rational(1373807808903, 274877906944))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_152(c:sympy.Rational):
	#(x**2 < 418089297004601/68719476736) & (262144*c + 20430421*x < -417402102237241/262144)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(418089297004601, 68719476736)), StrictLessThan(Add(Mul(Integer(262144), Symbol('c')), Mul(Integer(20430421), Symbol('x'))), Rational(-417402102237241, 262144)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_153(c:sympy.Rational):
	#c < 343455807431/68719476736

	pre_cond = StrictLessThan(Symbol('c'), Rational(343455807431, 68719476736))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_154(c:sympy.Rational):
	#(x**2 < 107219564031161/17179869184) & (131072*c + 10346389*x < -107047765339321/131072)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(107219564031161, 17179869184)), StrictLessThan(Add(Mul(Integer(131072), Symbol('c')), Mul(Integer(10346389), Symbol('x'))), Rational(-107047765339321, 131072)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_155(c:sympy.Rational):
	#c < 85864682311/17179869184

	pre_cond = StrictLessThan(Symbol('c'), Rational(85864682311, 17179869184))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_156(c:sympy.Rational):
	#(x**2 < 7036874521707121/1099511627776) & (1048576*c + 83820519*x < -7025879405429361/1048576)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(7036874521707121, 1099511627776)), StrictLessThan(Add(Mul(Integer(1048576), Symbol('c')), Mul(Integer(83820519), Symbol('x'))), Rational(-7025879405429361, 1048576)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_157(c:sympy.Rational):
	#c < 5495357046159/1099511627776

	pre_cond = StrictLessThan(Symbol('c'), Rational(5495357046159, 1099511627776))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_158(c:sympy.Rational):
	#(x**2 < 7213895890986785/1099511627776) & (1048576*c + 84869905*x < -7202900774709025/1048576)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(7213895890986785, 1099511627776)), StrictLessThan(Add(Mul(Integer(1048576), Symbol('c')), Mul(Integer(84869905), Symbol('x'))), Rational(-7202900774709025, 1048576)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_159(c:sympy.Rational):
	#c < 5495411218655/1099511627776

	pre_cond = StrictLessThan(Symbol('c'), Rational(5495411218655, 1099511627776))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_160(c:sympy.Rational):
	#(x**2 < 7393116245449201/1099511627776) & (1048576*c + 85919271*x < -7382121129171441/1048576)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(7393116245449201, 1099511627776)), StrictLessThan(Add(Mul(Integer(1048576), Symbol('c')), Mul(Integer(85919271), Symbol('x'))), Rational(-7382121129171441, 1048576)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_161(c:sympy.Rational):
	#c < 5495482492431/1099511627776

	pre_cond = StrictLessThan(Symbol('c'), Rational(5495482492431, 1099511627776))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_162(c:sympy.Rational):
	#(x**2 < 1893633908276921/274877906944) & (524288*c + 43484309*x < -1890885129207481/524288)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(1893633908276921, 274877906944)), StrictLessThan(Add(Mul(Integer(524288), Symbol('c')), Mul(Integer(43484309), Symbol('x'))), Rational(-1890885129207481, 524288)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_163(c:sympy.Rational):
	#c < 1373886742855/274877906944

	pre_cond = StrictLessThan(Symbol('c'), Rational(1373886742855, 274877906944))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_164(c:sympy.Rational):
	#(x**2 < 7758154110372569/1099511627776) & (1048576*c + 88017947*x < -7747158994094809/1048576)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(7758154110372569, 1099511627776)), StrictLessThan(Add(Mul(Integer(1048576), Symbol('c')), Mul(Integer(88017947), Symbol('x'))), Rational(-7747158994094809, 1048576)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_165(c:sympy.Rational):
	#c < 5495576556839/1099511627776

	pre_cond = StrictLessThan(Symbol('c'), Rational(5495576556839, 1099511627776))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_166(c:sympy.Rational):
	#(x**2 < 1985992890979081/274877906944) & (524288*c + 44533629*x < -1983244111909641/524288)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(1985992890979081, 274877906944)), StrictLessThan(Add(Mul(Integer(524288), Symbol('c')), Mul(Integer(44533629), Symbol('x'))), Rational(-1983244111909641, 524288)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_167(c:sympy.Rational):
	#c < 1373906988279/274877906944

	pre_cond = StrictLessThan(Symbol('c'), Rational(1373906988279, 274877906944))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_168(c:sympy.Rational):
	#(x**2 < 127062313447601/17179869184) & (131072*c + 11264569*x < -126890514755761/131072)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(127062313447601, 17179869184)), StrictLessThan(Add(Mul(Integer(131072), Symbol('c')), Mul(Integer(11264569), Symbol('x'))), Rational(-126890514755761, 131072)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_169(c:sympy.Rational):
	#c < 85869809487/17179869184

	pre_cond = StrictLessThan(Symbol('c'), Rational(85869809487, 17179869184))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_170(c:sympy.Rational):
	#(x**2 < 33288814338803321/4398046511104) & (2097152*c + 182331659*x < -33244833873692281/2097152)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(33288814338803321, 4398046511104)), StrictLessThan(Add(Mul(Integer(2097152), Symbol('c')), Mul(Integer(182331659), Symbol('x'))), Rational(-33244833873692281, 2097152)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_171(c:sympy.Rational):
	#c < 21982816467335/4398046511104

	pre_cond = StrictLessThan(Symbol('c'), Rational(21982816467335, 4398046511104))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_172(c:sympy.Rational):
	#(x**2 < 8514618124416041/1099511627776) & (1048576*c + 92215091*x < -8503623008138281/1048576)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(8514618124416041, 1099511627776)), StrictLessThan(Add(Mul(Integer(1048576), Symbol('c')), Mul(Integer(92215091), Symbol('x'))), Rational(-8503623008138281, 1048576)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_173(c:sympy.Rational):
	#c < 5495742778327/1099511627776

	pre_cond = StrictLessThan(Symbol('c'), Rational(5495742778327, 1099511627776))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_174(c:sympy.Rational):
	#(x**2 < 8709231672327329/1099511627776) & (1048576*c + 93264337*x < -8698236556049569/1048576)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(8709231672327329, 1099511627776)), StrictLessThan(Add(Mul(Integer(1048576), Symbol('c')), Mul(Integer(93264337), Symbol('x'))), Rational(-8698236556049569, 1048576)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_175(c:sympy.Rational):
	#c < 5495787586399/1099511627776

	pre_cond = StrictLessThan(Symbol('c'), Rational(5495787586399, 1099511627776))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_176(c:sympy.Rational):
	#(x**2 < 8697308813641/1073741824) & (32768*c + 2947299*x < -8686571395401/32768)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(8697308813641, 1073741824)), StrictLessThan(Add(Mul(Integer(32768), Symbol('c')), Mul(Integer(2947299), Symbol('x'))), Rational(-8686571395401, 32768)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_177(c:sympy.Rational):
	#c < 5367031479/1073741824

	pre_cond = StrictLessThan(Symbol('c'), Rational(5367031479, 1073741824))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_178(c:sympy.Rational):
	#(x**2 < 9105055879233985/1099511627776) & (1048576*c + 95362785*x < -9094060762956225/1048576)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(9105055879233985, 1099511627776)), StrictLessThan(Add(Mul(Integer(1048576), Symbol('c')), Mul(Integer(95362785), Symbol('x'))), Rational(-9094060762956225, 1048576)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_179(c:sympy.Rational):
	#c < 5495852662335/1099511627776

	pre_cond = StrictLessThan(Symbol('c'), Rational(5495852662335, 1099511627776))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_180(c:sympy.Rational):
	#(x**2 < 581641659149369/68719476736) & (262144*c + 24102997*x < -580954464382009/262144)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(581641659149369, 68719476736)), StrictLessThan(Add(Mul(Integer(262144), Symbol('c')), Mul(Integer(24102997), Symbol('x'))), Rational(-580954464382009, 262144)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_181(c:sympy.Rational):
	#c < 343491810247/68719476736

	pre_cond = StrictLessThan(Symbol('c'), Rational(343491810247, 68719476736))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_182(c:sympy.Rational):
	#(x**2 < 9509676138503089/1099511627776) & (1048576*c + 97461177*x < -9498681022225329/1048576)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(9509676138503089, 1099511627776)), StrictLessThan(Add(Mul(Integer(1048576), Symbol('c')), Mul(Integer(97461177), Symbol('x'))), Rational(-9498681022225329, 1048576)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_183(c:sympy.Rational):
	#c < 5495933232207/1099511627776

	pre_cond = StrictLessThan(Symbol('c'), Rational(5495933232207, 1099511627776))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_184(c:sympy.Rational):
	#(x**2 < 9715284764462369/1099511627776) & (1048576*c + 98510353*x < -9704289648184609/1048576)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(9715284764462369, 1099511627776)), StrictLessThan(Add(Mul(Integer(1048576), Symbol('c')), Mul(Integer(98510353), Symbol('x'))), Rational(-9704289648184609, 1048576)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_185(c:sympy.Rational):
	#c < 5495991104223/1099511627776

	pre_cond = StrictLessThan(Symbol('c'), Rational(5495991104223, 1099511627776))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_186(c:sympy.Rational):
	#(x**2 < 39692369767966129/4398046511104) & (2097152*c + 199119033*x < -39648389302855089/2097152)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(39692369767966129, 4398046511104)), StrictLessThan(Add(Mul(Integer(2097152), Symbol('c')), Mul(Integer(199119033), Symbol('x'))), Rational(-39648389302855089, 2097152)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_187(c:sympy.Rational):
	#c < 21984135076431/4398046511104

	pre_cond = StrictLessThan(Symbol('c'), Rational(21984135076431, 4398046511104))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_188(c:sympy.Rational):
	#(x**2 < 633318699563249/68719476736) & (262144*c + 25152167*x < -632631504795889/262144)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(633318699563249, 68719476736)), StrictLessThan(Add(Mul(Integer(262144), Symbol('c')), Mul(Integer(25152167), Symbol('x'))), Rational(-632631504795889, 262144)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_189(c:sympy.Rational):
	#c < 343503144719/68719476736

	pre_cond = StrictLessThan(Symbol('c'), Rational(343503144719, 68719476736))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_190(c:sympy.Rational):
	#(x**2 < 41381219767939265/4398046511104) & (2097152*c + 203315615*x < -41337239302828225/2097152)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(41381219767939265, 4398046511104)), StrictLessThan(Add(Mul(Integer(2097152), Symbol('c')), Mul(Integer(203315615), Symbol('x'))), Rational(-41337239302828225, 2097152)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_191(c:sympy.Rational):
	#c < 21984314134335/4398046511104

	pre_cond = StrictLessThan(Symbol('c'), Rational(21984314134335, 4398046511104))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_192(c:sympy.Rational):
	#(x**2 < 42238838864315681/4398046511104) & (2097152*c + 205413871*x < -42194858399204641/2097152)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(42238838864315681, 4398046511104)), StrictLessThan(Add(Mul(Integer(2097152), Symbol('c')), Mul(Integer(205413871), Symbol('x'))), Rational(-42194858399204641, 2097152)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_193(c:sympy.Rational):
	#c < 21984419543775/4398046511104

	pre_cond = StrictLessThan(Symbol('c'), Rational(21984419543775, 4398046511104))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_194(c:sympy.Rational):
	#(x**2 < 43105254186642065/4398046511104) & (2097152*c + 207512105*x < -43061273721531025/2097152)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(43105254186642065, 4398046511104)), StrictLessThan(Add(Mul(Integer(2097152), Symbol('c')), Mul(Integer(207512105), Symbol('x'))), Rational(-43061273721531025, 2097152)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_195(c:sympy.Rational):
	#c < 21984454940015/4398046511104

	pre_cond = StrictLessThan(Symbol('c'), Rational(21984454940015, 4398046511104))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_196(c:sympy.Rational):
	#(x**2 < 43980465457951529/4398046511104) & (2097152*c + 209610317*x < -43936484992840489/2097152)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(43980465457951529, 4398046511104)), StrictLessThan(Add(Mul(Integer(2097152), Symbol('c')), Mul(Integer(209610317), Symbol('x'))), Rational(-43936484992840489, 2097152)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_197(c:sympy.Rational):
	#c < 21984558877911/4398046511104

	pre_cond = StrictLessThan(Symbol('c'), Rational(21984558877911, 4398046511104))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_198(c:sympy.Rational):
	#(x**2 < 2804029551543569/274877906944) & (524288*c + 52927127*x < -2801280772474129/524288)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(2804029551543569, 274877906944)), StrictLessThan(Add(Mul(Integer(524288), Symbol('c')), Mul(Integer(52927127), Symbol('x'))), Rational(-2801280772474129, 524288)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_199(c:sympy.Rational):
	#c < 1374041144047/274877906944

	pre_cond = StrictLessThan(Symbol('c'), Rational(1374041144047, 274877906944))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_200(c:sympy.Rational):
	#(x**2 < 11439319005626681/1099511627776) & (1048576*c + 106903339*x < -11428323889348921/1048576)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(11439319005626681, 1099511627776)), StrictLessThan(Add(Mul(Integer(1048576), Symbol('c')), Mul(Integer(106903339), Symbol('x'))), Rational(-11428323889348921, 1048576)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_201(c:sympy.Rational):
	#c < 5496221368007/1099511627776

	pre_cond = StrictLessThan(Symbol('c'), Rational(5496221368007, 1099511627776))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_202(c:sympy.Rational):
	#(x**2 < 46658875650630281/4398046511104) & (2097152*c + 215904829*x < -46614895185519241/2097152)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(46658875650630281, 4398046511104)), StrictLessThan(Add(Mul(Integer(2097152), Symbol('c')), Mul(Integer(215904829), Symbol('x'))), Rational(-46614895185519241, 2097152)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_203(c:sympy.Rational):
	#c < 21984941022583/4398046511104

	pre_cond = StrictLessThan(Symbol('c'), Rational(21984941022583, 4398046511104))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_204(c:sympy.Rational):
	#(x**2 < 47569271469878561/4398046511104) & (2097152*c + 218002961*x < -47525291004767521/2097152)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(47569271469878561, 4398046511104)), StrictLessThan(Add(Mul(Integer(2097152), Symbol('c')), Mul(Integer(218002961), Symbol('x'))), Rational(-47525291004767521, 2097152)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_205(c:sympy.Rational):
	#c < 21984944607967/4398046511104

	pre_cond = StrictLessThan(Symbol('c'), Rational(21984944607967, 4398046511104))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_206(c:sympy.Rational):
	#(x**2 < 12122115810266129/1099511627776) & (1048576*c + 110050537*x < -12111120693988369/1048576)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(12122115810266129, 1099511627776)), StrictLessThan(Add(Mul(Integer(1048576), Symbol('c')), Mul(Integer(110050537), Symbol('x'))), Rational(-12111120693988369, 1048576)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_207(c:sympy.Rational):
	#c < 5496253969391/1099511627776

	pre_cond = StrictLessThan(Symbol('c'), Rational(5496253969391, 1099511627776))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_208(c:sympy.Rational):
	#(x**2 < 3016140791321/268435456) & (16384*c + 1735931*x < -3013456436761/16384)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(3016140791321, 268435456)), StrictLessThan(Add(Mul(Integer(16384), Symbol('c')), Mul(Integer(1735931), Symbol('x'))), Rational(-3013456436761, 16384)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_209(c:sympy.Rational):
	#c < 1341874663/268435456

	pre_cond = StrictLessThan(Symbol('c'), Rational(1341874663, 268435456))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_210(c:sympy.Rational):
	#(x**2 < 50353234579701065/4398046511104) & (2097152*c + 224297245*x < -50309254114590025/2097152)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(50353234579701065, 4398046511104)), StrictLessThan(Add(Mul(Integer(2097152), Symbol('c')), Mul(Integer(224297245), Symbol('x'))), Rational(-50309254114590025, 2097152)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_211(c:sympy.Rational):
	#c < 21985391657655/4398046511104

	pre_cond = StrictLessThan(Symbol('c'), Rational(21985391657655, 4398046511104))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_212(c:sympy.Rational):
	#(x**2 < 51298814591154065/4398046511104) & (2097152*c + 226395305*x < -51254834126043025/2097152)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(51298814591154065, 4398046511104)), StrictLessThan(Add(Mul(Integer(2097152), Symbol('c')), Mul(Integer(226395305), Symbol('x'))), Rational(-51254834126043025, 2097152)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_213(c:sympy.Rational):
	#c < 21985474463855/4398046511104

	pre_cond = StrictLessThan(Symbol('c'), Rational(21985474463855, 4398046511104))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_214(c:sympy.Rational):
	#(x**2 < 209012763095413969/17592186044416) & (4194304*c + 456986697*x < -208836841234969809/4194304)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(209012763095413969, 17592186044416)), StrictLessThan(Add(Mul(Integer(4194304), Symbol('c')), Mul(Integer(456986697), Symbol('x'))), Rational(-208836841234969809, 4194304)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_215(c:sympy.Rational):
	#c < 87942062983983/17592186044416

	pre_cond = StrictLessThan(Symbol('c'), Rational(87942062983983, 17592186044416))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_216(c:sympy.Rational):
	#(x**2 < 212865451680372161/17592186044416) & (4194304*c + 461182751*x < -212689529819928001/4194304)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(212865451680372161, 17592186044416)), StrictLessThan(Add(Mul(Integer(4194304), Symbol('c')), Mul(Integer(461182751), Symbol('x'))), Rational(-212689529819928001, 4194304)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_217(c:sympy.Rational):
	#c < 87942477605439/17592186044416

	pre_cond = StrictLessThan(Symbol('c'), Rational(87942477605439, 17592186044416))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_218(c:sympy.Rational):
	#(x**2 < 54188331287546809/4398046511104) & (2097152*c + 232689387*x < -54144350822435769/2097152)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(54188331287546809, 4398046511104)), StrictLessThan(Add(Mul(Integer(2097152), Symbol('c')), Mul(Integer(232689387), Symbol('x'))), Rational(-54144350822435769, 2097152)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_219(c:sympy.Rational):
	#c < 21985656730695/4398046511104

	pre_cond = StrictLessThan(Symbol('c'), Rational(21985656730695, 4398046511104))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_220(c:sympy.Rational):
	#(x**2 < 55169095681099729/4398046511104) & (2097152*c + 234787383*x < -55125115215988689/2097152)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(55169095681099729, 4398046511104)), StrictLessThan(Add(Mul(Integer(2097152), Symbol('c')), Mul(Integer(234787383), Symbol('x'))), Rational(-55125115215988689, 2097152)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_221(c:sympy.Rational):
	#c < 21985725331503/4398046511104

	pre_cond = StrictLessThan(Symbol('c'), Rational(21985725331503, 4398046511104))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_222(c:sympy.Rational):
	#(x**2 < 3509916008907721/274877906944) & (524288*c + 59221341*x < -3507167229838281/524288)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(3509916008907721, 274877906944)), StrictLessThan(Add(Mul(Integer(524288), Symbol('c')), Mul(Integer(59221341), Symbol('x'))), Rational(-3507167229838281, 524288)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_223(c:sympy.Rational):
	#c < 1374112775223/274877906944

	pre_cond = StrictLessThan(Symbol('c'), Rational(1374112775223, 274877906944))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_224(c:sympy.Rational):
	#(x**2 < 14289253120749985/1099511627776) & (1048576*c + 119491665*x < -14278258004472225/1048576)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(14289253120749985, 1099511627776)), StrictLessThan(Add(Mul(Integer(1048576), Symbol('c')), Mul(Integer(119491665), Symbol('x'))), Rational(-14278258004472225, 1048576)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_225(c:sympy.Rational):
	#c < 5496497098335/1099511627776

	pre_cond = StrictLessThan(Symbol('c'), Rational(5496497098335, 1099511627776))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_226(c:sympy.Rational):
	#(x**2 < 232656660947823385/17592186044416) & (4194304*c + 482162565*x < -232480739087379225/4194304)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(232656660947823385, 17592186044416)), StrictLessThan(Add(Mul(Integer(4194304), Symbol('c')), Mul(Integer(482162565), Symbol('x'))), Rational(-232480739087379225, 4194304)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_227(c:sympy.Rational):
	#c < 87944041043175/17592186044416

	pre_cond = StrictLessThan(Symbol('c'), Rational(87944041043175, 17592186044416))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_228(c:sympy.Rational):
	#(x**2 < 59180113991277881/4398046511104) & (2097152*c + 243179221*x < -59136133526166841/2097152)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(59180113991277881, 4398046511104)), StrictLessThan(Add(Mul(Integer(2097152), Symbol('c')), Mul(Integer(243179221), Symbol('x'))), Rational(-59136133526166841, 2097152)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_229(c:sympy.Rational):
	#c < 21986076549831/4398046511104

	pre_cond = StrictLessThan(Symbol('c'), Rational(21986076549831, 4398046511104))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_230(c:sympy.Rational):
	#(x**2 < 15051214703754089/1099511627776) & (1048576*c + 122638573*x < -15040219587476329/1048576)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(15051214703754089, 1099511627776)), StrictLessThan(Add(Mul(Integer(1048576), Symbol('c')), Mul(Integer(122638573), Symbol('x'))), Rational(-15040219587476329, 1048576)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_231(c:sympy.Rational):
	#c < 5496538203287/1099511627776

	pre_cond = StrictLessThan(Symbol('c'), Rational(5496538203287, 1099511627776))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_232(c:sympy.Rational):
	#(x**2 < 15309599946403601/1099511627776) & (1048576*c + 123687529*x < -15298604830125841/1048576)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(15309599946403601, 1099511627776)), StrictLessThan(Add(Mul(Integer(1048576), Symbol('c')), Mul(Integer(123687529), Symbol('x'))), Rational(-15298604830125841, 1048576)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_233(c:sympy.Rational):
	#c < 5496550101231/1099511627776

	pre_cond = StrictLessThan(Symbol('c'), Rational(5496550101231, 1099511627776))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_234(c:sympy.Rational):
	#(x**2 < 62280736739434889/4398046511104) & (2097152*c + 249472957*x < -62236756274323849/2097152)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(62280736739434889, 4398046511104)), StrictLessThan(Add(Mul(Integer(2097152), Symbol('c')), Mul(Integer(249472957), Symbol('x'))), Rational(-62236756274323849, 2097152)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_235(c:sympy.Rational):
	#c < 21986301173367/4398046511104

	pre_cond = StrictLessThan(Symbol('c'), Rational(21986301173367, 4398046511104))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_236(c:sympy.Rational):
	#(x**2 < 253327479057650129/17592186044416) & (4194304*c + 503141687*x < -253151557197205969/4194304)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(253327479057650129, 17592186044416)), StrictLessThan(Add(Mul(Integer(4194304), Symbol('c')), Mul(Integer(503141687), Symbol('x'))), Rational(-253151557197205969, 4194304)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_237(c:sympy.Rational):
	#c < 87945644895791/17592186044416

	pre_cond = StrictLessThan(Symbol('c'), Rational(87945644895791, 17592186044416))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_238(c:sympy.Rational):
	#(x**2 < 1030268785339342769/70368744177664) & (8388608*c + 1014674873*x < -1029565097897566129/8388608)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(1030268785339342769, 70368744177664)), StrictLessThan(Add(Mul(Integer(8388608), Symbol('c')), Mul(Integer(1014674873), Symbol('x'))), Rational(-1029565097897566129, 8388608)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_239(c:sympy.Rational):
	#c < 351782705094735/70368744177664

	pre_cond = StrictLessThan(Symbol('c'), Rational(351782705094735, 70368744177664))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_240(c:sympy.Rational):
	#(x**2 < 65460524421540601/4398046511104) & (2097152*c + 255766581*x < -65416543956429561/2097152)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(65460524421540601, 4398046511104)), StrictLessThan(Add(Mul(Integer(2097152), Symbol('c')), Mul(Integer(255766581), Symbol('x'))), Rational(-65416543956429561, 2097152)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_241(c:sympy.Rational):
	#c < 21986462602503/4398046511104

	pre_cond = StrictLessThan(Symbol('c'), Rational(21986462602503, 4398046511104))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_242(c:sympy.Rational):
	#(x**2 < 259914241233569/17179869184) & (131072*c + 16116527*x < -259742442541729/131072)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(259914241233569, 17179869184)), StrictLessThan(Add(Mul(Integer(131072), Symbol('c')), Mul(Integer(16116527), Symbol('x'))), Rational(-259742442541729, 131072)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_243(c:sympy.Rational):
	#c < 85884972383/17179869184

	pre_cond = StrictLessThan(Symbol('c'), Rational(85884972383, 17179869184))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_244(c:sympy.Rational):
	#(x**2 < 66039417313001/4294967296) & (65536*c + 8123821*x < -65996467640041/65536)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(66039417313001, 4294967296)), StrictLessThan(Add(Mul(Integer(65536), Symbol('c')), Mul(Integer(8123821), Symbol('x'))), Rational(-65996467640041, 65536)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_245(c:sympy.Rational):
	#c < 21471258903/4294967296

	pre_cond = StrictLessThan(Symbol('c'), Rational(21471258903, 4294967296))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_246(c:sympy.Rational):
	#(x**2 < 68719477001241241/4398046511104) & (2097152*c + 262060101*x < -68675496536130201/2097152)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(68719477001241241, 4398046511104)), StrictLessThan(Add(Mul(Integer(2097152), Symbol('c')), Mul(Integer(262060101), Symbol('x'))), Rational(-68675496536130201, 2097152)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_247(c:sympy.Rational):
	#c < 21986580413799/4398046511104

	pre_cond = StrictLessThan(Symbol('c'), Rational(21986580413799, 4398046511104))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_248(c:sympy.Rational):
	#(x**2 < 69823386635521601/4398046511104) & (2097152*c + 264157919*x < -69779406170410561/2097152)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(69823386635521601, 4398046511104)), StrictLessThan(Add(Mul(Integer(2097152), Symbol('c')), Mul(Integer(264157919), Symbol('x'))), Rational(-69779406170410561, 2097152)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_249(c:sympy.Rational):
	#c < 21986656072127/4398046511104

	pre_cond = StrictLessThan(Symbol('c'), Rational(21986656072127, 4398046511104))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_250(c:sympy.Rational):
	#(x**2 < 283744369436615369/17592186044416) & (4194304*c + 532511453*x < -283568447576171209/4194304)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(283744369436615369, 17592186044416)), StrictLessThan(Add(Mul(Integer(4194304), Symbol('c')), Mul(Integer(532511453), Symbol('x'))), Rational(-283568447576171209, 4194304)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_251(c:sympy.Rational):
	#c < 87946929020215/17592186044416

	pre_cond = StrictLessThan(Symbol('c'), Rational(87946929020215, 17592186044416))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_252(c:sympy.Rational):
	#(x**2 < 4503599644270601/274877906944) & (524288*c + 67088381*x < -4500850865201161/524288)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(4503599644270601, 274877906944)), StrictLessThan(Add(Mul(Integer(524288), Symbol('c')), Mul(Integer(67088381), Symbol('x'))), Rational(-4500850865201161, 524288)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_253(c:sympy.Rational):
	#c < 1374171308023/274877906944

	pre_cond = StrictLessThan(Symbol('c'), Rational(1374171308023, 274877906944))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_254(c:sympy.Rational):
	#(x**2 < 73187892086729761/4398046511104) & (2097152*c + 270451311*x < -73143911621618721/2097152)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(73187892086729761, 4398046511104)), StrictLessThan(Add(Mul(Integer(2097152), Symbol('c')), Mul(Integer(270451311), Symbol('x'))), Rational(-73143911621618721, 2097152)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_255(c:sympy.Rational):
	#c < 21986880230367/4398046511104

	pre_cond = StrictLessThan(Symbol('c'), Rational(21986880230367, 4398046511104))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_256(c:sympy.Rational):
	#(x**2 < 297307944429167489/17592186044416) & (4194304*c + 545098177*x < -297132022568723329/4194304)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(297307944429167489, 17592186044416)), StrictLessThan(Add(Mul(Integer(4194304), Symbol('c')), Mul(Integer(545098177), Symbol('x'))), Rational(-297132022568723329, 4194304)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_257(c:sympy.Rational):
	#c < 87947775171711/17592186044416

	pre_cond = StrictLessThan(Symbol('c'), Rational(87947775171711, 17592186044416))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_258(c:sympy.Rational):
	#(x**2 < 301899505001770529/17592186044416) & (4194304*c + 549293713*x < -301723583141326369/4194304)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(301899505001770529, 17592186044416)), StrictLessThan(Add(Mul(Integer(4194304), Symbol('c')), Mul(Integer(549293713), Symbol('x'))), Rational(-301723583141326369, 4194304)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_259(c:sympy.Rational):
	#c < 87947965682143/17592186044416

	pre_cond = StrictLessThan(Symbol('c'), Rational(87947965682143, 17592186044416))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_260(c:sympy.Rational):
	#(x**2 < 1226105000559705161/70368744177664) & (8388608*c + 1106978461*x < -1225401313117928521/8388608)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(1226105000559705161, 70368744177664)), StrictLessThan(Add(Mul(Integer(8388608), Symbol('c')), Mul(Integer(1106978461), Symbol('x'))), Rational(-1225401313117928521, 8388608)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_261(c:sympy.Rational):
	#c < 351792220013495/70368744177664

	pre_cond = StrictLessThan(Symbol('c'), Rational(351792220013495, 70368744177664))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_262(c:sympy.Rational):
	#(x**2 < 1244752717511729321/70368744177664) & (8388608*c + 1115369459*x < -1244049030069952681/8388608)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(1244752717511729321, 70368744177664)), StrictLessThan(Add(Mul(Integer(8388608), Symbol('c')), Mul(Integer(1115369459), Symbol('x'))), Rational(-1244049030069952681, 8388608)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_263(c:sympy.Rational):
	#c < 351793104215895/70368744177664

	pre_cond = StrictLessThan(Symbol('c'), Rational(351793104215895, 70368744177664))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_264(c:sympy.Rational):
	#(x**2 < 315885293373848681/17592186044416) & (4194304*c + 561880211*x < -315709371513404521/4194304)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(315885293373848681, 17592186044416)), StrictLessThan(Add(Mul(Integer(4194304), Symbol('c')), Mul(Integer(561880211), Symbol('x'))), Rational(-315709371513404521, 4194304)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_265(c:sympy.Rational):
	#c < 87948300026775/17592186044416

	pre_cond = StrictLessThan(Symbol('c'), Rational(87948300026775, 17592186044416))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_266(c:sympy.Rational):
	#(x**2 < 320617591687149785/17592186044416) & (4194304*c + 566075675*x < -320441669826705625/4194304)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(320617591687149785, 17592186044416)), StrictLessThan(Add(Mul(Integer(4194304), Symbol('c')), Mul(Integer(566075675), Symbol('x'))), Rational(-320441669826705625, 4194304)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_267(c:sympy.Rational):
	#c < 87948347246375/17592186044416

	pre_cond = StrictLessThan(Symbol('c'), Rational(87948347246375, 17592186044416))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_268(c:sympy.Rational):
	#(x**2 < 81346268611895761/4398046511104) & (2097152*c + 285135561*x < -81302288146784721/2097152)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(81346268611895761, 4398046511104)), StrictLessThan(Add(Mul(Integer(2097152), Symbol('c')), Mul(Integer(285135561), Symbol('x'))), Rational(-81302288146784721, 2097152)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_269(c:sympy.Rational):
	#c < 21987088244271/4398046511104

	pre_cond = StrictLessThan(Symbol('c'), Rational(21987088244271, 4398046511104))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_270(c:sympy.Rational):
	#(x**2 < 5159183456675201/274877906944) & (524288*c + 71808319*x < -5156434677605761/524288)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(5159183456675201, 274877906944)), StrictLessThan(Add(Mul(Integer(524288), Symbol('c')), Mul(Integer(71808319), Symbol('x'))), Rational(-5156434677605761, 524288)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_271(c:sympy.Rational):
	#c < 1374195800703/274877906944

	pre_cond = StrictLessThan(Symbol('c'), Rational(1374195800703, 274877906944))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_272(c:sympy.Rational):
	#(x**2 < 335025591598105385/17592186044416) & (4194304*c + 578661965*x < -334849669737661225/4194304)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(335025591598105385, 17592186044416)), StrictLessThan(Add(Mul(Integer(4194304), Symbol('c')), Mul(Integer(578661965), Symbol('x'))), Rational(-334849669737661225, 4194304)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_273(c:sympy.Rational):
	#c < 87949096074455/17592186044416

	pre_cond = StrictLessThan(Symbol('c'), Rational(87949096074455, 17592186044416))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_274(c:sympy.Rational):
	#(x**2 < 339898627463757929/17592186044416) & (4194304*c + 582857363*x < -339722705603313769/4194304)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(339898627463757929, 17592186044416)), StrictLessThan(Add(Mul(Integer(4194304), Symbol('c')), Mul(Integer(582857363), Symbol('x'))), Rational(-339722705603313769, 4194304)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_275(c:sympy.Rational):
	#c < 87949096075159/17592186044416

	pre_cond = StrictLessThan(Symbol('c'), Rational(87949096075159, 17592186044416))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_276(c:sympy.Rational):
	#(x**2 < 344806847272479185/17592186044416) & (4194304*c + 587052745*x < -344630925412035025/4194304)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(344806847272479185, 17592186044416)), StrictLessThan(Add(Mul(Integer(4194304), Symbol('c')), Mul(Integer(587052745), Symbol('x'))), Rational(-344630925412035025, 4194304)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_277(c:sympy.Rational):
	#c < 87949306992175/17592186044416

	pre_cond = StrictLessThan(Symbol('c'), Rational(87949306992175, 17592186044416))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_278(c:sympy.Rational):
	#(x**2 < 1366211921109409/68719476736) & (262144*c + 36953007*x < -1365524726342049/262144)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(1366211921109409, 68719476736)), StrictLessThan(Add(Mul(Integer(262144), Symbol('c')), Mul(Integer(36953007), Symbol('x'))), Rational(-1365524726342049, 262144)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_279(c:sympy.Rational):
	#c < 343552106079/68719476736

	pre_cond = StrictLessThan(Symbol('c'), Rational(343552106079, 68719476736))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_280(c:sympy.Rational):
	#(x**2 < 5542638135636929/274877906944) & (524288*c + 74430433*x < -5539889356567489/524288)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(5542638135636929, 274877906944)), StrictLessThan(Add(Mul(Integer(524288), Symbol('c')), Mul(Integer(74430433), Symbol('x'))), Rational(-5539889356567489, 524288)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_281(c:sympy.Rational):
	#c < 1374209084479/274877906944

	pre_cond = StrictLessThan(Symbol('c'), Rational(1374209084479, 274877906944))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_282(c:sympy.Rational):
	#(x**2 < 359742613525161761/17592186044416) & (4194304*c + 599638801*x < -359566691664717601/4194304)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(359742613525161761, 17592186044416)), StrictLessThan(Add(Mul(Integer(4194304), Symbol('c')), Mul(Integer(599638801), Symbol('x'))), Rational(-359566691664717601, 4194304)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_283(c:sympy.Rational):
	#c < 87949622581471/17592186044416

	pre_cond = StrictLessThan(Symbol('c'), Rational(87949622581471, 17592186044416))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_284(c:sympy.Rational):
	#(x**2 < 22799473197955721/1099511627776) & (1048576*c + 150958531*x < -22788478081677961/1048576)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(22799473197955721, 1099511627776)), StrictLessThan(Add(Mul(Integer(1048576), Symbol('c')), Mul(Integer(150958531), Symbol('x'))), Rational(-22788478081677961, 1048576)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_285(c:sympy.Rational):
	#c < 5496852989303/1099511627776

	pre_cond = StrictLessThan(Symbol('c'), Rational(5496852989303, 1099511627776))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_286(c:sympy.Rational):
	#(x**2 < 5779308000604481/274877906944) & (524288*c + 76003679*x < -5776559221535041/524288)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(5779308000604481, 274877906944)), StrictLessThan(Add(Mul(Integer(524288), Symbol('c')), Mul(Integer(76003679), Symbol('x'))), Rational(-5776559221535041, 524288)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_287(c:sympy.Rational):
	#c < 1374222519999/274877906944

	pre_cond = StrictLessThan(Symbol('c'), Rational(1374222519999, 274877906944))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_288(c:sympy.Rational):
	#(x**2 < 374995038210668689/17592186044416) & (4194304*c + 612224727*x < -374819116350224529/4194304)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(374995038210668689, 17592186044416)), StrictLessThan(Add(Mul(Integer(4194304), Symbol('c')), Mul(Integer(612224727), Symbol('x'))), Rational(-374819116350224529, 4194304)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_289(c:sympy.Rational):
	#c < 87950367606639/17592186044416

	pre_cond = StrictLessThan(Symbol('c'), Rational(87950367606639, 17592186044416))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_290(c:sympy.Rational):
	#(x**2 < 1520598194958336929/70368744177664) & (8388608*c + 1232840017*x < -1519894507516560289/8388608)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(1520598194958336929, 70368744177664)), StrictLessThan(Add(Mul(Integer(8388608), Symbol('c')), Mul(Integer(1232840017), Symbol('x'))), Rational(-1519894507516560289, 8388608)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_291(c:sympy.Rational):
	#c < 351801994411103/70368744177664

	pre_cond = StrictLessThan(Symbol('c'), Rational(351801994411103, 70368744177664))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_292(c:sympy.Rational):
	#(x**2 < 1541356973142462449/70368744177664) & (8388608*c + 1241230553*x < -1540653285700685809/8388608)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(1541356973142462449, 70368744177664)), StrictLessThan(Add(Mul(Integer(8388608), Symbol('c')), Mul(Integer(1241230553), Symbol('x'))), Rational(-1540653285700685809, 8388608)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_293(c:sympy.Rational):
	#c < 351803216867343/70368744177664

	pre_cond = StrictLessThan(Symbol('c'), Rational(351803216867343, 70368744177664))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_294(c:sympy.Rational):
	#(x**2 < 24410257672410449/1099511627776) & (1048576*c + 156202633*x < -24399262556132689/1048576)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(24410257672410449, 1099511627776)), StrictLessThan(Add(Mul(Integer(1048576), Symbol('c')), Mul(Integer(156202633), Symbol('x'))), Rational(-24399262556132689, 1048576)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_295(c:sympy.Rational):
	#c < 5496926857903/1099511627776

	pre_cond = StrictLessThan(Symbol('c'), Rational(5496926857903, 1099511627776))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_296(c:sympy.Rational):
	#(x**2 < 1583296744859156041/70368744177664) & (8388608*c + 1258011549*x < -1582593057417379401/8388608)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(1583296744859156041, 70368744177664)), StrictLessThan(Add(Mul(Integer(8388608), Symbol('c')), Mul(Integer(1258011549), Symbol('x'))), Rational(-1582593057417379401, 8388608)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_297(c:sympy.Rational):
	#c < 351804187689399/70368744177664

	pre_cond = StrictLessThan(Symbol('c'), Rational(351804187689399, 70368744177664))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_298(c:sympy.Rational):
	#(x**2 < 6417910948429658921/281474976710656) & (16777216*c + 2532804019*x < -6415096198662552361/16777216)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(6417910948429658921, 281474976710656)), StrictLessThan(Add(Mul(Integer(16777216), Symbol('c')), Mul(Integer(2532804019), Symbol('x'))), Rational(-6415096198662552361, 16777216)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_299(c:sympy.Rational):
	#c < 1407218314544343/281474976710656

	pre_cond = StrictLessThan(Symbol('c'), Rational(1407218314544343, 281474976710656))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_300(c:sympy.Rational):
	#(x**2 < 6503197866182588441/281474976710656) & (16777216*c + 2549584891*x < -6500383116415481881/16777216)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(6503197866182588441, 281474976710656)), StrictLessThan(Add(Mul(Integer(16777216), Symbol('c')), Mul(Integer(2549584891), Symbol('x'))), Rational(-6500383116415481881, 16777216)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_301(c:sympy.Rational):
	#c < 1407220434323431/281474976710656

	pre_cond = StrictLessThan(Symbol('c'), Rational(1407220434323431, 281474976710656))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_302(c:sympy.Rational):
	#(x**2 < 411815483626706201/17592186044416) & (4194304*c + 641591429*x < -411639561766262041/4194304)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(411815483626706201, 17592186044416)), StrictLessThan(Add(Mul(Integer(4194304), Symbol('c')), Mul(Integer(641591429), Symbol('x'))), Rational(-411639561766262041, 4194304)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_303(c:sympy.Rational):
	#c < 87951277861607/17592186044416

	pre_cond = StrictLessThan(Symbol('c'), Rational(87951277861607, 17592186044416))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_304(c:sympy.Rational):
	#(x**2 < 417216284306188289/17592186044416) & (4194304*c + 645786623*x < -417040362445744129/4194304)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(417216284306188289, 17592186044416)), StrictLessThan(Add(Mul(Integer(4194304), Symbol('c')), Mul(Integer(645786623), Symbol('x'))), Rational(-417040362445744129, 4194304)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_305(c:sympy.Rational):
	#c < 87951617546239/17592186044416

	pre_cond = StrictLessThan(Symbol('c'), Rational(87951617546239, 17592186044416))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_306(c:sympy.Rational):
	#(x**2 < 105663067497866449/4398046511104) & (2097152*c + 324990903*x < -105619087032755409/2097152)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(105663067497866449, 4398046511104)), StrictLessThan(Add(Mul(Integer(2097152), Symbol('c')), Mul(Integer(324990903), Symbol('x'))), Rational(-105619087032755409, 2097152)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_307(c:sympy.Rational):
	#c < 21987909524271/4398046511104

	pre_cond = StrictLessThan(Symbol('c'), Rational(21987909524271, 4398046511104))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_308(c:sympy.Rational):
	#(x**2 < 1712493759005918665/70368744177664) & (8388608*c + 1308353955*x < -1711790071564142025/8388608)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(1712493759005918665, 70368744177664)), StrictLessThan(Add(Mul(Integer(8388608), Symbol('c')), Mul(Integer(1308353955), Symbol('x'))), Rational(-1711790071564142025, 8388608)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_309(c:sympy.Rational):
	#c < 351807220021815/70368744177664

	pre_cond = StrictLessThan(Symbol('c'), Rational(351807220021815, 70368744177664))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_310(c:sympy.Rational):
	#(x**2 < 108407448488783801/4398046511104) & (2097152*c + 329186069*x < -108363468023672761/2097152)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(108407448488783801, 4398046511104)), StrictLessThan(Add(Mul(Integer(2097152), Symbol('c')), Mul(Integer(329186069), Symbol('x'))), Rational(-108363468023672761, 2097152)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_311(c:sympy.Rational):
	#c < 21987983478855/4398046511104

	pre_cond = StrictLessThan(Symbol('c'), Rational(21987983478855, 4398046511104))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_312(c:sympy.Rational):
	#(x**2 < 7026741322509367361/281474976710656) & (16777216*c + 2650269151*x < -7023926572742260801/16777216)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(7026741322509367361, 281474976710656)), StrictLessThan(Add(Mul(Integer(16777216), Symbol('c')), Mul(Integer(2650269151), Symbol('x'))), Rational(-7023926572742260801, 16777216)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_313(c:sympy.Rational):
	#c < 1407231962990527/281474976710656

	pre_cond = StrictLessThan(Symbol('c'), Rational(1407231962990527, 281474976710656))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_314(c:sympy.Rational):
	#(x**2 < 7115968889375892409/281474976710656) & (16777216*c + 2667049707*x < -7113154139608785849/16777216)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(7115968889375892409, 281474976710656)), StrictLessThan(Add(Mul(Integer(16777216), Symbol('c')), Mul(Integer(2667049707), Symbol('x'))), Rational(-7113154139608785849, 16777216)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_315(c:sympy.Rational):
	#c < 1407234106252359/281474976710656

	pre_cond = StrictLessThan(Symbol('c'), Rational(1407234106252359, 281474976710656))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_316(c:sympy.Rational):
	#(x**2 < 1801439852571918961/70368744177664) & (8388608*c + 1341915111*x < -1800736165130142321/8388608)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(1801439852571918961, 70368744177664)), StrictLessThan(Add(Mul(Integer(8388608), Symbol('c')), Mul(Integer(1341915111), Symbol('x'))), Rational(-1800736165130142321, 8388608)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_317(c:sympy.Rational):
	#c < 351808542735759/70368744177664

	pre_cond = StrictLessThan(Symbol('c'), Rational(351808542735759, 70368744177664))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_318(c:sympy.Rational):
	#(x**2 < 114001763767448609/4398046511104) & (2097152*c + 337576337*x < -113957783302337569/2097152)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(114001763767448609, 4398046511104)), StrictLessThan(Add(Mul(Integer(2097152), Symbol('c')), Mul(Integer(337576337), Symbol('x'))), Rational(-113957783302337569, 2097152)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_319(c:sympy.Rational):
	#c < 21988034710495/4398046511104

	pre_cond = StrictLessThan(Symbol('c'), Rational(21988034710495, 4398046511104))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_320(c:sympy.Rational):
	#(x**2 < 115422332692190921/4398046511104) & (2097152*c + 339673891*x < -115378352227079881/2097152)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(115422332692190921, 4398046511104)), StrictLessThan(Add(Mul(Integer(2097152), Symbol('c')), Mul(Integer(339673891), Symbol('x'))), Rational(-115378352227079881, 2097152)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_321(c:sympy.Rational):
	#c < 21988109986103/4398046511104

	pre_cond = StrictLessThan(Symbol('c'), Rational(21988109986103, 4398046511104))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_322(c:sympy.Rational):
	#(x**2 < 1869627165370725761/70368744177664) & (8388608*c + 1367085761*x < -1868923477928949121/8388608)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(1869627165370725761, 70368744177664)), StrictLessThan(Add(Mul(Integer(8388608), Symbol('c')), Mul(Integer(1367085761), Symbol('x'))), Rational(-1868923477928949121, 8388608)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_323(c:sympy.Rational):
	#c < 351809950993023/70368744177664

	pre_cond = StrictLessThan(Symbol('c'), Rational(351809950993023, 70368744177664))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_324(c:sympy.Rational):
	#(x**2 < 473159435864689121/17592186044416) & (4194304*c + 687737969*x < -472983514004244961/4194304)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(473159435864689121, 17592186044416)), StrictLessThan(Add(Mul(Integer(4194304), Symbol('c')), Mul(Integer(687737969), Symbol('x'))), Rational(-472983514004244961, 4194304)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_325(c:sympy.Rational):
	#c < 87952745641503/17592186044416

	pre_cond = StrictLessThan(Symbol('c'), Rational(87952745641503, 17592186044416))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_326(c:sympy.Rational):
	#(x**2 < 7663156241935695809/281474976710656) & (16777216*c + 2767732193*x < -7660341492168589249/16777216)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(7663156241935695809, 281474976710656)), StrictLessThan(Add(Mul(Integer(16777216), Symbol('c')), Mul(Integer(2767732193), Symbol('x'))), Rational(-7660341492168589249, 16777216)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_327(c:sympy.Rational):
	#c < 1407245130334271/281474976710656

	pre_cond = StrictLessThan(Symbol('c'), Rational(1407245130334271, 281474976710656))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_328(c:sympy.Rational):
	#(x**2 < 7756324462059682289/281474976710656) & (16777216*c + 2784512473*x < -7753509712292575729/16777216)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(7756324462059682289, 281474976710656)), StrictLessThan(Add(Mul(Integer(16777216), Symbol('c')), Mul(Integer(2784512473), Symbol('x'))), Rational(-7753509712292575729, 16777216)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_329(c:sympy.Rational):
	#c < 1407245267142159/281474976710656

	pre_cond = StrictLessThan(Symbol('c'), Rational(1407245267142159, 281474976710656))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_330(c:sympy.Rational):
	#(x**2 < 490628476905110201/17592186044416) & (4194304*c + 700323179*x < -490452555044666041/4194304)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(490628476905110201, 17592186044416)), StrictLessThan(Add(Mul(Integer(4194304), Symbol('c')), Mul(Integer(700323179), Symbol('x'))), Rational(-490452555044666041, 4194304)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_331(c:sympy.Rational):
	#c < 87952887727431/17592186044416

	pre_cond = StrictLessThan(Symbol('c'), Rational(87952887727431, 17592186044416))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_332(c:sympy.Rational):
	#(x**2 < 1986087435869181161/70368744177664) & (8388608*c + 1409036461*x < -1985383748427404521/8388608)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(1986087435869181161, 70368744177664)), StrictLessThan(Add(Mul(Integer(8388608), Symbol('c')), Mul(Integer(1409036461), Symbol('x'))), Rational(-1985383748427404521, 8388608)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_333(c:sympy.Rational):
	#c < 351812450691863/70368744177664

	pre_cond = StrictLessThan(Symbol('c'), Rational(351812450691863, 70368744177664))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_334(c:sympy.Rational):
	#(x**2 < 32156827245974505209/1125899906842624) & (33554432*c + 5669706187*x < -32145568246906078969/33554432)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(32156827245974505209, 1125899906842624)), StrictLessThan(Add(Mul(Integer(33554432), Symbol('c')), Mul(Integer(5669706187), Symbol('x'))), Rational(-32145568246906078969, 33554432)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_335(c:sympy.Rational):
	#c < 5629003366283527/1125899906842624

	pre_cond = StrictLessThan(Symbol('c'), Rational(5629003366283527, 1125899906842624))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_336(c:sympy.Rational):
	#(x**2 < 2033656707051834865/70368744177664) & (8388608*c + 1425816615*x < -2032953019610058225/8388608)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(2033656707051834865, 70368744177664)), StrictLessThan(Add(Mul(Integer(8388608), Symbol('c')), Mul(Integer(1425816615), Symbol('x'))), Rational(-2032953019610058225, 8388608)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_337(c:sympy.Rational):
	#c < 351813120668175/70368744177664

	pre_cond = StrictLessThan(Symbol('c'), Rational(351813120668175, 70368744177664))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_338(c:sympy.Rational):
	#(x**2 < 32922439183323448465/1125899906842624) & (33554432*c + 5736826665*x < -32911180184255022225/33554432)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(32922439183323448465, 1125899906842624)), StrictLessThan(Add(Mul(Integer(33554432), Symbol('c')), Mul(Integer(5736826665), Symbol('x'))), Rational(-32911180184255022225, 33554432)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_339(c:sympy.Rational):
	#c < 5629014481484655/1125899906842624

	pre_cond = StrictLessThan(Symbol('c'), Rational(5629014481484655, 1125899906842624))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_340(c:sympy.Rational):
	#(x**2 < 33308622855304987049/1125899906842624) & (33554432*c + 5770386803*x < -33297363856236560809/33554432)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(33308622855304987049, 1125899906842624)), StrictLessThan(Add(Mul(Integer(33554432), Symbol('c')), Mul(Integer(5770386803), Symbol('x'))), Rational(-33297363856236560809, 33554432)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_341(c:sympy.Rational):
	#c < 5629018096713303/1125899906842624

	pre_cond = StrictLessThan(Symbol('c'), Rational(5629018096713303, 1125899906842624))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_342(c:sympy.Rational):
	#(x**2 < 8424264578820699529/281474976710656) & (16777216*c + 2901973437*x < -8421449829053592969/16777216)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(8424264578820699529, 281474976710656)), StrictLessThan(Add(Mul(Integer(16777216), Symbol('c')), Mul(Integer(2901973437), Symbol('x'))), Rational(-8421449829053592969, 16777216)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_343(c:sympy.Rational):
	#c < 1407256880777847/281474976710656

	pre_cond = StrictLessThan(Symbol('c'), Rational(1407256880777847, 281474976710656))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_344(c:sympy.Rational):
	#(x**2 < 34087745584790774401/1125899906842624) & (33554432*c + 5837506881*x < -34076486585722348161/33554432)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(34087745584790774401, 1125899906842624)), StrictLessThan(Add(Mul(Integer(33554432), Symbol('c')), Mul(Integer(5837506881), Symbol('x'))), Rational(-34076486585722348161, 33554432)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_345(c:sympy.Rational):
	#c < 5629031997758847/1125899906842624

	pre_cond = StrictLessThan(Symbol('c'), Rational(5629031997758847, 1125899906842624))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_346(c:sympy.Rational):
	#(x**2 < 538760697670966769/17592186044416) & (4194304*c + 733883353*x < -538584775810522609/4194304)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(538760697670966769, 17592186044416)), StrictLessThan(Add(Mul(Integer(4194304), Symbol('c')), Mul(Integer(733883353), Symbol('x'))), Rational(-538584775810522609, 4194304)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_347(c:sympy.Rational):
	#c < 87953718206991/17592186044416

	pre_cond = StrictLessThan(Symbol('c'), Rational(87953718206991, 17592186044416))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_348(c:sympy.Rational):
	#(x**2 < 34875875524467583265/1125899906842624) & (33554432*c + 5904626705*x < -34864616525399157025/33554432)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(34875875524467583265, 1125899906842624)), StrictLessThan(Add(Mul(Integer(33554432), Symbol('c')), Mul(Integer(5904626705), Symbol('x'))), Rational(-34864616525399157025, 33554432)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_349(c:sympy.Rational):
	#c < 5629040062797535/1125899906842624

	pre_cond = StrictLessThan(Symbol('c'), Rational(5629040062797535, 1125899906842624))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_350(c:sympy.Rational):
	#(x**2 < 2204582387055226801/70368744177664) & (8388608*c + 1484546631*x < -2203878699613450161/8388608)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(2204582387055226801, 70368744177664)), StrictLessThan(Add(Mul(Integer(8388608), Symbol('c')), Mul(Integer(1484546631), Symbol('x'))), Rational(-2203878699613450161, 8388608)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_351(c:sympy.Rational):
	#c < 351815283347535/70368744177664

	pre_cond = StrictLessThan(Symbol('c'), Rational(351815283347535, 70368744177664))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_352(c:sympy.Rational):
	#(x**2 < 8918253163912312441/281474976710656) & (16777216*c + 2985873141*x < -8915438414145205881/16777216)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(8918253163912312441, 281474976710656)), StrictLessThan(Add(Mul(Integer(16777216), Symbol('c')), Mul(Integer(2985873141), Symbol('x'))), Rational(-8915438414145205881, 16777216)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_353(c:sympy.Rational):
	#c < 1407262912465287/281474976710656

	pre_cond = StrictLessThan(Symbol('c'), Rational(1407262912465287, 281474976710656))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_354(c:sympy.Rational):
	#(x**2 < 36074958924502798601/1125899906842624) & (33554432*c + 6005305981*x < -36063699925434372361/33554432)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(36074958924502798601, 1125899906842624)), StrictLessThan(Add(Mul(Integer(33554432), Symbol('c')), Mul(Integer(6005305981), Symbol('x'))), Rational(-36063699925434372361, 33554432)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_355(c:sympy.Rational):
	#c < 5629055545372407/1125899906842624

	pre_cond = StrictLessThan(Symbol('c'), Rational(5629055545372407, 1125899906842624))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_356(c:sympy.Rational):
	#(x**2 < 9119789249910468281/281474976710656) & (16777216*c + 3019432811*x < -9116974500143361721/16777216)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(9119789249910468281, 281474976710656)), StrictLessThan(Add(Mul(Integer(16777216), Symbol('c')), Mul(Integer(3019432811), Symbol('x'))), Rational(-9116974500143361721, 16777216)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_357(c:sympy.Rational):
	#c < 1407264030789959/281474976710656

	pre_cond = StrictLessThan(Symbol('c'), Rational(1407264030789959, 281474976710656))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_358(c:sympy.Rational):
	#(x**2 < 2305350428577679241/70368744177664) & (8388608*c + 1518106301*x < -2304646741135902601/8388608)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(2305350428577679241, 70368744177664)), StrictLessThan(Add(Mul(Integer(8388608), Symbol('c')), Mul(Integer(1518106301), Symbol('x'))), Rational(-2304646741135902601, 8388608)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_359(c:sympy.Rational):
	#c < 351816580937847/70368744177664

	pre_cond = StrictLessThan(Symbol('c'), Rational(351816580937847, 70368744177664))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_360(c:sympy.Rational):
	#(x**2 < 9323577130515399785/281474976710656) & (16777216*c + 3052992365*x < -9320762380748293225/16777216)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(9323577130515399785, 281474976710656)), StrictLessThan(Add(Mul(Integer(16777216), Symbol('c')), Mul(Integer(3052992365), Symbol('x'))), Rational(-9320762380748293225, 16777216)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_361(c:sympy.Rational):
	#c < 1407267671669655/281474976710656

	pre_cond = StrictLessThan(Symbol('c'), Rational(1407267671669655, 281474976710656))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_362(c:sympy.Rational):
	#(x**2 < 589144718481594785/17592186044416) & (4194304*c + 767443025*x < -588968796621150625/4194304)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(589144718481594785, 17592186044416)), StrictLessThan(Add(Mul(Integer(4194304), Symbol('c')), Mul(Integer(767443025), Symbol('x'))), Rational(-588968796621150625, 4194304)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_363(c:sympy.Rational):
	#c < 87954342766175/17592186044416

	pre_cond = StrictLessThan(Symbol('c'), Rational(87954342766175, 17592186044416))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_364(c:sympy.Rational):
	#(x**2 < 145410412799609/4294967296) & (65536*c + 12056843*x < -145367463126649/65536)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(145410412799609, 4294967296)), StrictLessThan(Add(Mul(Integer(65536), Symbol('c')), Mul(Integer(12056843), Symbol('x'))), Rational(-145367463126649, 65536)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_365(c:sympy.Rational):
	#c < 21473237383/4294967296

	pre_cond = StrictLessThan(Symbol('c'), Rational(21473237383, 4294967296))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_366(c:sympy.Rational):
	#(x**2 < 9633481080386063681/281474976710656) & (16777216*c + 3103331489*x < -9630666330618957121/16777216)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(9633481080386063681, 281474976710656)), StrictLessThan(Add(Mul(Integer(16777216), Symbol('c')), Mul(Integer(3103331489), Symbol('x'))), Rational(-9630666330618957121, 16777216)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_367(c:sympy.Rational):
	#c < 1407270833648319/281474976710656

	pre_cond = StrictLessThan(Symbol('c'), Rational(1407270833648319, 281474976710656))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_368(c:sympy.Rational):
	#(x**2 < 9737908294439873009/281474976710656) & (16777216*c + 3120111143*x < -9735093544672766449/16777216)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(9737908294439873009, 281474976710656)), StrictLessThan(Add(Mul(Integer(16777216), Symbol('c')), Mul(Integer(3120111143), Symbol('x'))), Rational(-9735093544672766449, 16777216)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_369(c:sympy.Rational):
	#c < 1407273089160719/281474976710656

	pre_cond = StrictLessThan(Symbol('c'), Rational(1407273089160719, 281474976710656))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_370(c:sympy.Rational):
	#(x**2 < 39371593848355887089/1125899906842624) & (33554432*c + 6273781543*x < -39360334849287460849/33554432)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(39371593848355887089, 1125899906842624)), StrictLessThan(Add(Mul(Integer(33554432), Symbol('c')), Mul(Integer(6273781543), Symbol('x'))), Rational(-39360334849287460849, 33554432)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_371(c:sympy.Rational):
	#c < 5629094025422863/1125899906842624

	pre_cond = StrictLessThan(Symbol('c'), Rational(5629094025422863, 1125899906842624))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_372(c:sympy.Rational):
	#(x**2 < 2487112894403101609/70368744177664) & (8388608*c + 1576835187*x < -2486409206961324969/8388608)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(2487112894403101609, 70368744177664)), StrictLessThan(Add(Mul(Integer(8388608), Symbol('c')), Mul(Integer(1576835187), Symbol('x'))), Rational(-2486409206961324969, 8388608)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_373(c:sympy.Rational):
	#c < 351818736417879/70368744177664

	pre_cond = StrictLessThan(Symbol('c'), Rational(351818736417879, 70368744177664))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_374(c:sympy.Rational):
	#(x**2 < 40218270578933835649/1125899906842624) & (33554432*c + 6340899903*x < -40207011579865409409/33554432)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(40218270578933835649, 1125899906842624)), StrictLessThan(Add(Mul(Integer(33554432), Symbol('c')), Mul(Integer(6340899903), Symbol('x'))), Rational(-40207011579865409409, 33554432)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_375(c:sympy.Rational):
	#c < 5629102184388735/1125899906842624

	pre_cond = StrictLessThan(Symbol('c'), Rational(5629102184388735, 1125899906842624))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_376(c:sympy.Rational):
	#(x**2 < 2480773110579881/68719476736) & (262144*c + 49800461*x < -2480085915812521/262144)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(2480773110579881, 68719476736)), StrictLessThan(Add(Mul(Integer(262144), Symbol('c')), Mul(Integer(49800461), Symbol('x'))), Rational(-2480085915812521, 262144)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_377(c:sympy.Rational):
	#c < 343573380439/68719476736

	pre_cond = StrictLessThan(Symbol('c'), Rational(343573380439, 68719476736))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_378(c:sympy.Rational):
	#(x**2 < 160445134795385681/4398046511104) & (2097152*c + 400501129*x < -160401154330274641/2097152)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(160445134795385681, 4398046511104)), StrictLessThan(Add(Mul(Integer(2097152), Symbol('c')), Mul(Integer(400501129), Symbol('x'))), Rational(-160401154330274641, 2097152)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_379(c:sympy.Rational):
	#c < 21988713485487/4398046511104

	pre_cond = StrictLessThan(Symbol('c'), Rational(21988713485487, 4398046511104))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_380(c:sympy.Rational):
	#(x**2 < 162129586615564529/4398046511104) & (2097152*c + 402598567*x < -162085606150453489/2097152)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(162129586615564529, 4398046511104)), StrictLessThan(Add(Mul(Integer(2097152), Symbol('c')), Mul(Integer(402598567), Symbol('x'))), Rational(-162085606150453489, 2097152)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_381(c:sympy.Rational):
	#c < 21988725933839/4398046511104

	pre_cond = StrictLessThan(Symbol('c'), Rational(21988725933839, 4398046511104))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_382(c:sympy.Rational):
	#(x**2 < 40955708624973761/1099511627776) & (1048576*c + 202348001*x < -40944713508696001/1048576)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(40955708624973761, 1099511627776)), StrictLessThan(Add(Mul(Integer(1048576), Symbol('c')), Mul(Integer(202348001), Symbol('x'))), Rational(-40944713508696001, 1048576)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_383(c:sympy.Rational):
	#c < 5497188143167/1099511627776

	pre_cond = StrictLessThan(Symbol('c'), Rational(5497188143167, 1099511627776))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_384(c:sympy.Rational):
	#(x**2 < 10593592224788592289/281474976710656) & (16777216*c + 3254347473*x < -10590777475021485729/16777216)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(10593592224788592289, 281474976710656)), StrictLessThan(Add(Mul(Integer(16777216), Symbol('c')), Mul(Integer(3254347473), Symbol('x'))), Rational(-10590777475021485729, 16777216)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_385(c:sympy.Rational):
	#c < 1407280732096863/281474976710656

	pre_cond = StrictLessThan(Symbol('c'), Rational(1407280732096863, 281474976710656))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_386(c:sympy.Rational):
	#(x**2 < 10703085991466493209/281474976710656) & (16777216*c + 3271126907*x < -10700271241699386649/16777216)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(10703085991466493209, 281474976710656)), StrictLessThan(Add(Mul(Integer(16777216), Symbol('c')), Mul(Integer(3271126907), Symbol('x'))), Rational(-10700271241699386649, 16777216)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_387(c:sympy.Rational):
	#c < 1407281320041191/281474976710656

	pre_cond = StrictLessThan(Symbol('c'), Rational(1407281320041191, 281474976710656))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_388(c:sympy.Rational):
	#(x**2 < 2703285676427855921/70368744177664) & (8388608*c + 1643953159*x < -2702581988986079281/8388608)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(2703285676427855921, 70368744177664)), StrictLessThan(Add(Mul(Integer(8388608), Symbol('c')), Mul(Integer(1643953159), Symbol('x'))), Rational(-2702581988986079281, 8388608)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_389(c:sympy.Rational):
	#c < 351820771604431/70368744177664

	pre_cond = StrictLessThan(Symbol('c'), Rational(351820771604431, 70368744177664))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_390(c:sympy.Rational):
	#(x**2 < 10923762371817196409/281474976710656) & (16777216*c + 3304685707*x < -10920947622050089849/16777216)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(10923762371817196409, 281474976710656)), StrictLessThan(Add(Mul(Integer(16777216), Symbol('c')), Mul(Integer(3304685707), Symbol('x'))), Rational(-10920947622050089849, 16777216)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_391(c:sympy.Rational):
	#c < 1407283884897415/281474976710656

	pre_cond = StrictLessThan(Symbol('c'), Rational(1407283884897415, 281474976710656))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_392(c:sympy.Rational):
	#(x**2 < 2758736246892233009/70368744177664) & (8388608*c + 1660732537*x < -2758032559450456369/8388608)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(2758736246892233009, 70368744177664)), StrictLessThan(Add(Mul(Integer(8388608), Symbol('c')), Mul(Integer(1660732537), Symbol('x'))), Rational(-2758032559450456369, 8388608)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_393(c:sympy.Rational):
	#c < 351821205765839/70368744177664

	pre_cond = StrictLessThan(Symbol('c'), Rational(351821205765839, 70368744177664))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_394(c:sympy.Rational):
	#(x**2 < 44586762216359994161/1125899906842624) & (33554432*c + 6676488839*x < -44575503217291567921/33554432)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(44586762216359994161, 1125899906842624)), StrictLessThan(Add(Mul(Integer(33554432), Symbol('c')), Mul(Integer(6676488839), Symbol('x'))), Rational(-44575503217291567921, 33554432)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_395(c:sympy.Rational):
	#c < 5629141358337231/1125899906842624

	pre_cond = StrictLessThan(Symbol('c'), Rational(5629141358337231, 1125899906842624))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_396(c:sympy.Rational):
	#(x**2 < 45035996276863441409/1125899906842624) & (33554432*c + 6710047487*x < -45024737277795015169/33554432)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(45035996276863441409, 1125899906842624)), StrictLessThan(Add(Mul(Integer(33554432), Symbol('c')), Mul(Integer(6710047487), Symbol('x'))), Rational(-45024737277795015169, 33554432)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_397(c:sympy.Rational):
	#c < 5629146067461631/1125899906842624

	pre_cond = StrictLessThan(Symbol('c'), Rational(5629146067461631, 1125899906842624))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_398(c:sympy.Rational):
	#(x**2 < 45487482136615150889/1125899906842624) & (33554432*c + 6743606093*x < -45476223137546724649/33554432)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(45487482136615150889, 1125899906842624)), StrictLessThan(Add(Mul(Integer(33554432), Symbol('c')), Mul(Integer(6743606093), Symbol('x'))), Rational(-45476223137546724649, 33554432)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_399(c:sympy.Rational):
	#c < 5629151006464727/1125899906842624

	pre_cond = StrictLessThan(Symbol('c'), Rational(5629151006464727, 1125899906842624))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_400(c:sympy.Rational):
	#(x**2 < 11485304950178170801/281474976710656) & (16777216*c + 3388582329*x < -11482490200411064241/16777216)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(11485304950178170801, 281474976710656)), StrictLessThan(Add(Mul(Integer(16777216), Symbol('c')), Mul(Integer(3388582329), Symbol('x'))), Rational(-11482490200411064241, 16777216)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_401(c:sympy.Rational):
	#c < 1407288406980687/281474976710656

	pre_cond = StrictLessThan(Symbol('c'), Rational(1407288406980687, 281474976710656))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_402(c:sympy.Rational):
	#(x**2 < 185588837070845418185/4503599627370496) & (67108864*c + 13621446365*x < -185543801074571713225/67108864)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(185588837070845418185, 4503599627370496)), StrictLessThan(Add(Mul(Integer(67108864), Symbol('c')), Mul(Integer(13621446365), Symbol('x'))), Rational(-185543801074571713225, 67108864)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_403(c:sympy.Rational):
	#c < 22516618620396855/4503599627370496

	pre_cond = StrictLessThan(Symbol('c'), Rational(22516618620396855, 4503599627370496))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_404(c:sympy.Rational):
	#(x**2 < 46855450536300725129/1125899906842624) & (33554432*c + 6844281667*x < -46844191537232298889/33554432)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(46855450536300725129, 1125899906842624)), StrictLessThan(Add(Mul(Integer(33554432), Symbol('c')), Mul(Integer(6844281667), Symbol('x'))), Rational(-46844191537232298889, 33554432)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_405(c:sympy.Rational):
	#c < 5629154744122487/1125899906842624

	pre_cond = StrictLessThan(Symbol('c'), Rational(5629154744122487, 1125899906842624))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_406(c:sympy.Rational):
	#(x**2 < 47315943591548918561/1125899906842624) & (33554432*c + 6877840111*x < -47304684592480492321/33554432)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(47315943591548918561, 1125899906842624)), StrictLessThan(Add(Mul(Integer(33554432), Symbol('c')), Mul(Integer(6877840111), Symbol('x'))), Rational(-47304684592480492321, 33554432)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_407(c:sympy.Rational):
	#c < 5629161361007839/1125899906842624

	pre_cond = StrictLessThan(Symbol('c'), Rational(5629161361007839, 1125899906842624))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_408(c:sympy.Rational):
	#(x**2 < 191114753811787308049/4503599627370496) & (67108864*c + 13822797033*x < -191069717815513603089/67108864)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(191114753811787308049, 4503599627370496)), StrictLessThan(Add(Mul(Integer(67108864), Symbol('c')), Mul(Integer(13822797033), Symbol('x'))), Rational(-191069717815513603089, 67108864)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_409(c:sympy.Rational):
	#c < 22516659049702383/4503599627370496

	pre_cond = StrictLessThan(Symbol('c'), Rational(22516659049702383, 4503599627370496))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_410(c:sympy.Rational):
	#(x**2 < 3015230319980463481/70368744177664) & (8388608*c + 1736239221*x < -3014526632538686841/8388608)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(3015230319980463481, 70368744177664)), StrictLessThan(Add(Mul(Integer(8388608), Symbol('c')), Mul(Integer(1736239221), Symbol('x'))), Rational(-3014526632538686841, 8388608)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_411(c:sympy.Rational):
	#c < 351822834547335/70368744177664

	pre_cond = StrictLessThan(Symbol('c'), Rational(351822834547335, 70368744177664))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_412(c:sympy.Rational):
	#(x**2 < 48710933577140861609/1125899906842624) & (33554432*c + 6978515213*x < -48699674578072435369/33554432)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(48710933577140861609, 1125899906842624)), StrictLessThan(Add(Mul(Integer(33554432), Symbol('c')), Mul(Integer(6978515213), Symbol('x'))), Rational(-48699674578072435369, 33554432)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_413(c:sympy.Rational):
	#c < 5629170446959959/1125899906842624

	pre_cond = StrictLessThan(Symbol('c'), Rational(5629170446959959, 1125899906842624))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_414(c:sympy.Rational):
	#(x**2 < 49180433838591411265/1125899906842624) & (33554432*c + 7012073505*x < -49169174839522985025/33554432)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(49180433838591411265, 1125899906842624)), StrictLessThan(Add(Mul(Integer(33554432), Symbol('c')), Mul(Integer(7012073505), Symbol('x'))), Rational(-49169174839522985025, 33554432)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_415(c:sympy.Rational):
	#c < 5629173404564415/1125899906842624

	pre_cond = StrictLessThan(Symbol('c'), Rational(5629173404564415, 1125899906842624))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_416(c:sympy.Rational):
	#(x**2 < 193953851158551265/4398046511104) & (2097152*c + 440351985*x < -193909870693440225/2097152)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(193953851158551265, 4398046511104)), StrictLessThan(Add(Mul(Integer(2097152), Symbol('c')), Mul(Integer(440351985), Symbol('x'))), Rational(-193909870693440225, 2097152)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_417(c:sympy.Rational):
	#c < 21988976370975/4398046511104

	pre_cond = StrictLessThan(Symbol('c'), Rational(21988976370975, 4398046511104))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_418(c:sympy.Rational):
	#(x**2 < 50126189757842446681/1125899906842624) & (33554432*c + 7079189979*x < -50114930758774020441/33554432)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(50126189757842446681, 1125899906842624)), StrictLessThan(Add(Mul(Integer(33554432), Symbol('c')), Mul(Integer(7079189979), Symbol('x'))), Rational(-50114930758774020441, 33554432)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_419(c:sympy.Rational):
	#c < 5629180733171367/1125899906842624

	pre_cond = StrictLessThan(Symbol('c'), Rational(5629180733171367, 1125899906842624))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_420(c:sympy.Rational):
	#(x**2 < 12650611353775701121/281474976710656) & (16777216*c + 3556374081*x < -12647796604008594561/16777216)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(12650611353775701121, 281474976710656)), StrictLessThan(Add(Mul(Integer(16777216), Symbol('c')), Mul(Integer(3556374081), Symbol('x'))), Rational(-12647796604008594561, 16777216)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_421(c:sympy.Rational):
	#c < 1407296343966591/281474976710656

	pre_cond = StrictLessThan(Symbol('c'), Rational(1407296343966591, 281474976710656))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_422(c:sympy.Rational):
	#(x**2 < 12770238218853560585/281474976710656) & (16777216*c + 3573153155*x < -12767423469086454025/16777216)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(12770238218853560585, 281474976710656)), StrictLessThan(Add(Mul(Integer(16777216), Symbol('c')), Mul(Integer(3573153155), Symbol('x'))), Rational(-12767423469086454025, 16777216)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_423(c:sympy.Rational):
	#c < 1407297089556215/281474976710656

	pre_cond = StrictLessThan(Symbol('c'), Rational(1407297089556215, 281474976710656))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_424(c:sympy.Rational):
	#(x**2 < 206246848555637654369/4503599627370496) & (67108864*c + 14359728847*x < -206201812559363949409/67108864)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(206246848555637654369, 4503599627370496)), StrictLessThan(Add(Mul(Integer(67108864), Symbol('c')), Mul(Integer(14359728847), Symbol('x'))), Rational(-206201812559363949409, 67108864)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_425(c:sympy.Rational):
	#c < 22516758458809503/4503599627370496

	pre_cond = StrictLessThan(Symbol('c'), Rational(22516758458809503, 4503599627370496))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_426(c:sympy.Rational):
	#(x**2 < 208178892794567154985/4503599627370496) & (67108864*c + 14426845005*x < -208133856798293450025/67108864)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(208178892794567154985, 4503599627370496)), StrictLessThan(Add(Mul(Integer(67108864), Symbol('c')), Mul(Integer(14426845005), Symbol('x'))), Rational(-208133856798293450025, 67108864)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_427(c:sympy.Rational):
	#c < 22516770475778775/4503599627370496

	pre_cond = StrictLessThan(Symbol('c'), Rational(22516770475778775, 4503599627370496))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_428(c:sympy.Rational):
	#(x**2 < 3283124128884925409/70368744177664) & (8388608*c + 1811745137*x < -3282420441443148769/8388608)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(3283124128884925409, 70368744177664)), StrictLessThan(Add(Mul(Integer(8388608), Symbol('c')), Mul(Integer(1811745137), Symbol('x'))), Rational(-3282420441443148769, 8388608)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_429(c:sympy.Rational):
	#c < 351824599899167/70368744177664

	pre_cond = StrictLessThan(Symbol('c'), Rational(351824599899167, 70368744177664))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_430(c:sympy.Rational):
	#(x**2 < 12943725762381665/274877906944) & (524288*c + 113758415*x < -12940976983312225/524288)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(12943725762381665, 274877906944)), StrictLessThan(Add(Mul(Integer(524288), Symbol('c')), Mul(Integer(113758415), Symbol('x'))), Rational(-12940976983312225, 524288)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_431(c:sympy.Rational):
	#c < 1374315411615/274877906944

	pre_cond = StrictLessThan(Symbol('c'), Rational(1374315411615, 274877906944))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_432(c:sympy.Rational):
	#(x**2 < 53507267180880204761/1125899906842624) & (33554432*c + 7314096539*x < -53496008181811778521/33554432)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(53507267180880204761, 1125899906842624)), StrictLessThan(Add(Mul(Integer(33554432), Symbol('c')), Mul(Integer(7314096539), Symbol('x'))), Rational(-53496008181811778521, 33554432)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_433(c:sympy.Rational):
	#c < 5629199317986343/1125899906842624

	pre_cond = StrictLessThan(Symbol('c'), Rational(5629199317986343, 1125899906842624))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_434(c:sympy.Rational):
	#(x**2 < 13499821361176087609/281474976710656) & (16777216*c + 3673827243*x < -13497006611408981049/16777216)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(13499821361176087609, 281474976710656)), StrictLessThan(Add(Mul(Integer(16777216), Symbol('c')), Mul(Integer(3673827243), Symbol('x'))), Rational(-13497006611408981049, 16777216)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_435(c:sympy.Rational):
	#c < 1407299937530823/281474976710656

	pre_cond = StrictLessThan(Symbol('c'), Rational(1407299937530823, 281474976710656))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_436(c:sympy.Rational):
	#(x**2 < 212865451144461665/4398046511104) & (2097152*c + 461325775*x < -212821470679350625/2097152)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(212865451144461665, 4398046511104)), StrictLessThan(Add(Mul(Integer(2097152), Symbol('c')), Mul(Integer(461325775), Symbol('x'))), Rational(-212821470679350625, 2097152)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_437(c:sympy.Rational):
	#c < 21989093065375/4398046511104

	pre_cond = StrictLessThan(Symbol('c'), Rational(21989093065375, 4398046511104))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_438(c:sympy.Rational):
	#(x**2 < 219960309424572386449/4503599627370496) & (67108864*c + 14829540567*x < -219915273428298681489/67108864)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(219960309424572386449, 4503599627370496)), StrictLessThan(Add(Mul(Integer(67108864), Symbol('c')), Mul(Integer(14829540567), Symbol('x'))), Rational(-219915273428298681489, 67108864)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_439(c:sympy.Rational):
	#c < 22516833317499759/4503599627370496

	pre_cond = StrictLessThan(Symbol('c'), Rational(22516833317499759, 4503599627370496))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_440(c:sympy.Rational):
	#(x**2 < 221955404052597330401/4503599627370496) & (67108864*c + 14896656271*x < -221910368056323625441/67108864)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(221955404052597330401, 4503599627370496)), StrictLessThan(Add(Mul(Integer(67108864), Symbol('c')), Mul(Integer(14896656271), Symbol('x'))), Rational(-221910368056323625441, 67108864)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_441(c:sympy.Rational):
	#c < 22516847129898527/4503599627370496

	pre_cond = StrictLessThan(Symbol('c'), Rational(22516847129898527, 4503599627370496))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_442(c:sympy.Rational):
	#(x**2 < 55989876472622232089/1125899906842624) & (33554432*c + 7481885957*x < -55978617473553805849/33554432)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(55989876472622232089, 1125899906842624)), StrictLessThan(Add(Mul(Integer(33554432), Symbol('c')), Mul(Integer(7481885957), Symbol('x'))), Rational(-55978617473553805849, 33554432)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_443(c:sympy.Rational):
	#c < 5629213874441703/1125899906842624

	pre_cond = StrictLessThan(Symbol('c'), Rational(5629213874441703, 1125899906842624))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_444(c:sympy.Rational):
	#(x**2 < 3530822108026294609/70368744177664) & (8388608*c + 1878860937*x < -3530118420584517969/8388608)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(3530822108026294609, 70368744177664)), StrictLessThan(Add(Mul(Integer(8388608), Symbol('c')), Mul(Integer(1878860937), Symbol('x'))), Rational(-3530118420584517969, 8388608)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_445(c:sympy.Rational):
	#c < 351826104757935/70368744177664

	pre_cond = StrictLessThan(Symbol('c'), Rational(351826104757935, 70368744177664))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_446(c:sympy.Rational):
	#(x**2 < 227994731158006819321/4503599627370496) & (67108864*c + 15098003019*x < -227949695161733114361/67108864)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(227994731158006819321, 4503599627370496)), StrictLessThan(Add(Mul(Integer(67108864), Symbol('c')), Mul(Integer(15098003019), Symbol('x'))), Rational(-227949695161733114361, 67108864)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_447(c:sympy.Rational):
	#c < 22516874840479239/4503599627370496

	pre_cond = StrictLessThan(Symbol('c'), Rational(22516874840479239, 4503599627370496))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_448(c:sympy.Rational):
	#(x**2 < 57506463642342922321/1125899906842624) & (33554432*c + 7582559241*x < -57495204643274496081/33554432)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(57506463642342922321, 1125899906842624)), StrictLessThan(Add(Mul(Integer(33554432), Symbol('c')), Mul(Integer(7582559241), Symbol('x'))), Rational(-57495204643274496081, 33554432)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_449(c:sympy.Rational):
	#c < 5629223737485231/1125899906842624

	pre_cond = StrictLessThan(Symbol('c'), Rational(5629223737485231, 1125899906842624))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_450(c:sympy.Rational):
	#(x**2 < 226626938686532521/4398046511104) & (2097152*c + 476007309*x < -226582958221421481/2097152)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(226626938686532521, 4398046511104)), StrictLessThan(Add(Mul(Integer(2097152), Symbol('c')), Mul(Integer(476007309), Symbol('x'))), Rational(-226582958221421481, 2097152)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_451(c:sympy.Rational):
	#c < 21989157639255/4398046511104

	pre_cond = StrictLessThan(Symbol('c'), Rational(21989157639255, 4398046511104))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_452(c:sympy.Rational):
	#(x**2 < 14632195190085468041/281474976710656) & (16777216*c + 3824837309*x < -14629380440318361481/16777216)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(14632195190085468041, 281474976710656)), StrictLessThan(Add(Mul(Integer(16777216), Symbol('c')), Mul(Integer(3824837309), Symbol('x'))), Rational(-14629380440318361481, 16777216)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_453(c:sympy.Rational):
	#c < 1407306814636151/281474976710656

	pre_cond = StrictLessThan(Symbol('c'), Rational(1407306814636151, 281474976710656))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_454(c:sympy.Rational):
	#(x**2 < 922551828463109249/17592186044416) & (4194304*c + 960404033*x < -922375906602665089/4194304)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(922551828463109249, 17592186044416)), StrictLessThan(Add(Mul(Integer(4194304), Symbol('c')), Mul(Integer(960404033), Symbol('x'))), Rational(-922375906602665089, 4194304)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_455(c:sympy.Rational):
	#c < 87956682554239/17592186044416

	pre_cond = StrictLessThan(Symbol('c'), Rational(87956682554239, 17592186044416))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_456(c:sympy.Rational):
	#(x**2 < 14890026270501500041/281474976710656) & (16777216*c + 3858394941*x < -14887211520734393481/16777216)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(14890026270501500041, 281474976710656)), StrictLessThan(Add(Mul(Integer(16777216), Symbol('c')), Mul(Integer(3858394941), Symbol('x'))), Rational(-14887211520734393481, 16777216)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_457(c:sympy.Rational):
	#c < 1407307112385399/281474976710656

	pre_cond = StrictLessThan(Symbol('c'), Rational(1407307112385399, 281474976710656))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_458(c:sympy.Rational):
	#(x**2 < 234684159905489129/4398046511104) & (2097152*c + 484396717*x < -234640179440378089/2097152)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(234684159905489129, 4398046511104)), StrictLessThan(Add(Mul(Integer(2097152), Symbol('c')), Mul(Integer(484396717), Symbol('x'))), Rational(-234640179440378089, 2097152)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_459(c:sympy.Rational):
	#c < 21989188968215/4398046511104

	pre_cond = StrictLessThan(Symbol('c'), Rational(21989188968215, 4398046511104))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_460(c:sympy.Rational):
	#(x**2 < 60600436592966777465/1125899906842624) & (33554432*c + 7783905035*x < -60589177593898351225/33554432)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(60600436592966777465, 1125899906842624)), StrictLessThan(Add(Mul(Integer(33554432), Symbol('c')), Mul(Integer(7783905035), Symbol('x'))), Rational(-60589177593898351225, 33554432)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_461(c:sympy.Rational):
	#c < 5629234498356615/1125899906842624

	pre_cond = StrictLessThan(Symbol('c'), Rational(5629234498356615, 1125899906842624))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_462(c:sympy.Rational):
	#(x**2 < 61123980048054356281/1125899906842624) & (33554432*c + 7817462571*x < -61112721048985930041/33554432)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(61123980048054356281, 1125899906842624)), StrictLessThan(Add(Mul(Integer(33554432), Symbol('c')), Mul(Integer(7817462571), Symbol('x'))), Rational(-61112721048985930041, 33554432)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_463(c:sympy.Rational):
	#c < 5629237535438535/1125899906842624

	pre_cond = StrictLessThan(Symbol('c'), Rational(5629237535438535, 1125899906842624))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_464(c:sympy.Rational):
	#(x**2 < 246599101213930610881/4503599627370496) & (67108864*c + 15702040161*x < -246554065217656905921/67108864)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(246599101213930610881, 4503599627370496)), StrictLessThan(Add(Mul(Integer(67108864), Symbol('c')), Mul(Integer(15702040161), Symbol('x'))), Rational(-246554065217656905921, 67108864)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_465(c:sympy.Rational):
	#c < 22516961121476415/4503599627370496

	pre_cond = StrictLessThan(Symbol('c'), Rational(22516961121476415, 4503599627370496))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_466(c:sympy.Rational):
	#(x**2 < 3886113897612537521/70368744177664) & (8388608*c + 1971144391*x < -3885410210170760881/8388608)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(3886113897612537521, 70368744177664)), StrictLessThan(Add(Mul(Integer(8388608), Symbol('c')), Mul(Integer(1971144391), Symbol('x'))), Rational(-3885410210170760881, 8388608)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_467(c:sympy.Rational):
	#c < 351827591205199/70368744177664

	pre_cond = StrictLessThan(Symbol('c'), Rational(351827591205199, 70368744177664))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_468(c:sympy.Rational):
	#(x**2 < 250832484871092926809/4503599627370496) & (67108864*c + 15836270043*x < -250787448874819221849/67108864)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(250832484871092926809, 4503599627370496)), StrictLessThan(Add(Mul(Integer(67108864), Symbol('c')), Mul(Integer(15836270043), Symbol('x'))), Rational(-250787448874819221849, 67108864)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_469(c:sympy.Rational):
	#c < 22516974759610023/4503599627370496

	pre_cond = StrictLessThan(Symbol('c'), Rational(22516974759610023, 4503599627370496))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_470(c:sympy.Rational):
	#(x**2 < 252962687496469103609/4503599627370496) & (67108864*c + 15903384907*x < -252917651500195398649/67108864)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(252962687496469103609, 4503599627370496)), StrictLessThan(Add(Mul(Integer(67108864), Symbol('c')), Mul(Integer(15903384907), Symbol('x'))), Rational(-252917651500195398649, 67108864)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_471(c:sympy.Rational):
	#c < 22516982457809927/4503599627370496

	pre_cond = StrictLessThan(Symbol('c'), Rational(22516982457809927, 4503599627370496))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_472(c:sympy.Rational):
	#(x**2 < 3985967145356152865/70368744177664) & (8388608*c + 1996312465*x < -3985263457914376225/8388608)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(3985967145356152865, 70368744177664)), StrictLessThan(Add(Mul(Integer(8388608), Symbol('c')), Mul(Integer(1996312465), Symbol('x'))), Rational(-3985263457914376225, 8388608)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_473(c:sympy.Rational):
	#c < 351828112519135/70368744177664

	pre_cond = StrictLessThan(Symbol('c'), Rational(351828112519135, 70368744177664))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_474(c:sympy.Rational):
	#(x**2 < 16078132145855018201/281474976710656) & (16777216*c + 4009403621*x < -16075317396087911641/16777216)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(16078132145855018201, 281474976710656)), StrictLessThan(Add(Mul(Integer(16777216), Symbol('c')), Mul(Integer(4009403621), Symbol('x'))), Rational(-16075317396087911641, 16777216)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_475(c:sympy.Rational):
	#c < 1407312699181863/281474976710656

	pre_cond = StrictLessThan(Symbol('c'), Rational(1407312699181863, 281474976710656))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_476(c:sympy.Rational):
	#(x**2 < 64851834634296857041/1125899906842624) & (33554432*c + 8052364599*x < -64840575635228430801/33554432)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(64851834634296857041, 1125899906842624)), StrictLessThan(Add(Mul(Integer(33554432), Symbol('c')), Mul(Integer(8052364599), Symbol('x'))), Rational(-64840575635228430801, 33554432)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_477(c:sympy.Rational):
	#c < 5629255096233519/1125899906842624

	pre_cond = StrictLessThan(Symbol('c'), Rational(5629255096233519, 1125899906842624))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_478(c:sympy.Rational):
	#(x**2 < 4087087030591689929/70368744177664) & (8388608*c + 2021480483*x < -4086383343149913289/8388608)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(4087087030591689929, 70368744177664)), StrictLessThan(Add(Mul(Integer(8388608), Symbol('c')), Mul(Integer(2021480483), Symbol('x'))), Rational(-4086383343149913289, 8388608)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_479(c:sympy.Rational):
	#c < 351828570663735/70368744177664

	pre_cond = StrictLessThan(Symbol('c'), Rational(351828570663735, 70368744177664))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_480(c:sympy.Rational):
	#(x**2 < 1054995234370529631065/18014398509481984) & (134217728*c + 32477916965*x < -1054815090385434811225/134217728)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(1054995234370529631065, 18014398509481984)), StrictLessThan(Add(Mul(Integer(134217728), Symbol('c')), Mul(Integer(32477916965), Symbol('x'))), Rational(-1054815090385434811225, 134217728)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_481(c:sympy.Rational):
	#c < 90068116584424615/18014398509481984

	pre_cond = StrictLessThan(Symbol('c'), Rational(90068116584424615, 18014398509481984))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_482(c:sympy.Rational):
	#(x**2 < 265933054406046445769/4503599627370496) & (67108864*c + 16306073053*x < -265888018409772740809/67108864)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(265933054406046445769, 4503599627370496)), StrictLessThan(Add(Mul(Integer(67108864), Symbol('c')), Mul(Integer(16306073053), Symbol('x'))), Rational(-265888018409772740809, 67108864)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_483(c:sympy.Rational):
	#c < 22517039972814647/4503599627370496

	pre_cond = StrictLessThan(Symbol('c'), Rational(22517039972814647, 4503599627370496))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_484(c:sympy.Rational):
	#(x**2 < 268126307427900835889/4503599627370496) & (67108864*c + 16373187577*x < -268081271431627130929/67108864)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(268126307427900835889, 4503599627370496)), StrictLessThan(Add(Mul(Integer(67108864), Symbol('c')), Mul(Integer(16373187577), Symbol('x'))), Rational(-268081271431627130929, 67108864)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_485(c:sympy.Rational):
	#c < 22517046110205903/4503599627370496

	pre_cond = StrictLessThan(Symbol('c'), Rational(22517046110205903, 4503599627370496))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_486(c:sympy.Rational):
	#(x**2 < 270328567655910927985/4503599627370496) & (67108864*c + 16440302055*x < -270283531659637223025/67108864)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(270328567655910927985, 4503599627370496)), StrictLessThan(Add(Mul(Integer(67108864), Symbol('c')), Mul(Integer(16440302055), Symbol('x'))), Rational(-270283531659637223025, 67108864)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_487(c:sympy.Rational):
	#c < 22517048702079375/4503599627370496

	pre_cond = StrictLessThan(Symbol('c'), Rational(22517048702079375, 4503599627370496))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_488(c:sympy.Rational):
	#(x**2 < 272539835071553126129/4503599627370496) & (67108864*c + 16507416487*x < -272494799075279421169/67108864)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(272539835071553126129, 4503599627370496)), StrictLessThan(Add(Mul(Integer(67108864), Symbol('c')), Mul(Integer(16507416487), Symbol('x'))), Rational(-272494799075279421169, 67108864)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_489(c:sympy.Rational):
	#c < 22517057011007759/4503599627370496

	pre_cond = StrictLessThan(Symbol('c'), Rational(22517057011007759, 4503599627370496))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_490(c:sympy.Rational):
	#(x**2 < 68690027422363227209/1125899906842624) & (33554432*c + 8287265437*x < -68678768423294800969/33554432)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(68690027422363227209, 1125899906842624)), StrictLessThan(Add(Mul(Integer(33554432), Symbol('c')), Mul(Integer(8287265437), Symbol('x'))), Rational(-68678768423294800969, 33554432)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_491(c:sympy.Rational):
	#c < 5629265931594679/1125899906842624

	pre_cond = StrictLessThan(Symbol('c'), Rational(5629265931594679, 1125899906842624))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_492(c:sympy.Rational):
	#(x**2 < 270497452628407609/4398046511104) & (2097152*c + 520051413*x < -270453472163296569/2097152)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(270497452628407609, 4398046511104)), StrictLessThan(Add(Mul(Integer(2097152), Symbol('c')), Mul(Integer(520051413), Symbol('x'))), Rational(-270453472163296569, 2097152)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_493(c:sympy.Rational):
	#c < 21989333895879/4398046511104

	pre_cond = StrictLessThan(Symbol('c'), Rational(21989333895879, 4398046511104))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_494(c:sympy.Rational):
	#(x**2 < 1116910722038671922681/18014398509481984) & (134217728*c + 33417519029*x < -1116730578053577102841/134217728)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(1116910722038671922681, 18014398509481984)), StrictLessThan(Add(Mul(Integer(134217728), Symbol('c')), Mul(Integer(33417519029), Symbol('x'))), Rational(-1116730578053577102841, 134217728)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_495(c:sympy.Rational):
	#c < 90068334240279047/18014398509481984

	pre_cond = StrictLessThan(Symbol('c'), Rational(90068334240279047, 18014398509481984))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_496(c:sympy.Rational):
	#(x**2 < 1125899906905887376361/18014398509481984) & (134217728*c + 33551747539*x < -1125719762920792556521/134217728)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(1125899906905887376361, 18014398509481984)), StrictLessThan(Add(Mul(Integer(134217728), Symbol('c')), Mul(Integer(33551747539), Symbol('x'))), Rational(-1125719762920792556521, 134217728)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_497(c:sympy.Rational):
	#c < 90068357750291479/18014398509481984

	pre_cond = StrictLessThan(Symbol('c'), Rational(90068357750291479, 18014398509481984))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_498(c:sympy.Rational):
	#(x**2 < 283731280124384161321/4503599627370496) & (67108864*c + 16842987981*x < -283686244128110456361/67108864)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(283731280124384161321, 4503599627370496)), StrictLessThan(Add(Mul(Integer(67108864), Symbol('c')), Mul(Integer(16842987981), Symbol('x'))), Rational(-283686244128110456361, 67108864)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_499(c:sympy.Rational):
	#c < 22517104301003223/4503599627370496

	pre_cond = StrictLessThan(Symbol('c'), Rational(22517104301003223, 4503599627370496))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_500(c:sympy.Rational):
	#(x**2 < 1143986362946473718441/18014398509481984) & (134217728*c + 33820204301*x < -1143806218961378898601/134217728)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(1143986362946473718441, 18014398509481984)), StrictLessThan(Add(Mul(Integer(134217728), Symbol('c')), Mul(Integer(33820204301), Symbol('x'))), Rational(-1143806218961378898601, 134217728)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_501(c:sympy.Rational):
	#c < 90068446185229655/18014398509481984

	pre_cond = StrictLessThan(Symbol('c'), Rational(90068446185229655, 18014398509481984))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_502(c:sympy.Rational):
	#(x**2 < 4612334536876007782129/72057594037927936) & (268435456*c + 67908865113*x < -4611613960935628502769/268435456)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(4612334536876007782129, 72057594037927936)), StrictLessThan(Add(Mul(Integer(268435456), Symbol('c')), Mul(Integer(67908865113), Symbol('x'))), Rational(-4611613960935628502769, 268435456)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_503(c:sympy.Rational):
	#c < 360273846185068815/72057594037927936

	pre_cond = StrictLessThan(Symbol('c'), Rational(360273846185068815, 72057594037927936))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_504(c:sympy.Rational):
	#(x**2 < 1162216934281961631281/18014398509481984) & (134217728*c + 34088660729*x < -1162036790296866811441/134217728)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(1162216934281961631281, 18014398509481984)), StrictLessThan(Add(Mul(Integer(134217728), Symbol('c')), Mul(Integer(34088660729), Symbol('x'))), Rational(-1162036790296866811441, 134217728)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_505(c:sympy.Rational):
	#c < 90068479870931407/18014398509481984

	pre_cond = StrictLessThan(Symbol('c'), Rational(90068479870931407, 18014398509481984))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_506(c:sympy.Rational):
	#(x**2 < 73211641448198488265/1125899906842624) & (33554432*c + 8555722205*x < -73200382449130062025/33554432)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(73211641448198488265, 1125899906842624)), StrictLessThan(Add(Mul(Integer(33554432), Symbol('c')), Mul(Integer(8555722205), Symbol('x'))), Rational(-73200382449130062025, 33554432)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_507(c:sympy.Rational):
	#c < 5629280203390775/1125899906842624

	pre_cond = StrictLessThan(Symbol('c'), Rational(5629280203390775, 1125899906842624))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_508(c:sympy.Rational):
	#(x**2 < 73786976294870975089/1125899906842624) & (33554432*c + 8589279207*x < -73775717295802548849/33554432)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(73786976294870975089, 1125899906842624)), StrictLessThan(Add(Mul(Integer(33554432), Symbol('c')), Mul(Integer(8589279207), Symbol('x'))), Rational(-73775717295802548849, 33554432)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_509(c:sympy.Rational):
	#c < 5629284753079695/1125899906842624

	pre_cond = StrictLessThan(Symbol('c'), Rational(5629284753079695, 1125899906842624))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_510(c:sympy.Rational):
	#(x**2 < 297458251800077224601/4503599627370496) & (67108864*c + 17245672379*x < -297413215803803519641/67108864)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(297458251800077224601, 4503599627370496)), StrictLessThan(Add(Mul(Integer(67108864), Symbol('c')), Mul(Integer(17245672379), Symbol('x'))), Rational(-297413215803803519641, 67108864)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_511(c:sympy.Rational):
	#c < 22517139809416551/4503599627370496

	pre_cond = StrictLessThan(Symbol('c'), Rational(22517139809416551, 4503599627370496))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_512(c:sympy.Rational):
	#(x**2 < 18296972998305889/274877906944) & (524288*c + 135256143*x < -18294224219236449/524288)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(18296972998305889, 274877906944)), StrictLessThan(Add(Mul(Integer(524288), Symbol('c')), Mul(Integer(135256143), Symbol('x'))), Rational(-18294224219236449, 524288)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_513(c:sympy.Rational):
	#c < 1374337669023/274877906944

	pre_cond = StrictLessThan(Symbol('c'), Rational(1374337669023, 274877906944))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_514(c:sympy.Rational):
	#(x**2 < 75526491652658935265/1125899906842624) & (33554432*c + 8689950095*x < -75515232653590509025/33554432)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(75526491652658935265, 1125899906842624)), StrictLessThan(Add(Mul(Integer(33554432), Symbol('c')), Mul(Integer(8689950095), Symbol('x'))), Rational(-75515232653590509025, 33554432)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_515(c:sympy.Rational):
	#c < 5629288841890335/1125899906842624

	pre_cond = StrictLessThan(Symbol('c'), Rational(5629288841890335, 1125899906842624))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_516(c:sympy.Rational):
	#(x**2 < 1217773339283983025465/18014398509481984) & (134217728*c + 34894028075*x < -1217593195298888205625/134217728)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(1217773339283983025465, 18014398509481984)), StrictLessThan(Add(Mul(Integer(134217728), Symbol('c')), Mul(Integer(34894028075), Symbol('x'))), Rational(-1217593195298888205625, 134217728)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_517(c:sympy.Rational):
	#c < 90068639737330375/18014398509481984

	pre_cond = StrictLessThan(Symbol('c'), Rational(90068639737330375, 18014398509481984))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_518(c:sympy.Rational):
	#(x**2 < 306789710237334560369/4503599627370496) & (67108864*c + 17514127847*x < -306744674241060855409/67108864)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(306789710237334560369, 4503599627370496)), StrictLessThan(Add(Mul(Integer(67108864), Symbol('c')), Mul(Integer(17514127847), Symbol('x'))), Rational(-306744674241060855409, 67108864)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_519(c:sympy.Rational):
	#c < 22517161065390479/4503599627370496

	pre_cond = StrictLessThan(Symbol('c'), Rational(22517161065390479, 4503599627370496))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_520(c:sympy.Rational):
	#(x**2 < 77286273206692240721/1125899906842624) & (33554432*c + 8790620809*x < -77275014207623814481/33554432)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(77286273206692240721, 1125899906842624)), StrictLessThan(Add(Mul(Integer(33554432), Symbol('c')), Mul(Integer(8790620809), Symbol('x'))), Rational(-77275014207623814481, 33554432)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_521(c:sympy.Rational):
	#c < 5629293800563375/1125899906842624

	pre_cond = StrictLessThan(Symbol('c'), Rational(5629293800563375, 1125899906842624))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_522(c:sympy.Rational):
	#(x**2 < 4867335666042824201/70368744177664) & (8388608*c + 2206044419*x < -4866631978601047561/8388608)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(4867335666042824201, 70368744177664)), StrictLessThan(Add(Mul(Integer(8388608), Symbol('c')), Mul(Integer(2206044419), Symbol('x'))), Rational(-4866631978601047561, 8388608)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_523(c:sympy.Rational):
	#c < 351830994164215/70368744177664

	pre_cond = StrictLessThan(Symbol('c'), Rational(351830994164215, 70368744177664))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_524(c:sympy.Rational):
	#(x**2 < 1255531518560264553641/18014398509481984) & (134217728*c + 35430938099*x < -1255351374575169733801/134217728)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(1255531518560264553641, 18014398509481984)), StrictLessThan(Add(Mul(Integer(134217728), Symbol('c')), Mul(Integer(35430938099), Symbol('x'))), Rational(-1255351374575169733801, 134217728)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_525(c:sympy.Rational):
	#c < 90068739724901207/18014398509481984

	pre_cond = StrictLessThan(Symbol('c'), Rational(90068739724901207, 18014398509481984))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_526(c:sympy.Rational):
	#(x**2 < 79066320958566162265/1125899906842624) & (33554432*c + 8891291355*x < -79055061959497736025/33554432)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(79066320958566162265, 1125899906842624)), StrictLessThan(Add(Mul(Integer(33554432), Symbol('c')), Mul(Integer(8891291355), Symbol('x'))), Rational(-79055061959497736025, 33554432)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_527(c:sympy.Rational):
	#c < 5629298839134375/1125899906842624

	pre_cond = StrictLessThan(Symbol('c'), Rational(5629298839134375, 1125899906842624))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_528(c:sympy.Rational):
	#(x**2 < 318656695247986137185/4503599627370496) & (67108864*c + 17849696335*x < -318611659251712432225/67108864)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(318656695247986137185, 4503599627370496)), StrictLessThan(Add(Mul(Integer(67108864), Symbol('c')), Mul(Integer(17849696335), Symbol('x'))), Rational(-318611659251712432225, 67108864)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_529(c:sympy.Rational):
	#c < 22517195579942815/4503599627370496

	pre_cond = StrictLessThan(Symbol('c'), Rational(22517195579942815, 4503599627370496))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_530(c:sympy.Rational):
	#(x**2 < 20066069615563661921/281474976710656) & (16777216*c + 4479202481*x < -20063254865796555361/16777216)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(20066069615563661921, 281474976710656)), StrictLessThan(Add(Mul(Integer(16777216), Symbol('c')), Mul(Integer(4479202481), Symbol('x'))), Rational(-20063254865796555361, 16777216)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_531(c:sympy.Rational):
	#c < 1407325106707871/281474976710656

	pre_cond = StrictLessThan(Symbol('c'), Rational(1407325106707871, 281474976710656))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_532(c:sympy.Rational):
	#(x**2 < 80866634914708330361/1125899906842624) & (33554432*c + 8991961739*x < -80855375915639904121/33554432)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(80866634914708330361, 1125899906842624)), StrictLessThan(Add(Mul(Integer(33554432), Symbol('c')), Mul(Integer(8991961739), Symbol('x'))), Rational(-80855375915639904121, 33554432)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_533(c:sympy.Rational):
	#c < 5629300751198343/1125899906842624

	pre_cond = StrictLessThan(Symbol('c'), Rational(5629300751198343, 1125899906842624))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_534(c:sympy.Rational):
	#(x**2 < 325884972663336482969/4503599627370496) & (67108864*c + 18051036997*x < -325839936667062778009/67108864)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(325884972663336482969, 4503599627370496)), StrictLessThan(Add(Mul(Integer(67108864), Symbol('c')), Mul(Integer(18051036997), Symbol('x'))), Rational(-325839936667062778009, 67108864)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_535(c:sympy.Rational):
	#c < 22517206519760743/4503599627370496

	pre_cond = StrictLessThan(Symbol('c'), Rational(22517206519760743, 4503599627370496))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_536(c:sympy.Rational):
	#(x**2 < 328312412848434236321/4503599627370496) & (67108864*c + 18118150481*x < -328267376852160531361/67108864)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(328312412848434236321, 4503599627370496)), StrictLessThan(Add(Mul(Integer(67108864), Symbol('c')), Mul(Integer(18118150481), Symbol('x'))), Rational(-328267376852160531361, 67108864)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_537(c:sympy.Rational):
	#c < 22517219299636319/4503599627370496

	pre_cond = StrictLessThan(Symbol('c'), Rational(22517219299636319, 4503599627370496))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_538(c:sympy.Rational):
	#(x**2 < 330748860236403277721/4503599627370496) & (67108864*c + 18185263931*x < -330703824240129572761/67108864)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(330748860236403277721, 4503599627370496)), StrictLessThan(Add(Mul(Integer(67108864), Symbol('c')), Mul(Integer(18185263931), Symbol('x'))), Rational(-330703824240129572761, 67108864)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_539(c:sympy.Rational):
	#c < 22517230207795303/4503599627370496

	pre_cond = StrictLessThan(Symbol('c'), Rational(22517230207795303, 4503599627370496))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_540(c:sympy.Rational):
	#(x**2 < 1332777259327219362865/18014398509481984) & (134217728*c + 36504754695*x < -1332597115342124543025/134217728)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(1332777259327219362865, 18014398509481984)), StrictLessThan(Add(Mul(Integer(134217728), Symbol('c')), Mul(Integer(36504754695), Symbol('x'))), Rational(-1332597115342124543025, 134217728)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_541(c:sympy.Rational):
	#c < 90068947858822095/18014398509481984

	pre_cond = StrictLessThan(Symbol('c'), Rational(90068947858822095, 18014398509481984))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_542(c:sympy.Rational):
	#(x**2 < 335648776639468619321/4503599627370496) & (67108864*c + 18319490731*x < -335603740643194914361/67108864)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(335648776639468619321, 4503599627370496)), StrictLessThan(Add(Mul(Integer(67108864), Symbol('c')), Mul(Integer(18319490731), Symbol('x'))), Rational(-335603740643194914361, 67108864)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_543(c:sympy.Rational):
	#c < 22517237156592071/4503599627370496

	pre_cond = StrictLessThan(Symbol('c'), Rational(22517237156592071, 4503599627370496))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_544(c:sympy.Rational):
	#(x**2 < 338112245627719559521/4503599627370496) & (67108864*c + 18386604081*x < -338067209631445854561/67108864)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(338112245627719559521, 4503599627370496)), StrictLessThan(Add(Mul(Integer(67108864), Symbol('c')), Mul(Integer(18386604081), Symbol('x'))), Rational(-338067209631445854561, 67108864)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_545(c:sympy.Rational):
	#c < 22517246620817055/4503599627370496

	pre_cond = StrictLessThan(Symbol('c'), Rational(22517246620817055, 4503599627370496))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_546(c:sympy.Rational):
	#(x**2 < 1362338887279901251049/18014398509481984) & (134217728*c + 36907434797*x < -1362158743294806431209/134217728)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(1362338887279901251049, 18014398509481984)), StrictLessThan(Add(Mul(Integer(134217728), Symbol('c')), Mul(Integer(36907434797), Symbol('x'))), Rational(-1362158743294806431209, 134217728)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_547(c:sympy.Rational):
	#c < 90069014600903191/18014398509481984

	pre_cond = StrictLessThan(Symbol('c'), Rational(90069014600903191, 18014398509481984))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_548(c:sympy.Rational):
	#(x**2 < 21441637826354350801/281474976710656) & (16777216*c + 4630207671*x < -21438823076587244241/16777216)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(21441637826354350801, 281474976710656)), StrictLessThan(Add(Mul(Integer(16777216), Symbol('c')), Mul(Integer(4630207671), Symbol('x'))), Rational(-21438823076587244241, 16777216)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_549(c:sympy.Rational):
	#c < 1407328470562095/281474976710656

	pre_cond = StrictLessThan(Symbol('c'), Rational(1407328470562095, 281474976710656))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_550(c:sympy.Rational):
	#(x**2 < 1382226783279666835465/18014398509481984) & (134217728*c + 37175887875*x < -1382046639294572015625/134217728)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(1382226783279666835465, 18014398509481984)), StrictLessThan(Add(Mul(Integer(134217728), Symbol('c')), Mul(Integer(37175887875), Symbol('x'))), Rational(-1382046639294572015625, 134217728)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_551(c:sympy.Rational):
	#c < 90069034801680375/18014398509481984

	pre_cond = StrictLessThan(Symbol('c'), Rational(90069034801680375, 18014398509481984))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_552(c:sympy.Rational):
	#(x**2 < 348056193601830856241/4503599627370496) & (67108864*c + 18655057159*x < -348011157605557151281/67108864)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(348056193601830856241, 4503599627370496)), StrictLessThan(Add(Mul(Integer(67108864), Symbol('c')), Mul(Integer(18655057159), Symbol('x'))), Rational(-348011157605557151281, 67108864)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_553(c:sympy.Rational):
	#c < 22517269607799247/4503599627370496

	pre_cond = StrictLessThan(Symbol('c'), Rational(22517269607799247, 4503599627370496))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_554(c:sympy.Rational):
	#(x**2 < 5609035177621307876561/72057594037927936) & (268435456*c + 74888681399*x < -5608314601680928597201/268435456)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(5609035177621307876561, 72057594037927936)), StrictLessThan(Add(Mul(Integer(268435456), Symbol('c')), Mul(Integer(74888681399), Symbol('x'))), Rational(-5608314601680928597201, 268435456)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_555(c:sympy.Rational):
	#c < 360276340691344175/72057594037927936

	pre_cond = StrictLessThan(Symbol('c'), Rational(360276340691344175, 72057594037927936))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_556(c:sympy.Rational):
	#(x**2 < 1412328843186569366201/18014398509481984) & (134217728*c + 37578567019*x < -1412148699201474546361/134217728)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(1412328843186569366201, 18014398509481984)), StrictLessThan(Add(Mul(Integer(134217728), Symbol('c')), Mul(Integer(37578567019), Symbol('x'))), Rational(-1412148699201474546361, 134217728)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_557(c:sympy.Rational):
	#c < 90069098581046599/18014398509481984

	pre_cond = StrictLessThan(Symbol('c'), Rational(90069098581046599, 18014398509481984))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_558(c:sympy.Rational):
	#(x**2 < 1422434920738831218569/18014398509481984) & (134217728*c + 37712793277*x < -1422254776753736398729/134217728)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(1422434920738831218569, 18014398509481984)), StrictLessThan(Add(Mul(Integer(134217728), Symbol('c')), Mul(Integer(37712793277), Symbol('x'))), Rational(-1422254776753736398729, 134217728)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_559(c:sympy.Rational):
	#c < 90069124768319607/18014398509481984

	pre_cond = StrictLessThan(Symbol('c'), Rational(90069124768319607, 18014398509481984))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_560(c:sympy.Rational):
	#(x**2 < 1432577027126124095465/18014398509481984) & (134217728*c + 37847019475*x < -1432396883141029275625/134217728)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(1432577027126124095465, 18014398509481984)), StrictLessThan(Add(Mul(Integer(134217728), Symbol('c')), Mul(Integer(37847019475), Symbol('x'))), Rational(-1432396883141029275625, 134217728)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_561(c:sympy.Rational):
	#c < 90069131734013975/18014398509481984

	pre_cond = StrictLessThan(Symbol('c'), Rational(90069131734013975, 18014398509481984))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_562(c:sympy.Rational):
	#(x**2 < 1442755162300126565609/18014398509481984) & (134217728*c + 37981245613*x < -1442575018315031745769/134217728)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(1442755162300126565609, 18014398509481984)), StrictLessThan(Add(Mul(Integer(134217728), Symbol('c')), Mul(Integer(37981245613), Symbol('x'))), Rational(-1442575018315031745769, 134217728)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_563(c:sympy.Rational):
	#c < 90069143640369943/18014398509481984

	pre_cond = StrictLessThan(Symbol('c'), Rational(90069143640369943, 18014398509481984))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_564(c:sympy.Rational):
	#(x**2 < 90810582893046760169/1125899906842624) & (33554432*c + 9528867923*x < -90799323893978333929/33554432)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(90810582893046760169, 1125899906842624)), StrictLessThan(Add(Mul(Integer(33554432), Symbol('c')), Mul(Integer(9528867923), Symbol('x'))), Rational(-90799323893978333929, 33554432)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_565(c:sympy.Rational):
	#c < 5629321658531095/1125899906842624

	pre_cond = StrictLessThan(Symbol('c'), Rational(5629321658531095, 1125899906842624))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_566(c:sympy.Rational):
	#(x**2 < 5715701246267472089/70368744177664) & (8388608*c + 2390606107*x < -5714997558825695449/8388608)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(5715701246267472089, 70368744177664)), StrictLessThan(Add(Mul(Integer(8388608), Symbol('c')), Mul(Integer(2390606107), Symbol('x'))), Rational(-5714997558825695449, 8388608)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_567(c:sympy.Rational):
	#c < 351832672585511/70368744177664

	pre_cond = StrictLessThan(Symbol('c'), Rational(351832672585511, 70368744177664))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_568(c:sympy.Rational):
	#(x**2 < 368376435149138119529/4503599627370496) & (67108864*c + 19191961837*x < -368331399152864414569/67108864)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(368376435149138119529, 4503599627370496)), StrictLessThan(Add(Mul(Integer(67108864), Symbol('c')), Mul(Integer(19191961837), Symbol('x'))), Rational(-368331399152864414569, 67108864)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_569(c:sympy.Rational):
	#c < 22517295488611479/4503599627370496

	pre_cond = StrictLessThan(Symbol('c'), Rational(22517295488611479, 4503599627370496))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_570(c:sympy.Rational):
	#(x**2 < 370956997724569099481/4503599627370496) & (67108864*c + 19259074789*x < -370911961728295394521/67108864)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(370956997724569099481, 4503599627370496)), StrictLessThan(Add(Mul(Integer(67108864), Symbol('c')), Mul(Integer(19259074789), Symbol('x'))), Rational(-370911961728295394521, 67108864)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_571(c:sympy.Rational):
	#c < 22517305802728231/4503599627370496

	pre_cond = StrictLessThan(Symbol('c'), Rational(22517305802728231, 4503599627370496))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_572(c:sympy.Rational):
	#(x**2 < 373546567514385875329/4503599627370496) & (67108864*c + 19326187713*x < -373501531518112170369/67108864)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(373546567514385875329, 4503599627370496)), StrictLessThan(Add(Mul(Integer(67108864), Symbol('c')), Mul(Integer(19326187713), Symbol('x'))), Rational(-373501531518112170369, 67108864)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_573(c:sympy.Rational):
	#c < 22517308501982847/4503599627370496

	pre_cond = StrictLessThan(Symbol('c'), Rational(22517308501982847, 4503599627370496))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_574(c:sympy.Rational):
	#(x**2 < 376145144507313475841/4503599627370496) & (67108864*c + 19393300609*x < -376100108511039770881/67108864)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(376145144507313475841, 4503599627370496)), StrictLessThan(Add(Mul(Integer(67108864), Symbol('c')), Mul(Integer(19393300609), Symbol('x'))), Rational(-376100108511039770881, 67108864)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_575(c:sympy.Rational):
	#c < 22517309224201983/4503599627370496

	pre_cond = StrictLessThan(Symbol('c'), Rational(22517309224201983, 4503599627370496))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_576(c:sympy.Rational):
	#(x**2 < 378752728692076934489/4503599627370496) & (67108864*c + 19460413477*x < -378707692695803229529/67108864)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(378752728692076934489, 4503599627370496)), StrictLessThan(Add(Mul(Integer(67108864), Symbol('c')), Mul(Integer(19460413477), Symbol('x'))), Rational(-378707692695803229529, 67108864)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_577(c:sympy.Rational):
	#c < 22517313607207591/4503599627370496

	pre_cond = StrictLessThan(Symbol('c'), Rational(22517313607207591, 4503599627370496))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_578(c:sympy.Rational):
	#(x**2 < 381369320057401289449/4503599627370496) & (67108864*c + 19527526317*x < -381324284061127584489/67108864)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(381369320057401289449, 4503599627370496)), StrictLessThan(Add(Mul(Integer(67108864), Symbol('c')), Mul(Integer(19527526317), Symbol('x'))), Rational(-381324284061127584489, 67108864)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_579(c:sympy.Rational):
	#c < 22517327288816919/4503599627370496

	pre_cond = StrictLessThan(Symbol('c'), Rational(22517327288816919, 4503599627370496))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_580(c:sympy.Rational):
	#(x**2 < 95998729657800215465/1125899906842624) & (33554432*c + 9797319565*x < -95987470658731789225/33554432)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(95998729657800215465, 1125899906842624)), StrictLessThan(Add(Mul(Integer(33554432), Symbol('c')), Mul(Integer(9797319565), Symbol('x'))), Rational(-95987470658731789225, 33554432)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_581(c:sympy.Rational):
	#c < 5629334078338135/1125899906842624

	pre_cond = StrictLessThan(Symbol('c'), Rational(5629334078338135, 1125899906842624))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_582(c:sympy.Rational):
	#(x**2 < 6186072390598948031585/72057594037927936) & (268435456*c + 78647007665*x < -6185351814658568752225/268435456)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(6186072390598948031585, 72057594037927936)), StrictLessThan(Add(Mul(Integer(268435456), Symbol('c')), Mul(Integer(78647007665), Symbol('x'))), Rational(-6185351814658568752225, 268435456)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_583(c:sympy.Rational):
	#c < 360277459233928095/72057594037927936

	pre_cond = StrictLessThan(Symbol('c'), Rational(360277459233928095, 72057594037927936))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_584(c:sympy.Rational):
	#(x**2 < 24329571087512143121/281474976710656) & (16777216*c + 4932216169*x < -24326756337745036561/16777216)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(24329571087512143121, 281474976710656)), StrictLessThan(Add(Mul(Integer(16777216), Symbol('c')), Mul(Integer(4932216169), Symbol('x'))), Rational(-24326756337745036561, 16777216)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_585(c:sympy.Rational):
	#c < 1407333900581615/281474976710656

	pre_cond = StrictLessThan(Symbol('c'), Rational(1407333900581615, 281474976710656))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_586(c:sympy.Rational):
	#(x**2 < 391925757573912058241/4503599627370496) & (67108864*c + 19795977409*x < -391880721577638353281/67108864)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(391925757573912058241, 4503599627370496)), StrictLessThan(Add(Mul(Integer(67108864), Symbol('c')), Mul(Integer(19795977409), Symbol('x'))), Rational(-391880721577638353281, 67108864)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_587(c:sympy.Rational):
	#c < 22517350219392639/4503599627370496

	pre_cond = StrictLessThan(Symbol('c'), Rational(22517350219392639, 4503599627370496))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_588(c:sympy.Rational):
	#(x**2 < 24661711559538162401/281474976710656) & (16777216*c + 4965772529*x < -24658896809771055841/16777216)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(24661711559538162401, 281474976710656)), StrictLessThan(Add(Mul(Integer(16777216), Symbol('c')), Mul(Integer(4965772529), Symbol('x'))), Rational(-24658896809771055841, 16777216)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_589(c:sympy.Rational):
	#c < 1407334695126303/281474976710656

	pre_cond = StrictLessThan(Symbol('c'), Rational(1407334695126303, 281474976710656))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_590(c:sympy.Rational):
	#(x**2 < 6356128312572566873081/72057594037927936) & (268435456*c + 79720811189*x < -6355407736632187593721/268435456)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(6356128312572566873081, 72057594037927936)), StrictLessThan(Add(Mul(Integer(268435456), Symbol('c')), Mul(Integer(79720811189), Symbol('x'))), Rational(-6355407736632187593721, 268435456)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_591(c:sympy.Rational):
	#c < 360277717920209927/72057594037927936

	pre_cond = StrictLessThan(Symbol('c'), Rational(360277717920209927, 72057594037927936))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_592(c:sympy.Rational):
	#(x**2 < 6399002581009082279081/72057594037927936) & (268435456*c + 79989261811*x < -6398282005068702999721/268435456)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(6399002581009082279081, 72057594037927936)), StrictLessThan(Add(Mul(Integer(268435456), Symbol('c')), Mul(Integer(79989261811), Symbol('x'))), Rational(-6398282005068702999721, 268435456)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_593(c:sympy.Rational):
	#c < 360277794369903447/72057594037927936

	pre_cond = StrictLessThan(Symbol('c'), Rational(360277794369903447, 72057594037927936))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_594(c:sympy.Rational):
	#(x**2 < 402626310294152759849/4503599627370496) & (67108864*c + 20064428083*x < -402581274297879054889/67108864)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(402626310294152759849, 4503599627370496)), StrictLessThan(Add(Mul(Integer(67108864), Symbol('c')), Mul(Integer(20064428083), Symbol('x'))), Rational(-402581274297879054889, 67108864)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_595(c:sympy.Rational):
	#c < 22517364609430999/4503599627370496

	pre_cond = StrictLessThan(Symbol('c'), Rational(22517364609430999, 4503599627370496))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_596(c:sympy.Rational):
	#(x**2 < 1583296744019036009/17592186044416) & (4194304*c + 1258221293*x < -1583120822158591849/4194304)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(1583296744019036009, 17592186044416)), StrictLessThan(Add(Mul(Integer(4194304), Symbol('c')), Mul(Integer(1258221293), Symbol('x'))), Rational(-1583120822158591849, 4194304)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_597(c:sympy.Rational):
	#c < 87958475929751/17592186044416

	pre_cond = StrictLessThan(Symbol('c'), Rational(87958475929751, 17592186044416))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_598(c:sympy.Rational):
	#(x**2 < 6528490077556161782689/72057594037927936) & (268435456*c + 80794613073*x < -6527769501615782503329/268435456)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(6528490077556161782689, 72057594037927936)), StrictLessThan(Add(Mul(Integer(268435456), Symbol('c')), Mul(Integer(80794613073), Symbol('x'))), Rational(-6527769501615782503329, 268435456)))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_599(c:sympy.Rational):
	#c < 360277965106699359/72057594037927936

	pre_cond = StrictLessThan(Symbol('c'), Rational(360277965106699359, 72057594037927936))

	eval = pre_cond.subs( { 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_600(c:sympy.Rational):
	#(x**2 < 100279858503291041/1099511627776) & (1048576*c + 316652591*x < -100268863387013281/1048576)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(100279858503291041, 1099511627776)), StrictLessThan(Add(Mul(Integer(1048576), Symbol('c')), Mul(Integer(316652591), Symbol('x'))), Rational(-100268863387013281, 1048576)))