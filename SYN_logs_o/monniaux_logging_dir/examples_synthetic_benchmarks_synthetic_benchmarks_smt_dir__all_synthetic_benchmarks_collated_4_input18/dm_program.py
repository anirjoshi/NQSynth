import sympy
from sympy import *

def pre_condition_0(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 > 0) & (b - z**3 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3)))), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3)))), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > 0) & (b - z**3 > 0) & (c - z**3 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3)))), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3)))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_2(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > 0) & (b > 0) & (c > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(0)), StrictGreaterThan(Symbol('b'), Integer(0)), StrictGreaterThan(Symbol('c'), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_3(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 1 > 0) & (b - z**3 + 1 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(1)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_4(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -1) & (c - z**3 > 0) & (b - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-1)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3)))), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_5(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -1) & (b > -1) & (c > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-1)), StrictGreaterThan(Symbol('b'), Integer(-1)), StrictGreaterThan(Symbol('c'), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_6(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 8 > 0) & (b - z**3 + 8 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(8)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(8)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_7(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -9) & (b - z**3 + 8 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-9)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(8)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_8(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -9) & (b > -65/8) & (c > -9/8)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-9)), StrictGreaterThan(Symbol('b'), Rational(-65, 8)), StrictGreaterThan(Symbol('c'), Rational(-9, 8)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_9(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 27 > 0) & (b - z**3 + 27 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(27)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(27)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_10(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -35) & (b - z**3 + 27 > 0) & (c - z**3 + 8 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-35)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(27)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(8)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_11(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -35) & (b > -26) & (c > -7)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-35)), StrictGreaterThan(Symbol('b'), Integer(-26)), StrictGreaterThan(Symbol('c'), Integer(-7)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_12(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 64 > 0) & (b - z**3 + 64 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(64)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(64)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_13(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -65) & (b - z**3 + 64 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-65)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(64)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_14(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -65) & (b > -65) & (c > -2)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-65)), StrictGreaterThan(Symbol('b'), Integer(-65)), StrictGreaterThan(Symbol('c'), Integer(-2)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_15(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 125 > 0) & (b - z**3 + 125 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(125)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(125)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_16(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -126) & (b - z**3 + 125 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-126)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(125)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_17(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -126) & (b > -999/8) & (c > -7/8)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-126)), StrictGreaterThan(Symbol('b'), Rational(-999, 8)), StrictGreaterThan(Symbol('c'), Rational(-7, 8)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_18(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 216 > 0) & (b - z**3 + 216 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(216)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_19(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -217) & (b - z**3 + 216 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-217)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(216)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_20(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -217) & (b > -1727/8) & (c > -7/8)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-217)), StrictGreaterThan(Symbol('b'), Rational(-1727, 8)), StrictGreaterThan(Symbol('c'), Rational(-7, 8)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_21(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 4096 > 0) & (b - z**3 + 4096 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(4096)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(4096)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_22(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -4096) & (c - z**3 > 0) & (b - z**3 + 4096 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-4096)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3)))), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(4096)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_23(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -4096) & (b > -32767/8) & (c > 1/8)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-4096)), StrictGreaterThan(Symbol('b'), Rational(-32767, 8)), StrictGreaterThan(Symbol('c'), Rational(1, 8)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_24(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 4913 > 0) & (b - z**3 + 4913 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(4913)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(4913)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_25(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -4914) & (b - z**3 + 4913 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-4914)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(4913)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_26(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -4914) & (b > -39303/8) & (c > -7/8)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-4914)), StrictGreaterThan(Symbol('b'), Rational(-39303, 8)), StrictGreaterThan(Symbol('c'), Rational(-7, 8)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_27(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 5832 > 0) & (b - z**3 + 5832 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(5832)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(5832)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_28(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -5833) & (b - z**3 + 5832 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-5833)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(5832)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_29(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -5833) & (b > -46655/8) & (c > -7/8)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-5833)), StrictGreaterThan(Symbol('b'), Rational(-46655, 8)), StrictGreaterThan(Symbol('c'), Rational(-7, 8)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_30(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 6859 > 0) & (b - z**3 + 6859 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(6859)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(6859)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_31(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -6860) & (b - z**3 + 6859 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-6860)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(6859)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_32(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -6860) & (b > -438975/64) & (c > -63/64)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-6860)), StrictGreaterThan(Symbol('b'), Rational(-438975, 64)), StrictGreaterThan(Symbol('c'), Rational(-63, 64)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_33(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 8000 > 0) & (b - z**3 + 8000 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(8000)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(8000)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_34(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -8001) & (b - z**3 + 8000 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-8001)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(8000)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_35(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -8001) & (b > -8001) & (c > -2)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-8001)), StrictGreaterThan(Symbol('b'), Integer(-8001)), StrictGreaterThan(Symbol('c'), Integer(-2)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_36(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 9261 > 0) & (b - z**3 + 9261 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(9261)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(9261)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_37(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -9262) & (b - z**3 + 9261 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-9262)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(9261)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_38(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -9262) & (b > -9269) & (c > -9)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-9262)), StrictGreaterThan(Symbol('b'), Integer(-9269)), StrictGreaterThan(Symbol('c'), Integer(-9)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_39(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 10648 > 0) & (b - z**3 + 10648 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(10648)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(10648)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_40(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -10649) & (b - z**3 + 10648 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-10649)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(10648)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_41(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -10649) & (b > -85183/8) & (c > -7/8)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-10649)), StrictGreaterThan(Symbol('b'), Rational(-85183, 8)), StrictGreaterThan(Symbol('c'), Rational(-7, 8)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_42(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 12167 > 0) & (b - z**3 + 12167 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(12167)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(12167)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_43(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -12168) & (b - z**3 + 12167 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-12168)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(12167)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_44(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -12168) & (b > -12168) & (c > -2)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-12168)), StrictGreaterThan(Symbol('b'), Integer(-12168)), StrictGreaterThan(Symbol('c'), Integer(-2)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_45(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 13824 > 0) & (b - z**3 + 13824 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(13824)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(13824)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_46(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -13825) & (b - z**3 + 13824 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-13825)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(13824)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_47(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -13825) & (b > -13832) & (c > -9)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-13825)), StrictGreaterThan(Symbol('b'), Integer(-13832)), StrictGreaterThan(Symbol('c'), Integer(-9)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_48(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 15625 > 0) & (b - z**3 + 15625 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(15625)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(15625)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_49(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -15626) & (b - z**3 + 15625 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-15626)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(15625)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_50(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -15626) & (b > -124999/8) & (c > -7/8)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-15626)), StrictGreaterThan(Symbol('b'), Rational(-124999, 8)), StrictGreaterThan(Symbol('c'), Rational(-7, 8)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_51(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 17576 > 0) & (b - z**3 + 17576 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(17576)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(17576)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_52(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -17577) & (b - z**3 + 17576 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-17577)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(17576)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_53(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -17577) & (b > -17577) & (c > -2)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-17577)), StrictGreaterThan(Symbol('b'), Integer(-17577)), StrictGreaterThan(Symbol('c'), Integer(-2)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_54(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 19683 > 0) & (b - z**3 + 19683 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(19683)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(19683)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_55(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -19684) & (b - z**3 + 19683 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-19684)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(19683)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_56(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -19684) & (b > -19691) & (c > -9)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-19684)), StrictGreaterThan(Symbol('b'), Integer(-19691)), StrictGreaterThan(Symbol('c'), Integer(-9)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_57(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 21952 > 0) & (b - z**3 + 21952 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(21952)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(21952)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_58(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -21953) & (b - z**3 + 21952 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-21953)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(21952)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_59(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -21953) & (b > -175615/8) & (c > -7/8)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-21953)), StrictGreaterThan(Symbol('b'), Rational(-175615, 8)), StrictGreaterThan(Symbol('c'), Rational(-7, 8)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_60(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 24389 > 0) & (b - z**3 + 24389 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(24389)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(24389)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_61(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -24390) & (b - z**3 + 24389 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-24390)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(24389)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_62(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -24390) & (b > -24390) & (c > -2)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-24390)), StrictGreaterThan(Symbol('b'), Integer(-24390)), StrictGreaterThan(Symbol('c'), Integer(-2)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_63(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 27000 > 0) & (b - z**3 + 27000 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(27000)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(27000)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_64(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -27001) & (b - z**3 + 27000 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-27001)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(27000)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_65(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -27001) & (b > -27008) & (c > -9)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-27001)), StrictGreaterThan(Symbol('b'), Integer(-27008)), StrictGreaterThan(Symbol('c'), Integer(-9)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_66(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 29791 > 0) & (b - z**3 + 29791 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(29791)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(29791)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_67(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -29792) & (b - z**3 + 29791 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-29792)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(29791)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_68(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -29792) & (b > -29818) & (c > -28)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-29792)), StrictGreaterThan(Symbol('b'), Integer(-29818)), StrictGreaterThan(Symbol('c'), Integer(-28)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_69(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 32768 > 0) & (b - z**3 + 32768 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(32768)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(32768)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_70(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -32769) & (b - z**3 + 32768 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-32769)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(32768)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_71(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -32769) & (b > -262143/8) & (c > -7/8)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-32769)), StrictGreaterThan(Symbol('b'), Rational(-262143, 8)), StrictGreaterThan(Symbol('c'), Rational(-7, 8)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_72(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 35937 > 0) & (b - z**3 + 35937 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(35937)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(35937)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_73(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -35938) & (b - z**3 + 35937 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-35938)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(35937)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_74(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -35938) & (b > -35964) & (c > -28)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-35938)), StrictGreaterThan(Symbol('b'), Integer(-35964)), StrictGreaterThan(Symbol('c'), Integer(-28)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_75(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 39304 > 0) & (b - z**3 + 39304 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(39304)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(39304)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_76(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -39305) & (b - z**3 + 39304 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-39305)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(39304)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_77(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -39305) & (b > -39331) & (c > -28)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-39305)), StrictGreaterThan(Symbol('b'), Integer(-39331)), StrictGreaterThan(Symbol('c'), Integer(-28)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_78(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 42875 > 0) & (b - z**3 + 42875 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(42875)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(42875)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_79(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -42876) & (b - z**3 + 42875 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-42876)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(42875)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_80(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -42876) & (b > -42939) & (c > -65)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-42876)), StrictGreaterThan(Symbol('b'), Integer(-42939)), StrictGreaterThan(Symbol('c'), Integer(-65)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_81(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 46656 > 0) & (b - z**3 + 46656 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(46656)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(46656)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_82(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -46657) & (b - z**3 + 46656 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-46657)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(46656)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_83(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -46657) & (b > -373247/8) & (c > -7/8)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-46657)), StrictGreaterThan(Symbol('b'), Rational(-373247, 8)), StrictGreaterThan(Symbol('c'), Rational(-7, 8)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_84(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 50653 > 0) & (b - z**3 + 50653 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(50653)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(50653)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_85(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -50654) & (b - z**3 + 50653 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-50654)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(50653)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_86(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -50654) & (b > -50717) & (c > -65)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-50654)), StrictGreaterThan(Symbol('b'), Integer(-50717)), StrictGreaterThan(Symbol('c'), Integer(-65)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_87(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 54872 > 0) & (b - z**3 + 54872 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(54872)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(54872)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_88(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -54873) & (b - z**3 + 54872 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-54873)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(54872)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_89(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -54873) & (b > -54936) & (c > -65)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-54873)), StrictGreaterThan(Symbol('b'), Integer(-54936)), StrictGreaterThan(Symbol('c'), Integer(-65)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_90(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 59319 > 0) & (b - z**3 + 59319 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(59319)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(59319)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_91(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -59320) & (b - z**3 + 59319 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-59320)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(59319)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_92(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -59320) & (b > -59444) & (c > -126)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-59320)), StrictGreaterThan(Symbol('b'), Integer(-59444)), StrictGreaterThan(Symbol('c'), Integer(-126)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_93(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 64000 > 0) & (b - z**3 + 64000 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(64000)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(64000)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_94(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -64001) & (b - z**3 + 64000 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-64001)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(64000)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_95(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -64001) & (b > -64216) & (c > -217)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-64001)), StrictGreaterThan(Symbol('b'), Integer(-64216)), StrictGreaterThan(Symbol('c'), Integer(-217)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_96(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 68921 > 0) & (b - z**3 + 68921 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(68921)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(68921)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_97(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -68922) & (b - z**3 + 68921 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-68922)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(68921)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_98(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -68922) & (b > -551367/8) & (c > -7/8)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-68922)), StrictGreaterThan(Symbol('b'), Rational(-551367, 8)), StrictGreaterThan(Symbol('c'), Rational(-7, 8)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_99(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 74088 > 0) & (b - z**3 + 74088 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(74088)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(74088)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_100(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -74089) & (b - z**3 + 74088 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-74089)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(74088)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_101(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -74089) & (b > -74096) & (c > -9)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-74089)), StrictGreaterThan(Symbol('b'), Integer(-74096)), StrictGreaterThan(Symbol('c'), Integer(-9)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_102(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 79507 > 0) & (b - z**3 + 79507 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(79507)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(79507)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_103(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -79508) & (b - z**3 + 79507 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-79508)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(79507)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_104(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -79508) & (b > -79723) & (c > -217)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-79508)), StrictGreaterThan(Symbol('b'), Integer(-79723)), StrictGreaterThan(Symbol('c'), Integer(-217)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_105(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 85184 > 0) & (b - z**3 + 85184 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(85184)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(85184)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_106(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -85185) & (b - z**3 + 85184 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-85185)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(85184)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_107(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -85185) & (b > -85527) & (c > -344)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-85185)), StrictGreaterThan(Symbol('b'), Integer(-85527)), StrictGreaterThan(Symbol('c'), Integer(-344)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_108(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 91125 > 0) & (b - z**3 + 91125 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(91125)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(91125)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_109(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -91126) & (b - z**3 + 91125 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-91126)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(91125)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_110(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -91126) & (b > -728999/8) & (c > -7/8)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-91126)), StrictGreaterThan(Symbol('b'), Rational(-728999, 8)), StrictGreaterThan(Symbol('c'), Rational(-7, 8)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_111(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 97336 > 0) & (b - z**3 + 97336 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(97336)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(97336)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_112(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -97337) & (b - z**3 + 97336 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-97337)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(97336)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_113(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -97337) & (b > -97337) & (c > -2)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-97337)), StrictGreaterThan(Symbol('b'), Integer(-97337)), StrictGreaterThan(Symbol('c'), Integer(-2)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_114(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 103823 > 0) & (b - z**3 + 103823 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(103823)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(103823)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_115(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -103824) & (b - z**3 + 103823 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-103824)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(103823)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_116(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -103824) & (b > -103850) & (c > -28)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-103824)), StrictGreaterThan(Symbol('b'), Integer(-103850)), StrictGreaterThan(Symbol('c'), Integer(-28)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_117(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 110592 > 0) & (b - z**3 + 110592 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(110592)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(110592)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_118(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -110593) & (b - z**3 + 110592 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-110593)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(110592)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_119(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -110593) & (b > -110656) & (c > -65)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-110593)), StrictGreaterThan(Symbol('b'), Integer(-110656)), StrictGreaterThan(Symbol('c'), Integer(-65)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_120(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 117649 > 0) & (b - z**3 + 117649 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(117649)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(117649)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_121(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -117650) & (b - z**3 + 117649 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-117650)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(117649)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_122(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -117650) & (b > -117774) & (c > -126)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-117650)), StrictGreaterThan(Symbol('b'), Integer(-117774)), StrictGreaterThan(Symbol('c'), Integer(-126)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_123(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 125000 > 0) & (b - z**3 + 125000 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(125000)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(125000)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_124(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -125001) & (b - z**3 + 125000 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-125001)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(125000)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_125(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -125001) & (b > -125216) & (c > -217)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-125001)), StrictGreaterThan(Symbol('b'), Integer(-125216)), StrictGreaterThan(Symbol('c'), Integer(-217)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_126(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 132651 > 0) & (b - z**3 + 132651 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(132651)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(132651)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_127(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -132652) & (b - z**3 + 132651 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-132652)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(132651)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_128(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -132652) & (b > -132994) & (c > -344)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-132652)), StrictGreaterThan(Symbol('b'), Integer(-132994)), StrictGreaterThan(Symbol('c'), Integer(-344)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_129(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 140608 > 0) & (b - z**3 + 140608 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(140608)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(140608)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_130(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -140609) & (b - z**3 + 140608 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-140609)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(140608)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_131(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -140609) & (b > -141120) & (c > -513)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-140609)), StrictGreaterThan(Symbol('b'), Integer(-141120)), StrictGreaterThan(Symbol('c'), Integer(-513)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_132(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 148877 > 0) & (b - z**3 + 148877 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(148877)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(148877)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_133(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -148878) & (b - z**3 + 148877 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-148878)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(148877)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_134(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -148878) & (b > -149606) & (c > -730)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-148878)), StrictGreaterThan(Symbol('b'), Integer(-149606)), StrictGreaterThan(Symbol('c'), Integer(-730)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_135(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 157464 > 0) & (b - z**3 + 157464 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(157464)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(157464)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_136(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -157465) & (b - z**3 + 157464 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-157465)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(157464)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_137(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -157465) & (b > -158464) & (c > -1001)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-157465)), StrictGreaterThan(Symbol('b'), Integer(-158464)), StrictGreaterThan(Symbol('c'), Integer(-1001)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_138(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 166375 > 0) & (b - z**3 + 166375 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(166375)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(166375)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_139(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -166376) & (b - z**3 + 166375 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-166376)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(166375)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_140(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -166376) & (b > -167706) & (c > -1332)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-166376)), StrictGreaterThan(Symbol('b'), Integer(-167706)), StrictGreaterThan(Symbol('c'), Integer(-1332)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_141(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 175616 > 0) & (b - z**3 + 175616 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(175616)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(175616)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_142(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -175617) & (b - z**3 + 175616 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-175617)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(175616)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_143(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -175617) & (b > -1404927/8) & (c > -7/8)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-175617)), StrictGreaterThan(Symbol('b'), Rational(-1404927, 8)), StrictGreaterThan(Symbol('c'), Rational(-7, 8)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_144(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 185193 > 0) & (b - z**3 + 185193 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(185193)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(185193)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_145(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -185194) & (b - z**3 + 185193 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-185194)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(185193)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_146(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -185194) & (b > -185409) & (c > -217)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-185194)), StrictGreaterThan(Symbol('b'), Integer(-185409)), StrictGreaterThan(Symbol('c'), Integer(-217)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_147(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 195112 > 0) & (b - z**3 + 195112 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(195112)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(195112)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_148(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -195113) & (b - z**3 + 195112 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-195113)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(195112)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_149(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -195113) & (b > -195841) & (c > -730)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-195113)), StrictGreaterThan(Symbol('b'), Integer(-195841)), StrictGreaterThan(Symbol('c'), Integer(-730)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_150(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 205379 > 0) & (b - z**3 + 205379 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(205379)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(205379)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_151(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -205380) & (b - z**3 + 205379 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-205380)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(205379)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_152(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -205380) & (b > -206379) & (c > -1001)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-205380)), StrictGreaterThan(Symbol('b'), Integer(-206379)), StrictGreaterThan(Symbol('c'), Integer(-1001)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_153(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 216000 > 0) & (b - z**3 + 216000 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(216000)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(216000)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_154(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -216001) & (b - z**3 + 216000 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-216001)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(216000)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_155(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -216001) & (b > -217331) & (c > -1332)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-216001)), StrictGreaterThan(Symbol('b'), Integer(-217331)), StrictGreaterThan(Symbol('c'), Integer(-1332)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_156(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 226981 > 0) & (b - z**3 + 226981 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(226981)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(226981)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_157(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -226982) & (b - z**3 + 226981 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-226982)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(226981)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_158(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -226982) & (b > -228709) & (c > -1729)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-226982)), StrictGreaterThan(Symbol('b'), Integer(-228709)), StrictGreaterThan(Symbol('c'), Integer(-1729)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_159(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 238328 > 0) & (b - z**3 + 238328 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(238328)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(238328)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_160(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -238329) & (b - z**3 + 238328 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-238329)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(238328)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_161(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -238329) & (b > -238453) & (c > -126)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-238329)), StrictGreaterThan(Symbol('b'), Integer(-238453)), StrictGreaterThan(Symbol('c'), Integer(-126)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_162(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 250047 > 0) & (b - z**3 + 250047 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(250047)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(250047)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_163(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -250048) & (b - z**3 + 250047 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-250048)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(250047)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_164(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -250048) & (b > -250776) & (c > -730)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-250048)), StrictGreaterThan(Symbol('b'), Integer(-250776)), StrictGreaterThan(Symbol('c'), Integer(-730)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_165(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 262144 > 0) & (b - z**3 + 262144 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(262144)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(262144)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_166(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -262145) & (b - z**3 + 262144 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-262145)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(262144)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_167(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -262145) & (b > -263144) & (c > -1001)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-262145)), StrictGreaterThan(Symbol('b'), Integer(-263144)), StrictGreaterThan(Symbol('c'), Integer(-1001)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_168(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 274625 > 0) & (b - z**3 + 274625 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(274625)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(274625)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_169(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -274626) & (b - z**3 + 274625 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-274626)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(274625)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_170(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -274626) & (b > -276353) & (c > -1729)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-274626)), StrictGreaterThan(Symbol('b'), Integer(-276353)), StrictGreaterThan(Symbol('c'), Integer(-1729)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_171(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 287496 > 0) & (b - z**3 + 287496 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(287496)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(287496)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_172(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -287497) & (b - z**3 + 287496 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-287497)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(287496)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_173(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -287497) & (b > -289693) & (c > -2198)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-287497)), StrictGreaterThan(Symbol('b'), Integer(-289693)), StrictGreaterThan(Symbol('c'), Integer(-2198)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_174(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 300763 > 0) & (b - z**3 + 300763 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(300763)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(300763)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_175(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -300764) & (b - z**3 + 300763 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-300764)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(300763)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_176(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -300764) & (b > -303507) & (c > -2745)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-300764)), StrictGreaterThan(Symbol('b'), Integer(-303507)), StrictGreaterThan(Symbol('c'), Integer(-2745)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_177(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 314432 > 0) & (b - z**3 + 314432 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(314432)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(314432)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_178(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -314433) & (b - z**3 + 314432 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-314433)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(314432)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_179(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -314433) & (b > -314775) & (c > -344)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-314433)), StrictGreaterThan(Symbol('b'), Integer(-314775)), StrictGreaterThan(Symbol('c'), Integer(-344)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_180(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 328509 > 0) & (b - z**3 + 328509 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(328509)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(328509)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_181(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -328510) & (b - z**3 + 328509 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-328510)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(328509)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_182(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -328510) & (b > -331253) & (c > -2745)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-328510)), StrictGreaterThan(Symbol('b'), Integer(-331253)), StrictGreaterThan(Symbol('c'), Integer(-2745)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_183(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 343000 > 0) & (b - z**3 + 343000 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(343000)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(343000)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_184(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -343001) & (b - z**3 + 343000 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-343001)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(343000)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_185(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -343001) & (b > -346375) & (c > -3376)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-343001)), StrictGreaterThan(Symbol('b'), Integer(-346375)), StrictGreaterThan(Symbol('c'), Integer(-3376)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_186(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 357911 > 0) & (b - z**3 + 357911 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(357911)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(357911)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_187(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -357912) & (b - z**3 + 357911 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-357912)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(357911)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_188(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -357912) & (b > -357912) & (c > -2)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-357912)), StrictGreaterThan(Symbol('b'), Integer(-357912)), StrictGreaterThan(Symbol('c'), Integer(-2)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_189(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 373248 > 0) & (b - z**3 + 373248 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(373248)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(373248)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_190(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -373249) & (b - z**3 + 373248 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-373249)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(373248)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_191(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -373249) & (b > -374976) & (c > -1729)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-373249)), StrictGreaterThan(Symbol('b'), Integer(-374976)), StrictGreaterThan(Symbol('c'), Integer(-1729)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_192(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 389017 > 0) & (b - z**3 + 389017 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(389017)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(389017)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_193(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -389018) & (b - z**3 + 389017 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-389018)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(389017)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_194(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -389018) & (b > -392392) & (c > -3376)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-389018)), StrictGreaterThan(Symbol('b'), Integer(-392392)), StrictGreaterThan(Symbol('c'), Integer(-3376)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_195(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 405224 > 0) & (b - z**3 + 405224 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(405224)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(405224)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_196(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -405225) & (b - z**3 + 405224 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-405225)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(405224)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_197(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -405225) & (b > -409320) & (c > -4097)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-405225)), StrictGreaterThan(Symbol('b'), Integer(-409320)), StrictGreaterThan(Symbol('c'), Integer(-4097)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_198(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 421875 > 0) & (b - z**3 + 421875 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(421875)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(421875)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_199(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -421876) & (b - z**3 + 421875 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-421876)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(421875)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_200(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -421876) & (b > -3374999/8) & (c > -7/8)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-421876)), StrictGreaterThan(Symbol('b'), Rational(-3374999, 8)), StrictGreaterThan(Symbol('c'), Rational(-7, 8)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_201(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 438976 > 0) & (b - z**3 + 438976 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(438976)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(438976)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_202(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -438977) & (b - z**3 + 438976 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-438977)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(438976)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_203(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -438977) & (b > -441720) & (c > -2745)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-438977)), StrictGreaterThan(Symbol('b'), Integer(-441720)), StrictGreaterThan(Symbol('c'), Integer(-2745)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_204(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 456533 > 0) & (b - z**3 + 456533 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(456533)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(456533)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_205(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -456534) & (b - z**3 + 456533 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-456534)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(456533)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_206(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -456534) & (b > -460629) & (c > -4097)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-456534)), StrictGreaterThan(Symbol('b'), Integer(-460629)), StrictGreaterThan(Symbol('c'), Integer(-4097)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_207(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 474552 > 0) & (b - z**3 + 474552 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(474552)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(474552)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_208(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -474553) & (b - z**3 + 474552 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-474553)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(474552)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_209(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -474553) & (b > -479465) & (c > -4914)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-474553)), StrictGreaterThan(Symbol('b'), Integer(-479465)), StrictGreaterThan(Symbol('c'), Integer(-4914)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_210(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 493039 > 0) & (b - z**3 + 493039 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(493039)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(493039)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_211(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -493040) & (b - z**3 + 493039 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-493040)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(493039)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_212(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -493040) & (b > -493040) & (c > -2)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-493040)), StrictGreaterThan(Symbol('b'), Integer(-493040)), StrictGreaterThan(Symbol('c'), Integer(-2)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_213(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 512000 > 0) & (b - z**3 + 512000 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(512000)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(512000)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_214(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -512001) & (b - z**3 + 512000 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-512001)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(512000)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_215(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -512001) & (b > -516913) & (c > -4914)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-512001)), StrictGreaterThan(Symbol('b'), Integer(-516913)), StrictGreaterThan(Symbol('c'), Integer(-4914)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_216(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 531441 > 0) & (b - z**3 + 531441 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(531441)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(531441)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_217(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -531442) & (b - z**3 + 531441 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-531442)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(531441)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_218(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -531442) & (b > -532441) & (c > -1001)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-531442)), StrictGreaterThan(Symbol('b'), Integer(-532441)), StrictGreaterThan(Symbol('c'), Integer(-1001)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_219(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 551368 > 0) & (b - z**3 + 551368 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(551368)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(551368)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_220(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -551369) & (b - z**3 + 551368 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-551369)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(551368)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_221(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -551369) & (b > -556281) & (c > -4914)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-551369)), StrictGreaterThan(Symbol('b'), Integer(-556281)), StrictGreaterThan(Symbol('c'), Integer(-4914)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_222(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 571787 > 0) & (b - z**3 + 571787 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(571787)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(571787)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_223(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -571788) & (b - z**3 + 571787 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-571788)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(571787)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_224(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -571788) & (b > -577619) & (c > -5833)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-571788)), StrictGreaterThan(Symbol('b'), Integer(-577619)), StrictGreaterThan(Symbol('c'), Integer(-5833)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_225(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 592704 > 0) & (b - z**3 + 592704 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(592704)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(592704)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_226(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -592705) & (b - z**3 + 592704 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-592705)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(592704)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_227(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -592705) & (b > -4741631/8) & (c > -7/8)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-592705)), StrictGreaterThan(Symbol('b'), Rational(-4741631, 8)), StrictGreaterThan(Symbol('c'), Rational(-7, 8)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_228(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 614125 > 0) & (b - z**3 + 614125 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(614125)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(614125)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_229(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -614126) & (b - z**3 + 614125 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-614126)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(614125)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_230(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -614126) & (b > -614637) & (c > -513)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-614126)), StrictGreaterThan(Symbol('b'), Integer(-614637)), StrictGreaterThan(Symbol('c'), Integer(-513)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_231(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 636056 > 0) & (b - z**3 + 636056 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(636056)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(636056)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_232(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -636057) & (b - z**3 + 636056 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-636057)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(636056)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_233(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -636057) & (b > -640969) & (c > -4914)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-636057)), StrictGreaterThan(Symbol('b'), Integer(-640969)), StrictGreaterThan(Symbol('c'), Integer(-4914)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_234(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 658503 > 0) & (b - z**3 + 658503 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(658503)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(658503)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_235(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -658504) & (b - z**3 + 658503 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-658504)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(658503)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_236(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -658504) & (b > -664335) & (c > -5833)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-658504)), StrictGreaterThan(Symbol('b'), Integer(-664335)), StrictGreaterThan(Symbol('c'), Integer(-5833)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_237(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 681472 > 0) & (b - z**3 + 681472 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(681472)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(681472)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_238(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -681473) & (b - z**3 + 681472 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-681473)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(681472)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_239(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -681473) & (b > -688331) & (c > -6860)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-681473)), StrictGreaterThan(Symbol('b'), Integer(-688331)), StrictGreaterThan(Symbol('c'), Integer(-6860)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_240(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 704969 > 0) & (b - z**3 + 704969 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(704969)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(704969)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_241(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -704970) & (b - z**3 + 704969 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-704970)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(704969)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_242(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -704970) & (b > -712969) & (c > -8001)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-704970)), StrictGreaterThan(Symbol('b'), Integer(-712969)), StrictGreaterThan(Symbol('c'), Integer(-8001)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_243(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 729000 > 0) & (b - z**3 + 729000 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(729000)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(729000)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_244(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -729001) & (b - z**3 + 729000 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-729001)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(729000)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_245(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -729001) & (b > -738261) & (c > -9262)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-729001)), StrictGreaterThan(Symbol('b'), Integer(-738261)), StrictGreaterThan(Symbol('c'), Integer(-9262)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_246(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 753571 > 0) & (b - z**3 + 753571 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(753571)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(753571)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_247(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -753572) & (b - z**3 + 753571 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-753572)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(753571)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_248(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -753572) & (b > -764219) & (c > -10649)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-753572)), StrictGreaterThan(Symbol('b'), Integer(-764219)), StrictGreaterThan(Symbol('c'), Integer(-10649)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_249(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 778688 > 0) & (b - z**3 + 778688 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(778688)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(778688)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_250(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -778689) & (b - z**3 + 778688 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-778689)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(778688)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_251(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -778689) & (b > -790855) & (c > -12168)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-778689)), StrictGreaterThan(Symbol('b'), Integer(-790855)), StrictGreaterThan(Symbol('c'), Integer(-12168)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_252(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 804357 > 0) & (b - z**3 + 804357 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(804357)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(804357)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_253(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -804358) & (b - z**3 + 804357 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-804358)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(804357)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_254(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -804358) & (b > -818181) & (c > -13825)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-804358)), StrictGreaterThan(Symbol('b'), Integer(-818181)), StrictGreaterThan(Symbol('c'), Integer(-13825)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_255(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 830584 > 0) & (b - z**3 + 830584 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(830584)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(830584)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_256(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -830585) & (b - z**3 + 830584 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-830585)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(830584)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_257(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -830585) & (b > -846209) & (c > -15626)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-830585)), StrictGreaterThan(Symbol('b'), Integer(-846209)), StrictGreaterThan(Symbol('c'), Integer(-15626)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_258(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 857375 > 0) & (b - z**3 + 857375 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(857375)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(857375)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_259(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -857376) & (b - z**3 + 857375 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-857376)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(857375)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_260(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -857376) & (b > -874951) & (c > -17577)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-857376)), StrictGreaterThan(Symbol('b'), Integer(-874951)), StrictGreaterThan(Symbol('c'), Integer(-17577)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_261(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 884736 > 0) & (b - z**3 + 884736 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(884736)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(884736)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_262(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -884737) & (b - z**3 + 884736 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-884737)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(884736)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_263(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -884737) & (b > -904419) & (c > -19684)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-884737)), StrictGreaterThan(Symbol('b'), Integer(-904419)), StrictGreaterThan(Symbol('c'), Integer(-19684)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_264(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 912673 > 0) & (b - z**3 + 912673 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(912673)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(912673)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_265(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -912674) & (b - z**3 + 912673 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-912674)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(912673)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_266(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -912674) & (b > -934625) & (c > -21953)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-912674)), StrictGreaterThan(Symbol('b'), Integer(-934625)), StrictGreaterThan(Symbol('c'), Integer(-21953)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_267(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 941192 > 0) & (b - z**3 + 941192 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(941192)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(941192)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_268(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -941193) & (b - z**3 + 941192 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-941193)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(941192)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_269(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -941193) & (b > -958768) & (c > -17577)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-941193)), StrictGreaterThan(Symbol('b'), Integer(-958768)), StrictGreaterThan(Symbol('c'), Integer(-17577)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_270(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 970299 > 0) & (b - z**3 + 970299 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(970299)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(970299)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_271(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -970300) & (b - z**3 + 970299 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-970300)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(970299)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_272(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -970300) & (b > -992251) & (c > -21953)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-970300)), StrictGreaterThan(Symbol('b'), Integer(-992251)), StrictGreaterThan(Symbol('c'), Integer(-21953)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_273(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 1000000 > 0) & (b - z**3 + 1000000 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(1000000)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1000000)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_274(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -1000001) & (b - z**3 + 1000000 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-1000001)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1000000)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_275(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -1000001) & (b > -1024389) & (c > -24390)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-1000001)), StrictGreaterThan(Symbol('b'), Integer(-1024389)), StrictGreaterThan(Symbol('c'), Integer(-24390)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_276(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 1030301 > 0) & (b - z**3 + 1030301 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(1030301)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1030301)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_277(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -1030302) & (b - z**3 + 1030301 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-1030302)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1030301)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_278(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -1030302) & (b > -1057301) & (c > -27001)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-1030302)), StrictGreaterThan(Symbol('b'), Integer(-1057301)), StrictGreaterThan(Symbol('c'), Integer(-27001)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_279(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 1061208 > 0) & (b - z**3 + 1061208 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(1061208)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1061208)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_280(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -1061209) & (b - z**3 + 1061208 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-1061209)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1061208)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_281(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -1061209) & (b > -1090999) & (c > -29792)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-1061209)), StrictGreaterThan(Symbol('b'), Integer(-1090999)), StrictGreaterThan(Symbol('c'), Integer(-29792)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_282(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 1092727 > 0) & (b - z**3 + 1092727 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(1092727)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1092727)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_283(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -1092728) & (b - z**3 + 1092727 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-1092728)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1092727)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_284(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -1092728) & (b > -1099586) & (c > -6860)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-1092728)), StrictGreaterThan(Symbol('b'), Integer(-1099586)), StrictGreaterThan(Symbol('c'), Integer(-6860)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_285(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 1124864 > 0) & (b - z**3 + 1124864 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(1124864)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1124864)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_286(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -1124865) & (b - z**3 + 1124864 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-1124865)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1124864)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_287(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -1124865) & (b > -1154655) & (c > -29792)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-1124865)), StrictGreaterThan(Symbol('b'), Integer(-1154655)), StrictGreaterThan(Symbol('c'), Integer(-29792)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_288(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 1157625 > 0) & (b - z**3 + 1157625 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(1157625)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1157625)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_289(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -1157626) & (b - z**3 + 1157625 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-1157626)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1157625)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_290(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -1157626) & (b > -1190393) & (c > -32769)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-1157626)), StrictGreaterThan(Symbol('b'), Integer(-1190393)), StrictGreaterThan(Symbol('c'), Integer(-32769)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_291(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 1191016 > 0) & (b - z**3 + 1191016 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(1191016)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1191016)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_292(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -1191017) & (b - z**3 + 1191016 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-1191017)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1191016)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_293(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -1191017) & (b > -1191017) & (c > -2)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-1191017)), StrictGreaterThan(Symbol('b'), Integer(-1191017)), StrictGreaterThan(Symbol('c'), Integer(-2)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_294(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 1225043 > 0) & (b - z**3 + 1225043 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(1225043)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1225043)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_295(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -1225044) & (b - z**3 + 1225043 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-1225044)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1225043)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_296(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -1225044) & (b > -1257811) & (c > -32769)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-1225044)), StrictGreaterThan(Symbol('b'), Integer(-1257811)), StrictGreaterThan(Symbol('c'), Integer(-32769)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_297(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 1259712 > 0) & (b - z**3 + 1259712 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(1259712)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1259712)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_298(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -1259713) & (b - z**3 + 1259712 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-1259713)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1259712)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_299(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -1259713) & (b > -1295649) & (c > -35938)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-1259713)), StrictGreaterThan(Symbol('b'), Integer(-1295649)), StrictGreaterThan(Symbol('c'), Integer(-35938)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_300(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 1295029 > 0) & (b - z**3 + 1295029 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(1295029)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1295029)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_301(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -1295030) & (b - z**3 + 1295029 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-1295030)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1295029)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_302(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -1295030) & (b > -1334333) & (c > -39305)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-1295030)), StrictGreaterThan(Symbol('b'), Integer(-1334333)), StrictGreaterThan(Symbol('c'), Integer(-39305)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_303(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 1331000 > 0) & (b - z**3 + 1331000 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(1331000)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1331000)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_304(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -1331001) & (b - z**3 + 1331000 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-1331001)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1331000)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_305(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -1331001) & (b > -1331008) & (c > -9)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-1331001)), StrictGreaterThan(Symbol('b'), Integer(-1331008)), StrictGreaterThan(Symbol('c'), Integer(-9)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_306(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 1367631 > 0) & (b - z**3 + 1367631 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(1367631)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1367631)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_307(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -1367632) & (b - z**3 + 1367631 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-1367632)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1367631)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_308(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -1367632) & (b > -1385207) & (c > -17577)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-1367632)), StrictGreaterThan(Symbol('b'), Integer(-1385207)), StrictGreaterThan(Symbol('c'), Integer(-17577)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_309(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 1404928 > 0) & (b - z**3 + 1404928 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(1404928)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1404928)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_310(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -1404929) & (b - z**3 + 1404928 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-1404929)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1404928)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_311(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -1404929) & (b > -1440865) & (c > -35938)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-1404929)), StrictGreaterThan(Symbol('b'), Integer(-1440865)), StrictGreaterThan(Symbol('c'), Integer(-35938)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_312(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 1442897 > 0) & (b - z**3 + 1442897 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(1442897)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1442897)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_313(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -1442898) & (b - z**3 + 1442897 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-1442898)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1442897)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_314(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -1442898) & (b > -1482201) & (c > -39305)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-1442898)), StrictGreaterThan(Symbol('b'), Integer(-1482201)), StrictGreaterThan(Symbol('c'), Integer(-39305)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_315(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 1481544 > 0) & (b - z**3 + 1481544 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(1481544)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1481544)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_316(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -1481545) & (b - z**3 + 1481544 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-1481545)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1481544)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_317(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -1481545) & (b > -11852351/8) & (c > -7/8)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-1481545)), StrictGreaterThan(Symbol('b'), Rational(-11852351, 8)), StrictGreaterThan(Symbol('c'), Rational(-7, 8)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_318(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 1520875 > 0) & (b - z**3 + 1520875 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(1520875)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1520875)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_319(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -1520876) & (b - z**3 + 1520875 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-1520876)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1520875)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_320(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -1520876) & (b > -1520876) & (c > -2)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-1520876)), StrictGreaterThan(Symbol('b'), Integer(-1520876)), StrictGreaterThan(Symbol('c'), Integer(-2)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_321(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 1560896 > 0) & (b - z**3 + 1560896 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(1560896)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1560896)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_322(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -1560897) & (b - z**3 + 1560896 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-1560897)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1560896)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_323(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -1560897) & (b > -1600200) & (c > -39305)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-1560897)), StrictGreaterThan(Symbol('b'), Integer(-1600200)), StrictGreaterThan(Symbol('c'), Integer(-39305)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_324(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 1601613 > 0) & (b - z**3 + 1601613 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(1601613)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1601613)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_325(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -1601614) & (b - z**3 + 1601613 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-1601614)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1601613)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_326(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -1601614) & (b > -1640917) & (c > -39305)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-1601614)), StrictGreaterThan(Symbol('b'), Integer(-1640917)), StrictGreaterThan(Symbol('c'), Integer(-39305)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_327(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 1643032 > 0) & (b - z**3 + 1643032 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(1643032)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1643032)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_328(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -1643033) & (b - z**3 + 1643032 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-1643033)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1643032)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_329(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -1643033) & (b > -1685907) & (c > -42876)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-1643033)), StrictGreaterThan(Symbol('b'), Integer(-1685907)), StrictGreaterThan(Symbol('c'), Integer(-42876)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_330(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 1685159 > 0) & (b - z**3 + 1685159 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(1685159)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1685159)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_331(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -1685160) & (b - z**3 + 1685159 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-1685160)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1685159)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_332(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -1685160) & (b > -13481271/8) & (c > -7/8)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-1685160)), StrictGreaterThan(Symbol('b'), Rational(-13481271, 8)), StrictGreaterThan(Symbol('c'), Rational(-7, 8)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_333(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 1728000 > 0) & (b - z**3 + 1728000 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(1728000)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1728000)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_334(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -1728001) & (b - z**3 + 1728000 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-1728001)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1728000)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_335(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -1728001) & (b > -1770875) & (c > -42876)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-1728001)), StrictGreaterThan(Symbol('b'), Integer(-1770875)), StrictGreaterThan(Symbol('c'), Integer(-42876)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_336(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 1771561 > 0) & (b - z**3 + 1771561 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(1771561)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1771561)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_337(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -1771562) & (b - z**3 + 1771561 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-1771562)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1771561)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_338(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -1771562) & (b > -1771562) & (c > -2)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-1771562)), StrictGreaterThan(Symbol('b'), Integer(-1771562)), StrictGreaterThan(Symbol('c'), Integer(-2)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_339(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 1815848 > 0) & (b - z**3 + 1815848 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(1815848)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1815848)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_340(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -1815849) & (b - z**3 + 1815848 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-1815849)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1815848)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_341(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -1815849) & (b > -1815856) & (c > -9)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-1815849)), StrictGreaterThan(Symbol('b'), Integer(-1815856)), StrictGreaterThan(Symbol('c'), Integer(-9)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_342(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 1860867 > 0) & (b - z**3 + 1860867 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(1860867)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1860867)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_343(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -1860868) & (b - z**3 + 1860867 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-1860868)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1860867)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_344(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -1860868) & (b > -1860894) & (c > -28)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-1860868)), StrictGreaterThan(Symbol('b'), Integer(-1860894)), StrictGreaterThan(Symbol('c'), Integer(-28)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_345(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 1906624 > 0) & (b - z**3 + 1906624 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(1906624)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1906624)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_346(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -1906625) & (b - z**3 + 1906624 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-1906625)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1906624)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_347(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -1906625) & (b > -1906688) & (c > -65)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-1906625)), StrictGreaterThan(Symbol('b'), Integer(-1906688)), StrictGreaterThan(Symbol('c'), Integer(-65)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_348(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 1953125 > 0) & (b - z**3 + 1953125 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(1953125)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1953125)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_349(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -1953126) & (b - z**3 + 1953125 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-1953126)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1953125)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_350(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -1953126) & (b > -1953250) & (c > -126)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-1953126)), StrictGreaterThan(Symbol('b'), Integer(-1953250)), StrictGreaterThan(Symbol('c'), Integer(-126)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_351(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 2000376 > 0) & (b - z**3 + 2000376 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(2000376)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(2000376)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_352(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -2000377) & (b - z**3 + 2000376 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-2000377)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(2000376)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_353(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -2000377) & (b > -2000592) & (c > -217)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-2000377)), StrictGreaterThan(Symbol('b'), Integer(-2000592)), StrictGreaterThan(Symbol('c'), Integer(-217)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_354(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 2048383 > 0) & (b - z**3 + 2048383 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(2048383)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(2048383)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_355(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -2048384) & (b - z**3 + 2048383 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-2048384)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(2048383)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_356(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -2048384) & (b > -2048726) & (c > -344)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-2048384)), StrictGreaterThan(Symbol('b'), Integer(-2048726)), StrictGreaterThan(Symbol('c'), Integer(-344)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_357(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 2097152 > 0) & (b - z**3 + 2097152 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(2097152)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(2097152)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_358(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -2097153) & (b - z**3 + 2097152 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-2097153)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(2097152)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_359(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -2097153) & (b > -2140027) & (c > -42876)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-2097153)), StrictGreaterThan(Symbol('b'), Integer(-2140027)), StrictGreaterThan(Symbol('c'), Integer(-42876)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_360(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 2146689 > 0) & (b - z**3 + 2146689 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(2146689)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(2146689)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_361(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -2146690) & (b - z**3 + 2146689 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-2146690)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(2146689)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_362(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -2146690) & (b > -2189564) & (c > -42876)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-2146690)), StrictGreaterThan(Symbol('b'), Integer(-2189564)), StrictGreaterThan(Symbol('c'), Integer(-42876)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_363(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 2197000 > 0) & (b - z**3 + 2197000 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(2197000)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(2197000)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_364(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -2197001) & (b - z**3 + 2197000 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-2197001)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(2197000)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_365(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -2197001) & (b > -2243656) & (c > -46657)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-2197001)), StrictGreaterThan(Symbol('b'), Integer(-2243656)), StrictGreaterThan(Symbol('c'), Integer(-46657)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_366(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 2248091 > 0) & (b - z**3 + 2248091 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(2248091)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(2248091)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_367(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -2248092) & (b - z**3 + 2248091 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-2248092)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(2248091)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_368(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -2248092) & (b > -2287395) & (c > -39305)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-2248092)), StrictGreaterThan(Symbol('b'), Integer(-2287395)), StrictGreaterThan(Symbol('c'), Integer(-39305)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_369(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 2299968 > 0) & (b - z**3 + 2299968 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(2299968)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(2299968)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_370(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -2299969) & (b - z**3 + 2299968 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-2299969)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(2299968)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_371(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -2299969) & (b > -2346624) & (c > -46657)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-2299969)), StrictGreaterThan(Symbol('b'), Integer(-2346624)), StrictGreaterThan(Symbol('c'), Integer(-46657)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_372(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 2352637 > 0) & (b - z**3 + 2352637 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(2352637)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(2352637)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_373(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -2352638) & (b - z**3 + 2352637 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-2352638)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(2352637)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_374(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -2352638) & (b > -2403290) & (c > -50654)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-2352638)), StrictGreaterThan(Symbol('b'), Integer(-2403290)), StrictGreaterThan(Symbol('c'), Integer(-50654)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_375(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 2406104 > 0) & (b - z**3 + 2406104 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(2406104)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(2406104)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_376(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -2406105) & (b - z**3 + 2406104 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-2406105)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(2406104)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_377(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -2406105) & (b > -2456757) & (c > -50654)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-2406105)), StrictGreaterThan(Symbol('b'), Integer(-2456757)), StrictGreaterThan(Symbol('c'), Integer(-50654)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_378(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 2460375 > 0) & (b - z**3 + 2460375 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(2460375)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(2460375)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_379(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -2460376) & (b - z**3 + 2460375 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-2460376)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(2460375)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_380(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -2460376) & (b > -2515247) & (c > -54873)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-2460376)), StrictGreaterThan(Symbol('b'), Integer(-2515247)), StrictGreaterThan(Symbol('c'), Integer(-54873)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_381(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 2515456 > 0) & (b - z**3 + 2515456 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(2515456)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(2515456)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_382(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -2515457) & (b - z**3 + 2515456 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-2515457)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(2515456)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_383(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -2515457) & (b > -2515968) & (c > -513)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-2515457)), StrictGreaterThan(Symbol('b'), Integer(-2515968)), StrictGreaterThan(Symbol('c'), Integer(-513)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_384(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 2571353 > 0) & (b - z**3 + 2571353 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(2571353)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(2571353)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_385(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -2571354) & (b - z**3 + 2571353 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-2571354)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(2571353)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_386(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -2571354) & (b > -2626225) & (c > -54873)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-2571354)), StrictGreaterThan(Symbol('b'), Integer(-2626225)), StrictGreaterThan(Symbol('c'), Integer(-54873)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_387(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 2628072 > 0) & (b - z**3 + 2628072 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(2628072)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(2628072)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_388(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -2628073) & (b - z**3 + 2628072 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-2628073)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(2628072)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_389(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -2628073) & (b > -2687391) & (c > -59320)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-2628073)), StrictGreaterThan(Symbol('b'), Integer(-2687391)), StrictGreaterThan(Symbol('c'), Integer(-59320)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_390(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 2685619 > 0) & (b - z**3 + 2685619 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(2685619)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(2685619)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_391(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -2685620) & (b - z**3 + 2685619 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-2685620)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(2685619)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_392(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -2685620) & (b > -2749619) & (c > -64001)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-2685620)), StrictGreaterThan(Symbol('b'), Integer(-2749619)), StrictGreaterThan(Symbol('c'), Integer(-64001)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_393(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 2744000 > 0) & (b - z**3 + 2744000 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(2744000)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(2744000)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_394(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -2744001) & (b - z**3 + 2744000 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-2744001)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(2744000)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_395(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -2744001) & (b > -2812921) & (c > -68922)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-2744001)), StrictGreaterThan(Symbol('b'), Integer(-2812921)), StrictGreaterThan(Symbol('c'), Integer(-68922)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_396(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 2803221 > 0) & (b - z**3 + 2803221 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(2803221)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(2803221)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_397(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -2803222) & (b - z**3 + 2803221 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-2803222)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(2803221)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_398(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -2803222) & (b > -2877309) & (c > -74089)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-2803222)), StrictGreaterThan(Symbol('b'), Integer(-2877309)), StrictGreaterThan(Symbol('c'), Integer(-74089)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_399(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 2863288 > 0) & (b - z**3 + 2863288 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(2863288)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(2863288)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_400(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -2863289) & (b - z**3 + 2863288 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-2863289)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(2863288)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_401(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -2863289) & (b > -2864017) & (c > -730)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-2863289)), StrictGreaterThan(Symbol('b'), Integer(-2864017)), StrictGreaterThan(Symbol('c'), Integer(-730)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_402(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 2924207 > 0) & (b - z**3 + 2924207 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(2924207)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(2924207)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_403(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -2924208) & (b - z**3 + 2924207 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-2924208)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(2924207)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_404(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -2924208) & (b > -2925207) & (c > -1001)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-2924208)), StrictGreaterThan(Symbol('b'), Integer(-2925207)), StrictGreaterThan(Symbol('c'), Integer(-1001)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_405(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 2985984 > 0) & (b - z**3 + 2985984 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(2985984)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(2985984)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_406(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -2985985) & (b - z**3 + 2985984 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-2985985)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(2985984)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_407(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -2985985) & (b > -3060072) & (c > -74089)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-2985985)), StrictGreaterThan(Symbol('b'), Integer(-3060072)), StrictGreaterThan(Symbol('c'), Integer(-74089)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_408(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 3048625 > 0) & (b - z**3 + 3048625 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(3048625)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(3048625)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_409(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -3048626) & (b - z**3 + 3048625 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-3048626)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(3048625)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_410(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -3048626) & (b > -24388999/8) & (c > -7/8)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-3048626)), StrictGreaterThan(Symbol('b'), Rational(-24388999, 8)), StrictGreaterThan(Symbol('c'), Rational(-7, 8)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_411(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 3112136 > 0) & (b - z**3 + 3112136 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(3112136)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(3112136)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_412(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -3112137) & (b - z**3 + 3112136 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-3112137)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(3112136)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_413(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -3112137) & (b > -3113467) & (c > -1332)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-3112137)), StrictGreaterThan(Symbol('b'), Integer(-3113467)), StrictGreaterThan(Symbol('c'), Integer(-1332)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_414(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 3176523 > 0) & (b - z**3 + 3176523 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(3176523)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(3176523)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_415(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -3176524) & (b - z**3 + 3176523 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-3176524)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(3176523)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_416(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -3176524) & (b > -3250611) & (c > -74089)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-3176524)), StrictGreaterThan(Symbol('b'), Integer(-3250611)), StrictGreaterThan(Symbol('c'), Integer(-74089)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_417(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 3241792 > 0) & (b - z**3 + 3241792 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(3241792)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(3241792)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_418(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -3241793) & (b - z**3 + 3241792 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-3241793)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(3241792)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_419(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -3241793) & (b > -3321299) & (c > -79508)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-3241793)), StrictGreaterThan(Symbol('b'), Integer(-3321299)), StrictGreaterThan(Symbol('c'), Integer(-79508)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_420(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 3307949 > 0) & (b - z**3 + 3307949 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(3307949)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(3307949)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_421(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -3307950) & (b - z**3 + 3307949 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-3307950)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(3307949)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_422(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -3307950) & (b > -3393133) & (c > -85185)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-3307950)), StrictGreaterThan(Symbol('b'), Integer(-3393133)), StrictGreaterThan(Symbol('c'), Integer(-85185)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_423(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 3375000 > 0) & (b - z**3 + 3375000 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(3375000)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(3375000)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_424(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -3375001) & (b - z**3 + 3375000 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-3375001)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(3375000)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_425(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -3375001) & (b > -3466125) & (c > -91126)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-3375001)), StrictGreaterThan(Symbol('b'), Integer(-3466125)), StrictGreaterThan(Symbol('c'), Integer(-91126)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_426(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 3442951 > 0) & (b - z**3 + 3442951 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(3442951)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(3442951)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_427(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -3442952) & (b - z**3 + 3442951 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-3442952)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(3442951)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_428(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -3442952) & (b > -3540287) & (c > -97337)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-3442952)), StrictGreaterThan(Symbol('b'), Integer(-3540287)), StrictGreaterThan(Symbol('c'), Integer(-97337)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_429(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 3511808 > 0) & (b - z**3 + 3511808 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(3511808)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(3511808)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_430(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -3511809) & (b - z**3 + 3511808 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-3511809)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(3511808)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_431(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -3511809) & (b > -3615631) & (c > -103824)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-3511809)), StrictGreaterThan(Symbol('b'), Integer(-3615631)), StrictGreaterThan(Symbol('c'), Integer(-103824)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_432(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 3581577 > 0) & (b - z**3 + 3581577 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(3581577)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(3581577)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_433(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -3581578) & (b - z**3 + 3581577 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-3581578)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(3581577)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_434(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -3581578) & (b > -3645577) & (c > -64001)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-3581578)), StrictGreaterThan(Symbol('b'), Integer(-3645577)), StrictGreaterThan(Symbol('c'), Integer(-64001)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_435(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 3652264 > 0) & (b - z**3 + 3652264 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(3652264)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(3652264)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_436(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -3652265) & (b - z**3 + 3652264 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-3652265)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(3652264)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_437(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -3652265) & (b > -3743389) & (c > -91126)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-3652265)), StrictGreaterThan(Symbol('b'), Integer(-3743389)), StrictGreaterThan(Symbol('c'), Integer(-91126)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_438(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 3723875 > 0) & (b - z**3 + 3723875 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(3723875)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(3723875)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_439(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -3723876) & (b - z**3 + 3723875 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-3723876)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(3723875)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_440(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -3723876) & (b > -3821211) & (c > -97337)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-3723876)), StrictGreaterThan(Symbol('b'), Integer(-3821211)), StrictGreaterThan(Symbol('c'), Integer(-97337)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_441(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 3796416 > 0) & (b - z**3 + 3796416 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(3796416)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(3796416)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_442(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -3796417) & (b - z**3 + 3796416 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-3796417)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(3796416)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_443(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -3796417) & (b > -3900239) & (c > -103824)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-3796417)), StrictGreaterThan(Symbol('b'), Integer(-3900239)), StrictGreaterThan(Symbol('c'), Integer(-103824)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_444(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 3869893 > 0) & (b - z**3 + 3869893 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(3869893)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(3869893)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_445(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -3869901) & (b - z**3 + 3869893 > 0) & (c - z**3 + 8 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-3869901)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(3869893)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(8)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_446(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -3869901) & (b > -5967045) & (c > -2097160)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-3869901)), StrictGreaterThan(Symbol('b'), Integer(-5967045)), StrictGreaterThan(Symbol('c'), Integer(-2097160)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_447(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 134217728 > 0) & (b - z**3 + 134217728 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(134217728)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(134217728)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_448(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -134217729) & (b - z**3 + 134217728 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-134217729)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(134217728)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_449(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -134217729) & (b > -134217853) & (c > -126)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-134217729)), StrictGreaterThan(Symbol('b'), Integer(-134217853)), StrictGreaterThan(Symbol('c'), Integer(-126)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_450(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 135005697 > 0) & (b - z**3 + 135005697 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(135005697)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(135005697)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_451(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -135005698) & (b - z**3 + 135005697 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-135005698)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(135005697)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_452(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -135005698) & (b > -135085204) & (c > -79508)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-135005698)), StrictGreaterThan(Symbol('b'), Integer(-135085204)), StrictGreaterThan(Symbol('c'), Integer(-79508)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_453(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 135796744 > 0) & (b - z**3 + 135796744 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(135796744)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(135796744)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_454(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -135796745) & (b - z**3 + 135796744 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-135796745)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(135796744)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_455(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -135796745) & (b > -135881928) & (c > -85185)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-135796745)), StrictGreaterThan(Symbol('b'), Integer(-135881928)), StrictGreaterThan(Symbol('c'), Integer(-85185)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_456(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 136590875 > 0) & (b - z**3 + 136590875 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(136590875)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(136590875)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_457(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -136590876) & (b - z**3 + 136590875 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-136590876)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(136590875)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_458(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -136590876) & (b > -136701467) & (c > -110593)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-136590876)), StrictGreaterThan(Symbol('b'), Integer(-136701467)), StrictGreaterThan(Symbol('c'), Integer(-110593)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_459(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 137388096 > 0) & (b - z**3 + 137388096 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(137388096)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(137388096)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_460(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -137388097) & (b - z**3 + 137388096 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-137388097)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(137388096)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_461(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -137388097) & (b > -137505745) & (c > -117650)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-137388097)), StrictGreaterThan(Symbol('b'), Integer(-137505745)), StrictGreaterThan(Symbol('c'), Integer(-117650)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_462(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 138188413 > 0) & (b - z**3 + 138188413 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(138188413)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(138188413)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_463(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -138188414) & (b - z**3 + 138188413 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-138188414)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(138188413)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_464(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -138188414) & (b > -138279538) & (c > -91126)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-138188414)), StrictGreaterThan(Symbol('b'), Integer(-138279538)), StrictGreaterThan(Symbol('c'), Integer(-91126)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_465(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 138991832 > 0) & (b - z**3 + 138991832 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(138991832)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(138991832)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_466(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -138991833) & (b - z**3 + 138991832 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-138991833)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(138991832)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_467(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -138991833) & (b > -139089168) & (c > -97337)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-138991833)), StrictGreaterThan(Symbol('b'), Integer(-139089168)), StrictGreaterThan(Symbol('c'), Integer(-97337)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_468(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 139798359 > 0) & (b - z**3 + 139798359 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(139798359)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(139798359)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_469(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -139798360) & (b - z**3 + 139798359 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-139798360)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(139798359)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_470(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -139798360) & (b > -139902182) & (c > -103824)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-139798360)), StrictGreaterThan(Symbol('b'), Integer(-139902182)), StrictGreaterThan(Symbol('c'), Integer(-103824)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_471(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 140608000 > 0) & (b - z**3 + 140608000 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(140608000)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(140608000)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_472(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -140608001) & (b - z**3 + 140608000 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-140608001)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(140608000)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_473(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -140608001) & (b > -140718592) & (c > -110593)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-140608001)), StrictGreaterThan(Symbol('b'), Integer(-140718592)), StrictGreaterThan(Symbol('c'), Integer(-110593)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_474(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 141420761 > 0) & (b - z**3 + 141420761 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(141420761)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(141420761)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_475(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -141420762) & (b - z**3 + 141420761 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-141420762)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(141420761)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_476(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -141420762) & (b > -141538410) & (c > -117650)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-141420762)), StrictGreaterThan(Symbol('b'), Integer(-141538410)), StrictGreaterThan(Symbol('c'), Integer(-117650)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_477(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 142236648 > 0) & (b - z**3 + 142236648 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(142236648)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(142236648)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_478(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -142236649) & (b - z**3 + 142236648 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-142236649)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(142236648)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_479(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -142236649) & (b > -142361648) & (c > -125001)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-142236649)), StrictGreaterThan(Symbol('b'), Integer(-142361648)), StrictGreaterThan(Symbol('c'), Integer(-125001)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_480(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 143055667 > 0) & (b - z**3 + 143055667 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(143055667)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(143055667)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_481(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -143055668) & (b - z**3 + 143055667 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-143055668)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(143055667)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_482(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -143055668) & (b > -143188318) & (c > -132652)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-143055668)), StrictGreaterThan(Symbol('b'), Integer(-143188318)), StrictGreaterThan(Symbol('c'), Integer(-132652)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_483(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 143877824 > 0) & (b - z**3 + 143877824 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(143877824)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(143877824)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_484(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -143877825) & (b - z**3 + 143877824 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-143877825)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(143877824)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_485(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -143877825) & (b > -144018432) & (c > -140609)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-143877825)), StrictGreaterThan(Symbol('b'), Integer(-144018432)), StrictGreaterThan(Symbol('c'), Integer(-140609)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_486(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 144703125 > 0) & (b - z**3 + 144703125 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(144703125)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(144703125)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_487(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -144703126) & (b - z**3 + 144703125 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-144703126)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(144703125)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_488(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -144703126) & (b > -144852002) & (c > -148878)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-144703126)), StrictGreaterThan(Symbol('b'), Integer(-144852002)), StrictGreaterThan(Symbol('c'), Integer(-148878)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_489(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 145531576 > 0) & (b - z**3 + 145531576 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(145531576)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(145531576)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_490(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -145531577) & (b - z**3 + 145531576 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-145531577)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(145531576)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_491(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -145531577) & (b > -145664227) & (c > -132652)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-145531577)), StrictGreaterThan(Symbol('b'), Integer(-145664227)), StrictGreaterThan(Symbol('c'), Integer(-132652)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_492(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 146363183 > 0) & (b - z**3 + 146363183 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(146363183)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(146363183)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_493(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -146363184) & (b - z**3 + 146363183 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-146363184)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(146363183)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_494(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -146363184) & (b > -146503791) & (c > -140609)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-146363184)), StrictGreaterThan(Symbol('b'), Integer(-146503791)), StrictGreaterThan(Symbol('c'), Integer(-140609)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_495(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 147197952 > 0) & (b - z**3 + 147197952 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(147197952)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(147197952)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_496(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -147197953) & (b - z**3 + 147197952 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-147197953)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(147197952)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_497(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -147197953) & (b > -147346829) & (c > -148878)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-147197953)), StrictGreaterThan(Symbol('b'), Integer(-147346829)), StrictGreaterThan(Symbol('c'), Integer(-148878)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_498(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 148035889 > 0) & (b - z**3 + 148035889 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(148035889)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(148035889)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_499(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -148035890) & (b - z**3 + 148035889 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-148035890)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(148035889)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_500(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -148035890) & (b > -148057841) & (c > -21953)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-148035890)), StrictGreaterThan(Symbol('b'), Integer(-148057841)), StrictGreaterThan(Symbol('c'), Integer(-21953)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_501(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 148877000 > 0) & (b - z**3 + 148877000 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(148877000)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(148877000)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_502(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -148877001) & (b - z**3 + 148877000 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-148877001)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(148877000)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_503(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -148877001) & (b > -148945921) & (c > -68922)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-148877001)), StrictGreaterThan(Symbol('b'), Integer(-148945921)), StrictGreaterThan(Symbol('c'), Integer(-68922)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_504(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 149721291 > 0) & (b - z**3 + 149721291 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(149721291)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(149721291)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_505(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -149721292) & (b - z**3 + 149721291 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-149721292)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(149721291)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_506(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -149721292) & (b > -149806475) & (c > -85185)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-149721292)), StrictGreaterThan(Symbol('b'), Integer(-149806475)), StrictGreaterThan(Symbol('c'), Integer(-85185)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_507(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 150568768 > 0) & (b - z**3 + 150568768 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(150568768)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(150568768)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_508(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -150568769) & (b - z**3 + 150568768 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-150568769)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(150568768)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_509(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -150568769) & (b > -150686417) & (c > -117650)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-150568769)), StrictGreaterThan(Symbol('b'), Integer(-150686417)), StrictGreaterThan(Symbol('c'), Integer(-117650)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_510(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 151419437 > 0) & (b - z**3 + 151419437 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(151419437)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(151419437)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_511(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -151419438) & (b - z**3 + 151419437 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-151419438)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(151419437)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_512(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -151419438) & (b > -151544437) & (c > -125001)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-151419438)), StrictGreaterThan(Symbol('b'), Integer(-151544437)), StrictGreaterThan(Symbol('c'), Integer(-125001)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_513(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 152273304 > 0) & (b - z**3 + 152273304 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(152273304)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(152273304)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_514(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -152273305) & (b - z**3 + 152273304 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-152273305)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(152273304)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_515(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -152273305) & (b > -152422181) & (c > -148878)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-152273305)), StrictGreaterThan(Symbol('b'), Integer(-152422181)), StrictGreaterThan(Symbol('c'), Integer(-148878)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_516(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 153130375 > 0) & (b - z**3 + 153130375 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(153130375)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(153130375)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_517(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -153130376) & (b - z**3 + 153130375 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-153130376)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(153130375)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_518(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -153130376) & (b > -153255375) & (c > -125001)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-153130376)), StrictGreaterThan(Symbol('b'), Integer(-153255375)), StrictGreaterThan(Symbol('c'), Integer(-125001)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_519(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 153990656 > 0) & (b - z**3 + 153990656 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(153990656)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(153990656)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_520(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -153990657) & (b - z**3 + 153990656 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-153990657)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(153990656)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_521(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -153990657) & (b > -154123307) & (c > -132652)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-153990657)), StrictGreaterThan(Symbol('b'), Integer(-154123307)), StrictGreaterThan(Symbol('c'), Integer(-132652)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_522(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 154854153 > 0) & (b - z**3 + 154854153 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(154854153)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(154854153)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_523(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -154854154) & (b - z**3 + 154854153 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-154854154)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(154854153)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_524(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -154854154) & (b > -155003030) & (c > -148878)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-154854154)), StrictGreaterThan(Symbol('b'), Integer(-155003030)), StrictGreaterThan(Symbol('c'), Integer(-148878)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_525(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 155720872 > 0) & (b - z**3 + 155720872 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(155720872)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(155720872)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_526(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -155720873) & (b - z**3 + 155720872 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-155720873)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(155720872)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_527(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -155720873) & (b > -155869749) & (c > -148878)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-155720873)), StrictGreaterThan(Symbol('b'), Integer(-155869749)), StrictGreaterThan(Symbol('c'), Integer(-148878)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_528(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 156590819 > 0) & (b - z**3 + 156590819 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(156590819)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(156590819)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_529(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -156590820) & (b - z**3 + 156590819 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-156590820)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(156590819)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_530(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -156590820) & (b > -156739696) & (c > -148878)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-156590820)), StrictGreaterThan(Symbol('b'), Integer(-156739696)), StrictGreaterThan(Symbol('c'), Integer(-148878)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_531(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 157464000 > 0) & (b - z**3 + 157464000 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(157464000)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(157464000)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_532(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -157464001) & (b - z**3 + 157464000 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-157464001)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(157464000)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_533(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -157464001) & (b > -157621464) & (c > -157465)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-157464001)), StrictGreaterThan(Symbol('b'), Integer(-157621464)), StrictGreaterThan(Symbol('c'), Integer(-157465)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_534(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 158340421 > 0) & (b - z**3 + 158340421 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(158340421)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(158340421)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_535(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -158340422) & (b - z**3 + 158340421 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-158340422)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(158340421)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_536(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -158340422) & (b > -158497885) & (c > -157465)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-158340422)), StrictGreaterThan(Symbol('b'), Integer(-158497885)), StrictGreaterThan(Symbol('c'), Integer(-157465)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_537(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 159220088 > 0) & (b - z**3 + 159220088 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(159220088)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(159220088)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_538(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -159220089) & (b - z**3 + 159220088 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-159220089)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(159220088)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_539(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -159220089) & (b > -159386463) & (c > -166376)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-159220089)), StrictGreaterThan(Symbol('b'), Integer(-159386463)), StrictGreaterThan(Symbol('c'), Integer(-166376)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_540(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 160103007 > 0) & (b - z**3 + 160103007 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(160103007)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(160103007)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_541(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -160103008) & (b - z**3 + 160103007 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-160103008)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(160103007)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_542(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -160103008) & (b > -160278623) & (c > -175617)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-160103008)), StrictGreaterThan(Symbol('b'), Integer(-160278623)), StrictGreaterThan(Symbol('c'), Integer(-175617)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_543(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 160989184 > 0) & (b - z**3 + 160989184 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(160989184)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(160989184)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_544(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -160989185) & (b - z**3 + 160989184 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-160989185)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(160989184)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_545(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -160989185) & (b > -161174377) & (c > -185194)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-160989185)), StrictGreaterThan(Symbol('b'), Integer(-161174377)), StrictGreaterThan(Symbol('c'), Integer(-185194)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_546(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 161878625 > 0) & (b - z**3 + 161878625 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(161878625)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(161878625)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_547(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -161878626) & (b - z**3 + 161878625 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-161878626)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(161878625)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_548(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -161878626) & (b > -162073737) & (c > -195113)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-161878626)), StrictGreaterThan(Symbol('b'), Integer(-162073737)), StrictGreaterThan(Symbol('c'), Integer(-195113)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_549(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 162771336 > 0) & (b - z**3 + 162771336 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(162771336)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(162771336)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_550(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -162771337) & (b - z**3 + 162771336 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-162771337)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(162771336)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_551(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -162771337) & (b > -162976715) & (c > -205380)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-162771337)), StrictGreaterThan(Symbol('b'), Integer(-162976715)), StrictGreaterThan(Symbol('c'), Integer(-205380)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_552(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 163667323 > 0) & (b - z**3 + 163667323 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(163667323)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(163667323)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_553(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -163667324) & (b - z**3 + 163667323 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-163667324)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(163667323)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_554(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -163667324) & (b > -1309338583/8) & (c > -7/8)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-163667324)), StrictGreaterThan(Symbol('b'), Rational(-1309338583, 8)), StrictGreaterThan(Symbol('c'), Rational(-7, 8)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_555(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 164566592 > 0) & (b - z**3 + 164566592 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(164566592)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(164566592)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_556(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -164566593) & (b - z**3 + 164566592 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-164566593)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(164566592)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_557(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -164566593) & (b > -164590981) & (c > -24390)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-164566593)), StrictGreaterThan(Symbol('b'), Integer(-164590981)), StrictGreaterThan(Symbol('c'), Integer(-24390)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_558(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 165469149 > 0) & (b - z**3 + 165469149 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(165469149)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(165469149)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_559(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -165469150) & (b - z**3 + 165469149 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-165469150)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(165469149)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_560(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -165469150) & (b > -165664261) & (c > -195113)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-165469150)), StrictGreaterThan(Symbol('b'), Integer(-165664261)), StrictGreaterThan(Symbol('c'), Integer(-195113)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_561(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 166375000 > 0) & (b - z**3 + 166375000 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(166375000)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(166375000)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_562(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -166375001) & (b - z**3 + 166375000 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-166375001)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(166375000)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_563(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -166375001) & (b > -166580379) & (c > -205380)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-166375001)), StrictGreaterThan(Symbol('b'), Integer(-166580379)), StrictGreaterThan(Symbol('c'), Integer(-205380)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_564(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 167284151 > 0) & (b - z**3 + 167284151 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(167284151)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(167284151)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_565(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -167284152) & (b - z**3 + 167284151 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-167284152)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(167284151)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_566(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -167284152) & (b > -167284152) & (c > -2)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-167284152)), StrictGreaterThan(Symbol('b'), Integer(-167284152)), StrictGreaterThan(Symbol('c'), Integer(-2)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_567(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 168196608 > 0) & (b - z**3 + 168196608 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(168196608)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(168196608)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_568(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -168196609) & (b - z**3 + 168196608 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-168196609)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(168196608)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_569(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -168196609) & (b > -168401987) & (c > -205380)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-168196609)), StrictGreaterThan(Symbol('b'), Integer(-168401987)), StrictGreaterThan(Symbol('c'), Integer(-205380)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_570(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 169112377 > 0) & (b - z**3 + 169112377 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(169112377)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(169112377)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_571(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -169112378) & (b - z**3 + 169112377 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-169112378)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(169112377)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_572(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -169112378) & (b > -169139377) & (c > -27001)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-169112378)), StrictGreaterThan(Symbol('b'), Integer(-169139377)), StrictGreaterThan(Symbol('c'), Integer(-27001)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_573(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 170031464 > 0) & (b - z**3 + 170031464 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(170031464)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(170031464)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_574(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -170031465) & (b - z**3 + 170031464 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-170031465)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(170031464)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_575(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -170031465) & (b > -170236843) & (c > -205380)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-170031465)), StrictGreaterThan(Symbol('b'), Integer(-170236843)), StrictGreaterThan(Symbol('c'), Integer(-205380)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_576(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 170953875 > 0) & (b - z**3 + 170953875 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(170953875)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(170953875)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_577(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -170953876) & (b - z**3 + 170953875 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-170953876)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(170953875)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_578(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -170953876) & (b > -171169875) & (c > -216001)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-170953876)), StrictGreaterThan(Symbol('b'), Integer(-171169875)), StrictGreaterThan(Symbol('c'), Integer(-216001)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_579(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 171879616 > 0) & (b - z**3 + 171879616 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(171879616)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(171879616)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_580(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -171879617) & (b - z**3 + 171879616 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-171879617)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(171879616)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_581(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -171879617) & (b > -172012267) & (c > -132652)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-171879617)), StrictGreaterThan(Symbol('b'), Integer(-172012267)), StrictGreaterThan(Symbol('c'), Integer(-132652)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_582(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 172808693 > 0) & (b - z**3 + 172808693 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(172808693)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(172808693)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_583(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -172808694) & (b - z**3 + 172808693 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-172808694)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(172808693)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_584(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -172808694) & (b > -172993886) & (c > -185194)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-172808694)), StrictGreaterThan(Symbol('b'), Integer(-172993886)), StrictGreaterThan(Symbol('c'), Integer(-185194)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_585(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 173741112 > 0) & (b - z**3 + 173741112 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(173741112)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(173741112)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_586(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -173741113) & (b - z**3 + 173741112 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-173741113)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(173741112)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_587(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -173741113) & (b > -173946491) & (c > -205380)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-173741113)), StrictGreaterThan(Symbol('b'), Integer(-173946491)), StrictGreaterThan(Symbol('c'), Integer(-205380)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_588(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 174676879 > 0) & (b - z**3 + 174676879 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(174676879)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(174676879)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_589(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -174676880) & (b - z**3 + 174676879 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-174676880)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(174676879)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_590(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -174676880) & (b > -174892879) & (c > -216001)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-174676880)), StrictGreaterThan(Symbol('b'), Integer(-174892879)), StrictGreaterThan(Symbol('c'), Integer(-216001)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_591(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 175616000 > 0) & (b - z**3 + 175616000 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(175616000)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(175616000)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_592(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -175616001) & (b - z**3 + 175616000 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-175616001)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(175616000)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_593(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -175616001) & (b > -175842981) & (c > -226982)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-175616001)), StrictGreaterThan(Symbol('b'), Integer(-175842981)), StrictGreaterThan(Symbol('c'), Integer(-226982)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_594(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 176558481 > 0) & (b - z**3 + 176558481 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(176558481)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(176558481)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_595(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -176558482) & (b - z**3 + 176558481 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-176558482)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(176558481)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_596(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -176558482) & (b > -176699089) & (c > -140609)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-176558482)), StrictGreaterThan(Symbol('b'), Integer(-176699089)), StrictGreaterThan(Symbol('c'), Integer(-140609)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_597(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 177504328 > 0) & (b - z**3 + 177504328 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(177504328)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(177504328)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_598(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -177504329) & (b - z**3 + 177504328 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-177504329)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(177504328)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_599(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -177504329) & (b > -177653205) & (c > -148878)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-177504329)), StrictGreaterThan(Symbol('b'), Integer(-177653205)), StrictGreaterThan(Symbol('c'), Integer(-148878)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_600(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 178453547 > 0) & (b - z**3 + 178453547 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(178453547)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(178453547)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_601(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -178453548) & (b - z**3 + 178453547 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-178453548)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(178453547)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_602(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -178453548) & (b > -178648659) & (c > -195113)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-178453548)), StrictGreaterThan(Symbol('b'), Integer(-178648659)), StrictGreaterThan(Symbol('c'), Integer(-195113)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_603(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 179406144 > 0) & (b - z**3 + 179406144 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(179406144)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(179406144)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_604(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -179406145) & (b - z**3 + 179406144 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-179406145)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(179406144)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_605(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -179406145) & (b > -179611523) & (c > -205380)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-179406145)), StrictGreaterThan(Symbol('b'), Integer(-179611523)), StrictGreaterThan(Symbol('c'), Integer(-205380)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_606(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 180362125 > 0) & (b - z**3 + 180362125 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(180362125)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(180362125)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_607(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -180362126) & (b - z**3 + 180362125 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-180362126)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(180362125)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_608(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -180362126) & (b > -180589106) & (c > -226982)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-180362126)), StrictGreaterThan(Symbol('b'), Integer(-180589106)), StrictGreaterThan(Symbol('c'), Integer(-226982)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_609(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 181321496 > 0) & (b - z**3 + 181321496 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(181321496)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(181321496)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_610(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -181321497) & (b - z**3 + 181321496 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-181321497)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(181321496)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_611(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -181321497) & (b > -181559824) & (c > -238329)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-181321497)), StrictGreaterThan(Symbol('b'), Integer(-181559824)), StrictGreaterThan(Symbol('c'), Integer(-238329)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_612(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 182284263 > 0) & (b - z**3 + 182284263 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(182284263)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(182284263)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_613(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -182284264) & (b - z**3 + 182284263 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-182284264)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(182284263)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_614(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -182284264) & (b > -182511244) & (c > -226982)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-182284264)), StrictGreaterThan(Symbol('b'), Integer(-182511244)), StrictGreaterThan(Symbol('c'), Integer(-226982)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_615(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 183250432 > 0) & (b - z**3 + 183250432 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(183250432)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(183250432)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_616(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -183250433) & (b - z**3 + 183250432 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-183250433)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(183250432)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_617(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -183250433) & (b > -183488760) & (c > -238329)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-183250433)), StrictGreaterThan(Symbol('b'), Integer(-183488760)), StrictGreaterThan(Symbol('c'), Integer(-238329)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_618(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 184220009 > 0) & (b - z**3 + 184220009 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(184220009)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(184220009)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_619(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -184220010) & (b - z**3 + 184220009 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-184220010)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(184220009)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_620(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -184220010) & (b > -184470056) & (c > -250048)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-184220010)), StrictGreaterThan(Symbol('b'), Integer(-184470056)), StrictGreaterThan(Symbol('c'), Integer(-250048)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_621(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 185193000 > 0) & (b - z**3 + 185193000 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(185193000)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(185193000)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_622(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -185193001) & (b - z**3 + 185193000 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-185193001)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(185193000)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_623(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -185193001) & (b > -1481543999/8) & (c > -7/8)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-185193001)), StrictGreaterThan(Symbol('b'), Rational(-1481543999, 8)), StrictGreaterThan(Symbol('c'), Rational(-7, 8)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_624(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 186169411 > 0) & (b - z**3 + 186169411 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(186169411)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(186169411)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_625(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -186169412) & (b - z**3 + 186169411 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-186169412)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(186169411)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_626(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -186169412) & (b > -186407739) & (c > -238329)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-186169412)), StrictGreaterThan(Symbol('b'), Integer(-186407739)), StrictGreaterThan(Symbol('c'), Integer(-238329)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_627(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 187149248 > 0) & (b - z**3 + 187149248 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(187149248)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(187149248)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_628(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -187149249) & (b - z**3 + 187149248 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-187149249)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(187149248)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_629(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -187149249) & (b > -187399295) & (c > -250048)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-187149249)), StrictGreaterThan(Symbol('b'), Integer(-187399295)), StrictGreaterThan(Symbol('c'), Integer(-250048)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_630(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 188132517 > 0) & (b - z**3 + 188132517 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(188132517)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(188132517)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_631(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -188132518) & (b - z**3 + 188132517 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-188132518)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(188132517)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_632(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -188132518) & (b > -188394661) & (c > -262145)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-188132518)), StrictGreaterThan(Symbol('b'), Integer(-188394661)), StrictGreaterThan(Symbol('c'), Integer(-262145)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_633(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 189119224 > 0) & (b - z**3 + 189119224 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(189119224)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(189119224)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_634(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -189119225) & (b - z**3 + 189119224 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-189119225)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(189119224)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_635(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -189119225) & (b > -189119225) & (c > -2)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-189119225)), StrictGreaterThan(Symbol('b'), Integer(-189119225)), StrictGreaterThan(Symbol('c'), Integer(-2)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_636(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 190109375 > 0) & (b - z**3 + 190109375 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(190109375)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(190109375)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_637(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -190109376) & (b - z**3 + 190109375 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-190109376)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(190109375)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_638(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -190109376) & (b > -190371519) & (c > -262145)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-190109376)), StrictGreaterThan(Symbol('b'), Integer(-190371519)), StrictGreaterThan(Symbol('c'), Integer(-262145)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_639(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 191102976 > 0) & (b - z**3 + 191102976 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(191102976)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(191102976)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_640(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -191102977) & (b - z**3 + 191102976 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-191102977)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(191102976)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_641(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -191102977) & (b > -191377601) & (c > -274626)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-191102977)), StrictGreaterThan(Symbol('b'), Integer(-191377601)), StrictGreaterThan(Symbol('c'), Integer(-274626)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_642(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 192100033 > 0) & (b - z**3 + 192100033 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(192100033)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(192100033)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_643(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -192100034) & (b - z**3 + 192100033 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-192100034)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(192100033)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_644(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -192100034) & (b > -192100041) & (c > -9)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-192100034)), StrictGreaterThan(Symbol('b'), Integer(-192100041)), StrictGreaterThan(Symbol('c'), Integer(-9)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_645(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 193100552 > 0) & (b - z**3 + 193100552 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(193100552)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(193100552)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_646(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -193100553) & (b - z**3 + 193100552 > 0) & (c - z**3 + 1 > 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-193100553)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(193100552)), Integer(0)), StrictGreaterThan(Add(Symbol('c'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_647(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a > -193100553) & (b > -193375177) & (c > -274626)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(-193100553)), StrictGreaterThan(Symbol('b'), Integer(-193375177)), StrictGreaterThan(Symbol('c'), Integer(-274626)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_648(a:sympy.Rational,b:sympy.Rational,c:sympy.Rational):
	#(a - y**3 + 194104539 > 0) & (b - z**3 + 194104539 > 0) & (-c + y**3 + z**3 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Integer(194104539)), Integer(0)), StrictGreaterThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(3))), Integer(194104539)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b, 'c':c })

	if eval==True:
		assert eval!=False
		return True
	return False


def post_condition(a:sympy.Rational, b:sympy.Rational, c:sympy.Rational, x:sympy.Rational, y:sympy.Rational, z:sympy.Rational):
	# (0 > -a + x**3 + y**3) & (0 > -b + x**3 + z**3) & (0 > -c + y**3 + z**3)

	post_cond =  And(StrictGreaterThan(Integer(0), Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('x'), Integer(3)), Pow(Symbol('y'), Integer(3)))), StrictGreaterThan(Integer(0), Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('x'), Integer(3)), Pow(Symbol('z'), Integer(3)))), StrictGreaterThan(Integer(0), Add(Mul(Integer(-1), Symbol('c')), Pow(Symbol('y'), Integer(3)), Pow(Symbol('z'), Integer(3)))))

	eval = post_cond.subs( { 'a':a, 'b':b, 'c':c, 'x':x, 'y':y, 'z':z })

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
	
	
	ip_0=int(input("enter integer numerator of c:\n"))
	ip_1=int(input("enter integer denominator of c:\n"))
	assert(ip_1!=0), ("Error denominator entered is 0")
	c=sympy.Rational(ip_0,ip_1)
	
	
	
	
	if pre_condition_0(a=a,b=b,c=c)==True:
		print("pre_condition_0 SAT")
		print('x = 0')
		print('y = 0')
		print('a = 1')
		print('z = 0')
		print('b = 1')
		print('c = 1')
		exit(0)
	
	
	if pre_condition_1(a=a,b=b,c=c)==True:
		print("pre_condition_1 SAT")
		print('x = 0')
		print('y = 0')
		print('a = 1')
		print('z = 0')
		print('b = 1')
		print('c = 1')
		exit(0)
	
	
	if pre_condition_2(a=a,b=b,c=c)==True:
		print("pre_condition_2 SAT")
		print('x = 0')
		print('y = 0')
		print('a = 1')
		print('z = 0')
		print('b = 1')
		print('c = 1')
		exit(0)
	
	
	if pre_condition_3(a=a,b=b,c=c)==True:
		print("pre_condition_3 SAT")
		print('x = -1')
		print('y = 0')
		print('a = 0')
		print('z = 0')
		print('b = 0')
		print('c = 1')
		exit(0)
	
	
	if pre_condition_4(a=a,b=b,c=c)==True:
		print("pre_condition_4 SAT")
		print('x = -1')
		print('y = 0')
		print('a = 0')
		print('z = 0')
		print('b = 0')
		print('c = 1')
		exit(0)
	
	
	if pre_condition_5(a=a,b=b,c=c)==True:
		print("pre_condition_5 SAT")
		print('x = -1')
		print('y = 0')
		print('a = 0')
		print('z = 0')
		print('b = 0')
		print('c = 1')
		exit(0)
	
	
	if pre_condition_6(a=a,b=b,c=c)==True:
		print("pre_condition_6 SAT")
		print('x = -2')
		print('y = -1')
		print('a = -8')
		print('z = -1/2')
		print('b = -7')
		print('c = -1')
		exit(0)
	
	
	if pre_condition_7(a=a,b=b,c=c)==True:
		print("pre_condition_7 SAT")
		print('x = -2')
		print('y = -1')
		print('a = -8')
		print('z = -1/2')
		print('b = -7')
		print('c = -1')
		exit(0)
	
	
	if pre_condition_8(a=a,b=b,c=c)==True:
		print("pre_condition_8 SAT")
		print('x = -2')
		print('y = -1')
		print('a = -8')
		print('z = -1/2')
		print('b = -7')
		print('c = -1')
		exit(0)
	
	
	if pre_condition_9(a=a,b=b,c=c)==True:
		print("pre_condition_9 SAT")
		print('x = -3')
		print('y = -2')
		print('a = -17')
		print('z = 1')
		print('b = -25')
		print('c = -6')
		exit(0)
	
	
	if pre_condition_10(a=a,b=b,c=c)==True:
		print("pre_condition_10 SAT")
		print('x = -3')
		print('y = -2')
		print('a = -17')
		print('z = 1')
		print('b = -25')
		print('c = -6')
		exit(0)
	
	
	if pre_condition_11(a=a,b=b,c=c)==True:
		print("pre_condition_11 SAT")
		print('x = -3')
		print('y = -2')
		print('a = -17')
		print('z = 1')
		print('b = -25')
		print('c = -6')
		exit(0)
	
	
	if pre_condition_12(a=a,b=b,c=c)==True:
		print("pre_condition_12 SAT")
		print('x = -4')
		print('y = -1')
		print('a = -64')
		print('z = -1')
		print('b = -64')
		print('c = -1')
		exit(0)
	
	
	if pre_condition_13(a=a,b=b,c=c)==True:
		print("pre_condition_13 SAT")
		print('x = -4')
		print('y = -1')
		print('a = -64')
		print('z = -1')
		print('b = -64')
		print('c = -1')
		exit(0)
	
	
	if pre_condition_14(a=a,b=b,c=c)==True:
		print("pre_condition_14 SAT")
		print('x = -4')
		print('y = -1')
		print('a = -64')
		print('z = -1')
		print('b = -64')
		print('c = -1')
		exit(0)
	
	
	if pre_condition_15(a=a,b=b,c=c)==True:
		print("pre_condition_15 SAT")
		print('x = -5')
		print('y = -1')
		print('a = -66')
		print('z = 1/2')
		print('b = -124')
		print('c = 1')
		exit(0)
	
	
	if pre_condition_16(a=a,b=b,c=c)==True:
		print("pre_condition_16 SAT")
		print('x = -5')
		print('y = -1')
		print('a = -66')
		print('z = 1/2')
		print('b = -124')
		print('c = 1')
		exit(0)
	
	
	if pre_condition_17(a=a,b=b,c=c)==True:
		print("pre_condition_17 SAT")
		print('x = -5')
		print('y = -1')
		print('a = -66')
		print('z = 1/2')
		print('b = -124')
		print('c = 1')
		exit(0)
	
	
	if pre_condition_18(a=a,b=b,c=c)==True:
		print("pre_condition_18 SAT")
		print('x = -6')
		print('y = -1')
		print('a = -127')
		print('z = 1/2')
		print('b = -215')
		print('c = 1')
		exit(0)
	
	
	if pre_condition_19(a=a,b=b,c=c)==True:
		print("pre_condition_19 SAT")
		print('x = -6')
		print('y = -1')
		print('a = -127')
		print('z = 1/2')
		print('b = -215')
		print('c = 1')
		exit(0)
	
	
	if pre_condition_20(a=a,b=b,c=c)==True:
		print("pre_condition_20 SAT")
		print('x = -6')
		print('y = -1')
		print('a = -127')
		print('z = 1/2')
		print('b = -215')
		print('c = 1')
		exit(0)
	
	
	if pre_condition_21(a=a,b=b,c=c)==True:
		print("pre_condition_21 SAT")
		print('x = -16')
		print('y = 0')
		print('a = -4095')
		print('z = 1/2')
		print('b = -217')
		print('c = 2')
		exit(0)
	
	
	if pre_condition_22(a=a,b=b,c=c)==True:
		print("pre_condition_22 SAT")
		print('x = -16')
		print('y = 0')
		print('a = -4095')
		print('z = 1/2')
		print('b = -217')
		print('c = 2')
		exit(0)
	
	
	if pre_condition_23(a=a,b=b,c=c)==True:
		print("pre_condition_23 SAT")
		print('x = -16')
		print('y = 0')
		print('a = -4095')
		print('z = 1/2')
		print('b = -217')
		print('c = 2')
		exit(0)
	
	
	if pre_condition_24(a=a,b=b,c=c)==True:
		print("pre_condition_24 SAT")
		print('x = -17')
		print('y = -1')
		print('a = -4097')
		print('z = 1/2')
		print('b = -4912')
		print('c = 0')
		exit(0)
	
	
	if pre_condition_25(a=a,b=b,c=c)==True:
		print("pre_condition_25 SAT")
		print('x = -17')
		print('y = -1')
		print('a = -4097')
		print('z = 1/2')
		print('b = -4912')
		print('c = 0')
		exit(0)
	
	
	if pre_condition_26(a=a,b=b,c=c)==True:
		print("pre_condition_26 SAT")
		print('x = -17')
		print('y = -1')
		print('a = -4097')
		print('z = 1/2')
		print('b = -4912')
		print('c = 0')
		exit(0)
	
	
	if pre_condition_27(a=a,b=b,c=c)==True:
		print("pre_condition_27 SAT")
		print('x = -18')
		print('y = -1')
		print('a = -5832')
		print('z = 1/2')
		print('b = -5831')
		print('c = 0')
		exit(0)
	
	
	if pre_condition_28(a=a,b=b,c=c)==True:
		print("pre_condition_28 SAT")
		print('x = -18')
		print('y = -1')
		print('a = -5832')
		print('z = 1/2')
		print('b = -5831')
		print('c = 0')
		exit(0)
	
	
	if pre_condition_29(a=a,b=b,c=c)==True:
		print("pre_condition_29 SAT")
		print('x = -18')
		print('y = -1')
		print('a = -5832')
		print('z = 1/2')
		print('b = -5831')
		print('c = 0')
		exit(0)
	
	
	if pre_condition_30(a=a,b=b,c=c)==True:
		print("pre_condition_30 SAT")
		print('x = -19')
		print('y = -1')
		print('a = -127')
		print('z = 1/4')
		print('b = -6858')
		print('c = -15/16')
		exit(0)
	
	
	if pre_condition_31(a=a,b=b,c=c)==True:
		print("pre_condition_31 SAT")
		print('x = -19')
		print('y = -1')
		print('a = -127')
		print('z = 1/4')
		print('b = -6858')
		print('c = -15/16')
		exit(0)
	
	
	if pre_condition_32(a=a,b=b,c=c)==True:
		print("pre_condition_32 SAT")
		print('x = -19')
		print('y = -1')
		print('a = -127')
		print('z = 1/4')
		print('b = -6858')
		print('c = -15/16')
		exit(0)
	
	
	if pre_condition_33(a=a,b=b,c=c)==True:
		print("pre_condition_33 SAT")
		print('x = -20')
		print('y = -1')
		print('a = -127')
		print('z = -1')
		print('b = -8000')
		print('c = -3/2')
		exit(0)
	
	
	if pre_condition_34(a=a,b=b,c=c)==True:
		print("pre_condition_34 SAT")
		print('x = -20')
		print('y = -1')
		print('a = -127')
		print('z = -1')
		print('b = -8000')
		print('c = -3/2')
		exit(0)
	
	
	if pre_condition_35(a=a,b=b,c=c)==True:
		print("pre_condition_35 SAT")
		print('x = -20')
		print('y = -1')
		print('a = -127')
		print('z = -1')
		print('b = -8000')
		print('c = -3/2')
		exit(0)
	
	
	if pre_condition_36(a=a,b=b,c=c)==True:
		print("pre_condition_36 SAT")
		print('x = -21')
		print('y = -1')
		print('a = -127')
		print('z = -2')
		print('b = -9268')
		print('c = -17/2')
		exit(0)
	
	
	if pre_condition_37(a=a,b=b,c=c)==True:
		print("pre_condition_37 SAT")
		print('x = -21')
		print('y = -1')
		print('a = -127')
		print('z = -2')
		print('b = -9268')
		print('c = -17/2')
		exit(0)
	
	
	if pre_condition_38(a=a,b=b,c=c)==True:
		print("pre_condition_38 SAT")
		print('x = -21')
		print('y = -1')
		print('a = -127')
		print('z = -2')
		print('b = -9268')
		print('c = -17/2')
		exit(0)
	
	
	if pre_condition_39(a=a,b=b,c=c)==True:
		print("pre_condition_39 SAT")
		print('x = -22')
		print('y = -1')
		print('a = -9263')
		print('z = 1/2')
		print('b = -10647')
		print('c = 0')
		exit(0)
	
	
	if pre_condition_40(a=a,b=b,c=c)==True:
		print("pre_condition_40 SAT")
		print('x = -22')
		print('y = -1')
		print('a = -9263')
		print('z = 1/2')
		print('b = -10647')
		print('c = 0')
		exit(0)
	
	
	if pre_condition_41(a=a,b=b,c=c)==True:
		print("pre_condition_41 SAT")
		print('x = -22')
		print('y = -1')
		print('a = -9263')
		print('z = 1/2')
		print('b = -10647')
		print('c = 0')
		exit(0)
	
	
	if pre_condition_42(a=a,b=b,c=c)==True:
		print("pre_condition_42 SAT")
		print('x = -23')
		print('y = -1')
		print('a = -9263')
		print('z = -1')
		print('b = -12167')
		print('c = -3/2')
		exit(0)
	
	
	if pre_condition_43(a=a,b=b,c=c)==True:
		print("pre_condition_43 SAT")
		print('x = -23')
		print('y = -1')
		print('a = -9263')
		print('z = -1')
		print('b = -12167')
		print('c = -3/2')
		exit(0)
	
	
	if pre_condition_44(a=a,b=b,c=c)==True:
		print("pre_condition_44 SAT")
		print('x = -23')
		print('y = -1')
		print('a = -9263')
		print('z = -1')
		print('b = -12167')
		print('c = -3/2')
		exit(0)
	
	
	if pre_condition_45(a=a,b=b,c=c)==True:
		print("pre_condition_45 SAT")
		print('x = -24')
		print('y = -1')
		print('a = -9263')
		print('z = -2')
		print('b = -13831')
		print('c = -17/2')
		exit(0)
	
	
	if pre_condition_46(a=a,b=b,c=c)==True:
		print("pre_condition_46 SAT")
		print('x = -24')
		print('y = -1')
		print('a = -9263')
		print('z = -2')
		print('b = -13831')
		print('c = -17/2')
		exit(0)
	
	
	if pre_condition_47(a=a,b=b,c=c)==True:
		print("pre_condition_47 SAT")
		print('x = -24')
		print('y = -1')
		print('a = -9263')
		print('z = -2')
		print('b = -13831')
		print('c = -17/2')
		exit(0)
	
	
	if pre_condition_48(a=a,b=b,c=c)==True:
		print("pre_condition_48 SAT")
		print('x = -25')
		print('y = -1')
		print('a = -13826')
		print('z = 1/2')
		print('b = -15624')
		print('c = 0')
		exit(0)
	
	
	if pre_condition_49(a=a,b=b,c=c)==True:
		print("pre_condition_49 SAT")
		print('x = -25')
		print('y = -1')
		print('a = -13826')
		print('z = 1/2')
		print('b = -15624')
		print('c = 0')
		exit(0)
	
	
	if pre_condition_50(a=a,b=b,c=c)==True:
		print("pre_condition_50 SAT")
		print('x = -25')
		print('y = -1')
		print('a = -13826')
		print('z = 1/2')
		print('b = -15624')
		print('c = 0')
		exit(0)
	
	
	if pre_condition_51(a=a,b=b,c=c)==True:
		print("pre_condition_51 SAT")
		print('x = -26')
		print('y = -1')
		print('a = -13826')
		print('z = -1')
		print('b = -17576')
		print('c = -3/2')
		exit(0)
	
	
	if pre_condition_52(a=a,b=b,c=c)==True:
		print("pre_condition_52 SAT")
		print('x = -26')
		print('y = -1')
		print('a = -13826')
		print('z = -1')
		print('b = -17576')
		print('c = -3/2')
		exit(0)
	
	
	if pre_condition_53(a=a,b=b,c=c)==True:
		print("pre_condition_53 SAT")
		print('x = -26')
		print('y = -1')
		print('a = -13826')
		print('z = -1')
		print('b = -17576')
		print('c = -3/2')
		exit(0)
	
	
	if pre_condition_54(a=a,b=b,c=c)==True:
		print("pre_condition_54 SAT")
		print('x = -27')
		print('y = -1')
		print('a = -13826')
		print('z = -2')
		print('b = -19690')
		print('c = -17/2')
		exit(0)
	
	
	if pre_condition_55(a=a,b=b,c=c)==True:
		print("pre_condition_55 SAT")
		print('x = -27')
		print('y = -1')
		print('a = -13826')
		print('z = -2')
		print('b = -19690')
		print('c = -17/2')
		exit(0)
	
	
	if pre_condition_56(a=a,b=b,c=c)==True:
		print("pre_condition_56 SAT")
		print('x = -27')
		print('y = -1')
		print('a = -13826')
		print('z = -2')
		print('b = -19690')
		print('c = -17/2')
		exit(0)
	
	
	if pre_condition_57(a=a,b=b,c=c)==True:
		print("pre_condition_57 SAT")
		print('x = -28')
		print('y = -1')
		print('a = -19685')
		print('z = 1/2')
		print('b = -21951')
		print('c = 0')
		exit(0)
	
	
	if pre_condition_58(a=a,b=b,c=c)==True:
		print("pre_condition_58 SAT")
		print('x = -28')
		print('y = -1')
		print('a = -19685')
		print('z = 1/2')
		print('b = -21951')
		print('c = 0')
		exit(0)
	
	
	if pre_condition_59(a=a,b=b,c=c)==True:
		print("pre_condition_59 SAT")
		print('x = -28')
		print('y = -1')
		print('a = -19685')
		print('z = 1/2')
		print('b = -21951')
		print('c = 0')
		exit(0)
	
	
	if pre_condition_60(a=a,b=b,c=c)==True:
		print("pre_condition_60 SAT")
		print('x = -29')
		print('y = -1')
		print('a = -19685')
		print('z = -1')
		print('b = -24389')
		print('c = -3/2')
		exit(0)
	
	
	if pre_condition_61(a=a,b=b,c=c)==True:
		print("pre_condition_61 SAT")
		print('x = -29')
		print('y = -1')
		print('a = -19685')
		print('z = -1')
		print('b = -24389')
		print('c = -3/2')
		exit(0)
	
	
	if pre_condition_62(a=a,b=b,c=c)==True:
		print("pre_condition_62 SAT")
		print('x = -29')
		print('y = -1')
		print('a = -19685')
		print('z = -1')
		print('b = -24389')
		print('c = -3/2')
		exit(0)
	
	
	if pre_condition_63(a=a,b=b,c=c)==True:
		print("pre_condition_63 SAT")
		print('x = -30')
		print('y = -1')
		print('a = -19685')
		print('z = -2')
		print('b = -27007')
		print('c = -17/2')
		exit(0)
	
	
	if pre_condition_64(a=a,b=b,c=c)==True:
		print("pre_condition_64 SAT")
		print('x = -30')
		print('y = -1')
		print('a = -19685')
		print('z = -2')
		print('b = -27007')
		print('c = -17/2')
		exit(0)
	
	
	if pre_condition_65(a=a,b=b,c=c)==True:
		print("pre_condition_65 SAT")
		print('x = -30')
		print('y = -1')
		print('a = -19685')
		print('z = -2')
		print('b = -27007')
		print('c = -17/2')
		exit(0)
	
	
	if pre_condition_66(a=a,b=b,c=c)==True:
		print("pre_condition_66 SAT")
		print('x = -31')
		print('y = -1')
		print('a = -19685')
		print('z = -3')
		print('b = -29817')
		print('c = -55/2')
		exit(0)
	
	
	if pre_condition_67(a=a,b=b,c=c)==True:
		print("pre_condition_67 SAT")
		print('x = -31')
		print('y = -1')
		print('a = -19685')
		print('z = -3')
		print('b = -29817')
		print('c = -55/2')
		exit(0)
	
	
	if pre_condition_68(a=a,b=b,c=c)==True:
		print("pre_condition_68 SAT")
		print('x = -31')
		print('y = -1')
		print('a = -19685')
		print('z = -3')
		print('b = -29817')
		print('c = -55/2')
		exit(0)
	
	
	if pre_condition_69(a=a,b=b,c=c)==True:
		print("pre_condition_69 SAT")
		print('x = -32')
		print('y = -1')
		print('a = -29793')
		print('z = 1/2')
		print('b = -32767')
		print('c = 0')
		exit(0)
	
	
	if pre_condition_70(a=a,b=b,c=c)==True:
		print("pre_condition_70 SAT")
		print('x = -32')
		print('y = -1')
		print('a = -29793')
		print('z = 1/2')
		print('b = -32767')
		print('c = 0')
		exit(0)
	
	
	if pre_condition_71(a=a,b=b,c=c)==True:
		print("pre_condition_71 SAT")
		print('x = -32')
		print('y = -1')
		print('a = -29793')
		print('z = 1/2')
		print('b = -32767')
		print('c = 0')
		exit(0)
	
	
	if pre_condition_72(a=a,b=b,c=c)==True:
		print("pre_condition_72 SAT")
		print('x = -33')
		print('y = -1')
		print('a = -29793')
		print('z = -3')
		print('b = -35963')
		print('c = -55/2')
		exit(0)
	
	
	if pre_condition_73(a=a,b=b,c=c)==True:
		print("pre_condition_73 SAT")
		print('x = -33')
		print('y = -1')
		print('a = -29793')
		print('z = -3')
		print('b = -35963')
		print('c = -55/2')
		exit(0)
	
	
	if pre_condition_74(a=a,b=b,c=c)==True:
		print("pre_condition_74 SAT")
		print('x = -33')
		print('y = -1')
		print('a = -29793')
		print('z = -3')
		print('b = -35963')
		print('c = -55/2')
		exit(0)
	
	
	if pre_condition_75(a=a,b=b,c=c)==True:
		print("pre_condition_75 SAT")
		print('x = -34')
		print('y = -1')
		print('a = -39304')
		print('z = -3')
		print('b = -39330')
		print('c = -55/2')
		exit(0)
	
	
	if pre_condition_76(a=a,b=b,c=c)==True:
		print("pre_condition_76 SAT")
		print('x = -34')
		print('y = -1')
		print('a = -39304')
		print('z = -3')
		print('b = -39330')
		print('c = -55/2')
		exit(0)
	
	
	if pre_condition_77(a=a,b=b,c=c)==True:
		print("pre_condition_77 SAT")
		print('x = -34')
		print('y = -1')
		print('a = -39304')
		print('z = -3')
		print('b = -39330')
		print('c = -55/2')
		exit(0)
	
	
	if pre_condition_78(a=a,b=b,c=c)==True:
		print("pre_condition_78 SAT")
		print('x = -35')
		print('y = -1')
		print('a = -32770')
		print('z = -4')
		print('b = -42938')
		print('c = -129/2')
		exit(0)
	
	
	if pre_condition_79(a=a,b=b,c=c)==True:
		print("pre_condition_79 SAT")
		print('x = -35')
		print('y = -1')
		print('a = -32770')
		print('z = -4')
		print('b = -42938')
		print('c = -129/2')
		exit(0)
	
	
	if pre_condition_80(a=a,b=b,c=c)==True:
		print("pre_condition_80 SAT")
		print('x = -35')
		print('y = -1')
		print('a = -32770')
		print('z = -4')
		print('b = -42938')
		print('c = -129/2')
		exit(0)
	
	
	if pre_condition_81(a=a,b=b,c=c)==True:
		print("pre_condition_81 SAT")
		print('x = -36')
		print('y = -1')
		print('a = -42877')
		print('z = 1/2')
		print('b = -46655')
		print('c = 0')
		exit(0)
	
	
	if pre_condition_82(a=a,b=b,c=c)==True:
		print("pre_condition_82 SAT")
		print('x = -36')
		print('y = -1')
		print('a = -42877')
		print('z = 1/2')
		print('b = -46655')
		print('c = 0')
		exit(0)
	
	
	if pre_condition_83(a=a,b=b,c=c)==True:
		print("pre_condition_83 SAT")
		print('x = -36')
		print('y = -1')
		print('a = -42877')
		print('z = 1/2')
		print('b = -46655')
		print('c = 0')
		exit(0)
	
	
	if pre_condition_84(a=a,b=b,c=c)==True:
		print("pre_condition_84 SAT")
		print('x = -37')
		print('y = -1')
		print('a = -42877')
		print('z = -4')
		print('b = -50716')
		print('c = -129/2')
		exit(0)
	
	
	if pre_condition_85(a=a,b=b,c=c)==True:
		print("pre_condition_85 SAT")
		print('x = -37')
		print('y = -1')
		print('a = -42877')
		print('z = -4')
		print('b = -50716')
		print('c = -129/2')
		exit(0)
	
	
	if pre_condition_86(a=a,b=b,c=c)==True:
		print("pre_condition_86 SAT")
		print('x = -37')
		print('y = -1')
		print('a = -42877')
		print('z = -4')
		print('b = -50716')
		print('c = -129/2')
		exit(0)
	
	
	if pre_condition_87(a=a,b=b,c=c)==True:
		print("pre_condition_87 SAT")
		print('x = -38')
		print('y = -1')
		print('a = -54872')
		print('z = -4')
		print('b = -50718')
		print('c = -129/2')
		exit(0)
	
	
	if pre_condition_88(a=a,b=b,c=c)==True:
		print("pre_condition_88 SAT")
		print('x = -38')
		print('y = -1')
		print('a = -54872')
		print('z = -4')
		print('b = -50718')
		print('c = -129/2')
		exit(0)
	
	
	if pre_condition_89(a=a,b=b,c=c)==True:
		print("pre_condition_89 SAT")
		print('x = -38')
		print('y = -1')
		print('a = -54872')
		print('z = -4')
		print('b = -50718')
		print('c = -129/2')
		exit(0)
	
	
	if pre_condition_90(a=a,b=b,c=c)==True:
		print("pre_condition_90 SAT")
		print('x = -39')
		print('y = -1')
		print('a = -21954')
		print('z = -5')
		print('b = -59443')
		print('c = -251/2')
		exit(0)
	
	
	if pre_condition_91(a=a,b=b,c=c)==True:
		print("pre_condition_91 SAT")
		print('x = -39')
		print('y = -1')
		print('a = -21954')
		print('z = -5')
		print('b = -59443')
		print('c = -251/2')
		exit(0)
	
	
	if pre_condition_92(a=a,b=b,c=c)==True:
		print("pre_condition_92 SAT")
		print('x = -39')
		print('y = -1')
		print('a = -21954')
		print('z = -5')
		print('b = -59443')
		print('c = -251/2')
		exit(0)
	
	
	if pre_condition_93(a=a,b=b,c=c)==True:
		print("pre_condition_93 SAT")
		print('x = -40')
		print('y = -1')
		print('a = -42877')
		print('z = -6')
		print('b = -64215')
		print('c = -433/2')
		exit(0)
	
	
	if pre_condition_94(a=a,b=b,c=c)==True:
		print("pre_condition_94 SAT")
		print('x = -40')
		print('y = -1')
		print('a = -42877')
		print('z = -6')
		print('b = -64215')
		print('c = -433/2')
		exit(0)
	
	
	if pre_condition_95(a=a,b=b,c=c)==True:
		print("pre_condition_95 SAT")
		print('x = -40')
		print('y = -1')
		print('a = -42877')
		print('z = -6')
		print('b = -64215')
		print('c = -433/2')
		exit(0)
	
	
	if pre_condition_96(a=a,b=b,c=c)==True:
		print("pre_condition_96 SAT")
		print('x = -41')
		print('y = -1')
		print('a = -64002')
		print('z = 1/2')
		print('b = -68920')
		print('c = 0')
		exit(0)
	
	
	if pre_condition_97(a=a,b=b,c=c)==True:
		print("pre_condition_97 SAT")
		print('x = -41')
		print('y = -1')
		print('a = -64002')
		print('z = 1/2')
		print('b = -68920')
		print('c = 0')
		exit(0)
	
	
	if pre_condition_98(a=a,b=b,c=c)==True:
		print("pre_condition_98 SAT")
		print('x = -41')
		print('y = -1')
		print('a = -64002')
		print('z = 1/2')
		print('b = -68920')
		print('c = 0')
		exit(0)
	
	
	if pre_condition_99(a=a,b=b,c=c)==True:
		print("pre_condition_99 SAT")
		print('x = -42')
		print('y = -1')
		print('a = -64002')
		print('z = -2')
		print('b = -74095')
		print('c = -17/2')
		exit(0)
	
	
	if pre_condition_100(a=a,b=b,c=c)==True:
		print("pre_condition_100 SAT")
		print('x = -42')
		print('y = -1')
		print('a = -64002')
		print('z = -2')
		print('b = -74095')
		print('c = -17/2')
		exit(0)
	
	
	if pre_condition_101(a=a,b=b,c=c)==True:
		print("pre_condition_101 SAT")
		print('x = -42')
		print('y = -1')
		print('a = -64002')
		print('z = -2')
		print('b = -74095')
		print('c = -17/2')
		exit(0)
	
	
	if pre_condition_102(a=a,b=b,c=c)==True:
		print("pre_condition_102 SAT")
		print('x = -43')
		print('y = -1')
		print('a = -64002')
		print('z = -6')
		print('b = -79722')
		print('c = -433/2')
		exit(0)
	
	
	if pre_condition_103(a=a,b=b,c=c)==True:
		print("pre_condition_103 SAT")
		print('x = -43')
		print('y = -1')
		print('a = -64002')
		print('z = -6')
		print('b = -79722')
		print('c = -433/2')
		exit(0)
	
	
	if pre_condition_104(a=a,b=b,c=c)==True:
		print("pre_condition_104 SAT")
		print('x = -43')
		print('y = -1')
		print('a = -64002')
		print('z = -6')
		print('b = -79722')
		print('c = -433/2')
		exit(0)
	
	
	if pre_condition_105(a=a,b=b,c=c)==True:
		print("pre_condition_105 SAT")
		print('x = -44')
		print('y = -1')
		print('a = -42877')
		print('z = -7')
		print('b = -85526')
		print('c = -687/2')
		exit(0)
	
	
	if pre_condition_106(a=a,b=b,c=c)==True:
		print("pre_condition_106 SAT")
		print('x = -44')
		print('y = -1')
		print('a = -42877')
		print('z = -7')
		print('b = -85526')
		print('c = -687/2')
		exit(0)
	
	
	if pre_condition_107(a=a,b=b,c=c)==True:
		print("pre_condition_107 SAT")
		print('x = -44')
		print('y = -1')
		print('a = -42877')
		print('z = -7')
		print('b = -85526')
		print('c = -687/2')
		exit(0)
	
	
	if pre_condition_108(a=a,b=b,c=c)==True:
		print("pre_condition_108 SAT")
		print('x = -45')
		print('y = -1')
		print('a = -85186')
		print('z = 1/2')
		print('b = -91124')
		print('c = 0')
		exit(0)
	
	
	if pre_condition_109(a=a,b=b,c=c)==True:
		print("pre_condition_109 SAT")
		print('x = -45')
		print('y = -1')
		print('a = -85186')
		print('z = 1/2')
		print('b = -91124')
		print('c = 0')
		exit(0)
	
	
	if pre_condition_110(a=a,b=b,c=c)==True:
		print("pre_condition_110 SAT")
		print('x = -45')
		print('y = -1')
		print('a = -85186')
		print('z = 1/2')
		print('b = -91124')
		print('c = 0')
		exit(0)
	
	
	if pre_condition_111(a=a,b=b,c=c)==True:
		print("pre_condition_111 SAT")
		print('x = -46')
		print('y = -1')
		print('a = -85186')
		print('z = -1')
		print('b = -97336')
		print('c = -3/2')
		exit(0)
	
	
	if pre_condition_112(a=a,b=b,c=c)==True:
		print("pre_condition_112 SAT")
		print('x = -46')
		print('y = -1')
		print('a = -85186')
		print('z = -1')
		print('b = -97336')
		print('c = -3/2')
		exit(0)
	
	
	if pre_condition_113(a=a,b=b,c=c)==True:
		print("pre_condition_113 SAT")
		print('x = -46')
		print('y = -1')
		print('a = -85186')
		print('z = -1')
		print('b = -97336')
		print('c = -3/2')
		exit(0)
	
	
	if pre_condition_114(a=a,b=b,c=c)==True:
		print("pre_condition_114 SAT")
		print('x = -47')
		print('y = -1')
		print('a = -85186')
		print('z = -3')
		print('b = -103849')
		print('c = -55/2')
		exit(0)
	
	
	if pre_condition_115(a=a,b=b,c=c)==True:
		print("pre_condition_115 SAT")
		print('x = -47')
		print('y = -1')
		print('a = -85186')
		print('z = -3')
		print('b = -103849')
		print('c = -55/2')
		exit(0)
	
	
	if pre_condition_116(a=a,b=b,c=c)==True:
		print("pre_condition_116 SAT")
		print('x = -47')
		print('y = -1')
		print('a = -85186')
		print('z = -3')
		print('b = -103849')
		print('c = -55/2')
		exit(0)
	
	
	if pre_condition_117(a=a,b=b,c=c)==True:
		print("pre_condition_117 SAT")
		print('x = -48')
		print('y = -1')
		print('a = -85186')
		print('z = -4')
		print('b = -110655')
		print('c = -129/2')
		exit(0)
	
	
	if pre_condition_118(a=a,b=b,c=c)==True:
		print("pre_condition_118 SAT")
		print('x = -48')
		print('y = -1')
		print('a = -85186')
		print('z = -4')
		print('b = -110655')
		print('c = -129/2')
		exit(0)
	
	
	if pre_condition_119(a=a,b=b,c=c)==True:
		print("pre_condition_119 SAT")
		print('x = -48')
		print('y = -1')
		print('a = -85186')
		print('z = -4')
		print('b = -110655')
		print('c = -129/2')
		exit(0)
	
	
	if pre_condition_120(a=a,b=b,c=c)==True:
		print("pre_condition_120 SAT")
		print('x = -49')
		print('y = -1')
		print('a = -85186')
		print('z = -5')
		print('b = -117773')
		print('c = -251/2')
		exit(0)
	
	
	if pre_condition_121(a=a,b=b,c=c)==True:
		print("pre_condition_121 SAT")
		print('x = -49')
		print('y = -1')
		print('a = -85186')
		print('z = -5')
		print('b = -117773')
		print('c = -251/2')
		exit(0)
	
	
	if pre_condition_122(a=a,b=b,c=c)==True:
		print("pre_condition_122 SAT")
		print('x = -49')
		print('y = -1')
		print('a = -85186')
		print('z = -5')
		print('b = -117773')
		print('c = -251/2')
		exit(0)
	
	
	if pre_condition_123(a=a,b=b,c=c)==True:
		print("pre_condition_123 SAT")
		print('x = -50')
		print('y = -1')
		print('a = -85186')
		print('z = -6')
		print('b = -125215')
		print('c = -433/2')
		exit(0)
	
	
	if pre_condition_124(a=a,b=b,c=c)==True:
		print("pre_condition_124 SAT")
		print('x = -50')
		print('y = -1')
		print('a = -85186')
		print('z = -6')
		print('b = -125215')
		print('c = -433/2')
		exit(0)
	
	
	if pre_condition_125(a=a,b=b,c=c)==True:
		print("pre_condition_125 SAT")
		print('x = -50')
		print('y = -1')
		print('a = -85186')
		print('z = -6')
		print('b = -125215')
		print('c = -433/2')
		exit(0)
	
	
	if pre_condition_126(a=a,b=b,c=c)==True:
		print("pre_condition_126 SAT")
		print('x = -51')
		print('y = -1')
		print('a = -85186')
		print('z = -7')
		print('b = -132993')
		print('c = -687/2')
		exit(0)
	
	
	if pre_condition_127(a=a,b=b,c=c)==True:
		print("pre_condition_127 SAT")
		print('x = -51')
		print('y = -1')
		print('a = -85186')
		print('z = -7')
		print('b = -132993')
		print('c = -687/2')
		exit(0)
	
	
	if pre_condition_128(a=a,b=b,c=c)==True:
		print("pre_condition_128 SAT")
		print('x = -51')
		print('y = -1')
		print('a = -85186')
		print('z = -7')
		print('b = -132993')
		print('c = -687/2')
		exit(0)
	
	
	if pre_condition_129(a=a,b=b,c=c)==True:
		print("pre_condition_129 SAT")
		print('x = -52')
		print('y = -1')
		print('a = -85186')
		print('z = -8')
		print('b = -141119')
		print('c = -1025/2')
		exit(0)
	
	
	if pre_condition_130(a=a,b=b,c=c)==True:
		print("pre_condition_130 SAT")
		print('x = -52')
		print('y = -1')
		print('a = -85186')
		print('z = -8')
		print('b = -141119')
		print('c = -1025/2')
		exit(0)
	
	
	if pre_condition_131(a=a,b=b,c=c)==True:
		print("pre_condition_131 SAT")
		print('x = -52')
		print('y = -1')
		print('a = -85186')
		print('z = -8')
		print('b = -141119')
		print('c = -1025/2')
		exit(0)
	
	
	if pre_condition_132(a=a,b=b,c=c)==True:
		print("pre_condition_132 SAT")
		print('x = -53')
		print('y = -1')
		print('a = -10')
		print('z = -9')
		print('b = -149605')
		print('c = -1459/2')
		exit(0)
	
	
	if pre_condition_133(a=a,b=b,c=c)==True:
		print("pre_condition_133 SAT")
		print('x = -53')
		print('y = -1')
		print('a = -10')
		print('z = -9')
		print('b = -149605')
		print('c = -1459/2')
		exit(0)
	
	
	if pre_condition_134(a=a,b=b,c=c)==True:
		print("pre_condition_134 SAT")
		print('x = -53')
		print('y = -1')
		print('a = -10')
		print('z = -9')
		print('b = -149605')
		print('c = -1459/2')
		exit(0)
	
	
	if pre_condition_135(a=a,b=b,c=c)==True:
		print("pre_condition_135 SAT")
		print('x = -54')
		print('y = -1')
		print('a = -68923')
		print('z = -10')
		print('b = -158463')
		print('c = -2001/2')
		exit(0)
	
	
	if pre_condition_136(a=a,b=b,c=c)==True:
		print("pre_condition_136 SAT")
		print('x = -54')
		print('y = -1')
		print('a = -68923')
		print('z = -10')
		print('b = -158463')
		print('c = -2001/2')
		exit(0)
	
	
	if pre_condition_137(a=a,b=b,c=c)==True:
		print("pre_condition_137 SAT")
		print('x = -54')
		print('y = -1')
		print('a = -68923')
		print('z = -10')
		print('b = -158463')
		print('c = -2001/2')
		exit(0)
	
	
	if pre_condition_138(a=a,b=b,c=c)==True:
		print("pre_condition_138 SAT")
		print('x = -55')
		print('y = -1')
		print('a = -10')
		print('z = -11')
		print('b = -167705')
		print('c = -2663/2')
		exit(0)
	
	
	if pre_condition_139(a=a,b=b,c=c)==True:
		print("pre_condition_139 SAT")
		print('x = -55')
		print('y = -1')
		print('a = -10')
		print('z = -11')
		print('b = -167705')
		print('c = -2663/2')
		exit(0)
	
	
	if pre_condition_140(a=a,b=b,c=c)==True:
		print("pre_condition_140 SAT")
		print('x = -55')
		print('y = -1')
		print('a = -10')
		print('z = -11')
		print('b = -167705')
		print('c = -2663/2')
		exit(0)
	
	
	if pre_condition_141(a=a,b=b,c=c)==True:
		print("pre_condition_141 SAT")
		print('x = -56')
		print('y = -1')
		print('a = -166377')
		print('z = 1/2')
		print('b = -175615')
		print('c = 0')
		exit(0)
	
	
	if pre_condition_142(a=a,b=b,c=c)==True:
		print("pre_condition_142 SAT")
		print('x = -56')
		print('y = -1')
		print('a = -166377')
		print('z = 1/2')
		print('b = -175615')
		print('c = 0')
		exit(0)
	
	
	if pre_condition_143(a=a,b=b,c=c)==True:
		print("pre_condition_143 SAT")
		print('x = -56')
		print('y = -1')
		print('a = -166377')
		print('z = 1/2')
		print('b = -175615')
		print('c = 0')
		exit(0)
	
	
	if pre_condition_144(a=a,b=b,c=c)==True:
		print("pre_condition_144 SAT")
		print('x = -57')
		print('y = -1')
		print('a = -166377')
		print('z = -6')
		print('b = -185408')
		print('c = -433/2')
		exit(0)
	
	
	if pre_condition_145(a=a,b=b,c=c)==True:
		print("pre_condition_145 SAT")
		print('x = -57')
		print('y = -1')
		print('a = -166377')
		print('z = -6')
		print('b = -185408')
		print('c = -433/2')
		exit(0)
	
	
	if pre_condition_146(a=a,b=b,c=c)==True:
		print("pre_condition_146 SAT")
		print('x = -57')
		print('y = -1')
		print('a = -166377')
		print('z = -6')
		print('b = -185408')
		print('c = -433/2')
		exit(0)
	
	
	if pre_condition_147(a=a,b=b,c=c)==True:
		print("pre_condition_147 SAT")
		print('x = -58')
		print('y = -1')
		print('a = -166377')
		print('z = -9')
		print('b = -195840')
		print('c = -1459/2')
		exit(0)
	
	
	if pre_condition_148(a=a,b=b,c=c)==True:
		print("pre_condition_148 SAT")
		print('x = -58')
		print('y = -1')
		print('a = -166377')
		print('z = -9')
		print('b = -195840')
		print('c = -1459/2')
		exit(0)
	
	
	if pre_condition_149(a=a,b=b,c=c)==True:
		print("pre_condition_149 SAT")
		print('x = -58')
		print('y = -1')
		print('a = -166377')
		print('z = -9')
		print('b = -195840')
		print('c = -1459/2')
		exit(0)
	
	
	if pre_condition_150(a=a,b=b,c=c)==True:
		print("pre_condition_150 SAT")
		print('x = -59')
		print('y = -1')
		print('a = -166377')
		print('z = -10')
		print('b = -206378')
		print('c = -2001/2')
		exit(0)
	
	
	if pre_condition_151(a=a,b=b,c=c)==True:
		print("pre_condition_151 SAT")
		print('x = -59')
		print('y = -1')
		print('a = -166377')
		print('z = -10')
		print('b = -206378')
		print('c = -2001/2')
		exit(0)
	
	
	if pre_condition_152(a=a,b=b,c=c)==True:
		print("pre_condition_152 SAT")
		print('x = -59')
		print('y = -1')
		print('a = -166377')
		print('z = -10')
		print('b = -206378')
		print('c = -2001/2')
		exit(0)
	
	
	if pre_condition_153(a=a,b=b,c=c)==True:
		print("pre_condition_153 SAT")
		print('x = -60')
		print('y = -1')
		print('a = -166377')
		print('z = -11')
		print('b = -217330')
		print('c = -2663/2')
		exit(0)
	
	
	if pre_condition_154(a=a,b=b,c=c)==True:
		print("pre_condition_154 SAT")
		print('x = -60')
		print('y = -1')
		print('a = -166377')
		print('z = -11')
		print('b = -217330')
		print('c = -2663/2')
		exit(0)
	
	
	if pre_condition_155(a=a,b=b,c=c)==True:
		print("pre_condition_155 SAT")
		print('x = -60')
		print('y = -1')
		print('a = -166377')
		print('z = -11')
		print('b = -217330')
		print('c = -2663/2')
		exit(0)
	
	
	if pre_condition_156(a=a,b=b,c=c)==True:
		print("pre_condition_156 SAT")
		print('x = -61')
		print('y = -1')
		print('a = -64002')
		print('z = -12')
		print('b = -228708')
		print('c = -3457/2')
		exit(0)
	
	
	if pre_condition_157(a=a,b=b,c=c)==True:
		print("pre_condition_157 SAT")
		print('x = -61')
		print('y = -1')
		print('a = -64002')
		print('z = -12')
		print('b = -228708')
		print('c = -3457/2')
		exit(0)
	
	
	if pre_condition_158(a=a,b=b,c=c)==True:
		print("pre_condition_158 SAT")
		print('x = -61')
		print('y = -1')
		print('a = -64002')
		print('z = -12')
		print('b = -228708')
		print('c = -3457/2')
		exit(0)
	
	
	if pre_condition_159(a=a,b=b,c=c)==True:
		print("pre_condition_159 SAT")
		print('x = -62')
		print('y = -1')
		print('a = -238328')
		print('z = -5')
		print('b = -227107')
		print('c = -251/2')
		exit(0)
	
	
	if pre_condition_160(a=a,b=b,c=c)==True:
		print("pre_condition_160 SAT")
		print('x = -62')
		print('y = -1')
		print('a = -238328')
		print('z = -5')
		print('b = -227107')
		print('c = -251/2')
		exit(0)
	
	
	if pre_condition_161(a=a,b=b,c=c)==True:
		print("pre_condition_161 SAT")
		print('x = -62')
		print('y = -1')
		print('a = -238328')
		print('z = -5')
		print('b = -227107')
		print('c = -251/2')
		exit(0)
	
	
	if pre_condition_162(a=a,b=b,c=c)==True:
		print("pre_condition_162 SAT")
		print('x = -63')
		print('y = -1')
		print('a = -226983')
		print('z = -9')
		print('b = -250775')
		print('c = -1459/2')
		exit(0)
	
	
	if pre_condition_163(a=a,b=b,c=c)==True:
		print("pre_condition_163 SAT")
		print('x = -63')
		print('y = -1')
		print('a = -226983')
		print('z = -9')
		print('b = -250775')
		print('c = -1459/2')
		exit(0)
	
	
	if pre_condition_164(a=a,b=b,c=c)==True:
		print("pre_condition_164 SAT")
		print('x = -63')
		print('y = -1')
		print('a = -226983')
		print('z = -9')
		print('b = -250775')
		print('c = -1459/2')
		exit(0)
	
	
	if pre_condition_165(a=a,b=b,c=c)==True:
		print("pre_condition_165 SAT")
		print('x = -64')
		print('y = -1')
		print('a = -226983')
		print('z = -10')
		print('b = -263143')
		print('c = -2001/2')
		exit(0)
	
	
	if pre_condition_166(a=a,b=b,c=c)==True:
		print("pre_condition_166 SAT")
		print('x = -64')
		print('y = -1')
		print('a = -226983')
		print('z = -10')
		print('b = -263143')
		print('c = -2001/2')
		exit(0)
	
	
	if pre_condition_167(a=a,b=b,c=c)==True:
		print("pre_condition_167 SAT")
		print('x = -64')
		print('y = -1')
		print('a = -226983')
		print('z = -10')
		print('b = -263143')
		print('c = -2001/2')
		exit(0)
	
	
	if pre_condition_168(a=a,b=b,c=c)==True:
		print("pre_condition_168 SAT")
		print('x = -65')
		print('y = -1')
		print('a = -226983')
		print('z = -12')
		print('b = -276352')
		print('c = -3457/2')
		exit(0)
	
	
	if pre_condition_169(a=a,b=b,c=c)==True:
		print("pre_condition_169 SAT")
		print('x = -65')
		print('y = -1')
		print('a = -226983')
		print('z = -12')
		print('b = -276352')
		print('c = -3457/2')
		exit(0)
	
	
	if pre_condition_170(a=a,b=b,c=c)==True:
		print("pre_condition_170 SAT")
		print('x = -65')
		print('y = -1')
		print('a = -226983')
		print('z = -12')
		print('b = -276352')
		print('c = -3457/2')
		exit(0)
	
	
	if pre_condition_171(a=a,b=b,c=c)==True:
		print("pre_condition_171 SAT")
		print('x = -66')
		print('y = -1')
		print('a = -19685')
		print('z = -13')
		print('b = -289692')
		print('c = -4395/2')
		exit(0)
	
	
	if pre_condition_172(a=a,b=b,c=c)==True:
		print("pre_condition_172 SAT")
		print('x = -66')
		print('y = -1')
		print('a = -19685')
		print('z = -13')
		print('b = -289692')
		print('c = -4395/2')
		exit(0)
	
	
	if pre_condition_173(a=a,b=b,c=c)==True:
		print("pre_condition_173 SAT")
		print('x = -66')
		print('y = -1')
		print('a = -19685')
		print('z = -13')
		print('b = -289692')
		print('c = -4395/2')
		exit(0)
	
	
	if pre_condition_174(a=a,b=b,c=c)==True:
		print("pre_condition_174 SAT")
		print('x = -67')
		print('y = -1')
		print('a = -166377')
		print('z = -14')
		print('b = -303506')
		print('c = -5489/2')
		exit(0)
	
	
	if pre_condition_175(a=a,b=b,c=c)==True:
		print("pre_condition_175 SAT")
		print('x = -67')
		print('y = -1')
		print('a = -166377')
		print('z = -14')
		print('b = -303506')
		print('c = -5489/2')
		exit(0)
	
	
	if pre_condition_176(a=a,b=b,c=c)==True:
		print("pre_condition_176 SAT")
		print('x = -67')
		print('y = -1')
		print('a = -166377')
		print('z = -14')
		print('b = -303506')
		print('c = -5489/2')
		exit(0)
	
	
	if pre_condition_177(a=a,b=b,c=c)==True:
		print("pre_condition_177 SAT")
		print('x = -68')
		print('y = -1')
		print('a = -314432')
		print('z = -7')
		print('b = -314774')
		print('c = -687/2')
		exit(0)
	
	
	if pre_condition_178(a=a,b=b,c=c)==True:
		print("pre_condition_178 SAT")
		print('x = -68')
		print('y = -1')
		print('a = -314432')
		print('z = -7')
		print('b = -314774')
		print('c = -687/2')
		exit(0)
	
	
	if pre_condition_179(a=a,b=b,c=c)==True:
		print("pre_condition_179 SAT")
		print('x = -68')
		print('y = -1')
		print('a = -314432')
		print('z = -7')
		print('b = -314774')
		print('c = -687/2')
		exit(0)
	
	
	if pre_condition_180(a=a,b=b,c=c)==True:
		print("pre_condition_180 SAT")
		print('x = -69')
		print('y = -1')
		print('a = -300765')
		print('z = -14')
		print('b = -331252')
		print('c = -5489/2')
		exit(0)
	
	
	if pre_condition_181(a=a,b=b,c=c)==True:
		print("pre_condition_181 SAT")
		print('x = -69')
		print('y = -1')
		print('a = -300765')
		print('z = -14')
		print('b = -331252')
		print('c = -5489/2')
		exit(0)
	
	
	if pre_condition_182(a=a,b=b,c=c)==True:
		print("pre_condition_182 SAT")
		print('x = -69')
		print('y = -1')
		print('a = -300765')
		print('z = -14')
		print('b = -331252')
		print('c = -5489/2')
		exit(0)
	
	
	if pre_condition_183(a=a,b=b,c=c)==True:
		print("pre_condition_183 SAT")
		print('x = -70')
		print('y = -1')
		print('a = -226983')
		print('z = -15')
		print('b = -346374')
		print('c = -6751/2')
		exit(0)
	
	
	if pre_condition_184(a=a,b=b,c=c)==True:
		print("pre_condition_184 SAT")
		print('x = -70')
		print('y = -1')
		print('a = -226983')
		print('z = -15')
		print('b = -346374')
		print('c = -6751/2')
		exit(0)
	
	
	if pre_condition_185(a=a,b=b,c=c)==True:
		print("pre_condition_185 SAT")
		print('x = -70')
		print('y = -1')
		print('a = -226983')
		print('z = -15')
		print('b = -346374')
		print('c = -6751/2')
		exit(0)
	
	
	if pre_condition_186(a=a,b=b,c=c)==True:
		print("pre_condition_186 SAT")
		print('x = -71')
		print('y = -1')
		print('a = -343002')
		print('z = -1')
		print('b = -357911')
		print('c = -3/2')
		exit(0)
	
	
	if pre_condition_187(a=a,b=b,c=c)==True:
		print("pre_condition_187 SAT")
		print('x = -71')
		print('y = -1')
		print('a = -343002')
		print('z = -1')
		print('b = -357911')
		print('c = -3/2')
		exit(0)
	
	
	if pre_condition_188(a=a,b=b,c=c)==True:
		print("pre_condition_188 SAT")
		print('x = -71')
		print('y = -1')
		print('a = -343002')
		print('z = -1')
		print('b = -357911')
		print('c = -3/2')
		exit(0)
	
	
	if pre_condition_189(a=a,b=b,c=c)==True:
		print("pre_condition_189 SAT")
		print('x = -72')
		print('y = -1')
		print('a = -343002')
		print('z = -12')
		print('b = -374975')
		print('c = -3457/2')
		exit(0)
	
	
	if pre_condition_190(a=a,b=b,c=c)==True:
		print("pre_condition_190 SAT")
		print('x = -72')
		print('y = -1')
		print('a = -343002')
		print('z = -12')
		print('b = -374975')
		print('c = -3457/2')
		exit(0)
	
	
	if pre_condition_191(a=a,b=b,c=c)==True:
		print("pre_condition_191 SAT")
		print('x = -72')
		print('y = -1')
		print('a = -343002')
		print('z = -12')
		print('b = -374975')
		print('c = -3457/2')
		exit(0)
	
	
	if pre_condition_192(a=a,b=b,c=c)==True:
		print("pre_condition_192 SAT")
		print('x = -73')
		print('y = -1')
		print('a = -343002')
		print('z = -15')
		print('b = -392391')
		print('c = -6751/2')
		exit(0)
	
	
	if pre_condition_193(a=a,b=b,c=c)==True:
		print("pre_condition_193 SAT")
		print('x = -73')
		print('y = -1')
		print('a = -343002')
		print('z = -15')
		print('b = -392391')
		print('c = -6751/2')
		exit(0)
	
	
	if pre_condition_194(a=a,b=b,c=c)==True:
		print("pre_condition_194 SAT")
		print('x = -73')
		print('y = -1')
		print('a = -343002')
		print('z = -15')
		print('b = -392391')
		print('c = -6751/2')
		exit(0)
	
	
	if pre_condition_195(a=a,b=b,c=c)==True:
		print("pre_condition_195 SAT")
		print('x = -74')
		print('y = -1')
		print('a = -300765')
		print('z = -16')
		print('b = -409319')
		print('c = -8193/2')
		exit(0)
	
	
	if pre_condition_196(a=a,b=b,c=c)==True:
		print("pre_condition_196 SAT")
		print('x = -74')
		print('y = -1')
		print('a = -300765')
		print('z = -16')
		print('b = -409319')
		print('c = -8193/2')
		exit(0)
	
	
	if pre_condition_197(a=a,b=b,c=c)==True:
		print("pre_condition_197 SAT")
		print('x = -74')
		print('y = -1')
		print('a = -300765')
		print('z = -16')
		print('b = -409319')
		print('c = -8193/2')
		exit(0)
	
	
	if pre_condition_198(a=a,b=b,c=c)==True:
		print("pre_condition_198 SAT")
		print('x = -75')
		print('y = -1')
		print('a = -405226')
		print('z = 1/2')
		print('b = -421874')
		print('c = 0')
		exit(0)
	
	
	if pre_condition_199(a=a,b=b,c=c)==True:
		print("pre_condition_199 SAT")
		print('x = -75')
		print('y = -1')
		print('a = -405226')
		print('z = 1/2')
		print('b = -421874')
		print('c = 0')
		exit(0)
	
	
	if pre_condition_200(a=a,b=b,c=c)==True:
		print("pre_condition_200 SAT")
		print('x = -75')
		print('y = -1')
		print('a = -405226')
		print('z = 1/2')
		print('b = -421874')
		print('c = 0')
		exit(0)
	
	
	if pre_condition_201(a=a,b=b,c=c)==True:
		print("pre_condition_201 SAT")
		print('x = -76')
		print('y = -1')
		print('a = -405226')
		print('z = -14')
		print('b = -441719')
		print('c = -5489/2')
		exit(0)
	
	
	if pre_condition_202(a=a,b=b,c=c)==True:
		print("pre_condition_202 SAT")
		print('x = -76')
		print('y = -1')
		print('a = -405226')
		print('z = -14')
		print('b = -441719')
		print('c = -5489/2')
		exit(0)
	
	
	if pre_condition_203(a=a,b=b,c=c)==True:
		print("pre_condition_203 SAT")
		print('x = -76')
		print('y = -1')
		print('a = -405226')
		print('z = -14')
		print('b = -441719')
		print('c = -5489/2')
		exit(0)
	
	
	if pre_condition_204(a=a,b=b,c=c)==True:
		print("pre_condition_204 SAT")
		print('x = -77')
		print('y = -1')
		print('a = -405226')
		print('z = -16')
		print('b = -460628')
		print('c = -8193/2')
		exit(0)
	
	
	if pre_condition_205(a=a,b=b,c=c)==True:
		print("pre_condition_205 SAT")
		print('x = -77')
		print('y = -1')
		print('a = -405226')
		print('z = -16')
		print('b = -460628')
		print('c = -8193/2')
		exit(0)
	
	
	if pre_condition_206(a=a,b=b,c=c)==True:
		print("pre_condition_206 SAT")
		print('x = -77')
		print('y = -1')
		print('a = -405226')
		print('z = -16')
		print('b = -460628')
		print('c = -8193/2')
		exit(0)
	
	
	if pre_condition_207(a=a,b=b,c=c)==True:
		print("pre_condition_207 SAT")
		print('x = -78')
		print('y = -1')
		print('a = -166377')
		print('z = -17')
		print('b = -479464')
		print('c = -9827/2')
		exit(0)
	
	
	if pre_condition_208(a=a,b=b,c=c)==True:
		print("pre_condition_208 SAT")
		print('x = -78')
		print('y = -1')
		print('a = -166377')
		print('z = -17')
		print('b = -479464')
		print('c = -9827/2')
		exit(0)
	
	
	if pre_condition_209(a=a,b=b,c=c)==True:
		print("pre_condition_209 SAT")
		print('x = -78')
		print('y = -1')
		print('a = -166377')
		print('z = -17')
		print('b = -479464')
		print('c = -9827/2')
		exit(0)
	
	
	if pre_condition_210(a=a,b=b,c=c)==True:
		print("pre_condition_210 SAT")
		print('x = -79')
		print('y = -1')
		print('a = -474554')
		print('z = -1')
		print('b = -493039')
		print('c = -3/2')
		exit(0)
	
	
	if pre_condition_211(a=a,b=b,c=c)==True:
		print("pre_condition_211 SAT")
		print('x = -79')
		print('y = -1')
		print('a = -474554')
		print('z = -1')
		print('b = -493039')
		print('c = -3/2')
		exit(0)
	
	
	if pre_condition_212(a=a,b=b,c=c)==True:
		print("pre_condition_212 SAT")
		print('x = -79')
		print('y = -1')
		print('a = -474554')
		print('z = -1')
		print('b = -493039')
		print('c = -3/2')
		exit(0)
	
	
	if pre_condition_213(a=a,b=b,c=c)==True:
		print("pre_condition_213 SAT")
		print('x = -80')
		print('y = -1')
		print('a = -474554')
		print('z = -17')
		print('b = -516912')
		print('c = -9827/2')
		exit(0)
	
	
	if pre_condition_214(a=a,b=b,c=c)==True:
		print("pre_condition_214 SAT")
		print('x = -80')
		print('y = -1')
		print('a = -474554')
		print('z = -17')
		print('b = -516912')
		print('c = -9827/2')
		exit(0)
	
	
	if pre_condition_215(a=a,b=b,c=c)==True:
		print("pre_condition_215 SAT")
		print('x = -80')
		print('y = -1')
		print('a = -474554')
		print('z = -17')
		print('b = -516912')
		print('c = -9827/2')
		exit(0)
	
	
	if pre_condition_216(a=a,b=b,c=c)==True:
		print("pre_condition_216 SAT")
		print('x = -81')
		print('y = -1')
		print('a = -531441')
		print('z = -10')
		print('b = -532440')
		print('c = -2001/2')
		exit(0)
	
	
	if pre_condition_217(a=a,b=b,c=c)==True:
		print("pre_condition_217 SAT")
		print('x = -81')
		print('y = -1')
		print('a = -531441')
		print('z = -10')
		print('b = -532440')
		print('c = -2001/2')
		exit(0)
	
	
	if pre_condition_218(a=a,b=b,c=c)==True:
		print("pre_condition_218 SAT")
		print('x = -81')
		print('y = -1')
		print('a = -531441')
		print('z = -10')
		print('b = -532440')
		print('c = -2001/2')
		exit(0)
	
	
	if pre_condition_219(a=a,b=b,c=c)==True:
		print("pre_condition_219 SAT")
		print('x = -82')
		print('y = -1')
		print('a = -512002')
		print('z = -17')
		print('b = -556280')
		print('c = -9827/2')
		exit(0)
	
	
	if pre_condition_220(a=a,b=b,c=c)==True:
		print("pre_condition_220 SAT")
		print('x = -82')
		print('y = -1')
		print('a = -512002')
		print('z = -17')
		print('b = -556280')
		print('c = -9827/2')
		exit(0)
	
	
	if pre_condition_221(a=a,b=b,c=c)==True:
		print("pre_condition_221 SAT")
		print('x = -82')
		print('y = -1')
		print('a = -512002')
		print('z = -17')
		print('b = -556280')
		print('c = -9827/2')
		exit(0)
	
	
	if pre_condition_222(a=a,b=b,c=c)==True:
		print("pre_condition_222 SAT")
		print('x = -83')
		print('y = -1')
		print('a = -438978')
		print('z = -18')
		print('b = -577618')
		print('c = -11665/2')
		exit(0)
	
	
	if pre_condition_223(a=a,b=b,c=c)==True:
		print("pre_condition_223 SAT")
		print('x = -83')
		print('y = -1')
		print('a = -438978')
		print('z = -18')
		print('b = -577618')
		print('c = -11665/2')
		exit(0)
	
	
	if pre_condition_224(a=a,b=b,c=c)==True:
		print("pre_condition_224 SAT")
		print('x = -83')
		print('y = -1')
		print('a = -438978')
		print('z = -18')
		print('b = -577618')
		print('c = -11665/2')
		exit(0)
	
	
	if pre_condition_225(a=a,b=b,c=c)==True:
		print("pre_condition_225 SAT")
		print('x = -84')
		print('y = -1')
		print('a = -571789')
		print('z = 1/2')
		print('b = -592703')
		print('c = 0')
		exit(0)
	
	
	if pre_condition_226(a=a,b=b,c=c)==True:
		print("pre_condition_226 SAT")
		print('x = -84')
		print('y = -1')
		print('a = -571789')
		print('z = 1/2')
		print('b = -592703')
		print('c = 0')
		exit(0)
	
	
	if pre_condition_227(a=a,b=b,c=c)==True:
		print("pre_condition_227 SAT")
		print('x = -84')
		print('y = -1')
		print('a = -571789')
		print('z = 1/2')
		print('b = -592703')
		print('c = 0')
		exit(0)
	
	
	if pre_condition_228(a=a,b=b,c=c)==True:
		print("pre_condition_228 SAT")
		print('x = -85')
		print('y = -1')
		print('a = -571789')
		print('z = -8')
		print('b = -614636')
		print('c = -1025/2')
		exit(0)
	
	
	if pre_condition_229(a=a,b=b,c=c)==True:
		print("pre_condition_229 SAT")
		print('x = -85')
		print('y = -1')
		print('a = -571789')
		print('z = -8')
		print('b = -614636')
		print('c = -1025/2')
		exit(0)
	
	
	if pre_condition_230(a=a,b=b,c=c)==True:
		print("pre_condition_230 SAT")
		print('x = -85')
		print('y = -1')
		print('a = -571789')
		print('z = -8')
		print('b = -614636')
		print('c = -1025/2')
		exit(0)
	
	
	if pre_condition_231(a=a,b=b,c=c)==True:
		print("pre_condition_231 SAT")
		print('x = -86')
		print('y = -1')
		print('a = -571789')
		print('z = -17')
		print('b = -640968')
		print('c = -9827/2')
		exit(0)
	
	
	if pre_condition_232(a=a,b=b,c=c)==True:
		print("pre_condition_232 SAT")
		print('x = -86')
		print('y = -1')
		print('a = -571789')
		print('z = -17')
		print('b = -640968')
		print('c = -9827/2')
		exit(0)
	
	
	if pre_condition_233(a=a,b=b,c=c)==True:
		print("pre_condition_233 SAT")
		print('x = -86')
		print('y = -1')
		print('a = -571789')
		print('z = -17')
		print('b = -640968')
		print('c = -9827/2')
		exit(0)
	
	
	if pre_condition_234(a=a,b=b,c=c)==True:
		print("pre_condition_234 SAT")
		print('x = -87')
		print('y = -1')
		print('a = -571789')
		print('z = -18')
		print('b = -664334')
		print('c = -11665/2')
		exit(0)
	
	
	if pre_condition_235(a=a,b=b,c=c)==True:
		print("pre_condition_235 SAT")
		print('x = -87')
		print('y = -1')
		print('a = -571789')
		print('z = -18')
		print('b = -664334')
		print('c = -11665/2')
		exit(0)
	
	
	if pre_condition_236(a=a,b=b,c=c)==True:
		print("pre_condition_236 SAT")
		print('x = -87')
		print('y = -1')
		print('a = -571789')
		print('z = -18')
		print('b = -664334')
		print('c = -11665/2')
		exit(0)
	
	
	if pre_condition_237(a=a,b=b,c=c)==True:
		print("pre_condition_237 SAT")
		print('x = -88')
		print('y = -1')
		print('a = -262146')
		print('z = -19')
		print('b = -688330')
		print('c = -13719/2')
		exit(0)
	
	
	if pre_condition_238(a=a,b=b,c=c)==True:
		print("pre_condition_238 SAT")
		print('x = -88')
		print('y = -1')
		print('a = -262146')
		print('z = -19')
		print('b = -688330')
		print('c = -13719/2')
		exit(0)
	
	
	if pre_condition_239(a=a,b=b,c=c)==True:
		print("pre_condition_239 SAT")
		print('x = -88')
		print('y = -1')
		print('a = -262146')
		print('z = -19')
		print('b = -688330')
		print('c = -13719/2')
		exit(0)
	
	
	if pre_condition_240(a=a,b=b,c=c)==True:
		print("pre_condition_240 SAT")
		print('x = -89')
		print('y = -1')
		print('a = -512002')
		print('z = -20')
		print('b = -712968')
		print('c = -16001/2')
		exit(0)
	
	
	if pre_condition_241(a=a,b=b,c=c)==True:
		print("pre_condition_241 SAT")
		print('x = -89')
		print('y = -1')
		print('a = -512002')
		print('z = -20')
		print('b = -712968')
		print('c = -16001/2')
		exit(0)
	
	
	if pre_condition_242(a=a,b=b,c=c)==True:
		print("pre_condition_242 SAT")
		print('x = -89')
		print('y = -1')
		print('a = -512002')
		print('z = -20')
		print('b = -712968')
		print('c = -16001/2')
		exit(0)
	
	
	if pre_condition_243(a=a,b=b,c=c)==True:
		print("pre_condition_243 SAT")
		print('x = -90')
		print('y = -1')
		print('a = -531443')
		print('z = -21')
		print('b = -738260')
		print('c = -18523/2')
		exit(0)
	
	
	if pre_condition_244(a=a,b=b,c=c)==True:
		print("pre_condition_244 SAT")
		print('x = -90')
		print('y = -1')
		print('a = -531443')
		print('z = -21')
		print('b = -738260')
		print('c = -18523/2')
		exit(0)
	
	
	if pre_condition_245(a=a,b=b,c=c)==True:
		print("pre_condition_245 SAT")
		print('x = -90')
		print('y = -1')
		print('a = -531443')
		print('z = -21')
		print('b = -738260')
		print('c = -18523/2')
		exit(0)
	
	
	if pre_condition_246(a=a,b=b,c=c)==True:
		print("pre_condition_246 SAT")
		print('x = -91')
		print('y = -1')
		print('a = -531443')
		print('z = -22')
		print('b = -764218')
		print('c = -21297/2')
		exit(0)
	
	
	if pre_condition_247(a=a,b=b,c=c)==True:
		print("pre_condition_247 SAT")
		print('x = -91')
		print('y = -1')
		print('a = -531443')
		print('z = -22')
		print('b = -764218')
		print('c = -21297/2')
		exit(0)
	
	
	if pre_condition_248(a=a,b=b,c=c)==True:
		print("pre_condition_248 SAT")
		print('x = -91')
		print('y = -1')
		print('a = -531443')
		print('z = -22')
		print('b = -764218')
		print('c = -21297/2')
		exit(0)
	
	
	if pre_condition_249(a=a,b=b,c=c)==True:
		print("pre_condition_249 SAT")
		print('x = -92')
		print('y = -1')
		print('a = -216002')
		print('z = -23')
		print('b = -790854')
		print('c = -24335/2')
		exit(0)
	
	
	if pre_condition_250(a=a,b=b,c=c)==True:
		print("pre_condition_250 SAT")
		print('x = -92')
		print('y = -1')
		print('a = -216002')
		print('z = -23')
		print('b = -790854')
		print('c = -24335/2')
		exit(0)
	
	
	if pre_condition_251(a=a,b=b,c=c)==True:
		print("pre_condition_251 SAT")
		print('x = -92')
		print('y = -1')
		print('a = -216002')
		print('z = -23')
		print('b = -790854')
		print('c = -24335/2')
		exit(0)
	
	
	if pre_condition_252(a=a,b=b,c=c)==True:
		print("pre_condition_252 SAT")
		print('x = -93')
		print('y = -1')
		print('a = -571789')
		print('z = -24')
		print('b = -818180')
		print('c = -27649/2')
		exit(0)
	
	
	if pre_condition_253(a=a,b=b,c=c)==True:
		print("pre_condition_253 SAT")
		print('x = -93')
		print('y = -1')
		print('a = -571789')
		print('z = -24')
		print('b = -818180')
		print('c = -27649/2')
		exit(0)
	
	
	if pre_condition_254(a=a,b=b,c=c)==True:
		print("pre_condition_254 SAT")
		print('x = -93')
		print('y = -1')
		print('a = -571789')
		print('z = -24')
		print('b = -818180')
		print('c = -27649/2')
		exit(0)
	
	
	if pre_condition_255(a=a,b=b,c=c)==True:
		print("pre_condition_255 SAT")
		print('x = -94')
		print('y = -1')
		print('a = -68923')
		print('z = -25')
		print('b = -846208')
		print('c = -31251/2')
		exit(0)
	
	
	if pre_condition_256(a=a,b=b,c=c)==True:
		print("pre_condition_256 SAT")
		print('x = -94')
		print('y = -1')
		print('a = -68923')
		print('z = -25')
		print('b = -846208')
		print('c = -31251/2')
		exit(0)
	
	
	if pre_condition_257(a=a,b=b,c=c)==True:
		print("pre_condition_257 SAT")
		print('x = -94')
		print('y = -1')
		print('a = -68923')
		print('z = -25')
		print('b = -846208')
		print('c = -31251/2')
		exit(0)
	
	
	if pre_condition_258(a=a,b=b,c=c)==True:
		print("pre_condition_258 SAT")
		print('x = -95')
		print('y = -1')
		print('a = -438978')
		print('z = -26')
		print('b = -874950')
		print('c = -35153/2')
		exit(0)
	
	
	if pre_condition_259(a=a,b=b,c=c)==True:
		print("pre_condition_259 SAT")
		print('x = -95')
		print('y = -1')
		print('a = -438978')
		print('z = -26')
		print('b = -874950')
		print('c = -35153/2')
		exit(0)
	
	
	if pre_condition_260(a=a,b=b,c=c)==True:
		print("pre_condition_260 SAT")
		print('x = -95')
		print('y = -1')
		print('a = -438978')
		print('z = -26')
		print('b = -874950')
		print('c = -35153/2')
		exit(0)
	
	
	if pre_condition_261(a=a,b=b,c=c)==True:
		print("pre_condition_261 SAT")
		print('x = -96')
		print('y = -1')
		print('a = -531443')
		print('z = -27')
		print('b = -904418')
		print('c = -39367/2')
		exit(0)
	
	
	if pre_condition_262(a=a,b=b,c=c)==True:
		print("pre_condition_262 SAT")
		print('x = -96')
		print('y = -1')
		print('a = -531443')
		print('z = -27')
		print('b = -904418')
		print('c = -39367/2')
		exit(0)
	
	
	if pre_condition_263(a=a,b=b,c=c)==True:
		print("pre_condition_263 SAT")
		print('x = -96')
		print('y = -1')
		print('a = -531443')
		print('z = -27')
		print('b = -904418')
		print('c = -39367/2')
		exit(0)
	
	
	if pre_condition_264(a=a,b=b,c=c)==True:
		print("pre_condition_264 SAT")
		print('x = -97')
		print('y = -1')
		print('a = -551370')
		print('z = -28')
		print('b = -934624')
		print('c = -43905/2')
		exit(0)
	
	
	if pre_condition_265(a=a,b=b,c=c)==True:
		print("pre_condition_265 SAT")
		print('x = -97')
		print('y = -1')
		print('a = -551370')
		print('z = -28')
		print('b = -934624')
		print('c = -43905/2')
		exit(0)
	
	
	if pre_condition_266(a=a,b=b,c=c)==True:
		print("pre_condition_266 SAT")
		print('x = -97')
		print('y = -1')
		print('a = -551370')
		print('z = -28')
		print('b = -934624')
		print('c = -43905/2')
		exit(0)
	
	
	if pre_condition_267(a=a,b=b,c=c)==True:
		print("pre_condition_267 SAT")
		print('x = -98')
		print('y = -1')
		print('a = -941192')
		print('z = -26')
		print('b = -958767')
		print('c = -35153/2')
		exit(0)
	
	
	if pre_condition_268(a=a,b=b,c=c)==True:
		print("pre_condition_268 SAT")
		print('x = -98')
		print('y = -1')
		print('a = -941192')
		print('z = -26')
		print('b = -958767')
		print('c = -35153/2')
		exit(0)
	
	
	if pre_condition_269(a=a,b=b,c=c)==True:
		print("pre_condition_269 SAT")
		print('x = -98')
		print('y = -1')
		print('a = -941192')
		print('z = -26')
		print('b = -958767')
		print('c = -35153/2')
		exit(0)
	
	
	if pre_condition_270(a=a,b=b,c=c)==True:
		print("pre_condition_270 SAT")
		print('x = -99')
		print('y = -1')
		print('a = -912675')
		print('z = -28')
		print('b = -992250')
		print('c = -43905/2')
		exit(0)
	
	
	if pre_condition_271(a=a,b=b,c=c)==True:
		print("pre_condition_271 SAT")
		print('x = -99')
		print('y = -1')
		print('a = -912675')
		print('z = -28')
		print('b = -992250')
		print('c = -43905/2')
		exit(0)
	
	
	if pre_condition_272(a=a,b=b,c=c)==True:
		print("pre_condition_272 SAT")
		print('x = -99')
		print('y = -1')
		print('a = -912675')
		print('z = -28')
		print('b = -992250')
		print('c = -43905/2')
		exit(0)
	
	
	if pre_condition_273(a=a,b=b,c=c)==True:
		print("pre_condition_273 SAT")
		print('x = -100')
		print('y = -1')
		print('a = -571789')
		print('z = -29')
		print('b = -1024388')
		print('c = -48779/2')
		exit(0)
	
	
	if pre_condition_274(a=a,b=b,c=c)==True:
		print("pre_condition_274 SAT")
		print('x = -100')
		print('y = -1')
		print('a = -571789')
		print('z = -29')
		print('b = -1024388')
		print('c = -48779/2')
		exit(0)
	
	
	if pre_condition_275(a=a,b=b,c=c)==True:
		print("pre_condition_275 SAT")
		print('x = -100')
		print('y = -1')
		print('a = -571789')
		print('z = -29')
		print('b = -1024388')
		print('c = -48779/2')
		exit(0)
	
	
	if pre_condition_276(a=a,b=b,c=c)==True:
		print("pre_condition_276 SAT")
		print('x = -101')
		print('y = -1')
		print('a = -592706')
		print('z = -30')
		print('b = -1057300')
		print('c = -54001/2')
		exit(0)
	
	
	if pre_condition_277(a=a,b=b,c=c)==True:
		print("pre_condition_277 SAT")
		print('x = -101')
		print('y = -1')
		print('a = -592706')
		print('z = -30')
		print('b = -1057300')
		print('c = -54001/2')
		exit(0)
	
	
	if pre_condition_278(a=a,b=b,c=c)==True:
		print("pre_condition_278 SAT")
		print('x = -101')
		print('y = -1')
		print('a = -592706')
		print('z = -30')
		print('b = -1057300')
		print('c = -54001/2')
		exit(0)
	
	
	if pre_condition_279(a=a,b=b,c=c)==True:
		print("pre_condition_279 SAT")
		print('x = -102')
		print('y = -1')
		print('a = -658505')
		print('z = -31')
		print('b = -1090998')
		print('c = -59583/2')
		exit(0)
	
	
	if pre_condition_280(a=a,b=b,c=c)==True:
		print("pre_condition_280 SAT")
		print('x = -102')
		print('y = -1')
		print('a = -658505')
		print('z = -31')
		print('b = -1090998')
		print('c = -59583/2')
		exit(0)
	
	
	if pre_condition_281(a=a,b=b,c=c)==True:
		print("pre_condition_281 SAT")
		print('x = -102')
		print('y = -1')
		print('a = -658505')
		print('z = -31')
		print('b = -1090998')
		print('c = -59583/2')
		exit(0)
	
	
	if pre_condition_282(a=a,b=b,c=c)==True:
		print("pre_condition_282 SAT")
		print('x = -103')
		print('y = -1')
		print('a = -1092727')
		print('z = -19')
		print('b = -1068068')
		print('c = -13719/2')
		exit(0)
	
	
	if pre_condition_283(a=a,b=b,c=c)==True:
		print("pre_condition_283 SAT")
		print('x = -103')
		print('y = -1')
		print('a = -1092727')
		print('z = -19')
		print('b = -1068068')
		print('c = -13719/2')
		exit(0)
	
	
	if pre_condition_284(a=a,b=b,c=c)==True:
		print("pre_condition_284 SAT")
		print('x = -103')
		print('y = -1')
		print('a = -1092727')
		print('z = -19')
		print('b = -1068068')
		print('c = -13719/2')
		exit(0)
	
	
	if pre_condition_285(a=a,b=b,c=c)==True:
		print("pre_condition_285 SAT")
		print('x = -104')
		print('y = -1')
		print('a = -1061210')
		print('z = -31')
		print('b = -1154654')
		print('c = -59583/2')
		exit(0)
	
	
	if pre_condition_286(a=a,b=b,c=c)==True:
		print("pre_condition_286 SAT")
		print('x = -104')
		print('y = -1')
		print('a = -1061210')
		print('z = -31')
		print('b = -1154654')
		print('c = -59583/2')
		exit(0)
	
	
	if pre_condition_287(a=a,b=b,c=c)==True:
		print("pre_condition_287 SAT")
		print('x = -104')
		print('y = -1')
		print('a = -1061210')
		print('z = -31')
		print('b = -1154654')
		print('c = -59583/2')
		exit(0)
	
	
	if pre_condition_288(a=a,b=b,c=c)==True:
		print("pre_condition_288 SAT")
		print('x = -105')
		print('y = -1')
		print('a = -274627')
		print('z = -32')
		print('b = -1190392')
		print('c = -65537/2')
		exit(0)
	
	
	if pre_condition_289(a=a,b=b,c=c)==True:
		print("pre_condition_289 SAT")
		print('x = -105')
		print('y = -1')
		print('a = -274627')
		print('z = -32')
		print('b = -1190392')
		print('c = -65537/2')
		exit(0)
	
	
	if pre_condition_290(a=a,b=b,c=c)==True:
		print("pre_condition_290 SAT")
		print('x = -105')
		print('y = -1')
		print('a = -274627')
		print('z = -32')
		print('b = -1190392')
		print('c = -65537/2')
		exit(0)
	
	
	if pre_condition_291(a=a,b=b,c=c)==True:
		print("pre_condition_291 SAT")
		print('x = -106')
		print('y = -1')
		print('a = -1157627')
		print('z = -1')
		print('b = -1191016')
		print('c = -3/2')
		exit(0)
	
	
	if pre_condition_292(a=a,b=b,c=c)==True:
		print("pre_condition_292 SAT")
		print('x = -106')
		print('y = -1')
		print('a = -1157627')
		print('z = -1')
		print('b = -1191016')
		print('c = -3/2')
		exit(0)
	
	
	if pre_condition_293(a=a,b=b,c=c)==True:
		print("pre_condition_293 SAT")
		print('x = -106')
		print('y = -1')
		print('a = -1157627')
		print('z = -1')
		print('b = -1191016')
		print('c = -3/2')
		exit(0)
	
	
	if pre_condition_294(a=a,b=b,c=c)==True:
		print("pre_condition_294 SAT")
		print('x = -107')
		print('y = -1')
		print('a = -1157627')
		print('z = -32')
		print('b = -1257810')
		print('c = -65537/2')
		exit(0)
	
	
	if pre_condition_295(a=a,b=b,c=c)==True:
		print("pre_condition_295 SAT")
		print('x = -107')
		print('y = -1')
		print('a = -1157627')
		print('z = -32')
		print('b = -1257810')
		print('c = -65537/2')
		exit(0)
	
	
	if pre_condition_296(a=a,b=b,c=c)==True:
		print("pre_condition_296 SAT")
		print('x = -107')
		print('y = -1')
		print('a = -1157627')
		print('z = -32')
		print('b = -1257810')
		print('c = -65537/2')
		exit(0)
	
	
	if pre_condition_297(a=a,b=b,c=c)==True:
		print("pre_condition_297 SAT")
		print('x = -108')
		print('y = -1')
		print('a = -636058')
		print('z = -33')
		print('b = -1295648')
		print('c = -71875/2')
		exit(0)
	
	
	if pre_condition_298(a=a,b=b,c=c)==True:
		print("pre_condition_298 SAT")
		print('x = -108')
		print('y = -1')
		print('a = -636058')
		print('z = -33')
		print('b = -1295648')
		print('c = -71875/2')
		exit(0)
	
	
	if pre_condition_299(a=a,b=b,c=c)==True:
		print("pre_condition_299 SAT")
		print('x = -108')
		print('y = -1')
		print('a = -636058')
		print('z = -33')
		print('b = -1295648')
		print('c = -71875/2')
		exit(0)
	
	
	if pre_condition_300(a=a,b=b,c=c)==True:
		print("pre_condition_300 SAT")
		print('x = -109')
		print('y = -1')
		print('a = -1061210')
		print('z = -34')
		print('b = -1334332')
		print('c = -78609/2')
		exit(0)
	
	
	if pre_condition_301(a=a,b=b,c=c)==True:
		print("pre_condition_301 SAT")
		print('x = -109')
		print('y = -1')
		print('a = -1061210')
		print('z = -34')
		print('b = -1334332')
		print('c = -78609/2')
		exit(0)
	
	
	if pre_condition_302(a=a,b=b,c=c)==True:
		print("pre_condition_302 SAT")
		print('x = -109')
		print('y = -1')
		print('a = -1061210')
		print('z = -34')
		print('b = -1334332')
		print('c = -78609/2')
		exit(0)
	
	
	if pre_condition_303(a=a,b=b,c=c)==True:
		print("pre_condition_303 SAT")
		print('x = -110')
		print('y = -1')
		print('a = -1331000')
		print('z = -2')
		print('b = -1295038')
		print('c = -17/2')
		exit(0)
	
	
	if pre_condition_304(a=a,b=b,c=c)==True:
		print("pre_condition_304 SAT")
		print('x = -110')
		print('y = -1')
		print('a = -1331000')
		print('z = -2')
		print('b = -1295038')
		print('c = -17/2')
		exit(0)
	
	
	if pre_condition_305(a=a,b=b,c=c)==True:
		print("pre_condition_305 SAT")
		print('x = -110')
		print('y = -1')
		print('a = -1331000')
		print('z = -2')
		print('b = -1295038')
		print('c = -17/2')
		exit(0)
	
	
	if pre_condition_306(a=a,b=b,c=c)==True:
		print("pre_condition_306 SAT")
		print('x = -111')
		print('y = -1')
		print('a = -1295031')
		print('z = -26')
		print('b = -1385206')
		print('c = -35153/2')
		exit(0)
	
	
	if pre_condition_307(a=a,b=b,c=c)==True:
		print("pre_condition_307 SAT")
		print('x = -111')
		print('y = -1')
		print('a = -1295031')
		print('z = -26')
		print('b = -1385206')
		print('c = -35153/2')
		exit(0)
	
	
	if pre_condition_308(a=a,b=b,c=c)==True:
		print("pre_condition_308 SAT")
		print('x = -111')
		print('y = -1')
		print('a = -1295031')
		print('z = -26')
		print('b = -1385206')
		print('c = -35153/2')
		exit(0)
	
	
	if pre_condition_309(a=a,b=b,c=c)==True:
		print("pre_condition_309 SAT")
		print('x = -112')
		print('y = -1')
		print('a = -1295031')
		print('z = -33')
		print('b = -1440864')
		print('c = -71875/2')
		exit(0)
	
	
	if pre_condition_310(a=a,b=b,c=c)==True:
		print("pre_condition_310 SAT")
		print('x = -112')
		print('y = -1')
		print('a = -1295031')
		print('z = -33')
		print('b = -1440864')
		print('c = -71875/2')
		exit(0)
	
	
	if pre_condition_311(a=a,b=b,c=c)==True:
		print("pre_condition_311 SAT")
		print('x = -112')
		print('y = -1')
		print('a = -1295031')
		print('z = -33')
		print('b = -1440864')
		print('c = -71875/2')
		exit(0)
	
	
	if pre_condition_312(a=a,b=b,c=c)==True:
		print("pre_condition_312 SAT")
		print('x = -113')
		print('y = -1')
		print('a = -1295031')
		print('z = -34')
		print('b = -1482200')
		print('c = -78609/2')
		exit(0)
	
	
	if pre_condition_313(a=a,b=b,c=c)==True:
		print("pre_condition_313 SAT")
		print('x = -113')
		print('y = -1')
		print('a = -1295031')
		print('z = -34')
		print('b = -1482200')
		print('c = -78609/2')
		exit(0)
	
	
	if pre_condition_314(a=a,b=b,c=c)==True:
		print("pre_condition_314 SAT")
		print('x = -113')
		print('y = -1')
		print('a = -1295031')
		print('z = -34')
		print('b = -1482200')
		print('c = -78609/2')
		exit(0)
	
	
	if pre_condition_315(a=a,b=b,c=c)==True:
		print("pre_condition_315 SAT")
		print('x = -114')
		print('y = -1')
		print('a = -1442899')
		print('z = 1/2')
		print('b = -1481543')
		print('c = 0')
		exit(0)
	
	
	if pre_condition_316(a=a,b=b,c=c)==True:
		print("pre_condition_316 SAT")
		print('x = -114')
		print('y = -1')
		print('a = -1442899')
		print('z = 1/2')
		print('b = -1481543')
		print('c = 0')
		exit(0)
	
	
	if pre_condition_317(a=a,b=b,c=c)==True:
		print("pre_condition_317 SAT")
		print('x = -114')
		print('y = -1')
		print('a = -1442899')
		print('z = 1/2')
		print('b = -1481543')
		print('c = 0')
		exit(0)
	
	
	if pre_condition_318(a=a,b=b,c=c)==True:
		print("pre_condition_318 SAT")
		print('x = -115')
		print('y = -1')
		print('a = -1442899')
		print('z = -1')
		print('b = -1520875')
		print('c = -3/2')
		exit(0)
	
	
	if pre_condition_319(a=a,b=b,c=c)==True:
		print("pre_condition_319 SAT")
		print('x = -115')
		print('y = -1')
		print('a = -1442899')
		print('z = -1')
		print('b = -1520875')
		print('c = -3/2')
		exit(0)
	
	
	if pre_condition_320(a=a,b=b,c=c)==True:
		print("pre_condition_320 SAT")
		print('x = -115')
		print('y = -1')
		print('a = -1442899')
		print('z = -1')
		print('b = -1520875')
		print('c = -3/2')
		exit(0)
	
	
	if pre_condition_321(a=a,b=b,c=c)==True:
		print("pre_condition_321 SAT")
		print('x = -116')
		print('y = -1')
		print('a = -1442899')
		print('z = -34')
		print('b = -1600199')
		print('c = -78609/2')
		exit(0)
	
	
	if pre_condition_322(a=a,b=b,c=c)==True:
		print("pre_condition_322 SAT")
		print('x = -116')
		print('y = -1')
		print('a = -1442899')
		print('z = -34')
		print('b = -1600199')
		print('c = -78609/2')
		exit(0)
	
	
	if pre_condition_323(a=a,b=b,c=c)==True:
		print("pre_condition_323 SAT")
		print('x = -116')
		print('y = -1')
		print('a = -1442899')
		print('z = -34')
		print('b = -1600199')
		print('c = -78609/2')
		exit(0)
	
	
	if pre_condition_324(a=a,b=b,c=c)==True:
		print("pre_condition_324 SAT")
		print('x = -117')
		print('y = -1')
		print('a = -1601613')
		print('z = -34')
		print('b = -1600201')
		print('c = -78609/2')
		exit(0)
	
	
	if pre_condition_325(a=a,b=b,c=c)==True:
		print("pre_condition_325 SAT")
		print('x = -117')
		print('y = -1')
		print('a = -1601613')
		print('z = -34')
		print('b = -1600201')
		print('c = -78609/2')
		exit(0)
	
	
	if pre_condition_326(a=a,b=b,c=c)==True:
		print("pre_condition_326 SAT")
		print('x = -117')
		print('y = -1')
		print('a = -1601613')
		print('z = -34')
		print('b = -1600201')
		print('c = -78609/2')
		exit(0)
	
	
	if pre_condition_327(a=a,b=b,c=c)==True:
		print("pre_condition_327 SAT")
		print('x = -118')
		print('y = -1')
		print('a = -1442899')
		print('z = -35')
		print('b = -1685906')
		print('c = -85751/2')
		exit(0)
	
	
	if pre_condition_328(a=a,b=b,c=c)==True:
		print("pre_condition_328 SAT")
		print('x = -118')
		print('y = -1')
		print('a = -1442899')
		print('z = -35')
		print('b = -1685906')
		print('c = -85751/2')
		exit(0)
	
	
	if pre_condition_329(a=a,b=b,c=c)==True:
		print("pre_condition_329 SAT")
		print('x = -118')
		print('y = -1')
		print('a = -1442899')
		print('z = -35')
		print('b = -1685906')
		print('c = -85751/2')
		exit(0)
	
	
	if pre_condition_330(a=a,b=b,c=c)==True:
		print("pre_condition_330 SAT")
		print('x = -119')
		print('y = -1')
		print('a = -1643034')
		print('z = 1/2')
		print('b = -1685158')
		print('c = 0')
		exit(0)
	
	
	if pre_condition_331(a=a,b=b,c=c)==True:
		print("pre_condition_331 SAT")
		print('x = -119')
		print('y = -1')
		print('a = -1643034')
		print('z = 1/2')
		print('b = -1685158')
		print('c = 0')
		exit(0)
	
	
	if pre_condition_332(a=a,b=b,c=c)==True:
		print("pre_condition_332 SAT")
		print('x = -119')
		print('y = -1')
		print('a = -1643034')
		print('z = 1/2')
		print('b = -1685158')
		print('c = 0')
		exit(0)
	
	
	if pre_condition_333(a=a,b=b,c=c)==True:
		print("pre_condition_333 SAT")
		print('x = -120')
		print('y = -1')
		print('a = -1643034')
		print('z = -35')
		print('b = -1770874')
		print('c = -85751/2')
		exit(0)
	
	
	if pre_condition_334(a=a,b=b,c=c)==True:
		print("pre_condition_334 SAT")
		print('x = -120')
		print('y = -1')
		print('a = -1643034')
		print('z = -35')
		print('b = -1770874')
		print('c = -85751/2')
		exit(0)
	
	
	if pre_condition_335(a=a,b=b,c=c)==True:
		print("pre_condition_335 SAT")
		print('x = -120')
		print('y = -1')
		print('a = -1643034')
		print('z = -35')
		print('b = -1770874')
		print('c = -85751/2')
		exit(0)
	
	
	if pre_condition_336(a=a,b=b,c=c)==True:
		print("pre_condition_336 SAT")
		print('x = -121')
		print('y = -1')
		print('a = -1728002')
		print('z = -1')
		print('b = -1771561')
		print('c = -3/2')
		exit(0)
	
	
	if pre_condition_337(a=a,b=b,c=c)==True:
		print("pre_condition_337 SAT")
		print('x = -121')
		print('y = -1')
		print('a = -1728002')
		print('z = -1')
		print('b = -1771561')
		print('c = -3/2')
		exit(0)
	
	
	if pre_condition_338(a=a,b=b,c=c)==True:
		print("pre_condition_338 SAT")
		print('x = -121')
		print('y = -1')
		print('a = -1728002')
		print('z = -1')
		print('b = -1771561')
		print('c = -3/2')
		exit(0)
	
	
	if pre_condition_339(a=a,b=b,c=c)==True:
		print("pre_condition_339 SAT")
		print('x = -122')
		print('y = -1')
		print('a = -1728002')
		print('z = -2')
		print('b = -1815855')
		print('c = -17/2')
		exit(0)
	
	
	if pre_condition_340(a=a,b=b,c=c)==True:
		print("pre_condition_340 SAT")
		print('x = -122')
		print('y = -1')
		print('a = -1728002')
		print('z = -2')
		print('b = -1815855')
		print('c = -17/2')
		exit(0)
	
	
	if pre_condition_341(a=a,b=b,c=c)==True:
		print("pre_condition_341 SAT")
		print('x = -122')
		print('y = -1')
		print('a = -1728002')
		print('z = -2')
		print('b = -1815855')
		print('c = -17/2')
		exit(0)
	
	
	if pre_condition_342(a=a,b=b,c=c)==True:
		print("pre_condition_342 SAT")
		print('x = -123')
		print('y = -1')
		print('a = -1728002')
		print('z = -3')
		print('b = -1860893')
		print('c = -55/2')
		exit(0)
	
	
	if pre_condition_343(a=a,b=b,c=c)==True:
		print("pre_condition_343 SAT")
		print('x = -123')
		print('y = -1')
		print('a = -1728002')
		print('z = -3')
		print('b = -1860893')
		print('c = -55/2')
		exit(0)
	
	
	if pre_condition_344(a=a,b=b,c=c)==True:
		print("pre_condition_344 SAT")
		print('x = -123')
		print('y = -1')
		print('a = -1728002')
		print('z = -3')
		print('b = -1860893')
		print('c = -55/2')
		exit(0)
	
	
	if pre_condition_345(a=a,b=b,c=c)==True:
		print("pre_condition_345 SAT")
		print('x = -124')
		print('y = -1')
		print('a = -1728002')
		print('z = -4')
		print('b = -1906687')
		print('c = -129/2')
		exit(0)
	
	
	if pre_condition_346(a=a,b=b,c=c)==True:
		print("pre_condition_346 SAT")
		print('x = -124')
		print('y = -1')
		print('a = -1728002')
		print('z = -4')
		print('b = -1906687')
		print('c = -129/2')
		exit(0)
	
	
	if pre_condition_347(a=a,b=b,c=c)==True:
		print("pre_condition_347 SAT")
		print('x = -124')
		print('y = -1')
		print('a = -1728002')
		print('z = -4')
		print('b = -1906687')
		print('c = -129/2')
		exit(0)
	
	
	if pre_condition_348(a=a,b=b,c=c)==True:
		print("pre_condition_348 SAT")
		print('x = -125')
		print('y = -1')
		print('a = -1728002')
		print('z = -5')
		print('b = -1953249')
		print('c = -251/2')
		exit(0)
	
	
	if pre_condition_349(a=a,b=b,c=c)==True:
		print("pre_condition_349 SAT")
		print('x = -125')
		print('y = -1')
		print('a = -1728002')
		print('z = -5')
		print('b = -1953249')
		print('c = -251/2')
		exit(0)
	
	
	if pre_condition_350(a=a,b=b,c=c)==True:
		print("pre_condition_350 SAT")
		print('x = -125')
		print('y = -1')
		print('a = -1728002')
		print('z = -5')
		print('b = -1953249')
		print('c = -251/2')
		exit(0)
	
	
	if pre_condition_351(a=a,b=b,c=c)==True:
		print("pre_condition_351 SAT")
		print('x = -126')
		print('y = -1')
		print('a = -1728002')
		print('z = -6')
		print('b = -2000591')
		print('c = -433/2')
		exit(0)
	
	
	if pre_condition_352(a=a,b=b,c=c)==True:
		print("pre_condition_352 SAT")
		print('x = -126')
		print('y = -1')
		print('a = -1728002')
		print('z = -6')
		print('b = -2000591')
		print('c = -433/2')
		exit(0)
	
	
	if pre_condition_353(a=a,b=b,c=c)==True:
		print("pre_condition_353 SAT")
		print('x = -126')
		print('y = -1')
		print('a = -1728002')
		print('z = -6')
		print('b = -2000591')
		print('c = -433/2')
		exit(0)
	
	
	if pre_condition_354(a=a,b=b,c=c)==True:
		print("pre_condition_354 SAT")
		print('x = -127')
		print('y = -1')
		print('a = -1728002')
		print('z = -7')
		print('b = -2048725')
		print('c = -687/2')
		exit(0)
	
	
	if pre_condition_355(a=a,b=b,c=c)==True:
		print("pre_condition_355 SAT")
		print('x = -127')
		print('y = -1')
		print('a = -1728002')
		print('z = -7')
		print('b = -2048725')
		print('c = -687/2')
		exit(0)
	
	
	if pre_condition_356(a=a,b=b,c=c)==True:
		print("pre_condition_356 SAT")
		print('x = -127')
		print('y = -1')
		print('a = -1728002')
		print('z = -7')
		print('b = -2048725')
		print('c = -687/2')
		exit(0)
	
	
	if pre_condition_357(a=a,b=b,c=c)==True:
		print("pre_condition_357 SAT")
		print('x = -128')
		print('y = -1')
		print('a = -1728002')
		print('z = -35')
		print('b = -2140026')
		print('c = -85751/2')
		exit(0)
	
	
	if pre_condition_358(a=a,b=b,c=c)==True:
		print("pre_condition_358 SAT")
		print('x = -128')
		print('y = -1')
		print('a = -1728002')
		print('z = -35')
		print('b = -2140026')
		print('c = -85751/2')
		exit(0)
	
	
	if pre_condition_359(a=a,b=b,c=c)==True:
		print("pre_condition_359 SAT")
		print('x = -128')
		print('y = -1')
		print('a = -1728002')
		print('z = -35')
		print('b = -2140026')
		print('c = -85751/2')
		exit(0)
	
	
	if pre_condition_360(a=a,b=b,c=c)==True:
		print("pre_condition_360 SAT")
		print('x = -129')
		print('y = -1')
		print('a = -2146689')
		print('z = -35')
		print('b = -2140028')
		print('c = -85751/2')
		exit(0)
	
	
	if pre_condition_361(a=a,b=b,c=c)==True:
		print("pre_condition_361 SAT")
		print('x = -129')
		print('y = -1')
		print('a = -2146689')
		print('z = -35')
		print('b = -2140028')
		print('c = -85751/2')
		exit(0)
	
	
	if pre_condition_362(a=a,b=b,c=c)==True:
		print("pre_condition_362 SAT")
		print('x = -129')
		print('y = -1')
		print('a = -2146689')
		print('z = -35')
		print('b = -2140028')
		print('c = -85751/2')
		exit(0)
	
	
	if pre_condition_363(a=a,b=b,c=c)==True:
		print("pre_condition_363 SAT")
		print('x = -130')
		print('y = -1')
		print('a = -1520877')
		print('z = -36')
		print('b = -2243655')
		print('c = -93313/2')
		exit(0)
	
	
	if pre_condition_364(a=a,b=b,c=c)==True:
		print("pre_condition_364 SAT")
		print('x = -130')
		print('y = -1')
		print('a = -1520877')
		print('z = -36')
		print('b = -2243655')
		print('c = -93313/2')
		exit(0)
	
	
	if pre_condition_365(a=a,b=b,c=c)==True:
		print("pre_condition_365 SAT")
		print('x = -130')
		print('y = -1')
		print('a = -1520877')
		print('z = -36')
		print('b = -2243655')
		print('c = -93313/2')
		exit(0)
	
	
	if pre_condition_366(a=a,b=b,c=c)==True:
		print("pre_condition_366 SAT")
		print('x = -131')
		print('y = -1')
		print('a = -2248091')
		print('z = -34')
		print('b = -2287394')
		print('c = -78609/2')
		exit(0)
	
	
	if pre_condition_367(a=a,b=b,c=c)==True:
		print("pre_condition_367 SAT")
		print('x = -131')
		print('y = -1')
		print('a = -2248091')
		print('z = -34')
		print('b = -2287394')
		print('c = -78609/2')
		exit(0)
	
	
	if pre_condition_368(a=a,b=b,c=c)==True:
		print("pre_condition_368 SAT")
		print('x = -131')
		print('y = -1')
		print('a = -2248091')
		print('z = -34')
		print('b = -2287394')
		print('c = -78609/2')
		exit(0)
	
	
	if pre_condition_369(a=a,b=b,c=c)==True:
		print("pre_condition_369 SAT")
		print('x = -132')
		print('y = -1')
		print('a = -2197002')
		print('z = -36')
		print('b = -2346623')
		print('c = -46656')
		exit(0)
	
	
	if pre_condition_370(a=a,b=b,c=c)==True:
		print("pre_condition_370 SAT")
		print('x = -132')
		print('y = -1')
		print('a = -2197002')
		print('z = -36')
		print('b = -2346623')
		print('c = -46656')
		exit(0)
	
	
	if pre_condition_371(a=a,b=b,c=c)==True:
		print("pre_condition_371 SAT")
		print('x = -132')
		print('y = -1')
		print('a = -2197002')
		print('z = -36')
		print('b = -2346623')
		print('c = -46656')
		exit(0)
	
	
	if pre_condition_372(a=a,b=b,c=c)==True:
		print("pre_condition_372 SAT")
		print('x = -133')
		print('y = -1')
		print('a = -2146691')
		print('z = -37')
		print('b = -2403289')
		print('c = -101307/2')
		exit(0)
	
	
	if pre_condition_373(a=a,b=b,c=c)==True:
		print("pre_condition_373 SAT")
		print('x = -133')
		print('y = -1')
		print('a = -2146691')
		print('z = -37')
		print('b = -2403289')
		print('c = -101307/2')
		exit(0)
	
	
	if pre_condition_374(a=a,b=b,c=c)==True:
		print("pre_condition_374 SAT")
		print('x = -133')
		print('y = -1')
		print('a = -2146691')
		print('z = -37')
		print('b = -2403289')
		print('c = -101307/2')
		exit(0)
	
	
	if pre_condition_375(a=a,b=b,c=c)==True:
		print("pre_condition_375 SAT")
		print('x = -134')
		print('y = -1')
		print('a = -2406104')
		print('z = -37')
		print('b = -2403291')
		print('c = -101307/2')
		exit(0)
	
	
	if pre_condition_376(a=a,b=b,c=c)==True:
		print("pre_condition_376 SAT")
		print('x = -134')
		print('y = -1')
		print('a = -2406104')
		print('z = -37')
		print('b = -2403291')
		print('c = -101307/2')
		exit(0)
	
	
	if pre_condition_377(a=a,b=b,c=c)==True:
		print("pre_condition_377 SAT")
		print('x = -134')
		print('y = -1')
		print('a = -2406104')
		print('z = -37')
		print('b = -2403291')
		print('c = -101307/2')
		exit(0)
	
	
	if pre_condition_378(a=a,b=b,c=c)==True:
		print("pre_condition_378 SAT")
		print('x = -135')
		print('y = -1')
		print('a = -2352639')
		print('z = -38')
		print('b = -2515246')
		print('c = -109745/2')
		exit(0)
	
	
	if pre_condition_379(a=a,b=b,c=c)==True:
		print("pre_condition_379 SAT")
		print('x = -135')
		print('y = -1')
		print('a = -2352639')
		print('z = -38')
		print('b = -2515246')
		print('c = -109745/2')
		exit(0)
	
	
	if pre_condition_380(a=a,b=b,c=c)==True:
		print("pre_condition_380 SAT")
		print('x = -135')
		print('y = -1')
		print('a = -2352639')
		print('z = -38')
		print('b = -2515246')
		print('c = -109745/2')
		exit(0)
	
	
	if pre_condition_381(a=a,b=b,c=c)==True:
		print("pre_condition_381 SAT")
		print('x = -136')
		print('y = -1')
		print('a = -2515456')
		print('z = -8')
		print('b = -2460888')
		print('c = -1025/2')
		exit(0)
	
	
	if pre_condition_382(a=a,b=b,c=c)==True:
		print("pre_condition_382 SAT")
		print('x = -136')
		print('y = -1')
		print('a = -2515456')
		print('z = -8')
		print('b = -2460888')
		print('c = -1025/2')
		exit(0)
	
	
	if pre_condition_383(a=a,b=b,c=c)==True:
		print("pre_condition_383 SAT")
		print('x = -136')
		print('y = -1')
		print('a = -2515456')
		print('z = -8')
		print('b = -2460888')
		print('c = -1025/2')
		exit(0)
	
	
	if pre_condition_384(a=a,b=b,c=c)==True:
		print("pre_condition_384 SAT")
		print('x = -137')
		print('y = -1')
		print('a = -2460377')
		print('z = -38')
		print('b = -2626224')
		print('c = -109745/2')
		exit(0)
	
	
	if pre_condition_385(a=a,b=b,c=c)==True:
		print("pre_condition_385 SAT")
		print('x = -137')
		print('y = -1')
		print('a = -2460377')
		print('z = -38')
		print('b = -2626224')
		print('c = -109745/2')
		exit(0)
	
	
	if pre_condition_386(a=a,b=b,c=c)==True:
		print("pre_condition_386 SAT")
		print('x = -137')
		print('y = -1')
		print('a = -2460377')
		print('z = -38')
		print('b = -2626224')
		print('c = -109745/2')
		exit(0)
	
	
	if pre_condition_387(a=a,b=b,c=c)==True:
		print("pre_condition_387 SAT")
		print('x = -138')
		print('y = -1')
		print('a = -2460377')
		print('z = -39')
		print('b = -2687390')
		print('c = -118639/2')
		exit(0)
	
	
	if pre_condition_388(a=a,b=b,c=c)==True:
		print("pre_condition_388 SAT")
		print('x = -138')
		print('y = -1')
		print('a = -2460377')
		print('z = -39')
		print('b = -2687390')
		print('c = -118639/2')
		exit(0)
	
	
	if pre_condition_389(a=a,b=b,c=c)==True:
		print("pre_condition_389 SAT")
		print('x = -138')
		print('y = -1')
		print('a = -2460377')
		print('z = -39')
		print('b = -2687390')
		print('c = -118639/2')
		exit(0)
	
	
	if pre_condition_390(a=a,b=b,c=c)==True:
		print("pre_condition_390 SAT")
		print('x = -139')
		print('y = -1')
		print('a = -2048385')
		print('z = -40')
		print('b = -2749618')
		print('c = -128001/2')
		exit(0)
	
	
	if pre_condition_391(a=a,b=b,c=c)==True:
		print("pre_condition_391 SAT")
		print('x = -139')
		print('y = -1')
		print('a = -2048385')
		print('z = -40')
		print('b = -2749618')
		print('c = -128001/2')
		exit(0)
	
	
	if pre_condition_392(a=a,b=b,c=c)==True:
		print("pre_condition_392 SAT")
		print('x = -139')
		print('y = -1')
		print('a = -2048385')
		print('z = -40')
		print('b = -2749618')
		print('c = -128001/2')
		exit(0)
	
	
	if pre_condition_393(a=a,b=b,c=c)==True:
		print("pre_condition_393 SAT")
		print('x = -140')
		print('y = -1')
		print('a = -1728002')
		print('z = -41')
		print('b = -2812920')
		print('c = -137843/2')
		exit(0)
	
	
	if pre_condition_394(a=a,b=b,c=c)==True:
		print("pre_condition_394 SAT")
		print('x = -140')
		print('y = -1')
		print('a = -1728002')
		print('z = -41')
		print('b = -2812920')
		print('c = -137843/2')
		exit(0)
	
	
	if pre_condition_395(a=a,b=b,c=c)==True:
		print("pre_condition_395 SAT")
		print('x = -140')
		print('y = -1')
		print('a = -1728002')
		print('z = -41')
		print('b = -2812920')
		print('c = -137843/2')
		exit(0)
	
	
	if pre_condition_396(a=a,b=b,c=c)==True:
		print("pre_condition_396 SAT")
		print('x = -141')
		print('y = -1')
		print('a = -1728002')
		print('z = -42')
		print('b = -2877308')
		print('c = -148177/2')
		exit(0)
	
	
	if pre_condition_397(a=a,b=b,c=c)==True:
		print("pre_condition_397 SAT")
		print('x = -141')
		print('y = -1')
		print('a = -1728002')
		print('z = -42')
		print('b = -2877308')
		print('c = -148177/2')
		exit(0)
	
	
	if pre_condition_398(a=a,b=b,c=c)==True:
		print("pre_condition_398 SAT")
		print('x = -141')
		print('y = -1')
		print('a = -1728002')
		print('z = -42')
		print('b = -2877308')
		print('c = -148177/2')
		exit(0)
	
	
	if pre_condition_399(a=a,b=b,c=c)==True:
		print("pre_condition_399 SAT")
		print('x = -142')
		print('y = -1')
		print('a = -2803223')
		print('z = -9')
		print('b = -2864016')
		print('c = -1459/2')
		exit(0)
	
	
	if pre_condition_400(a=a,b=b,c=c)==True:
		print("pre_condition_400 SAT")
		print('x = -142')
		print('y = -1')
		print('a = -2803223')
		print('z = -9')
		print('b = -2864016')
		print('c = -1459/2')
		exit(0)
	
	
	if pre_condition_401(a=a,b=b,c=c)==True:
		print("pre_condition_401 SAT")
		print('x = -142')
		print('y = -1')
		print('a = -2803223')
		print('z = -9')
		print('b = -2864016')
		print('c = -1459/2')
		exit(0)
	
	
	if pre_condition_402(a=a,b=b,c=c)==True:
		print("pre_condition_402 SAT")
		print('x = -143')
		print('y = -1')
		print('a = -2803223')
		print('z = -10')
		print('b = -2925206')
		print('c = -2001/2')
		exit(0)
	
	
	if pre_condition_403(a=a,b=b,c=c)==True:
		print("pre_condition_403 SAT")
		print('x = -143')
		print('y = -1')
		print('a = -2803223')
		print('z = -10')
		print('b = -2925206')
		print('c = -2001/2')
		exit(0)
	
	
	if pre_condition_404(a=a,b=b,c=c)==True:
		print("pre_condition_404 SAT")
		print('x = -143')
		print('y = -1')
		print('a = -2803223')
		print('z = -10')
		print('b = -2925206')
		print('c = -2001/2')
		exit(0)
	
	
	if pre_condition_405(a=a,b=b,c=c)==True:
		print("pre_condition_405 SAT")
		print('x = -144')
		print('y = -1')
		print('a = -2803223')
		print('z = -42')
		print('b = -3060071')
		print('c = -148177/2')
		exit(0)
	
	
	if pre_condition_406(a=a,b=b,c=c)==True:
		print("pre_condition_406 SAT")
		print('x = -144')
		print('y = -1')
		print('a = -2803223')
		print('z = -42')
		print('b = -3060071')
		print('c = -148177/2')
		exit(0)
	
	
	if pre_condition_407(a=a,b=b,c=c)==True:
		print("pre_condition_407 SAT")
		print('x = -144')
		print('y = -1')
		print('a = -2803223')
		print('z = -42')
		print('b = -3060071')
		print('c = -148177/2')
		exit(0)
	
	
	if pre_condition_408(a=a,b=b,c=c)==True:
		print("pre_condition_408 SAT")
		print('x = -145')
		print('y = -1')
		print('a = -2985986')
		print('z = 1/2')
		print('b = -3048624')
		print('c = 0')
		exit(0)
	
	
	if pre_condition_409(a=a,b=b,c=c)==True:
		print("pre_condition_409 SAT")
		print('x = -145')
		print('y = -1')
		print('a = -2985986')
		print('z = 1/2')
		print('b = -3048624')
		print('c = 0')
		exit(0)
	
	
	if pre_condition_410(a=a,b=b,c=c)==True:
		print("pre_condition_410 SAT")
		print('x = -145')
		print('y = -1')
		print('a = -2985986')
		print('z = 1/2')
		print('b = -3048624')
		print('c = 0')
		exit(0)
	
	
	if pre_condition_411(a=a,b=b,c=c)==True:
		print("pre_condition_411 SAT")
		print('x = -146')
		print('y = -1')
		print('a = -2985986')
		print('z = -11')
		print('b = -3113466')
		print('c = -2663/2')
		exit(0)
	
	
	if pre_condition_412(a=a,b=b,c=c)==True:
		print("pre_condition_412 SAT")
		print('x = -146')
		print('y = -1')
		print('a = -2985986')
		print('z = -11')
		print('b = -3113466')
		print('c = -2663/2')
		exit(0)
	
	
	if pre_condition_413(a=a,b=b,c=c)==True:
		print("pre_condition_413 SAT")
		print('x = -146')
		print('y = -1')
		print('a = -2985986')
		print('z = -11')
		print('b = -3113466')
		print('c = -2663/2')
		exit(0)
	
	
	if pre_condition_414(a=a,b=b,c=c)==True:
		print("pre_condition_414 SAT")
		print('x = -147')
		print('y = -1')
		print('a = -2985986')
		print('z = -42')
		print('b = -3250610')
		print('c = -148177/2')
		exit(0)
	
	
	if pre_condition_415(a=a,b=b,c=c)==True:
		print("pre_condition_415 SAT")
		print('x = -147')
		print('y = -1')
		print('a = -2985986')
		print('z = -42')
		print('b = -3250610')
		print('c = -148177/2')
		exit(0)
	
	
	if pre_condition_416(a=a,b=b,c=c)==True:
		print("pre_condition_416 SAT")
		print('x = -147')
		print('y = -1')
		print('a = -2985986')
		print('z = -42')
		print('b = -3250610')
		print('c = -148177/2')
		exit(0)
	
	
	if pre_condition_417(a=a,b=b,c=c)==True:
		print("pre_condition_417 SAT")
		print('x = -148')
		print('y = -1')
		print('a = -2803223')
		print('z = -43')
		print('b = -3321298')
		print('c = -159015/2')
		exit(0)
	
	
	if pre_condition_418(a=a,b=b,c=c)==True:
		print("pre_condition_418 SAT")
		print('x = -148')
		print('y = -1')
		print('a = -2803223')
		print('z = -43')
		print('b = -3321298')
		print('c = -159015/2')
		exit(0)
	
	
	if pre_condition_419(a=a,b=b,c=c)==True:
		print("pre_condition_419 SAT")
		print('x = -148')
		print('y = -1')
		print('a = -2803223')
		print('z = -43')
		print('b = -3321298')
		print('c = -159015/2')
		exit(0)
	
	
	if pre_condition_420(a=a,b=b,c=c)==True:
		print("pre_condition_420 SAT")
		print('x = -149')
		print('y = -1')
		print('a = -2352639')
		print('z = -44')
		print('b = -3393132')
		print('c = -170369/2')
		exit(0)
	
	
	if pre_condition_421(a=a,b=b,c=c)==True:
		print("pre_condition_421 SAT")
		print('x = -149')
		print('y = -1')
		print('a = -2352639')
		print('z = -44')
		print('b = -3393132')
		print('c = -170369/2')
		exit(0)
	
	
	if pre_condition_422(a=a,b=b,c=c)==True:
		print("pre_condition_422 SAT")
		print('x = -149')
		print('y = -1')
		print('a = -2352639')
		print('z = -44')
		print('b = -3393132')
		print('c = -170369/2')
		exit(0)
	
	
	if pre_condition_423(a=a,b=b,c=c)==True:
		print("pre_condition_423 SAT")
		print('x = -150')
		print('y = -1')
		print('a = -2924209')
		print('z = -45')
		print('b = -3466124')
		print('c = -182251/2')
		exit(0)
	
	
	if pre_condition_424(a=a,b=b,c=c)==True:
		print("pre_condition_424 SAT")
		print('x = -150')
		print('y = -1')
		print('a = -2924209')
		print('z = -45')
		print('b = -3466124')
		print('c = -182251/2')
		exit(0)
	
	
	if pre_condition_425(a=a,b=b,c=c)==True:
		print("pre_condition_425 SAT")
		print('x = -150')
		print('y = -1')
		print('a = -2924209')
		print('z = -45')
		print('b = -3466124')
		print('c = -182251/2')
		exit(0)
	
	
	if pre_condition_426(a=a,b=b,c=c)==True:
		print("pre_condition_426 SAT")
		print('x = -151')
		print('y = -1')
		print('a = -2924209')
		print('z = -46')
		print('b = -3540286')
		print('c = -194673/2')
		exit(0)
	
	
	if pre_condition_427(a=a,b=b,c=c)==True:
		print("pre_condition_427 SAT")
		print('x = -151')
		print('y = -1')
		print('a = -2924209')
		print('z = -46')
		print('b = -3540286')
		print('c = -194673/2')
		exit(0)
	
	
	if pre_condition_428(a=a,b=b,c=c)==True:
		print("pre_condition_428 SAT")
		print('x = -151')
		print('y = -1')
		print('a = -2924209')
		print('z = -46')
		print('b = -3540286')
		print('c = -194673/2')
		exit(0)
	
	
	if pre_condition_429(a=a,b=b,c=c)==True:
		print("pre_condition_429 SAT")
		print('x = -152')
		print('y = -1')
		print('a = -912675')
		print('z = -47')
		print('b = -3615630')
		print('c = -207647/2')
		exit(0)
	
	
	if pre_condition_430(a=a,b=b,c=c)==True:
		print("pre_condition_430 SAT")
		print('x = -152')
		print('y = -1')
		print('a = -912675')
		print('z = -47')
		print('b = -3615630')
		print('c = -207647/2')
		exit(0)
	
	
	if pre_condition_431(a=a,b=b,c=c)==True:
		print("pre_condition_431 SAT")
		print('x = -152')
		print('y = -1')
		print('a = -912675')
		print('z = -47')
		print('b = -3615630')
		print('c = -207647/2')
		exit(0)
	
	
	if pre_condition_432(a=a,b=b,c=c)==True:
		print("pre_condition_432 SAT")
		print('x = -153')
		print('y = -1')
		print('a = -3581577')
		print('z = -40')
		print('b = -3645576')
		print('c = -128001/2')
		exit(0)
	
	
	if pre_condition_433(a=a,b=b,c=c)==True:
		print("pre_condition_433 SAT")
		print('x = -153')
		print('y = -1')
		print('a = -3581577')
		print('z = -40')
		print('b = -3645576')
		print('c = -128001/2')
		exit(0)
	
	
	if pre_condition_434(a=a,b=b,c=c)==True:
		print("pre_condition_434 SAT")
		print('x = -153')
		print('y = -1')
		print('a = -3581577')
		print('z = -40')
		print('b = -3645576')
		print('c = -128001/2')
		exit(0)
	
	
	if pre_condition_435(a=a,b=b,c=c)==True:
		print("pre_condition_435 SAT")
		print('x = -154')
		print('y = -1')
		print('a = -3511810')
		print('z = -45')
		print('b = -3743388')
		print('c = -182251/2')
		exit(0)
	
	
	if pre_condition_436(a=a,b=b,c=c)==True:
		print("pre_condition_436 SAT")
		print('x = -154')
		print('y = -1')
		print('a = -3511810')
		print('z = -45')
		print('b = -3743388')
		print('c = -182251/2')
		exit(0)
	
	
	if pre_condition_437(a=a,b=b,c=c)==True:
		print("pre_condition_437 SAT")
		print('x = -154')
		print('y = -1')
		print('a = -3511810')
		print('z = -45')
		print('b = -3743388')
		print('c = -182251/2')
		exit(0)
	
	
	if pre_condition_438(a=a,b=b,c=c)==True:
		print("pre_condition_438 SAT")
		print('x = -155')
		print('y = -1')
		print('a = -3511810')
		print('z = -46')
		print('b = -3821210')
		print('c = -194673/2')
		exit(0)
	
	
	if pre_condition_439(a=a,b=b,c=c)==True:
		print("pre_condition_439 SAT")
		print('x = -155')
		print('y = -1')
		print('a = -3511810')
		print('z = -46')
		print('b = -3821210')
		print('c = -194673/2')
		exit(0)
	
	
	if pre_condition_440(a=a,b=b,c=c)==True:
		print("pre_condition_440 SAT")
		print('x = -155')
		print('y = -1')
		print('a = -3511810')
		print('z = -46')
		print('b = -3821210')
		print('c = -194673/2')
		exit(0)
	
	
	if pre_condition_441(a=a,b=b,c=c)==True:
		print("pre_condition_441 SAT")
		print('x = -156')
		print('y = -1')
		print('a = -3511810')
		print('z = -47')
		print('b = -3900238')
		print('c = -207647/2')
		exit(0)
	
	
	if pre_condition_442(a=a,b=b,c=c)==True:
		print("pre_condition_442 SAT")
		print('x = -156')
		print('y = -1')
		print('a = -3511810')
		print('z = -47')
		print('b = -3900238')
		print('c = -207647/2')
		exit(0)
	
	
	if pre_condition_443(a=a,b=b,c=c)==True:
		print("pre_condition_443 SAT")
		print('x = -156')
		print('y = -1')
		print('a = -3511810')
		print('z = -47')
		print('b = -3900238')
		print('c = -207647/2')
		exit(0)
	
	
	if pre_condition_444(a=a,b=b,c=c)==True:
		print("pre_condition_444 SAT")
		print('x = -157')
		print('y = -2')
		print('a = -3442953')
		print('z = -128')
		print('b = -5967044')
		print('c = -2097159')
		exit(0)
	
	
	if pre_condition_445(a=a,b=b,c=c)==True:
		print("pre_condition_445 SAT")
		print('x = -157')
		print('y = -2')
		print('a = -3442953')
		print('z = -128')
		print('b = -5967044')
		print('c = -2097159')
		exit(0)
	
	
	if pre_condition_446(a=a,b=b,c=c)==True:
		print("pre_condition_446 SAT")
		print('x = -157')
		print('y = -2')
		print('a = -3442953')
		print('z = -128')
		print('b = -5967044')
		print('c = -2097159')
		exit(0)
	
	
	if pre_condition_447(a=a,b=b,c=c)==True:
		print("pre_condition_447 SAT")
		print('x = -512')
		print('y = -1')
		print('a = -134217728')
		print('z = -5')
		print('b = -3870019')
		print('c = -251/2')
		exit(0)
	
	
	if pre_condition_448(a=a,b=b,c=c)==True:
		print("pre_condition_448 SAT")
		print('x = -512')
		print('y = -1')
		print('a = -134217728')
		print('z = -5')
		print('b = -3870019')
		print('c = -251/2')
		exit(0)
	
	
	if pre_condition_449(a=a,b=b,c=c)==True:
		print("pre_condition_449 SAT")
		print('x = -512')
		print('y = -1')
		print('a = -134217728')
		print('z = -5')
		print('b = -3870019')
		print('c = -251/2')
		exit(0)
	
	
	if pre_condition_450(a=a,b=b,c=c)==True:
		print("pre_condition_450 SAT")
		print('x = -513')
		print('y = -1')
		print('a = -3869902')
		print('z = -43')
		print('b = -135085203')
		print('c = -159015/2')
		exit(0)
	
	
	if pre_condition_451(a=a,b=b,c=c)==True:
		print("pre_condition_451 SAT")
		print('x = -513')
		print('y = -1')
		print('a = -3869902')
		print('z = -43')
		print('b = -135085203')
		print('c = -159015/2')
		exit(0)
	
	
	if pre_condition_452(a=a,b=b,c=c)==True:
		print("pre_condition_452 SAT")
		print('x = -513')
		print('y = -1')
		print('a = -3869902')
		print('z = -43')
		print('b = -135085203')
		print('c = -159015/2')
		exit(0)
	
	
	if pre_condition_453(a=a,b=b,c=c)==True:
		print("pre_condition_453 SAT")
		print('x = -514')
		print('y = -1')
		print('a = -3869902')
		print('z = -44')
		print('b = -135881927')
		print('c = -170369/2')
		exit(0)
	
	
	if pre_condition_454(a=a,b=b,c=c)==True:
		print("pre_condition_454 SAT")
		print('x = -514')
		print('y = -1')
		print('a = -3869902')
		print('z = -44')
		print('b = -135881927')
		print('c = -170369/2')
		exit(0)
	
	
	if pre_condition_455(a=a,b=b,c=c)==True:
		print("pre_condition_455 SAT")
		print('x = -514')
		print('y = -1')
		print('a = -3869902')
		print('z = -44')
		print('b = -135881927')
		print('c = -170369/2')
		exit(0)
	
	
	if pre_condition_456(a=a,b=b,c=c)==True:
		print("pre_condition_456 SAT")
		print('x = -515')
		print('y = -1')
		print('a = -3869902')
		print('z = -48')
		print('b = -136701466')
		print('c = -221185/2')
		exit(0)
	
	
	if pre_condition_457(a=a,b=b,c=c)==True:
		print("pre_condition_457 SAT")
		print('x = -515')
		print('y = -1')
		print('a = -3869902')
		print('z = -48')
		print('b = -136701466')
		print('c = -221185/2')
		exit(0)
	
	
	if pre_condition_458(a=a,b=b,c=c)==True:
		print("pre_condition_458 SAT")
		print('x = -515')
		print('y = -1')
		print('a = -3869902')
		print('z = -48')
		print('b = -136701466')
		print('c = -221185/2')
		exit(0)
	
	
	if pre_condition_459(a=a,b=b,c=c)==True:
		print("pre_condition_459 SAT")
		print('x = -516')
		print('y = -1')
		print('a = -3869902')
		print('z = -49')
		print('b = -137505744')
		print('c = -235299/2')
		exit(0)
	
	
	if pre_condition_460(a=a,b=b,c=c)==True:
		print("pre_condition_460 SAT")
		print('x = -516')
		print('y = -1')
		print('a = -3869902')
		print('z = -49')
		print('b = -137505744')
		print('c = -235299/2')
		exit(0)
	
	
	if pre_condition_461(a=a,b=b,c=c)==True:
		print("pre_condition_461 SAT")
		print('x = -516')
		print('y = -1')
		print('a = -3869902')
		print('z = -49')
		print('b = -137505744')
		print('c = -235299/2')
		exit(0)
	
	
	if pre_condition_462(a=a,b=b,c=c)==True:
		print("pre_condition_462 SAT")
		print('x = -517')
		print('y = -1')
		print('a = -138188413')
		print('z = -45')
		print('b = -137479222')
		print('c = -182251/2')
		exit(0)
	
	
	if pre_condition_463(a=a,b=b,c=c)==True:
		print("pre_condition_463 SAT")
		print('x = -517')
		print('y = -1')
		print('a = -138188413')
		print('z = -45')
		print('b = -137479222')
		print('c = -182251/2')
		exit(0)
	
	
	if pre_condition_464(a=a,b=b,c=c)==True:
		print("pre_condition_464 SAT")
		print('x = -517')
		print('y = -1')
		print('a = -138188413')
		print('z = -45')
		print('b = -137479222')
		print('c = -182251/2')
		exit(0)
	
	
	if pre_condition_465(a=a,b=b,c=c)==True:
		print("pre_condition_465 SAT")
		print('x = -518')
		print('y = -1')
		print('a = -137388098')
		print('z = -46')
		print('b = -139089167')
		print('c = -194673/2')
		exit(0)
	
	
	if pre_condition_466(a=a,b=b,c=c)==True:
		print("pre_condition_466 SAT")
		print('x = -518')
		print('y = -1')
		print('a = -137388098')
		print('z = -46')
		print('b = -139089167')
		print('c = -194673/2')
		exit(0)
	
	
	if pre_condition_467(a=a,b=b,c=c)==True:
		print("pre_condition_467 SAT")
		print('x = -518')
		print('y = -1')
		print('a = -137388098')
		print('z = -46')
		print('b = -139089167')
		print('c = -194673/2')
		exit(0)
	
	
	if pre_condition_468(a=a,b=b,c=c)==True:
		print("pre_condition_468 SAT")
		print('x = -519')
		print('y = -1')
		print('a = -137388098')
		print('z = -47')
		print('b = -139902181')
		print('c = -207647/2')
		exit(0)
	
	
	if pre_condition_469(a=a,b=b,c=c)==True:
		print("pre_condition_469 SAT")
		print('x = -519')
		print('y = -1')
		print('a = -137388098')
		print('z = -47')
		print('b = -139902181')
		print('c = -207647/2')
		exit(0)
	
	
	if pre_condition_470(a=a,b=b,c=c)==True:
		print("pre_condition_470 SAT")
		print('x = -519')
		print('y = -1')
		print('a = -137388098')
		print('z = -47')
		print('b = -139902181')
		print('c = -207647/2')
		exit(0)
	
	
	if pre_condition_471(a=a,b=b,c=c)==True:
		print("pre_condition_471 SAT")
		print('x = -520')
		print('y = -1')
		print('a = -137388098')
		print('z = -48')
		print('b = -140718591')
		print('c = -221185/2')
		exit(0)
	
	
	if pre_condition_472(a=a,b=b,c=c)==True:
		print("pre_condition_472 SAT")
		print('x = -520')
		print('y = -1')
		print('a = -137388098')
		print('z = -48')
		print('b = -140718591')
		print('c = -221185/2')
		exit(0)
	
	
	if pre_condition_473(a=a,b=b,c=c)==True:
		print("pre_condition_473 SAT")
		print('x = -520')
		print('y = -1')
		print('a = -137388098')
		print('z = -48')
		print('b = -140718591')
		print('c = -221185/2')
		exit(0)
	
	
	if pre_condition_474(a=a,b=b,c=c)==True:
		print("pre_condition_474 SAT")
		print('x = -521')
		print('y = -1')
		print('a = -137388098')
		print('z = -49')
		print('b = -141538409')
		print('c = -235299/2')
		exit(0)
	
	
	if pre_condition_475(a=a,b=b,c=c)==True:
		print("pre_condition_475 SAT")
		print('x = -521')
		print('y = -1')
		print('a = -137388098')
		print('z = -49')
		print('b = -141538409')
		print('c = -235299/2')
		exit(0)
	
	
	if pre_condition_476(a=a,b=b,c=c)==True:
		print("pre_condition_476 SAT")
		print('x = -521')
		print('y = -1')
		print('a = -137388098')
		print('z = -49')
		print('b = -141538409')
		print('c = -235299/2')
		exit(0)
	
	
	if pre_condition_477(a=a,b=b,c=c)==True:
		print("pre_condition_477 SAT")
		print('x = -522')
		print('y = -1')
		print('a = -3869902')
		print('z = -50')
		print('b = -142361647')
		print('c = -250001/2')
		exit(0)
	
	
	if pre_condition_478(a=a,b=b,c=c)==True:
		print("pre_condition_478 SAT")
		print('x = -522')
		print('y = -1')
		print('a = -3869902')
		print('z = -50')
		print('b = -142361647')
		print('c = -250001/2')
		exit(0)
	
	
	if pre_condition_479(a=a,b=b,c=c)==True:
		print("pre_condition_479 SAT")
		print('x = -522')
		print('y = -1')
		print('a = -3869902')
		print('z = -50')
		print('b = -142361647')
		print('c = -250001/2')
		exit(0)
	
	
	if pre_condition_480(a=a,b=b,c=c)==True:
		print("pre_condition_480 SAT")
		print('x = -523')
		print('y = -1')
		print('a = -3869902')
		print('z = -51')
		print('b = -143188317')
		print('c = -265303/2')
		exit(0)
	
	
	if pre_condition_481(a=a,b=b,c=c)==True:
		print("pre_condition_481 SAT")
		print('x = -523')
		print('y = -1')
		print('a = -3869902')
		print('z = -51')
		print('b = -143188317')
		print('c = -265303/2')
		exit(0)
	
	
	if pre_condition_482(a=a,b=b,c=c)==True:
		print("pre_condition_482 SAT")
		print('x = -523')
		print('y = -1')
		print('a = -3869902')
		print('z = -51')
		print('b = -143188317')
		print('c = -265303/2')
		exit(0)
	
	
	if pre_condition_483(a=a,b=b,c=c)==True:
		print("pre_condition_483 SAT")
		print('x = -524')
		print('y = -1')
		print('a = -3869902')
		print('z = -52')
		print('b = -144018431')
		print('c = -281217/2')
		exit(0)
	
	
	if pre_condition_484(a=a,b=b,c=c)==True:
		print("pre_condition_484 SAT")
		print('x = -524')
		print('y = -1')
		print('a = -3869902')
		print('z = -52')
		print('b = -144018431')
		print('c = -281217/2')
		exit(0)
	
	
	if pre_condition_485(a=a,b=b,c=c)==True:
		print("pre_condition_485 SAT")
		print('x = -524')
		print('y = -1')
		print('a = -3869902')
		print('z = -52')
		print('b = -144018431')
		print('c = -281217/2')
		exit(0)
	
	
	if pre_condition_486(a=a,b=b,c=c)==True:
		print("pre_condition_486 SAT")
		print('x = -525')
		print('y = -1')
		print('a = -3869902')
		print('z = -53')
		print('b = -144852001')
		print('c = -297755/2')
		exit(0)
	
	
	if pre_condition_487(a=a,b=b,c=c)==True:
		print("pre_condition_487 SAT")
		print('x = -525')
		print('y = -1')
		print('a = -3869902')
		print('z = -53')
		print('b = -144852001')
		print('c = -297755/2')
		exit(0)
	
	
	if pre_condition_488(a=a,b=b,c=c)==True:
		print("pre_condition_488 SAT")
		print('x = -525')
		print('y = -1')
		print('a = -3869902')
		print('z = -53')
		print('b = -144852001')
		print('c = -297755/2')
		exit(0)
	
	
	if pre_condition_489(a=a,b=b,c=c)==True:
		print("pre_condition_489 SAT")
		print('x = -526')
		print('y = -1')
		print('a = -145531576')
		print('z = -51')
		print('b = -144835777')
		print('c = -265303/2')
		exit(0)
	
	
	if pre_condition_490(a=a,b=b,c=c)==True:
		print("pre_condition_490 SAT")
		print('x = -526')
		print('y = -1')
		print('a = -145531576')
		print('z = -51')
		print('b = -144835777')
		print('c = -265303/2')
		exit(0)
	
	
	if pre_condition_491(a=a,b=b,c=c)==True:
		print("pre_condition_491 SAT")
		print('x = -526')
		print('y = -1')
		print('a = -145531576')
		print('z = -51')
		print('b = -144835777')
		print('c = -265303/2')
		exit(0)
	
	
	if pre_condition_492(a=a,b=b,c=c)==True:
		print("pre_condition_492 SAT")
		print('x = -527')
		print('y = -1')
		print('a = -144703127')
		print('z = -52')
		print('b = -146503790')
		print('c = -281217/2')
		exit(0)
	
	
	if pre_condition_493(a=a,b=b,c=c)==True:
		print("pre_condition_493 SAT")
		print('x = -527')
		print('y = -1')
		print('a = -144703127')
		print('z = -52')
		print('b = -146503790')
		print('c = -281217/2')
		exit(0)
	
	
	if pre_condition_494(a=a,b=b,c=c)==True:
		print("pre_condition_494 SAT")
		print('x = -527')
		print('y = -1')
		print('a = -144703127')
		print('z = -52')
		print('b = -146503790')
		print('c = -281217/2')
		exit(0)
	
	
	if pre_condition_495(a=a,b=b,c=c)==True:
		print("pre_condition_495 SAT")
		print('x = -528')
		print('y = -1')
		print('a = -144703127')
		print('z = -53')
		print('b = -147346828')
		print('c = -297755/2')
		exit(0)
	
	
	if pre_condition_496(a=a,b=b,c=c)==True:
		print("pre_condition_496 SAT")
		print('x = -528')
		print('y = -1')
		print('a = -144703127')
		print('z = -53')
		print('b = -147346828')
		print('c = -297755/2')
		exit(0)
	
	
	if pre_condition_497(a=a,b=b,c=c)==True:
		print("pre_condition_497 SAT")
		print('x = -528')
		print('y = -1')
		print('a = -144703127')
		print('z = -53')
		print('b = -147346828')
		print('c = -297755/2')
		exit(0)
	
	
	if pre_condition_498(a=a,b=b,c=c)==True:
		print("pre_condition_498 SAT")
		print('x = -529')
		print('y = -1')
		print('a = -148035889')
		print('z = -28')
		print('b = -147219905')
		print('c = -43905/2')
		exit(0)
	
	
	if pre_condition_499(a=a,b=b,c=c)==True:
		print("pre_condition_499 SAT")
		print('x = -529')
		print('y = -1')
		print('a = -148035889')
		print('z = -28')
		print('b = -147219905')
		print('c = -43905/2')
		exit(0)
	
	
	if pre_condition_500(a=a,b=b,c=c)==True:
		print("pre_condition_500 SAT")
		print('x = -529')
		print('y = -1')
		print('a = -148035889')
		print('z = -28')
		print('b = -147219905')
		print('c = -43905/2')
		exit(0)
	
	
	if pre_condition_501(a=a,b=b,c=c)==True:
		print("pre_condition_501 SAT")
		print('x = -530')
		print('y = -1')
		print('a = -147197954')
		print('z = -41')
		print('b = -148945920')
		print('c = -137843/2')
		exit(0)
	
	
	if pre_condition_502(a=a,b=b,c=c)==True:
		print("pre_condition_502 SAT")
		print('x = -530')
		print('y = -1')
		print('a = -147197954')
		print('z = -41')
		print('b = -148945920')
		print('c = -137843/2')
		exit(0)
	
	
	if pre_condition_503(a=a,b=b,c=c)==True:
		print("pre_condition_503 SAT")
		print('x = -530')
		print('y = -1')
		print('a = -147197954')
		print('z = -41')
		print('b = -148945920')
		print('c = -137843/2')
		exit(0)
	
	
	if pre_condition_504(a=a,b=b,c=c)==True:
		print("pre_condition_504 SAT")
		print('x = -531')
		print('y = -1')
		print('a = -147197954')
		print('z = -44')
		print('b = -149806474')
		print('c = -170369/2')
		exit(0)
	
	
	if pre_condition_505(a=a,b=b,c=c)==True:
		print("pre_condition_505 SAT")
		print('x = -531')
		print('y = -1')
		print('a = -147197954')
		print('z = -44')
		print('b = -149806474')
		print('c = -170369/2')
		exit(0)
	
	
	if pre_condition_506(a=a,b=b,c=c)==True:
		print("pre_condition_506 SAT")
		print('x = -531')
		print('y = -1')
		print('a = -147197954')
		print('z = -44')
		print('b = -149806474')
		print('c = -170369/2')
		exit(0)
	
	
	if pre_condition_507(a=a,b=b,c=c)==True:
		print("pre_condition_507 SAT")
		print('x = -532')
		print('y = -1')
		print('a = -147197954')
		print('z = -49')
		print('b = -150686416')
		print('c = -235299/2')
		exit(0)
	
	
	if pre_condition_508(a=a,b=b,c=c)==True:
		print("pre_condition_508 SAT")
		print('x = -532')
		print('y = -1')
		print('a = -147197954')
		print('z = -49')
		print('b = -150686416')
		print('c = -235299/2')
		exit(0)
	
	
	if pre_condition_509(a=a,b=b,c=c)==True:
		print("pre_condition_509 SAT")
		print('x = -532')
		print('y = -1')
		print('a = -147197954')
		print('z = -49')
		print('b = -150686416')
		print('c = -235299/2')
		exit(0)
	
	
	if pre_condition_510(a=a,b=b,c=c)==True:
		print("pre_condition_510 SAT")
		print('x = -533')
		print('y = -1')
		print('a = -147197954')
		print('z = -50')
		print('b = -151544436')
		print('c = -250001/2')
		exit(0)
	
	
	if pre_condition_511(a=a,b=b,c=c)==True:
		print("pre_condition_511 SAT")
		print('x = -533')
		print('y = -1')
		print('a = -147197954')
		print('z = -50')
		print('b = -151544436')
		print('c = -250001/2')
		exit(0)
	
	
	if pre_condition_512(a=a,b=b,c=c)==True:
		print("pre_condition_512 SAT")
		print('x = -533')
		print('y = -1')
		print('a = -147197954')
		print('z = -50')
		print('b = -151544436')
		print('c = -250001/2')
		exit(0)
	
	
	if pre_condition_513(a=a,b=b,c=c)==True:
		print("pre_condition_513 SAT")
		print('x = -534')
		print('y = -1')
		print('a = -147197954')
		print('z = -53')
		print('b = -152422180')
		print('c = -297755/2')
		exit(0)
	
	
	if pre_condition_514(a=a,b=b,c=c)==True:
		print("pre_condition_514 SAT")
		print('x = -534')
		print('y = -1')
		print('a = -147197954')
		print('z = -53')
		print('b = -152422180')
		print('c = -297755/2')
		exit(0)
	
	
	if pre_condition_515(a=a,b=b,c=c)==True:
		print("pre_condition_515 SAT")
		print('x = -534')
		print('y = -1')
		print('a = -147197954')
		print('z = -53')
		print('b = -152422180')
		print('c = -297755/2')
		exit(0)
	
	
	if pre_condition_516(a=a,b=b,c=c)==True:
		print("pre_condition_516 SAT")
		print('x = -535')
		print('y = -1')
		print('a = -153130375')
		print('z = -50')
		print('b = -152398305')
		print('c = -250001/2')
		exit(0)
	
	
	if pre_condition_517(a=a,b=b,c=c)==True:
		print("pre_condition_517 SAT")
		print('x = -535')
		print('y = -1')
		print('a = -153130375')
		print('z = -50')
		print('b = -152398305')
		print('c = -250001/2')
		exit(0)
	
	
	if pre_condition_518(a=a,b=b,c=c)==True:
		print("pre_condition_518 SAT")
		print('x = -535')
		print('y = -1')
		print('a = -153130375')
		print('z = -50')
		print('b = -152398305')
		print('c = -250001/2')
		exit(0)
	
	
	if pre_condition_519(a=a,b=b,c=c)==True:
		print("pre_condition_519 SAT")
		print('x = -536')
		print('y = -1')
		print('a = -152273306')
		print('z = -51')
		print('b = -154123306')
		print('c = -265303/2')
		exit(0)
	
	
	if pre_condition_520(a=a,b=b,c=c)==True:
		print("pre_condition_520 SAT")
		print('x = -536')
		print('y = -1')
		print('a = -152273306')
		print('z = -51')
		print('b = -154123306')
		print('c = -265303/2')
		exit(0)
	
	
	if pre_condition_521(a=a,b=b,c=c)==True:
		print("pre_condition_521 SAT")
		print('x = -536')
		print('y = -1')
		print('a = -152273306')
		print('z = -51')
		print('b = -154123306')
		print('c = -265303/2')
		exit(0)
	
	
	if pre_condition_522(a=a,b=b,c=c)==True:
		print("pre_condition_522 SAT")
		print('x = -537')
		print('y = -1')
		print('a = -152273306')
		print('z = -53')
		print('b = -155003029')
		print('c = -297755/2')
		exit(0)
	
	
	if pre_condition_523(a=a,b=b,c=c)==True:
		print("pre_condition_523 SAT")
		print('x = -537')
		print('y = -1')
		print('a = -152273306')
		print('z = -53')
		print('b = -155003029')
		print('c = -297755/2')
		exit(0)
	
	
	if pre_condition_524(a=a,b=b,c=c)==True:
		print("pre_condition_524 SAT")
		print('x = -537')
		print('y = -1')
		print('a = -152273306')
		print('z = -53')
		print('b = -155003029')
		print('c = -297755/2')
		exit(0)
	
	
	if pre_condition_525(a=a,b=b,c=c)==True:
		print("pre_condition_525 SAT")
		print('x = -538')
		print('y = -1')
		print('a = -155720872')
		print('z = -53')
		print('b = -155869748')
		print('c = -297755/2')
		exit(0)
	
	
	if pre_condition_526(a=a,b=b,c=c)==True:
		print("pre_condition_526 SAT")
		print('x = -538')
		print('y = -1')
		print('a = -155720872')
		print('z = -53')
		print('b = -155869748')
		print('c = -297755/2')
		exit(0)
	
	
	if pre_condition_527(a=a,b=b,c=c)==True:
		print("pre_condition_527 SAT")
		print('x = -538')
		print('y = -1')
		print('a = -155720872')
		print('z = -53')
		print('b = -155869748')
		print('c = -297755/2')
		exit(0)
	
	
	if pre_condition_528(a=a,b=b,c=c)==True:
		print("pre_condition_528 SAT")
		print('x = -539')
		print('y = -1')
		print('a = -156590819')
		print('z = -53')
		print('b = -156739695')
		print('c = -297755/2')
		exit(0)
	
	
	if pre_condition_529(a=a,b=b,c=c)==True:
		print("pre_condition_529 SAT")
		print('x = -539')
		print('y = -1')
		print('a = -156590819')
		print('z = -53')
		print('b = -156739695')
		print('c = -297755/2')
		exit(0)
	
	
	if pre_condition_530(a=a,b=b,c=c)==True:
		print("pre_condition_530 SAT")
		print('x = -539')
		print('y = -1')
		print('a = -156590819')
		print('z = -53')
		print('b = -156739695')
		print('c = -297755/2')
		exit(0)
	
	
	if pre_condition_531(a=a,b=b,c=c)==True:
		print("pre_condition_531 SAT")
		print('x = -540')
		print('y = -1')
		print('a = -153990658')
		print('z = -54')
		print('b = -157621463')
		print('c = -314929/2')
		exit(0)
	
	
	if pre_condition_532(a=a,b=b,c=c)==True:
		print("pre_condition_532 SAT")
		print('x = -540')
		print('y = -1')
		print('a = -153990658')
		print('z = -54')
		print('b = -157621463')
		print('c = -314929/2')
		exit(0)
	
	
	if pre_condition_533(a=a,b=b,c=c)==True:
		print("pre_condition_533 SAT")
		print('x = -540')
		print('y = -1')
		print('a = -153990658')
		print('z = -54')
		print('b = -157621463')
		print('c = -314929/2')
		exit(0)
	
	
	if pre_condition_534(a=a,b=b,c=c)==True:
		print("pre_condition_534 SAT")
		print('x = -541')
		print('y = -1')
		print('a = -158340421')
		print('z = -54')
		print('b = -157621465')
		print('c = -314929/2')
		exit(0)
	
	
	if pre_condition_535(a=a,b=b,c=c)==True:
		print("pre_condition_535 SAT")
		print('x = -541')
		print('y = -1')
		print('a = -158340421')
		print('z = -54')
		print('b = -157621465')
		print('c = -314929/2')
		exit(0)
	
	
	if pre_condition_536(a=a,b=b,c=c)==True:
		print("pre_condition_536 SAT")
		print('x = -541')
		print('y = -1')
		print('a = -158340421')
		print('z = -54')
		print('b = -157621465')
		print('c = -314929/2')
		exit(0)
	
	
	if pre_condition_537(a=a,b=b,c=c)==True:
		print("pre_condition_537 SAT")
		print('x = -542')
		print('y = -1')
		print('a = -154854155')
		print('z = -55')
		print('b = -159386462')
		print('c = -332751/2')
		exit(0)
	
	
	if pre_condition_538(a=a,b=b,c=c)==True:
		print("pre_condition_538 SAT")
		print('x = -542')
		print('y = -1')
		print('a = -154854155')
		print('z = -55')
		print('b = -159386462')
		print('c = -332751/2')
		exit(0)
	
	
	if pre_condition_539(a=a,b=b,c=c)==True:
		print("pre_condition_539 SAT")
		print('x = -542')
		print('y = -1')
		print('a = -154854155')
		print('z = -55')
		print('b = -159386462')
		print('c = -332751/2')
		exit(0)
	
	
	if pre_condition_540(a=a,b=b,c=c)==True:
		print("pre_condition_540 SAT")
		print('x = -543')
		print('y = -1')
		print('a = -155720874')
		print('z = -56')
		print('b = -160278622')
		print('c = -351233/2')
		exit(0)
	
	
	if pre_condition_541(a=a,b=b,c=c)==True:
		print("pre_condition_541 SAT")
		print('x = -543')
		print('y = -1')
		print('a = -155720874')
		print('z = -56')
		print('b = -160278622')
		print('c = -351233/2')
		exit(0)
	
	
	if pre_condition_542(a=a,b=b,c=c)==True:
		print("pre_condition_542 SAT")
		print('x = -543')
		print('y = -1')
		print('a = -155720874')
		print('z = -56')
		print('b = -160278622')
		print('c = -351233/2')
		exit(0)
	
	
	if pre_condition_543(a=a,b=b,c=c)==True:
		print("pre_condition_543 SAT")
		print('x = -544')
		print('y = -1')
		print('a = -3869902')
		print('z = -57')
		print('b = -161174376')
		print('c = -370387/2')
		exit(0)
	
	
	if pre_condition_544(a=a,b=b,c=c)==True:
		print("pre_condition_544 SAT")
		print('x = -544')
		print('y = -1')
		print('a = -3869902')
		print('z = -57')
		print('b = -161174376')
		print('c = -370387/2')
		exit(0)
	
	
	if pre_condition_545(a=a,b=b,c=c)==True:
		print("pre_condition_545 SAT")
		print('x = -544')
		print('y = -1')
		print('a = -3869902')
		print('z = -57')
		print('b = -161174376')
		print('c = -370387/2')
		exit(0)
	
	
	if pre_condition_546(a=a,b=b,c=c)==True:
		print("pre_condition_546 SAT")
		print('x = -545')
		print('y = -1')
		print('a = -3869902')
		print('z = -58')
		print('b = -162073736')
		print('c = -390225/2')
		exit(0)
	
	
	if pre_condition_547(a=a,b=b,c=c)==True:
		print("pre_condition_547 SAT")
		print('x = -545')
		print('y = -1')
		print('a = -3869902')
		print('z = -58')
		print('b = -162073736')
		print('c = -390225/2')
		exit(0)
	
	
	if pre_condition_548(a=a,b=b,c=c)==True:
		print("pre_condition_548 SAT")
		print('x = -545')
		print('y = -1')
		print('a = -3869902')
		print('z = -58')
		print('b = -162073736')
		print('c = -390225/2')
		exit(0)
	
	
	if pre_condition_549(a=a,b=b,c=c)==True:
		print("pre_condition_549 SAT")
		print('x = -546')
		print('y = -1')
		print('a = -143877826')
		print('z = -59')
		print('b = -162976714')
		print('c = -410759/2')
		exit(0)
	
	
	if pre_condition_550(a=a,b=b,c=c)==True:
		print("pre_condition_550 SAT")
		print('x = -546')
		print('y = -1')
		print('a = -143877826')
		print('z = -59')
		print('b = -162976714')
		print('c = -410759/2')
		exit(0)
	
	
	if pre_condition_551(a=a,b=b,c=c)==True:
		print("pre_condition_551 SAT")
		print('x = -546')
		print('y = -1')
		print('a = -143877826')
		print('z = -59')
		print('b = -162976714')
		print('c = -410759/2')
		exit(0)
	
	
	if pre_condition_552(a=a,b=b,c=c)==True:
		print("pre_condition_552 SAT")
		print('x = -547')
		print('y = -1')
		print('a = -162771338')
		print('z = 1/2')
		print('b = -163667322')
		print('c = 0')
		exit(0)
	
	
	if pre_condition_553(a=a,b=b,c=c)==True:
		print("pre_condition_553 SAT")
		print('x = -547')
		print('y = -1')
		print('a = -162771338')
		print('z = 1/2')
		print('b = -163667322')
		print('c = 0')
		exit(0)
	
	
	if pre_condition_554(a=a,b=b,c=c)==True:
		print("pre_condition_554 SAT")
		print('x = -547')
		print('y = -1')
		print('a = -162771338')
		print('z = 1/2')
		print('b = -163667322')
		print('c = 0')
		exit(0)
	
	
	if pre_condition_555(a=a,b=b,c=c)==True:
		print("pre_condition_555 SAT")
		print('x = -548')
		print('y = -1')
		print('a = -162771338')
		print('z = -29')
		print('b = -164590980')
		print('c = -48779/2')
		exit(0)
	
	
	if pre_condition_556(a=a,b=b,c=c)==True:
		print("pre_condition_556 SAT")
		print('x = -548')
		print('y = -1')
		print('a = -162771338')
		print('z = -29')
		print('b = -164590980')
		print('c = -48779/2')
		exit(0)
	
	
	if pre_condition_557(a=a,b=b,c=c)==True:
		print("pre_condition_557 SAT")
		print('x = -548')
		print('y = -1')
		print('a = -162771338')
		print('z = -29')
		print('b = -164590980')
		print('c = -48779/2')
		exit(0)
	
	
	if pre_condition_558(a=a,b=b,c=c)==True:
		print("pre_condition_558 SAT")
		print('x = -549')
		print('y = -1')
		print('a = -162771338')
		print('z = -58')
		print('b = -165664260')
		print('c = -390225/2')
		exit(0)
	
	
	if pre_condition_559(a=a,b=b,c=c)==True:
		print("pre_condition_559 SAT")
		print('x = -549')
		print('y = -1')
		print('a = -162771338')
		print('z = -58')
		print('b = -165664260')
		print('c = -390225/2')
		exit(0)
	
	
	if pre_condition_560(a=a,b=b,c=c)==True:
		print("pre_condition_560 SAT")
		print('x = -549')
		print('y = -1')
		print('a = -162771338')
		print('z = -58')
		print('b = -165664260')
		print('c = -390225/2')
		exit(0)
	
	
	if pre_condition_561(a=a,b=b,c=c)==True:
		print("pre_condition_561 SAT")
		print('x = -550')
		print('y = -1')
		print('a = -162771338')
		print('z = -59')
		print('b = -166580378')
		print('c = -410759/2')
		exit(0)
	
	
	if pre_condition_562(a=a,b=b,c=c)==True:
		print("pre_condition_562 SAT")
		print('x = -550')
		print('y = -1')
		print('a = -162771338')
		print('z = -59')
		print('b = -166580378')
		print('c = -410759/2')
		exit(0)
	
	
	if pre_condition_563(a=a,b=b,c=c)==True:
		print("pre_condition_563 SAT")
		print('x = -550')
		print('y = -1')
		print('a = -162771338')
		print('z = -59')
		print('b = -166580378')
		print('c = -410759/2')
		exit(0)
	
	
	if pre_condition_564(a=a,b=b,c=c)==True:
		print("pre_condition_564 SAT")
		print('x = -551')
		print('y = -1')
		print('a = -166375002')
		print('z = -1')
		print('b = -167284151')
		print('c = -3/2')
		exit(0)
	
	
	if pre_condition_565(a=a,b=b,c=c)==True:
		print("pre_condition_565 SAT")
		print('x = -551')
		print('y = -1')
		print('a = -166375002')
		print('z = -1')
		print('b = -167284151')
		print('c = -3/2')
		exit(0)
	
	
	if pre_condition_566(a=a,b=b,c=c)==True:
		print("pre_condition_566 SAT")
		print('x = -551')
		print('y = -1')
		print('a = -166375002')
		print('z = -1')
		print('b = -167284151')
		print('c = -3/2')
		exit(0)
	
	
	if pre_condition_567(a=a,b=b,c=c)==True:
		print("pre_condition_567 SAT")
		print('x = -552')
		print('y = -1')
		print('a = -166375002')
		print('z = -59')
		print('b = -168401986')
		print('c = -410759/2')
		exit(0)
	
	
	if pre_condition_568(a=a,b=b,c=c)==True:
		print("pre_condition_568 SAT")
		print('x = -552')
		print('y = -1')
		print('a = -166375002')
		print('z = -59')
		print('b = -168401986')
		print('c = -410759/2')
		exit(0)
	
	
	if pre_condition_569(a=a,b=b,c=c)==True:
		print("pre_condition_569 SAT")
		print('x = -552')
		print('y = -1')
		print('a = -166375002')
		print('z = -59')
		print('b = -168401986')
		print('c = -410759/2')
		exit(0)
	
	
	if pre_condition_570(a=a,b=b,c=c)==True:
		print("pre_condition_570 SAT")
		print('x = -553')
		print('y = -1')
		print('a = -169112377')
		print('z = -30')
		print('b = -168223609')
		print('c = -54001/2')
		exit(0)
	
	
	if pre_condition_571(a=a,b=b,c=c)==True:
		print("pre_condition_571 SAT")
		print('x = -553')
		print('y = -1')
		print('a = -169112377')
		print('z = -30')
		print('b = -168223609')
		print('c = -54001/2')
		exit(0)
	
	
	if pre_condition_572(a=a,b=b,c=c)==True:
		print("pre_condition_572 SAT")
		print('x = -553')
		print('y = -1')
		print('a = -169112377')
		print('z = -30')
		print('b = -168223609')
		print('c = -54001/2')
		exit(0)
	
	
	if pre_condition_573(a=a,b=b,c=c)==True:
		print("pre_condition_573 SAT")
		print('x = -554')
		print('y = -1')
		print('a = -168196610')
		print('z = -59')
		print('b = -170236842')
		print('c = -410759/2')
		exit(0)
	
	
	if pre_condition_574(a=a,b=b,c=c)==True:
		print("pre_condition_574 SAT")
		print('x = -554')
		print('y = -1')
		print('a = -168196610')
		print('z = -59')
		print('b = -170236842')
		print('c = -410759/2')
		exit(0)
	
	
	if pre_condition_575(a=a,b=b,c=c)==True:
		print("pre_condition_575 SAT")
		print('x = -554')
		print('y = -1')
		print('a = -168196610')
		print('z = -59')
		print('b = -170236842')
		print('c = -410759/2')
		exit(0)
	
	
	if pre_condition_576(a=a,b=b,c=c)==True:
		print("pre_condition_576 SAT")
		print('x = -555')
		print('y = -1')
		print('a = -166375002')
		print('z = -60')
		print('b = -171169874')
		print('c = -432001/2')
		exit(0)
	
	
	if pre_condition_577(a=a,b=b,c=c)==True:
		print("pre_condition_577 SAT")
		print('x = -555')
		print('y = -1')
		print('a = -166375002')
		print('z = -60')
		print('b = -171169874')
		print('c = -432001/2')
		exit(0)
	
	
	if pre_condition_578(a=a,b=b,c=c)==True:
		print("pre_condition_578 SAT")
		print('x = -555')
		print('y = -1')
		print('a = -166375002')
		print('z = -60')
		print('b = -171169874')
		print('c = -432001/2')
		exit(0)
	
	
	if pre_condition_579(a=a,b=b,c=c)==True:
		print("pre_condition_579 SAT")
		print('x = -556')
		print('y = -1')
		print('a = -171879616')
		print('z = -51')
		print('b = -171086527')
		print('c = -265303/2')
		exit(0)
	
	
	if pre_condition_580(a=a,b=b,c=c)==True:
		print("pre_condition_580 SAT")
		print('x = -556')
		print('y = -1')
		print('a = -171879616')
		print('z = -51')
		print('b = -171086527')
		print('c = -265303/2')
		exit(0)
	
	
	if pre_condition_581(a=a,b=b,c=c)==True:
		print("pre_condition_581 SAT")
		print('x = -556')
		print('y = -1')
		print('a = -171879616')
		print('z = -51')
		print('b = -171086527')
		print('c = -265303/2')
		exit(0)
	
	
	if pre_condition_582(a=a,b=b,c=c)==True:
		print("pre_condition_582 SAT")
		print('x = -557')
		print('y = -1')
		print('a = -170953877')
		print('z = -57')
		print('b = -172993885')
		print('c = -370387/2')
		exit(0)
	
	
	if pre_condition_583(a=a,b=b,c=c)==True:
		print("pre_condition_583 SAT")
		print('x = -557')
		print('y = -1')
		print('a = -170953877')
		print('z = -57')
		print('b = -172993885')
		print('c = -370387/2')
		exit(0)
	
	
	if pre_condition_584(a=a,b=b,c=c)==True:
		print("pre_condition_584 SAT")
		print('x = -557')
		print('y = -1')
		print('a = -170953877')
		print('z = -57')
		print('b = -172993885')
		print('c = -370387/2')
		exit(0)
	
	
	if pre_condition_585(a=a,b=b,c=c)==True:
		print("pre_condition_585 SAT")
		print('x = -558')
		print('y = -1')
		print('a = -170953877')
		print('z = -59')
		print('b = -173946490')
		print('c = -410759/2')
		exit(0)
	
	
	if pre_condition_586(a=a,b=b,c=c)==True:
		print("pre_condition_586 SAT")
		print('x = -558')
		print('y = -1')
		print('a = -170953877')
		print('z = -59')
		print('b = -173946490')
		print('c = -410759/2')
		exit(0)
	
	
	if pre_condition_587(a=a,b=b,c=c)==True:
		print("pre_condition_587 SAT")
		print('x = -558')
		print('y = -1')
		print('a = -170953877')
		print('z = -59')
		print('b = -173946490')
		print('c = -410759/2')
		exit(0)
	
	
	if pre_condition_588(a=a,b=b,c=c)==True:
		print("pre_condition_588 SAT")
		print('x = -559')
		print('y = -1')
		print('a = -170953877')
		print('z = -60')
		print('b = -174892878')
		print('c = -432001/2')
		exit(0)
	
	
	if pre_condition_589(a=a,b=b,c=c)==True:
		print("pre_condition_589 SAT")
		print('x = -559')
		print('y = -1')
		print('a = -170953877')
		print('z = -60')
		print('b = -174892878')
		print('c = -432001/2')
		exit(0)
	
	
	if pre_condition_590(a=a,b=b,c=c)==True:
		print("pre_condition_590 SAT")
		print('x = -559')
		print('y = -1')
		print('a = -170953877')
		print('z = -60')
		print('b = -174892878')
		print('c = -432001/2')
		exit(0)
	
	
	if pre_condition_591(a=a,b=b,c=c)==True:
		print("pre_condition_591 SAT")
		print('x = -560')
		print('y = -1')
		print('a = -3869902')
		print('z = -61')
		print('b = -175842980')
		print('c = -453963/2')
		exit(0)
	
	
	if pre_condition_592(a=a,b=b,c=c)==True:
		print("pre_condition_592 SAT")
		print('x = -560')
		print('y = -1')
		print('a = -3869902')
		print('z = -61')
		print('b = -175842980')
		print('c = -453963/2')
		exit(0)
	
	
	if pre_condition_593(a=a,b=b,c=c)==True:
		print("pre_condition_593 SAT")
		print('x = -560')
		print('y = -1')
		print('a = -3869902')
		print('z = -61')
		print('b = -175842980')
		print('c = -453963/2')
		exit(0)
	
	
	if pre_condition_594(a=a,b=b,c=c)==True:
		print("pre_condition_594 SAT")
		print('x = -561')
		print('y = -1')
		print('a = -175616002')
		print('z = -52')
		print('b = -176699088')
		print('c = -281217/2')
		exit(0)
	
	
	if pre_condition_595(a=a,b=b,c=c)==True:
		print("pre_condition_595 SAT")
		print('x = -561')
		print('y = -1')
		print('a = -175616002')
		print('z = -52')
		print('b = -176699088')
		print('c = -281217/2')
		exit(0)
	
	
	if pre_condition_596(a=a,b=b,c=c)==True:
		print("pre_condition_596 SAT")
		print('x = -561')
		print('y = -1')
		print('a = -175616002')
		print('z = -52')
		print('b = -176699088')
		print('c = -281217/2')
		exit(0)
	
	
	if pre_condition_597(a=a,b=b,c=c)==True:
		print("pre_condition_597 SAT")
		print('x = -562')
		print('y = -1')
		print('a = -175616002')
		print('z = -53')
		print('b = -177653204')
		print('c = -297755/2')
		exit(0)
	
	
	if pre_condition_598(a=a,b=b,c=c)==True:
		print("pre_condition_598 SAT")
		print('x = -562')
		print('y = -1')
		print('a = -175616002')
		print('z = -53')
		print('b = -177653204')
		print('c = -297755/2')
		exit(0)
	
	
	if pre_condition_599(a=a,b=b,c=c)==True:
		print("pre_condition_599 SAT")
		print('x = -562')
		print('y = -1')
		print('a = -175616002')
		print('z = -53')
		print('b = -177653204')
		print('c = -297755/2')
		exit(0)
	
	
	if pre_condition_600(a=a,b=b,c=c)==True:
		print("pre_condition_600 SAT")
		print('x = -563')
		print('y = -1')
		print('a = -175616002')
		print('z = -58')
		print('b = -178648658')
		print('c = -390225/2')
		exit(0)
	
	
	if pre_condition_601(a=a,b=b,c=c)==True:
		print("pre_condition_601 SAT")
		print('x = -563')
		print('y = -1')
		print('a = -175616002')
		print('z = -58')
		print('b = -178648658')
		print('c = -390225/2')
		exit(0)
	
	
	if pre_condition_602(a=a,b=b,c=c)==True:
		print("pre_condition_602 SAT")
		print('x = -563')
		print('y = -1')
		print('a = -175616002')
		print('z = -58')
		print('b = -178648658')
		print('c = -390225/2')
		exit(0)
	
	
	if pre_condition_603(a=a,b=b,c=c)==True:
		print("pre_condition_603 SAT")
		print('x = -564')
		print('y = -1')
		print('a = -175616002')
		print('z = -59')
		print('b = -179611522')
		print('c = -410759/2')
		exit(0)
	
	
	if pre_condition_604(a=a,b=b,c=c)==True:
		print("pre_condition_604 SAT")
		print('x = -564')
		print('y = -1')
		print('a = -175616002')
		print('z = -59')
		print('b = -179611522')
		print('c = -410759/2')
		exit(0)
	
	
	if pre_condition_605(a=a,b=b,c=c)==True:
		print("pre_condition_605 SAT")
		print('x = -564')
		print('y = -1')
		print('a = -175616002')
		print('z = -59')
		print('b = -179611522')
		print('c = -410759/2')
		exit(0)
	
	
	if pre_condition_606(a=a,b=b,c=c)==True:
		print("pre_condition_606 SAT")
		print('x = -565')
		print('y = -1')
		print('a = -175616002')
		print('z = -61')
		print('b = -180589105')
		print('c = -453963/2')
		exit(0)
	
	
	if pre_condition_607(a=a,b=b,c=c)==True:
		print("pre_condition_607 SAT")
		print('x = -565')
		print('y = -1')
		print('a = -175616002')
		print('z = -61')
		print('b = -180589105')
		print('c = -453963/2')
		exit(0)
	
	
	if pre_condition_608(a=a,b=b,c=c)==True:
		print("pre_condition_608 SAT")
		print('x = -565')
		print('y = -1')
		print('a = -175616002')
		print('z = -61')
		print('b = -180589105')
		print('c = -453963/2')
		exit(0)
	
	
	if pre_condition_609(a=a,b=b,c=c)==True:
		print("pre_condition_609 SAT")
		print('x = -566')
		print('y = -1')
		print('a = -3869902')
		print('z = -62')
		print('b = -181559823')
		print('c = -476657/2')
		exit(0)
	
	
	if pre_condition_610(a=a,b=b,c=c)==True:
		print("pre_condition_610 SAT")
		print('x = -566')
		print('y = -1')
		print('a = -3869902')
		print('z = -62')
		print('b = -181559823')
		print('c = -476657/2')
		exit(0)
	
	
	if pre_condition_611(a=a,b=b,c=c)==True:
		print("pre_condition_611 SAT")
		print('x = -566')
		print('y = -1')
		print('a = -3869902')
		print('z = -62')
		print('b = -181559823')
		print('c = -476657/2')
		exit(0)
	
	
	if pre_condition_612(a=a,b=b,c=c)==True:
		print("pre_condition_612 SAT")
		print('x = -567')
		print('y = -1')
		print('a = -182284263')
		print('z = -61')
		print('b = -181548478')
		print('c = -453963/2')
		exit(0)
	
	
	if pre_condition_613(a=a,b=b,c=c)==True:
		print("pre_condition_613 SAT")
		print('x = -567')
		print('y = -1')
		print('a = -182284263')
		print('z = -61')
		print('b = -181548478')
		print('c = -453963/2')
		exit(0)
	
	
	if pre_condition_614(a=a,b=b,c=c)==True:
		print("pre_condition_614 SAT")
		print('x = -567')
		print('y = -1')
		print('a = -182284263')
		print('z = -61')
		print('b = -181548478')
		print('c = -453963/2')
		exit(0)
	
	
	if pre_condition_615(a=a,b=b,c=c)==True:
		print("pre_condition_615 SAT")
		print('x = -568')
		print('y = -1')
		print('a = -181321498')
		print('z = -62')
		print('b = -183488759')
		print('c = -476657/2')
		exit(0)
	
	
	if pre_condition_616(a=a,b=b,c=c)==True:
		print("pre_condition_616 SAT")
		print('x = -568')
		print('y = -1')
		print('a = -181321498')
		print('z = -62')
		print('b = -183488759')
		print('c = -476657/2')
		exit(0)
	
	
	if pre_condition_617(a=a,b=b,c=c)==True:
		print("pre_condition_617 SAT")
		print('x = -568')
		print('y = -1')
		print('a = -181321498')
		print('z = -62')
		print('b = -183488759')
		print('c = -476657/2')
		exit(0)
	
	
	if pre_condition_618(a=a,b=b,c=c)==True:
		print("pre_condition_618 SAT")
		print('x = -569')
		print('y = -1')
		print('a = -179406146')
		print('z = -63')
		print('b = -184470055')
		print('c = -500095/2')
		exit(0)
	
	
	if pre_condition_619(a=a,b=b,c=c)==True:
		print("pre_condition_619 SAT")
		print('x = -569')
		print('y = -1')
		print('a = -179406146')
		print('z = -63')
		print('b = -184470055')
		print('c = -500095/2')
		exit(0)
	
	
	if pre_condition_620(a=a,b=b,c=c)==True:
		print("pre_condition_620 SAT")
		print('x = -569')
		print('y = -1')
		print('a = -179406146')
		print('z = -63')
		print('b = -184470055')
		print('c = -500095/2')
		exit(0)
	
	
	if pre_condition_621(a=a,b=b,c=c)==True:
		print("pre_condition_621 SAT")
		print('x = -570')
		print('y = -1')
		print('a = -184220011')
		print('z = 1/2')
		print('b = -185192999')
		print('c = 0')
		exit(0)
	
	
	if pre_condition_622(a=a,b=b,c=c)==True:
		print("pre_condition_622 SAT")
		print('x = -570')
		print('y = -1')
		print('a = -184220011')
		print('z = 1/2')
		print('b = -185192999')
		print('c = 0')
		exit(0)
	
	
	if pre_condition_623(a=a,b=b,c=c)==True:
		print("pre_condition_623 SAT")
		print('x = -570')
		print('y = -1')
		print('a = -184220011')
		print('z = 1/2')
		print('b = -185192999')
		print('c = 0')
		exit(0)
	
	
	if pre_condition_624(a=a,b=b,c=c)==True:
		print("pre_condition_624 SAT")
		print('x = -571')
		print('y = -1')
		print('a = -184220011')
		print('z = -62')
		print('b = -186407738')
		print('c = -476657/2')
		exit(0)
	
	
	if pre_condition_625(a=a,b=b,c=c)==True:
		print("pre_condition_625 SAT")
		print('x = -571')
		print('y = -1')
		print('a = -184220011')
		print('z = -62')
		print('b = -186407738')
		print('c = -476657/2')
		exit(0)
	
	
	if pre_condition_626(a=a,b=b,c=c)==True:
		print("pre_condition_626 SAT")
		print('x = -571')
		print('y = -1')
		print('a = -184220011')
		print('z = -62')
		print('b = -186407738')
		print('c = -476657/2')
		exit(0)
	
	
	if pre_condition_627(a=a,b=b,c=c)==True:
		print("pre_condition_627 SAT")
		print('x = -572')
		print('y = -1')
		print('a = -184220011')
		print('z = -63')
		print('b = -187399294')
		print('c = -500095/2')
		exit(0)
	
	
	if pre_condition_628(a=a,b=b,c=c)==True:
		print("pre_condition_628 SAT")
		print('x = -572')
		print('y = -1')
		print('a = -184220011')
		print('z = -63')
		print('b = -187399294')
		print('c = -500095/2')
		exit(0)
	
	
	if pre_condition_629(a=a,b=b,c=c)==True:
		print("pre_condition_629 SAT")
		print('x = -572')
		print('y = -1')
		print('a = -184220011')
		print('z = -63')
		print('b = -187399294')
		print('c = -500095/2')
		exit(0)
	
	
	if pre_condition_630(a=a,b=b,c=c)==True:
		print("pre_condition_630 SAT")
		print('x = -573')
		print('y = -1')
		print('a = -183250434')
		print('z = -64')
		print('b = -188394660')
		print('c = -524289/2')
		exit(0)
	
	
	if pre_condition_631(a=a,b=b,c=c)==True:
		print("pre_condition_631 SAT")
		print('x = -573')
		print('y = -1')
		print('a = -183250434')
		print('z = -64')
		print('b = -188394660')
		print('c = -524289/2')
		exit(0)
	
	
	if pre_condition_632(a=a,b=b,c=c)==True:
		print("pre_condition_632 SAT")
		print('x = -573')
		print('y = -1')
		print('a = -183250434')
		print('z = -64')
		print('b = -188394660')
		print('c = -524289/2')
		exit(0)
	
	
	if pre_condition_633(a=a,b=b,c=c)==True:
		print("pre_condition_633 SAT")
		print('x = -574')
		print('y = -1')
		print('a = -188132519')
		print('z = -1')
		print('b = -189119224')
		print('c = -3/2')
		exit(0)
	
	
	if pre_condition_634(a=a,b=b,c=c)==True:
		print("pre_condition_634 SAT")
		print('x = -574')
		print('y = -1')
		print('a = -188132519')
		print('z = -1')
		print('b = -189119224')
		print('c = -3/2')
		exit(0)
	
	
	if pre_condition_635(a=a,b=b,c=c)==True:
		print("pre_condition_635 SAT")
		print('x = -574')
		print('y = -1')
		print('a = -188132519')
		print('z = -1')
		print('b = -189119224')
		print('c = -3/2')
		exit(0)
	
	
	if pre_condition_636(a=a,b=b,c=c)==True:
		print("pre_condition_636 SAT")
		print('x = -575')
		print('y = -1')
		print('a = -188132519')
		print('z = -64')
		print('b = -190371518')
		print('c = -524289/2')
		exit(0)
	
	
	if pre_condition_637(a=a,b=b,c=c)==True:
		print("pre_condition_637 SAT")
		print('x = -575')
		print('y = -1')
		print('a = -188132519')
		print('z = -64')
		print('b = -190371518')
		print('c = -524289/2')
		exit(0)
	
	
	if pre_condition_638(a=a,b=b,c=c)==True:
		print("pre_condition_638 SAT")
		print('x = -575')
		print('y = -1')
		print('a = -188132519')
		print('z = -64')
		print('b = -190371518')
		print('c = -524289/2')
		exit(0)
	
	
	if pre_condition_639(a=a,b=b,c=c)==True:
		print("pre_condition_639 SAT")
		print('x = -576')
		print('y = -1')
		print('a = -175616002')
		print('z = -65')
		print('b = -191377600')
		print('c = -549251/2')
		exit(0)
	
	
	if pre_condition_640(a=a,b=b,c=c)==True:
		print("pre_condition_640 SAT")
		print('x = -576')
		print('y = -1')
		print('a = -175616002')
		print('z = -65')
		print('b = -191377600')
		print('c = -549251/2')
		exit(0)
	
	
	if pre_condition_641(a=a,b=b,c=c)==True:
		print("pre_condition_641 SAT")
		print('x = -576')
		print('y = -1')
		print('a = -175616002')
		print('z = -65')
		print('b = -191377600')
		print('c = -549251/2')
		exit(0)
	
	
	if pre_condition_642(a=a,b=b,c=c)==True:
		print("pre_condition_642 SAT")
		print('x = -577')
		print('y = -1')
		print('a = -192100033')
		print('z = -2')
		print('b = -191102985')
		print('c = -17/2')
		exit(0)
	
	
	if pre_condition_643(a=a,b=b,c=c)==True:
		print("pre_condition_643 SAT")
		print('x = -577')
		print('y = -1')
		print('a = -192100033')
		print('z = -2')
		print('b = -191102985')
		print('c = -17/2')
		exit(0)
	
	
	if pre_condition_644(a=a,b=b,c=c)==True:
		print("pre_condition_644 SAT")
		print('x = -577')
		print('y = -1')
		print('a = -192100033')
		print('z = -2')
		print('b = -191102985')
		print('c = -17/2')
		exit(0)
	
	
	if pre_condition_645(a=a,b=b,c=c)==True:
		print("pre_condition_645 SAT")
		print('x = -578')
		print('y = -1')
		print('a = -191102978')
		print('z = -65')
		print('b = -193375176')
		print('c = -549251/2')
		exit(0)
	
	
	if pre_condition_646(a=a,b=b,c=c)==True:
		print("pre_condition_646 SAT")
		print('x = -578')
		print('y = -1')
		print('a = -191102978')
		print('z = -65')
		print('b = -193375176')
		print('c = -549251/2')
		exit(0)
	
	
	if pre_condition_647(a=a,b=b,c=c)==True:
		print("pre_condition_647 SAT")
		print('x = -578')
		print('y = -1')
		print('a = -191102978')
		print('z = -65')
		print('b = -193375176')
		print('c = -549251/2')
		exit(0)
	
	
	if pre_condition_648(a=a,b=b,c=c)==True:
		print("pre_condition_648 SAT")
		print('x = -579')
		print('y = -1')
		print('a = -3869902')
		print('z = -66')
		print('b = -194392034')
		print('c = -574993/2')
		exit(0)


	print("UNKNOWN")
	exit(0)
