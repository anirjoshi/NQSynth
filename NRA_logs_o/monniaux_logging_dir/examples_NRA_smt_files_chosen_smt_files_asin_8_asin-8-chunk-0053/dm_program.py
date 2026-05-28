import sympy
from sympy import *

def pre_condition_0(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (pi*skoS2/8 + pi/16 + 1/160 < skoSM*(20*pi*skoS2 + 10*pi - 1)/20 - 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictLessThan(Add(Mul(Rational(1, 8), Symbol('pi'), Symbol('skoS2')), Mul(Rational(1, 16), Symbol('pi')), Rational(1, 160)), Add(Mul(Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(-1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (2*pi*skoS2 + pi - 3/10 > pi*skoS2/8 + pi/16 + 1/160)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Integer(2), Symbol('pi'), Symbol('skoS2')), Symbol('pi'), Rational(-3, 10)), Add(Mul(Rational(1, 8), Symbol('pi'), Symbol('skoS2')), Mul(Rational(1, 16), Symbol('pi')), Rational(1, 160))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_2(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (pi*skoS2 + pi/2 + 1/20 < skoSM*(20*pi*skoS2 + 10*pi - 1)/20 - 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictLessThan(Add(Mul(Symbol('pi'), Symbol('skoS2')), Mul(Rational(1, 2), Symbol('pi')), Rational(1, 20)), Add(Mul(Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(-1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_3(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (pi*skoS2 + pi/2 + 1/20 < -1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictLessThan(Add(Mul(Symbol('pi'), Symbol('skoS2')), Mul(Rational(1, 2), Symbol('pi')), Rational(1, 20)), Rational(-1, 5)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_4(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (skoSM*(20*pi*skoS2 + 10*pi - 1)/20 - 1/5 > 0)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(-1, 5)), Integer(0)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_5(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (2*pi*skoS2 + pi - 3/10 > 0)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Integer(2), Symbol('pi'), Symbol('skoS2')), Symbol('pi'), Rational(-3, 10)), Integer(0)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_6(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (5*pi*skoS2 + 5*pi/2 + 1/4 < skoSM*(20*pi*skoS2 + 10*pi - 1)/20 - 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictLessThan(Add(Mul(Integer(5), Symbol('pi'), Symbol('skoS2')), Mul(Rational(5, 2), Symbol('pi')), Rational(1, 4)), Add(Mul(Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(-1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_7(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (pi*skoS2 + pi/2 - 1/4 > 5*pi*skoS2 + 5*pi/2 + 1/4)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Symbol('pi'), Symbol('skoS2')), Mul(Rational(1, 2), Symbol('pi')), Rational(-1, 4)), Add(Mul(Integer(5), Symbol('pi'), Symbol('skoS2')), Mul(Rational(5, 2), Symbol('pi')), Rational(1, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_8(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (49*pi*skoS2 + 49*pi/2 + 49/20 < skoSM*(20*pi*skoS2 + 10*pi - 1)/20 - 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictLessThan(Add(Mul(Integer(49), Symbol('pi'), Symbol('skoS2')), Mul(Rational(49, 2), Symbol('pi')), Rational(49, 20)), Add(Mul(Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(-1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_9(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (49*pi*skoS2 + 49*pi/2 + 49/20 < -1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictLessThan(Add(Mul(Integer(49), Symbol('pi'), Symbol('skoS2')), Mul(Rational(49, 2), Symbol('pi')), Rational(49, 20)), Rational(-1, 5)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_10(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (337*pi*skoS2 + 337*pi/2 + 337/20 < skoSM*(20*pi*skoS2 + 10*pi - 1)/20 - 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictLessThan(Add(Mul(Integer(337), Symbol('pi'), Symbol('skoS2')), Mul(Rational(337, 2), Symbol('pi')), Rational(337, 20)), Add(Mul(Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(-1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_11(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (pi*skoS2 + pi/2 + 3/20 < -337*pi*skoS2 - 337*pi/2 - 337/20)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictLessThan(Add(Mul(Symbol('pi'), Symbol('skoS2')), Mul(Rational(1, 2), Symbol('pi')), Rational(3, 20)), Add(Mul(Integer(-1), Integer(337), Symbol('pi'), Symbol('skoS2')), Mul(Integer(-1), Rational(337, 2), Symbol('pi')), Rational(-337, 20))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_12(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (1877*pi*skoS2 + 1877*pi/2 + 1877/20 < skoSM*(20*pi*skoS2 + 10*pi - 1)/20 - 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictLessThan(Add(Mul(Integer(1877), Symbol('pi'), Symbol('skoS2')), Mul(Rational(1877, 2), Symbol('pi')), Rational(1877, 20)), Add(Mul(Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(-1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_13(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (pi*skoS2 + pi/2 + 3/20 < -1877*pi*skoS2 - 1877*pi/2 - 1877/20)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictLessThan(Add(Mul(Symbol('pi'), Symbol('skoS2')), Mul(Rational(1, 2), Symbol('pi')), Rational(3, 20)), Add(Mul(Integer(-1), Integer(1877), Symbol('pi'), Symbol('skoS2')), Mul(Integer(-1), Rational(1877, 2), Symbol('pi')), Rational(-1877, 20))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_14(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (4390*pi*skoS2 + 2195*pi + 439/2 < skoSM*(20*pi*skoS2 + 10*pi - 1)/20 - 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictLessThan(Add(Mul(Integer(4390), Symbol('pi'), Symbol('skoS2')), Mul(Integer(2195), Symbol('pi')), Rational(439, 2)), Add(Mul(Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(-1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_15(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (pi*skoS2 + pi/2 + 3/20 < -4390*pi*skoS2 - 2195*pi - 439/2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictLessThan(Add(Mul(Symbol('pi'), Symbol('skoS2')), Mul(Rational(1, 2), Symbol('pi')), Rational(3, 20)), Add(Mul(Integer(-1), Integer(4390), Symbol('pi'), Symbol('skoS2')), Mul(Integer(-1), Integer(2195), Symbol('pi')), Rational(-439, 2))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_16(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (13295*pi*skoS2 + 13295*pi/2 + 2659/4 < skoSM*(20*pi*skoS2 + 10*pi - 1)/20 - 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictLessThan(Add(Mul(Integer(13295), Symbol('pi'), Symbol('skoS2')), Mul(Rational(13295, 2), Symbol('pi')), Rational(2659, 4)), Add(Mul(Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(-1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_17(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (pi*skoS2 + pi/2 + 3/20 < -13295*pi*skoS2 - 13295*pi/2 - 2659/4)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictLessThan(Add(Mul(Symbol('pi'), Symbol('skoS2')), Mul(Rational(1, 2), Symbol('pi')), Rational(3, 20)), Add(Mul(Integer(-1), Integer(13295), Symbol('pi'), Symbol('skoS2')), Mul(Integer(-1), Rational(13295, 2), Symbol('pi')), Rational(-2659, 4))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_18(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (26974*pi*skoS2 + 13487*pi + 13487/10 < skoSM*(20*pi*skoS2 + 10*pi - 1)/20 - 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictLessThan(Add(Mul(Integer(26974), Symbol('pi'), Symbol('skoS2')), Mul(Integer(13487), Symbol('pi')), Rational(13487, 10)), Add(Mul(Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(-1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_19(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (pi*skoS2 + pi/2 + 3/20 < -26974*pi*skoS2 - 13487*pi - 13487/10)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictLessThan(Add(Mul(Symbol('pi'), Symbol('skoS2')), Mul(Rational(1, 2), Symbol('pi')), Rational(3, 20)), Add(Mul(Integer(-1), Integer(26974), Symbol('pi'), Symbol('skoS2')), Mul(Integer(-1), Integer(13487), Symbol('pi')), Rational(-13487, 10))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_20(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (55554*pi*skoS2 + 27777*pi + 27777/10 < skoSM*(20*pi*skoS2 + 10*pi - 1)/20 - 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictLessThan(Add(Mul(Integer(55554), Symbol('pi'), Symbol('skoS2')), Mul(Integer(27777), Symbol('pi')), Rational(27777, 10)), Add(Mul(Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(-1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_21(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (pi*skoS2 + pi/2 + 3/20 < -55554*pi*skoS2 - 27777*pi - 27777/10)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictLessThan(Add(Mul(Symbol('pi'), Symbol('skoS2')), Mul(Rational(1, 2), Symbol('pi')), Rational(3, 20)), Add(Mul(Integer(-1), Integer(55554), Symbol('pi'), Symbol('skoS2')), Mul(Integer(-1), Integer(27777), Symbol('pi')), Rational(-27777, 10))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_22(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (118150*pi*skoS2 + 59075*pi + 11815/2 < skoSM*(20*pi*skoS2 + 10*pi - 1)/20 - 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictLessThan(Add(Mul(Integer(118150), Symbol('pi'), Symbol('skoS2')), Mul(Integer(59075), Symbol('pi')), Rational(11815, 2)), Add(Mul(Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(-1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_23(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (pi*skoS2 + pi/2 + 3/20 < -118150*pi*skoS2 - 59075*pi - 11815/2)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictLessThan(Add(Mul(Symbol('pi'), Symbol('skoS2')), Mul(Rational(1, 2), Symbol('pi')), Rational(3, 20)), Add(Mul(Integer(-1), Integer(118150), Symbol('pi'), Symbol('skoS2')), Mul(Integer(-1), Integer(59075), Symbol('pi')), Rational(-11815, 2))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_24(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (270601*pi*skoS2 + 270601*pi/2 + 270601/20 < skoSM*(20*pi*skoS2 + 10*pi - 1)/20 - 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictLessThan(Add(Mul(Integer(270601), Symbol('pi'), Symbol('skoS2')), Mul(Rational(270601, 2), Symbol('pi')), Rational(270601, 20)), Add(Mul(Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(-1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_25(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (pi*skoS2 + pi/2 + 3/20 < -270601*pi*skoS2 - 270601*pi/2 - 270601/20)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictLessThan(Add(Mul(Symbol('pi'), Symbol('skoS2')), Mul(Rational(1, 2), Symbol('pi')), Rational(3, 20)), Add(Mul(Integer(-1), Integer(270601), Symbol('pi'), Symbol('skoS2')), Mul(Integer(-1), Rational(270601, 2), Symbol('pi')), Rational(-270601, 20))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_26(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (762601*pi*skoS2 + 762601*pi/2 + 762601/20 < skoSM*(20*pi*skoS2 + 10*pi - 1)/20 - 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictLessThan(Add(Mul(Integer(762601), Symbol('pi'), Symbol('skoS2')), Mul(Rational(762601, 2), Symbol('pi')), Rational(762601, 20)), Add(Mul(Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(-1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_27(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (pi*skoS2 + pi/2 + 3/20 < -762601*pi*skoS2 - 762601*pi/2 - 762601/20)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictLessThan(Add(Mul(Symbol('pi'), Symbol('skoS2')), Mul(Rational(1, 2), Symbol('pi')), Rational(3, 20)), Add(Mul(Integer(-1), Integer(762601), Symbol('pi'), Symbol('skoS2')), Mul(Integer(-1), Rational(762601, 2), Symbol('pi')), Rational(-762601, 20))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_28(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (8388608*pi*skoS2 + 4194304*pi + 2097152/5 < skoSM*(20*pi*skoS2 + 10*pi - 1)/20 - 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictLessThan(Add(Mul(Integer(8388608), Symbol('pi'), Symbol('skoS2')), Mul(Integer(4194304), Symbol('pi')), Rational(2097152, 5)), Add(Mul(Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(-1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_29(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (pi*skoS2 + pi/2 + 3/20 < -8388608*pi*skoS2 - 4194304*pi - 2097152/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictLessThan(Add(Mul(Symbol('pi'), Symbol('skoS2')), Mul(Rational(1, 2), Symbol('pi')), Rational(3, 20)), Add(Mul(Integer(-1), Integer(8388608), Symbol('pi'), Symbol('skoS2')), Mul(Integer(-1), Integer(4194304), Symbol('pi')), Rational(-2097152, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_30(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (22369622*pi*skoS2 + 11184811*pi + 11184811/10 < skoSM*(20*pi*skoS2 + 10*pi - 1)/20 - 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictLessThan(Add(Mul(Integer(22369622), Symbol('pi'), Symbol('skoS2')), Mul(Integer(11184811), Symbol('pi')), Rational(11184811, 10)), Add(Mul(Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(-1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_31(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (pi*skoS2 + pi/2 + 3/20 < -22369622*pi*skoS2 - 11184811*pi - 11184811/10)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictLessThan(Add(Mul(Symbol('pi'), Symbol('skoS2')), Mul(Rational(1, 2), Symbol('pi')), Rational(3, 20)), Add(Mul(Integer(-1), Integer(22369622), Symbol('pi'), Symbol('skoS2')), Mul(Integer(-1), Integer(11184811), Symbol('pi')), Rational(-11184811, 10))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_32(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (134217728*pi*skoS2 + 67108864*pi + 33554432/5 < skoSM*(20*pi*skoS2 + 10*pi - 1)/20 - 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictLessThan(Add(Mul(Integer(134217728), Symbol('pi'), Symbol('skoS2')), Mul(Integer(67108864), Symbol('pi')), Rational(33554432, 5)), Add(Mul(Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(-1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_33(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (pi*skoS2 + pi/2 + 3/20 < -134217728*pi*skoS2 - 67108864*pi - 33554432/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictLessThan(Add(Mul(Symbol('pi'), Symbol('skoS2')), Mul(Rational(1, 2), Symbol('pi')), Rational(3, 20)), Add(Mul(Integer(-1), Integer(134217728), Symbol('pi'), Symbol('skoS2')), Mul(Integer(-1), Integer(67108864), Symbol('pi')), Rational(-33554432, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_34(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (357913942*pi*skoS2 + 178956971*pi + 178956971/10 < skoSM*(20*pi*skoS2 + 10*pi - 1)/20 - 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictLessThan(Add(Mul(Integer(357913942), Symbol('pi'), Symbol('skoS2')), Mul(Integer(178956971), Symbol('pi')), Rational(178956971, 10)), Add(Mul(Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(-1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_35(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (pi*skoS2 + pi/2 + 3/20 < -357913942*pi*skoS2 - 178956971*pi - 178956971/10)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictLessThan(Add(Mul(Symbol('pi'), Symbol('skoS2')), Mul(Rational(1, 2), Symbol('pi')), Rational(3, 20)), Add(Mul(Integer(-1), Integer(357913942), Symbol('pi'), Symbol('skoS2')), Mul(Integer(-1), Integer(178956971), Symbol('pi')), Rational(-178956971, 10))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_36(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (2147483648*pi*skoS2 + 1073741824*pi + 536870912/5 < skoSM*(20*pi*skoS2 + 10*pi - 1)/20 - 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictLessThan(Add(Mul(Integer(2147483648), Symbol('pi'), Symbol('skoS2')), Mul(Integer(1073741824), Symbol('pi')), Rational(536870912, 5)), Add(Mul(Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(-1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_37(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (pi*skoS2 + pi/2 + 3/20 < -2147483648*pi*skoS2 - 1073741824*pi - 536870912/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictLessThan(Add(Mul(Symbol('pi'), Symbol('skoS2')), Mul(Rational(1, 2), Symbol('pi')), Rational(3, 20)), Add(Mul(Integer(-1), Integer(2147483648), Symbol('pi'), Symbol('skoS2')), Mul(Integer(-1), Integer(1073741824), Symbol('pi')), Rational(-536870912, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_38(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (5726623062*pi*skoS2 + 2863311531*pi + 2863311531/10 < skoSM*(20*pi*skoS2 + 10*pi - 1)/20 - 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictLessThan(Add(Mul(Integer(5726623062), Symbol('pi'), Symbol('skoS2')), Mul(Integer(2863311531), Symbol('pi')), Rational(2863311531, 10)), Add(Mul(Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(-1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_39(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (pi*skoS2 + pi/2 + 3/20 < -5726623062*pi*skoS2 - 2863311531*pi - 2863311531/10)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictLessThan(Add(Mul(Symbol('pi'), Symbol('skoS2')), Mul(Rational(1, 2), Symbol('pi')), Rational(3, 20)), Add(Mul(Integer(-1), Integer(5726623062), Symbol('pi'), Symbol('skoS2')), Mul(Integer(-1), Integer(2863311531), Symbol('pi')), Rational(-2863311531, 10))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_40(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (34359738368*pi*skoS2 + 17179869184*pi + 8589934592/5 < skoSM*(20*pi*skoS2 + 10*pi - 1)/20 - 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictLessThan(Add(Mul(Integer(34359738368), Symbol('pi'), Symbol('skoS2')), Mul(Integer(17179869184), Symbol('pi')), Rational(8589934592, 5)), Add(Mul(Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(-1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_41(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (pi*skoS2 + pi/2 + 3/20 < -34359738368*pi*skoS2 - 17179869184*pi - 8589934592/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictLessThan(Add(Mul(Symbol('pi'), Symbol('skoS2')), Mul(Rational(1, 2), Symbol('pi')), Rational(3, 20)), Add(Mul(Integer(-1), Integer(34359738368), Symbol('pi'), Symbol('skoS2')), Mul(Integer(-1), Integer(17179869184), Symbol('pi')), Rational(-8589934592, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_42(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (91625968982*pi*skoS2 + 45812984491*pi + 45812984491/10 < skoSM*(20*pi*skoS2 + 10*pi - 1)/20 - 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictLessThan(Add(Mul(Integer(91625968982), Symbol('pi'), Symbol('skoS2')), Mul(Integer(45812984491), Symbol('pi')), Rational(45812984491, 10)), Add(Mul(Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(-1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_43(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (pi*skoS2 + pi/2 + 3/20 < -91625968982*pi*skoS2 - 45812984491*pi - 45812984491/10)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictLessThan(Add(Mul(Symbol('pi'), Symbol('skoS2')), Mul(Rational(1, 2), Symbol('pi')), Rational(3, 20)), Add(Mul(Integer(-1), Integer(91625968982), Symbol('pi'), Symbol('skoS2')), Mul(Integer(-1), Integer(45812984491), Symbol('pi')), Rational(-45812984491, 10))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_44(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (549755813888*pi*skoS2 + 274877906944*pi + 137438953472/5 < skoSM*(20*pi*skoS2 + 10*pi - 1)/20 - 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictLessThan(Add(Mul(Integer(549755813888), Symbol('pi'), Symbol('skoS2')), Mul(Integer(274877906944), Symbol('pi')), Rational(137438953472, 5)), Add(Mul(Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(-1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_45(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (pi*skoS2 + pi/2 + 3/20 < -549755813888*pi*skoS2 - 274877906944*pi - 137438953472/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictLessThan(Add(Mul(Symbol('pi'), Symbol('skoS2')), Mul(Rational(1, 2), Symbol('pi')), Rational(3, 20)), Add(Mul(Integer(-1), Integer(549755813888), Symbol('pi'), Symbol('skoS2')), Mul(Integer(-1), Integer(274877906944), Symbol('pi')), Rational(-137438953472, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_46(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (1466015503702*pi*skoS2 + 733007751851*pi + 733007751851/10 < skoSM*(20*pi*skoS2 + 10*pi - 1)/20 - 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictLessThan(Add(Mul(Integer(1466015503702), Symbol('pi'), Symbol('skoS2')), Mul(Integer(733007751851), Symbol('pi')), Rational(733007751851, 10)), Add(Mul(Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(-1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_47(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (pi*skoS2 + pi/2 + 3/20 < -1466015503702*pi*skoS2 - 733007751851*pi - 733007751851/10)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictLessThan(Add(Mul(Symbol('pi'), Symbol('skoS2')), Mul(Rational(1, 2), Symbol('pi')), Rational(3, 20)), Add(Mul(Integer(-1), Integer(1466015503702), Symbol('pi'), Symbol('skoS2')), Mul(Integer(-1), Integer(733007751851), Symbol('pi')), Rational(-733007751851, 10))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_48(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (8796093022208*pi*skoS2 + 4398046511104*pi + 2199023255552/5 < skoSM*(20*pi*skoS2 + 10*pi - 1)/20 - 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictLessThan(Add(Mul(Integer(8796093022208), Symbol('pi'), Symbol('skoS2')), Mul(Integer(4398046511104), Symbol('pi')), Rational(2199023255552, 5)), Add(Mul(Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(-1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_49(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (pi*skoS2 + pi/2 + 3/20 < -8796093022208*pi*skoS2 - 4398046511104*pi - 2199023255552/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictLessThan(Add(Mul(Symbol('pi'), Symbol('skoS2')), Mul(Rational(1, 2), Symbol('pi')), Rational(3, 20)), Add(Mul(Integer(-1), Integer(8796093022208), Symbol('pi'), Symbol('skoS2')), Mul(Integer(-1), Integer(4398046511104), Symbol('pi')), Rational(-2199023255552, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_50(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (23456248059222*pi*skoS2 + 11728124029611*pi + 11728124029611/10 < skoSM*(20*pi*skoS2 + 10*pi - 1)/20 - 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictLessThan(Add(Mul(Integer(23456248059222), Symbol('pi'), Symbol('skoS2')), Mul(Integer(11728124029611), Symbol('pi')), Rational(11728124029611, 10)), Add(Mul(Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(-1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_51(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (pi*skoS2 + pi/2 + 3/20 < -23456248059222*pi*skoS2 - 11728124029611*pi - 11728124029611/10)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictLessThan(Add(Mul(Symbol('pi'), Symbol('skoS2')), Mul(Rational(1, 2), Symbol('pi')), Rational(3, 20)), Add(Mul(Integer(-1), Integer(23456248059222), Symbol('pi'), Symbol('skoS2')), Mul(Integer(-1), Integer(11728124029611), Symbol('pi')), Rational(-11728124029611, 10))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_52(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (140737488355328*pi*skoS2 + 70368744177664*pi + 35184372088832/5 < skoSM*(20*pi*skoS2 + 10*pi - 1)/20 - 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictLessThan(Add(Mul(Integer(140737488355328), Symbol('pi'), Symbol('skoS2')), Mul(Integer(70368744177664), Symbol('pi')), Rational(35184372088832, 5)), Add(Mul(Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(-1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_53(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (pi*skoS2 + pi/2 + 3/20 < -140737488355328*pi*skoS2 - 70368744177664*pi - 35184372088832/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictLessThan(Add(Mul(Symbol('pi'), Symbol('skoS2')), Mul(Rational(1, 2), Symbol('pi')), Rational(3, 20)), Add(Mul(Integer(-1), Integer(140737488355328), Symbol('pi'), Symbol('skoS2')), Mul(Integer(-1), Integer(70368744177664), Symbol('pi')), Rational(-35184372088832, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_54(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (375299968947542*pi*skoS2 + 187649984473771*pi + 187649984473771/10 < skoSM*(20*pi*skoS2 + 10*pi - 1)/20 - 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictLessThan(Add(Mul(Integer(375299968947542), Symbol('pi'), Symbol('skoS2')), Mul(Integer(187649984473771), Symbol('pi')), Rational(187649984473771, 10)), Add(Mul(Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(-1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_55(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (pi*skoS2 + pi/2 + 3/20 < -375299968947542*pi*skoS2 - 187649984473771*pi - 187649984473771/10)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictLessThan(Add(Mul(Symbol('pi'), Symbol('skoS2')), Mul(Rational(1, 2), Symbol('pi')), Rational(3, 20)), Add(Mul(Integer(-1), Integer(375299968947542), Symbol('pi'), Symbol('skoS2')), Mul(Integer(-1), Integer(187649984473771), Symbol('pi')), Rational(-187649984473771, 10))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_56(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (2251799813685248*pi*skoS2 + 1125899906842624*pi + 562949953421312/5 < skoSM*(20*pi*skoS2 + 10*pi - 1)/20 - 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictLessThan(Add(Mul(Integer(2251799813685248), Symbol('pi'), Symbol('skoS2')), Mul(Integer(1125899906842624), Symbol('pi')), Rational(562949953421312, 5)), Add(Mul(Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(-1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_57(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (pi*skoS2 + pi/2 + 3/20 < -2251799813685248*pi*skoS2 - 1125899906842624*pi - 562949953421312/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictLessThan(Add(Mul(Symbol('pi'), Symbol('skoS2')), Mul(Rational(1, 2), Symbol('pi')), Rational(3, 20)), Add(Mul(Integer(-1), Integer(2251799813685248), Symbol('pi'), Symbol('skoS2')), Mul(Integer(-1), Integer(1125899906842624), Symbol('pi')), Rational(-562949953421312, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_58(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (6004799503160662*pi*skoS2 + 3002399751580331*pi + 3002399751580331/10 < skoSM*(20*pi*skoS2 + 10*pi - 1)/20 - 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictLessThan(Add(Mul(Integer(6004799503160662), Symbol('pi'), Symbol('skoS2')), Mul(Integer(3002399751580331), Symbol('pi')), Rational(3002399751580331, 10)), Add(Mul(Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(-1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_59(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (pi*skoS2 + pi/2 + 3/20 < -6004799503160662*pi*skoS2 - 3002399751580331*pi - 3002399751580331/10)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictLessThan(Add(Mul(Symbol('pi'), Symbol('skoS2')), Mul(Rational(1, 2), Symbol('pi')), Rational(3, 20)), Add(Mul(Integer(-1), Integer(6004799503160662), Symbol('pi'), Symbol('skoS2')), Mul(Integer(-1), Integer(3002399751580331), Symbol('pi')), Rational(-3002399751580331, 10))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_60(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (36028797018963968*pi*skoS2 + 18014398509481984*pi + 9007199254740992/5 < skoSM*(20*pi*skoS2 + 10*pi - 1)/20 - 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictLessThan(Add(Mul(Integer(36028797018963968), Symbol('pi'), Symbol('skoS2')), Mul(Integer(18014398509481984), Symbol('pi')), Rational(9007199254740992, 5)), Add(Mul(Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(-1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_61(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (pi*skoS2 + pi/2 + 3/20 < -36028797018963968*pi*skoS2 - 18014398509481984*pi - 9007199254740992/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictLessThan(Add(Mul(Symbol('pi'), Symbol('skoS2')), Mul(Rational(1, 2), Symbol('pi')), Rational(3, 20)), Add(Mul(Integer(-1), Integer(36028797018963968), Symbol('pi'), Symbol('skoS2')), Mul(Integer(-1), Integer(18014398509481984), Symbol('pi')), Rational(-9007199254740992, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_62(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (3*pi*skoS2 + 3*pi/2 + 3/20 > -skoSM*(20*pi*skoS2 + 10*pi - 1)/20 + 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Integer(3), Symbol('pi'), Symbol('skoS2')), Mul(Rational(3, 2), Symbol('pi')), Rational(3, 20)), Add(Mul(Integer(-1), Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_63(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (3*pi*skoS2 + 3*pi/2 + 3/20 > -pi*skoS2/8 - pi/16 + 33/160)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Integer(3), Symbol('pi'), Symbol('skoS2')), Mul(Rational(3, 2), Symbol('pi')), Rational(3, 20)), Add(Mul(Integer(-1), Rational(1, 8), Symbol('pi'), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 16), Symbol('pi')), Rational(33, 160))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_64(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (5*pi*skoS2 + 5*pi/2 + 1/4 > -skoSM*(20*pi*skoS2 + 10*pi - 1)/20 + 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Integer(5), Symbol('pi'), Symbol('skoS2')), Mul(Rational(5, 2), Symbol('pi')), Rational(1, 4)), Add(Mul(Integer(-1), Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_65(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (5*pi*skoS2 + 5*pi/2 + 1/4 > 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Integer(5), Symbol('pi'), Symbol('skoS2')), Mul(Rational(5, 2), Symbol('pi')), Rational(1, 4)), Rational(1, 5)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_66(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (9*pi*skoS2 + 9*pi/2 + 9/20 > -skoSM*(20*pi*skoS2 + 10*pi - 1)/20 + 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Integer(9), Symbol('pi'), Symbol('skoS2')), Mul(Rational(9, 2), Symbol('pi')), Rational(9, 20)), Add(Mul(Integer(-1), Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_67(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (9*pi*skoS2 + 9*pi/2 + 9/20 > -pi*skoS2/8 - pi/16 + 33/160)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Integer(9), Symbol('pi'), Symbol('skoS2')), Mul(Rational(9, 2), Symbol('pi')), Rational(9, 20)), Add(Mul(Integer(-1), Rational(1, 8), Symbol('pi'), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 16), Symbol('pi')), Rational(33, 160))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_68(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (20*pi*skoS2 + 10*pi + 1 > -skoSM*(20*pi*skoS2 + 10*pi - 1)/20 + 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(1)), Add(Mul(Integer(-1), Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_69(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (20*pi*skoS2 + 10*pi + 1 > -pi*skoS2/8 - pi/16 + 33/160)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(1)), Add(Mul(Integer(-1), Rational(1, 8), Symbol('pi'), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 16), Symbol('pi')), Rational(33, 160))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_70(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (60*pi*skoS2 + 30*pi + 3 > -skoSM*(20*pi*skoS2 + 10*pi - 1)/20 + 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Integer(60), Symbol('pi'), Symbol('skoS2')), Mul(Integer(30), Symbol('pi')), Integer(3)), Add(Mul(Integer(-1), Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_71(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (60*pi*skoS2 + 30*pi + 3 > -pi*skoS2/8 - pi/16 + 33/160)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Integer(60), Symbol('pi'), Symbol('skoS2')), Mul(Integer(30), Symbol('pi')), Integer(3)), Add(Mul(Integer(-1), Rational(1, 8), Symbol('pi'), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 16), Symbol('pi')), Rational(33, 160))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_72(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (130*pi*skoS2 + 65*pi + 13/2 > -skoSM*(20*pi*skoS2 + 10*pi - 1)/20 + 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Integer(130), Symbol('pi'), Symbol('skoS2')), Mul(Integer(65), Symbol('pi')), Rational(13, 2)), Add(Mul(Integer(-1), Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_73(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (130*pi*skoS2 + 65*pi + 13/2 > -pi*skoS2/8 - pi/16 + 33/160)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Integer(130), Symbol('pi'), Symbol('skoS2')), Mul(Integer(65), Symbol('pi')), Rational(13, 2)), Add(Mul(Integer(-1), Rational(1, 8), Symbol('pi'), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 16), Symbol('pi')), Rational(33, 160))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_74(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (314*pi*skoS2 + 157*pi + 157/10 > -skoSM*(20*pi*skoS2 + 10*pi - 1)/20 + 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Integer(314), Symbol('pi'), Symbol('skoS2')), Mul(Integer(157), Symbol('pi')), Rational(157, 10)), Add(Mul(Integer(-1), Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_75(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (314*pi*skoS2 + 157*pi + 157/10 > -pi*skoS2/8 - pi/16 + 33/160)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Integer(314), Symbol('pi'), Symbol('skoS2')), Mul(Integer(157), Symbol('pi')), Rational(157, 10)), Add(Mul(Integer(-1), Rational(1, 8), Symbol('pi'), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 16), Symbol('pi')), Rational(33, 160))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_76(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (1115*pi*skoS2 + 1115*pi/2 + 223/4 > -skoSM*(20*pi*skoS2 + 10*pi - 1)/20 + 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Integer(1115), Symbol('pi'), Symbol('skoS2')), Mul(Rational(1115, 2), Symbol('pi')), Rational(223, 4)), Add(Mul(Integer(-1), Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_77(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (1115*pi*skoS2 + 1115*pi/2 + 223/4 > -pi*skoS2/8 - pi/16 + 33/160)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Integer(1115), Symbol('pi'), Symbol('skoS2')), Mul(Rational(1115, 2), Symbol('pi')), Rational(223, 4)), Add(Mul(Integer(-1), Rational(1, 8), Symbol('pi'), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 16), Symbol('pi')), Rational(33, 160))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_78(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (3091*pi*skoS2 + 3091*pi/2 + 3091/20 > -skoSM*(20*pi*skoS2 + 10*pi - 1)/20 + 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Integer(3091), Symbol('pi'), Symbol('skoS2')), Mul(Rational(3091, 2), Symbol('pi')), Rational(3091, 20)), Add(Mul(Integer(-1), Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_79(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (3091*pi*skoS2 + 3091*pi/2 + 3091/20 > -pi*skoS2/8 - pi/16 + 33/160)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Integer(3091), Symbol('pi'), Symbol('skoS2')), Mul(Rational(3091, 2), Symbol('pi')), Rational(3091, 20)), Add(Mul(Integer(-1), Rational(1, 8), Symbol('pi'), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 16), Symbol('pi')), Rational(33, 160))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_80(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (27468*pi*skoS2 + 13734*pi + 6867/5 > -skoSM*(20*pi*skoS2 + 10*pi - 1)/20 + 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Integer(27468), Symbol('pi'), Symbol('skoS2')), Mul(Integer(13734), Symbol('pi')), Rational(6867, 5)), Add(Mul(Integer(-1), Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_81(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (27468*pi*skoS2 + 13734*pi + 6867/5 > -pi*skoS2/8 - pi/16 + 33/160)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Integer(27468), Symbol('pi'), Symbol('skoS2')), Mul(Integer(13734), Symbol('pi')), Rational(6867, 5)), Add(Mul(Integer(-1), Rational(1, 8), Symbol('pi'), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 16), Symbol('pi')), Rational(33, 160))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_82(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (1980645*pi*skoS2 + 1980645*pi/2 + 396129/4 > -skoSM*(20*pi*skoS2 + 10*pi - 1)/20 + 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Integer(1980645), Symbol('pi'), Symbol('skoS2')), Mul(Rational(1980645, 2), Symbol('pi')), Rational(396129, 4)), Add(Mul(Integer(-1), Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_83(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (1980645*pi*skoS2 + 1980645*pi/2 + 396129/4 > -pi*skoS2/8 - pi/16 + 33/160)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Integer(1980645), Symbol('pi'), Symbol('skoS2')), Mul(Rational(1980645, 2), Symbol('pi')), Rational(396129, 4)), Add(Mul(Integer(-1), Rational(1, 8), Symbol('pi'), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 16), Symbol('pi')), Rational(33, 160))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_84(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (4456449*pi*skoS2 + 4456449*pi/2 + 4456449/20 > -skoSM*(20*pi*skoS2 + 10*pi - 1)/20 + 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Integer(4456449), Symbol('pi'), Symbol('skoS2')), Mul(Rational(4456449, 2), Symbol('pi')), Rational(4456449, 20)), Add(Mul(Integer(-1), Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_85(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (4456449*pi*skoS2 + 4456449*pi/2 + 4456449/20 > -pi*skoS2/8 - pi/16 + 33/160)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Integer(4456449), Symbol('pi'), Symbol('skoS2')), Mul(Rational(4456449, 2), Symbol('pi')), Rational(4456449, 20)), Add(Mul(Integer(-1), Rational(1, 8), Symbol('pi'), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 16), Symbol('pi')), Rational(33, 160))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_86(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (11883863*pi*skoS2 + 11883863*pi/2 + 11883863/20 > -skoSM*(20*pi*skoS2 + 10*pi - 1)/20 + 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Integer(11883863), Symbol('pi'), Symbol('skoS2')), Mul(Rational(11883863, 2), Symbol('pi')), Rational(11883863, 20)), Add(Mul(Integer(-1), Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_87(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (11883863*pi*skoS2 + 11883863*pi/2 + 11883863/20 > -pi*skoS2/8 - pi/16 + 33/160)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Integer(11883863), Symbol('pi'), Symbol('skoS2')), Mul(Rational(11883863, 2), Symbol('pi')), Rational(11883863, 20)), Add(Mul(Integer(-1), Rational(1, 8), Symbol('pi'), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 16), Symbol('pi')), Rational(33, 160))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_88(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (71303169*pi*skoS2 + 71303169*pi/2 + 71303169/20 > -skoSM*(20*pi*skoS2 + 10*pi - 1)/20 + 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Integer(71303169), Symbol('pi'), Symbol('skoS2')), Mul(Rational(71303169, 2), Symbol('pi')), Rational(71303169, 20)), Add(Mul(Integer(-1), Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_89(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (71303169*pi*skoS2 + 71303169*pi/2 + 71303169/20 > -pi*skoS2/8 - pi/16 + 33/160)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Integer(71303169), Symbol('pi'), Symbol('skoS2')), Mul(Rational(71303169, 2), Symbol('pi')), Rational(71303169, 20)), Add(Mul(Integer(-1), Rational(1, 8), Symbol('pi'), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 16), Symbol('pi')), Rational(33, 160))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_90(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (190141783*pi*skoS2 + 190141783*pi/2 + 190141783/20 > -skoSM*(20*pi*skoS2 + 10*pi - 1)/20 + 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Integer(190141783), Symbol('pi'), Symbol('skoS2')), Mul(Rational(190141783, 2), Symbol('pi')), Rational(190141783, 20)), Add(Mul(Integer(-1), Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_91(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (190141783*pi*skoS2 + 190141783*pi/2 + 190141783/20 > -pi*skoS2/8 - pi/16 + 33/160)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Integer(190141783), Symbol('pi'), Symbol('skoS2')), Mul(Rational(190141783, 2), Symbol('pi')), Rational(190141783, 20)), Add(Mul(Integer(-1), Rational(1, 8), Symbol('pi'), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 16), Symbol('pi')), Rational(33, 160))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_92(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (1140850689*pi*skoS2 + 1140850689*pi/2 + 1140850689/20 > -skoSM*(20*pi*skoS2 + 10*pi - 1)/20 + 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Integer(1140850689), Symbol('pi'), Symbol('skoS2')), Mul(Rational(1140850689, 2), Symbol('pi')), Rational(1140850689, 20)), Add(Mul(Integer(-1), Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_93(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (1140850689*pi*skoS2 + 1140850689*pi/2 + 1140850689/20 > -pi*skoS2/8 - pi/16 + 33/160)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Integer(1140850689), Symbol('pi'), Symbol('skoS2')), Mul(Rational(1140850689, 2), Symbol('pi')), Rational(1140850689, 20)), Add(Mul(Integer(-1), Rational(1, 8), Symbol('pi'), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 16), Symbol('pi')), Rational(33, 160))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_94(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (3042268503*pi*skoS2 + 3042268503*pi/2 + 3042268503/20 > -skoSM*(20*pi*skoS2 + 10*pi - 1)/20 + 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Integer(3042268503), Symbol('pi'), Symbol('skoS2')), Mul(Rational(3042268503, 2), Symbol('pi')), Rational(3042268503, 20)), Add(Mul(Integer(-1), Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_95(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (3042268503*pi*skoS2 + 3042268503*pi/2 + 3042268503/20 > -pi*skoS2/8 - pi/16 + 33/160)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Integer(3042268503), Symbol('pi'), Symbol('skoS2')), Mul(Rational(3042268503, 2), Symbol('pi')), Rational(3042268503, 20)), Add(Mul(Integer(-1), Rational(1, 8), Symbol('pi'), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 16), Symbol('pi')), Rational(33, 160))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_96(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (18253611009*pi*skoS2 + 18253611009*pi/2 + 18253611009/20 > -skoSM*(20*pi*skoS2 + 10*pi - 1)/20 + 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Integer(18253611009), Symbol('pi'), Symbol('skoS2')), Mul(Rational(18253611009, 2), Symbol('pi')), Rational(18253611009, 20)), Add(Mul(Integer(-1), Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_97(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (18253611009*pi*skoS2 + 18253611009*pi/2 + 18253611009/20 > -pi*skoS2/8 - pi/16 + 33/160)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Integer(18253611009), Symbol('pi'), Symbol('skoS2')), Mul(Rational(18253611009, 2), Symbol('pi')), Rational(18253611009, 20)), Add(Mul(Integer(-1), Rational(1, 8), Symbol('pi'), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 16), Symbol('pi')), Rational(33, 160))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_98(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (48676296023*pi*skoS2 + 48676296023*pi/2 + 48676296023/20 > -skoSM*(20*pi*skoS2 + 10*pi - 1)/20 + 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Integer(48676296023), Symbol('pi'), Symbol('skoS2')), Mul(Rational(48676296023, 2), Symbol('pi')), Rational(48676296023, 20)), Add(Mul(Integer(-1), Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_99(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (48676296023*pi*skoS2 + 48676296023*pi/2 + 48676296023/20 > -pi*skoS2/8 - pi/16 + 33/160)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Integer(48676296023), Symbol('pi'), Symbol('skoS2')), Mul(Rational(48676296023, 2), Symbol('pi')), Rational(48676296023, 20)), Add(Mul(Integer(-1), Rational(1, 8), Symbol('pi'), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 16), Symbol('pi')), Rational(33, 160))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_100(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (292057776129*pi*skoS2 + 292057776129*pi/2 + 292057776129/20 > -skoSM*(20*pi*skoS2 + 10*pi - 1)/20 + 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Integer(292057776129), Symbol('pi'), Symbol('skoS2')), Mul(Rational(292057776129, 2), Symbol('pi')), Rational(292057776129, 20)), Add(Mul(Integer(-1), Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_101(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (292057776129*pi*skoS2 + 292057776129*pi/2 + 292057776129/20 > -pi*skoS2/8 - pi/16 + 33/160)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Integer(292057776129), Symbol('pi'), Symbol('skoS2')), Mul(Rational(292057776129, 2), Symbol('pi')), Rational(292057776129, 20)), Add(Mul(Integer(-1), Rational(1, 8), Symbol('pi'), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 16), Symbol('pi')), Rational(33, 160))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_102(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (778820736343*pi*skoS2 + 778820736343*pi/2 + 778820736343/20 > -skoSM*(20*pi*skoS2 + 10*pi - 1)/20 + 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Integer(778820736343), Symbol('pi'), Symbol('skoS2')), Mul(Rational(778820736343, 2), Symbol('pi')), Rational(778820736343, 20)), Add(Mul(Integer(-1), Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_103(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (778820736343*pi*skoS2 + 778820736343*pi/2 + 778820736343/20 > -pi*skoS2/8 - pi/16 + 33/160)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Integer(778820736343), Symbol('pi'), Symbol('skoS2')), Mul(Rational(778820736343, 2), Symbol('pi')), Rational(778820736343, 20)), Add(Mul(Integer(-1), Rational(1, 8), Symbol('pi'), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 16), Symbol('pi')), Rational(33, 160))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_104(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (4672924418049*pi*skoS2 + 4672924418049*pi/2 + 4672924418049/20 > -skoSM*(20*pi*skoS2 + 10*pi - 1)/20 + 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Integer(4672924418049), Symbol('pi'), Symbol('skoS2')), Mul(Rational(4672924418049, 2), Symbol('pi')), Rational(4672924418049, 20)), Add(Mul(Integer(-1), Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_105(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (4672924418049*pi*skoS2 + 4672924418049*pi/2 + 4672924418049/20 > -pi*skoS2/8 - pi/16 + 33/160)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Integer(4672924418049), Symbol('pi'), Symbol('skoS2')), Mul(Rational(4672924418049, 2), Symbol('pi')), Rational(4672924418049, 20)), Add(Mul(Integer(-1), Rational(1, 8), Symbol('pi'), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 16), Symbol('pi')), Rational(33, 160))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_106(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (12461131781463*pi*skoS2 + 12461131781463*pi/2 + 12461131781463/20 > -skoSM*(20*pi*skoS2 + 10*pi - 1)/20 + 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Integer(12461131781463), Symbol('pi'), Symbol('skoS2')), Mul(Rational(12461131781463, 2), Symbol('pi')), Rational(12461131781463, 20)), Add(Mul(Integer(-1), Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_107(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (12461131781463*pi*skoS2 + 12461131781463*pi/2 + 12461131781463/20 > -pi*skoS2/8 - pi/16 + 33/160)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Integer(12461131781463), Symbol('pi'), Symbol('skoS2')), Mul(Rational(12461131781463, 2), Symbol('pi')), Rational(12461131781463, 20)), Add(Mul(Integer(-1), Rational(1, 8), Symbol('pi'), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 16), Symbol('pi')), Rational(33, 160))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_108(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (74766790688769*pi*skoS2 + 74766790688769*pi/2 + 74766790688769/20 > -skoSM*(20*pi*skoS2 + 10*pi - 1)/20 + 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Integer(74766790688769), Symbol('pi'), Symbol('skoS2')), Mul(Rational(74766790688769, 2), Symbol('pi')), Rational(74766790688769, 20)), Add(Mul(Integer(-1), Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_109(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (74766790688769*pi*skoS2 + 74766790688769*pi/2 + 74766790688769/20 > -pi*skoS2/8 - pi/16 + 33/160)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Integer(74766790688769), Symbol('pi'), Symbol('skoS2')), Mul(Rational(74766790688769, 2), Symbol('pi')), Rational(74766790688769, 20)), Add(Mul(Integer(-1), Rational(1, 8), Symbol('pi'), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 16), Symbol('pi')), Rational(33, 160))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_110(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (199378108503383*pi*skoS2 + 199378108503383*pi/2 + 199378108503383/20 > -skoSM*(20*pi*skoS2 + 10*pi - 1)/20 + 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Integer(199378108503383), Symbol('pi'), Symbol('skoS2')), Mul(Rational(199378108503383, 2), Symbol('pi')), Rational(199378108503383, 20)), Add(Mul(Integer(-1), Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_111(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (199378108503383*pi*skoS2 + 199378108503383*pi/2 + 199378108503383/20 > -pi*skoS2/8 - pi/16 + 33/160)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Integer(199378108503383), Symbol('pi'), Symbol('skoS2')), Mul(Rational(199378108503383, 2), Symbol('pi')), Rational(199378108503383, 20)), Add(Mul(Integer(-1), Rational(1, 8), Symbol('pi'), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 16), Symbol('pi')), Rational(33, 160))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_112(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (1196268651020289*pi*skoS2 + 1196268651020289*pi/2 + 1196268651020289/20 > -skoSM*(20*pi*skoS2 + 10*pi - 1)/20 + 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Integer(1196268651020289), Symbol('pi'), Symbol('skoS2')), Mul(Rational(1196268651020289, 2), Symbol('pi')), Rational(1196268651020289, 20)), Add(Mul(Integer(-1), Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_113(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (1196268651020289*pi*skoS2 + 1196268651020289*pi/2 + 1196268651020289/20 > -pi*skoS2/8 - pi/16 + 33/160)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Integer(1196268651020289), Symbol('pi'), Symbol('skoS2')), Mul(Rational(1196268651020289, 2), Symbol('pi')), Rational(1196268651020289, 20)), Add(Mul(Integer(-1), Rational(1, 8), Symbol('pi'), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 16), Symbol('pi')), Rational(33, 160))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_114(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (1740027128756784*pi*skoS2 + 870013564378392*pi + 435006782189196/5 > -skoSM*(20*pi*skoS2 + 10*pi - 1)/20 + 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Integer(1740027128756784), Symbol('pi'), Symbol('skoS2')), Mul(Integer(870013564378392), Symbol('pi')), Rational(435006782189196, 5)), Add(Mul(Integer(-1), Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_115(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (1740027128756784*pi*skoS2 + 870013564378392*pi + 435006782189196/5 > -pi*skoS2/8 - pi/16 + 33/160)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Integer(1740027128756784), Symbol('pi'), Symbol('skoS2')), Mul(Integer(870013564378392), Symbol('pi')), Rational(435006782189196, 5)), Add(Mul(Integer(-1), Rational(1, 8), Symbol('pi'), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 16), Symbol('pi')), Rational(33, 160))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_116(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (2251799813685249*pi*skoS2 + 2251799813685249*pi/2 + 2251799813685249/20 > -skoSM*(20*pi*skoS2 + 10*pi - 1)/20 + 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Integer(2251799813685249), Symbol('pi'), Symbol('skoS2')), Mul(Rational(2251799813685249, 2), Symbol('pi')), Rational(2251799813685249, 20)), Add(Mul(Integer(-1), Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_117(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (2251799813685249*pi*skoS2 + 2251799813685249*pi/2 + 2251799813685249/20 > -pi*skoS2/8 - pi/16 + 33/160)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Integer(2251799813685249), Symbol('pi'), Symbol('skoS2')), Mul(Rational(2251799813685249, 2), Symbol('pi')), Rational(2251799813685249, 20)), Add(Mul(Integer(-1), Rational(1, 8), Symbol('pi'), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 16), Symbol('pi')), Rational(33, 160))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_118(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (2430514084612650*pi*skoS2 + 1215257042306325*pi + 243051408461265/2 > -skoSM*(20*pi*skoS2 + 10*pi - 1)/20 + 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Integer(2430514084612650), Symbol('pi'), Symbol('skoS2')), Mul(Integer(1215257042306325), Symbol('pi')), Rational(243051408461265, 2)), Add(Mul(Integer(-1), Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_119(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (2430514084612650*pi*skoS2 + 1215257042306325*pi + 243051408461265/2 > -pi*skoS2/8 - pi/16 + 33/160)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Integer(2430514084612650), Symbol('pi'), Symbol('skoS2')), Mul(Integer(1215257042306325), Symbol('pi')), Rational(243051408461265, 2)), Add(Mul(Integer(-1), Rational(1, 8), Symbol('pi'), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 16), Symbol('pi')), Rational(33, 160))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_120(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (3500773799413503*pi*skoS2 + 3500773799413503*pi/2 + 3500773799413503/20 > -skoSM*(20*pi*skoS2 + 10*pi - 1)/20 + 1/5)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Integer(3500773799413503), Symbol('pi'), Symbol('skoS2')), Mul(Rational(3500773799413503, 2), Symbol('pi')), Rational(3500773799413503, 20)), Add(Mul(Integer(-1), Rational(1, 20), Symbol('skoSM'), Add(Mul(Integer(20), Symbol('pi'), Symbol('skoS2')), Mul(Integer(10), Symbol('pi')), Integer(-1))), Rational(1, 5))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_121(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational,pi:sympy.Rational):
	#(delta >= 0) & (pi > 15707963/5000000) & (skoX > 0) & (pi < 31415927/10000000) & (skoX < 1) & (pi*skoS2 + pi/2 - 1/4 > -3500773799413503*pi*skoS2 - 3500773799413503*pi/2 - 3500773799413503/20)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('pi'), Rational(31415927, 10000000)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Symbol('pi'), Symbol('skoS2')), Mul(Rational(1, 2), Symbol('pi')), Rational(-1, 4)), Add(Mul(Integer(-1), Integer(3500773799413503), Symbol('pi'), Symbol('skoS2')), Mul(Integer(-1), Rational(3500773799413503, 2), Symbol('pi')), Rational(-3500773799413503, 20))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi })

	if eval==True:
		assert eval!=False
		return True
	return False


def post_condition(delta:sympy.Rational, skoX:sympy.Rational, skoS2:sympy.Rational, pi:sympy.Rational, skoSP:sympy.Rational, skoSM:sympy.Rational):
	# (0 <= delta) & (1 > skoX) & (31415927/10000000 > pi) & (pi > 15707963/5000000) & (skoX > 0) & (skoSP*(-pi*skoS2 - pi/2 - 1/20) > skoSM*(-pi*skoS2 - pi/2 + 1/20) + 1/5)

	post_cond =  And(LessThan(Integer(0), Symbol('delta')), StrictGreaterThan(Integer(1), Symbol('skoX')), StrictGreaterThan(Rational(31415927, 10000000), Symbol('pi')), StrictGreaterThan(Symbol('pi'), Rational(15707963, 5000000)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictGreaterThan(Mul(Symbol('skoSP'), Add(Mul(Integer(-1), Symbol('pi'), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 2), Symbol('pi')), Rational(-1, 20))), Add(Mul(Symbol('skoSM'), Add(Mul(Integer(-1), Symbol('pi'), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 2), Symbol('pi')), Rational(1, 20))), Rational(1, 5))))

	eval = post_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'pi':pi, 'skoSP':skoSP, 'skoSM':skoSM })

	return eval == sympy.logic.boolalg.BooleanTrue





if __name__=="__main__":
	
	ip_0=int(input("enter integer numerator of delta:\n"))
	ip_1=int(input("enter integer denominator of delta:\n"))
	assert(ip_1!=0), ("Error denominator entered is 0")
	delta=sympy.Rational(ip_0,ip_1)
	
	
	ip_0=int(input("enter integer numerator of skoX:\n"))
	ip_1=int(input("enter integer denominator of skoX:\n"))
	assert(ip_1!=0), ("Error denominator entered is 0")
	skoX=sympy.Rational(ip_0,ip_1)
	
	
	ip_0=int(input("enter integer numerator of skoS2:\n"))
	ip_1=int(input("enter integer denominator of skoS2:\n"))
	assert(ip_1!=0), ("Error denominator entered is 0")
	skoS2=sympy.Rational(ip_0,ip_1)
	
	
	ip_0=int(input("enter integer numerator of pi:\n"))
	ip_1=int(input("enter integer denominator of pi:\n"))
	assert(ip_1!=0), ("Error denominator entered is 0")
	pi=sympy.Rational(ip_0,ip_1)
	
	
	
	
	if pre_condition_0(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_0 SAT")
		print('delta = 0')
		print('skoX = 1/2')
		print('pi = 26353589/8388608')
		print('skoSP = 1/8')
		print('skoS2 = 1/2')
		print('skoSM = 2')
		exit(0)
	
	
	if pre_condition_1(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_1 SAT")
		print('delta = 0')
		print('skoX = 1/2')
		print('pi = 26353589/8388608')
		print('skoSP = 1/8')
		print('skoS2 = 1/2')
		print('skoSM = 2')
		exit(0)
	
	
	if pre_condition_2(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_2 SAT")
		print('delta = 0')
		print('skoX = 1/20000000')
		print('pi = 26353589/8388608')
		print('skoSP = 1')
		print('skoS2 = -25165824/26353589')
		print('skoSM = 0')
		exit(0)
	
	
	if pre_condition_3(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_3 SAT")
		print('delta = 0')
		print('skoX = 1/20000000')
		print('pi = 26353589/8388608')
		print('skoSP = 1')
		print('skoS2 = -25165824/26353589')
		print('skoSM = 0')
		exit(0)
	
	
	if pre_condition_4(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_4 SAT")
		print('delta = 0')
		print('skoX = 1/20000000')
		print('pi = 210828717/67108864')
		print('skoSP = 0')
		print('skoS2 = -94896128/210828717')
		print('skoSM = 2')
		exit(0)
	
	
	if pre_condition_5(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_5 SAT")
		print('delta = 0')
		print('skoX = 1/20000000')
		print('pi = 210828717/67108864')
		print('skoSP = 0')
		print('skoS2 = -94896128/210828717')
		print('skoSM = 2')
		exit(0)
	
	
	if pre_condition_6(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_6 SAT")
		print('delta = 0')
		print('skoX = 1/20000000')
		print('pi = 26353589/8388608')
		print('skoSP = 5')
		print('skoS2 = -14680064/26353589')
		print('skoSM = 1')
		exit(0)
	
	
	if pre_condition_7(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_7 SAT")
		print('delta = 0')
		print('skoX = 1/20000000')
		print('pi = 26353589/8388608')
		print('skoSP = 5')
		print('skoS2 = -14680064/26353589')
		print('skoSM = 1')
		exit(0)
	
	
	if pre_condition_8(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_8 SAT")
		print('delta = 0')
		print('skoX = 1/20000000')
		print('pi = 26353589/8388608')
		print('skoSP = 49')
		print('skoS2 = -13631488/26353589')
		print('skoSM = 0')
		exit(0)
	
	
	if pre_condition_9(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_9 SAT")
		print('delta = 0')
		print('skoX = 1/20000000')
		print('pi = 26353589/8388608')
		print('skoSP = 49')
		print('skoS2 = -13631488/26353589')
		print('skoSM = 0')
		exit(0)
	
	
	if pre_condition_10(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_10 SAT")
		print('delta = 0')
		print('skoX = 1/20000000')
		print('pi = 26353589/8388608')
		print('skoSP = 337')
		print('skoS2 = -13598720/26353589')
		print('skoSM = -1')
		exit(0)
	
	
	if pre_condition_11(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_11 SAT")
		print('delta = 0')
		print('skoX = 1/20000000')
		print('pi = 26353589/8388608')
		print('skoSP = 337')
		print('skoS2 = -13598720/26353589')
		print('skoSM = -1')
		exit(0)
	
	
	if pre_condition_12(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_12 SAT")
		print('delta = 0')
		print('skoX = 1/20000000')
		print('pi = 26353589/8388608')
		print('skoSP = 1877')
		print('skoS2 = -13596672/26353589')
		print('skoSM = -1')
		exit(0)
	
	
	if pre_condition_13(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_13 SAT")
		print('delta = 0')
		print('skoX = 1/20000000')
		print('pi = 26353589/8388608')
		print('skoSP = 1877')
		print('skoS2 = -13596672/26353589')
		print('skoSM = -1')
		exit(0)
	
	
	if pre_condition_14(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_14 SAT")
		print('delta = 0')
		print('skoX = 1/20000000')
		print('pi = 26353589/8388608')
		print('skoSP = 4390')
		print('skoS2 = -13596416/26353589')
		print('skoSM = -1')
		exit(0)
	
	
	if pre_condition_15(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_15 SAT")
		print('delta = 0')
		print('skoX = 1/20000000')
		print('pi = 26353589/8388608')
		print('skoSP = 4390')
		print('skoS2 = -13596416/26353589')
		print('skoSM = -1')
		exit(0)
	
	
	if pre_condition_16(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_16 SAT")
		print('delta = 0')
		print('skoX = 1/20000000')
		print('pi = 26353589/8388608')
		print('skoSP = 13295')
		print('skoS2 = -13596288/26353589')
		print('skoSM = -1')
		exit(0)
	
	
	if pre_condition_17(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_17 SAT")
		print('delta = 0')
		print('skoX = 1/20000000')
		print('pi = 26353589/8388608')
		print('skoSP = 13295')
		print('skoS2 = -13596288/26353589')
		print('skoSM = -1')
		exit(0)
	
	
	if pre_condition_18(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_18 SAT")
		print('delta = 0')
		print('skoX = 1/20000000')
		print('pi = 26353589/8388608')
		print('skoSP = 26974')
		print('skoS2 = -13596256/26353589')
		print('skoSM = -1')
		exit(0)
	
	
	if pre_condition_19(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_19 SAT")
		print('delta = 0')
		print('skoX = 1/20000000')
		print('pi = 26353589/8388608')
		print('skoSP = 26974')
		print('skoS2 = -13596256/26353589')
		print('skoSM = -1')
		exit(0)
	
	
	if pre_condition_20(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_20 SAT")
		print('delta = 0')
		print('skoX = 1/20000000')
		print('pi = 26353589/8388608')
		print('skoSP = 55554')
		print('skoS2 = -13596240/26353589')
		print('skoSM = -1')
		exit(0)
	
	
	if pre_condition_21(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_21 SAT")
		print('delta = 0')
		print('skoX = 1/20000000')
		print('pi = 26353589/8388608')
		print('skoSP = 55554')
		print('skoS2 = -13596240/26353589')
		print('skoSM = -1')
		exit(0)
	
	
	if pre_condition_22(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_22 SAT")
		print('delta = 0')
		print('skoX = 1/20000000')
		print('pi = 26353589/8388608')
		print('skoSP = 118150')
		print('skoS2 = -13596232/26353589')
		print('skoSM = -1')
		exit(0)
	
	
	if pre_condition_23(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_23 SAT")
		print('delta = 0')
		print('skoX = 1/20000000')
		print('pi = 26353589/8388608')
		print('skoSP = 118150')
		print('skoS2 = -13596232/26353589')
		print('skoSM = -1')
		exit(0)
	
	
	if pre_condition_24(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_24 SAT")
		print('delta = 0')
		print('skoX = 1/20000000')
		print('pi = 26353589/8388608')
		print('skoSP = 270601')
		print('skoS2 = -13596228/26353589')
		print('skoSM = -1')
		exit(0)
	
	
	if pre_condition_25(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_25 SAT")
		print('delta = 0')
		print('skoX = 1/20000000')
		print('pi = 26353589/8388608')
		print('skoSP = 270601')
		print('skoS2 = -13596228/26353589')
		print('skoSM = -1')
		exit(0)
	
	
	if pre_condition_26(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_26 SAT")
		print('delta = 0')
		print('skoX = 1/20000000')
		print('pi = 26353589/8388608')
		print('skoSP = 762601')
		print('skoS2 = -13596226/26353589')
		print('skoSM = -1')
		exit(0)
	
	
	if pre_condition_27(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_27 SAT")
		print('delta = 0')
		print('skoX = 1/20000000')
		print('pi = 26353589/8388608')
		print('skoSP = 762601')
		print('skoS2 = -13596226/26353589')
		print('skoSM = -1')
		exit(0)
	
	
	if pre_condition_28(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_28 SAT")
		print('delta = 0')
		print('skoX = 1/20000000')
		print('pi = 26353589/8388608')
		print('skoSP = 8388608')
		print('skoS2 = -13596225/26353589')
		print('skoSM = -1')
		exit(0)
	
	
	if pre_condition_29(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_29 SAT")
		print('delta = 0')
		print('skoX = 1/20000000')
		print('pi = 26353589/8388608')
		print('skoSP = 8388608')
		print('skoS2 = -13596225/26353589')
		print('skoSM = -1')
		exit(0)
	
	
	if pre_condition_30(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_30 SAT")
		print('delta = 0')
		print('skoX = 1/20000000')
		print('pi = 26353589/8388608')
		print('skoSP = 22369622')
		print('skoS2 = -217539599/421657424')
		print('skoSM = -1')
		exit(0)
	
	
	if pre_condition_31(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_31 SAT")
		print('delta = 0')
		print('skoX = 1/20000000')
		print('pi = 26353589/8388608')
		print('skoSP = 22369622')
		print('skoS2 = -217539599/421657424')
		print('skoSM = -1')
		exit(0)
	
	
	if pre_condition_32(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_32 SAT")
		print('delta = 0')
		print('skoX = 1/20000000')
		print('pi = 26353589/8388608')
		print('skoSP = 134217728')
		print('skoS2 = -435079197/843314848')
		print('skoSM = -1')
		exit(0)
	
	
	if pre_condition_33(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_33 SAT")
		print('delta = 0')
		print('skoX = 1/20000000')
		print('pi = 26353589/8388608')
		print('skoSP = 134217728')
		print('skoS2 = -435079197/843314848')
		print('skoSM = -1')
		exit(0)
	
	
	if pre_condition_34(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_34 SAT")
		print('delta = 0')
		print('skoX = 1/20000000')
		print('pi = 26353589/8388608')
		print('skoSP = 357913942')
		print('skoS2 = -3480633575/6746518784')
		print('skoSM = -1')
		exit(0)
	
	
	if pre_condition_35(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_35 SAT")
		print('delta = 0')
		print('skoX = 1/20000000')
		print('pi = 26353589/8388608')
		print('skoSP = 357913942')
		print('skoS2 = -3480633575/6746518784')
		print('skoSM = -1')
		exit(0)
	
	
	if pre_condition_36(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_36 SAT")
		print('delta = 0')
		print('skoX = 1/20000000')
		print('pi = 26353589/8388608')
		print('skoSP = 2147483648')
		print('skoS2 = -6961267149/13493037568')
		print('skoSM = -1')
		exit(0)
	
	
	if pre_condition_37(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_37 SAT")
		print('delta = 0')
		print('skoX = 1/20000000')
		print('pi = 26353589/8388608')
		print('skoSP = 2147483648')
		print('skoS2 = -6961267149/13493037568')
		print('skoSM = -1')
		exit(0)
	
	
	if pre_condition_38(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_38 SAT")
		print('delta = 0')
		print('skoX = 1/20000000')
		print('pi = 26353589/8388608')
		print('skoSP = 5726623062')
		print('skoS2 = -55690137191/107944300544')
		print('skoSM = -1')
		exit(0)
	
	
	if pre_condition_39(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_39 SAT")
		print('delta = 0')
		print('skoX = 1/20000000')
		print('pi = 26353589/8388608')
		print('skoSP = 5726623062')
		print('skoS2 = -55690137191/107944300544')
		print('skoSM = -1')
		exit(0)
	
	
	if pre_condition_40(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_40 SAT")
		print('delta = 0')
		print('skoX = 1/20000000')
		print('pi = 26353589/8388608')
		print('skoSP = 34359738368')
		print('skoS2 = -111380274381/215888601088')
		print('skoSM = -1')
		exit(0)
	
	
	if pre_condition_41(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_41 SAT")
		print('delta = 0')
		print('skoX = 1/20000000')
		print('pi = 26353589/8388608')
		print('skoSP = 34359738368')
		print('skoS2 = -111380274381/215888601088')
		print('skoSM = -1')
		exit(0)
	
	
	if pre_condition_42(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_42 SAT")
		print('delta = 0')
		print('skoX = 1/20000000')
		print('pi = 26353589/8388608')
		print('skoSP = 91625968982')
		print('skoS2 = -891042195047/1727108808704')
		print('skoSM = -1')
		exit(0)
	
	
	if pre_condition_43(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_43 SAT")
		print('delta = 0')
		print('skoX = 1/20000000')
		print('pi = 26353589/8388608')
		print('skoSP = 91625968982')
		print('skoS2 = -891042195047/1727108808704')
		print('skoSM = -1')
		exit(0)
	
	
	if pre_condition_44(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_44 SAT")
		print('delta = 0')
		print('skoX = 1/20000000')
		print('pi = 26353589/8388608')
		print('skoSP = 549755813888')
		print('skoS2 = -1782084390093/3454217617408')
		print('skoSM = -1')
		exit(0)
	
	
	if pre_condition_45(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_45 SAT")
		print('delta = 0')
		print('skoX = 1/20000000')
		print('pi = 26353589/8388608')
		print('skoSP = 549755813888')
		print('skoS2 = -1782084390093/3454217617408')
		print('skoSM = -1')
		exit(0)
	
	
	if pre_condition_46(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_46 SAT")
		print('delta = 0')
		print('skoX = 1/20000000')
		print('pi = 26353589/8388608')
		print('skoSP = 1466015503702')
		print('skoS2 = -14256675120743/27633740939264')
		print('skoSM = -1')
		exit(0)
	
	
	if pre_condition_47(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_47 SAT")
		print('delta = 0')
		print('skoX = 1/20000000')
		print('pi = 26353589/8388608')
		print('skoSP = 1466015503702')
		print('skoS2 = -14256675120743/27633740939264')
		print('skoSM = -1')
		exit(0)
	
	
	if pre_condition_48(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_48 SAT")
		print('delta = 0')
		print('skoX = 1/20000000')
		print('pi = 26353589/8388608')
		print('skoSP = 8796093022208')
		print('skoS2 = -28513350241485/55267481878528')
		print('skoSM = -1')
		exit(0)
	
	
	if pre_condition_49(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_49 SAT")
		print('delta = 0')
		print('skoX = 1/20000000')
		print('pi = 26353589/8388608')
		print('skoSP = 8796093022208')
		print('skoS2 = -28513350241485/55267481878528')
		print('skoSM = -1')
		exit(0)
	
	
	if pre_condition_50(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_50 SAT")
		print('delta = 0')
		print('skoX = 1/20000000')
		print('pi = 26353589/8388608')
		print('skoSP = 23456248059222')
		print('skoS2 = -228106801931879/442139855028224')
		print('skoSM = -1')
		exit(0)
	
	
	if pre_condition_51(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_51 SAT")
		print('delta = 0')
		print('skoX = 1/20000000')
		print('pi = 26353589/8388608')
		print('skoSP = 23456248059222')
		print('skoS2 = -228106801931879/442139855028224')
		print('skoSM = -1')
		exit(0)
	
	
	if pre_condition_52(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_52 SAT")
		print('delta = 0')
		print('skoX = 1/20000000')
		print('pi = 26353589/8388608')
		print('skoSP = 140737488355328')
		print('skoS2 = -456213603863757/884279710056448')
		print('skoSM = -1')
		exit(0)
	
	
	if pre_condition_53(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_53 SAT")
		print('delta = 0')
		print('skoX = 1/20000000')
		print('pi = 26353589/8388608')
		print('skoSP = 140737488355328')
		print('skoS2 = -456213603863757/884279710056448')
		print('skoSM = -1')
		exit(0)
	
	
	if pre_condition_54(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_54 SAT")
		print('delta = 0')
		print('skoX = 1/20000000')
		print('pi = 26353589/8388608')
		print('skoSP = 375299968947542')
		print('skoS2 = -3649708830910055/7074237680451584')
		print('skoSM = -1')
		exit(0)
	
	
	if pre_condition_55(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_55 SAT")
		print('delta = 0')
		print('skoX = 1/20000000')
		print('pi = 26353589/8388608')
		print('skoSP = 375299968947542')
		print('skoS2 = -3649708830910055/7074237680451584')
		print('skoSM = -1')
		exit(0)
	
	
	if pre_condition_56(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_56 SAT")
		print('delta = 0')
		print('skoX = 1/20000000')
		print('pi = 26353589/8388608')
		print('skoSP = 2251799813685248')
		print('skoS2 = -7299417661820109/14148475360903168')
		print('skoSM = -1')
		exit(0)
	
	
	if pre_condition_57(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_57 SAT")
		print('delta = 0')
		print('skoX = 1/20000000')
		print('pi = 26353589/8388608')
		print('skoSP = 2251799813685248')
		print('skoS2 = -7299417661820109/14148475360903168')
		print('skoSM = -1')
		exit(0)
	
	
	if pre_condition_58(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_58 SAT")
		print('delta = 0')
		print('skoX = 1/20000000')
		print('pi = 26353589/8388608')
		print('skoSP = 6004799503160662')
		print('skoS2 = -58395341294560871/113187802887225344')
		print('skoSM = -1')
		exit(0)
	
	
	if pre_condition_59(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_59 SAT")
		print('delta = 0')
		print('skoX = 1/20000000')
		print('pi = 26353589/8388608')
		print('skoSP = 6004799503160662')
		print('skoS2 = -58395341294560871/113187802887225344')
		print('skoSM = -1')
		exit(0)
	
	
	if pre_condition_60(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_60 SAT")
		print('delta = 0')
		print('skoX = 1/20000000')
		print('pi = 26353589/8388608')
		print('skoSP = 36028797018963968')
		print('skoS2 = -116790682589121741/226375605774450688')
		print('skoSM = -1')
		exit(0)
	
	
	if pre_condition_61(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_61 SAT")
		print('delta = 0')
		print('skoX = 1/20000000')
		print('pi = 26353589/8388608')
		print('skoSP = 36028797018963968')
		print('skoS2 = -116790682589121741/226375605774450688')
		print('skoSM = -1')
		exit(0)
	
	
	if pre_condition_62(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_62 SAT")
		print('delta = 0')
		print('skoX = 1/20000000')
		print('pi = 26353589/8388608')
		print('skoSP = -3')
		print('skoS2 = -12582912/26353589')
		print('skoSM = 1/8')
		exit(0)
	
	
	if pre_condition_63(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_63 SAT")
		print('delta = 0')
		print('skoX = 1/20000000')
		print('pi = 26353589/8388608')
		print('skoSP = -3')
		print('skoS2 = -12582912/26353589')
		print('skoSM = 1/8')
		exit(0)
	
	
	if pre_condition_64(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_64 SAT")
		print('delta = 0')
		print('skoX = 1/20000000')
		print('pi = 26353589/8388608')
		print('skoSP = -5')
		print('skoS2 = -13107200/26353589')
		print('skoSM = 0')
		exit(0)
	
	
	if pre_condition_65(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_65 SAT")
		print('delta = 0')
		print('skoX = 1/20000000')
		print('pi = 26353589/8388608')
		print('skoSP = -5')
		print('skoS2 = -13107200/26353589')
		print('skoSM = 0')
		exit(0)
	
	
	if pre_condition_66(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_66 SAT")
		print('delta = 0')
		print('skoX = 1/20000000')
		print('pi = 26353589/8388608')
		print('skoSP = -9')
		print('skoS2 = -13369344/26353589')
		print('skoSM = 1/8')
		exit(0)
	
	
	if pre_condition_67(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_67 SAT")
		print('delta = 0')
		print('skoX = 1/20000000')
		print('pi = 26353589/8388608')
		print('skoSP = -9')
		print('skoS2 = -13369344/26353589')
		print('skoSM = 1/8')
		exit(0)
	
	
	if pre_condition_68(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_68 SAT")
		print('delta = 0')
		print('skoX = 1/20000000')
		print('pi = 26353589/8388608')
		print('skoSP = -20')
		print('skoS2 = -13500416/26353589')
		print('skoSM = 1/8')
		exit(0)
	
	
	if pre_condition_69(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_69 SAT")
		print('delta = 0')
		print('skoX = 1/20000000')
		print('pi = 26353589/8388608')
		print('skoSP = -20')
		print('skoS2 = -13500416/26353589')
		print('skoSM = 1/8')
		exit(0)
	
	
	if pre_condition_70(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_70 SAT")
		print('delta = 0')
		print('skoX = 1/20000000')
		print('pi = 26353589/8388608')
		print('skoSP = -60')
		print('skoS2 = -13565952/26353589')
		print('skoSM = 1/8')
		exit(0)
	
	
	if pre_condition_71(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_71 SAT")
		print('delta = 0')
		print('skoX = 1/20000000')
		print('pi = 26353589/8388608')
		print('skoSP = -60')
		print('skoS2 = -13565952/26353589')
		print('skoSM = 1/8')
		exit(0)
	
	
	if pre_condition_72(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_72 SAT")
		print('delta = 0')
		print('skoX = 1/20000000')
		print('pi = 26353589/8388608')
		print('skoSP = -130')
		print('skoS2 = -13582336/26353589')
		print('skoSM = 1/8')
		exit(0)
	
	
	if pre_condition_73(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_73 SAT")
		print('delta = 0')
		print('skoX = 1/20000000')
		print('pi = 26353589/8388608')
		print('skoSP = -130')
		print('skoS2 = -13582336/26353589')
		print('skoSM = 1/8')
		exit(0)
	
	
	if pre_condition_74(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_74 SAT")
		print('delta = 0')
		print('skoX = 1/20000000')
		print('pi = 26353589/8388608')
		print('skoSP = -314')
		print('skoS2 = -13590528/26353589')
		print('skoSM = 1/8')
		exit(0)
	
	
	if pre_condition_75(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_75 SAT")
		print('delta = 0')
		print('skoX = 1/20000000')
		print('pi = 26353589/8388608')
		print('skoSP = -314')
		print('skoS2 = -13590528/26353589')
		print('skoSM = 1/8')
		exit(0)
	
	
	if pre_condition_76(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_76 SAT")
		print('delta = 0')
		print('skoX = 1/20000000')
		print('pi = 26353589/8388608')
		print('skoSP = -1115')
		print('skoS2 = -13594624/26353589')
		print('skoSM = 1/8')
		exit(0)
	
	
	if pre_condition_77(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_77 SAT")
		print('delta = 0')
		print('skoX = 1/20000000')
		print('pi = 26353589/8388608')
		print('skoSP = -1115')
		print('skoS2 = -13594624/26353589')
		print('skoSM = 1/8')
		exit(0)
	
	
	if pre_condition_78(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_78 SAT")
		print('delta = 0')
		print('skoX = 1/20000000')
		print('pi = 26353589/8388608')
		print('skoSP = -3091')
		print('skoS2 = -13595648/26353589')
		print('skoSM = 1/8')
		exit(0)
	
	
	if pre_condition_79(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_79 SAT")
		print('delta = 0')
		print('skoX = 1/20000000')
		print('pi = 26353589/8388608')
		print('skoSP = -3091')
		print('skoS2 = -13595648/26353589')
		print('skoSM = 1/8')
		exit(0)
	
	
	if pre_condition_80(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_80 SAT")
		print('delta = 0')
		print('skoX = 1/20000000')
		print('pi = 26353589/8388608')
		print('skoSP = -27468')
		print('skoS2 = -13596160/26353589')
		print('skoSM = 1/8')
		exit(0)
	
	
	if pre_condition_81(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_81 SAT")
		print('delta = 0')
		print('skoX = 1/20000000')
		print('pi = 26353589/8388608')
		print('skoSP = -27468')
		print('skoS2 = -13596160/26353589')
		print('skoSM = 1/8')
		exit(0)
	
	
	if pre_condition_82(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_82 SAT")
		print('delta = 0')
		print('skoX = 1/20000000')
		print('pi = 26353589/8388608')
		print('skoSP = -1980645')
		print('skoS2 = -13596224/26353589')
		print('skoSM = 1/8')
		exit(0)
	
	
	if pre_condition_83(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_83 SAT")
		print('delta = 0')
		print('skoX = 1/20000000')
		print('pi = 26353589/8388608')
		print('skoSP = -1980645')
		print('skoS2 = -13596224/26353589')
		print('skoSM = 1/8')
		exit(0)
	
	
	if pre_condition_84(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_84 SAT")
		print('delta = 0')
		print('skoX = 1/20000000')
		print('pi = 26353589/8388608')
		print('skoSP = -4456449')
		print('skoS2 = -27192449/52707178')
		print('skoSM = 1/8')
		exit(0)
	
	
	if pre_condition_85(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_85 SAT")
		print('delta = 0')
		print('skoX = 1/20000000')
		print('pi = 26353589/8388608')
		print('skoSP = -4456449')
		print('skoS2 = -27192449/52707178')
		print('skoSM = 1/8')
		exit(0)
	
	
	if pre_condition_86(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_86 SAT")
		print('delta = 0')
		print('skoX = 1/20000000')
		print('pi = 26353589/8388608')
		print('skoSP = -11883863')
		print('skoS2 = -54384899/105414356')
		print('skoSM = 1/8')
		exit(0)
	
	
	if pre_condition_87(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_87 SAT")
		print('delta = 0')
		print('skoX = 1/20000000')
		print('pi = 26353589/8388608')
		print('skoSP = -11883863')
		print('skoS2 = -54384899/105414356')
		print('skoSM = 1/8')
		exit(0)
	
	
	if pre_condition_88(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_88 SAT")
		print('delta = 0')
		print('skoX = 1/20000000')
		print('pi = 26353589/8388608')
		print('skoSP = -71303169')
		print('skoS2 = -108769799/210828712')
		print('skoSM = 1/8')
		exit(0)
	
	
	if pre_condition_89(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_89 SAT")
		print('delta = 0')
		print('skoX = 1/20000000')
		print('pi = 26353589/8388608')
		print('skoSP = -71303169')
		print('skoS2 = -108769799/210828712')
		print('skoSM = 1/8')
		exit(0)
	
	
	if pre_condition_90(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_90 SAT")
		print('delta = 0')
		print('skoX = 1/20000000')
		print('pi = 26353589/8388608')
		print('skoSP = -190141783')
		print('skoS2 = -870158393/1686629696')
		print('skoSM = 1/8')
		exit(0)
	
	
	if pre_condition_91(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_91 SAT")
		print('delta = 0')
		print('skoX = 1/20000000')
		print('pi = 26353589/8388608')
		print('skoSP = -190141783')
		print('skoS2 = -870158393/1686629696')
		print('skoSM = 1/8')
		exit(0)
	
	
	if pre_condition_92(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_92 SAT")
		print('delta = 0')
		print('skoX = 1/20000000')
		print('pi = 26353589/8388608')
		print('skoSP = -1140850689')
		print('skoS2 = -1740316787/3373259392')
		print('skoSM = 1/8')
		exit(0)
	
	
	if pre_condition_93(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_93 SAT")
		print('delta = 0')
		print('skoX = 1/20000000')
		print('pi = 26353589/8388608')
		print('skoSP = -1140850689')
		print('skoS2 = -1740316787/3373259392')
		print('skoSM = 1/8')
		exit(0)
	
	
	if pre_condition_94(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_94 SAT")
		print('delta = 0')
		print('skoX = 1/20000000')
		print('pi = 26353589/8388608')
		print('skoSP = -3042268503')
		print('skoS2 = -732764963/1420319744')
		print('skoSM = 1/8')
		exit(0)
	
	
	if pre_condition_95(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_95 SAT")
		print('delta = 0')
		print('skoX = 1/20000000')
		print('pi = 26353589/8388608')
		print('skoSP = -3042268503')
		print('skoS2 = -732764963/1420319744')
		print('skoSM = 1/8')
		exit(0)
	
	
	if pre_condition_96(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_96 SAT")
		print('delta = 0')
		print('skoX = 1/20000000')
		print('pi = 26353589/8388608')
		print('skoSP = -18253611009')
		print('skoS2 = -27845068595/53972150272')
		print('skoSM = 1/8')
		exit(0)
	
	
	if pre_condition_97(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_97 SAT")
		print('delta = 0')
		print('skoX = 1/20000000')
		print('pi = 26353589/8388608')
		print('skoSP = -18253611009')
		print('skoS2 = -27845068595/53972150272')
		print('skoSM = 1/8')
		exit(0)
	
	
	if pre_condition_98(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_98 SAT")
		print('delta = 0')
		print('skoX = 1/20000000')
		print('pi = 26353589/8388608')
		print('skoSP = -48676296023')
		print('skoS2 = -222760548761/431777202176')
		print('skoSM = 1/8')
		exit(0)
	
	
	if pre_condition_99(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_99 SAT")
		print('delta = 0')
		print('skoX = 1/20000000')
		print('pi = 26353589/8388608')
		print('skoSP = -48676296023')
		print('skoS2 = -222760548761/431777202176')
		print('skoSM = 1/8')
		exit(0)
	
	
	if pre_condition_100(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_100 SAT")
		print('delta = 0')
		print('skoX = 1/20000000')
		print('pi = 26353589/8388608')
		print('skoSP = -292057776129')
		print('skoS2 = -23448478817/45450231808')
		print('skoSM = 1/8')
		exit(0)
	
	
	if pre_condition_101(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_101 SAT")
		print('delta = 0')
		print('skoX = 1/20000000')
		print('pi = 26353589/8388608')
		print('skoSP = -292057776129')
		print('skoS2 = -23448478817/45450231808')
		print('skoSM = 1/8')
		exit(0)
	
	
	if pre_condition_102(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_102 SAT")
		print('delta = 0')
		print('skoX = 1/20000000')
		print('pi = 26353589/8388608')
		print('skoSP = -778820736343')
		print('skoS2 = -3564168780185/6908435234816')
		print('skoSM = 1/8')
		exit(0)
	
	
	if pre_condition_103(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_103 SAT")
		print('delta = 0')
		print('skoX = 1/20000000')
		print('pi = 26353589/8388608')
		print('skoSP = -778820736343')
		print('skoS2 = -3564168780185/6908435234816')
		print('skoSM = 1/8')
		exit(0)
	
	
	if pre_condition_104(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_104 SAT")
		print('delta = 0')
		print('skoX = 1/20000000')
		print('pi = 26353589/8388608')
		print('skoSP = -4672924418049')
		print('skoS2 = -7128337560371/13816870469632')
		print('skoSM = 1/8')
		exit(0)
	
	
	if pre_condition_105(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_105 SAT")
		print('delta = 0')
		print('skoX = 1/20000000')
		print('pi = 26353589/8388608')
		print('skoSP = -4672924418049')
		print('skoS2 = -7128337560371/13816870469632')
		print('skoSM = 1/8')
		exit(0)
	
	
	if pre_condition_106(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_106 SAT")
		print('delta = 0')
		print('skoX = 1/20000000')
		print('pi = 26353589/8388608')
		print('skoSP = -12461131781463')
		print('skoS2 = -57026700482969/110534963757056')
		print('skoSM = 1/8')
		exit(0)
	
	
	if pre_condition_107(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_107 SAT")
		print('delta = 0')
		print('skoX = 1/20000000')
		print('pi = 26353589/8388608')
		print('skoSP = -12461131781463')
		print('skoS2 = -57026700482969/110534963757056')
		print('skoSM = 1/8')
		exit(0)
	
	
	if pre_condition_108(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_108 SAT")
		print('delta = 0')
		print('skoX = 1/20000000')
		print('pi = 26353589/8388608')
		print('skoSP = -74766790688769')
		print('skoS2 = -114053400965939/221069927514112')
		print('skoSM = 1/8')
		exit(0)
	
	
	if pre_condition_109(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_109 SAT")
		print('delta = 0')
		print('skoX = 1/20000000')
		print('pi = 26353589/8388608')
		print('skoSP = -74766790688769')
		print('skoS2 = -114053400965939/221069927514112')
		print('skoSM = 1/8')
		exit(0)
	
	
	if pre_condition_110(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_110 SAT")
		print('delta = 0')
		print('skoX = 1/20000000')
		print('pi = 26353589/8388608')
		print('skoSP = -199378108503383')
		print('skoS2 = -912427207727513/1768559420112896')
		print('skoSM = 1/8')
		exit(0)
	
	
	if pre_condition_111(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_111 SAT")
		print('delta = 0')
		print('skoX = 1/20000000')
		print('pi = 26353589/8388608')
		print('skoSP = -199378108503383')
		print('skoS2 = -912427207727513/1768559420112896')
		print('skoSM = 1/8')
		exit(0)
	
	
	if pre_condition_112(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_112 SAT")
		print('delta = 0')
		print('skoX = 1/20000000')
		print('pi = 26353589/8388608')
		print('skoSP = -1196268651020289')
		print('skoS2 = -1824854415455027/3537118840225792')
		print('skoSM = 1/8')
		exit(0)
	
	
	if pre_condition_113(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_113 SAT")
		print('delta = 0')
		print('skoX = 1/20000000')
		print('pi = 26353589/8388608')
		print('skoSP = -1196268651020289')
		print('skoS2 = -1824854415455027/3537118840225792')
		print('skoSM = 1/8')
		exit(0)
	
	
	if pre_condition_114(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_114 SAT")
		print('delta = 0')
		print('skoX = 1/20000000')
		print('pi = 26353589/8388608')
		print('skoSP = -1740027128756784')
		print('skoS2 = -29197670647280433/56593901443612672')
		print('skoSM = 1/8')
		exit(0)
	
	
	if pre_condition_115(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_115 SAT")
		print('delta = 0')
		print('skoX = 1/20000000')
		print('pi = 26353589/8388608')
		print('skoSP = -1740027128756784')
		print('skoS2 = -29197670647280433/56593901443612672')
		print('skoSM = 1/8')
		exit(0)
	
	
	if pre_condition_116(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_116 SAT")
		print('delta = 0')
		print('skoX = 1/20000000')
		print('pi = 26353589/8388608')
		print('skoSP = -2251799813685249')
		print('skoS2 = -58395341294560867/113187802887225344')
		print('skoSM = 1/8')
		exit(0)
	
	
	if pre_condition_117(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_117 SAT")
		print('delta = 0')
		print('skoX = 1/20000000')
		print('pi = 26353589/8388608')
		print('skoSP = -2251799813685249')
		print('skoS2 = -58395341294560867/113187802887225344')
		print('skoSM = 1/8')
		exit(0)
	
	
	if pre_condition_118(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_118 SAT")
		print('delta = 0')
		print('skoX = 1/20000000')
		print('pi = 26353589/8388608')
		print('skoSP = -2430514084612650')
		print('skoS2 = -233581365178243469/452751211548901376')
		print('skoSM = 1/8')
		exit(0)
	
	
	if pre_condition_119(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_119 SAT")
		print('delta = 0')
		print('skoX = 1/20000000')
		print('pi = 26353589/8388608')
		print('skoSP = -2430514084612650')
		print('skoS2 = -233581365178243469/452751211548901376')
		print('skoSM = 1/8')
		exit(0)
	
	
	if pre_condition_120(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_120 SAT")
		print('delta = 0')
		print('skoX = 1/20000000')
		print('pi = 26353589/8388608')
		print('skoSP = -3500773799413503')
		print('skoS2 = -934325460712973877/1811004846195605504')
		print('skoSM = 1')
		exit(0)
	
	
	if pre_condition_121(delta=delta,skoX=skoX,skoS2=skoS2,pi=pi)==True:
		print("pre_condition_121 SAT")
		print('delta = 0')
		print('skoX = 1/20000000')
		print('pi = 26353589/8388608')
		print('skoSP = -3500773799413503')
		print('skoS2 = -934325460712973877/1811004846195605504')
		print('skoSM = 1')
		exit(0)


	print("Weakest pre-condition UNSAT")
	exit(0)
