import sympy
from sympy import *

def pre_condition_0(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (skoS >= skoSINS) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (delta >= skoSINS**2) & (pi > 2*skoS) & (delta >= -skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), GreaterThan(Symbol('skoS'), Symbol('skoSINS')), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), GreaterThan(Symbol('delta'), Pow(Symbol('skoSINS'), Integer(2))), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), GreaterThan(Symbol('delta'), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 1/64) & (skoS >= 1/8) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(1, 64)), GreaterThan(Symbol('skoS'), Rational(1, 8)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_2(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (skoS >= skoSINS) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & (delta >= skoSINS**2 - 1) & (delta >= 1 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), GreaterThan(Symbol('skoS'), Symbol('skoSINS')), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Integer(-1))), GreaterThan(Symbol('delta'), Add(Integer(1), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_3(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 1) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(1)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_4(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (skoS >= skoSINS) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & (delta >= skoSINS**2 - 511/65536) & (delta >= 511/65536 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), GreaterThan(Symbol('skoS'), Symbol('skoSINS')), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-511, 65536))), GreaterThan(Symbol('delta'), Add(Rational(511, 65536), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_5(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 255/65536) & (skoS >= 1/16) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(255, 65536)), GreaterThan(Symbol('skoS'), Rational(1, 16)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_6(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (skoS >= skoSINS) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & (delta >= skoSINS**2 - 1023/262144) & (delta >= 1023/262144 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), GreaterThan(Symbol('skoS'), Symbol('skoSINS')), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-1023, 262144))), GreaterThan(Symbol('delta'), Add(Rational(1023, 262144), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_7(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 1/262144) & (skoS >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(1, 262144)), GreaterThan(Symbol('skoS'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_8(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (skoS >= skoSINS) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & (delta >= skoSINS**2 - 4095/4194304) & (delta >= 4095/4194304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), GreaterThan(Symbol('skoS'), Symbol('skoSINS')), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4095, 4194304))), GreaterThan(Symbol('delta'), Add(Rational(4095, 4194304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_9(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 1/4194304) & (skoS >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(1, 4194304)), GreaterThan(Symbol('skoS'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_10(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (skoS >= skoSINS) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & (delta >= skoSINS**2 - 16383/67108864) & (delta >= 16383/67108864 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), GreaterThan(Symbol('skoS'), Symbol('skoSINS')), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-16383, 67108864))), GreaterThan(Symbol('delta'), Add(Rational(16383, 67108864), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_11(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 1/67108864) & (skoS >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(1, 67108864)), GreaterThan(Symbol('skoS'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_12(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (skoS >= skoSINS) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & (delta >= skoSINS**2 - 65535/1073741824) & (delta >= 65535/1073741824 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), GreaterThan(Symbol('skoS'), Symbol('skoSINS')), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-65535, 1073741824))), GreaterThan(Symbol('delta'), Add(Rational(65535, 1073741824), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_13(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 1/1073741824) & (skoS >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(1, 1073741824)), GreaterThan(Symbol('skoS'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_14(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (skoS >= skoSINS) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & (delta >= skoSINS**2 - 262143/17179869184) & (delta >= 262143/17179869184 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), GreaterThan(Symbol('skoS'), Symbol('skoSINS')), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-262143, 17179869184))), GreaterThan(Symbol('delta'), Add(Rational(262143, 17179869184), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_15(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 1/17179869184) & (skoS >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(1, 17179869184)), GreaterThan(Symbol('skoS'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_16(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (skoS >= skoSINS) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & (delta >= skoSINS**2 - 1048575/274877906944) & (delta >= 1048575/274877906944 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), GreaterThan(Symbol('skoS'), Symbol('skoSINS')), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-1048575, 274877906944))), GreaterThan(Symbol('delta'), Add(Rational(1048575, 274877906944), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_17(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 1/274877906944) & (skoS >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(1, 274877906944)), GreaterThan(Symbol('skoS'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_18(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (skoS >= skoSINS) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & (delta >= skoSINS**2 - 4194303/4398046511104) & (delta >= 4194303/4398046511104 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), GreaterThan(Symbol('skoS'), Symbol('skoSINS')), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4194303, 4398046511104))), GreaterThan(Symbol('delta'), Add(Rational(4194303, 4398046511104), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_19(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 1/4398046511104) & (skoS >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(1, 4398046511104)), GreaterThan(Symbol('skoS'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_20(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (skoS >= skoSINS) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & (delta >= skoSINS**2 - 16777215/70368744177664) & (delta >= 16777215/70368744177664 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), GreaterThan(Symbol('skoS'), Symbol('skoSINS')), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-16777215, 70368744177664))), GreaterThan(Symbol('delta'), Add(Rational(16777215, 70368744177664), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_21(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 1/70368744177664) & (skoS >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(1, 70368744177664)), GreaterThan(Symbol('skoS'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_22(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (skoS >= skoSINS) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & (delta >= skoSINS**2 - 67108863/1125899906842624) & (delta >= 67108863/1125899906842624 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), GreaterThan(Symbol('skoS'), Symbol('skoSINS')), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-67108863, 1125899906842624))), GreaterThan(Symbol('delta'), Add(Rational(67108863, 1125899906842624), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_23(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 1/1125899906842624) & (skoS >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(1, 1125899906842624)), GreaterThan(Symbol('skoS'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_24(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (skoS >= skoSINS) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & (delta >= skoSINS**2 - 268435455/18014398509481984) & (delta >= 268435455/18014398509481984 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), GreaterThan(Symbol('skoS'), Symbol('skoSINS')), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-268435455, 18014398509481984))), GreaterThan(Symbol('delta'), Add(Rational(268435455, 18014398509481984), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_25(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 1/18014398509481984) & (skoS >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(1, 18014398509481984)), GreaterThan(Symbol('skoS'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_26(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (skoS >= skoSINS) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & (delta >= skoSINS**2 - 1073741823/288230376151711744) & (delta >= 1073741823/288230376151711744 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), GreaterThan(Symbol('skoS'), Symbol('skoSINS')), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-1073741823, 288230376151711744))), GreaterThan(Symbol('delta'), Add(Rational(1073741823, 288230376151711744), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_27(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 1/288230376151711744) & (skoS >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(1, 288230376151711744)), GreaterThan(Symbol('skoS'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_28(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (skoS >= skoSINS) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & (delta >= skoSINS**2 - 4294967295/4611686018427387904) & (delta >= 4294967295/4611686018427387904 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), GreaterThan(Symbol('skoS'), Symbol('skoSINS')), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4294967295, 4611686018427387904))), GreaterThan(Symbol('delta'), Add(Rational(4294967295, 4611686018427387904), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_29(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 1/4611686018427387904) & (skoS >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(1, 4611686018427387904)), GreaterThan(Symbol('skoS'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_30(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (skoS >= skoSINS) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & (delta >= skoSINS**2 - 17179869183/73786976294838206464) & (delta >= 17179869183/73786976294838206464 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), GreaterThan(Symbol('skoS'), Symbol('skoSINS')), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-17179869183, 73786976294838206464))), GreaterThan(Symbol('delta'), Add(Rational(17179869183, 73786976294838206464), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_31(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 1/73786976294838206464) & (skoS >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(1, 73786976294838206464)), GreaterThan(Symbol('skoS'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_32(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (skoS >= skoSINS) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & (delta >= skoSINS**2 - 68719476735/1180591620717411303424) & (delta >= 68719476735/1180591620717411303424 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), GreaterThan(Symbol('skoS'), Symbol('skoSINS')), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-68719476735, 1180591620717411303424))), GreaterThan(Symbol('delta'), Add(Rational(68719476735, 1180591620717411303424), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_33(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 1/1180591620717411303424) & (skoS >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(1, 1180591620717411303424)), GreaterThan(Symbol('skoS'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_34(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (skoS >= skoSINS) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & (delta >= skoSINS**2 - 274877906943/18889465931478580854784) & (delta >= 274877906943/18889465931478580854784 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), GreaterThan(Symbol('skoS'), Symbol('skoSINS')), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-274877906943, 18889465931478580854784))), GreaterThan(Symbol('delta'), Add(Rational(274877906943, 18889465931478580854784), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_35(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 1/18889465931478580854784) & (skoS >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(1, 18889465931478580854784)), GreaterThan(Symbol('skoS'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_36(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (skoS >= skoSINS) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & (delta >= skoSINS**2 - 1099511627775/302231454903657293676544) & (delta >= 1099511627775/302231454903657293676544 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), GreaterThan(Symbol('skoS'), Symbol('skoSINS')), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-1099511627775, 302231454903657293676544))), GreaterThan(Symbol('delta'), Add(Rational(1099511627775, 302231454903657293676544), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_37(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 1/302231454903657293676544) & (skoS >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(1, 302231454903657293676544)), GreaterThan(Symbol('skoS'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_38(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (skoS >= skoSINS) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & (delta >= skoSINS**2 - 4398046511103/4835703278458516698824704) & (delta >= 4398046511103/4835703278458516698824704 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), GreaterThan(Symbol('skoS'), Symbol('skoSINS')), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4398046511103, 4835703278458516698824704))), GreaterThan(Symbol('delta'), Add(Rational(4398046511103, 4835703278458516698824704), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_39(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 1/4835703278458516698824704) & (skoS >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(1, 4835703278458516698824704)), GreaterThan(Symbol('skoS'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_40(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (skoS >= skoSINS) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & (delta >= skoSINS**2 - 17592186044415/77371252455336267181195264) & (delta >= 17592186044415/77371252455336267181195264 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), GreaterThan(Symbol('skoS'), Symbol('skoSINS')), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-17592186044415, 77371252455336267181195264))), GreaterThan(Symbol('delta'), Add(Rational(17592186044415, 77371252455336267181195264), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_41(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 1/77371252455336267181195264) & (skoS >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(1, 77371252455336267181195264)), GreaterThan(Symbol('skoS'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_42(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (skoS >= skoSINS) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & (delta >= skoSINS**2 - 70368744177663/1237940039285380274899124224) & (delta >= 70368744177663/1237940039285380274899124224 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), GreaterThan(Symbol('skoS'), Symbol('skoSINS')), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-70368744177663, 1237940039285380274899124224))), GreaterThan(Symbol('delta'), Add(Rational(70368744177663, 1237940039285380274899124224), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_43(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 1/1237940039285380274899124224) & (skoS >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(1, 1237940039285380274899124224)), GreaterThan(Symbol('skoS'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_44(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (skoS >= skoSINS) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & (delta >= skoSINS**2 - 281474976710655/19807040628566084398385987584) & (delta >= 281474976710655/19807040628566084398385987584 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), GreaterThan(Symbol('skoS'), Symbol('skoSINS')), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-281474976710655, 19807040628566084398385987584))), GreaterThan(Symbol('delta'), Add(Rational(281474976710655, 19807040628566084398385987584), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_45(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 1/19807040628566084398385987584) & (skoS >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(1, 19807040628566084398385987584)), GreaterThan(Symbol('skoS'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_46(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (skoS >= skoSINS) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & (delta >= skoSINS**2 - 1125899906842623/316912650057057350374175801344) & (delta >= 1125899906842623/316912650057057350374175801344 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), GreaterThan(Symbol('skoS'), Symbol('skoSINS')), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-1125899906842623, 316912650057057350374175801344))), GreaterThan(Symbol('delta'), Add(Rational(1125899906842623, 316912650057057350374175801344), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_47(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 1/316912650057057350374175801344) & (skoS >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(1, 316912650057057350374175801344)), GreaterThan(Symbol('skoS'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_48(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (skoS >= skoSINS) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & (delta >= skoSINS**2 - 4503599627370495/5070602400912917605986812821504) & (delta >= 4503599627370495/5070602400912917605986812821504 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), GreaterThan(Symbol('skoS'), Symbol('skoSINS')), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-4503599627370495, 5070602400912917605986812821504))), GreaterThan(Symbol('delta'), Add(Rational(4503599627370495, 5070602400912917605986812821504), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_49(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 1/5070602400912917605986812821504) & (skoS >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(1, 5070602400912917605986812821504)), GreaterThan(Symbol('skoS'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_50(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (skoS >= skoSINS) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & (delta >= skoSINS**2 - 18014398509481983/81129638414606681695789005144064) & (delta >= 18014398509481983/81129638414606681695789005144064 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), GreaterThan(Symbol('skoS'), Symbol('skoSINS')), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-18014398509481983, 81129638414606681695789005144064))), GreaterThan(Symbol('delta'), Add(Rational(18014398509481983, 81129638414606681695789005144064), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_51(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 1/81129638414606681695789005144064) & (skoS >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(1, 81129638414606681695789005144064)), GreaterThan(Symbol('skoS'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_52(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (skoS >= skoSINS) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & (delta >= skoSINS**2 - 72057594037927935/1298074214633706907132624082305024) & (delta >= 72057594037927935/1298074214633706907132624082305024 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), GreaterThan(Symbol('skoS'), Symbol('skoSINS')), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-72057594037927935, 1298074214633706907132624082305024))), GreaterThan(Symbol('delta'), Add(Rational(72057594037927935, 1298074214633706907132624082305024), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_53(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 1/1298074214633706907132624082305024) & (skoS >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(1, 1298074214633706907132624082305024)), GreaterThan(Symbol('skoS'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_54(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (skoS >= skoSINS) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & (delta >= skoSINS**2 - 93536104789177788063110043927548948333009727127551/1684996666696914987166688442938726917102321526408785780068975640576) & (delta >= 93536104789177788063110043927548948333009727127551/1684996666696914987166688442938726917102321526408785780068975640576 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), GreaterThan(Symbol('skoS'), Symbol('skoSINS')), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-93536104789177788063110043927548948333009727127551, 1684996666696914987166688442938726917102321526408785780068975640576))), GreaterThan(Symbol('delta'), Add(Rational(93536104789177788063110043927548948333009727127551, 1684996666696914987166688442938726917102321526408785780068975640576), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_55(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 1298074214633706835075030044377087/1684996666696914987166688442938726917102321526408785780068975640576) & (skoS >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(1298074214633706835075030044377087, 1684996666696914987166688442938726917102321526408785780068975640576)), GreaterThan(Symbol('skoS'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_56(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (skoS >= skoSINS) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & (delta >= skoSINS**2 - 374144419156711147060143317175368308916730655145983/6739986666787659948666753771754907668409286105635143120275902562304) & (delta >= 374144419156711147060143317175368308916730655145983/6739986666787659948666753771754907668409286105635143120275902562304 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), GreaterThan(Symbol('skoS'), Symbol('skoSINS')), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-374144419156711147060143317175368308916730655145983, 6739986666787659948666753771754907668409286105635143120275902562304))), GreaterThan(Symbol('delta'), Add(Rational(374144419156711147060143317175368308916730655145983, 6739986666787659948666753771754907668409286105635143120275902562304), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_57(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 144115188075855873/6739986666787659948666753771754907668409286105635143120275902562304) & (skoS >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(144115188075855873, 6739986666787659948666753771754907668409286105635143120275902562304)), GreaterThan(Symbol('skoS'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_58(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (skoS >= skoSINS) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & (delta >= skoSINS**2 - 121416805764108066932466369176469978433202822029649181929169996689161069613962756095/2187250724783011924372502227117621365353169430893212436425770606409952999199375923223513177023053824) & (delta >= 121416805764108066932466369176469978433202822029649181929169996689161069613962756095/2187250724783011924372502227117621365353169430893212436425770606409952999199375923223513177023053824 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), GreaterThan(Symbol('skoS'), Symbol('skoSINS')), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-121416805764108066932466369176469978433202822029649181929169996689161069613962756095, 2187250724783011924372502227117621365353169430893212436425770606409952999199375923223513177023053824))), GreaterThan(Symbol('delta'), Add(Rational(121416805764108066932466369176469978433202822029649181929169996689161069613962756095, 2187250724783011924372502227117621365353169430893212436425770606409952999199375923223513177023053824), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_59(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 46768052394588890461850931721080479551788637224959/2187250724783011924372502227117621365353169430893212436425770606409952999199375923223513177023053824) & (skoS >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(46768052394588890461850931721080479551788637224959, 2187250724783011924372502227117621365353169430893212436425770606409952999199375923223513177023053824)), GreaterThan(Symbol('skoS'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_60(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (skoS >= skoSINS) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & (delta >= skoSINS**2 - 485667223056432267729865476705879726660601709763028389941879933900118350586852671487/8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296) & (delta >= 485667223056432267729865476705879726660601709763028389941879933900118350586852671487/8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), GreaterThan(Symbol('skoS'), Symbol('skoSINS')), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-485667223056432267729865476705879726660601709763028389941879933900118350586852671487, 8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296))), GreaterThan(Symbol('delta'), Add(Rational(485667223056432267729865476705879726660601709763028389941879933900118350586852671487, 8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_61(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 6490371073168534607720714449453057/8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296) & (skoS >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(6490371073168534607720714449453057, 8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296)), GreaterThan(Symbol('skoS'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_62(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (skoS >= skoSINS) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & (delta >= skoSINS**2 - 485667223056432267729865476705879726660601709763028389941879933900118350586852671487/8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296) & (delta >= 485667223056432267729865476705879726660601709763028389941879933900118350586852671487/8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), GreaterThan(Symbol('skoS'), Symbol('skoSINS')), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-485667223056432267729865476705879726660601709763028389941879933900118350586852671487, 8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296))), GreaterThan(Symbol('delta'), Add(Rational(485667223056432267729865476705879726660601709763028389941879933900118350586852671487, 8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_63(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 6490371073168534607720714449453057/8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296) & (skoS >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(6490371073168534607720714449453057, 8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296)), GreaterThan(Symbol('skoS'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_64(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (skoS >= skoSINS) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & (delta >= skoSINS**2 - 485667223056432267729865476705879726660601709763028389941879933900118350586852671487/8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296) & (delta >= 485667223056432267729865476705879726660601709763028389941879933900118350586852671487/8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), GreaterThan(Symbol('skoS'), Symbol('skoSINS')), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-485667223056432267729865476705879726660601709763028389941879933900118350586852671487, 8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296))), GreaterThan(Symbol('delta'), Add(Rational(485667223056432267729865476705879726660601709763028389941879933900118350586852671487, 8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_65(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 6490371073168534607720714449453057/8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296) & (skoS >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(6490371073168534607720714449453057, 8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296)), GreaterThan(Symbol('skoS'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_66(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (skoS >= skoSINS) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & (delta >= skoSINS**2 - 485667223056432267729865476705879726660601709763028389941879933900118350586852671487/8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296) & (delta >= 485667223056432267729865476705879726660601709763028389941879933900118350586852671487/8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), GreaterThan(Symbol('skoS'), Symbol('skoSINS')), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-485667223056432267729865476705879726660601709763028389941879933900118350586852671487, 8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296))), GreaterThan(Symbol('delta'), Add(Rational(485667223056432267729865476705879726660601709763028389941879933900118350586852671487, 8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_67(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 6490371073168534607720714449453057/8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296) & (skoS >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(6490371073168534607720714449453057, 8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296)), GreaterThan(Symbol('skoS'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_68(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (skoS >= skoSINS) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & (delta >= skoSINS**2 - 485667223056432267729865476705879726660601709763028389941879933900118350586852671487/8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296) & (delta >= 485667223056432267729865476705879726660601709763028389941879933900118350586852671487/8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), GreaterThan(Symbol('skoS'), Symbol('skoSINS')), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-485667223056432267729865476705879726660601709763028389941879933900118350586852671487, 8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296))), GreaterThan(Symbol('delta'), Add(Rational(485667223056432267729865476705879726660601709763028389941879933900118350586852671487, 8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_69(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 6490371073168534607720714449453057/8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296) & (skoS >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(6490371073168534607720714449453057, 8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296)), GreaterThan(Symbol('skoS'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_70(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (skoS >= skoSINS) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & (delta >= skoSINS**2 - 485667223056432267729865476705879726660601709763028389941879933900118350586852671487/8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296) & (delta >= 485667223056432267729865476705879726660601709763028389941879933900118350586852671487/8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), GreaterThan(Symbol('skoS'), Symbol('skoSINS')), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-485667223056432267729865476705879726660601709763028389941879933900118350586852671487, 8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296))), GreaterThan(Symbol('delta'), Add(Rational(485667223056432267729865476705879726660601709763028389941879933900118350586852671487, 8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_71(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 6490371073168534607720714449453057/8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296) & (skoS >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(6490371073168534607720714449453057, 8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296)), GreaterThan(Symbol('skoS'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_72(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (skoS >= skoSINS) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & (delta >= skoSINS**2 - 485667223056432267729865476705879726660601709763028389941879933900118350586852671487/8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296) & (delta >= 485667223056432267729865476705879726660601709763028389941879933900118350586852671487/8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), GreaterThan(Symbol('skoS'), Symbol('skoSINS')), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-485667223056432267729865476705879726660601709763028389941879933900118350586852671487, 8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296))), GreaterThan(Symbol('delta'), Add(Rational(485667223056432267729865476705879726660601709763028389941879933900118350586852671487, 8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_73(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 6490371073168534607720714449453057/8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296) & (skoS >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(6490371073168534607720714449453057, 8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296)), GreaterThan(Symbol('skoS'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_74(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (skoS >= skoSINS) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & (delta >= skoSINS**2 - 485667223056432267729865476705879726660601709763028389941879933900118350586852671487/8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296) & (delta >= 485667223056432267729865476705879726660601709763028389941879933900118350586852671487/8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), GreaterThan(Symbol('skoS'), Symbol('skoSINS')), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-485667223056432267729865476705879726660601709763028389941879933900118350586852671487, 8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296))), GreaterThan(Symbol('delta'), Add(Rational(485667223056432267729865476705879726660601709763028389941879933900118350586852671487, 8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_75(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 6490371073168534607720714449453057/8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296) & (skoS >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(6490371073168534607720714449453057, 8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296)), GreaterThan(Symbol('skoS'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_76(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (skoS >= skoSINS) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & (delta >= skoSINS**2 - 485667223056432267729865476705879726660601709763028389941879933900118350586852671487/8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296) & (delta >= 485667223056432267729865476705879726660601709763028389941879933900118350586852671487/8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), GreaterThan(Symbol('skoS'), Symbol('skoSINS')), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-485667223056432267729865476705879726660601709763028389941879933900118350586852671487, 8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296))), GreaterThan(Symbol('delta'), Add(Rational(485667223056432267729865476705879726660601709763028389941879933900118350586852671487, 8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_77(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 6490371073168534607720714449453057/8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296) & (skoS >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(6490371073168534607720714449453057, 8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296)), GreaterThan(Symbol('skoS'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_78(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (skoS >= skoSINS) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & (delta >= skoSINS**2 - 485667223056432267729865476705879726660601709763028389941879933900118350586852671487/8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296) & (delta >= 485667223056432267729865476705879726660601709763028389941879933900118350586852671487/8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), GreaterThan(Symbol('skoS'), Symbol('skoSINS')), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-485667223056432267729865476705879726660601709763028389941879933900118350586852671487, 8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296))), GreaterThan(Symbol('delta'), Add(Rational(485667223056432267729865476705879726660601709763028389941879933900118350586852671487, 8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_79(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 6490371073168534607720714449453057/8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296) & (skoS >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(6490371073168534607720714449453057, 8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296)), GreaterThan(Symbol('skoS'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_80(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (skoS >= skoSINS) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & (delta >= skoSINS**2 - 485667223056432267729865476705879726660601709763028389941879933900118350586852671487/8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296) & (delta >= 485667223056432267729865476705879726660601709763028389941879933900118350586852671487/8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), GreaterThan(Symbol('skoS'), Symbol('skoSINS')), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-485667223056432267729865476705879726660601709763028389941879933900118350586852671487, 8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296))), GreaterThan(Symbol('delta'), Add(Rational(485667223056432267729865476705879726660601709763028389941879933900118350586852671487, 8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_81(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 6490371073168534607720714449453057/8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296) & (skoS >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(6490371073168534607720714449453057, 8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296)), GreaterThan(Symbol('skoS'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_82(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (skoS >= skoSINS) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & (delta >= skoSINS**2 - 485667223056432267729865476705879726660601709763028389941879933900118350586852671487/8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296) & (delta >= 485667223056432267729865476705879726660601709763028389941879933900118350586852671487/8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), GreaterThan(Symbol('skoS'), Symbol('skoSINS')), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-485667223056432267729865476705879726660601709763028389941879933900118350586852671487, 8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296))), GreaterThan(Symbol('delta'), Add(Rational(485667223056432267729865476705879726660601709763028389941879933900118350586852671487, 8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_83(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 6490371073168534607720714449453057/8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296) & (skoS >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(6490371073168534607720714449453057, 8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296)), GreaterThan(Symbol('skoS'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_84(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (skoS >= skoSINS) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & (delta >= skoSINS**2 - 485667223056432267729865476705879726660601709763028389941879933900118350586852671487/8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296) & (delta >= 485667223056432267729865476705879726660601709763028389941879933900118350586852671487/8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), GreaterThan(Symbol('skoS'), Symbol('skoSINS')), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-485667223056432267729865476705879726660601709763028389941879933900118350586852671487, 8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296))), GreaterThan(Symbol('delta'), Add(Rational(485667223056432267729865476705879726660601709763028389941879933900118350586852671487, 8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_85(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 6490371073168534607720714449453057/8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296) & (skoS >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(6490371073168534607720714449453057, 8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296)), GreaterThan(Symbol('skoS'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_86(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (skoS >= skoSINS) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & (delta >= skoSINS**2 - 485667223056432267729865476705879726660601709763028389941879933900118350586852671487/8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296) & (delta >= 485667223056432267729865476705879726660601709763028389941879933900118350586852671487/8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), GreaterThan(Symbol('skoS'), Symbol('skoSINS')), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-485667223056432267729865476705879726660601709763028389941879933900118350586852671487, 8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296))), GreaterThan(Symbol('delta'), Add(Rational(485667223056432267729865476705879726660601709763028389941879933900118350586852671487, 8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_87(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 6490371073168534607720714449453057/8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296) & (skoS >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(6490371073168534607720714449453057, 8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296)), GreaterThan(Symbol('skoS'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_88(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (skoS >= skoSINS) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & (delta >= skoSINS**2 - 485667223056432267729865476705879726660601709763028389941879933900118350586852671487/8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296) & (delta >= 485667223056432267729865476705879726660601709763028389941879933900118350586852671487/8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), GreaterThan(Symbol('skoS'), Symbol('skoSINS')), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-485667223056432267729865476705879726660601709763028389941879933900118350586852671487, 8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296))), GreaterThan(Symbol('delta'), Add(Rational(485667223056432267729865476705879726660601709763028389941879933900118350586852671487, 8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_89(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 6490371073168534607720714449453057/8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296) & (skoS >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(6490371073168534607720714449453057, 8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296)), GreaterThan(Symbol('skoS'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_90(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (skoS >= skoSINS) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & (delta >= skoSINS**2 - 485667223056432267729865476705879726660601709763028389941879933900118350586852671487/8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296) & (delta >= 485667223056432267729865476705879726660601709763028389941879933900118350586852671487/8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), GreaterThan(Symbol('skoS'), Symbol('skoSINS')), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-485667223056432267729865476705879726660601709763028389941879933900118350586852671487, 8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296))), GreaterThan(Symbol('delta'), Add(Rational(485667223056432267729865476705879726660601709763028389941879933900118350586852671487, 8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_91(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 6490371073168534607720714449453057/8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296) & (skoS >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(6490371073168534607720714449453057, 8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296)), GreaterThan(Symbol('skoS'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_92(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (skoS >= skoSINS) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & (delta >= skoSINS**2 - 485667223056432267729865476705879726660601709763028389941879933900118350586852671487/8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296) & (delta >= 485667223056432267729865476705879726660601709763028389941879933900118350586852671487/8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), GreaterThan(Symbol('skoS'), Symbol('skoSINS')), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-485667223056432267729865476705879726660601709763028389941879933900118350586852671487, 8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296))), GreaterThan(Symbol('delta'), Add(Rational(485667223056432267729865476705879726660601709763028389941879933900118350586852671487, 8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_93(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 6490371073168534607720714449453057/8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296) & (skoS >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(6490371073168534607720714449453057, 8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296)), GreaterThan(Symbol('skoS'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_94(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (skoS >= skoSINS) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & (delta >= skoSINS**2 - 485667223056432267729865476705879726660601709763028389941879933900118350586852671487/8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296) & (delta >= 485667223056432267729865476705879726660601709763028389941879933900118350586852671487/8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), GreaterThan(Symbol('skoS'), Symbol('skoSINS')), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-485667223056432267729865476705879726660601709763028389941879933900118350586852671487, 8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296))), GreaterThan(Symbol('delta'), Add(Rational(485667223056432267729865476705879726660601709763028389941879933900118350586852671487, 8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_95(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 6490371073168534607720714449453057/8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296) & (skoS >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(6490371073168534607720714449453057, 8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296)), GreaterThan(Symbol('skoS'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_96(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (skoS >= skoSINS) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & (delta >= skoSINS**2 - 485667223056432267729865476705879726660601709763028389941879933900118350586852671487/8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296) & (delta >= 485667223056432267729865476705879726660601709763028389941879933900118350586852671487/8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), GreaterThan(Symbol('skoS'), Symbol('skoSINS')), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-485667223056432267729865476705879726660601709763028389941879933900118350586852671487, 8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296))), GreaterThan(Symbol('delta'), Add(Rational(485667223056432267729865476705879726660601709763028389941879933900118350586852671487, 8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_97(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 6490371073168534607720714449453057/8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296) & (skoS >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(6490371073168534607720714449453057, 8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296)), GreaterThan(Symbol('skoS'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_98(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (skoS >= skoSINS) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & (delta >= skoSINS**2 - 485667223056432267729865476705879726660601709763028389941879933900118350586852671487/8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296) & (delta >= 485667223056432267729865476705879726660601709763028389941879933900118350586852671487/8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), GreaterThan(Symbol('skoS'), Symbol('skoSINS')), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-485667223056432267729865476705879726660601709763028389941879933900118350586852671487, 8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296))), GreaterThan(Symbol('delta'), Add(Rational(485667223056432267729865476705879726660601709763028389941879933900118350586852671487, 8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_99(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 6490371073168534607720714449453057/8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296) & (skoS >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(6490371073168534607720714449453057, 8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296)), GreaterThan(Symbol('skoS'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_100(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (skoS >= skoSINS) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & (delta >= skoSINS**2 - 485667223056432267729865476705879726660601709763028389941879933900118350586852671487/8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296) & (delta >= 485667223056432267729865476705879726660601709763028389941879933900118350586852671487/8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), GreaterThan(Symbol('skoS'), Symbol('skoSINS')), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-485667223056432267729865476705879726660601709763028389941879933900118350586852671487, 8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296))), GreaterThan(Symbol('delta'), Add(Rational(485667223056432267729865476705879726660601709763028389941879933900118350586852671487, 8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_101(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 6490371073168534607720714449453057/8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296) & (skoS >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(6490371073168534607720714449453057, 8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296)), GreaterThan(Symbol('skoS'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_102(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (skoS >= skoSINS) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & (delta >= skoSINS**2 - 485667223056432267729865476705879726660601709763028389941879933900118350586852671487/8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296) & (delta >= 485667223056432267729865476705879726660601709763028389941879933900118350586852671487/8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), GreaterThan(Symbol('skoS'), Symbol('skoSINS')), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-485667223056432267729865476705879726660601709763028389941879933900118350586852671487, 8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296))), GreaterThan(Symbol('delta'), Add(Rational(485667223056432267729865476705879726660601709763028389941879933900118350586852671487, 8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_103(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 6490371073168534607720714449453057/8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296) & (skoS >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(6490371073168534607720714449453057, 8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296)), GreaterThan(Symbol('skoS'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_104(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (skoS >= skoSINS) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & (delta >= skoSINS**2 - 485667223056432267729865476705879726660601709763028389941879933900118350586852671487/8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296) & (delta >= 485667223056432267729865476705879726660601709763028389941879933900118350586852671487/8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), GreaterThan(Symbol('skoS'), Symbol('skoSINS')), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-485667223056432267729865476705879726660601709763028389941879933900118350586852671487, 8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296))), GreaterThan(Symbol('delta'), Add(Rational(485667223056432267729865476705879726660601709763028389941879933900118350586852671487, 8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_105(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 6490371073168534607720714449453057/8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296) & (skoS >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(6490371073168534607720714449453057, 8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296)), GreaterThan(Symbol('skoS'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_106(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (skoS >= skoSINS) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & (delta >= skoSINS**2 - 485667223056432267729865476705879726660601709763028389941879933900118350586852671487/8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296) & (delta >= 485667223056432267729865476705879726660601709763028389941879933900118350586852671487/8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), GreaterThan(Symbol('skoS'), Symbol('skoSINS')), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-485667223056432267729865476705879726660601709763028389941879933900118350586852671487, 8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296))), GreaterThan(Symbol('delta'), Add(Rational(485667223056432267729865476705879726660601709763028389941879933900118350586852671487, 8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_107(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 6490371073168534607720714449453057/8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296) & (skoS >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(6490371073168534607720714449453057, 8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296)), GreaterThan(Symbol('skoS'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_108(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (skoS >= skoSINS) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & (delta >= skoSINS**2 - 485667223056432267729865476705879726660601709763028389941879933900118350586852671487/8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296) & (delta >= 485667223056432267729865476705879726660601709763028389941879933900118350586852671487/8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), GreaterThan(Symbol('skoS'), Symbol('skoSINS')), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-485667223056432267729865476705879726660601709763028389941879933900118350586852671487, 8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296))), GreaterThan(Symbol('delta'), Add(Rational(485667223056432267729865476705879726660601709763028389941879933900118350586852671487, 8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_109(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 6490371073168534607720714449453057/8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296) & (skoS >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(6490371073168534607720714449453057, 8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296)), GreaterThan(Symbol('skoS'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_110(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (skoS >= skoSINS) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & (delta >= skoSINS**2 - 485667223056432267729865476705879726660601709763028389941879933900118350586852671487/8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296) & (delta >= 485667223056432267729865476705879726660601709763028389941879933900118350586852671487/8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), GreaterThan(Symbol('skoS'), Symbol('skoSINS')), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-485667223056432267729865476705879726660601709763028389941879933900118350586852671487, 8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296))), GreaterThan(Symbol('delta'), Add(Rational(485667223056432267729865476705879726660601709763028389941879933900118350586852671487, 8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_111(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 6490371073168534607720714449453057/8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296) & (skoS >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(6490371073168534607720714449453057, 8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296)), GreaterThan(Symbol('skoS'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_112(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (skoS >= skoSINS) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & (delta >= skoSINS**2 - 485667223056432267729865476705879726660601709763028389941879933900118350586852671487/8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296) & (delta >= 485667223056432267729865476705879726660601709763028389941879933900118350586852671487/8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), GreaterThan(Symbol('skoS'), Symbol('skoSINS')), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-485667223056432267729865476705879726660601709763028389941879933900118350586852671487, 8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296))), GreaterThan(Symbol('delta'), Add(Rational(485667223056432267729865476705879726660601709763028389941879933900118350586852671487, 8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_113(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 6490371073168534607720714449453057/8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296) & (skoS >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(6490371073168534607720714449453057, 8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296)), GreaterThan(Symbol('skoS'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_114(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (skoS >= skoSINS) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & (delta >= skoSINS**2 - 485667223056432267729865476705879726660601709763028389941879933900118350586852671487/8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296) & (delta >= 485667223056432267729865476705879726660601709763028389941879933900118350586852671487/8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), GreaterThan(Symbol('skoS'), Symbol('skoSINS')), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-485667223056432267729865476705879726660601709763028389941879933900118350586852671487, 8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296))), GreaterThan(Symbol('delta'), Add(Rational(485667223056432267729865476705879726660601709763028389941879933900118350586852671487, 8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_115(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 6490371073168534607720714449453057/8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296) & (skoS >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(6490371073168534607720714449453057, 8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296)), GreaterThan(Symbol('skoS'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_116(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (skoS >= skoSINS) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & (delta >= skoSINS**2 - 485667223056432267729865476705879726660601709763028389941879933900118350586852671487/8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296) & (delta >= 485667223056432267729865476705879726660601709763028389941879933900118350586852671487/8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), GreaterThan(Symbol('skoS'), Symbol('skoSINS')), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-485667223056432267729865476705879726660601709763028389941879933900118350586852671487, 8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296))), GreaterThan(Symbol('delta'), Add(Rational(485667223056432267729865476705879726660601709763028389941879933900118350586852671487, 8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_117(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 6490371073168534607720714449453057/8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296) & (skoS >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(6490371073168534607720714449453057, 8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296)), GreaterThan(Symbol('skoS'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_118(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (skoS >= skoSINS) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & (delta >= skoSINS**2 - 485667223056432267729865476705879726660601709763028389941879933900118350586852671487/8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296) & (delta >= 485667223056432267729865476705879726660601709763028389941879933900118350586852671487/8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), GreaterThan(Symbol('skoS'), Symbol('skoSINS')), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-485667223056432267729865476705879726660601709763028389941879933900118350586852671487, 8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296))), GreaterThan(Symbol('delta'), Add(Rational(485667223056432267729865476705879726660601709763028389941879933900118350586852671487, 8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_119(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 6490371073168534607720714449453057/8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296) & (skoS >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(6490371073168534607720714449453057, 8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296)), GreaterThan(Symbol('skoS'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_120(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (skoS >= skoSINS) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & (delta >= skoSINS**2 - 485667223056432267729865476705879726660601709763028389941879933900118350586852671487/8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296) & (delta >= 485667223056432267729865476705879726660601709763028389941879933900118350586852671487/8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), GreaterThan(Symbol('skoS'), Symbol('skoSINS')), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-485667223056432267729865476705879726660601709763028389941879933900118350586852671487, 8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296))), GreaterThan(Symbol('delta'), Add(Rational(485667223056432267729865476705879726660601709763028389941879933900118350586852671487, 8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_121(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 6490371073168534607720714449453057/8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296) & (skoS >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(6490371073168534607720714449453057, 8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296)), GreaterThan(Symbol('skoS'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_122(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (skoS >= skoSINS) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & (delta >= skoSINS**2 - 485667223056432267729865476705879726660601709763028389941879933900118350586852671487/8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296) & (delta >= 485667223056432267729865476705879726660601709763028389941879933900118350586852671487/8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), GreaterThan(Symbol('skoS'), Symbol('skoSINS')), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-485667223056432267729865476705879726660601709763028389941879933900118350586852671487, 8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296))), GreaterThan(Symbol('delta'), Add(Rational(485667223056432267729865476705879726660601709763028389941879933900118350586852671487, 8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_123(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 6490371073168534607720714449453057/8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296) & (skoS >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(6490371073168534607720714449453057, 8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296)), GreaterThan(Symbol('skoS'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_124(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (skoS >= skoSINS) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & (delta >= skoSINS**2 - 485667223056432267729865476705879726660601709763028389941879933900118350586852671487/8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296) & (delta >= 485667223056432267729865476705879726660601709763028389941879933900118350586852671487/8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), GreaterThan(Symbol('skoS'), Symbol('skoSINS')), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-485667223056432267729865476705879726660601709763028389941879933900118350586852671487, 8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296))), GreaterThan(Symbol('delta'), Add(Rational(485667223056432267729865476705879726660601709763028389941879933900118350586852671487, 8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_125(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 6490371073168534607720714449453057/8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296) & (skoS >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(6490371073168534607720714449453057, 8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296)), GreaterThan(Symbol('skoS'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_126(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (skoS >= skoSINS) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & (delta >= skoSINS**2 - 485667223056432267729865476705879726660601709763028389941879933900118350586852671487/8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296) & (delta >= 485667223056432267729865476705879726660601709763028389941879933900118350586852671487/8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), GreaterThan(Symbol('skoS'), Symbol('skoSINS')), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-485667223056432267729865476705879726660601709763028389941879933900118350586852671487, 8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296))), GreaterThan(Symbol('delta'), Add(Rational(485667223056432267729865476705879726660601709763028389941879933900118350586852671487, 8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_127(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 6490371073168534607720714449453057/8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296) & (skoS >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(6490371073168534607720714449453057, 8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296)), GreaterThan(Symbol('skoS'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_128(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (skoS >= skoSINS) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & (delta >= skoSINS**2 - 485667223056432267729865476705879726660601709763028389941879933900118350586852671487/8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296) & (delta >= 485667223056432267729865476705879726660601709763028389941879933900118350586852671487/8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), GreaterThan(Symbol('skoS'), Symbol('skoSINS')), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-485667223056432267729865476705879726660601709763028389941879933900118350586852671487, 8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296))), GreaterThan(Symbol('delta'), Add(Rational(485667223056432267729865476705879726660601709763028389941879933900118350586852671487, 8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_129(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 6490371073168534607720714449453057/8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296) & (skoS >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(6490371073168534607720714449453057, 8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296)), GreaterThan(Symbol('skoS'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_130(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (skoS >= skoSINS) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & (delta >= skoSINS**2 - 485667223056432267729865476705879726660601709763028389941879933900118350586852671487/8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296) & (delta >= 485667223056432267729865476705879726660601709763028389941879933900118350586852671487/8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), GreaterThan(Symbol('skoS'), Symbol('skoSINS')), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-485667223056432267729865476705879726660601709763028389941879933900118350586852671487, 8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296))), GreaterThan(Symbol('delta'), Add(Rational(485667223056432267729865476705879726660601709763028389941879933900118350586852671487, 8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_131(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 6490371073168534607720714449453057/8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296) & (skoS >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(6490371073168534607720714449453057, 8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296)), GreaterThan(Symbol('skoS'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_132(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (skoS >= skoSINS) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & (delta >= skoSINS**2 - 485667223056432267729865476705879726660601709763028389941879933900118350586852671487/8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296) & (delta >= 485667223056432267729865476705879726660601709763028389941879933900118350586852671487/8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), GreaterThan(Symbol('skoS'), Symbol('skoSINS')), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-485667223056432267729865476705879726660601709763028389941879933900118350586852671487, 8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296))), GreaterThan(Symbol('delta'), Add(Rational(485667223056432267729865476705879726660601709763028389941879933900118350586852671487, 8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_133(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 6490371073168534607720714449453057/8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296) & (skoS >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(6490371073168534607720714449453057, 8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296)), GreaterThan(Symbol('skoS'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_134(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (skoS >= skoSINS) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & (delta >= skoSINS**2 - 485667223056432267729865476705879726660601709763028389941879933900118350586852671487/8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296) & (delta >= 485667223056432267729865476705879726660601709763028389941879933900118350586852671487/8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), GreaterThan(Symbol('skoS'), Symbol('skoSINS')), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-485667223056432267729865476705879726660601709763028389941879933900118350586852671487, 8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296))), GreaterThan(Symbol('delta'), Add(Rational(485667223056432267729865476705879726660601709763028389941879933900118350586852671487, 8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_135(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 6490371073168534607720714449453057/8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296) & (skoS >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(6490371073168534607720714449453057, 8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296)), GreaterThan(Symbol('skoS'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_136(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (skoS >= skoSINS) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & (delta >= skoSINS**2 - 485667223056432267729865476705879726660601709763028389941879933900118350586852671487/8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296) & (delta >= 485667223056432267729865476705879726660601709763028389941879933900118350586852671487/8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), GreaterThan(Symbol('skoS'), Symbol('skoSINS')), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-485667223056432267729865476705879726660601709763028389941879933900118350586852671487, 8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296))), GreaterThan(Symbol('delta'), Add(Rational(485667223056432267729865476705879726660601709763028389941879933900118350586852671487, 8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_137(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 6490371073168534607720714449453057/8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296) & (skoS >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(6490371073168534607720714449453057, 8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296)), GreaterThan(Symbol('skoS'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_138(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (skoS >= 0) & (skoS >= skoSINS) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS) & (delta >= skoSINS**2 - 485667223056432267729865476705879726660601709763028389941879933900118350586852671487/8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296) & (delta >= 485667223056432267729865476705879726660601709763028389941879933900118350586852671487/8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296 - skoSINS**2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), GreaterThan(Symbol('skoS'), Integer(0)), GreaterThan(Symbol('skoS'), Symbol('skoSINS')), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))), GreaterThan(Symbol('delta'), Add(Pow(Symbol('skoSINS'), Integer(2)), Rational(-485667223056432267729865476705879726660601709763028389941879933900118350586852671487, 8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296))), GreaterThan(Symbol('delta'), Add(Rational(485667223056432267729865476705879726660601709763028389941879933900118350586852671487, 8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_139(delta:sympy.Rational,skoS:sympy.Rational,pi:sympy.Rational):
	#(delta >= 6490371073168534607720714449453057/8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296) & (skoS >= 0) & (pi > 15707963/5000000) & (pi < 31415927/10000000) & (pi > 2*skoS)

	pre_cond = And(GreaterThan(Symbol('delta'), Rational(6490371073168534607720714449453057, 8749002899132047697490008908470485461412677723572849745703082425639811996797503692894052708092215296)), GreaterThan(Symbol('skoS'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictGreaterThan(Symbol('pi'), Mul(Integer(2), Symbol('skoS'))))

	eval = pre_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def post_condition(delta:sympy.Rational, skoS:sympy.Rational, pi:sympy.Rational, skoCOSS:sympy.Rational, skoSINS:sympy.Rational):
	# (0 <= delta) & (0 <= skoCOSS) & (0 <= skoS) & (skoSINS <= skoS) & (31415927/10000000 > pi) & (pi > 15707963/5000000) & (pi/2 > skoS) & (skoCOSS**2 + skoSINS**2 - 1 <= delta) & (-skoCOSS**2 - skoSINS**2 + 1 <= delta)

	post_cond =  And(LessThan(Integer(0), Symbol('delta')), LessThan(Integer(0), Symbol('skoCOSS')), LessThan(Integer(0), Symbol('skoS')), LessThan(Symbol('skoSINS'), Symbol('skoS')), StrictGreaterThan(Rational(31415927, 10000000), Symbol('pi')), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Mul(Rational(1, 2), Symbol('pi')), Symbol('skoS')), LessThan(Add(Pow(Symbol('skoCOSS'), Integer(2)), Pow(Symbol('skoSINS'), Integer(2)), Integer(-1)), Symbol('delta')), LessThan(Add(Mul(Integer(-1), Pow(Symbol('skoCOSS'), Integer(2))), Mul(Integer(-1), Pow(Symbol('skoSINS'), Integer(2))), Integer(1)), Symbol('delta')))

	eval = post_cond.subs( { 'delta':delta, 'skoS':skoS, 'pi':pi, 'skoCOSS':skoCOSS, 'skoSINS':skoSINS })

	return eval == sympy.logic.boolalg.BooleanTrue





if __name__=="__main__":
	
	ip_0=int(input("enter integer numerator of delta:\n"))
	ip_1=int(input("enter integer denominator of delta:\n"))
	assert(ip_1!=0), ("Error denominator entered is 0")
	delta=sympy.Rational(ip_0,ip_1)
	
	
	ip_0=int(input("enter integer numerator of skoS:\n"))
	ip_1=int(input("enter integer denominator of skoS:\n"))
	assert(ip_1!=0), ("Error denominator entered is 0")
	skoS=sympy.Rational(ip_0,ip_1)
	
	
	ip_0=int(input("enter integer numerator of pi:\n"))
	ip_1=int(input("enter integer denominator of pi:\n"))
	assert(ip_1!=0), ("Error denominator entered is 0")
	pi=sympy.Rational(ip_0,ip_1)
	
	
	
	
	if pre_condition_0(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_0 SAT")
		print('delta = 2')
		print('skoCOSS = 1')
		print('skoS = 1')
		print('skoSINS = 1/8')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_1(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_1 SAT")
		print('delta = 2')
		print('skoCOSS = 1')
		print('skoS = 1')
		print('skoSINS = 1/8')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_2(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_2 SAT")
		print('delta = 1/128')
		print('skoCOSS = 0')
		print('skoS = 3/2')
		print('skoSINS = 1')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_3(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_3 SAT")
		print('delta = 1/128')
		print('skoCOSS = 0')
		print('skoS = 3/2')
		print('skoSINS = 1')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_4(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_4 SAT")
		print('delta = 511/131072')
		print('skoCOSS = 255/256')
		print('skoS = 3/32')
		print('skoSINS = 1/16')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_5(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_5 SAT")
		print('delta = 511/131072')
		print('skoCOSS = 255/256')
		print('skoS = 3/32')
		print('skoSINS = 1/16')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_6(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_6 SAT")
		print('delta = 1/512')
		print('skoCOSS = 511/512')
		print('skoS = 1/32')
		print('skoSINS = -1/16')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_7(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_7 SAT")
		print('delta = 1/512')
		print('skoCOSS = 511/512')
		print('skoS = 1/32')
		print('skoSINS = -1/16')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_8(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_8 SAT")
		print('delta = 1/524288')
		print('skoCOSS = 2047/2048')
		print('skoS = 1/2')
		print('skoSINS = -1/32')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_9(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_9 SAT")
		print('delta = 1/524288')
		print('skoCOSS = 2047/2048')
		print('skoS = 1/2')
		print('skoSINS = -1/32')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_10(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_10 SAT")
		print('delta = 1/8388608')
		print('skoCOSS = 8191/8192')
		print('skoS = 1/2')
		print('skoSINS = -1/64')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_11(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_11 SAT")
		print('delta = 1/8388608')
		print('skoCOSS = 8191/8192')
		print('skoS = 1/2')
		print('skoSINS = -1/64')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_12(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_12 SAT")
		print('delta = 1/134217728')
		print('skoCOSS = 32767/32768')
		print('skoS = 1/2')
		print('skoSINS = -1/128')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_13(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_13 SAT")
		print('delta = 1/134217728')
		print('skoCOSS = 32767/32768')
		print('skoS = 1/2')
		print('skoSINS = -1/128')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_14(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_14 SAT")
		print('delta = 1/2147483648')
		print('skoCOSS = 131071/131072')
		print('skoS = 1/2')
		print('skoSINS = -1/256')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_15(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_15 SAT")
		print('delta = 1/2147483648')
		print('skoCOSS = 131071/131072')
		print('skoS = 1/2')
		print('skoSINS = -1/256')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_16(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_16 SAT")
		print('delta = 1/17179869184')
		print('skoCOSS = 524287/524288')
		print('skoS = 1/2')
		print('skoSINS = -1/512')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_17(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_17 SAT")
		print('delta = 1/17179869184')
		print('skoCOSS = 524287/524288')
		print('skoS = 1/2')
		print('skoSINS = -1/512')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_18(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_18 SAT")
		print('delta = 1/274877906944')
		print('skoCOSS = 2097151/2097152')
		print('skoS = 1/2')
		print('skoSINS = -1/1024')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_19(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_19 SAT")
		print('delta = 1/274877906944')
		print('skoCOSS = 2097151/2097152')
		print('skoS = 1/2')
		print('skoSINS = -1/1024')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_20(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_20 SAT")
		print('delta = 1/4398046511104')
		print('skoCOSS = 8388607/8388608')
		print('skoS = 1/2')
		print('skoSINS = -1/2048')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_21(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_21 SAT")
		print('delta = 1/4398046511104')
		print('skoCOSS = 8388607/8388608')
		print('skoS = 1/2')
		print('skoSINS = -1/2048')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_22(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_22 SAT")
		print('delta = 1/70368744177664')
		print('skoCOSS = 33554431/33554432')
		print('skoS = 1/2')
		print('skoSINS = -1/4096')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_23(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_23 SAT")
		print('delta = 1/70368744177664')
		print('skoCOSS = 33554431/33554432')
		print('skoS = 1/2')
		print('skoSINS = -1/4096')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_24(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_24 SAT")
		print('delta = 1/2251799813685248')
		print('skoCOSS = 134217727/134217728')
		print('skoS = 1/2')
		print('skoSINS = -1/8192')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_25(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_25 SAT")
		print('delta = 1/2251799813685248')
		print('skoCOSS = 134217727/134217728')
		print('skoS = 1/2')
		print('skoSINS = -1/8192')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_26(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_26 SAT")
		print('delta = 1/18014398509481984')
		print('skoCOSS = 536870911/536870912')
		print('skoS = 1/2')
		print('skoSINS = -1/16384')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_27(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_27 SAT")
		print('delta = 1/18014398509481984')
		print('skoCOSS = 536870911/536870912')
		print('skoS = 1/2')
		print('skoSINS = -1/16384')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_28(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_28 SAT")
		print('delta = 1/576460752303423488')
		print('skoCOSS = 2147483647/2147483648')
		print('skoS = 1/2')
		print('skoSINS = -1/32768')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_29(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_29 SAT")
		print('delta = 1/576460752303423488')
		print('skoCOSS = 2147483647/2147483648')
		print('skoS = 1/2')
		print('skoSINS = -1/32768')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_30(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_30 SAT")
		print('delta = 1/4611686018427387904')
		print('skoCOSS = 8589934591/8589934592')
		print('skoS = 1/2')
		print('skoSINS = -1/65536')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_31(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_31 SAT")
		print('delta = 1/4611686018427387904')
		print('skoCOSS = 8589934591/8589934592')
		print('skoS = 1/2')
		print('skoSINS = -1/65536')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_32(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_32 SAT")
		print('delta = 1/147573952589676412928')
		print('skoCOSS = 34359738367/34359738368')
		print('skoS = 1/2')
		print('skoSINS = -1/131072')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_33(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_33 SAT")
		print('delta = 1/147573952589676412928')
		print('skoCOSS = 34359738367/34359738368')
		print('skoS = 1/2')
		print('skoSINS = -1/131072')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_34(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_34 SAT")
		print('delta = 1/2361183241434822606848')
		print('skoCOSS = 137438953471/137438953472')
		print('skoS = 1/2')
		print('skoSINS = -1/262144')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_35(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_35 SAT")
		print('delta = 1/2361183241434822606848')
		print('skoCOSS = 137438953471/137438953472')
		print('skoS = 1/2')
		print('skoSINS = -1/262144')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_36(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_36 SAT")
		print('delta = 1/37778931862957161709568')
		print('skoCOSS = 549755813887/549755813888')
		print('skoS = 1/2')
		print('skoSINS = -1/524288')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_37(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_37 SAT")
		print('delta = 1/37778931862957161709568')
		print('skoCOSS = 549755813887/549755813888')
		print('skoS = 1/2')
		print('skoSINS = -1/524288')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_38(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_38 SAT")
		print('delta = 1/302231454903657293676544')
		print('skoCOSS = 2199023255551/2199023255552')
		print('skoS = 1/2')
		print('skoSINS = -1/1048576')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_39(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_39 SAT")
		print('delta = 1/302231454903657293676544')
		print('skoCOSS = 2199023255551/2199023255552')
		print('skoS = 1/2')
		print('skoSINS = -1/1048576')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_40(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_40 SAT")
		print('delta = 1/4835703278458516698824704')
		print('skoCOSS = 8796093022207/8796093022208')
		print('skoS = 1/2')
		print('skoSINS = -1/2097152')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_41(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_41 SAT")
		print('delta = 1/4835703278458516698824704')
		print('skoCOSS = 8796093022207/8796093022208')
		print('skoS = 1/2')
		print('skoSINS = -1/2097152')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_42(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_42 SAT")
		print('delta = 1/154742504910672534362390528')
		print('skoCOSS = 35184372088831/35184372088832')
		print('skoS = 1/2')
		print('skoSINS = -1/4194304')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_43(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_43 SAT")
		print('delta = 1/154742504910672534362390528')
		print('skoCOSS = 35184372088831/35184372088832')
		print('skoS = 1/2')
		print('skoSINS = -1/4194304')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_44(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_44 SAT")
		print('delta = 1/1237940039285380274899124224')
		print('skoCOSS = 140737488355327/140737488355328')
		print('skoS = 1/2')
		print('skoSINS = -1/8388608')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_45(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_45 SAT")
		print('delta = 1/1237940039285380274899124224')
		print('skoCOSS = 140737488355327/140737488355328')
		print('skoS = 1/2')
		print('skoSINS = -1/8388608')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_46(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_46 SAT")
		print('delta = 1/19807040628566084398385987584')
		print('skoCOSS = 562949953421311/562949953421312')
		print('skoS = 1/2')
		print('skoSINS = -1/16777216')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_47(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_47 SAT")
		print('delta = 1/19807040628566084398385987584')
		print('skoCOSS = 562949953421311/562949953421312')
		print('skoS = 1/2')
		print('skoSINS = -1/16777216')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_48(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_48 SAT")
		print('delta = 1/633825300114114700748351602688')
		print('skoCOSS = 2251799813685247/2251799813685248')
		print('skoS = 1/2')
		print('skoSINS = -1/33554432')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_49(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_49 SAT")
		print('delta = 1/633825300114114700748351602688')
		print('skoCOSS = 2251799813685247/2251799813685248')
		print('skoS = 1/2')
		print('skoSINS = -1/33554432')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_50(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_50 SAT")
		print('delta = 1/10141204801825835211973625643008')
		print('skoCOSS = 9007199254740991/9007199254740992')
		print('skoS = 1/2')
		print('skoSINS = -1/67108864')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_51(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_51 SAT")
		print('delta = 1/10141204801825835211973625643008')
		print('skoCOSS = 9007199254740991/9007199254740992')
		print('skoS = 1/2')
		print('skoSINS = -1/67108864')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_52(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_52 SAT")
		print('delta = 1/81129638414606681695789005144064')
		print('skoCOSS = 36028797018963967/36028797018963968')
		print('skoS = 1/2')
		print('skoSINS = -1/134217728')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_53(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_53 SAT")
		print('delta = 1/81129638414606681695789005144064')
		print('skoCOSS = 36028797018963967/36028797018963968')
		print('skoS = 1/2')
		print('skoSINS = -1/134217728')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_54(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_54 SAT")
		print('delta = 18014398509481983/23384026197294446691258957323460528314494920687616')
		print('skoCOSS = 1298074214633706871103827063341055/1298074214633706907132624082305024')
		print('skoS = 1/2')
		print('skoSINS = -1/134217728')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_55(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_55 SAT")
		print('delta = 18014398509481983/23384026197294446691258957323460528314494920687616')
		print('skoCOSS = 1298074214633706871103827063341055/1298074214633706907132624082305024')
		print('skoS = 1/2')
		print('skoSINS = -1/134217728')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_56(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_56 SAT")
		print('delta = 1/2596148429267413814265248164610048')
		print('skoCOSS = 2596148429267413742207654126682111/2596148429267413814265248164610048')
		print('skoS = 1/2')
		print('skoSINS = -1/134217728')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_57(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_57 SAT")
		print('delta = 1/2596148429267413814265248164610048')
		print('skoCOSS = 2596148429267413742207654126682111/2596148429267413814265248164610048')
		print('skoS = 1/2')
		print('skoSINS = -1/134217728')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_58(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_58 SAT")
		print('delta = 18014398509481983/842498333348457493583344221469363458551160763204392890034487820288')
		print('skoCOSS = 46768052394588892084443700013214131481967249588223/46768052394588893382517914646921056628989841375232')
		print('skoS = 1/2')
		print('skoSINS = -1/134217728')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_59(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_59 SAT")
		print('delta = 18014398509481983/842498333348457493583344221469363458551160763204392890034487820288')
		print('skoCOSS = 46768052394588892084443700013214131481967249588223/46768052394588893382517914646921056628989841375232')
		print('skoS = 1/2')
		print('skoSINS = -1/134217728')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_60(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_60 SAT")
		print('delta = 1/93536104789177786765035829293842113257979682750464')
		print('skoCOSS = 93536104789177784168887400026428262963934499176447/93536104789177786765035829293842113257979682750464')
		print('skoS = 1/2')
		print('skoSINS = -1/134217728')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_61(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_61 SAT")
		print('delta = 1/93536104789177786765035829293842113257979682750464')
		print('skoCOSS = 93536104789177784168887400026428262963934499176447/93536104789177786765035829293842113257979682750464')
		print('skoS = 1/2')
		print('skoSINS = -1/134217728')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_62(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_62 SAT")
		print('delta = 45035996273704961/60708402882054033466233184588234965832575213720379360039119137804340758912662765568')
		print('skoCOSS = 93536104789177784168887400026428262963934499176447/93536104789177786765035829293842113257979682750464')
		print('skoS = 1/2')
		print('skoSINS = -1/134217728')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_63(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_63 SAT")
		print('delta = 45035996273704961/60708402882054033466233184588234965832575213720379360039119137804340758912662765568')
		print('skoCOSS = 93536104789177784168887400026428262963934499176447/93536104789177786765035829293842113257979682750464')
		print('skoS = 1/2')
		print('skoSINS = -1/134217728')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_64(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_64 SAT")
		print('delta = 45035996273704961/60708402882054033466233184588234965832575213720379360039119137804340758912662765568')
		print('skoCOSS = 93536104789177784168887400026428262963934499176447/93536104789177786765035829293842113257979682750464')
		print('skoS = 1/2')
		print('skoSINS = -1/134217728')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_65(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_65 SAT")
		print('delta = 45035996273704961/60708402882054033466233184588234965832575213720379360039119137804340758912662765568')
		print('skoCOSS = 93536104789177784168887400026428262963934499176447/93536104789177786765035829293842113257979682750464')
		print('skoS = 1/2')
		print('skoSINS = -1/134217728')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_66(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_66 SAT")
		print('delta = 45035996273704961/60708402882054033466233184588234965832575213720379360039119137804340758912662765568')
		print('skoCOSS = 93536104789177784168887400026428262963934499176447/93536104789177786765035829293842113257979682750464')
		print('skoS = 1/2')
		print('skoSINS = -1/134217728')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_67(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_67 SAT")
		print('delta = 45035996273704961/60708402882054033466233184588234965832575213720379360039119137804340758912662765568')
		print('skoCOSS = 93536104789177784168887400026428262963934499176447/93536104789177786765035829293842113257979682750464')
		print('skoS = 1/2')
		print('skoSINS = -1/134217728')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_68(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_68 SAT")
		print('delta = 45035996273704961/60708402882054033466233184588234965832575213720379360039119137804340758912662765568')
		print('skoCOSS = 93536104789177784168887400026428262963934499176447/93536104789177786765035829293842113257979682750464')
		print('skoS = 1/2')
		print('skoSINS = -1/134217728')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_69(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_69 SAT")
		print('delta = 45035996273704961/60708402882054033466233184588234965832575213720379360039119137804340758912662765568')
		print('skoCOSS = 93536104789177784168887400026428262963934499176447/93536104789177786765035829293842113257979682750464')
		print('skoS = 1/2')
		print('skoSINS = -1/134217728')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_70(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_70 SAT")
		print('delta = 45035996273704961/60708402882054033466233184588234965832575213720379360039119137804340758912662765568')
		print('skoCOSS = 93536104789177784168887400026428262963934499176447/93536104789177786765035829293842113257979682750464')
		print('skoS = 1/2')
		print('skoSINS = -1/134217728')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_71(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_71 SAT")
		print('delta = 45035996273704961/60708402882054033466233184588234965832575213720379360039119137804340758912662765568')
		print('skoCOSS = 93536104789177784168887400026428262963934499176447/93536104789177786765035829293842113257979682750464')
		print('skoS = 1/2')
		print('skoSINS = -1/134217728')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_72(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_72 SAT")
		print('delta = 45035996273704961/60708402882054033466233184588234965832575213720379360039119137804340758912662765568')
		print('skoCOSS = 93536104789177784168887400026428262963934499176447/93536104789177786765035829293842113257979682750464')
		print('skoS = 1/2')
		print('skoSINS = -1/134217728')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_73(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_73 SAT")
		print('delta = 45035996273704961/60708402882054033466233184588234965832575213720379360039119137804340758912662765568')
		print('skoCOSS = 93536104789177784168887400026428262963934499176447/93536104789177786765035829293842113257979682750464')
		print('skoS = 1/2')
		print('skoSINS = -1/134217728')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_74(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_74 SAT")
		print('delta = 45035996273704961/60708402882054033466233184588234965832575213720379360039119137804340758912662765568')
		print('skoCOSS = 93536104789177784168887400026428262963934499176447/93536104789177786765035829293842113257979682750464')
		print('skoS = 1/2')
		print('skoSINS = -1/134217728')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_75(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_75 SAT")
		print('delta = 45035996273704961/60708402882054033466233184588234965832575213720379360039119137804340758912662765568')
		print('skoCOSS = 93536104789177784168887400026428262963934499176447/93536104789177786765035829293842113257979682750464')
		print('skoS = 1/2')
		print('skoSINS = -1/134217728')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_76(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_76 SAT")
		print('delta = 45035996273704961/60708402882054033466233184588234965832575213720379360039119137804340758912662765568')
		print('skoCOSS = 93536104789177784168887400026428262963934499176447/93536104789177786765035829293842113257979682750464')
		print('skoS = 1/2')
		print('skoSINS = -1/134217728')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_77(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_77 SAT")
		print('delta = 45035996273704961/60708402882054033466233184588234965832575213720379360039119137804340758912662765568')
		print('skoCOSS = 93536104789177784168887400026428262963934499176447/93536104789177786765035829293842113257979682750464')
		print('skoS = 1/2')
		print('skoSINS = -1/134217728')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_78(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_78 SAT")
		print('delta = 45035996273704961/60708402882054033466233184588234965832575213720379360039119137804340758912662765568')
		print('skoCOSS = 93536104789177784168887400026428262963934499176447/93536104789177786765035829293842113257979682750464')
		print('skoS = 1/2')
		print('skoSINS = -1/134217728')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_79(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_79 SAT")
		print('delta = 45035996273704961/60708402882054033466233184588234965832575213720379360039119137804340758912662765568')
		print('skoCOSS = 93536104789177784168887400026428262963934499176447/93536104789177786765035829293842113257979682750464')
		print('skoS = 1/2')
		print('skoSINS = -1/134217728')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_80(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_80 SAT")
		print('delta = 45035996273704961/60708402882054033466233184588234965832575213720379360039119137804340758912662765568')
		print('skoCOSS = 93536104789177784168887400026428262963934499176447/93536104789177786765035829293842113257979682750464')
		print('skoS = 1/2')
		print('skoSINS = -1/134217728')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_81(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_81 SAT")
		print('delta = 45035996273704961/60708402882054033466233184588234965832575213720379360039119137804340758912662765568')
		print('skoCOSS = 93536104789177784168887400026428262963934499176447/93536104789177786765035829293842113257979682750464')
		print('skoS = 1/2')
		print('skoSINS = -1/134217728')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_82(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_82 SAT")
		print('delta = 45035996273704961/60708402882054033466233184588234965832575213720379360039119137804340758912662765568')
		print('skoCOSS = 93536104789177784168887400026428262963934499176447/93536104789177786765035829293842113257979682750464')
		print('skoS = 1/2')
		print('skoSINS = -1/134217728')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_83(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_83 SAT")
		print('delta = 45035996273704961/60708402882054033466233184588234965832575213720379360039119137804340758912662765568')
		print('skoCOSS = 93536104789177784168887400026428262963934499176447/93536104789177786765035829293842113257979682750464')
		print('skoS = 1/2')
		print('skoSINS = -1/134217728')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_84(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_84 SAT")
		print('delta = 45035996273704961/60708402882054033466233184588234965832575213720379360039119137804340758912662765568')
		print('skoCOSS = 93536104789177784168887400026428262963934499176447/93536104789177786765035829293842113257979682750464')
		print('skoS = 1/2')
		print('skoSINS = -1/134217728')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_85(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_85 SAT")
		print('delta = 45035996273704961/60708402882054033466233184588234965832575213720379360039119137804340758912662765568')
		print('skoCOSS = 93536104789177784168887400026428262963934499176447/93536104789177786765035829293842113257979682750464')
		print('skoS = 1/2')
		print('skoSINS = -1/134217728')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_86(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_86 SAT")
		print('delta = 45035996273704961/60708402882054033466233184588234965832575213720379360039119137804340758912662765568')
		print('skoCOSS = 93536104789177784168887400026428262963934499176447/93536104789177786765035829293842113257979682750464')
		print('skoS = 1/2')
		print('skoSINS = -1/134217728')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_87(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_87 SAT")
		print('delta = 45035996273704961/60708402882054033466233184588234965832575213720379360039119137804340758912662765568')
		print('skoCOSS = 93536104789177784168887400026428262963934499176447/93536104789177786765035829293842113257979682750464')
		print('skoS = 1/2')
		print('skoSINS = -1/134217728')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_88(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_88 SAT")
		print('delta = 45035996273704961/60708402882054033466233184588234965832575213720379360039119137804340758912662765568')
		print('skoCOSS = 93536104789177784168887400026428262963934499176447/93536104789177786765035829293842113257979682750464')
		print('skoS = 1/2')
		print('skoSINS = -1/134217728')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_89(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_89 SAT")
		print('delta = 45035996273704961/60708402882054033466233184588234965832575213720379360039119137804340758912662765568')
		print('skoCOSS = 93536104789177784168887400026428262963934499176447/93536104789177786765035829293842113257979682750464')
		print('skoS = 1/2')
		print('skoSINS = -1/134217728')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_90(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_90 SAT")
		print('delta = 45035996273704961/60708402882054033466233184588234965832575213720379360039119137804340758912662765568')
		print('skoCOSS = 93536104789177784168887400026428262963934499176447/93536104789177786765035829293842113257979682750464')
		print('skoS = 1/2')
		print('skoSINS = -1/134217728')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_91(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_91 SAT")
		print('delta = 45035996273704961/60708402882054033466233184588234965832575213720379360039119137804340758912662765568')
		print('skoCOSS = 93536104789177784168887400026428262963934499176447/93536104789177786765035829293842113257979682750464')
		print('skoS = 1/2')
		print('skoSINS = -1/134217728')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_92(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_92 SAT")
		print('delta = 45035996273704961/60708402882054033466233184588234965832575213720379360039119137804340758912662765568')
		print('skoCOSS = 93536104789177784168887400026428262963934499176447/93536104789177786765035829293842113257979682750464')
		print('skoS = 1/2')
		print('skoSINS = -1/134217728')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_93(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_93 SAT")
		print('delta = 45035996273704961/60708402882054033466233184588234965832575213720379360039119137804340758912662765568')
		print('skoCOSS = 93536104789177784168887400026428262963934499176447/93536104789177786765035829293842113257979682750464')
		print('skoS = 1/2')
		print('skoSINS = -1/134217728')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_94(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_94 SAT")
		print('delta = 45035996273704961/60708402882054033466233184588234965832575213720379360039119137804340758912662765568')
		print('skoCOSS = 93536104789177784168887400026428262963934499176447/93536104789177786765035829293842113257979682750464')
		print('skoS = 1/2')
		print('skoSINS = -1/134217728')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_95(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_95 SAT")
		print('delta = 45035996273704961/60708402882054033466233184588234965832575213720379360039119137804340758912662765568')
		print('skoCOSS = 93536104789177784168887400026428262963934499176447/93536104789177786765035829293842113257979682750464')
		print('skoS = 1/2')
		print('skoSINS = -1/134217728')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_96(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_96 SAT")
		print('delta = 45035996273704961/60708402882054033466233184588234965832575213720379360039119137804340758912662765568')
		print('skoCOSS = 93536104789177784168887400026428262963934499176447/93536104789177786765035829293842113257979682750464')
		print('skoS = 1/2')
		print('skoSINS = -1/134217728')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_97(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_97 SAT")
		print('delta = 45035996273704961/60708402882054033466233184588234965832575213720379360039119137804340758912662765568')
		print('skoCOSS = 93536104789177784168887400026428262963934499176447/93536104789177786765035829293842113257979682750464')
		print('skoS = 1/2')
		print('skoSINS = -1/134217728')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_98(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_98 SAT")
		print('delta = 45035996273704961/60708402882054033466233184588234965832575213720379360039119137804340758912662765568')
		print('skoCOSS = 93536104789177784168887400026428262963934499176447/93536104789177786765035829293842113257979682750464')
		print('skoS = 1/2')
		print('skoSINS = -1/134217728')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_99(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_99 SAT")
		print('delta = 45035996273704961/60708402882054033466233184588234965832575213720379360039119137804340758912662765568')
		print('skoCOSS = 93536104789177784168887400026428262963934499176447/93536104789177786765035829293842113257979682750464')
		print('skoS = 1/2')
		print('skoSINS = -1/134217728')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_100(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_100 SAT")
		print('delta = 45035996273704961/60708402882054033466233184588234965832575213720379360039119137804340758912662765568')
		print('skoCOSS = 93536104789177784168887400026428262963934499176447/93536104789177786765035829293842113257979682750464')
		print('skoS = 1/2')
		print('skoSINS = -1/134217728')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_101(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_101 SAT")
		print('delta = 45035996273704961/60708402882054033466233184588234965832575213720379360039119137804340758912662765568')
		print('skoCOSS = 93536104789177784168887400026428262963934499176447/93536104789177786765035829293842113257979682750464')
		print('skoS = 1/2')
		print('skoSINS = -1/134217728')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_102(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_102 SAT")
		print('delta = 45035996273704961/60708402882054033466233184588234965832575213720379360039119137804340758912662765568')
		print('skoCOSS = 93536104789177784168887400026428262963934499176447/93536104789177786765035829293842113257979682750464')
		print('skoS = 1/2')
		print('skoSINS = -1/134217728')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_103(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_103 SAT")
		print('delta = 45035996273704961/60708402882054033466233184588234965832575213720379360039119137804340758912662765568')
		print('skoCOSS = 93536104789177784168887400026428262963934499176447/93536104789177786765035829293842113257979682750464')
		print('skoS = 1/2')
		print('skoSINS = -1/134217728')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_104(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_104 SAT")
		print('delta = 45035996273704961/60708402882054033466233184588234965832575213720379360039119137804340758912662765568')
		print('skoCOSS = 93536104789177784168887400026428262963934499176447/93536104789177786765035829293842113257979682750464')
		print('skoS = 1/2')
		print('skoSINS = -1/134217728')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_105(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_105 SAT")
		print('delta = 45035996273704961/60708402882054033466233184588234965832575213720379360039119137804340758912662765568')
		print('skoCOSS = 93536104789177784168887400026428262963934499176447/93536104789177786765035829293842113257979682750464')
		print('skoS = 1/2')
		print('skoSINS = -1/134217728')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_106(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_106 SAT")
		print('delta = 45035996273704961/60708402882054033466233184588234965832575213720379360039119137804340758912662765568')
		print('skoCOSS = 93536104789177784168887400026428262963934499176447/93536104789177786765035829293842113257979682750464')
		print('skoS = 1/2')
		print('skoSINS = -1/134217728')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_107(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_107 SAT")
		print('delta = 45035996273704961/60708402882054033466233184588234965832575213720379360039119137804340758912662765568')
		print('skoCOSS = 93536104789177784168887400026428262963934499176447/93536104789177786765035829293842113257979682750464')
		print('skoS = 1/2')
		print('skoSINS = -1/134217728')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_108(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_108 SAT")
		print('delta = 45035996273704961/60708402882054033466233184588234965832575213720379360039119137804340758912662765568')
		print('skoCOSS = 93536104789177784168887400026428262963934499176447/93536104789177786765035829293842113257979682750464')
		print('skoS = 1/2')
		print('skoSINS = -1/134217728')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_109(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_109 SAT")
		print('delta = 45035996273704961/60708402882054033466233184588234965832575213720379360039119137804340758912662765568')
		print('skoCOSS = 93536104789177784168887400026428262963934499176447/93536104789177786765035829293842113257979682750464')
		print('skoS = 1/2')
		print('skoSINS = -1/134217728')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_110(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_110 SAT")
		print('delta = 45035996273704961/60708402882054033466233184588234965832575213720379360039119137804340758912662765568')
		print('skoCOSS = 93536104789177784168887400026428262963934499176447/93536104789177786765035829293842113257979682750464')
		print('skoS = 1/2')
		print('skoSINS = -1/134217728')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_111(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_111 SAT")
		print('delta = 45035996273704961/60708402882054033466233184588234965832575213720379360039119137804340758912662765568')
		print('skoCOSS = 93536104789177784168887400026428262963934499176447/93536104789177786765035829293842113257979682750464')
		print('skoS = 1/2')
		print('skoSINS = -1/134217728')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_112(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_112 SAT")
		print('delta = 45035996273704961/60708402882054033466233184588234965832575213720379360039119137804340758912662765568')
		print('skoCOSS = 93536104789177784168887400026428262963934499176447/93536104789177786765035829293842113257979682750464')
		print('skoS = 1/2')
		print('skoSINS = -1/134217728')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_113(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_113 SAT")
		print('delta = 45035996273704961/60708402882054033466233184588234965832575213720379360039119137804340758912662765568')
		print('skoCOSS = 93536104789177784168887400026428262963934499176447/93536104789177786765035829293842113257979682750464')
		print('skoS = 1/2')
		print('skoSINS = -1/134217728')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_114(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_114 SAT")
		print('delta = 45035996273704961/60708402882054033466233184588234965832575213720379360039119137804340758912662765568')
		print('skoCOSS = 93536104789177784168887400026428262963934499176447/93536104789177786765035829293842113257979682750464')
		print('skoS = 1/2')
		print('skoSINS = -1/134217728')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_115(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_115 SAT")
		print('delta = 45035996273704961/60708402882054033466233184588234965832575213720379360039119137804340758912662765568')
		print('skoCOSS = 93536104789177784168887400026428262963934499176447/93536104789177786765035829293842113257979682750464')
		print('skoS = 1/2')
		print('skoSINS = -1/134217728')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_116(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_116 SAT")
		print('delta = 45035996273704961/60708402882054033466233184588234965832575213720379360039119137804340758912662765568')
		print('skoCOSS = 93536104789177784168887400026428262963934499176447/93536104789177786765035829293842113257979682750464')
		print('skoS = 1/2')
		print('skoSINS = -1/134217728')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_117(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_117 SAT")
		print('delta = 45035996273704961/60708402882054033466233184588234965832575213720379360039119137804340758912662765568')
		print('skoCOSS = 93536104789177784168887400026428262963934499176447/93536104789177786765035829293842113257979682750464')
		print('skoS = 1/2')
		print('skoSINS = -1/134217728')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_118(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_118 SAT")
		print('delta = 45035996273704961/60708402882054033466233184588234965832575213720379360039119137804340758912662765568')
		print('skoCOSS = 93536104789177784168887400026428262963934499176447/93536104789177786765035829293842113257979682750464')
		print('skoS = 1/2')
		print('skoSINS = -1/134217728')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_119(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_119 SAT")
		print('delta = 45035996273704961/60708402882054033466233184588234965832575213720379360039119137804340758912662765568')
		print('skoCOSS = 93536104789177784168887400026428262963934499176447/93536104789177786765035829293842113257979682750464')
		print('skoS = 1/2')
		print('skoSINS = -1/134217728')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_120(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_120 SAT")
		print('delta = 45035996273704961/60708402882054033466233184588234965832575213720379360039119137804340758912662765568')
		print('skoCOSS = 93536104789177784168887400026428262963934499176447/93536104789177786765035829293842113257979682750464')
		print('skoS = 1/2')
		print('skoSINS = -1/134217728')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_121(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_121 SAT")
		print('delta = 45035996273704961/60708402882054033466233184588234965832575213720379360039119137804340758912662765568')
		print('skoCOSS = 93536104789177784168887400026428262963934499176447/93536104789177786765035829293842113257979682750464')
		print('skoS = 1/2')
		print('skoSINS = -1/134217728')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_122(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_122 SAT")
		print('delta = 45035996273704961/60708402882054033466233184588234965832575213720379360039119137804340758912662765568')
		print('skoCOSS = 93536104789177784168887400026428262963934499176447/93536104789177786765035829293842113257979682750464')
		print('skoS = 1/2')
		print('skoSINS = -1/134217728')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_123(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_123 SAT")
		print('delta = 45035996273704961/60708402882054033466233184588234965832575213720379360039119137804340758912662765568')
		print('skoCOSS = 93536104789177784168887400026428262963934499176447/93536104789177786765035829293842113257979682750464')
		print('skoS = 1/2')
		print('skoSINS = -1/134217728')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_124(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_124 SAT")
		print('delta = 45035996273704961/60708402882054033466233184588234965832575213720379360039119137804340758912662765568')
		print('skoCOSS = 93536104789177784168887400026428262963934499176447/93536104789177786765035829293842113257979682750464')
		print('skoS = 1/2')
		print('skoSINS = -1/134217728')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_125(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_125 SAT")
		print('delta = 45035996273704961/60708402882054033466233184588234965832575213720379360039119137804340758912662765568')
		print('skoCOSS = 93536104789177784168887400026428262963934499176447/93536104789177786765035829293842113257979682750464')
		print('skoS = 1/2')
		print('skoSINS = -1/134217728')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_126(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_126 SAT")
		print('delta = 45035996273704961/60708402882054033466233184588234965832575213720379360039119137804340758912662765568')
		print('skoCOSS = 93536104789177784168887400026428262963934499176447/93536104789177786765035829293842113257979682750464')
		print('skoS = 1/2')
		print('skoSINS = -1/134217728')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_127(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_127 SAT")
		print('delta = 45035996273704961/60708402882054033466233184588234965832575213720379360039119137804340758912662765568')
		print('skoCOSS = 93536104789177784168887400026428262963934499176447/93536104789177786765035829293842113257979682750464')
		print('skoS = 1/2')
		print('skoSINS = -1/134217728')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_128(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_128 SAT")
		print('delta = 45035996273704961/60708402882054033466233184588234965832575213720379360039119137804340758912662765568')
		print('skoCOSS = 93536104789177784168887400026428262963934499176447/93536104789177786765035829293842113257979682750464')
		print('skoS = 1/2')
		print('skoSINS = -1/134217728')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_129(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_129 SAT")
		print('delta = 45035996273704961/60708402882054033466233184588234965832575213720379360039119137804340758912662765568')
		print('skoCOSS = 93536104789177784168887400026428262963934499176447/93536104789177786765035829293842113257979682750464')
		print('skoS = 1/2')
		print('skoSINS = -1/134217728')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_130(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_130 SAT")
		print('delta = 45035996273704961/60708402882054033466233184588234965832575213720379360039119137804340758912662765568')
		print('skoCOSS = 93536104789177784168887400026428262963934499176447/93536104789177786765035829293842113257979682750464')
		print('skoS = 1/2')
		print('skoSINS = -1/134217728')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_131(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_131 SAT")
		print('delta = 45035996273704961/60708402882054033466233184588234965832575213720379360039119137804340758912662765568')
		print('skoCOSS = 93536104789177784168887400026428262963934499176447/93536104789177786765035829293842113257979682750464')
		print('skoS = 1/2')
		print('skoSINS = -1/134217728')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_132(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_132 SAT")
		print('delta = 45035996273704961/60708402882054033466233184588234965832575213720379360039119137804340758912662765568')
		print('skoCOSS = 93536104789177784168887400026428262963934499176447/93536104789177786765035829293842113257979682750464')
		print('skoS = 1/2')
		print('skoSINS = -1/134217728')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_133(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_133 SAT")
		print('delta = 45035996273704961/60708402882054033466233184588234965832575213720379360039119137804340758912662765568')
		print('skoCOSS = 93536104789177784168887400026428262963934499176447/93536104789177786765035829293842113257979682750464')
		print('skoS = 1/2')
		print('skoSINS = -1/134217728')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_134(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_134 SAT")
		print('delta = 45035996273704961/60708402882054033466233184588234965832575213720379360039119137804340758912662765568')
		print('skoCOSS = 93536104789177784168887400026428262963934499176447/93536104789177786765035829293842113257979682750464')
		print('skoS = 1/2')
		print('skoSINS = -1/134217728')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_135(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_135 SAT")
		print('delta = 45035996273704961/60708402882054033466233184588234965832575213720379360039119137804340758912662765568')
		print('skoCOSS = 93536104789177784168887400026428262963934499176447/93536104789177786765035829293842113257979682750464')
		print('skoS = 1/2')
		print('skoSINS = -1/134217728')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_136(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_136 SAT")
		print('delta = 45035996273704961/60708402882054033466233184588234965832575213720379360039119137804340758912662765568')
		print('skoCOSS = 93536104789177784168887400026428262963934499176447/93536104789177786765035829293842113257979682750464')
		print('skoS = 1/2')
		print('skoSINS = -1/134217728')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_137(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_137 SAT")
		print('delta = 45035996273704961/60708402882054033466233184588234965832575213720379360039119137804340758912662765568')
		print('skoCOSS = 93536104789177784168887400026428262963934499176447/93536104789177786765035829293842113257979682750464')
		print('skoS = 1/2')
		print('skoSINS = -1/134217728')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_138(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_138 SAT")
		print('delta = 45035996273704961/60708402882054033466233184588234965832575213720379360039119137804340758912662765568')
		print('skoCOSS = 93536104789177784168887400026428262963934499176447/93536104789177786765035829293842113257979682750464')
		print('skoS = 1/2')
		print('skoSINS = -1/134217728')
		print('pi = 26353589/8388608')
		exit(0)
	
	
	if pre_condition_139(delta=delta,skoS=skoS,pi=pi)==True:
		print("pre_condition_139 SAT")
		print('delta = 45035996273704961/60708402882054033466233184588234965832575213720379360039119137804340758912662765568')
		print('skoCOSS = 93536104789177784168887400026428262963934499176447/93536104789177786765035829293842113257979682750464')
		print('skoS = 1/2')
		print('skoSINS = -1/134217728')
		print('pi = 26353589/8388608')
		exit(0)


	print("UNKNOWN")
	exit(0)
