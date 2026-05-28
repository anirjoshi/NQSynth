import sympy
from sympy import *

def pre_condition_0(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 7/4) & (b + delta >= 1/2) & (delta >= b**2 - 3) & (b - delta <= 1/2) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(7, 4)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(1, 2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(1, 2)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 1) & (b + delta >= -1) & (delta >= b**2 - 3) & (b - delta <= -1) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(1)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Integer(-1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Integer(-1)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_2(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 1) & (b + delta >= 1) & (delta >= b**2 - 3) & (b - delta <= 1) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(1)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Integer(1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Integer(1)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_3(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 1/4) & (b + delta >= 3/2) & (delta >= b**2 - 3) & (b - delta <= 3/2) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(1, 4)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(3, 2)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(3, 2)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_4(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 161/1024) & (b + delta >= 47/32) & (delta >= b**2 - 3) & (b - delta <= 47/32) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(161, 1024)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(47, 32)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(47, 32)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_5(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 1217/4096) & (b + delta >= 97/64) & (delta >= b**2 - 3) & (b - delta <= 97/64) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(1217, 4096)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(97, 64)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(97, 64)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_6(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 314657/1048576) & (b + delta >= 1553/1024) & (delta >= b**2 - 3) & (b - delta <= 1553/1024) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(314657, 1048576)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(1553, 1024)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(1553, 1024)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_7(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 5022089/16777216) & (b + delta >= 6211/4096) & (delta >= b**2 - 3) & (b - delta <= 6211/4096) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(5022089, 16777216)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(6211, 4096)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(6211, 4096)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_8(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 20113201/67108864) & (b + delta >= 12423/8192) & (delta >= b**2 - 3) & (b - delta <= 12423/8192) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(20113201, 67108864)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(12423, 8192)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(12423, 8192)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_9(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 80403113/268435456) & (b + delta >= 24845/16384) & (delta >= b**2 - 3) & (b - delta <= 24845/16384) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(80403113, 268435456)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(24845, 16384)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(24845, 16384)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_10(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 1286251049/4294967296) & (b + delta >= 99379/65536) & (delta >= b**2 - 3) & (b - delta <= 99379/65536) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(1286251049, 4294967296)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(99379, 65536)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(99379, 65536)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_11(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 1252417/4194304) & (b + delta >= 3105/2048) & (delta >= b**2 - 3) & (b - delta <= 3105/2048) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(1252417, 4194304)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(3105, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(3105, 2048)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_12(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 4997249/16777216) & (b + delta >= 6209/4096) & (delta >= b**2 - 3) & (b - delta <= 6209/4096) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(4997249, 16777216)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(6209, 4096)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(6209, 4096)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_13(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 20063513/67108864) & (b + delta >= 12421/8192) & (delta >= b**2 - 3) & (b - delta <= 12421/8192) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(20063513, 67108864)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(12421, 8192)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(12421, 8192)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_14(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 321513073/1073741824) & (b + delta >= 49689/32768) & (delta >= b**2 - 3) & (b - delta <= 49689/32768) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(321513073, 1073741824)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(49689, 32768)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(49689, 32768)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_15(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 19964161/67108864) & (b + delta >= 12417/8192) & (delta >= b**2 - 3) & (b - delta <= 12417/8192) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(19964161, 67108864)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(12417, 8192)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(12417, 8192)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_16(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 79806977/268435456) & (b + delta >= 24833/16384) & (delta >= b**2 - 3) & (b - delta <= 24833/16384) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(79806977, 268435456)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(24833, 16384)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(24833, 16384)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_17(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 81720755137/274877906944) & (b + delta >= 794655/524288) & (delta >= b**2 - 3) & (b - delta <= 794655/524288) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(81720755137, 274877906944)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(794655, 524288)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(794655, 524288)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_18(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 326886199169/1099511627776) & (b + delta >= 1589311/1048576) & (delta >= b**2 - 3) & (b - delta <= 1589311/1048576) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(326886199169, 1099511627776)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(1589311, 1048576)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(1589311, 1048576)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_19(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 319128577/1073741824) & (b + delta >= 49665/32768) & (delta >= b**2 - 3) & (b - delta <= 49665/32768) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(319128577, 1073741824)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(49665, 32768)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(49665, 32768)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_20(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 319128577/1073741824) & (b + delta >= 49665/32768) & (delta >= b**2 - 3) & (b - delta <= 49665/32768) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(319128577, 1073741824)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(49665, 32768)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(49665, 32768)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_21(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 20013833/67108864) & (b + delta >= 12419/8192) & (delta >= b**2 - 3) & (b - delta <= 12419/8192) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(20013833, 67108864)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(12419, 8192)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(12419, 8192)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_22(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 80502497/268435456) & (b + delta >= 24847/16384) & (delta >= b**2 - 3) & (b - delta <= 24847/16384) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(80502497, 268435456)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(24847, 16384)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(24847, 16384)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_23(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 1287841177/4294967296) & (b + delta >= 99387/65536) & (delta >= b**2 - 3) & (b - delta <= 99387/65536) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(1287841177, 4294967296)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(99387, 65536)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(99387, 65536)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_24(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 321910601/1073741824) & (b + delta >= 49693/32768) & (delta >= b**2 - 3) & (b - delta <= 49693/32768) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(321910601, 1073741824)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(49693, 32768)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(49693, 32768)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_25(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 5145401713/17179869184) & (b + delta >= 198759/131072) & (delta >= b**2 - 3) & (b - delta <= 198759/131072) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(5145401713, 17179869184)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(198759, 131072)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(198759, 131072)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_26(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 80105009/268435456) & (b + delta >= 24839/16384) & (delta >= b**2 - 3) & (b - delta <= 24839/16384) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(80105009, 268435456)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(24839, 16384)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(24839, 16384)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_27(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 5126323153/17179869184) & (b + delta >= 198711/131072) & (delta >= b**2 - 3) & (b - delta <= 198711/131072) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(5126323153, 17179869184)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(198711, 131072)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(198711, 131072)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_28(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 79906313/268435456) & (b + delta >= 24835/16384) & (delta >= b**2 - 3) & (b - delta <= 24835/16384) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(79906313, 268435456)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(24835, 16384)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(24835, 16384)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_29(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 80204369/268435456) & (b + delta >= 24841/16384) & (delta >= b**2 - 3) & (b - delta <= 24841/16384) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(80204369, 268435456)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(24841, 16384)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(24841, 16384)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_30(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 329283448673/1099511627776) & (b + delta >= 1590065/1048576) & (delta >= b**2 - 3) & (b - delta <= 1590065/1048576) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(329283448673, 1099511627776)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(1590065, 1048576)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(1590065, 1048576)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_31(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 5144606681/17179869184) & (b + delta >= 198757/131072) & (delta >= b**2 - 3) & (b - delta <= 198757/131072) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(5144606681, 17179869184)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(198757, 131072)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(198757, 131072)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_32(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 20506087457/68719476736) & (b + delta >= 397423/262144) & (delta >= b**2 - 3) & (b - delta <= 397423/262144) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(20506087457, 68719476736)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(397423, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(397423, 262144)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_33(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 1307538439433/4398046511104) & (b + delta >= 3178621/2097152) & (delta >= b**2 - 3) & (b - delta <= 3178621/2097152) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(1307538439433, 4398046511104)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(3178621, 2097152)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(3178621, 2097152)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_34(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 1312345085921/4398046511104) & (b + delta >= 3179377/2097152) & (delta >= b**2 - 3) & (b - delta <= 3179377/2097152) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(1312345085921, 4398046511104)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(3179377, 2097152)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(3179377, 2097152)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_35(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 319128577/1073741824) & (b + delta >= 49665/32768) & (delta >= b**2 - 3) & (b - delta <= 49665/32768) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(319128577, 1073741824)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(49665, 32768)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(49665, 32768)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_36(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 1343841571463233/4503599627370496) & (b + delta >= 101740065/67108864) & (delta >= b**2 - 3) & (b - delta <= 101740065/67108864) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(1343841571463233, 4503599627370496)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(101740065, 67108864)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(101740065, 67108864)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_37(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 1283866097/4294967296) & (b + delta >= 99367/65536) & (delta >= b**2 - 3) & (b - delta <= 99367/65536) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(1283866097, 4294967296)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(99367, 65536)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(99367, 65536)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_38(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 80303737/268435456) & (b + delta >= 24843/16384) & (delta >= b**2 - 3) & (b - delta <= 24843/16384) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(80303737, 268435456)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(24843, 16384)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(24843, 16384)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_39(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 1284661049/4294967296) & (b + delta >= 99371/65536) & (delta >= b**2 - 3) & (b - delta <= 99371/65536) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(1284661049, 4294967296)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(99371, 65536)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(99371, 65536)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_40(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 5022089/16777216) & (b + delta >= 6211/4096) & (delta >= b**2 - 3) & (b - delta <= 6211/4096) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(5022089, 16777216)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(6211, 4096)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(6211, 4096)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_41(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 5139041681/17179869184) & (b + delta >= 198743/131072) & (delta >= b**2 - 3) & (b - delta <= 198743/131072) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(5139041681, 17179869184)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(198743, 131072)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(198743, 131072)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_42(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 80204369/268435456) & (b + delta >= 24841/16384) & (delta >= b**2 - 3) & (b - delta <= 24841/16384) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(80204369, 268435456)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(24841, 16384)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(24841, 16384)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_43(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 5135861857/17179869184) & (b + delta >= 198735/131072) & (delta >= b**2 - 3) & (b - delta <= 198735/131072) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(5135861857, 17179869184)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(198735, 131072)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(198735, 131072)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_44(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 1287443633/4294967296) & (b + delta >= 99385/65536) & (delta >= b**2 - 3) & (b - delta <= 99385/65536) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(1287443633, 4294967296)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(99385, 65536)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(99385, 65536)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_45(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 1317127434433/4398046511104) & (b + delta >= 3180129/2097152) & (delta >= b**2 - 3) & (b - delta <= 3180129/2097152) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(1317127434433, 4398046511104)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(3180129, 2097152)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(3180129, 2097152)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_46(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 329308889777/1099511627776) & (b + delta >= 1590073/1048576) & (delta >= b**2 - 3) & (b - delta <= 1590073/1048576) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(329308889777, 1099511627776)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(1590073, 1048576)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(1590073, 1048576)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_47(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 5150967161/17179869184) & (b + delta >= 198773/131072) & (delta >= b**2 - 3) & (b - delta <= 198773/131072) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(5150967161, 17179869184)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(198773, 131072)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(198773, 131072)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_48(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 320916841/1073741824) & (b + delta >= 49683/32768) & (delta >= b**2 - 3) & (b - delta <= 49683/32768) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(320916841, 1073741824)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(49683, 32768)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(49683, 32768)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_49(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 319128577/1073741824) & (b + delta >= 49665/32768) & (delta >= b**2 - 3) & (b - delta <= 49665/32768) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(319128577, 1073741824)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(49665, 32768)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(49665, 32768)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_50(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 20442506177/68719476736) & (b + delta >= 397343/262144) & (delta >= b**2 - 3) & (b - delta <= 397343/262144) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(20442506177, 68719476736)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(397343, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(397343, 262144)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_51(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 1276712969/4294967296) & (b + delta >= 99331/65536) & (delta >= b**2 - 3) & (b - delta <= 99331/65536) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(1276712969, 4294967296)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(99331, 65536)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(99331, 65536)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_52(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 5116785601/17179869184) & (b + delta >= 198687/131072) & (delta >= b**2 - 3) & (b - delta <= 198687/131072) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(5116785601, 17179869184)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(198687, 131072)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(198687, 131072)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_53(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 82308936737/274877906944) & (b + delta >= 795025/524288) & (delta >= b**2 - 3) & (b - delta <= 795025/524288) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(82308936737, 274877906944)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(795025, 524288)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(795025, 524288)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_54(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 82308936737/274877906944) & (b + delta >= 795025/524288) & (delta >= b**2 - 3) & (b - delta <= 795025/524288) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(82308936737, 274877906944)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(795025, 524288)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(795025, 524288)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_55(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 322109377/1073741824) & (b + delta >= 49695/32768) & (delta >= b**2 - 3) & (b - delta <= 49695/32768) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(322109377, 1073741824)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(49695, 32768)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(49695, 32768)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_56(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 322109377/1073741824) & (b + delta >= 49695/32768) & (delta >= b**2 - 3) & (b - delta <= 49695/32768) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(322109377, 1073741824)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(49695, 32768)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(49695, 32768)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_57(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 5022089/16777216) & (b + delta >= 6211/4096) & (delta >= b**2 - 3) & (b - delta <= 6211/4096) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(5022089, 16777216)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(6211, 4096)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(6211, 4096)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_58(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 329283448673/1099511627776) & (b + delta >= 1590065/1048576) & (delta >= b**2 - 3) & (b - delta <= 1590065/1048576) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(329283448673, 1099511627776)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(1590065, 1048576)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(1590065, 1048576)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_59(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 1312395956017/4398046511104) & (b + delta >= 3179385/2097152) & (delta >= b**2 - 3) & (b - delta <= 3179385/2097152) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(1312395956017, 4398046511104)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(3179385, 2097152)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(3179385, 2097152)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_60(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 81771614081/274877906944) & (b + delta >= 794687/524288) & (delta >= b**2 - 3) & (b - delta <= 794687/524288) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(81771614081, 274877906944)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(794687, 524288)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(794687, 524288)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_61(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 319128577/1073741824) & (b + delta >= 49665/32768) & (delta >= b**2 - 3) & (b - delta <= 49665/32768) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(319128577, 1073741824)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(49665, 32768)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(49665, 32768)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_62(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 326835341473/1099511627776) & (b + delta >= 1589295/1048576) & (delta >= b**2 - 3) & (b - delta <= 1589295/1048576) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(326835341473, 1099511627776)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(1589295, 1048576)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(1589295, 1048576)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_63(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 5149376993/17179869184) & (b + delta >= 198769/131072) & (delta >= b**2 - 3) & (b - delta <= 198769/131072) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(5149376993, 17179869184)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(198769, 131072)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(198769, 131072)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_64(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 82219897073/274877906944) & (b + delta >= 794969/524288) & (delta >= b**2 - 3) & (b - delta <= 794969/524288) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(82219897073, 274877906944)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(794969, 524288)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(794969, 524288)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_65(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 82308936737/274877906944) & (b + delta >= 795025/524288) & (delta >= b**2 - 3) & (b - delta <= 795025/524288) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(82308936737, 274877906944)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(795025, 524288)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(795025, 524288)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_66(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 5150967161/17179869184) & (b + delta >= 198773/131072) & (delta >= b**2 - 3) & (b - delta <= 198773/131072) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(5150967161, 17179869184)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(198773, 131072)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(198773, 131072)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_67(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 329537865473/1099511627776) & (b + delta >= 1590145/1048576) & (delta >= b**2 - 3) & (b - delta <= 1590145/1048576) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(329537865473, 1099511627776)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(1590145, 1048576)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(1590145, 1048576)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_68(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 5150172073/17179869184) & (b + delta >= 198771/131072) & (delta >= b**2 - 3) & (b - delta <= 198771/131072) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(5150172073, 17179869184)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(198771, 131072)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(198771, 131072)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_69(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 1317229198817/4398046511104) & (b + delta >= 3180145/2097152) & (delta >= b**2 - 3) & (b - delta <= 3180145/2097152) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(1317229198817, 4398046511104)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(3180145, 2097152)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(3180145, 2097152)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_70(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 5022089/16777216) & (b + delta >= 6211/4096) & (delta >= b**2 - 3) & (b - delta <= 6211/4096) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(5022089, 16777216)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(6211, 4096)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(6211, 4096)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_71(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 20113201/67108864) & (b + delta >= 12423/8192) & (delta >= b**2 - 3) & (b - delta <= 12423/8192) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(20113201, 67108864)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(12423, 8192)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(12423, 8192)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_72(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 5135066921/17179869184) & (b + delta >= 198733/131072) & (delta >= b**2 - 3) & (b - delta <= 198733/131072) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(5135066921, 17179869184)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(198733, 131072)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(198733, 131072)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_73(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 1343841571463233/4503599627370496) & (b + delta >= 101740065/67108864) & (delta >= b**2 - 3) & (b - delta <= 101740065/67108864) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(1343841571463233, 4503599627370496)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(101740065, 67108864)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(101740065, 67108864)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_74(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 326835341473/1099511627776) & (b + delta >= 1589295/1048576) & (delta >= b**2 - 3) & (b - delta <= 1589295/1048576) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(326835341473, 1099511627776)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(1589295, 1048576)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(1589295, 1048576)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_75(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 319724593/1073741824) & (b + delta >= 49671/32768) & (delta >= b**2 - 3) & (b - delta <= 49671/32768) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(319724593, 1073741824)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(49671, 32768)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(49671, 32768)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_76(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 82169020081/274877906944) & (b + delta >= 794937/524288) & (delta >= b**2 - 3) & (b - delta <= 794937/524288) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(82169020081, 274877906944)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(794937, 524288)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(794937, 524288)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_77(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 80005657/268435456) & (b + delta >= 24837/16384) & (delta >= b**2 - 3) & (b - delta <= 24837/16384) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(80005657, 268435456)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(24837, 16384)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(24837, 16384)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_78(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 1343841571463233/4503599627370496) & (b + delta >= 101740065/67108864) & (delta >= b**2 - 3) & (b - delta <= 101740065/67108864) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(1343841571463233, 4503599627370496)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(101740065, 67108864)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(101740065, 67108864)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_79(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 5144606681/17179869184) & (b + delta >= 198757/131072) & (delta >= b**2 - 3) & (b - delta <= 198757/131072) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(5144606681, 17179869184)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(198757, 131072)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(198757, 131072)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_80(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 82169020081/274877906944) & (b + delta >= 794937/524288) & (delta >= b**2 - 3) & (b - delta <= 794937/524288) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(82169020081, 274877906944)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(794937, 524288)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(794937, 524288)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_81(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 82022760137/274877906944) & (b + delta >= 794845/524288) & (delta >= b**2 - 3) & (b - delta <= 794845/524288) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(82022760137, 274877906944)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(794845, 524288)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(794845, 524288)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_82(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 5119964657/17179869184) & (b + delta >= 198695/131072) & (delta >= b**2 - 3) & (b - delta <= 198695/131072) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(5119964657, 17179869184)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(198695, 131072)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(198695, 131072)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_83(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 20455221409/68719476736) & (b + delta >= 397359/262144) & (delta >= b**2 - 3) & (b - delta <= 397359/262144) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(20455221409, 68719476736)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(397359, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(397359, 262144)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_84(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 320320681/1073741824) & (b + delta >= 49677/32768) & (delta >= b**2 - 3) & (b - delta <= 49677/32768) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(320320681, 1073741824)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(49677, 32768)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(49677, 32768)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_85(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 329283448673/1099511627776) & (b + delta >= 1590065/1048576) & (delta >= b**2 - 3) & (b - delta <= 1590065/1048576) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(329283448673, 1099511627776)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(1590065, 1048576)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(1590065, 1048576)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_86(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 1283468633/4294967296) & (b + delta >= 99365/65536) & (delta >= b**2 - 3) & (b - delta <= 99365/65536) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(1283468633, 4294967296)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(99365, 65536)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(99365, 65536)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_87(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 1279097057/4294967296) & (b + delta >= 99343/65536) & (delta >= b**2 - 3) & (b - delta <= 99343/65536) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(1279097057, 4294967296)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(99343, 65536)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(99343, 65536)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_88(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 5268904074689/17592186044416) & (b + delta >= 6360289/4194304) & (delta >= b**2 - 3) & (b - delta <= 6360289/4194304) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(5268904074689, 17592186044416)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(6360289, 4194304)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(6360289, 4194304)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_89(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 21075641739913/70368744177664) & (b + delta >= 12720579/8388608) & (delta >= b**2 - 3) & (b - delta <= 12720579/8388608) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(21075641739913, 70368744177664)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(12720579, 8388608)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(12720579, 8388608)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_90(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 5116785601/17179869184) & (b + delta >= 198687/131072) & (delta >= b**2 - 3) & (b - delta <= 198687/131072) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(5116785601, 17179869184)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(198687, 131072)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(198687, 131072)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_91(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 5133477073/17179869184) & (b + delta >= 198729/131072) & (delta >= b**2 - 3) & (b - delta <= 198729/131072) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(5133477073, 17179869184)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(198729, 131072)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(198729, 131072)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_92(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 320320681/1073741824) & (b + delta >= 49677/32768) & (delta >= b**2 - 3) & (b - delta <= 49677/32768) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(320320681, 1073741824)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(49677, 32768)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(49677, 32768)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_93(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 5123143841/17179869184) & (b + delta >= 198703/131072) & (delta >= b**2 - 3) & (b - delta <= 198703/131072) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(5123143841, 17179869184)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(198703, 131072)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(198703, 131072)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_94(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 1312370520953/4398046511104) & (b + delta >= 3179381/2097152) & (delta >= b**2 - 3) & (b - delta <= 3179381/2097152) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(1312370520953, 4398046511104)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(3179381, 2097152)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(3179381, 2097152)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_95(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 1343841571463233/4503599627370496) & (b + delta >= 101740065/67108864) & (delta >= b**2 - 3) & (b - delta <= 101740065/67108864) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(1343841571463233, 4503599627370496)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(101740065, 67108864)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(101740065, 67108864)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_96(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 321513073/1073741824) & (b + delta >= 49689/32768) & (delta >= b**2 - 3) & (b - delta <= 49689/32768) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(321513073, 1073741824)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(49689, 32768)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(49689, 32768)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_97(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 5268929515849/17592186044416) & (b + delta >= 6360291/4194304) & (delta >= b**2 - 3) & (b - delta <= 6360291/4194304) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(5268929515849, 17592186044416)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(6360291, 4194304)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(6360291, 4194304)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_98(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 20493370177/68719476736) & (b + delta >= 397407/262144) & (delta >= b**2 - 3) & (b - delta <= 397407/262144) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(20493370177, 68719476736)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(397407, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(397407, 262144)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_99(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 1281481433/4294967296) & (b + delta >= 99355/65536) & (delta >= b**2 - 3) & (b - delta <= 99355/65536) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(1281481433, 4294967296)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(99355, 65536)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(99355, 65536)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_100(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 21075641739913/70368744177664) & (b + delta >= 12720579/8388608) & (delta >= b**2 - 3) & (b - delta <= 12720579/8388608) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(21075641739913, 70368744177664)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(12720579, 8388608)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(12720579, 8388608)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_101(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 82308936737/274877906944) & (b + delta >= 795025/524288) & (delta >= b**2 - 3) & (b - delta <= 795025/524288) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(82308936737, 274877906944)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(795025, 524288)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(795025, 524288)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_102(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 1317140154953/4398046511104) & (b + delta >= 3180131/2097152) & (delta >= b**2 - 3) & (b - delta <= 3180131/2097152) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(1317140154953, 4398046511104)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(3180131, 2097152)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(3180131, 2097152)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_103(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 82219897073/274877906944) & (b + delta >= 794969/524288) & (delta >= b**2 - 3) & (b - delta <= 794969/524288) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(82219897073, 274877906944)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(794969, 524288)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(794969, 524288)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_104(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 82025939521/274877906944) & (b + delta >= 794847/524288) & (delta >= b**2 - 3) & (b - delta <= 794847/524288) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(82025939521, 274877906944)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(794847, 524288)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(794847, 524288)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_105(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 20480653409/68719476736) & (b + delta >= 397391/262144) & (delta >= b**2 - 3) & (b - delta <= 397391/262144) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(20480653409, 68719476736)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(397391, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(397391, 262144)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_106(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 328087861169/1099511627776) & (b + delta >= 1589689/1048576) & (delta >= b**2 - 3) & (b - delta <= 1589689/1048576) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(328087861169, 1099511627776)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(1589689, 1048576)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(1589689, 1048576)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_107(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 5355677854781057/18014398509481984) & (b + delta >= 203431745/134217728) & (delta >= b**2 - 3) & (b - delta <= 203431745/134217728) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(5355677854781057, 18014398509481984)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(203431745, 134217728)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(203431745, 134217728)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_108(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 1307551153921/4398046511104) & (b + delta >= 3178623/2097152) & (delta >= b**2 - 3) & (b - delta <= 3178623/2097152) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(1307551153921, 4398046511104)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(3178623, 2097152)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(3178623, 2097152)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_109(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 83993290314929/281474976710656) & (b + delta >= 25435079/16777216) & (delta >= b**2 - 3) & (b - delta <= 25435079/16777216) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(83993290314929, 281474976710656)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(25435079, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(25435079, 16777216)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_110(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 328672900577/1099511627776) & (b + delta >= 1589873/1048576) & (delta >= b**2 - 3) & (b - delta <= 1589873/1048576) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(328672900577, 1099511627776)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(1589873, 1048576)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(1589873, 1048576)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_111(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 83993290314929/281474976710656) & (b + delta >= 25435079/16777216) & (delta >= b**2 - 3) & (b - delta <= 25435079/16777216) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(83993290314929, 281474976710656)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(25435079, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(25435079, 16777216)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_112(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 319327241/1073741824) & (b + delta >= 49667/32768) & (delta >= b**2 - 3) & (b - delta <= 49667/32768) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(319327241, 1073741824)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(49667, 32768)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(49667, 32768)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_113(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 327897102089/1099511627776) & (b + delta >= 1589629/1048576) & (delta >= b**2 - 3) & (b - delta <= 1589629/1048576) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(327897102089, 1099511627776)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(1589629, 1048576)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(1589629, 1048576)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_114(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 80204369/268435456) & (b + delta >= 24841/16384) & (delta >= b**2 - 3) & (b - delta <= 24841/16384) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(80204369, 268435456)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(24841, 16384)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(24841, 16384)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_115(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 327693633673/1099511627776) & (b + delta >= 1589565/1048576) & (delta >= b**2 - 3) & (b - delta <= 1589565/1048576) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(327693633673, 1099511627776)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(1589565, 1048576)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(1589565, 1048576)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_116(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 1312357803433/4398046511104) & (b + delta >= 3179379/2097152) & (delta >= b**2 - 3) & (b - delta <= 3179379/2097152) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(1312357803433, 4398046511104)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(3179379, 2097152)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(3179379, 2097152)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_117(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 336557895883777/1125899906842624) & (b + delta >= 50875905/33554432) & (delta >= b**2 - 3) & (b - delta <= 50875905/33554432) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(336557895883777, 1125899906842624)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(50875905, 33554432)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(50875905, 33554432)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_118(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 1317241919401/4398046511104) & (b + delta >= 3180147/2097152) & (delta >= b**2 - 3) & (b - delta <= 3180147/2097152) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(1317241919401, 4398046511104)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(3180147, 2097152)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(3180147, 2097152)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_119(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 20596712897/68719476736) & (b + delta >= 397537/262144) & (delta >= b**2 - 3) & (b - delta <= 397537/262144) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(20596712897, 68719476736)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(397537, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(397537, 262144)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_120(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 82308936737/274877906944) & (b + delta >= 795025/524288) & (delta >= b**2 - 3) & (b - delta <= 795025/524288) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(82308936737, 274877906944)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(795025, 524288)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(795025, 524288)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_121(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 1312421391113/4398046511104) & (b + delta >= 3179389/2097152) & (delta >= b**2 - 3) & (b - delta <= 3179389/2097152) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(1312421391113, 4398046511104)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(3179389, 2097152)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(3179389, 2097152)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_122(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 327089635073/1099511627776) & (b + delta >= 1589375/1048576) & (delta >= b**2 - 3) & (b - delta <= 1589375/1048576) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(327089635073, 1099511627776)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(1589375, 1048576)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(1589375, 1048576)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_123(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 319724593/1073741824) & (b + delta >= 49671/32768) & (delta >= b**2 - 3) & (b - delta <= 49671/32768) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(319724593, 1073741824)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(49671, 32768)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(49671, 32768)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_124(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 81921024073/274877906944) & (b + delta >= 794781/524288) & (delta >= b**2 - 3) & (b - delta <= 794781/524288) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(81921024073, 274877906944)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(794781, 524288)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(794781, 524288)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_125(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 344635184447193089/1152921504606846976) & (b + delta >= 1628028929/1073741824) & (delta >= b**2 - 3) & (b - delta <= 1628028929/1073741824) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(344635184447193089, 1152921504606846976)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(1628028929, 1073741824)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(1628028929, 1073741824)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_126(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 5125528313/17179869184) & (b + delta >= 198709/131072) & (delta >= b**2 - 3) & (b - delta <= 198709/131072) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(5125528313, 17179869184)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(198709, 131072)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(198709, 131072)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_127(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 21422710605397249/72057594037927936) & (b + delta >= 406863489/268435456) & (delta >= b**2 - 3) & (b - delta <= 406863489/268435456) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(21422710605397249, 72057594037927936)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(406863489, 268435456)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(406863489, 268435456)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_128(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 82175379593/274877906944) & (b + delta >= 794941/524288) & (delta >= b**2 - 3) & (b - delta <= 794941/524288) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(82175379593, 274877906944)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(794941, 524288)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(794941, 524288)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_129(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 20582401889/68719476736) & (b + delta >= 397519/262144) & (delta >= b**2 - 3) & (b - delta <= 397519/262144) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(20582401889, 68719476736)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(397519, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(397519, 262144)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_130(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 328698338609/1099511627776) & (b + delta >= 1589881/1048576) & (delta >= b**2 - 3) & (b - delta <= 1589881/1048576) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(328698338609, 1099511627776)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(1589881, 1048576)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(1589881, 1048576)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_131(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 21501671065367297/72057594037927936) & (b + delta >= 406960513/268435456) & (delta >= b**2 - 3) & (b - delta <= 406960513/268435456) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(21501671065367297, 72057594037927936)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(406960513, 268435456)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(406960513, 268435456)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_132(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 328100578697/1099511627776) & (b + delta >= 1589693/1048576) & (delta >= b**2 - 3) & (b - delta <= 1589693/1048576) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(328100578697, 1099511627776)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(1589693, 1048576)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(1589693, 1048576)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_133(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 21075692622233/70368744177664) & (b + delta >= 12720581/8388608) & (delta >= b**2 - 3) & (b - delta <= 12720581/8388608) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(21075692622233, 70368744177664)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(12720581, 8388608)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(12720581, 8388608)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_134(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 21075641739913/70368744177664) & (b + delta >= 12720579/8388608) & (delta >= b**2 - 3) & (b - delta <= 12720579/8388608) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(21075641739913, 70368744177664)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(12720579, 8388608)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(12720579, 8388608)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_135(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 5249393061193/17592186044416) & (b + delta >= 6358755/4194304) & (delta >= b**2 - 3) & (b - delta <= 6358755/4194304) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(5249393061193, 17592186044416)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(6358755, 4194304)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(6358755, 4194304)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_136(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 5106454553/17179869184) & (b + delta >= 198661/131072) & (delta >= b**2 - 3) & (b - delta <= 198661/131072) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(5106454553, 17179869184)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(198661, 131072)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(198661, 131072)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_137(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 319525913/1073741824) & (b + delta >= 49669/32768) & (delta >= b**2 - 3) & (b - delta <= 49669/32768) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(319525913, 1073741824)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(49669, 32768)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(49669, 32768)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_138(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 81975070337/274877906944) & (b + delta >= 794815/524288) & (delta >= b**2 - 3) & (b - delta <= 794815/524288) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(81975070337, 274877906944)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(794815, 524288)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(794815, 524288)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_139(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 319128577/1073741824) & (b + delta >= 49665/32768) & (delta >= b**2 - 3) & (b - delta <= 49665/32768) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(319128577, 1073741824)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(49665, 32768)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(49665, 32768)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_140(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 21036871737697/70368744177664) & (b + delta >= 12719055/8388608) & (delta >= b**2 - 3) & (b - delta <= 12719055/8388608) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(21036871737697, 70368744177664)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(12719055, 8388608)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(12719055, 8388608)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_141(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 327884385073/1099511627776) & (b + delta >= 1589625/1048576) & (delta >= b**2 - 3) & (b - delta <= 1589625/1048576) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(327884385073, 1099511627776)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(1589625, 1048576)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(1589625, 1048576)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_142(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 81921024073/274877906944) & (b + delta >= 794781/524288) & (delta >= b**2 - 3) & (b - delta <= 794781/524288) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(81921024073, 274877906944)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(794781, 524288)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(794781, 524288)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_143(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 5375391924353281/18014398509481984) & (b + delta >= 203480193/134217728) & (delta >= b**2 - 3) & (b - delta <= 203480193/134217728) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(5375391924353281, 18014398509481984)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(203480193, 134217728)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(203480193, 134217728)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_144(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 1312408673561/4398046511104) & (b + delta >= 3179387/2097152) & (delta >= b**2 - 3) & (b - delta <= 3179387/2097152) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(1312408673561, 4398046511104)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(3179387, 2097152)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(3179387, 2097152)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_145(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 5116785601/17179869184) & (b + delta >= 198687/131072) & (delta >= b**2 - 3) & (b - delta <= 198687/131072) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(5116785601, 17179869184)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(198687, 131072)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(198687, 131072)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_146(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 5022089/16777216) & (b + delta >= 6211/4096) & (delta >= b**2 - 3) & (b - delta <= 6211/4096) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(5022089, 16777216)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(6211, 4096)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(6211, 4096)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_147(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 20539472753/68719476736) & (b + delta >= 397465/262144) & (delta >= b**2 - 3) & (b - delta <= 397465/262144) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(20539472753, 68719476736)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(397465, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(397465, 262144)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_148(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 85691674050821633/288230376151711744) & (b + delta >= 813727489/536870912) & (delta >= b**2 - 3) & (b - delta <= 813727489/536870912) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(85691674050821633, 288230376151711744)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(813727489, 536870912)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(813727489, 536870912)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_149(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 1310768176433/4398046511104) & (b + delta >= 3179129/2097152) & (delta >= b**2 - 3) & (b - delta <= 3179129/2097152) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(1310768176433, 4398046511104)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(3179129, 2097152)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(3179129, 2097152)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_150(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 83942421156929/281474976710656) & (b + delta >= 25434079/16777216) & (delta >= b**2 - 3) & (b - delta <= 25434079/16777216) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(83942421156929, 281474976710656)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(25434079, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(25434079, 16777216)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_151(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 5106454553/17179869184) & (b + delta >= 198661/131072) & (delta >= b**2 - 3) & (b - delta <= 198661/131072) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(5106454553, 17179869184)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(198661, 131072)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(198661, 131072)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_152(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 1376106954694875217/4611686018427387904) & (b + delta >= 3255684105/2147483648) & (delta >= b**2 - 3) & (b - delta <= 3255684105/2147483648) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(1376106954694875217, 4611686018427387904)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(3255684105, 2147483648)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(3255684105, 2147483648)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_153(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 1343835060100097/4503599627370496) & (b + delta >= 101740033/67108864) & (delta >= b**2 - 3) & (b - delta <= 101740033/67108864) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(1343835060100097, 4503599627370496)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(101740033, 67108864)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(101740033, 67108864)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_154(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 5504427805756764449/18446744073709551616) & (b + delta >= 6511368209/4294967296) & (delta >= b**2 - 3) & (b - delta <= 6511368209/4294967296) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(5504427805756764449, 18446744073709551616)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(6511368209, 4294967296)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(6511368209, 4294967296)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_155(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 5504427805756764449/18446744073709551616) & (b + delta >= 6511368209/4294967296) & (delta >= b**2 - 3) & (b - delta <= 6511368209/4294967296) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(5504427805756764449, 18446744073709551616)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(6511368209, 4294967296)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(6511368209, 4294967296)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_156(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 20596712897/68719476736) & (b + delta >= 397537/262144) & (delta >= b**2 - 3) & (b - delta <= 397537/262144) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(20596712897, 68719476736)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(397537, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(397537, 262144)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_157(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 21074217038201/70368744177664) & (b + delta >= 12720523/8388608) & (delta >= b**2 - 3) & (b - delta <= 12720523/8388608) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(21074217038201, 70368744177664)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(12720523, 8388608)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(12720523, 8388608)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_158(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 82226256841/274877906944) & (b + delta >= 794973/524288) & (delta >= b**2 - 3) & (b - delta <= 794973/524288) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(82226256841, 274877906944)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(794973, 524288)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(794973, 524288)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_159(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 82308936737/274877906944) & (b + delta >= 795025/524288) & (delta >= b**2 - 3) & (b - delta <= 795025/524288) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(82308936737, 274877906944)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(795025, 524288)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(795025, 524288)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_160(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 82169020081/274877906944) & (b + delta >= 794937/524288) & (delta >= b**2 - 3) & (b - delta <= 794937/524288) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(82169020081, 274877906944)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(794937, 524288)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(794937, 524288)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_161(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 5022089/16777216) & (b + delta >= 6211/4096) & (delta >= b**2 - 3) & (b - delta <= 6211/4096) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(5022089, 16777216)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(6211, 4096)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(6211, 4096)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_162(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 21036871737697/70368744177664) & (b + delta >= 12719055/8388608) & (delta >= b**2 - 3) & (b - delta <= 12719055/8388608) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(21036871737697, 70368744177664)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(12719055, 8388608)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(12719055, 8388608)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_163(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 20113201/67108864) & (b + delta >= 12423/8192) & (delta >= b**2 - 3) & (b - delta <= 12423/8192) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(20113201, 67108864)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(12423, 8192)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(12423, 8192)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_164(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 20577631697/68719476736) & (b + delta >= 397513/262144) & (delta >= b**2 - 3) & (b - delta <= 397513/262144) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(20577631697, 68719476736)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(397513, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(397513, 262144)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_165(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 5134271993/17179869184) & (b + delta >= 198731/131072) & (delta >= b**2 - 3) & (b - delta <= 198731/131072) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(5134271993, 17179869184)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(198731, 131072)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(198731, 131072)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_166(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 329238927049/1099511627776) & (b + delta >= 1590051/1048576) & (delta >= b**2 - 3) & (b - delta <= 1590051/1048576) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(329238927049, 1099511627776)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(1590051, 1048576)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(1590051, 1048576)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_167(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 82219897073/274877906944) & (b + delta >= 794969/524288) & (delta >= b**2 - 3) & (b - delta <= 794969/524288) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(82219897073, 274877906944)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(794969, 524288)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(794969, 524288)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_168(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 20480653409/68719476736) & (b + delta >= 397391/262144) & (delta >= b**2 - 3) & (b - delta <= 397391/262144) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(20480653409, 68719476736)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(397391, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(397391, 262144)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_169(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 20480653409/68719476736) & (b + delta >= 397391/262144) & (delta >= b**2 - 3) & (b - delta <= 397391/262144) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(20480653409, 68719476736)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(397391, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(397391, 262144)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_170(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 20536293049/68719476736) & (b + delta >= 397461/262144) & (delta >= b**2 - 3) & (b - delta <= 397461/262144) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(20536293049, 68719476736)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(397461, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(397461, 262144)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_171(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 1376100234963947521/4611686018427387904) & (b + delta >= 3255683073/2147483648) & (delta >= b**2 - 3) & (b - delta <= 3255683073/2147483648) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(1376100234963947521, 4611686018427387904)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(3255683073, 2147483648)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(3255683073, 2147483648)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_172(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 20480653409/68719476736) & (b + delta >= 397391/262144) & (delta >= b**2 - 3) & (b - delta <= 397391/262144) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(20480653409, 68719476736)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(397391, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(397391, 262144)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_173(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 1376100234963947521/4611686018427387904) & (b + delta >= 3255683073/2147483648) & (delta >= b**2 - 3) & (b - delta <= 3255683073/2147483648) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(1376100234963947521, 4611686018427387904)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(3255683073, 2147483648)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(3255683073, 2147483648)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_174(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 20480653409/68719476736) & (b + delta >= 397391/262144) & (delta >= b**2 - 3) & (b - delta <= 397391/262144) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(20480653409, 68719476736)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(397391, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(397391, 262144)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_175(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 336561151942721/1125899906842624) & (b + delta >= 50875937/33554432) & (delta >= b**2 - 3) & (b - delta <= 50875937/33554432) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(336561151942721, 1125899906842624)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(50875937, 33554432)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(50875937, 33554432)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_176(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 328704698137/1099511627776) & (b + delta >= 1589883/1048576) & (delta >= b**2 - 3) & (b - delta <= 1589883/1048576) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(328704698137, 1099511627776)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(1589883, 1048576)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(1589883, 1048576)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_177(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 84296919034897/281474976710656) & (b + delta >= 25441047/16777216) & (delta >= b**2 - 3) & (b - delta <= 25441047/16777216) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(84296919034897, 281474976710656)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(25441047, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(25441047, 16777216)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_178(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 5144606681/17179869184) & (b + delta >= 198757/131072) & (delta >= b**2 - 3) & (b - delta <= 198757/131072) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(5144606681, 17179869184)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(198757, 131072)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(198757, 131072)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_179(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 20504497769/68719476736) & (b + delta >= 397421/262144) & (delta >= b**2 - 3) & (b - delta <= 397421/262144) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(20504497769, 68719476736)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(397421, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(397421, 262144)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_180(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 20577631697/68719476736) & (b + delta >= 397513/262144) & (delta >= b**2 - 3) & (b - delta <= 397513/262144) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(20577631697, 68719476736)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(397513, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(397513, 262144)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_181(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 328094219929/1099511627776) & (b + delta >= 1589691/1048576) & (delta >= b**2 - 3) & (b - delta <= 1589691/1048576) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(328094219929, 1099511627776)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(1589691, 1048576)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(1589691, 1048576)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_182(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 5358984907292161/18014398509481984) & (b + delta >= 203439873/134217728) & (delta >= b**2 - 3) & (b - delta <= 203439873/134217728) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(5358984907292161, 18014398509481984)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(203439873, 134217728)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(203439873, 134217728)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_183(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 1343014644731009/4503599627370496) & (b + delta >= 101736001/67108864) & (delta >= b**2 - 3) & (b - delta <= 101736001/67108864) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(1343014644731009, 4503599627370496)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(101736001, 67108864)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(101736001, 67108864)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_184(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 327897102089/1099511627776) & (b + delta >= 1589629/1048576) & (delta >= b**2 - 3) & (b - delta <= 1589629/1048576) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(327897102089, 1099511627776)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(1589629, 1048576)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(1589629, 1048576)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_185(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 327897102089/1099511627776) & (b + delta >= 1589629/1048576) & (delta >= b**2 - 3) & (b - delta <= 1589629/1048576) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(327897102089, 1099511627776)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(1589629, 1048576)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(1589629, 1048576)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_186(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 5375469246862721/18014398509481984) & (b + delta >= 203480383/134217728) & (delta >= b**2 - 3) & (b - delta <= 203480383/134217728) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(5375469246862721, 18014398509481984)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(203480383, 134217728)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(203480383, 134217728)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_187(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 21501877801372417/72057594037927936) & (b + delta >= 406960767/268435456) & (delta >= b**2 - 3) & (b - delta <= 406960767/268435456) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(21501877801372417, 72057594037927936)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(406960767, 268435456)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(406960767, 268435456)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_188(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 5249571106529/17592186044416) & (b + delta >= 6358769/4194304) & (delta >= b**2 - 3) & (b - delta <= 6358769/4194304) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(5249571106529, 17592186044416)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(6358769, 4194304)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(6358769, 4194304)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_189(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 1348750093973233/4503599627370496) & (b + delta >= 101764185/67108864) & (delta >= b**2 - 3) & (b - delta <= 101764185/67108864) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(1348750093973233, 4503599627370496)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(101764185, 67108864)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(101764185, 67108864)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_190(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 20577631697/68719476736) & (b + delta >= 397513/262144) & (delta >= b**2 - 3) & (b - delta <= 397513/262144) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(20577631697, 68719476736)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(397513, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(397513, 262144)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_191(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 329537865473/1099511627776) & (b + delta >= 1590145/1048576) & (delta >= b**2 - 3) & (b - delta <= 1590145/1048576) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(329537865473, 1099511627776)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(1590145, 1048576)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(1590145, 1048576)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_192(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 20537882897/68719476736) & (b + delta >= 397463/262144) & (delta >= b**2 - 3) & (b - delta <= 397463/262144) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(20537882897, 68719476736)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(397463, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(397463, 262144)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_193(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 328094219929/1099511627776) & (b + delta >= 1589691/1048576) & (delta >= b**2 - 3) & (b - delta <= 1589691/1048576) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(328094219929, 1099511627776)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(1589691, 1048576)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(1589691, 1048576)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_194(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 83994104237713/281474976710656) & (b + delta >= 25435095/16777216) & (delta >= b**2 - 3) & (b - delta <= 25435095/16777216) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(83994104237713, 281474976710656)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(25435095, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(25435095, 16777216)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_195(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 5249571106529/17592186044416) & (b + delta >= 6358769/4194304) & (delta >= b**2 - 3) & (b - delta <= 6358769/4194304) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(5249571106529, 17592186044416)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(6358769, 4194304)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(6358769, 4194304)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_196(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 83942421156929/281474976710656) & (b + delta >= 25434079/16777216) & (delta >= b**2 - 3) & (b - delta <= 25434079/16777216) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(83942421156929, 281474976710656)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(25434079, 16777216)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(25434079, 16777216)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_197(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 5249393061193/17592186044416) & (b + delta >= 6358755/4194304) & (delta >= b**2 - 3) & (b - delta <= 6358755/4194304) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(5249393061193, 17592186044416)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(6358755, 4194304)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(6358755, 4194304)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_198(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 328094219929/1099511627776) & (b + delta >= 1589691/1048576) & (delta >= b**2 - 3) & (b - delta <= 1589691/1048576) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(328094219929, 1099511627776)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(1589691, 1048576)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(1589691, 1048576)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_199(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 328094219929/1099511627776) & (b + delta >= 1589691/1048576) & (delta >= b**2 - 3) & (b - delta <= 1589691/1048576) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(328094219929, 1099511627776)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(1589691, 1048576)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(1589691, 1048576)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_200(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 327897102089/1099511627776) & (b + delta >= 1589629/1048576) & (delta >= b**2 - 3) & (b - delta <= 1589629/1048576) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(327897102089, 1099511627776)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(1589629, 1048576)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(1589629, 1048576)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_201(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 5249393061193/17592186044416) & (b + delta >= 6358755/4194304) & (delta >= b**2 - 3) & (b - delta <= 6358755/4194304) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(5249393061193, 17592186044416)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(6358755, 4194304)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(6358755, 4194304)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_202(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 1346244404267137/4503599627370496) & (b + delta >= 101751873/67108864) & (delta >= b**2 - 3) & (b - delta <= 101751873/67108864) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(1346244404267137, 4503599627370496)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(101751873, 67108864)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(101751873, 67108864)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_203(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 329238927049/1099511627776) & (b + delta >= 1590051/1048576) & (delta >= b**2 - 3) & (b - delta <= 1590051/1048576) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(329238927049, 1099511627776)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(1590051, 1048576)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(1590051, 1048576)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_204(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 20113201/67108864) & (b + delta >= 12423/8192) & (delta >= b**2 - 3) & (b - delta <= 12423/8192) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(20113201, 67108864)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(12423, 8192)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(12423, 8192)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_205(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 1311594766873/4398046511104) & (b + delta >= 3179259/2097152) & (delta >= b**2 - 3) & (b - delta <= 3179259/2097152) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(1311594766873, 4398046511104)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(3179259, 2097152)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(3179259, 2097152)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_206(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 1338913055596289/4503599627370496) & (b + delta >= 101715841/67108864) & (delta >= b**2 - 3) & (b - delta <= 101715841/67108864) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(1338913055596289, 4503599627370496)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(101715841, 67108864)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(101715841, 67108864)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_207(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 1376106902603929601/4611686018427387904) & (b + delta >= 3255684097/2147483648) & (delta >= b**2 - 3) & (b - delta <= 3255684097/2147483648) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(1376106902603929601, 4611686018427387904)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(3255684097, 2147483648)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(3255684097, 2147483648)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_208(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 321115577/1073741824) & (b + delta >= 49685/32768) & (delta >= b**2 - 3) & (b - delta <= 49685/32768) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(321115577, 1073741824)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(49685, 32768)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(49685, 32768)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_209(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 5149376993/17179869184) & (b + delta >= 198769/131072) & (delta >= b**2 - 3) & (b - delta <= 198769/131072) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(5149376993, 17179869184)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(198769, 131072)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(198769, 131072)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_210(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 5150967161/17179869184) & (b + delta >= 198773/131072) & (delta >= b**2 - 3) & (b - delta <= 198773/131072) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(5150967161, 17179869184)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(198773, 131072)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(198773, 131072)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_211(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 5249571106529/17592186044416) & (b + delta >= 6358769/4194304) & (delta >= b**2 - 3) & (b - delta <= 6358769/4194304) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(5249571106529, 17592186044416)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(6358769, 4194304)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(6358769, 4194304)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_212(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 21435940442928137/72057594037927936) & (b + delta >= 406879747/268435456) & (delta >= b**2 - 3) & (b - delta <= 406879747/268435456) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(21435940442928137, 72057594037927936)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(406879747, 268435456)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(406879747, 268435456)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_213(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 5249571106529/17592186044416) & (b + delta >= 6358769/4194304) & (delta >= b**2 - 3) & (b - delta <= 6358769/4194304) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(5249571106529, 17592186044416)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(6358769, 4194304)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(6358769, 4194304)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_214(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 86006682633627137/288230376151711744) & (b + delta >= 813921025/536870912) & (delta >= b**2 - 3) & (b - delta <= 813921025/536870912) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(86006682633627137, 288230376151711744)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(813921025, 536870912)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(813921025, 536870912)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_215(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 319525913/1073741824) & (b + delta >= 49669/32768) & (delta >= b**2 - 3) & (b - delta <= 49669/32768) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(319525913, 1073741824)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(49669, 32768)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(49669, 32768)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_216(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 5504427805756764449/18446744073709551616) & (b + delta >= 6511368209/4294967296) & (delta >= b**2 - 3) & (b - delta <= 6511368209/4294967296) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(5504427805756764449, 18446744073709551616)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(6511368209, 4294967296)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(6511368209, 4294967296)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_217(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 20480653409/68719476736) & (b + delta >= 397391/262144) & (delta >= b**2 - 3) & (b - delta <= 397391/262144) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(20480653409, 68719476736)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(397391, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(397391, 262144)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_218(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 327897102089/1099511627776) & (b + delta >= 1589629/1048576) & (delta >= b**2 - 3) & (b - delta <= 1589629/1048576) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(327897102089, 1099511627776)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(1589629, 1048576)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(1589629, 1048576)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_219(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 82153121441/274877906944) & (b + delta >= 794927/524288) & (delta >= b**2 - 3) & (b - delta <= 794927/524288) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(82153121441, 274877906944)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(794927, 524288)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(794927, 524288)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_220(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 5135066921/17179869184) & (b + delta >= 198733/131072) & (delta >= b**2 - 3) & (b - delta <= 198733/131072) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(5135066921, 17179869184)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(198733, 131072)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(198733, 131072)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_221(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 5268954957017/17592186044416) & (b + delta >= 6360293/4194304) & (delta >= b**2 - 3) & (b - delta <= 6360293/4194304) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(5268954957017, 17592186044416)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(6360293, 4194304)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(6360293, 4194304)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_222(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 21037075242641/70368744177664) & (b + delta >= 12719063/8388608) & (delta >= b**2 - 3) & (b - delta <= 12719063/8388608) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(21037075242641, 70368744177664)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(12719063, 8388608)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(12719063, 8388608)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_223(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 20480653409/68719476736) & (b + delta >= 397391/262144) & (delta >= b**2 - 3) & (b - delta <= 397391/262144) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(20480653409, 68719476736)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(397391, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(397391, 262144)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_224(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 319327241/1073741824) & (b + delta >= 49667/32768) & (delta >= b**2 - 3) & (b - delta <= 49667/32768) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(319327241, 1073741824)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(49667, 32768)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(49667, 32768)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_225(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 1312383238481/4398046511104) & (b + delta >= 3179383/2097152) & (delta >= b**2 - 3) & (b - delta <= 3179383/2097152) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(1312383238481, 4398046511104)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(3179383, 2097152)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(3179383, 2097152)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_226(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 335970007310881/1125899906842624) & (b + delta >= 50870127/33554432) & (delta >= b**2 - 3) & (b - delta <= 50870127/33554432) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(335970007310881, 1125899906842624)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(50870127, 33554432)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(50870127, 33554432)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_227(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 20544242369/68719476736) & (b + delta >= 397471/262144) & (delta >= b**2 - 3) & (b - delta <= 397471/262144) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(20544242369, 68719476736)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(397471, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(397471, 262144)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_228(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 5249571106529/17592186044416) & (b + delta >= 6358769/4194304) & (delta >= b**2 - 3) & (b - delta <= 6358769/4194304) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(5249571106529, 17592186044416)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(6358769, 4194304)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(6358769, 4194304)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_229(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 21435940442928137/72057594037927936) & (b + delta >= 406879747/268435456) & (delta >= b**2 - 3) & (b - delta <= 406879747/268435456) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(21435940442928137, 72057594037927936)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(406879747, 268435456)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(406879747, 268435456)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_230(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 5355703894048513/18014398509481984) & (b + delta >= 203431809/134217728) & (delta >= b**2 - 3) & (b - delta <= 203431809/134217728) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(5355703894048513, 18014398509481984)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(203431809, 134217728)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(203431809, 134217728)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_231(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 85690847303950873/288230376151711744) & (b + delta >= 813726981/536870912) & (delta >= b**2 - 3) & (b - delta <= 813726981/536870912) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(85690847303950873, 288230376151711744)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(813726981, 536870912)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(813726981, 536870912)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_232(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 20480653409/68719476736) & (b + delta >= 397391/262144) & (delta >= b**2 - 3) & (b - delta <= 397391/262144) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(20480653409, 68719476736)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(397391, 262144)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(397391, 262144)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_233(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 87801608773155373313/295147905179352825856) & (b + delta >= 26040303745/17179869184) & (delta >= b**2 - 3) & (b - delta <= 26040303745/17179869184) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(87801608773155373313, 295147905179352825856)), GreaterThan(Add(Symbol('b'), Symbol('delta')), Rational(26040303745, 17179869184)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), LessThan(Add(Symbol('b'), Mul(Integer(-1), Symbol('delta'))), Rational(26040303745, 17179869184)), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))