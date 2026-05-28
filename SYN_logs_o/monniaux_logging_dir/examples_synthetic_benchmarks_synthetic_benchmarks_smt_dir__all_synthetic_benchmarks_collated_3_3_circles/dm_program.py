import sympy
from sympy import *

def pre_condition_0(a:sympy.Rational,b:sympy.Rational,r2:sympy.Rational,r3:sympy.Rational):
	#(-r1**2 + y**2 + 1/64 <= 0) & (a**2 - a/4 + b**2 - 2*b*y - r2**2 + y**2 + 1/64 <= 0) & (a**2 - 2*a*y + b**2 - b/4 - r3**2 + y**2 + 1/64 <= 0)

	pre_cond = And(LessThan(Add(Mul(Integer(-1), Pow(Symbol('r1'), Integer(2))), Pow(Symbol('y'), Integer(2)), Rational(1, 64)), Integer(0)), LessThan(Add(Pow(Symbol('a'), Integer(2)), Mul(Integer(-1), Rational(1, 4), Symbol('a')), Pow(Symbol('b'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('b'), Symbol('y')), Mul(Integer(-1), Pow(Symbol('r2'), Integer(2))), Pow(Symbol('y'), Integer(2)), Rational(1, 64)), Integer(0)), LessThan(Add(Pow(Symbol('a'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('a'), Symbol('y')), Pow(Symbol('b'), Integer(2)), Mul(Integer(-1), Rational(1, 4), Symbol('b')), Mul(Integer(-1), Pow(Symbol('r3'), Integer(2))), Pow(Symbol('y'), Integer(2)), Rational(1, 64)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'r2':r2, 'r3':r3 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1(a:sympy.Rational,b:sympy.Rational,r2:sympy.Rational,r3:sympy.Rational):
	#(r1**2 >= 17/64) & (a**2 - a + b**2 - b/4 - r3**2 + 17/64 <= 0) & (a**2 - a/4 + b**2 - b - r2**2 + 17/64 <= 0)

	pre_cond = And(GreaterThan(Pow(Symbol('r1'), Integer(2)), Rational(17, 64)), LessThan(Add(Pow(Symbol('a'), Integer(2)), Mul(Integer(-1), Symbol('a')), Pow(Symbol('b'), Integer(2)), Mul(Integer(-1), Rational(1, 4), Symbol('b')), Mul(Integer(-1), Pow(Symbol('r3'), Integer(2))), Rational(17, 64)), Integer(0)), LessThan(Add(Pow(Symbol('a'), Integer(2)), Mul(Integer(-1), Rational(1, 4), Symbol('a')), Pow(Symbol('b'), Integer(2)), Mul(Integer(-1), Symbol('b')), Mul(Integer(-1), Pow(Symbol('r2'), Integer(2))), Rational(17, 64)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'r2':r2, 'r3':r3 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_2(a:sympy.Rational,b:sympy.Rational,r2:sympy.Rational,r3:sympy.Rational):
	#(a**2 - a + b**2 - b/4 - r3**2 + 17/64 <= 0) & (a**2 - a/4 + b**2 - b - r2**2 + 17/64 <= 0)

	pre_cond = And(LessThan(Add(Pow(Symbol('a'), Integer(2)), Mul(Integer(-1), Symbol('a')), Pow(Symbol('b'), Integer(2)), Mul(Integer(-1), Rational(1, 4), Symbol('b')), Mul(Integer(-1), Pow(Symbol('r3'), Integer(2))), Rational(17, 64)), Integer(0)), LessThan(Add(Pow(Symbol('a'), Integer(2)), Mul(Integer(-1), Rational(1, 4), Symbol('a')), Pow(Symbol('b'), Integer(2)), Mul(Integer(-1), Symbol('b')), Mul(Integer(-1), Pow(Symbol('r2'), Integer(2))), Rational(17, 64)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'r2':r2, 'r3':r3 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_3(a:sympy.Rational,b:sympy.Rational,r2:sympy.Rational,r3:sympy.Rational):
	#(r1**2 - y**2 >= 0) & (a**2 + b**2 - 2*b*y - r2**2 + y**2 <= 0) & (a**2 - 2*a*y + b**2 - r3**2 + y**2 <= 0)

	pre_cond = And(GreaterThan(Add(Pow(Symbol('r1'), Integer(2)), Mul(Integer(-1), Pow(Symbol('y'), Integer(2)))), Integer(0)), LessThan(Add(Pow(Symbol('a'), Integer(2)), Pow(Symbol('b'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('b'), Symbol('y')), Mul(Integer(-1), Pow(Symbol('r2'), Integer(2))), Pow(Symbol('y'), Integer(2))), Integer(0)), LessThan(Add(Pow(Symbol('a'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('a'), Symbol('y')), Pow(Symbol('b'), Integer(2)), Mul(Integer(-1), Pow(Symbol('r3'), Integer(2))), Pow(Symbol('y'), Integer(2))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'r2':r2, 'r3':r3 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_4(a:sympy.Rational,b:sympy.Rational,r2:sympy.Rational,r3:sympy.Rational):
	#(r1**2 >= 0) & (a**2 + b**2 - r2**2 <= 0) & (a**2 + b**2 - r3**2 <= 0)

	pre_cond = And(GreaterThan(Pow(Symbol('r1'), Integer(2)), Integer(0)), LessThan(Add(Pow(Symbol('a'), Integer(2)), Pow(Symbol('b'), Integer(2)), Mul(Integer(-1), Pow(Symbol('r2'), Integer(2)))), Integer(0)), LessThan(Add(Pow(Symbol('a'), Integer(2)), Pow(Symbol('b'), Integer(2)), Mul(Integer(-1), Pow(Symbol('r3'), Integer(2)))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'r2':r2, 'r3':r3 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_5(a:sympy.Rational,b:sympy.Rational,r2:sympy.Rational,r3:sympy.Rational):
	#(a**2 + b**2 - r2**2 <= 0) & (a**2 + b**2 - r3**2 <= 0)

	pre_cond = And(LessThan(Add(Pow(Symbol('a'), Integer(2)), Pow(Symbol('b'), Integer(2)), Mul(Integer(-1), Pow(Symbol('r2'), Integer(2)))), Integer(0)), LessThan(Add(Pow(Symbol('a'), Integer(2)), Pow(Symbol('b'), Integer(2)), Mul(Integer(-1), Pow(Symbol('r3'), Integer(2)))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'r2':r2, 'r3':r3 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_6(a:sympy.Rational,b:sympy.Rational,r2:sympy.Rational,r3:sympy.Rational):
	#(-r1**2 + y**2 + 1/256 <= 0) & (a**2 + a/8 + b**2 - 2*b*y - r2**2 + y**2 + 1/256 <= 0) & (a**2 - 2*a*y + b**2 + b/8 - r3**2 + y**2 + 1/256 <= 0)

	pre_cond = And(LessThan(Add(Mul(Integer(-1), Pow(Symbol('r1'), Integer(2))), Pow(Symbol('y'), Integer(2)), Rational(1, 256)), Integer(0)), LessThan(Add(Pow(Symbol('a'), Integer(2)), Mul(Rational(1, 8), Symbol('a')), Pow(Symbol('b'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('b'), Symbol('y')), Mul(Integer(-1), Pow(Symbol('r2'), Integer(2))), Pow(Symbol('y'), Integer(2)), Rational(1, 256)), Integer(0)), LessThan(Add(Pow(Symbol('a'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('a'), Symbol('y')), Pow(Symbol('b'), Integer(2)), Mul(Rational(1, 8), Symbol('b')), Mul(Integer(-1), Pow(Symbol('r3'), Integer(2))), Pow(Symbol('y'), Integer(2)), Rational(1, 256)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'r2':r2, 'r3':r3 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_7(a:sympy.Rational,b:sympy.Rational,r2:sympy.Rational,r3:sympy.Rational):
	#(r1**2 >= 17/256) & (a**2 + a/8 + b**2 + b/2 - r2**2 + 17/256 <= 0) & (a**2 + a/2 + b**2 + b/8 - r3**2 + 17/256 <= 0)

	pre_cond = And(GreaterThan(Pow(Symbol('r1'), Integer(2)), Rational(17, 256)), LessThan(Add(Pow(Symbol('a'), Integer(2)), Mul(Rational(1, 8), Symbol('a')), Pow(Symbol('b'), Integer(2)), Mul(Rational(1, 2), Symbol('b')), Mul(Integer(-1), Pow(Symbol('r2'), Integer(2))), Rational(17, 256)), Integer(0)), LessThan(Add(Pow(Symbol('a'), Integer(2)), Mul(Rational(1, 2), Symbol('a')), Pow(Symbol('b'), Integer(2)), Mul(Rational(1, 8), Symbol('b')), Mul(Integer(-1), Pow(Symbol('r3'), Integer(2))), Rational(17, 256)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'r2':r2, 'r3':r3 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_8(a:sympy.Rational,b:sympy.Rational,r2:sympy.Rational,r3:sympy.Rational):
	#(a**2 + a/8 + b**2 + b/2 - r2**2 + 17/256 <= 0) & (a**2 + a/2 + b**2 + b/8 - r3**2 + 17/256 <= 0)

	pre_cond = And(LessThan(Add(Pow(Symbol('a'), Integer(2)), Mul(Rational(1, 8), Symbol('a')), Pow(Symbol('b'), Integer(2)), Mul(Rational(1, 2), Symbol('b')), Mul(Integer(-1), Pow(Symbol('r2'), Integer(2))), Rational(17, 256)), Integer(0)), LessThan(Add(Pow(Symbol('a'), Integer(2)), Mul(Rational(1, 2), Symbol('a')), Pow(Symbol('b'), Integer(2)), Mul(Rational(1, 8), Symbol('b')), Mul(Integer(-1), Pow(Symbol('r3'), Integer(2))), Rational(17, 256)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'r2':r2, 'r3':r3 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_9(a:sympy.Rational,b:sympy.Rational,r2:sympy.Rational,r3:sympy.Rational):
	#(-r1**2 + y**2 + 1/1024 <= 0) & (a**2 + a/16 + b**2 - 2*b*y - r2**2 + y**2 + 1/1024 <= 0) & (a**2 - 2*a*y + b**2 + b/16 - r3**2 + y**2 + 1/1024 <= 0)

	pre_cond = And(LessThan(Add(Mul(Integer(-1), Pow(Symbol('r1'), Integer(2))), Pow(Symbol('y'), Integer(2)), Rational(1, 1024)), Integer(0)), LessThan(Add(Pow(Symbol('a'), Integer(2)), Mul(Rational(1, 16), Symbol('a')), Pow(Symbol('b'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('b'), Symbol('y')), Mul(Integer(-1), Pow(Symbol('r2'), Integer(2))), Pow(Symbol('y'), Integer(2)), Rational(1, 1024)), Integer(0)), LessThan(Add(Pow(Symbol('a'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('a'), Symbol('y')), Pow(Symbol('b'), Integer(2)), Mul(Rational(1, 16), Symbol('b')), Mul(Integer(-1), Pow(Symbol('r3'), Integer(2))), Pow(Symbol('y'), Integer(2)), Rational(1, 1024)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'r2':r2, 'r3':r3 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_10(a:sympy.Rational,b:sympy.Rational,r2:sympy.Rational,r3:sympy.Rational):
	#(r1**2 >= 1/1024) & (a**2 + a/16 + b**2 - r2**2 + 1/1024 <= 0) & (a**2 + b**2 + b/16 - r3**2 + 1/1024 <= 0)

	pre_cond = And(GreaterThan(Pow(Symbol('r1'), Integer(2)), Rational(1, 1024)), LessThan(Add(Pow(Symbol('a'), Integer(2)), Mul(Rational(1, 16), Symbol('a')), Pow(Symbol('b'), Integer(2)), Mul(Integer(-1), Pow(Symbol('r2'), Integer(2))), Rational(1, 1024)), Integer(0)), LessThan(Add(Pow(Symbol('a'), Integer(2)), Pow(Symbol('b'), Integer(2)), Mul(Rational(1, 16), Symbol('b')), Mul(Integer(-1), Pow(Symbol('r3'), Integer(2))), Rational(1, 1024)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'r2':r2, 'r3':r3 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_11(a:sympy.Rational,b:sympy.Rational,r2:sympy.Rational,r3:sympy.Rational):
	#(a**2 + a/16 + b**2 - r2**2 + 1/1024 <= 0) & (a**2 + b**2 + b/16 - r3**2 + 1/1024 <= 0)

	pre_cond = And(LessThan(Add(Pow(Symbol('a'), Integer(2)), Mul(Rational(1, 16), Symbol('a')), Pow(Symbol('b'), Integer(2)), Mul(Integer(-1), Pow(Symbol('r2'), Integer(2))), Rational(1, 1024)), Integer(0)), LessThan(Add(Pow(Symbol('a'), Integer(2)), Pow(Symbol('b'), Integer(2)), Mul(Rational(1, 16), Symbol('b')), Mul(Integer(-1), Pow(Symbol('r3'), Integer(2))), Rational(1, 1024)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'r2':r2, 'r3':r3 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_12(a:sympy.Rational,b:sympy.Rational,r2:sympy.Rational,r3:sympy.Rational):
	#(-r1**2 + y**2 + 49/65536 <= 0) & (a**2 + 7*a/128 + b**2 - 2*b*y - r2**2 + y**2 + 49/65536 <= 0) & (a**2 - 2*a*y + b**2 + 7*b/128 - r3**2 + y**2 + 49/65536 <= 0)

	pre_cond = And(LessThan(Add(Mul(Integer(-1), Pow(Symbol('r1'), Integer(2))), Pow(Symbol('y'), Integer(2)), Rational(49, 65536)), Integer(0)), LessThan(Add(Pow(Symbol('a'), Integer(2)), Mul(Rational(7, 128), Symbol('a')), Pow(Symbol('b'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('b'), Symbol('y')), Mul(Integer(-1), Pow(Symbol('r2'), Integer(2))), Pow(Symbol('y'), Integer(2)), Rational(49, 65536)), Integer(0)), LessThan(Add(Pow(Symbol('a'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('a'), Symbol('y')), Pow(Symbol('b'), Integer(2)), Mul(Rational(7, 128), Symbol('b')), Mul(Integer(-1), Pow(Symbol('r3'), Integer(2))), Pow(Symbol('y'), Integer(2)), Rational(49, 65536)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'r2':r2, 'r3':r3 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_13(a:sympy.Rational,b:sympy.Rational,r2:sympy.Rational,r3:sympy.Rational):
	#(r1**2 >= 53/65536) & (a**2 - a/64 + b**2 + 7*b/128 - r3**2 + 53/65536 <= 0) & (a**2 + 7*a/128 + b**2 - b/64 - r2**2 + 53/65536 <= 0)

	pre_cond = And(GreaterThan(Pow(Symbol('r1'), Integer(2)), Rational(53, 65536)), LessThan(Add(Pow(Symbol('a'), Integer(2)), Mul(Integer(-1), Rational(1, 64), Symbol('a')), Pow(Symbol('b'), Integer(2)), Mul(Rational(7, 128), Symbol('b')), Mul(Integer(-1), Pow(Symbol('r3'), Integer(2))), Rational(53, 65536)), Integer(0)), LessThan(Add(Pow(Symbol('a'), Integer(2)), Mul(Rational(7, 128), Symbol('a')), Pow(Symbol('b'), Integer(2)), Mul(Integer(-1), Rational(1, 64), Symbol('b')), Mul(Integer(-1), Pow(Symbol('r2'), Integer(2))), Rational(53, 65536)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'r2':r2, 'r3':r3 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_14(a:sympy.Rational,b:sympy.Rational,r2:sympy.Rational,r3:sympy.Rational):
	#(a**2 - a/64 + b**2 + 7*b/128 - r3**2 + 53/65536 <= 0) & (a**2 + 7*a/128 + b**2 - b/64 - r2**2 + 53/65536 <= 0)

	pre_cond = And(LessThan(Add(Pow(Symbol('a'), Integer(2)), Mul(Integer(-1), Rational(1, 64), Symbol('a')), Pow(Symbol('b'), Integer(2)), Mul(Rational(7, 128), Symbol('b')), Mul(Integer(-1), Pow(Symbol('r3'), Integer(2))), Rational(53, 65536)), Integer(0)), LessThan(Add(Pow(Symbol('a'), Integer(2)), Mul(Rational(7, 128), Symbol('a')), Pow(Symbol('b'), Integer(2)), Mul(Integer(-1), Rational(1, 64), Symbol('b')), Mul(Integer(-1), Pow(Symbol('r2'), Integer(2))), Rational(53, 65536)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'r2':r2, 'r3':r3 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_15(a:sympy.Rational,b:sympy.Rational,r2:sympy.Rational,r3:sympy.Rational):
	#(-r1**2 + y**2 + 1/16384 <= 0) & (a**2 + a/64 + b**2 - 2*b*y - r2**2 + y**2 + 1/16384 <= 0) & (a**2 - 2*a*y + b**2 + b/64 - r3**2 + y**2 + 1/16384 <= 0)

	pre_cond = And(LessThan(Add(Mul(Integer(-1), Pow(Symbol('r1'), Integer(2))), Pow(Symbol('y'), Integer(2)), Rational(1, 16384)), Integer(0)), LessThan(Add(Pow(Symbol('a'), Integer(2)), Mul(Rational(1, 64), Symbol('a')), Pow(Symbol('b'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('b'), Symbol('y')), Mul(Integer(-1), Pow(Symbol('r2'), Integer(2))), Pow(Symbol('y'), Integer(2)), Rational(1, 16384)), Integer(0)), LessThan(Add(Pow(Symbol('a'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('a'), Symbol('y')), Pow(Symbol('b'), Integer(2)), Mul(Rational(1, 64), Symbol('b')), Mul(Integer(-1), Pow(Symbol('r3'), Integer(2))), Pow(Symbol('y'), Integer(2)), Rational(1, 16384)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'r2':r2, 'r3':r3 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_16(a:sympy.Rational,b:sympy.Rational,r2:sympy.Rational,r3:sympy.Rational):
	#(r1**2 >= 5/8192) & (a**2 - 3*a/64 + b**2 + b/64 - r3**2 + 5/8192 <= 0) & (a**2 + a/64 + b**2 - 3*b/64 - r2**2 + 5/8192 <= 0)

	pre_cond = And(GreaterThan(Pow(Symbol('r1'), Integer(2)), Rational(5, 8192)), LessThan(Add(Pow(Symbol('a'), Integer(2)), Mul(Integer(-1), Rational(3, 64), Symbol('a')), Pow(Symbol('b'), Integer(2)), Mul(Rational(1, 64), Symbol('b')), Mul(Integer(-1), Pow(Symbol('r3'), Integer(2))), Rational(5, 8192)), Integer(0)), LessThan(Add(Pow(Symbol('a'), Integer(2)), Mul(Rational(1, 64), Symbol('a')), Pow(Symbol('b'), Integer(2)), Mul(Integer(-1), Rational(3, 64), Symbol('b')), Mul(Integer(-1), Pow(Symbol('r2'), Integer(2))), Rational(5, 8192)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'r2':r2, 'r3':r3 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_17(a:sympy.Rational,b:sympy.Rational,r2:sympy.Rational,r3:sympy.Rational):
	#(a**2 - 3*a/64 + b**2 + b/64 - r3**2 + 5/8192 <= 0) & (a**2 + a/64 + b**2 - 3*b/64 - r2**2 + 5/8192 <= 0)

	pre_cond = And(LessThan(Add(Pow(Symbol('a'), Integer(2)), Mul(Integer(-1), Rational(3, 64), Symbol('a')), Pow(Symbol('b'), Integer(2)), Mul(Rational(1, 64), Symbol('b')), Mul(Integer(-1), Pow(Symbol('r3'), Integer(2))), Rational(5, 8192)), Integer(0)), LessThan(Add(Pow(Symbol('a'), Integer(2)), Mul(Rational(1, 64), Symbol('a')), Pow(Symbol('b'), Integer(2)), Mul(Integer(-1), Rational(3, 64), Symbol('b')), Mul(Integer(-1), Pow(Symbol('r2'), Integer(2))), Rational(5, 8192)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'r2':r2, 'r3':r3 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_18(a:sympy.Rational,b:sympy.Rational,r2:sympy.Rational,r3:sympy.Rational):
	#(-r1**2 + y**2 + 1/4096 <= 0) & (a**2 + a/32 + b**2 - 2*b*y - r2**2 + y**2 + 1/4096 <= 0) & (a**2 - 2*a*y + b**2 + b/32 - r3**2 + y**2 + 1/4096 <= 0)

	pre_cond = And(LessThan(Add(Mul(Integer(-1), Pow(Symbol('r1'), Integer(2))), Pow(Symbol('y'), Integer(2)), Rational(1, 4096)), Integer(0)), LessThan(Add(Pow(Symbol('a'), Integer(2)), Mul(Rational(1, 32), Symbol('a')), Pow(Symbol('b'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('b'), Symbol('y')), Mul(Integer(-1), Pow(Symbol('r2'), Integer(2))), Pow(Symbol('y'), Integer(2)), Rational(1, 4096)), Integer(0)), LessThan(Add(Pow(Symbol('a'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('a'), Symbol('y')), Pow(Symbol('b'), Integer(2)), Mul(Rational(1, 32), Symbol('b')), Mul(Integer(-1), Pow(Symbol('r3'), Integer(2))), Pow(Symbol('y'), Integer(2)), Rational(1, 4096)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'r2':r2, 'r3':r3 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_19(a:sympy.Rational,b:sympy.Rational,r2:sympy.Rational,r3:sympy.Rational):
	#(r1**2 >= 1/2048) & (a**2 - a/32 + b**2 + b/32 - r3**2 + 1/2048 <= 0) & (a**2 + a/32 + b**2 - b/32 - r2**2 + 1/2048 <= 0)

	pre_cond = And(GreaterThan(Pow(Symbol('r1'), Integer(2)), Rational(1, 2048)), LessThan(Add(Pow(Symbol('a'), Integer(2)), Mul(Integer(-1), Rational(1, 32), Symbol('a')), Pow(Symbol('b'), Integer(2)), Mul(Rational(1, 32), Symbol('b')), Mul(Integer(-1), Pow(Symbol('r3'), Integer(2))), Rational(1, 2048)), Integer(0)), LessThan(Add(Pow(Symbol('a'), Integer(2)), Mul(Rational(1, 32), Symbol('a')), Pow(Symbol('b'), Integer(2)), Mul(Integer(-1), Rational(1, 32), Symbol('b')), Mul(Integer(-1), Pow(Symbol('r2'), Integer(2))), Rational(1, 2048)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'r2':r2, 'r3':r3 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_20(a:sympy.Rational,b:sympy.Rational,r2:sympy.Rational,r3:sympy.Rational):
	#(a**2 - a/32 + b**2 + b/32 - r3**2 + 1/2048 <= 0) & (a**2 + a/32 + b**2 - b/32 - r2**2 + 1/2048 <= 0)

	pre_cond = And(LessThan(Add(Pow(Symbol('a'), Integer(2)), Mul(Integer(-1), Rational(1, 32), Symbol('a')), Pow(Symbol('b'), Integer(2)), Mul(Rational(1, 32), Symbol('b')), Mul(Integer(-1), Pow(Symbol('r3'), Integer(2))), Rational(1, 2048)), Integer(0)), LessThan(Add(Pow(Symbol('a'), Integer(2)), Mul(Rational(1, 32), Symbol('a')), Pow(Symbol('b'), Integer(2)), Mul(Integer(-1), Rational(1, 32), Symbol('b')), Mul(Integer(-1), Pow(Symbol('r2'), Integer(2))), Rational(1, 2048)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'r2':r2, 'r3':r3 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_21(a:sympy.Rational,b:sympy.Rational,r2:sympy.Rational,r3:sympy.Rational):
	#(-r1**2 + y**2 + 1/65536 <= 0) & (a**2 + a/128 + b**2 - 2*b*y - r2**2 + y**2 + 1/65536 <= 0) & (a**2 - 2*a*y + b**2 + b/128 - r3**2 + y**2 + 1/65536 <= 0)

	pre_cond = And(LessThan(Add(Mul(Integer(-1), Pow(Symbol('r1'), Integer(2))), Pow(Symbol('y'), Integer(2)), Rational(1, 65536)), Integer(0)), LessThan(Add(Pow(Symbol('a'), Integer(2)), Mul(Rational(1, 128), Symbol('a')), Pow(Symbol('b'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('b'), Symbol('y')), Mul(Integer(-1), Pow(Symbol('r2'), Integer(2))), Pow(Symbol('y'), Integer(2)), Rational(1, 65536)), Integer(0)), LessThan(Add(Pow(Symbol('a'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('a'), Symbol('y')), Pow(Symbol('b'), Integer(2)), Mul(Rational(1, 128), Symbol('b')), Mul(Integer(-1), Pow(Symbol('r3'), Integer(2))), Pow(Symbol('y'), Integer(2)), Rational(1, 65536)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'r2':r2, 'r3':r3 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_22(a:sympy.Rational,b:sympy.Rational,r2:sympy.Rational,r3:sympy.Rational):
	#(r1**2 >= 17/65536) & (a**2 - a/32 + b**2 + b/128 - r3**2 + 17/65536 <= 0) & (a**2 + a/128 + b**2 - b/32 - r2**2 + 17/65536 <= 0)

	pre_cond = And(GreaterThan(Pow(Symbol('r1'), Integer(2)), Rational(17, 65536)), LessThan(Add(Pow(Symbol('a'), Integer(2)), Mul(Integer(-1), Rational(1, 32), Symbol('a')), Pow(Symbol('b'), Integer(2)), Mul(Rational(1, 128), Symbol('b')), Mul(Integer(-1), Pow(Symbol('r3'), Integer(2))), Rational(17, 65536)), Integer(0)), LessThan(Add(Pow(Symbol('a'), Integer(2)), Mul(Rational(1, 128), Symbol('a')), Pow(Symbol('b'), Integer(2)), Mul(Integer(-1), Rational(1, 32), Symbol('b')), Mul(Integer(-1), Pow(Symbol('r2'), Integer(2))), Rational(17, 65536)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'r2':r2, 'r3':r3 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_23(a:sympy.Rational,b:sympy.Rational,r2:sympy.Rational,r3:sympy.Rational):
	#(a**2 - a/32 + b**2 + b/128 - r3**2 + 17/65536 <= 0) & (a**2 + a/128 + b**2 - b/32 - r2**2 + 17/65536 <= 0)

	pre_cond = And(LessThan(Add(Pow(Symbol('a'), Integer(2)), Mul(Integer(-1), Rational(1, 32), Symbol('a')), Pow(Symbol('b'), Integer(2)), Mul(Rational(1, 128), Symbol('b')), Mul(Integer(-1), Pow(Symbol('r3'), Integer(2))), Rational(17, 65536)), Integer(0)), LessThan(Add(Pow(Symbol('a'), Integer(2)), Mul(Rational(1, 128), Symbol('a')), Pow(Symbol('b'), Integer(2)), Mul(Integer(-1), Rational(1, 32), Symbol('b')), Mul(Integer(-1), Pow(Symbol('r2'), Integer(2))), Rational(17, 65536)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'r2':r2, 'r3':r3 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_24(a:sympy.Rational,b:sympy.Rational,r2:sympy.Rational,r3:sympy.Rational):
	#(-r1**2 + y**2 + 1/262144 <= 0) & (a**2 + a/256 + b**2 - 2*b*y - r2**2 + y**2 + 1/262144 <= 0) & (a**2 - 2*a*y + b**2 + b/256 - r3**2 + y**2 + 1/262144 <= 0)

	pre_cond = And(LessThan(Add(Mul(Integer(-1), Pow(Symbol('r1'), Integer(2))), Pow(Symbol('y'), Integer(2)), Rational(1, 262144)), Integer(0)), LessThan(Add(Pow(Symbol('a'), Integer(2)), Mul(Rational(1, 256), Symbol('a')), Pow(Symbol('b'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('b'), Symbol('y')), Mul(Integer(-1), Pow(Symbol('r2'), Integer(2))), Pow(Symbol('y'), Integer(2)), Rational(1, 262144)), Integer(0)), LessThan(Add(Pow(Symbol('a'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('a'), Symbol('y')), Pow(Symbol('b'), Integer(2)), Mul(Rational(1, 256), Symbol('b')), Mul(Integer(-1), Pow(Symbol('r3'), Integer(2))), Pow(Symbol('y'), Integer(2)), Rational(1, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'r2':r2, 'r3':r3 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_25(a:sympy.Rational,b:sympy.Rational,r2:sympy.Rational,r3:sympy.Rational):
	#(r1**2 >= 65/262144) & (a**2 - a/32 + b**2 + b/256 - r3**2 + 65/262144 <= 0) & (a**2 + a/256 + b**2 - b/32 - r2**2 + 65/262144 <= 0)

	pre_cond = And(GreaterThan(Pow(Symbol('r1'), Integer(2)), Rational(65, 262144)), LessThan(Add(Pow(Symbol('a'), Integer(2)), Mul(Integer(-1), Rational(1, 32), Symbol('a')), Pow(Symbol('b'), Integer(2)), Mul(Rational(1, 256), Symbol('b')), Mul(Integer(-1), Pow(Symbol('r3'), Integer(2))), Rational(65, 262144)), Integer(0)), LessThan(Add(Pow(Symbol('a'), Integer(2)), Mul(Rational(1, 256), Symbol('a')), Pow(Symbol('b'), Integer(2)), Mul(Integer(-1), Rational(1, 32), Symbol('b')), Mul(Integer(-1), Pow(Symbol('r2'), Integer(2))), Rational(65, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'r2':r2, 'r3':r3 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_26(a:sympy.Rational,b:sympy.Rational,r2:sympy.Rational,r3:sympy.Rational):
	#(a**2 - a/32 + b**2 + b/256 - r3**2 + 65/262144 <= 0) & (a**2 + a/256 + b**2 - b/32 - r2**2 + 65/262144 <= 0)

	pre_cond = And(LessThan(Add(Pow(Symbol('a'), Integer(2)), Mul(Integer(-1), Rational(1, 32), Symbol('a')), Pow(Symbol('b'), Integer(2)), Mul(Rational(1, 256), Symbol('b')), Mul(Integer(-1), Pow(Symbol('r3'), Integer(2))), Rational(65, 262144)), Integer(0)), LessThan(Add(Pow(Symbol('a'), Integer(2)), Mul(Rational(1, 256), Symbol('a')), Pow(Symbol('b'), Integer(2)), Mul(Integer(-1), Rational(1, 32), Symbol('b')), Mul(Integer(-1), Pow(Symbol('r2'), Integer(2))), Rational(65, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'r2':r2, 'r3':r3 })

	if eval==True:
		assert eval!=False
		return True
	return False


def post_condition(a:sympy.Rational, b:sympy.Rational, r2:sympy.Rational, r3:sympy.Rational, x:sympy.Rational, y:sympy.Rational, r1:sympy.Rational):
	# (0 >= -r1**2 + x**2 + y**2) & (0 >= a**2 - 2*a*x + b**2 - 2*b*y - r2**2 + x**2 + y**2) & (0 >= a**2 - 2*a*y + b**2 - 2*b*x - r3**2 + x**2 + y**2)

	post_cond =  And(GreaterThan(Integer(0), Add(Mul(Integer(-1), Pow(Symbol('r1'), Integer(2))), Pow(Symbol('x'), Integer(2)), Pow(Symbol('y'), Integer(2)))), GreaterThan(Integer(0), Add(Pow(Symbol('a'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('a'), Symbol('x')), Pow(Symbol('b'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('b'), Symbol('y')), Mul(Integer(-1), Pow(Symbol('r2'), Integer(2))), Pow(Symbol('x'), Integer(2)), Pow(Symbol('y'), Integer(2)))), GreaterThan(Integer(0), Add(Pow(Symbol('a'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('a'), Symbol('y')), Pow(Symbol('b'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('b'), Symbol('x')), Mul(Integer(-1), Pow(Symbol('r3'), Integer(2))), Pow(Symbol('x'), Integer(2)), Pow(Symbol('y'), Integer(2)))))

	eval = post_cond.subs( { 'a':a, 'b':b, 'r2':r2, 'r3':r3, 'x':x, 'y':y, 'r1':r1 })

	return eval == sympy.logic.boolalg.BooleanTrue





if __name__=="__main__":
	
	ip_0=int(input("enter integer numerator of a:\n"))
	ip_1=int(input("enter integer denominator of a:\n"))
	assert(ip_1!=0), ("Error denominator entered is 0")
	a=sympy.Rational(ip_0,ip_1)
	
	
	ip_0=int(input("enter integer numerator of b:\n"))
	ip_1=int(input("enter integer denominator of b:\n"))
	assert(ip_1!=0), ("Error denominator entered is 0")
	b=sympy.Rational(ip_0,ip_1)
	
	
	ip_0=int(input("enter integer numerator of r2:\n"))
	ip_1=int(input("enter integer denominator of r2:\n"))
	assert(ip_1!=0), ("Error denominator entered is 0")
	r2=sympy.Rational(ip_0,ip_1)
	
	
	ip_0=int(input("enter integer numerator of r3:\n"))
	ip_1=int(input("enter integer denominator of r3:\n"))
	assert(ip_1!=0), ("Error denominator entered is 0")
	r3=sympy.Rational(ip_0,ip_1)
	
	
	
	
	if pre_condition_0(a=a,b=b,r2=r2,r3=r3)==True:
		print("pre_condition_0 SAT")
		print('x = 1/8')
		print('y = 1/2')
		print('r1 = 1')
		print('a = -1/2')
		print('b = -1/2')
		print('r2 = 2')
		print('r3 = -2')
		exit(0)
	
	
	if pre_condition_1(a=a,b=b,r2=r2,r3=r3)==True:
		print("pre_condition_1 SAT")
		print('x = 1/8')
		print('y = 1/2')
		print('r1 = 1')
		print('a = -1/2')
		print('b = -1/2')
		print('r2 = 2')
		print('r3 = -2')
		exit(0)
	
	
	if pre_condition_2(a=a,b=b,r2=r2,r3=r3)==True:
		print("pre_condition_2 SAT")
		print('x = 1/8')
		print('y = 1/2')
		print('r1 = 1')
		print('a = -1/2')
		print('b = -1/2')
		print('r2 = 2')
		print('r3 = -2')
		exit(0)
	
	
	if pre_condition_3(a=a,b=b,r2=r2,r3=r3)==True:
		print("pre_condition_3 SAT")
		print('x = 0')
		print('y = 0')
		print('r1 = 0')
		print('a = 0')
		print('b = 0')
		print('r2 = 0')
		print('r3 = 0')
		exit(0)
	
	
	if pre_condition_4(a=a,b=b,r2=r2,r3=r3)==True:
		print("pre_condition_4 SAT")
		print('x = 0')
		print('y = 0')
		print('r1 = 0')
		print('a = 0')
		print('b = 0')
		print('r2 = 0')
		print('r3 = 0')
		exit(0)
	
	
	if pre_condition_5(a=a,b=b,r2=r2,r3=r3)==True:
		print("pre_condition_5 SAT")
		print('x = 0')
		print('y = 0')
		print('r1 = 0')
		print('a = 0')
		print('b = 0')
		print('r2 = 0')
		print('r3 = 0')
		exit(0)
	
	
	if pre_condition_6(a=a,b=b,r2=r2,r3=r3)==True:
		print("pre_condition_6 SAT")
		print('x = -1/16')
		print('y = -1/4')
		print('r1 = 17/64')
		print('a = 0')
		print('b = -1')
		print('r2 = -1')
		print('r3 = -63/64')
		exit(0)
	
	
	if pre_condition_7(a=a,b=b,r2=r2,r3=r3)==True:
		print("pre_condition_7 SAT")
		print('x = -1/16')
		print('y = -1/4')
		print('r1 = 17/64')
		print('a = 0')
		print('b = -1')
		print('r2 = -1')
		print('r3 = -63/64')
		exit(0)
	
	
	if pre_condition_8(a=a,b=b,r2=r2,r3=r3)==True:
		print("pre_condition_8 SAT")
		print('x = -1/16')
		print('y = -1/4')
		print('r1 = 17/64')
		print('a = 0')
		print('b = -1')
		print('r2 = -1')
		print('r3 = -63/64')
		exit(0)
	
	
	if pre_condition_9(a=a,b=b,r2=r2,r3=r3)==True:
		print("pre_condition_9 SAT")
		print('x = -1/32')
		print('y = 0')
		print('r1 = 3/64')
		print('a = 1/4')
		print('b = -1/8')
		print('r2 = -5/16')
		print('r3 = 35/128')
		exit(0)
	
	
	if pre_condition_10(a=a,b=b,r2=r2,r3=r3)==True:
		print("pre_condition_10 SAT")
		print('x = -1/32')
		print('y = 0')
		print('r1 = 3/64')
		print('a = 1/4')
		print('b = -1/8')
		print('r2 = -5/16')
		print('r3 = 35/128')
		exit(0)
	
	
	if pre_condition_11(a=a,b=b,r2=r2,r3=r3)==True:
		print("pre_condition_11 SAT")
		print('x = -1/32')
		print('y = 0')
		print('r1 = 3/64')
		print('a = 1/4')
		print('b = -1/8')
		print('r2 = -5/16')
		print('r3 = 35/128')
		exit(0)
	
	
	if pre_condition_12(a=a,b=b,r2=r2,r3=r3)==True:
		print("pre_condition_12 SAT")
		print('x = -7/256')
		print('y = 1/128')
		print('r1 = -15/512')
		print('a = 1/64')
		print('b = -3/128')
		print('r2 = -1/8')
		print('r3 = 5/512')
		exit(0)
	
	
	if pre_condition_13(a=a,b=b,r2=r2,r3=r3)==True:
		print("pre_condition_13 SAT")
		print('x = -7/256')
		print('y = 1/128')
		print('r1 = -15/512')
		print('a = 1/64')
		print('b = -3/128')
		print('r2 = -1/8')
		print('r3 = 5/512')
		exit(0)
	
	
	if pre_condition_14(a=a,b=b,r2=r2,r3=r3)==True:
		print("pre_condition_14 SAT")
		print('x = -7/256')
		print('y = 1/128')
		print('r1 = -15/512')
		print('a = 1/64')
		print('b = -3/128')
		print('r2 = -1/8')
		print('r3 = 5/512')
		exit(0)
	
	
	if pre_condition_15(a=a,b=b,r2=r2,r3=r3)==True:
		print("pre_condition_15 SAT")
		print('x = -1/128')
		print('y = 3/128')
		print('r1 = -7/256')
		print('a = 1/64')
		print('b = -1/64')
		print('r2 = 3/64')
		print('r3 = 3/256')
		exit(0)
	
	
	if pre_condition_16(a=a,b=b,r2=r2,r3=r3)==True:
		print("pre_condition_16 SAT")
		print('x = -1/128')
		print('y = 3/128')
		print('r1 = -7/256')
		print('a = 1/64')
		print('b = -1/64')
		print('r2 = 3/64')
		print('r3 = 3/256')
		exit(0)
	
	
	if pre_condition_17(a=a,b=b,r2=r2,r3=r3)==True:
		print("pre_condition_17 SAT")
		print('x = -1/128')
		print('y = 3/128')
		print('r1 = -7/256')
		print('a = 1/64')
		print('b = -1/64')
		print('r2 = 3/64')
		print('r3 = 3/256')
		exit(0)
	
	
	if pre_condition_18(a=a,b=b,r2=r2,r3=r3)==True:
		print("pre_condition_18 SAT")
		print('x = -1/64')
		print('y = 1/64')
		print('r1 = -3/128')
		print('a = 1')
		print('b = -1')
		print('r2 = -23533/16384')
		print('r3 = -357/256')
		exit(0)
	
	
	if pre_condition_19(a=a,b=b,r2=r2,r3=r3)==True:
		print("pre_condition_19 SAT")
		print('x = -1/64')
		print('y = 1/64')
		print('r1 = -3/128')
		print('a = 1')
		print('b = -1')
		print('r2 = -23533/16384')
		print('r3 = -357/256')
		exit(0)
	
	
	if pre_condition_20(a=a,b=b,r2=r2,r3=r3)==True:
		print("pre_condition_20 SAT")
		print('x = -1/64')
		print('y = 1/64')
		print('r1 = -3/128')
		print('a = 1')
		print('b = -1')
		print('r2 = -23533/16384')
		print('r3 = -357/256')
		exit(0)
	
	
	if pre_condition_21(a=a,b=b,r2=r2,r3=r3)==True:
		print("pre_condition_21 SAT")
		print('x = -1/256')
		print('y = 1/64')
		print('r1 = -5/256')
		print('a = 1/64')
		print('b = -1/128')
		print('r2 = 1/32')
		print('r3 = 3/512')
		exit(0)
	
	
	if pre_condition_22(a=a,b=b,r2=r2,r3=r3)==True:
		print("pre_condition_22 SAT")
		print('x = -1/256')
		print('y = 1/64')
		print('r1 = -5/256')
		print('a = 1/64')
		print('b = -1/128')
		print('r2 = 1/32')
		print('r3 = 3/512')
		exit(0)
	
	
	if pre_condition_23(a=a,b=b,r2=r2,r3=r3)==True:
		print("pre_condition_23 SAT")
		print('x = -1/256')
		print('y = 1/64')
		print('r1 = -5/256')
		print('a = 1/64')
		print('b = -1/128')
		print('r2 = 1/32')
		print('r3 = 3/512')
		exit(0)
	
	
	if pre_condition_24(a=a,b=b,r2=r2,r3=r3)==True:
		print("pre_condition_24 SAT")
		print('x = -1/512')
		print('y = 1/64')
		print('r1 = 65/4096')
		print('a = 1/64')
		print('b = -1/512')
		print('r2 = -7/256')
		print('r3 = 0')
		exit(0)
	
	
	if pre_condition_25(a=a,b=b,r2=r2,r3=r3)==True:
		print("pre_condition_25 SAT")
		print('x = -1/512')
		print('y = 1/64')
		print('r1 = 65/4096')
		print('a = 1/64')
		print('b = -1/512')
		print('r2 = -7/256')
		print('r3 = 0')
		exit(0)
	
	
	if pre_condition_26(a=a,b=b,r2=r2,r3=r3)==True:
		print("pre_condition_26 SAT")
		print('x = -1/512')
		print('y = 1/64')
		print('r1 = 65/4096')
		print('a = 1/64')
		print('b = -1/512')
		print('r2 = -7/256')
		print('r3 = 0')
		exit(0)


	print("UNKNOWN")
	exit(0)
