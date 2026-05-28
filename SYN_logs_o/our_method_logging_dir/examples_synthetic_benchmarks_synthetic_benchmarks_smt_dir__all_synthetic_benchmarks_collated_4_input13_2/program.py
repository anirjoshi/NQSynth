import sympy
from sympy import *
from NQS.helper_program_cav import get_lambda_val

def pre_condition_0(a:sympy.Rational,b:sympy.Rational):
	#(8*b + 7 > 0) & (8*b - 9 < 0) & ((64*a**2 - 63 < 0) | (16*a**4 + 32*a**2*b**2 - 8*a**2*b - 63*a**2 + 16*b**4 - 8*b**3 + b**2 < 0))

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(8), Symbol('b')), Integer(7)), Integer(0)), StrictLessThan(Add(Mul(Integer(8), Symbol('b')), Integer(-9)), Integer(0)), Or(StrictLessThan(Add(Mul(Integer(64), Pow(Symbol('a'), Integer(2))), Integer(-63)), Integer(0)), StrictLessThan(Add(Mul(Integer(16), Pow(Symbol('a'), Integer(4))), Mul(Integer(32), Pow(Symbol('a'), Integer(2)), Pow(Symbol('b'), Integer(2))), Mul(Integer(-1), Integer(8), Pow(Symbol('a'), Integer(2)), Symbol('b')), Mul(Integer(-1), Integer(63), Pow(Symbol('a'), Integer(2))), Mul(Integer(16), Pow(Symbol('b'), Integer(4))), Mul(Integer(-1), Integer(8), Pow(Symbol('b'), Integer(3))), Pow(Symbol('b'), Integer(2))), Integer(0))))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1(a:sympy.Rational,b:sympy.Rational):
	#(a + 1 > 0) & (a - 1 < 0) & (((b + 1 > 0) & (b - 1 < 0)) | (a**2 + b**2 - 2*b < 0) | (a**2 + b**2 + 2*b < 0))

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Integer(1)), Integer(0)), StrictLessThan(Add(Symbol('a'), Integer(-1)), Integer(0)), Or(And(StrictGreaterThan(Add(Symbol('b'), Integer(1)), Integer(0)), StrictLessThan(Add(Symbol('b'), Integer(-1)), Integer(0))), StrictLessThan(Add(Pow(Symbol('a'), Integer(2)), Pow(Symbol('b'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('b'))), Integer(0)), StrictLessThan(Add(Pow(Symbol('a'), Integer(2)), Pow(Symbol('b'), Integer(2)), Mul(Integer(2), Symbol('b'))), Integer(0))))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_2(a:sympy.Rational,b:sympy.Rational):
	#(4*b + 7 > 0) & (4*b - 1 < 0) & ((16*a**2 - 7 < 0) | (4*a**4 + 8*a**2*b**2 + 12*a**2*b - 7*a**2 + 4*b**4 + 12*b**3 + 9*b**2 < 0))

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(4), Symbol('b')), Integer(7)), Integer(0)), StrictLessThan(Add(Mul(Integer(4), Symbol('b')), Integer(-1)), Integer(0)), Or(StrictLessThan(Add(Mul(Integer(16), Pow(Symbol('a'), Integer(2))), Integer(-7)), Integer(0)), StrictLessThan(Add(Mul(Integer(4), Pow(Symbol('a'), Integer(4))), Mul(Integer(8), Pow(Symbol('a'), Integer(2)), Pow(Symbol('b'), Integer(2))), Mul(Integer(12), Pow(Symbol('a'), Integer(2)), Symbol('b')), Mul(Integer(-1), Integer(7), Pow(Symbol('a'), Integer(2))), Mul(Integer(4), Pow(Symbol('b'), Integer(4))), Mul(Integer(12), Pow(Symbol('b'), Integer(3))), Mul(Integer(9), Pow(Symbol('b'), Integer(2)))), Integer(0))))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_3(a:sympy.Rational,b:sympy.Rational):
	#(2*a + 1 > 0) & (2*a - 3 < 0) & ((2*a**2 - 2*a + 2*b**2 - 3 < 0) | (a**4 - 2*a**3 + 2*a**2*b**2 + a**2 - 2*a*b**2 + b**4 - 3*b**2 < 0))

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(2), Symbol('a')), Integer(1)), Integer(0)), StrictLessThan(Add(Mul(Integer(2), Symbol('a')), Integer(-3)), Integer(0)), Or(StrictLessThan(Add(Mul(Integer(2), Pow(Symbol('a'), Integer(2))), Mul(Integer(-1), Integer(2), Symbol('a')), Mul(Integer(2), Pow(Symbol('b'), Integer(2))), Integer(-3)), Integer(0)), StrictLessThan(Add(Pow(Symbol('a'), Integer(4)), Mul(Integer(-1), Integer(2), Pow(Symbol('a'), Integer(3))), Mul(Integer(2), Pow(Symbol('a'), Integer(2)), Pow(Symbol('b'), Integer(2))), Pow(Symbol('a'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('a'), Pow(Symbol('b'), Integer(2))), Pow(Symbol('b'), Integer(4)), Mul(Integer(-1), Integer(3), Pow(Symbol('b'), Integer(2)))), Integer(0))))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_4(a:sympy.Rational,b:sympy.Rational):
	#(32*b + 53 > 0) & (32*b - 11 < 0) & ((1024*a**2 - 583 < 0) | (256*a**4 + 512*a**2*b**2 + 672*a**2*b - 583*a**2 + 256*b**4 + 672*b**3 + 441*b**2 < 0))

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(32), Symbol('b')), Integer(53)), Integer(0)), StrictLessThan(Add(Mul(Integer(32), Symbol('b')), Integer(-11)), Integer(0)), Or(StrictLessThan(Add(Mul(Integer(1024), Pow(Symbol('a'), Integer(2))), Integer(-583)), Integer(0)), StrictLessThan(Add(Mul(Integer(256), Pow(Symbol('a'), Integer(4))), Mul(Integer(512), Pow(Symbol('a'), Integer(2)), Pow(Symbol('b'), Integer(2))), Mul(Integer(672), Pow(Symbol('a'), Integer(2)), Symbol('b')), Mul(Integer(-1), Integer(583), Pow(Symbol('a'), Integer(2))), Mul(Integer(256), Pow(Symbol('b'), Integer(4))), Mul(Integer(672), Pow(Symbol('b'), Integer(3))), Mul(Integer(441), Pow(Symbol('b'), Integer(2)))), Integer(0))))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_5(a:sympy.Rational,b:sympy.Rational):
	#(4*a + 1 > 0) & (4*a - 7 < 0) & ((8*a**2 - 12*a + 8*b**2 - 7 < 0) | (4*a**4 - 12*a**3 + 8*a**2*b**2 + 9*a**2 - 12*a*b**2 + 4*b**4 - 7*b**2 < 0))

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(4), Symbol('a')), Integer(1)), Integer(0)), StrictLessThan(Add(Mul(Integer(4), Symbol('a')), Integer(-7)), Integer(0)), Or(StrictLessThan(Add(Mul(Integer(8), Pow(Symbol('a'), Integer(2))), Mul(Integer(-1), Integer(12), Symbol('a')), Mul(Integer(8), Pow(Symbol('b'), Integer(2))), Integer(-7)), Integer(0)), StrictLessThan(Add(Mul(Integer(4), Pow(Symbol('a'), Integer(4))), Mul(Integer(-1), Integer(12), Pow(Symbol('a'), Integer(3))), Mul(Integer(8), Pow(Symbol('a'), Integer(2)), Pow(Symbol('b'), Integer(2))), Mul(Integer(9), Pow(Symbol('a'), Integer(2))), Mul(Integer(-1), Integer(12), Symbol('a'), Pow(Symbol('b'), Integer(2))), Mul(Integer(4), Pow(Symbol('b'), Integer(4))), Mul(Integer(-1), Integer(7), Pow(Symbol('b'), Integer(2)))), Integer(0))))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_6(a:sympy.Rational,b:sympy.Rational):
	#(8*b + 15 > 0) & (8*b - 1 < 0) & ((64*a**2 - 15 < 0) | (4*a**2 + 4*b**2 + 7*b < 0) | (16*a**4 + 32*a**2*b**2 + 56*a**2*b - 15*a**2 + 16*b**4 + 56*b**3 + 49*b**2 < 0))

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(8), Symbol('b')), Integer(15)), Integer(0)), StrictLessThan(Add(Mul(Integer(8), Symbol('b')), Integer(-1)), Integer(0)), Or(StrictLessThan(Add(Mul(Integer(64), Pow(Symbol('a'), Integer(2))), Integer(-15)), Integer(0)), StrictLessThan(Add(Mul(Integer(4), Pow(Symbol('a'), Integer(2))), Mul(Integer(4), Pow(Symbol('b'), Integer(2))), Mul(Integer(7), Symbol('b'))), Integer(0)), StrictLessThan(Add(Mul(Integer(16), Pow(Symbol('a'), Integer(4))), Mul(Integer(32), Pow(Symbol('a'), Integer(2)), Pow(Symbol('b'), Integer(2))), Mul(Integer(56), Pow(Symbol('a'), Integer(2)), Symbol('b')), Mul(Integer(-1), Integer(15), Pow(Symbol('a'), Integer(2))), Mul(Integer(16), Pow(Symbol('b'), Integer(4))), Mul(Integer(56), Pow(Symbol('b'), Integer(3))), Mul(Integer(49), Pow(Symbol('b'), Integer(2)))), Integer(0))))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_7(a:sympy.Rational,b:sympy.Rational):
	#(8*a + 11 > 0) & (8*a - 5 < 0) & ((32*a**2 + 24*a + 32*b**2 - 55 < 0) | (16*a**4 + 24*a**3 + 32*a**2*b**2 + 9*a**2 + 24*a*b**2 + 16*b**4 - 55*b**2 < 0))

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(8), Symbol('a')), Integer(11)), Integer(0)), StrictLessThan(Add(Mul(Integer(8), Symbol('a')), Integer(-5)), Integer(0)), Or(StrictLessThan(Add(Mul(Integer(32), Pow(Symbol('a'), Integer(2))), Mul(Integer(24), Symbol('a')), Mul(Integer(32), Pow(Symbol('b'), Integer(2))), Integer(-55)), Integer(0)), StrictLessThan(Add(Mul(Integer(16), Pow(Symbol('a'), Integer(4))), Mul(Integer(24), Pow(Symbol('a'), Integer(3))), Mul(Integer(32), Pow(Symbol('a'), Integer(2)), Pow(Symbol('b'), Integer(2))), Mul(Integer(9), Pow(Symbol('a'), Integer(2))), Mul(Integer(24), Symbol('a'), Pow(Symbol('b'), Integer(2))), Mul(Integer(16), Pow(Symbol('b'), Integer(4))), Mul(Integer(-1), Integer(55), Pow(Symbol('b'), Integer(2)))), Integer(0))))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_8(a:sympy.Rational,b:sympy.Rational):
	#(16*b + 31 > 0) & (16*b - 1 < 0) & ((256*a**2 - 31 < 0) | (8*a**2 + 8*b**2 + 15*b < 0) | (64*a**4 + 128*a**2*b**2 + 240*a**2*b - 31*a**2 + 64*b**4 + 240*b**3 + 225*b**2 < 0))

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(16), Symbol('b')), Integer(31)), Integer(0)), StrictLessThan(Add(Mul(Integer(16), Symbol('b')), Integer(-1)), Integer(0)), Or(StrictLessThan(Add(Mul(Integer(256), Pow(Symbol('a'), Integer(2))), Integer(-31)), Integer(0)), StrictLessThan(Add(Mul(Integer(8), Pow(Symbol('a'), Integer(2))), Mul(Integer(8), Pow(Symbol('b'), Integer(2))), Mul(Integer(15), Symbol('b'))), Integer(0)), StrictLessThan(Add(Mul(Integer(64), Pow(Symbol('a'), Integer(4))), Mul(Integer(128), Pow(Symbol('a'), Integer(2)), Pow(Symbol('b'), Integer(2))), Mul(Integer(240), Pow(Symbol('a'), Integer(2)), Symbol('b')), Mul(Integer(-1), Integer(31), Pow(Symbol('a'), Integer(2))), Mul(Integer(64), Pow(Symbol('b'), Integer(4))), Mul(Integer(240), Pow(Symbol('b'), Integer(3))), Mul(Integer(225), Pow(Symbol('b'), Integer(2)))), Integer(0))))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_9(a:sympy.Rational,b:sympy.Rational):
	#(256*a + 345 > 0) & (256*a - 167 < 0) & ((32768*a**2 + 22784*a + 32768*b**2 - 57615 < 0) | (16384*a**4 + 22784*a**3 + 32768*a**2*b**2 + 7921*a**2 + 22784*a*b**2 + 16384*b**4 - 57615*b**2 < 0))

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(256), Symbol('a')), Integer(345)), Integer(0)), StrictLessThan(Add(Mul(Integer(256), Symbol('a')), Integer(-167)), Integer(0)), Or(StrictLessThan(Add(Mul(Integer(32768), Pow(Symbol('a'), Integer(2))), Mul(Integer(22784), Symbol('a')), Mul(Integer(32768), Pow(Symbol('b'), Integer(2))), Integer(-57615)), Integer(0)), StrictLessThan(Add(Mul(Integer(16384), Pow(Symbol('a'), Integer(4))), Mul(Integer(22784), Pow(Symbol('a'), Integer(3))), Mul(Integer(32768), Pow(Symbol('a'), Integer(2)), Pow(Symbol('b'), Integer(2))), Mul(Integer(7921), Pow(Symbol('a'), Integer(2))), Mul(Integer(22784), Symbol('a'), Pow(Symbol('b'), Integer(2))), Mul(Integer(16384), Pow(Symbol('b'), Integer(4))), Mul(Integer(-1), Integer(57615), Pow(Symbol('b'), Integer(2)))), Integer(0))))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_10(a:sympy.Rational,b:sympy.Rational):
	#(32*b + 59 > 0) & (32*b - 5 < 0) & ((1024*a**2 - 295 < 0) | (256*a**4 + 512*a**2*b**2 + 864*a**2*b - 295*a**2 + 256*b**4 + 864*b**3 + 729*b**2 < 0))

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(32), Symbol('b')), Integer(59)), Integer(0)), StrictLessThan(Add(Mul(Integer(32), Symbol('b')), Integer(-5)), Integer(0)), Or(StrictLessThan(Add(Mul(Integer(1024), Pow(Symbol('a'), Integer(2))), Integer(-295)), Integer(0)), StrictLessThan(Add(Mul(Integer(256), Pow(Symbol('a'), Integer(4))), Mul(Integer(512), Pow(Symbol('a'), Integer(2)), Pow(Symbol('b'), Integer(2))), Mul(Integer(864), Pow(Symbol('a'), Integer(2)), Symbol('b')), Mul(Integer(-1), Integer(295), Pow(Symbol('a'), Integer(2))), Mul(Integer(256), Pow(Symbol('b'), Integer(4))), Mul(Integer(864), Pow(Symbol('b'), Integer(3))), Mul(Integer(729), Pow(Symbol('b'), Integer(2)))), Integer(0))))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_11(a:sympy.Rational,b:sympy.Rational):
	#(256*a + 393 > 0) & (256*a - 119 < 0) & ((32768*a**2 + 35072*a + 32768*b**2 - 46767 < 0) | (16384*a**4 + 35072*a**3 + 32768*a**2*b**2 + 18769*a**2 + 35072*a*b**2 + 16384*b**4 - 46767*b**2 < 0))

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(256), Symbol('a')), Integer(393)), Integer(0)), StrictLessThan(Add(Mul(Integer(256), Symbol('a')), Integer(-119)), Integer(0)), Or(StrictLessThan(Add(Mul(Integer(32768), Pow(Symbol('a'), Integer(2))), Mul(Integer(35072), Symbol('a')), Mul(Integer(32768), Pow(Symbol('b'), Integer(2))), Integer(-46767)), Integer(0)), StrictLessThan(Add(Mul(Integer(16384), Pow(Symbol('a'), Integer(4))), Mul(Integer(35072), Pow(Symbol('a'), Integer(3))), Mul(Integer(32768), Pow(Symbol('a'), Integer(2)), Pow(Symbol('b'), Integer(2))), Mul(Integer(18769), Pow(Symbol('a'), Integer(2))), Mul(Integer(35072), Symbol('a'), Pow(Symbol('b'), Integer(2))), Mul(Integer(16384), Pow(Symbol('b'), Integer(4))), Mul(Integer(-1), Integer(46767), Pow(Symbol('b'), Integer(2)))), Integer(0))))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_12(a:sympy.Rational,b:sympy.Rational):
	#(32*b + 63 > 0) & (32*b - 1 < 0) & ((1024*a**2 - 63 < 0) | (16*a**2 + 16*b**2 + 31*b < 0) | (256*a**4 + 512*a**2*b**2 + 992*a**2*b - 63*a**2 + 256*b**4 + 992*b**3 + 961*b**2 < 0))

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(32), Symbol('b')), Integer(63)), Integer(0)), StrictLessThan(Add(Mul(Integer(32), Symbol('b')), Integer(-1)), Integer(0)), Or(StrictLessThan(Add(Mul(Integer(1024), Pow(Symbol('a'), Integer(2))), Integer(-63)), Integer(0)), StrictLessThan(Add(Mul(Integer(16), Pow(Symbol('a'), Integer(2))), Mul(Integer(16), Pow(Symbol('b'), Integer(2))), Mul(Integer(31), Symbol('b'))), Integer(0)), StrictLessThan(Add(Mul(Integer(256), Pow(Symbol('a'), Integer(4))), Mul(Integer(512), Pow(Symbol('a'), Integer(2)), Pow(Symbol('b'), Integer(2))), Mul(Integer(992), Pow(Symbol('a'), Integer(2)), Symbol('b')), Mul(Integer(-1), Integer(63), Pow(Symbol('a'), Integer(2))), Mul(Integer(256), Pow(Symbol('b'), Integer(4))), Mul(Integer(992), Pow(Symbol('b'), Integer(3))), Mul(Integer(961), Pow(Symbol('b'), Integer(2)))), Integer(0))))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_13(a:sympy.Rational,b:sympy.Rational):
	#(128*a + 159 > 0) & (128*a - 97 < 0) & ((8192*a**2 + 3968*a + 8192*b**2 - 15423 < 0) | (4096*a**4 + 3968*a**3 + 8192*a**2*b**2 + 961*a**2 + 3968*a*b**2 + 4096*b**4 - 15423*b**2 < 0))

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(128), Symbol('a')), Integer(159)), Integer(0)), StrictLessThan(Add(Mul(Integer(128), Symbol('a')), Integer(-97)), Integer(0)), Or(StrictLessThan(Add(Mul(Integer(8192), Pow(Symbol('a'), Integer(2))), Mul(Integer(3968), Symbol('a')), Mul(Integer(8192), Pow(Symbol('b'), Integer(2))), Integer(-15423)), Integer(0)), StrictLessThan(Add(Mul(Integer(4096), Pow(Symbol('a'), Integer(4))), Mul(Integer(3968), Pow(Symbol('a'), Integer(3))), Mul(Integer(8192), Pow(Symbol('a'), Integer(2)), Pow(Symbol('b'), Integer(2))), Mul(Integer(961), Pow(Symbol('a'), Integer(2))), Mul(Integer(3968), Symbol('a'), Pow(Symbol('b'), Integer(2))), Mul(Integer(4096), Pow(Symbol('b'), Integer(4))), Mul(Integer(-1), Integer(15423), Pow(Symbol('b'), Integer(2)))), Integer(0))))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_14(a:sympy.Rational,b:sympy.Rational):
	#(128*b + 247 > 0) & (128*b - 9 < 0) & ((16384*a**2 - 2223 < 0) | (64*a**2 + 64*b**2 + 119*b < 0) | (4096*a**4 + 8192*a**2*b**2 + 15232*a**2*b - 2223*a**2 + 4096*b**4 + 15232*b**3 + 14161*b**2 < 0))

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(128), Symbol('b')), Integer(247)), Integer(0)), StrictLessThan(Add(Mul(Integer(128), Symbol('b')), Integer(-9)), Integer(0)), Or(StrictLessThan(Add(Mul(Integer(16384), Pow(Symbol('a'), Integer(2))), Integer(-2223)), Integer(0)), StrictLessThan(Add(Mul(Integer(64), Pow(Symbol('a'), Integer(2))), Mul(Integer(64), Pow(Symbol('b'), Integer(2))), Mul(Integer(119), Symbol('b'))), Integer(0)), StrictLessThan(Add(Mul(Integer(4096), Pow(Symbol('a'), Integer(4))), Mul(Integer(8192), Pow(Symbol('a'), Integer(2)), Pow(Symbol('b'), Integer(2))), Mul(Integer(15232), Pow(Symbol('a'), Integer(2)), Symbol('b')), Mul(Integer(-1), Integer(2223), Pow(Symbol('a'), Integer(2))), Mul(Integer(4096), Pow(Symbol('b'), Integer(4))), Mul(Integer(15232), Pow(Symbol('b'), Integer(3))), Mul(Integer(14161), Pow(Symbol('b'), Integer(2)))), Integer(0))))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_15(a:sympy.Rational,b:sympy.Rational):
	#(8192*a + 11209 > 0) & (8192*a - 5175 < 0) & ((33554432*a**2 + 24715264*a + 33554432*b**2 - 58006575 < 0) | (16777216*a**4 + 24715264*a**3 + 33554432*a**2*b**2 + 9102289*a**2 + 24715264*a*b**2 + 16777216*b**4 - 58006575*b**2 < 0))

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(8192), Symbol('a')), Integer(11209)), Integer(0)), StrictLessThan(Add(Mul(Integer(8192), Symbol('a')), Integer(-5175)), Integer(0)), Or(StrictLessThan(Add(Mul(Integer(33554432), Pow(Symbol('a'), Integer(2))), Mul(Integer(24715264), Symbol('a')), Mul(Integer(33554432), Pow(Symbol('b'), Integer(2))), Integer(-58006575)), Integer(0)), StrictLessThan(Add(Mul(Integer(16777216), Pow(Symbol('a'), Integer(4))), Mul(Integer(24715264), Pow(Symbol('a'), Integer(3))), Mul(Integer(33554432), Pow(Symbol('a'), Integer(2)), Pow(Symbol('b'), Integer(2))), Mul(Integer(9102289), Pow(Symbol('a'), Integer(2))), Mul(Integer(24715264), Symbol('a'), Pow(Symbol('b'), Integer(2))), Mul(Integer(16777216), Pow(Symbol('b'), Integer(4))), Mul(Integer(-1), Integer(58006575), Pow(Symbol('b'), Integer(2)))), Integer(0))))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_16(a:sympy.Rational,b:sympy.Rational):
	#(256*b + 497 > 0) & (256*b - 15 < 0) & ((65536*a**2 - 7455 < 0) | (128*a**2 + 128*b**2 + 241*b < 0) | (16384*a**4 + 32768*a**2*b**2 + 61696*a**2*b - 7455*a**2 + 16384*b**4 + 61696*b**3 + 58081*b**2 < 0))

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(256), Symbol('b')), Integer(497)), Integer(0)), StrictLessThan(Add(Mul(Integer(256), Symbol('b')), Integer(-15)), Integer(0)), Or(StrictLessThan(Add(Mul(Integer(65536), Pow(Symbol('a'), Integer(2))), Integer(-7455)), Integer(0)), StrictLessThan(Add(Mul(Integer(128), Pow(Symbol('a'), Integer(2))), Mul(Integer(128), Pow(Symbol('b'), Integer(2))), Mul(Integer(241), Symbol('b'))), Integer(0)), StrictLessThan(Add(Mul(Integer(16384), Pow(Symbol('a'), Integer(4))), Mul(Integer(32768), Pow(Symbol('a'), Integer(2)), Pow(Symbol('b'), Integer(2))), Mul(Integer(61696), Pow(Symbol('a'), Integer(2)), Symbol('b')), Mul(Integer(-1), Integer(7455), Pow(Symbol('a'), Integer(2))), Mul(Integer(16384), Pow(Symbol('b'), Integer(4))), Mul(Integer(61696), Pow(Symbol('b'), Integer(3))), Mul(Integer(58081), Pow(Symbol('b'), Integer(2)))), Integer(0))))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_17(a:sympy.Rational,b:sympy.Rational):
	#(4096*a + 5477 > 0) & (4096*a - 2715 < 0) & ((8388608*a**2 + 5656576*a + 8388608*b**2 - 14870055 < 0) | (4194304*a**4 + 5656576*a**3 + 8388608*a**2*b**2 + 1907161*a**2 + 5656576*a*b**2 + 4194304*b**4 - 14870055*b**2 < 0))

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(4096), Symbol('a')), Integer(5477)), Integer(0)), StrictLessThan(Add(Mul(Integer(4096), Symbol('a')), Integer(-2715)), Integer(0)), Or(StrictLessThan(Add(Mul(Integer(8388608), Pow(Symbol('a'), Integer(2))), Mul(Integer(5656576), Symbol('a')), Mul(Integer(8388608), Pow(Symbol('b'), Integer(2))), Integer(-14870055)), Integer(0)), StrictLessThan(Add(Mul(Integer(4194304), Pow(Symbol('a'), Integer(4))), Mul(Integer(5656576), Pow(Symbol('a'), Integer(3))), Mul(Integer(8388608), Pow(Symbol('a'), Integer(2)), Pow(Symbol('b'), Integer(2))), Mul(Integer(1907161), Pow(Symbol('a'), Integer(2))), Mul(Integer(5656576), Symbol('a'), Pow(Symbol('b'), Integer(2))), Mul(Integer(4194304), Pow(Symbol('b'), Integer(4))), Mul(Integer(-1), Integer(14870055), Pow(Symbol('b'), Integer(2)))), Integer(0))))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_18(a:sympy.Rational,b:sympy.Rational):
	#(256*b + 493 > 0) & (256*b - 19 < 0) & ((65536*a**2 - 9367 < 0) | (128*a**2 + 128*b**2 + 237*b < 0) | (16384*a**4 + 32768*a**2*b**2 + 60672*a**2*b - 9367*a**2 + 16384*b**4 + 60672*b**3 + 56169*b**2 < 0))

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(256), Symbol('b')), Integer(493)), Integer(0)), StrictLessThan(Add(Mul(Integer(256), Symbol('b')), Integer(-19)), Integer(0)), Or(StrictLessThan(Add(Mul(Integer(65536), Pow(Symbol('a'), Integer(2))), Integer(-9367)), Integer(0)), StrictLessThan(Add(Mul(Integer(128), Pow(Symbol('a'), Integer(2))), Mul(Integer(128), Pow(Symbol('b'), Integer(2))), Mul(Integer(237), Symbol('b'))), Integer(0)), StrictLessThan(Add(Mul(Integer(16384), Pow(Symbol('a'), Integer(4))), Mul(Integer(32768), Pow(Symbol('a'), Integer(2)), Pow(Symbol('b'), Integer(2))), Mul(Integer(60672), Pow(Symbol('a'), Integer(2)), Symbol('b')), Mul(Integer(-1), Integer(9367), Pow(Symbol('a'), Integer(2))), Mul(Integer(16384), Pow(Symbol('b'), Integer(4))), Mul(Integer(60672), Pow(Symbol('b'), Integer(3))), Mul(Integer(56169), Pow(Symbol('b'), Integer(2)))), Integer(0))))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_19(a:sympy.Rational,b:sympy.Rational):
	#(8192*a + 11289 > 0) & (8192*a - 5095 < 0) & ((33554432*a**2 + 25370624*a + 33554432*b**2 - 57517455 < 0) | (16777216*a**4 + 25370624*a**3 + 33554432*a**2*b**2 + 9591409*a**2 + 25370624*a*b**2 + 16777216*b**4 - 57517455*b**2 < 0))

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(8192), Symbol('a')), Integer(11289)), Integer(0)), StrictLessThan(Add(Mul(Integer(8192), Symbol('a')), Integer(-5095)), Integer(0)), Or(StrictLessThan(Add(Mul(Integer(33554432), Pow(Symbol('a'), Integer(2))), Mul(Integer(25370624), Symbol('a')), Mul(Integer(33554432), Pow(Symbol('b'), Integer(2))), Integer(-57517455)), Integer(0)), StrictLessThan(Add(Mul(Integer(16777216), Pow(Symbol('a'), Integer(4))), Mul(Integer(25370624), Pow(Symbol('a'), Integer(3))), Mul(Integer(33554432), Pow(Symbol('a'), Integer(2)), Pow(Symbol('b'), Integer(2))), Mul(Integer(9591409), Pow(Symbol('a'), Integer(2))), Mul(Integer(25370624), Symbol('a'), Pow(Symbol('b'), Integer(2))), Mul(Integer(16777216), Pow(Symbol('b'), Integer(4))), Mul(Integer(-1), Integer(57517455), Pow(Symbol('b'), Integer(2)))), Integer(0))))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_20(a:sympy.Rational,b:sympy.Rational):
	#(64*b + 125 > 0) & (64*b - 3 < 0) & ((4096*a**2 - 375 < 0) | (32*a**2 + 32*b**2 + 61*b < 0) | (1024*a**4 + 2048*a**2*b**2 + 3904*a**2*b - 375*a**2 + 1024*b**4 + 3904*b**3 + 3721*b**2 < 0))

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(64), Symbol('b')), Integer(125)), Integer(0)), StrictLessThan(Add(Mul(Integer(64), Symbol('b')), Integer(-3)), Integer(0)), Or(StrictLessThan(Add(Mul(Integer(4096), Pow(Symbol('a'), Integer(2))), Integer(-375)), Integer(0)), StrictLessThan(Add(Mul(Integer(32), Pow(Symbol('a'), Integer(2))), Mul(Integer(32), Pow(Symbol('b'), Integer(2))), Mul(Integer(61), Symbol('b'))), Integer(0)), StrictLessThan(Add(Mul(Integer(1024), Pow(Symbol('a'), Integer(4))), Mul(Integer(2048), Pow(Symbol('a'), Integer(2)), Pow(Symbol('b'), Integer(2))), Mul(Integer(3904), Pow(Symbol('a'), Integer(2)), Symbol('b')), Mul(Integer(-1), Integer(375), Pow(Symbol('a'), Integer(2))), Mul(Integer(1024), Pow(Symbol('b'), Integer(4))), Mul(Integer(3904), Pow(Symbol('b'), Integer(3))), Mul(Integer(3721), Pow(Symbol('b'), Integer(2)))), Integer(0))))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_21(a:sympy.Rational,b:sympy.Rational):
	#(256*a + 333 > 0) & (256*a - 179 < 0) & ((32768*a**2 + 19712*a + 32768*b**2 - 59607 < 0) | (16384*a**4 + 19712*a**3 + 32768*a**2*b**2 + 5929*a**2 + 19712*a*b**2 + 16384*b**4 - 59607*b**2 < 0))

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(256), Symbol('a')), Integer(333)), Integer(0)), StrictLessThan(Add(Mul(Integer(256), Symbol('a')), Integer(-179)), Integer(0)), Or(StrictLessThan(Add(Mul(Integer(32768), Pow(Symbol('a'), Integer(2))), Mul(Integer(19712), Symbol('a')), Mul(Integer(32768), Pow(Symbol('b'), Integer(2))), Integer(-59607)), Integer(0)), StrictLessThan(Add(Mul(Integer(16384), Pow(Symbol('a'), Integer(4))), Mul(Integer(19712), Pow(Symbol('a'), Integer(3))), Mul(Integer(32768), Pow(Symbol('a'), Integer(2)), Pow(Symbol('b'), Integer(2))), Mul(Integer(5929), Pow(Symbol('a'), Integer(2))), Mul(Integer(19712), Symbol('a'), Pow(Symbol('b'), Integer(2))), Mul(Integer(16384), Pow(Symbol('b'), Integer(4))), Mul(Integer(-1), Integer(59607), Pow(Symbol('b'), Integer(2)))), Integer(0))))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_22(a:sympy.Rational,b:sympy.Rational):
	#(256*b + 495 > 0) & (256*b - 17 < 0) & ((65536*a**2 - 8415 < 0) | (128*a**2 + 128*b**2 + 239*b < 0) | (16384*a**4 + 32768*a**2*b**2 + 61184*a**2*b - 8415*a**2 + 16384*b**4 + 61184*b**3 + 57121*b**2 < 0))

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(256), Symbol('b')), Integer(495)), Integer(0)), StrictLessThan(Add(Mul(Integer(256), Symbol('b')), Integer(-17)), Integer(0)), Or(StrictLessThan(Add(Mul(Integer(65536), Pow(Symbol('a'), Integer(2))), Integer(-8415)), Integer(0)), StrictLessThan(Add(Mul(Integer(128), Pow(Symbol('a'), Integer(2))), Mul(Integer(128), Pow(Symbol('b'), Integer(2))), Mul(Integer(239), Symbol('b'))), Integer(0)), StrictLessThan(Add(Mul(Integer(16384), Pow(Symbol('a'), Integer(4))), Mul(Integer(32768), Pow(Symbol('a'), Integer(2)), Pow(Symbol('b'), Integer(2))), Mul(Integer(61184), Pow(Symbol('a'), Integer(2)), Symbol('b')), Mul(Integer(-1), Integer(8415), Pow(Symbol('a'), Integer(2))), Mul(Integer(16384), Pow(Symbol('b'), Integer(4))), Mul(Integer(61184), Pow(Symbol('b'), Integer(3))), Mul(Integer(57121), Pow(Symbol('b'), Integer(2)))), Integer(0))))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def post_condition(a:sympy.Rational, b:sympy.Rational, y:sympy.Rational, x:sympy.Rational):
	# (0 > x**2 + y**2 - 1) & (0 > a**2 - 2*a*y + b**2 - 2*b*x + x**2 + y**2 - 1)

	post_cond =  And(StrictGreaterThan(Integer(0), Add(Pow(Symbol('x'), Integer(2)), Pow(Symbol('y'), Integer(2)), Integer(-1))), StrictGreaterThan(Integer(0), Add(Pow(Symbol('a'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('a'), Symbol('y')), Pow(Symbol('b'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('b'), Symbol('x')), Pow(Symbol('x'), Integer(2)), Pow(Symbol('y'), Integer(2)), Integer(-1))))

	eval = post_cond.subs( { 'a':a, 'b':b, 'y':y, 'x':x })

	return eval == sympy.logic.boolalg.BooleanTrue



#return post-condition single variable
def return_post_condition_single_var(post_condition, a:sympy.Rational=None, b:sympy.Rational=None, y:sympy.Rational=None, x:sympy.Rational=None):
	assert a!=None
	assert b!=None


	if y==None:
		assert x!=None
		return lambda y: post_condition(a=a, b=b, y=y, x=x)

	if x==None:
		assert y!=None
		return lambda x: post_condition(a=a, b=b, y=y, x=x)


	return post_condition(a=a, b=b, y=y, x=x)


def get_univariate_poly( a:sympy.Rational, b:sympy.Rational, y:sympy.Rational, x:sympy.Rational ):


	post_cond =  And(StrictGreaterThan(Integer(0), Add(Pow(Symbol('x'), Integer(2)), Pow(Symbol('y'), Integer(2)), Integer(-1))), StrictGreaterThan(Integer(0), Add(Pow(Symbol('a'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('a'), Symbol('y')), Pow(Symbol('b'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('b'), Symbol('x')), Pow(Symbol('x'), Integer(2)), Pow(Symbol('y'), Integer(2)), Integer(-1))))

	eval = post_cond.subs( { 'a':a, 'b':b, 'y':y, 'x':x })
	return eval



if __name__=="__main__":
	
	ip_0=int(input("enter numerator of a:\n"))
	ip_1=int(input("enter denominator of a:\n"))
	assert(ip_1!=0), ("Error denominator entered is 0")
	a=sympy.Rational(ip_0,ip_1)
	
	
	ip_0=int(input("enter numerator of b:\n"))
	ip_1=int(input("enter denominator of b:\n"))
	assert(ip_1!=0), ("Error denominator entered is 0")
	b=sympy.Rational(ip_0,ip_1)
	
	
	lambda_var_0 = sympy.symbols('lambda_var_0')
	
	
	if pre_condition_0(a=a,b=b)==True:
		all_vals = dict()
		all_vals['a'] = a
		all_vals['b'] = b
		all_vals['y'] = Symbol('lambda_var_0')
		all_vals['x'] = Rational(1, 8)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_0 SAT")

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_1(a=a,b=b)==True:
		all_vals = dict()
		all_vals['a'] = a
		all_vals['b'] = b
		all_vals['y'] = Integer(0)
		all_vals['x'] = Add(Symbol('lambda_var_0'), Rational(1, 8))
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_1 SAT")

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_2(a=a,b=b)==True:
		all_vals = dict()
		all_vals['a'] = a
		all_vals['b'] = b
		all_vals['y'] = Add(Symbol('lambda_var_0'), Rational(1, 2))
		all_vals['x'] = Rational(-3, 4)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_2 SAT")

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_3(a=a,b=b)==True:
		all_vals = dict()
		all_vals['a'] = a
		all_vals['b'] = b
		all_vals['y'] = Rational(1, 2)
		all_vals['x'] = Add(Symbol('lambda_var_0'), Rational(-3, 4))
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_3 SAT")

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_4(a=a,b=b)==True:
		all_vals = dict()
		all_vals['a'] = a
		all_vals['b'] = b
		all_vals['y'] = Add(Symbol('lambda_var_0'), Rational(3, 4))
		all_vals['x'] = Rational(-21, 32)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_4 SAT")

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_5(a=a,b=b)==True:
		all_vals = dict()
		all_vals['a'] = a
		all_vals['b'] = b
		all_vals['y'] = Rational(3, 4)
		all_vals['x'] = Add(Symbol('lambda_var_0'), Rational(-21, 32))
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_5 SAT")

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_6(a=a,b=b)==True:
		all_vals = dict()
		all_vals['a'] = a
		all_vals['b'] = b
		all_vals['y'] = Add(Symbol('lambda_var_0'), Rational(-3, 8))
		all_vals['x'] = Rational(-7, 8)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_6 SAT")

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_7(a=a,b=b)==True:
		all_vals = dict()
		all_vals['a'] = a
		all_vals['b'] = b
		all_vals['y'] = Rational(-3, 8)
		all_vals['x'] = Add(Symbol('lambda_var_0'), Rational(-7, 8))
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_7 SAT")

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_8(a=a,b=b)==True:
		all_vals = dict()
		all_vals['a'] = a
		all_vals['b'] = b
		all_vals['y'] = Add(Symbol('lambda_var_0'), Rational(-89, 256))
		all_vals['x'] = Rational(-15, 16)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_8 SAT")

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_9(a=a,b=b)==True:
		all_vals = dict()
		all_vals['a'] = a
		all_vals['b'] = b
		all_vals['y'] = Rational(-89, 256)
		all_vals['x'] = Add(Symbol('lambda_var_0'), Rational(-15, 16))
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_9 SAT")

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_10(a=a,b=b)==True:
		all_vals = dict()
		all_vals['a'] = a
		all_vals['b'] = b
		all_vals['y'] = Add(Symbol('lambda_var_0'), Rational(-137, 256))
		all_vals['x'] = Rational(-27, 32)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_10 SAT")

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_11(a=a,b=b)==True:
		all_vals = dict()
		all_vals['a'] = a
		all_vals['b'] = b
		all_vals['y'] = Rational(-137, 256)
		all_vals['x'] = Add(Symbol('lambda_var_0'), Rational(-27, 32))
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_11 SAT")

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_12(a=a,b=b)==True:
		all_vals = dict()
		all_vals['a'] = a
		all_vals['b'] = b
		all_vals['y'] = Add(Symbol('lambda_var_0'), Rational(-31, 128))
		all_vals['x'] = Rational(-31, 32)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_12 SAT")

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_13(a=a,b=b)==True:
		all_vals = dict()
		all_vals['a'] = a
		all_vals['b'] = b
		all_vals['y'] = Rational(-31, 128)
		all_vals['x'] = Add(Symbol('lambda_var_0'), Rational(-31, 32))
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_13 SAT")

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_14(a=a,b=b)==True:
		all_vals = dict()
		all_vals['a'] = a
		all_vals['b'] = b
		all_vals['y'] = Add(Symbol('lambda_var_0'), Rational(-3017, 8192))
		all_vals['x'] = Rational(-119, 128)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_14 SAT")

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_15(a=a,b=b)==True:
		all_vals = dict()
		all_vals['a'] = a
		all_vals['b'] = b
		all_vals['y'] = Rational(-3017, 8192)
		all_vals['x'] = Add(Symbol('lambda_var_0'), Rational(-119, 128))
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_15 SAT")

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_16(a=a,b=b)==True:
		all_vals = dict()
		all_vals['a'] = a
		all_vals['b'] = b
		all_vals['y'] = Add(Symbol('lambda_var_0'), Rational(-1381, 4096))
		all_vals['x'] = Rational(-241, 256)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_16 SAT")

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_17(a=a,b=b)==True:
		all_vals = dict()
		all_vals['a'] = a
		all_vals['b'] = b
		all_vals['y'] = Rational(-1381, 4096)
		all_vals['x'] = Add(Symbol('lambda_var_0'), Rational(-241, 256))
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_17 SAT")

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_18(a=a,b=b)==True:
		all_vals = dict()
		all_vals['a'] = a
		all_vals['b'] = b
		all_vals['y'] = Add(Symbol('lambda_var_0'), Rational(-3097, 8192))
		all_vals['x'] = Rational(-237, 256)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_18 SAT")

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_19(a=a,b=b)==True:
		all_vals = dict()
		all_vals['a'] = a
		all_vals['b'] = b
		all_vals['y'] = Rational(-3097, 8192)
		all_vals['x'] = Add(Symbol('lambda_var_0'), Rational(-237, 256))
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_19 SAT")

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_20(a=a,b=b)==True:
		all_vals = dict()
		all_vals['a'] = a
		all_vals['b'] = b
		all_vals['y'] = Add(Symbol('lambda_var_0'), Rational(-77, 256))
		all_vals['x'] = Rational(-61, 64)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_20 SAT")

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_21(a=a,b=b)==True:
		all_vals = dict()
		all_vals['a'] = a
		all_vals['b'] = b
		all_vals['y'] = Rational(-77, 256)
		all_vals['x'] = Add(Symbol('lambda_var_0'), Rational(-61, 64))
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_21 SAT")

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_22(a=a,b=b)==True:
		all_vals = dict()
		all_vals['a'] = a
		all_vals['b'] = b
		all_vals['y'] = Add(Symbol('lambda_var_0'), Rational(-2935, 8192))
		all_vals['x'] = Rational(-239, 256)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_22 SAT")

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass


	print("UNKNOWN")
