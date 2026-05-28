import sympy
from sympy import *

def pre_condition_0(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 1) & (b > -1) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(1)), StrictGreaterThan(Symbol('b'), Integer(-1)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 41/64) & (b > -13/8) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(41, 64)), StrictGreaterThan(Symbol('b'), Rational(-13, 8)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_2(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 553/1024) & (b > -51/32) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(553, 1024)), StrictGreaterThan(Symbol('b'), Rational(-51, 32)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_3(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 8441/16384) & (b > -203/128) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(8441, 16384)), StrictGreaterThan(Symbol('b'), Rational(-203, 128)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_4(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 32953/65536) & (b > -405/256) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(32953, 65536)), StrictGreaterThan(Symbol('b'), Rational(-405, 256)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_5(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_6(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_7(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_8(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_9(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_10(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_11(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_12(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_13(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_14(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_15(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_16(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_17(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_18(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_19(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_20(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_21(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_22(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_23(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_24(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_25(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_26(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_27(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_28(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_29(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_30(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_31(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_32(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_33(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_34(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_35(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_36(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_37(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_38(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_39(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_40(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_41(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_42(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_43(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_44(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_45(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_46(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_47(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_48(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_49(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_50(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_51(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_52(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_53(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_54(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_55(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_56(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_57(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_58(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_59(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_60(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_61(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_62(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_63(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_64(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_65(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_66(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_67(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_68(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_69(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_70(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_71(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_72(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_73(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_74(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_75(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_76(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_77(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_78(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_79(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_80(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_81(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_82(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_83(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_84(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_85(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_86(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_87(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_88(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_89(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_90(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_91(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_92(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_93(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_94(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_95(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_96(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_97(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_98(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_99(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_100(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_101(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_102(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_103(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_104(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_105(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_106(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_107(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_108(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_109(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_110(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_111(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_112(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_113(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_114(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_115(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_116(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_117(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_118(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_119(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_120(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_121(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_122(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_123(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_124(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_125(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_126(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_127(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_128(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_129(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_130(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_131(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_132(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_133(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_134(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_135(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_136(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_137(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_138(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_139(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_140(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_141(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_142(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_143(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_144(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_145(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_146(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_147(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_148(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_149(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_150(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_151(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_152(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_153(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_154(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_155(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_156(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_157(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_158(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_159(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_160(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_161(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_162(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_163(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_164(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_165(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_166(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_167(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_168(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_169(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_170(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_171(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_172(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_173(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_174(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_175(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_176(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_177(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_178(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_179(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_180(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_181(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_182(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_183(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_184(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_185(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_186(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_187(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_188(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_189(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_190(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_191(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_192(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_193(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_194(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_195(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_196(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_197(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_198(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_199(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_200(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_201(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_202(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_203(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_204(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_205(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_206(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_207(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_208(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_209(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_210(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_211(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_212(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_213(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_214(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_215(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_216(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_217(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_218(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_219(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_220(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_221(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_222(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_223(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_224(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_225(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_226(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_227(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_228(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_229(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_230(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_231(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_232(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_233(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_234(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_235(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_236(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_237(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_238(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_239(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_240(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_241(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_242(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_243(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_244(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_245(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_246(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_247(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_248(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_249(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_250(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_251(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_252(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_253(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_254(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_255(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_256(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_257(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_258(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_259(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_260(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_261(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_262(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_263(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_264(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_265(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_266(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_267(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_268(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_269(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_270(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_271(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_272(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_273(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_274(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_275(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_276(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_277(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_278(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_279(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_280(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_281(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_282(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_283(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_284(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_285(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_286(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_287(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_288(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_289(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_290(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_291(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_292(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_293(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_294(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_295(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_296(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_297(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_298(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_299(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_300(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_301(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_302(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_303(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_304(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_305(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_306(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_307(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_308(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_309(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_310(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_311(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_312(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_313(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_314(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_315(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_316(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_317(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_318(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_319(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_320(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_321(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_322(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_323(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_324(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_325(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_326(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_327(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_328(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_329(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_330(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_331(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_332(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_333(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_334(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_335(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_336(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_337(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_338(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_339(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_340(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_341(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_342(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_343(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_344(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_345(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_346(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_347(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_348(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_349(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_350(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_351(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_352(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_353(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_354(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_355(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_356(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_357(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_358(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_359(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_360(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_361(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_362(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_363(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_364(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_365(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_366(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_367(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_368(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_369(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_370(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_371(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_372(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_373(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_374(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_375(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_376(b:sympy.Rational,delta:sympy.Rational):
	#(delta >= 2102513/4194304) & (b > -3239/2048) & (delta >= b**2 - 3) & (delta >= 3 - b**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(2102513, 4194304)), StrictGreaterThan(Symbol('b'), Rational(-3239, 2048)), GreaterThan(Symbol('delta'), Add(Pow(Symbol('b'), Integer(2)), Integer(-3))), GreaterThan(Symbol('delta'), Add(Integer(3), Mul(Integer(-1), Pow(Symbol('b'), Integer(2))))))

	eval = pre_cond.subs( { 'b':b, 'delta':delta })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_377(b:sympy.Rational,delta:sympy.Rational):