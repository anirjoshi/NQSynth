import sympy
from sympy import *

def pre_condition_0(y:sympy.Rational):
	#((y >= sqrt(7959)/40) | (y > -sqrt(319)/8)) & ((y >= sqrt(7959)/40) | (y < -sqrt(7959)/40)) & ((y <= sqrt(319)/8) | (y > -sqrt(319)/8)) & ((y <= sqrt(319)/8) | (y < -sqrt(7959)/40))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(1, 40), Pow(Integer(7959), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 8), Pow(Integer(319), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(1, 40), Pow(Integer(7959), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 40), Pow(Integer(7959), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 8), Pow(Integer(319), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 8), Pow(Integer(319), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 8), Pow(Integer(319), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 40), Pow(Integer(7959), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1(y:sympy.Rational):
	#((y >= sqrt(24591)/1280) | (y > -sqrt(1639)/256)) & ((y >= sqrt(24591)/1280) | (y < -sqrt(24591)/1280)) & ((y <= sqrt(1639)/256) | (y > -sqrt(1639)/256)) & ((y <= sqrt(1639)/256) | (y < -sqrt(24591)/1280))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(1, 1280), Pow(Integer(24591), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 256), Pow(Integer(1639), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(1, 1280), Pow(Integer(24591), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1280), Pow(Integer(24591), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 256), Pow(Integer(1639), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 256), Pow(Integer(1639), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 256), Pow(Integer(1639), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1280), Pow(Integer(24591), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_2(y:sympy.Rational):
	#((y >= sqrt(6549991)/1280) | (y > -sqrt(262655)/256)) & ((y >= sqrt(6549991)/1280) | (y < -sqrt(6549991)/1280)) & ((y <= sqrt(262655)/256) | (y > -sqrt(262655)/256)) & ((y <= sqrt(262655)/256) | (y < -sqrt(6549991)/1280))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(1, 1280), Pow(Integer(6549991), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 256), Pow(Integer(262655), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(1, 1280), Pow(Integer(6549991), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1280), Pow(Integer(6549991), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 256), Pow(Integer(262655), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 256), Pow(Integer(262655), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 256), Pow(Integer(262655), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1280), Pow(Integer(6549991), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_3(y:sympy.Rational):
	#((y >= 7*sqrt(37671)/640) | (y > -sqrt(73999)/128)) & ((y >= 7*sqrt(37671)/640) | (y < -7*sqrt(37671)/640)) & ((y <= sqrt(73999)/128) | (y > -sqrt(73999)/128)) & ((y <= sqrt(73999)/128) | (y < -7*sqrt(37671)/640))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(7, 640), Pow(Integer(37671), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 128), Pow(Integer(73999), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(7, 640), Pow(Integer(37671), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(7, 640), Pow(Integer(37671), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 128), Pow(Integer(73999), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 128), Pow(Integer(73999), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 128), Pow(Integer(73999), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(7, 640), Pow(Integer(37671), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_4(y:sympy.Rational):
	#((y >= sqrt(435351)/320) | (y > -sqrt(17455)/64)) & ((y >= sqrt(435351)/320) | (y < -sqrt(435351)/320)) & ((y <= sqrt(17455)/64) | (y > -sqrt(17455)/64)) & ((y <= sqrt(17455)/64) | (y < -sqrt(435351)/320))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(1, 320), Pow(Integer(435351), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 64), Pow(Integer(17455), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(1, 320), Pow(Integer(435351), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 320), Pow(Integer(435351), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 64), Pow(Integer(17455), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 64), Pow(Integer(17455), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 64), Pow(Integer(17455), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 320), Pow(Integer(435351), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_5(y:sympy.Rational):
	#((y >= sqrt(6539239)/2560) | (y > -61*sqrt(71)/512)) & ((y >= sqrt(6539239)/2560) | (y < -sqrt(6539239)/2560)) & ((y <= 61*sqrt(71)/512) | (y > -61*sqrt(71)/512)) & ((y <= 61*sqrt(71)/512) | (y < -sqrt(6539239)/2560))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(1, 2560), Pow(Integer(6539239), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(61, 512), Pow(Integer(71), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(1, 2560), Pow(Integer(6539239), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2560), Pow(Integer(6539239), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(61, 512), Pow(Integer(71), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(61, 512), Pow(Integer(71), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(61, 512), Pow(Integer(71), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2560), Pow(Integer(6539239), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_6(y:sympy.Rational):
	#((y >= sqrt(1689879)/640) | (y > -sqrt(67759)/128)) & ((y >= sqrt(1689879)/640) | (y < -sqrt(1689879)/640)) & ((y <= sqrt(67759)/128) | (y > -sqrt(67759)/128)) & ((y <= sqrt(67759)/128) | (y < -sqrt(1689879)/640))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(1, 640), Pow(Integer(1689879), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 128), Pow(Integer(67759), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(1, 640), Pow(Integer(1689879), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 640), Pow(Integer(1689879), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 128), Pow(Integer(67759), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 128), Pow(Integer(67759), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 128), Pow(Integer(67759), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 640), Pow(Integer(1689879), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_7(y:sympy.Rational):
	#((y >= sqrt(1713279)/640) | (y > -sqrt(68695)/128)) & ((y >= sqrt(1713279)/640) | (y < -sqrt(1713279)/640)) & ((y <= sqrt(68695)/128) | (y > -sqrt(68695)/128)) & ((y <= sqrt(68695)/128) | (y < -sqrt(1713279)/640))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(1, 640), Pow(Integer(1713279), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 128), Pow(Integer(68695), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(1, 640), Pow(Integer(1713279), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 640), Pow(Integer(1713279), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 128), Pow(Integer(68695), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 128), Pow(Integer(68695), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 128), Pow(Integer(68695), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 640), Pow(Integer(1713279), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_8(y:sympy.Rational):
	#(y >= -sqrt(31)/64) & (y <= sqrt(31)/64)

	pre_cond = And(GreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 64), Pow(Integer(31), Rational(1, 2)))), LessThan(Symbol('y'), Mul(Rational(1, 64), Pow(Integer(31), Rational(1, 2)))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_9(y:sympy.Rational):
	#((y >= sqrt(41239)/2560) | (y > -sqrt(4271)/512)) & ((y >= sqrt(41239)/2560) | (y < -sqrt(41239)/2560)) & ((y <= sqrt(4271)/512) | (y > -sqrt(4271)/512)) & ((y <= sqrt(4271)/512) | (y < -sqrt(41239)/2560))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(1, 2560), Pow(Integer(41239), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 512), Pow(Integer(4271), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(1, 2560), Pow(Integer(41239), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2560), Pow(Integer(41239), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 512), Pow(Integer(4271), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 512), Pow(Integer(4271), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 512), Pow(Integer(4271), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2560), Pow(Integer(41239), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_10(y:sympy.Rational):
	#((y >= sqrt(1621839)/2560) | (y > -sqrt(67495)/512)) & ((y >= sqrt(1621839)/2560) | (y < -sqrt(1621839)/2560)) & ((y <= sqrt(67495)/512) | (y > -sqrt(67495)/512)) & ((y <= sqrt(67495)/512) | (y < -sqrt(1621839)/2560))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(1, 2560), Pow(Integer(1621839), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 512), Pow(Integer(67495), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(1, 2560), Pow(Integer(1621839), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2560), Pow(Integer(1621839), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 512), Pow(Integer(67495), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 512), Pow(Integer(67495), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 512), Pow(Integer(67495), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2560), Pow(Integer(1621839), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_11(y:sympy.Rational):
	#((y >= 3*sqrt(101399)/1280) | (y > -sqrt(37159)/256)) & ((y >= 3*sqrt(101399)/1280) | (y < -3*sqrt(101399)/1280)) & ((y <= sqrt(37159)/256) | (y > -sqrt(37159)/256)) & ((y <= sqrt(37159)/256) | (y < -3*sqrt(101399)/1280))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(3, 1280), Pow(Integer(101399), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 256), Pow(Integer(37159), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(3, 1280), Pow(Integer(101399), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(3, 1280), Pow(Integer(101399), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 256), Pow(Integer(37159), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 256), Pow(Integer(37159), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 256), Pow(Integer(37159), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(3, 1280), Pow(Integer(101399), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_12(y:sympy.Rational):
	#((y >= sqrt(4982239)/2560) | (y > -sqrt(201911)/512)) & ((y >= sqrt(4982239)/2560) | (y < -sqrt(4982239)/2560)) & ((y <= sqrt(201911)/512) | (y > -sqrt(201911)/512)) & ((y <= sqrt(201911)/512) | (y < -sqrt(4982239)/2560))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(1, 2560), Pow(Integer(4982239), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 512), Pow(Integer(201911), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(1, 2560), Pow(Integer(4982239), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2560), Pow(Integer(4982239), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 512), Pow(Integer(201911), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 512), Pow(Integer(201911), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 512), Pow(Integer(201911), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2560), Pow(Integer(4982239), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_13(y:sympy.Rational):
	#((y >= sqrt(5714439)/2560) | (y > -sqrt(231199)/512)) & ((y >= sqrt(5714439)/2560) | (y < -sqrt(5714439)/2560)) & ((y <= sqrt(231199)/512) | (y > -sqrt(231199)/512)) & ((y <= sqrt(231199)/512) | (y < -sqrt(5714439)/2560))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(1, 2560), Pow(Integer(5714439), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 512), Pow(Integer(231199), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(1, 2560), Pow(Integer(5714439), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2560), Pow(Integer(5714439), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 512), Pow(Integer(231199), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 512), Pow(Integer(231199), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 512), Pow(Integer(231199), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2560), Pow(Integer(5714439), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_14(y:sympy.Rational):
	#((y >= sqrt(1701679)/640) | (y > -31*sqrt(71)/128)) & ((y >= sqrt(1701679)/640) | (y < -sqrt(1701679)/640)) & ((y <= 31*sqrt(71)/128) | (y > -31*sqrt(71)/128)) & ((y <= 31*sqrt(71)/128) | (y < -sqrt(1701679)/640))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(1, 640), Pow(Integer(1701679), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(31, 128), Pow(Integer(71), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(1, 640), Pow(Integer(1701679), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 640), Pow(Integer(1701679), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(31, 128), Pow(Integer(71), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(31, 128), Pow(Integer(71), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(31, 128), Pow(Integer(71), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 640), Pow(Integer(1701679), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_15(y:sympy.Rational):
	#((y >= sqrt(2507439)/2560) | (y > -sqrt(102919)/512)) & ((y >= sqrt(2507439)/2560) | (y < -sqrt(2507439)/2560)) & ((y <= sqrt(102919)/512) | (y > -sqrt(102919)/512)) & ((y <= sqrt(102919)/512) | (y < -sqrt(2507439)/2560))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(1, 2560), Pow(Integer(2507439), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 512), Pow(Integer(102919), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(1, 2560), Pow(Integer(2507439), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2560), Pow(Integer(2507439), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 512), Pow(Integer(102919), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 512), Pow(Integer(102919), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 512), Pow(Integer(102919), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2560), Pow(Integer(2507439), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_16(y:sympy.Rational):
	#((y >= sqrt(3054439)/2560) | (y > -sqrt(124799)/512)) & ((y >= sqrt(3054439)/2560) | (y < -sqrt(3054439)/2560)) & ((y <= sqrt(124799)/512) | (y > -sqrt(124799)/512)) & ((y <= sqrt(124799)/512) | (y < -sqrt(3054439)/2560))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(1, 2560), Pow(Integer(3054439), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 512), Pow(Integer(124799), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(1, 2560), Pow(Integer(3054439), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2560), Pow(Integer(3054439), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 512), Pow(Integer(124799), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 512), Pow(Integer(124799), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 512), Pow(Integer(124799), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2560), Pow(Integer(3054439), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_17(y:sympy.Rational):
	#((y >= sqrt(207879)/640) | (y > -sqrt(8479)/128)) & ((y >= sqrt(207879)/640) | (y < -sqrt(207879)/640)) & ((y <= sqrt(8479)/128) | (y > -sqrt(8479)/128)) & ((y <= sqrt(8479)/128) | (y < -sqrt(207879)/640))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(1, 640), Pow(Integer(207879), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 128), Pow(Integer(8479), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(1, 640), Pow(Integer(207879), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 640), Pow(Integer(207879), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 128), Pow(Integer(8479), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 128), Pow(Integer(8479), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 128), Pow(Integer(8479), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 640), Pow(Integer(207879), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_18(y:sympy.Rational):
	#((y >= sqrt(6128439)/2560) | (y > -sqrt(247759)/512)) & ((y >= sqrt(6128439)/2560) | (y < -sqrt(6128439)/2560)) & ((y <= sqrt(247759)/512) | (y > -sqrt(247759)/512)) & ((y <= sqrt(247759)/512) | (y < -sqrt(6128439)/2560))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(1, 2560), Pow(Integer(6128439), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 512), Pow(Integer(247759), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(1, 2560), Pow(Integer(6128439), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2560), Pow(Integer(6128439), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 512), Pow(Integer(247759), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 512), Pow(Integer(247759), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 512), Pow(Integer(247759), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2560), Pow(Integer(6128439), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_19(y:sympy.Rational):
	#((y >= sqrt(6909991)/1280) | (y > -sqrt(277055)/256)) & ((y >= sqrt(6909991)/1280) | (y < -sqrt(6909991)/1280)) & ((y <= sqrt(277055)/256) | (y > -sqrt(277055)/256)) & ((y <= sqrt(277055)/256) | (y < -sqrt(6909991)/1280))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(1, 1280), Pow(Integer(6909991), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 256), Pow(Integer(277055), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(1, 1280), Pow(Integer(6909991), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1280), Pow(Integer(6909991), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 256), Pow(Integer(277055), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 256), Pow(Integer(277055), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 256), Pow(Integer(277055), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1280), Pow(Integer(6909991), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_20(y:sympy.Rational):
	#((y >= sqrt(423951)/320) | (y > -sqrt(16999)/64)) & ((y >= sqrt(423951)/320) | (y < -sqrt(423951)/320)) & ((y <= sqrt(16999)/64) | (y > -sqrt(16999)/64)) & ((y <= sqrt(16999)/64) | (y < -sqrt(423951)/320))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(1, 320), Pow(Integer(423951), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 64), Pow(Integer(16999), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(1, 320), Pow(Integer(423951), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 320), Pow(Integer(423951), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 64), Pow(Integer(16999), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 64), Pow(Integer(16999), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 64), Pow(Integer(16999), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 320), Pow(Integer(423951), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_21(y:sympy.Rational):
	#((y >= sqrt(804391)/1280) | (y > -sqrt(32831)/256)) & ((y >= sqrt(804391)/1280) | (y < -sqrt(804391)/1280)) & ((y <= sqrt(32831)/256) | (y > -sqrt(32831)/256)) & ((y <= sqrt(32831)/256) | (y < -sqrt(804391)/1280))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(1, 1280), Pow(Integer(804391), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 256), Pow(Integer(32831), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(1, 1280), Pow(Integer(804391), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1280), Pow(Integer(804391), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 256), Pow(Integer(32831), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 256), Pow(Integer(32831), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 256), Pow(Integer(32831), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1280), Pow(Integer(804391), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_22(y:sympy.Rational):
	#((y >= sqrt(5921839)/2560) | (y > -sqrt(239495)/512)) & ((y >= sqrt(5921839)/2560) | (y < -sqrt(5921839)/2560)) & ((y <= sqrt(239495)/512) | (y > -sqrt(239495)/512)) & ((y <= sqrt(239495)/512) | (y < -sqrt(5921839)/2560))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(1, 2560), Pow(Integer(5921839), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 512), Pow(Integer(239495), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(1, 2560), Pow(Integer(5921839), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2560), Pow(Integer(5921839), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 512), Pow(Integer(239495), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 512), Pow(Integer(239495), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 512), Pow(Integer(239495), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2560), Pow(Integer(5921839), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_23(y:sympy.Rational):
	#((y >= sqrt(695391)/1280) | (y > -sqrt(28471)/256)) & ((y >= sqrt(695391)/1280) | (y < -sqrt(695391)/1280)) & ((y <= sqrt(28471)/256) | (y > -sqrt(28471)/256)) & ((y <= sqrt(28471)/256) | (y < -sqrt(695391)/1280))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(1, 1280), Pow(Integer(695391), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 256), Pow(Integer(28471), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(1, 1280), Pow(Integer(695391), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1280), Pow(Integer(695391), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 256), Pow(Integer(28471), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 256), Pow(Integer(28471), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 256), Pow(Integer(28471), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1280), Pow(Integer(695391), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_24(y:sympy.Rational):
	#((y >= sqrt(6932391)/1280) | (y > -sqrt(277951)/256)) & ((y >= sqrt(6932391)/1280) | (y < -sqrt(6932391)/1280)) & ((y <= sqrt(277951)/256) | (y > -sqrt(277951)/256)) & ((y <= sqrt(277951)/256) | (y < -sqrt(6932391)/1280))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(1, 1280), Pow(Integer(6932391), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 256), Pow(Integer(277951), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(1, 1280), Pow(Integer(6932391), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1280), Pow(Integer(6932391), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 256), Pow(Integer(277951), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 256), Pow(Integer(277951), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 256), Pow(Integer(277951), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1280), Pow(Integer(6932391), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_25(y:sympy.Rational):
	#((y >= sqrt(6771391)/1280) | (y > -sqrt(271511)/256)) & ((y >= sqrt(6771391)/1280) | (y < -sqrt(6771391)/1280)) & ((y <= sqrt(271511)/256) | (y > -sqrt(271511)/256)) & ((y <= sqrt(271511)/256) | (y < -sqrt(6771391)/1280))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(1, 1280), Pow(Integer(6771391), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 256), Pow(Integer(271511), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(1, 1280), Pow(Integer(6771391), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1280), Pow(Integer(6771391), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 256), Pow(Integer(271511), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 256), Pow(Integer(271511), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 256), Pow(Integer(271511), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1280), Pow(Integer(6771391), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_26(y:sympy.Rational):
	#((y >= 3*sqrt(4639)/320) | (y > -sqrt(1711)/64)) & ((y >= 3*sqrt(4639)/320) | (y < -3*sqrt(4639)/320)) & ((y <= sqrt(1711)/64) | (y > -sqrt(1711)/64)) & ((y <= sqrt(1711)/64) | (y < -3*sqrt(4639)/320))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(3, 320), Pow(Integer(4639), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 64), Pow(Integer(1711), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(3, 320), Pow(Integer(4639), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(3, 320), Pow(Integer(4639), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 64), Pow(Integer(1711), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 64), Pow(Integer(1711), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 64), Pow(Integer(1711), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(3, 320), Pow(Integer(4639), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_27(y:sympy.Rational):
	#((y >= 3*sqrt(669471)/2560) | (y > -sqrt(243631)/512)) & ((y >= 3*sqrt(669471)/2560) | (y < -3*sqrt(669471)/2560)) & ((y <= sqrt(243631)/512) | (y > -sqrt(243631)/512)) & ((y <= sqrt(243631)/512) | (y < -3*sqrt(669471)/2560))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(3, 2560), Pow(Integer(669471), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 512), Pow(Integer(243631), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(3, 2560), Pow(Integer(669471), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(3, 2560), Pow(Integer(669471), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 512), Pow(Integer(243631), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 512), Pow(Integer(243631), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 512), Pow(Integer(243631), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(3, 2560), Pow(Integer(669471), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_28(y:sympy.Rational):
	#((y >= 3*sqrt(754999)/1280) | (y > -sqrt(272455)/256)) & ((y >= 3*sqrt(754999)/1280) | (y < -3*sqrt(754999)/1280)) & ((y <= sqrt(272455)/256) | (y > -sqrt(272455)/256)) & ((y <= sqrt(272455)/256) | (y < -3*sqrt(754999)/1280))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(3, 1280), Pow(Integer(754999), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 256), Pow(Integer(272455), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(3, 1280), Pow(Integer(754999), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(3, 1280), Pow(Integer(754999), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 256), Pow(Integer(272455), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 256), Pow(Integer(272455), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 256), Pow(Integer(272455), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(3, 1280), Pow(Integer(754999), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_29(y:sympy.Rational):
	#((y >= sqrt(3271839)/2560) | (y > -sqrt(133495)/512)) & ((y >= sqrt(3271839)/2560) | (y < -sqrt(3271839)/2560)) & ((y <= sqrt(133495)/512) | (y > -sqrt(133495)/512)) & ((y <= sqrt(133495)/512) | (y < -sqrt(3271839)/2560))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(1, 2560), Pow(Integer(3271839), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 512), Pow(Integer(133495), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(1, 2560), Pow(Integer(3271839), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2560), Pow(Integer(3271839), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 512), Pow(Integer(133495), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 512), Pow(Integer(133495), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 512), Pow(Integer(133495), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2560), Pow(Integer(3271839), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_30(y:sympy.Rational):
	#((y >= sqrt(106719)/160) | (y > -sqrt(4279)/32)) & ((y >= sqrt(106719)/160) | (y < -sqrt(106719)/160)) & ((y <= sqrt(4279)/32) | (y > -sqrt(4279)/32)) & ((y <= sqrt(4279)/32) | (y < -sqrt(106719)/160))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(1, 160), Pow(Integer(106719), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 32), Pow(Integer(4279), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(1, 160), Pow(Integer(106719), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 160), Pow(Integer(106719), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 32), Pow(Integer(4279), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 32), Pow(Integer(4279), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 32), Pow(Integer(4279), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 160), Pow(Integer(106719), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_31(y:sympy.Rational):
	#((y >= 3*sqrt(751)/40) | (y > -sqrt(271)/8)) & ((y >= 3*sqrt(751)/40) | (y < -3*sqrt(751)/40)) & ((y <= sqrt(271)/8) | (y > -sqrt(271)/8)) & ((y <= sqrt(271)/8) | (y < -3*sqrt(751)/40))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(3, 40), Pow(Integer(751), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 8), Pow(Integer(271), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(3, 40), Pow(Integer(751), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(3, 40), Pow(Integer(751), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 8), Pow(Integer(271), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 8), Pow(Integer(271), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 8), Pow(Integer(271), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(3, 40), Pow(Integer(751), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_32(y:sympy.Rational):
	#((y >= 3*sqrt(757599)/1280) | (y > -sqrt(273391)/256)) & ((y >= 3*sqrt(757599)/1280) | (y < -3*sqrt(757599)/1280)) & ((y <= sqrt(273391)/256) | (y > -sqrt(273391)/256)) & ((y <= sqrt(273391)/256) | (y < -3*sqrt(757599)/1280))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(3, 1280), Pow(Integer(757599), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 256), Pow(Integer(273391), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(3, 1280), Pow(Integer(757599), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(3, 1280), Pow(Integer(757599), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 256), Pow(Integer(273391), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 256), Pow(Integer(273391), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 256), Pow(Integer(273391), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(3, 1280), Pow(Integer(757599), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_33(y:sympy.Rational):
	#((y >= sqrt(6841591)/1280) | (y > -sqrt(274319)/256)) & ((y >= sqrt(6841591)/1280) | (y < -sqrt(6841591)/1280)) & ((y <= sqrt(274319)/256) | (y > -sqrt(274319)/256)) & ((y <= sqrt(274319)/256) | (y < -sqrt(6841591)/1280))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(1, 1280), Pow(Integer(6841591), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 256), Pow(Integer(274319), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(1, 1280), Pow(Integer(6841591), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1280), Pow(Integer(6841591), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 256), Pow(Integer(274319), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 256), Pow(Integer(274319), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 256), Pow(Integer(274319), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1280), Pow(Integer(6841591), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_34(y:sympy.Rational):
	#((y >= sqrt(112119)/160) | (y > -sqrt(4495)/32)) & ((y >= sqrt(112119)/160) | (y < -sqrt(112119)/160)) & ((y <= sqrt(4495)/32) | (y > -sqrt(4495)/32)) & ((y <= sqrt(4495)/32) | (y < -sqrt(112119)/160))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(1, 160), Pow(Integer(112119), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 32), Pow(Integer(4495), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(1, 160), Pow(Integer(112119), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 160), Pow(Integer(112119), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 32), Pow(Integer(4495), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 32), Pow(Integer(4495), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 32), Pow(Integer(4495), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 160), Pow(Integer(112119), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_35(y:sympy.Rational):
	#((y >= sqrt(1493391)/1280) | (y > -sqrt(60391)/256)) & ((y >= sqrt(1493391)/1280) | (y < -sqrt(1493391)/1280)) & ((y <= sqrt(60391)/256) | (y > -sqrt(60391)/256)) & ((y <= sqrt(60391)/256) | (y < -sqrt(1493391)/1280))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(1, 1280), Pow(Integer(1493391), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 256), Pow(Integer(60391), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(1, 1280), Pow(Integer(1493391), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1280), Pow(Integer(1493391), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 256), Pow(Integer(60391), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 256), Pow(Integer(60391), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 256), Pow(Integer(60391), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1280), Pow(Integer(1493391), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_36(y:sympy.Rational):
	#((y >= sqrt(1735879)/640) | (y > -sqrt(69599)/128)) & ((y >= sqrt(1735879)/640) | (y < -sqrt(1735879)/640)) & ((y <= sqrt(69599)/128) | (y > -sqrt(69599)/128)) & ((y <= sqrt(69599)/128) | (y < -sqrt(1735879)/640))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(1, 640), Pow(Integer(1735879), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 128), Pow(Integer(69599), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(1, 640), Pow(Integer(1735879), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 640), Pow(Integer(1735879), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 128), Pow(Integer(69599), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 128), Pow(Integer(69599), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 128), Pow(Integer(69599), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 640), Pow(Integer(1735879), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_37(y:sympy.Rational):
	#((y >= sqrt(94951)/320) | (y > -sqrt(3839)/64)) & ((y >= sqrt(94951)/320) | (y < -sqrt(94951)/320)) & ((y <= sqrt(3839)/64) | (y > -sqrt(3839)/64)) & ((y <= sqrt(3839)/64) | (y < -sqrt(94951)/320))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(1, 320), Pow(Integer(94951), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 64), Pow(Integer(3839), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(1, 320), Pow(Integer(94951), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 320), Pow(Integer(94951), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 64), Pow(Integer(3839), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 64), Pow(Integer(3839), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 64), Pow(Integer(3839), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 320), Pow(Integer(94951), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_38(y:sympy.Rational):
	#((y >= sqrt(6954591)/1280) | (y > -sqrt(278839)/256)) & ((y >= sqrt(6954591)/1280) | (y < -sqrt(6954591)/1280)) & ((y <= sqrt(278839)/256) | (y > -sqrt(278839)/256)) & ((y <= sqrt(278839)/256) | (y < -sqrt(6954591)/1280))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(1, 1280), Pow(Integer(6954591), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 256), Pow(Integer(278839), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(1, 1280), Pow(Integer(6954591), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1280), Pow(Integer(6954591), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 256), Pow(Integer(278839), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 256), Pow(Integer(278839), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 256), Pow(Integer(278839), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1280), Pow(Integer(6954591), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_39(y:sympy.Rational):
	#((y >= 29*sqrt(511)/320) | (y > -sqrt(17231)/64)) & ((y >= 29*sqrt(511)/320) | (y < -29*sqrt(511)/320)) & ((y <= sqrt(17231)/64) | (y > -sqrt(17231)/64)) & ((y <= sqrt(17231)/64) | (y < -29*sqrt(511)/320))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(29, 320), Pow(Integer(511), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 64), Pow(Integer(17231), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(29, 320), Pow(Integer(511), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(29, 320), Pow(Integer(511), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 64), Pow(Integer(17231), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 64), Pow(Integer(17231), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 64), Pow(Integer(17231), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(29, 320), Pow(Integer(511), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_40(y:sympy.Rational):
	#((y >= sqrt(6864591)/1280) | (y > -sqrt(275239)/256)) & ((y >= sqrt(6864591)/1280) | (y < -sqrt(6864591)/1280)) & ((y <= sqrt(275239)/256) | (y > -sqrt(275239)/256)) & ((y <= sqrt(275239)/256) | (y < -sqrt(6864591)/1280))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(1, 1280), Pow(Integer(6864591), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 256), Pow(Integer(275239), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(1, 1280), Pow(Integer(6864591), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1280), Pow(Integer(6864591), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 256), Pow(Integer(275239), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 256), Pow(Integer(275239), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 256), Pow(Integer(275239), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1280), Pow(Integer(6864591), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_41(y:sympy.Rational):
	#((y >= sqrt(1768279)/640) | (y > -sqrt(70895)/128)) & ((y >= sqrt(1768279)/640) | (y < -sqrt(1768279)/640)) & ((y <= sqrt(70895)/128) | (y > -sqrt(70895)/128)) & ((y <= sqrt(70895)/128) | (y < -sqrt(1768279)/640))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(1, 640), Pow(Integer(1768279), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 128), Pow(Integer(70895), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(1, 640), Pow(Integer(1768279), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 640), Pow(Integer(1768279), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 128), Pow(Integer(70895), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 128), Pow(Integer(70895), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 128), Pow(Integer(70895), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 640), Pow(Integer(1768279), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_42(y:sympy.Rational):
	#((y >= 9*sqrt(21959)/640) | (y > -sqrt(71311)/128)) & ((y >= 9*sqrt(21959)/640) | (y < -9*sqrt(21959)/640)) & ((y <= sqrt(71311)/128) | (y > -sqrt(71311)/128)) & ((y <= sqrt(71311)/128) | (y < -9*sqrt(21959)/640))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(9, 640), Pow(Integer(21959), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 128), Pow(Integer(71311), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(9, 640), Pow(Integer(21959), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(9, 640), Pow(Integer(21959), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 128), Pow(Integer(71311), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 128), Pow(Integer(71311), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 128), Pow(Integer(71311), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(9, 640), Pow(Integer(21959), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_43(y:sympy.Rational):
	#((y >= 3*sqrt(646471)/2560) | (y > -sqrt(235351)/512)) & ((y >= 3*sqrt(646471)/2560) | (y < -3*sqrt(646471)/2560)) & ((y <= sqrt(235351)/512) | (y > -sqrt(235351)/512)) & ((y <= sqrt(235351)/512) | (y < -3*sqrt(646471)/2560))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(3, 2560), Pow(Integer(646471), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 512), Pow(Integer(235351), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(3, 2560), Pow(Integer(646471), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(3, 2560), Pow(Integer(646471), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 512), Pow(Integer(235351), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 512), Pow(Integer(235351), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 512), Pow(Integer(235351), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(3, 2560), Pow(Integer(646471), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_44(y:sympy.Rational):
	#((y >= 3*sqrt(191631)/640) | (y > -sqrt(69151)/128)) & ((y >= 3*sqrt(191631)/640) | (y < -3*sqrt(191631)/640)) & ((y <= sqrt(69151)/128) | (y > -sqrt(69151)/128)) & ((y <= sqrt(69151)/128) | (y < -3*sqrt(191631)/640))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(3, 640), Pow(Integer(191631), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 128), Pow(Integer(69151), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(3, 640), Pow(Integer(191631), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(3, 640), Pow(Integer(191631), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 128), Pow(Integer(69151), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 128), Pow(Integer(69151), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 128), Pow(Integer(69151), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(3, 640), Pow(Integer(191631), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_45(y:sympy.Rational):
	#((y >= 3*sqrt(3079)/80) | (y > -sqrt(1111)/16)) & ((y >= 3*sqrt(3079)/80) | (y < -3*sqrt(3079)/80)) & ((y <= sqrt(1111)/16) | (y > -sqrt(1111)/16)) & ((y <= sqrt(1111)/16) | (y < -3*sqrt(3079)/80))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(3, 80), Pow(Integer(3079), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 16), Pow(Integer(1111), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(3, 80), Pow(Integer(3079), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(3, 80), Pow(Integer(3079), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 16), Pow(Integer(1111), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 16), Pow(Integer(1111), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 16), Pow(Integer(1111), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(3, 80), Pow(Integer(3079), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_46(y:sympy.Rational):
	#((y >= sqrt(366879)/640) | (y > -sqrt(14839)/128)) & ((y >= sqrt(366879)/640) | (y < -sqrt(366879)/640)) & ((y <= sqrt(14839)/128) | (y > -sqrt(14839)/128)) & ((y <= sqrt(14839)/128) | (y < -sqrt(366879)/640))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(1, 640), Pow(Integer(366879), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 128), Pow(Integer(14839), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(1, 640), Pow(Integer(366879), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 640), Pow(Integer(366879), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 128), Pow(Integer(14839), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 128), Pow(Integer(14839), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 128), Pow(Integer(14839), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 640), Pow(Integer(366879), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_47(y:sympy.Rational):
	#((y >= 7*sqrt(140559)/1280) | (y > -sqrt(276151)/256)) & ((y >= 7*sqrt(140559)/1280) | (y < -7*sqrt(140559)/1280)) & ((y <= sqrt(276151)/256) | (y > -sqrt(276151)/256)) & ((y <= sqrt(276151)/256) | (y < -7*sqrt(140559)/1280))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(7, 1280), Pow(Integer(140559), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 256), Pow(Integer(276151), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(7, 1280), Pow(Integer(140559), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(7, 1280), Pow(Integer(140559), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 256), Pow(Integer(276151), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 256), Pow(Integer(276151), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 256), Pow(Integer(276151), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(7, 1280), Pow(Integer(140559), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_48(y:sympy.Rational):
	#((y >= sqrt(6650391)/1280) | (y > -sqrt(266671)/256)) & ((y >= sqrt(6650391)/1280) | (y < -sqrt(6650391)/1280)) & ((y <= sqrt(266671)/256) | (y > -sqrt(266671)/256)) & ((y <= sqrt(266671)/256) | (y < -sqrt(6650391)/1280))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(1, 1280), Pow(Integer(6650391), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 256), Pow(Integer(266671), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(1, 1280), Pow(Integer(6650391), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1280), Pow(Integer(6650391), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 256), Pow(Integer(266671), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 256), Pow(Integer(266671), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 256), Pow(Integer(266671), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1280), Pow(Integer(6650391), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_49(y:sympy.Rational):
	#((y >= sqrt(6699391)/1280) | (y > -sqrt(268631)/256)) & ((y >= sqrt(6699391)/1280) | (y < -sqrt(6699391)/1280)) & ((y <= sqrt(268631)/256) | (y > -sqrt(268631)/256)) & ((y <= sqrt(268631)/256) | (y < -sqrt(6699391)/1280))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(1, 1280), Pow(Integer(6699391), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 256), Pow(Integer(268631), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(1, 1280), Pow(Integer(6699391), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1280), Pow(Integer(6699391), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 256), Pow(Integer(268631), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 256), Pow(Integer(268631), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 256), Pow(Integer(268631), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1280), Pow(Integer(6699391), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_50(y:sympy.Rational):
	#((y >= 21*sqrt(6679)/2560) | (y > -sqrt(120439)/512)) & ((y >= 21*sqrt(6679)/2560) | (y < -21*sqrt(6679)/2560)) & ((y <= sqrt(120439)/512) | (y > -sqrt(120439)/512)) & ((y <= sqrt(120439)/512) | (y < -21*sqrt(6679)/2560))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(21, 2560), Pow(Integer(6679), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 512), Pow(Integer(120439), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(21, 2560), Pow(Integer(6679), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(21, 2560), Pow(Integer(6679), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 512), Pow(Integer(120439), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 512), Pow(Integer(120439), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 512), Pow(Integer(120439), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(21, 2560), Pow(Integer(6679), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_51(y:sympy.Rational):
	#((y >= sqrt(1441591)/1280) | (y > -sqrt(58319)/256)) & ((y >= sqrt(1441591)/1280) | (y < -sqrt(1441591)/1280)) & ((y <= sqrt(58319)/256) | (y > -sqrt(58319)/256)) & ((y <= sqrt(58319)/256) | (y < -sqrt(1441591)/1280))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(1, 1280), Pow(Integer(1441591), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 256), Pow(Integer(58319), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(1, 1280), Pow(Integer(1441591), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1280), Pow(Integer(1441591), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 256), Pow(Integer(58319), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 256), Pow(Integer(58319), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 256), Pow(Integer(58319), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1280), Pow(Integer(1441591), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_52(y:sympy.Rational):
	#((y >= sqrt(759)/40) | (y > -sqrt(31)/8)) & ((y >= sqrt(759)/40) | (y < -sqrt(759)/40)) & ((y <= sqrt(31)/8) | (y > -sqrt(31)/8)) & ((y <= sqrt(31)/8) | (y < -sqrt(759)/40))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(1, 40), Pow(Integer(759), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 8), Pow(Integer(31), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(1, 40), Pow(Integer(759), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 40), Pow(Integer(759), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 8), Pow(Integer(31), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 8), Pow(Integer(31), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 8), Pow(Integer(31), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 40), Pow(Integer(759), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_53(y:sympy.Rational):
	#((y >= sqrt(749991)/1280) | (y > -sqrt(30655)/256)) & ((y >= sqrt(749991)/1280) | (y < -sqrt(749991)/1280)) & ((y <= sqrt(30655)/256) | (y > -sqrt(30655)/256)) & ((y <= sqrt(30655)/256) | (y < -sqrt(749991)/1280))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(1, 1280), Pow(Integer(749991), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 256), Pow(Integer(30655), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(1, 1280), Pow(Integer(749991), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1280), Pow(Integer(749991), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 256), Pow(Integer(30655), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 256), Pow(Integer(30655), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 256), Pow(Integer(30655), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1280), Pow(Integer(749991), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_54(y:sympy.Rational):
	#((y >= 3*sqrt(351471)/2560) | (y > -sqrt(129151)/512)) & ((y >= 3*sqrt(351471)/2560) | (y < -3*sqrt(351471)/2560)) & ((y <= sqrt(129151)/512) | (y > -sqrt(129151)/512)) & ((y <= sqrt(129151)/512) | (y < -3*sqrt(351471)/2560))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(3, 2560), Pow(Integer(351471), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 512), Pow(Integer(129151), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(3, 2560), Pow(Integer(351471), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(3, 2560), Pow(Integer(351471), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 512), Pow(Integer(129151), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 512), Pow(Integer(129151), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 512), Pow(Integer(129151), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(3, 2560), Pow(Integer(351471), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_55(y:sympy.Rational):
	#((y >= sqrt(7104391)/1280) | (y > -sqrt(284831)/256)) & ((y >= sqrt(7104391)/1280) | (y < -sqrt(7104391)/1280)) & ((y <= sqrt(284831)/256) | (y > -sqrt(284831)/256)) & ((y <= sqrt(284831)/256) | (y < -sqrt(7104391)/1280))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(1, 1280), Pow(Integer(7104391), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 256), Pow(Integer(284831), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(1, 1280), Pow(Integer(7104391), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1280), Pow(Integer(7104391), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 256), Pow(Integer(284831), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 256), Pow(Integer(284831), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 256), Pow(Integer(284831), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1280), Pow(Integer(7104391), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_56(y:sympy.Rational):
	#((y >= sqrt(6674991)/1280) | (y > -sqrt(267655)/256)) & ((y >= sqrt(6674991)/1280) | (y < -sqrt(6674991)/1280)) & ((y <= sqrt(267655)/256) | (y > -sqrt(267655)/256)) & ((y <= sqrt(267655)/256) | (y < -sqrt(6674991)/1280))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(1, 1280), Pow(Integer(6674991), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 256), Pow(Integer(267655), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(1, 1280), Pow(Integer(6674991), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1280), Pow(Integer(6674991), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 256), Pow(Integer(267655), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 256), Pow(Integer(267655), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 256), Pow(Integer(267655), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1280), Pow(Integer(6674991), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_57(y:sympy.Rational):
	#((y >= sqrt(3488439)/2560) | (y > -sqrt(142159)/512)) & ((y >= sqrt(3488439)/2560) | (y < -sqrt(3488439)/2560)) & ((y <= sqrt(142159)/512) | (y > -sqrt(142159)/512)) & ((y <= sqrt(142159)/512) | (y < -sqrt(3488439)/2560))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(1, 2560), Pow(Integer(3488439), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 512), Pow(Integer(142159), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(1, 2560), Pow(Integer(3488439), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2560), Pow(Integer(3488439), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 512), Pow(Integer(142159), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 512), Pow(Integer(142159), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 512), Pow(Integer(142159), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2560), Pow(Integer(3488439), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_58(y:sympy.Rational):
	#((y >= 9*sqrt(16511)/1280) | (y > -sqrt(54151)/256)) & ((y >= 9*sqrt(16511)/1280) | (y < -9*sqrt(16511)/1280)) & ((y <= sqrt(54151)/256) | (y > -sqrt(54151)/256)) & ((y <= sqrt(54151)/256) | (y < -9*sqrt(16511)/1280))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(9, 1280), Pow(Integer(16511), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 256), Pow(Integer(54151), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(9, 1280), Pow(Integer(16511), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(9, 1280), Pow(Integer(16511), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 256), Pow(Integer(54151), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 256), Pow(Integer(54151), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 256), Pow(Integer(54151), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(9, 1280), Pow(Integer(16511), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_59(y:sympy.Rational):
	#((y >= sqrt(7083591)/1280) | (y > -sqrt(283999)/256)) & ((y >= sqrt(7083591)/1280) | (y < -sqrt(7083591)/1280)) & ((y <= sqrt(283999)/256) | (y > -sqrt(283999)/256)) & ((y <= sqrt(283999)/256) | (y < -sqrt(7083591)/1280))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(1, 1280), Pow(Integer(7083591), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 256), Pow(Integer(283999), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(1, 1280), Pow(Integer(7083591), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1280), Pow(Integer(7083591), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 256), Pow(Integer(283999), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 256), Pow(Integer(283999), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 256), Pow(Integer(283999), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1280), Pow(Integer(7083591), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_60(y:sympy.Rational):
	#((y >= 21*sqrt(3151)/1280) | (y > -sqrt(56239)/256)) & ((y >= 21*sqrt(3151)/1280) | (y < -21*sqrt(3151)/1280)) & ((y <= sqrt(56239)/256) | (y > -sqrt(56239)/256)) & ((y <= sqrt(56239)/256) | (y < -21*sqrt(3151)/1280))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(21, 1280), Pow(Integer(3151), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 256), Pow(Integer(56239), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(21, 1280), Pow(Integer(3151), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(21, 1280), Pow(Integer(3151), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 256), Pow(Integer(56239), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 256), Pow(Integer(56239), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 256), Pow(Integer(56239), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(21, 1280), Pow(Integer(3151), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_61(y:sympy.Rational):
	#((y >= sqrt(640591)/1280) | (y > -sqrt(26279)/256)) & ((y >= sqrt(640591)/1280) | (y < -sqrt(640591)/1280)) & ((y <= sqrt(26279)/256) | (y > -sqrt(26279)/256)) & ((y <= sqrt(26279)/256) | (y < -sqrt(640591)/1280))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(1, 1280), Pow(Integer(640591), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 256), Pow(Integer(26279), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(1, 1280), Pow(Integer(640591), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1280), Pow(Integer(640591), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 256), Pow(Integer(26279), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 256), Pow(Integer(26279), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 256), Pow(Integer(26279), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1280), Pow(Integer(640591), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_62(y:sympy.Rational):
	#((y >= sqrt(340879)/640) | (y > -sqrt(13799)/128)) & ((y >= sqrt(340879)/640) | (y < -sqrt(340879)/640)) & ((y <= sqrt(13799)/128) | (y > -sqrt(13799)/128)) & ((y <= sqrt(13799)/128) | (y < -sqrt(340879)/640))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(1, 640), Pow(Integer(340879), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 128), Pow(Integer(13799), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(1, 640), Pow(Integer(340879), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 640), Pow(Integer(340879), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 128), Pow(Integer(13799), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 128), Pow(Integer(13799), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 128), Pow(Integer(13799), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 640), Pow(Integer(340879), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_63(y:sympy.Rational):
	#((y >= sqrt(1788879)/640) | (y > -sqrt(71719)/128)) & ((y >= sqrt(1788879)/640) | (y < -sqrt(1788879)/640)) & ((y <= sqrt(71719)/128) | (y > -sqrt(71719)/128)) & ((y <= sqrt(71719)/128) | (y < -sqrt(1788879)/640))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(1, 640), Pow(Integer(1788879), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 128), Pow(Integer(71719), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(1, 640), Pow(Integer(1788879), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 640), Pow(Integer(1788879), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 128), Pow(Integer(71719), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 128), Pow(Integer(71719), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 128), Pow(Integer(71719), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 640), Pow(Integer(1788879), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_64(y:sympy.Rational):
	#((y >= sqrt(1665679)/640) | (y > -sqrt(66791)/128)) & ((y >= sqrt(1665679)/640) | (y < -sqrt(1665679)/640)) & ((y <= sqrt(66791)/128) | (y > -sqrt(66791)/128)) & ((y <= sqrt(66791)/128) | (y < -sqrt(1665679)/640))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(1, 640), Pow(Integer(1665679), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 128), Pow(Integer(66791), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(1, 640), Pow(Integer(1665679), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 640), Pow(Integer(1665679), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 128), Pow(Integer(66791), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 128), Pow(Integer(66791), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 128), Pow(Integer(66791), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 640), Pow(Integer(1665679), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_65(y:sympy.Rational):
	#((y >= sqrt(7165591)/1280) | (y > -sqrt(287279)/256)) & ((y >= sqrt(7165591)/1280) | (y < -sqrt(7165591)/1280)) & ((y <= sqrt(287279)/256) | (y > -sqrt(287279)/256)) & ((y <= sqrt(287279)/256) | (y < -sqrt(7165591)/1280))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(1, 1280), Pow(Integer(7165591), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 256), Pow(Integer(287279), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(1, 1280), Pow(Integer(7165591), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1280), Pow(Integer(7165591), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 256), Pow(Integer(287279), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 256), Pow(Integer(287279), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 256), Pow(Integer(287279), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1280), Pow(Integer(7165591), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_66(y:sympy.Rational):
	#((y >= sqrt(5506239)/2560) | (y > -sqrt(222871)/512)) & ((y >= sqrt(5506239)/2560) | (y < -sqrt(5506239)/2560)) & ((y <= sqrt(222871)/512) | (y > -sqrt(222871)/512)) & ((y <= sqrt(222871)/512) | (y < -sqrt(5506239)/2560))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(1, 2560), Pow(Integer(5506239), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 512), Pow(Integer(222871), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(1, 2560), Pow(Integer(5506239), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2560), Pow(Integer(5506239), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 512), Pow(Integer(222871), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 512), Pow(Integer(222871), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 512), Pow(Integer(222871), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2560), Pow(Integer(5506239), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_67(y:sympy.Rational):
	#((y >= 3*sqrt(46439)/320) | (y > -sqrt(16759)/64)) & ((y >= 3*sqrt(46439)/320) | (y < -3*sqrt(46439)/320)) & ((y <= sqrt(16759)/64) | (y > -sqrt(16759)/64)) & ((y <= sqrt(16759)/64) | (y < -3*sqrt(46439)/320))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(3, 320), Pow(Integer(46439), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 64), Pow(Integer(16759), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(3, 320), Pow(Integer(46439), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(3, 320), Pow(Integer(46439), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 64), Pow(Integer(16759), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 64), Pow(Integer(16759), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 64), Pow(Integer(16759), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(3, 320), Pow(Integer(46439), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_68(y:sympy.Rational):
	#((y >= sqrt(6723591)/1280) | (y > -sqrt(269599)/256)) & ((y >= sqrt(6723591)/1280) | (y < -sqrt(6723591)/1280)) & ((y <= sqrt(269599)/256) | (y > -sqrt(269599)/256)) & ((y <= sqrt(269599)/256) | (y < -sqrt(6723591)/1280))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(1, 1280), Pow(Integer(6723591), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 256), Pow(Integer(269599), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(1, 1280), Pow(Integer(6723591), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1280), Pow(Integer(6723591), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 256), Pow(Integer(269599), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 256), Pow(Integer(269599), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 256), Pow(Integer(269599), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1280), Pow(Integer(6723591), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_69(y:sympy.Rational):
	#((y >= sqrt(1284991)/1280) | (y > -sqrt(52055)/256)) & ((y >= sqrt(1284991)/1280) | (y < -sqrt(1284991)/1280)) & ((y <= sqrt(52055)/256) | (y > -sqrt(52055)/256)) & ((y <= sqrt(52055)/256) | (y < -sqrt(1284991)/1280))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(1, 1280), Pow(Integer(1284991), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 256), Pow(Integer(52055), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(1, 1280), Pow(Integer(1284991), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1280), Pow(Integer(1284991), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 256), Pow(Integer(52055), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 256), Pow(Integer(52055), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 256), Pow(Integer(52055), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1280), Pow(Integer(1284991), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_70(y:sympy.Rational):
	#((y >= sqrt(26311)/80) | (y > -sqrt(1055)/16)) & ((y >= sqrt(26311)/80) | (y < -sqrt(26311)/80)) & ((y <= sqrt(1055)/16) | (y > -sqrt(1055)/16)) & ((y <= sqrt(1055)/16) | (y < -sqrt(26311)/80))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(1, 80), Pow(Integer(26311), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 16), Pow(Integer(1055), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(1, 80), Pow(Integer(26311), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 80), Pow(Integer(26311), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 16), Pow(Integer(1055), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 16), Pow(Integer(1055), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 16), Pow(Integer(1055), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 80), Pow(Integer(26311), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_71(y:sympy.Rational):
	#((y >= sqrt(3596439)/2560) | (y > -sqrt(146479)/512)) & ((y >= sqrt(3596439)/2560) | (y < -sqrt(3596439)/2560)) & ((y <= sqrt(146479)/512) | (y > -sqrt(146479)/512)) & ((y <= sqrt(146479)/512) | (y < -sqrt(3596439)/2560))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(1, 2560), Pow(Integer(3596439), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 512), Pow(Integer(146479), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(1, 2560), Pow(Integer(3596439), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2560), Pow(Integer(3596439), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 512), Pow(Integer(146479), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 512), Pow(Integer(146479), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 512), Pow(Integer(146479), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2560), Pow(Integer(3596439), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_72(y:sympy.Rational):
	#((y >= sqrt(22119)/160) | (y > -sqrt(895)/32)) & ((y >= sqrt(22119)/160) | (y < -sqrt(22119)/160)) & ((y <= sqrt(895)/32) | (y > -sqrt(895)/32)) & ((y <= sqrt(895)/32) | (y < -sqrt(22119)/160))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(1, 160), Pow(Integer(22119), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 32), Pow(Integer(895), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(1, 160), Pow(Integer(22119), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 160), Pow(Integer(22119), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 32), Pow(Integer(895), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 32), Pow(Integer(895), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 32), Pow(Integer(895), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 160), Pow(Integer(22119), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_73(y:sympy.Rational):
	#((y >= sqrt(6747591)/1280) | (y > -sqrt(270559)/256)) & ((y >= sqrt(6747591)/1280) | (y < -sqrt(6747591)/1280)) & ((y <= sqrt(270559)/256) | (y > -sqrt(270559)/256)) & ((y <= sqrt(270559)/256) | (y < -sqrt(6747591)/1280))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(1, 1280), Pow(Integer(6747591), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 256), Pow(Integer(270559), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(1, 1280), Pow(Integer(6747591), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1280), Pow(Integer(6747591), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 256), Pow(Integer(270559), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 256), Pow(Integer(270559), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 256), Pow(Integer(270559), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1280), Pow(Integer(6747591), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_74(y:sympy.Rational):
	#((y >= 3*sqrt(565271)/2560) | (y > -sqrt(206119)/512)) & ((y >= 3*sqrt(565271)/2560) | (y < -3*sqrt(565271)/2560)) & ((y <= sqrt(206119)/512) | (y > -sqrt(206119)/512)) & ((y <= sqrt(206119)/512) | (y < -3*sqrt(565271)/2560))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(3, 2560), Pow(Integer(565271), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 512), Pow(Integer(206119), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(3, 2560), Pow(Integer(565271), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(3, 2560), Pow(Integer(565271), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 512), Pow(Integer(206119), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 512), Pow(Integer(206119), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 512), Pow(Integer(206119), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(3, 2560), Pow(Integer(565271), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_75(y:sympy.Rational):
	#((y >= sqrt(314679)/640) | (y > -sqrt(12751)/128)) & ((y >= sqrt(314679)/640) | (y < -sqrt(314679)/640)) & ((y <= sqrt(12751)/128) | (y > -sqrt(12751)/128)) & ((y <= sqrt(12751)/128) | (y < -sqrt(314679)/640))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(1, 640), Pow(Integer(314679), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 128), Pow(Integer(12751), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(1, 640), Pow(Integer(314679), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 640), Pow(Integer(314679), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 128), Pow(Integer(12751), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 128), Pow(Integer(12751), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 128), Pow(Integer(12751), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 640), Pow(Integer(314679), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_76(y:sympy.Rational):
	#((y >= sqrt(2617239)/2560) | (y > -sqrt(107311)/512)) & ((y >= sqrt(2617239)/2560) | (y < -sqrt(2617239)/2560)) & ((y <= sqrt(107311)/512) | (y > -sqrt(107311)/512)) & ((y <= sqrt(107311)/512) | (y < -sqrt(2617239)/2560))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(1, 2560), Pow(Integer(2617239), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 512), Pow(Integer(107311), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(1, 2560), Pow(Integer(2617239), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2560), Pow(Integer(2617239), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 512), Pow(Integer(107311), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 512), Pow(Integer(107311), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 512), Pow(Integer(107311), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2560), Pow(Integer(2617239), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_77(y:sympy.Rational):
	#((y >= sqrt(81951)/320) | (y > -sqrt(3319)/64)) & ((y >= sqrt(81951)/320) | (y < -sqrt(81951)/320)) & ((y <= sqrt(3319)/64) | (y > -sqrt(3319)/64)) & ((y <= sqrt(3319)/64) | (y < -sqrt(81951)/320))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(1, 320), Pow(Integer(81951), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 64), Pow(Integer(3319), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(1, 320), Pow(Integer(81951), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 320), Pow(Integer(81951), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 64), Pow(Integer(3319), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 64), Pow(Integer(3319), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 64), Pow(Integer(3319), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 320), Pow(Integer(81951), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_78(y:sympy.Rational):
	#((y >= sqrt(445951)/320) | (y > -sqrt(17879)/64)) & ((y >= sqrt(445951)/320) | (y < -sqrt(445951)/320)) & ((y <= sqrt(17879)/64) | (y > -sqrt(17879)/64)) & ((y <= sqrt(17879)/64) | (y < -sqrt(445951)/320))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(1, 320), Pow(Integer(445951), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 64), Pow(Integer(17879), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(1, 320), Pow(Integer(445951), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 320), Pow(Integer(445951), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 64), Pow(Integer(17879), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 64), Pow(Integer(17879), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 64), Pow(Integer(17879), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 320), Pow(Integer(445951), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_79(y:sympy.Rational):
	#((y >= 3*sqrt(186431)/640) | (y > -sqrt(67279)/128)) & ((y >= 3*sqrt(186431)/640) | (y < -3*sqrt(186431)/640)) & ((y <= sqrt(67279)/128) | (y > -sqrt(67279)/128)) & ((y <= sqrt(67279)/128) | (y < -3*sqrt(186431)/640))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(3, 640), Pow(Integer(186431), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 128), Pow(Integer(67279), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(3, 640), Pow(Integer(186431), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(3, 640), Pow(Integer(186431), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 128), Pow(Integer(67279), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 128), Pow(Integer(67279), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 128), Pow(Integer(67279), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(3, 640), Pow(Integer(186431), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_80(y:sympy.Rational):
	#((y >= 3*sqrt(733399)/1280) | (y > -sqrt(264679)/256)) & ((y >= 3*sqrt(733399)/1280) | (y < -3*sqrt(733399)/1280)) & ((y <= sqrt(264679)/256) | (y > -sqrt(264679)/256)) & ((y <= sqrt(264679)/256) | (y < -3*sqrt(733399)/1280))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(3, 1280), Pow(Integer(733399), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 256), Pow(Integer(264679), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(3, 1280), Pow(Integer(733399), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(3, 1280), Pow(Integer(733399), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 256), Pow(Integer(264679), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 256), Pow(Integer(264679), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 256), Pow(Integer(264679), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(3, 1280), Pow(Integer(733399), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_81(y:sympy.Rational):
	#((y >= 3*sqrt(730599)/1280) | (y > -sqrt(263671)/256)) & ((y >= 3*sqrt(730599)/1280) | (y < -3*sqrt(730599)/1280)) & ((y <= sqrt(263671)/256) | (y > -sqrt(263671)/256)) & ((y <= sqrt(263671)/256) | (y < -3*sqrt(730599)/1280))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(3, 1280), Pow(Integer(730599), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 256), Pow(Integer(263671), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(3, 1280), Pow(Integer(730599), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(3, 1280), Pow(Integer(730599), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 256), Pow(Integer(263671), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 256), Pow(Integer(263671), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 256), Pow(Integer(263671), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(3, 1280), Pow(Integer(730599), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_82(y:sympy.Rational):
	#((y >= sqrt(5297239)/2560) | (y > -sqrt(214511)/512)) & ((y >= sqrt(5297239)/2560) | (y < -sqrt(5297239)/2560)) & ((y <= sqrt(214511)/512) | (y > -sqrt(214511)/512)) & ((y <= sqrt(214511)/512) | (y < -sqrt(5297239)/2560))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(1, 2560), Pow(Integer(5297239), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 512), Pow(Integer(214511), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(1, 2560), Pow(Integer(5297239), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2560), Pow(Integer(5297239), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 512), Pow(Integer(214511), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 512), Pow(Integer(214511), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 512), Pow(Integer(214511), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2560), Pow(Integer(5297239), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_83(y:sympy.Rational):
	#((y >= sqrt(6625591)/1280) | (y > -sqrt(265679)/256)) & ((y >= sqrt(6625591)/1280) | (y < -sqrt(6625591)/1280)) & ((y <= sqrt(265679)/256) | (y > -sqrt(265679)/256)) & ((y <= sqrt(265679)/256) | (y < -sqrt(6625591)/1280))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(1, 1280), Pow(Integer(6625591), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 256), Pow(Integer(265679), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(1, 1280), Pow(Integer(6625591), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1280), Pow(Integer(6625591), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 256), Pow(Integer(265679), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 256), Pow(Integer(265679), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 256), Pow(Integer(265679), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1280), Pow(Integer(6625591), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_84(y:sympy.Rational):
	#((y >= sqrt(55351)/320) | (y > -sqrt(2255)/64)) & ((y >= sqrt(55351)/320) | (y < -sqrt(55351)/320)) & ((y <= sqrt(2255)/64) | (y > -sqrt(2255)/64)) & ((y <= sqrt(2255)/64) | (y < -sqrt(55351)/320))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(1, 320), Pow(Integer(55351), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 64), Pow(Integer(2255), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(1, 320), Pow(Integer(55351), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 320), Pow(Integer(55351), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 64), Pow(Integer(2255), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 64), Pow(Integer(2255), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 64), Pow(Integer(2255), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 320), Pow(Integer(55351), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_85(y:sympy.Rational):
	#((y >= sqrt(411751)/320) | (y > -sqrt(16511)/64)) & ((y >= sqrt(411751)/320) | (y < -sqrt(411751)/320)) & ((y <= sqrt(16511)/64) | (y > -sqrt(16511)/64)) & ((y <= sqrt(16511)/64) | (y < -sqrt(411751)/320))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(1, 320), Pow(Integer(411751), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 64), Pow(Integer(16511), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(1, 320), Pow(Integer(411751), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 320), Pow(Integer(411751), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 64), Pow(Integer(16511), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 64), Pow(Integer(16511), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 64), Pow(Integer(16511), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 320), Pow(Integer(411751), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_86(y:sympy.Rational):
	#((y >= sqrt(5192439)/2560) | (y > -sqrt(210319)/512)) & ((y >= sqrt(5192439)/2560) | (y < -sqrt(5192439)/2560)) & ((y <= sqrt(210319)/512) | (y > -sqrt(210319)/512)) & ((y <= sqrt(210319)/512) | (y < -sqrt(5192439)/2560))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(1, 2560), Pow(Integer(5192439), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 512), Pow(Integer(210319), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(1, 2560), Pow(Integer(5192439), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2560), Pow(Integer(5192439), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 512), Pow(Integer(210319), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 512), Pow(Integer(210319), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 512), Pow(Integer(210319), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2560), Pow(Integer(5192439), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_87(y:sympy.Rational):
	#((y >= sqrt(1640679)/640) | (y > -sqrt(65791)/128)) & ((y >= sqrt(1640679)/640) | (y < -sqrt(1640679)/640)) & ((y <= sqrt(65791)/128) | (y > -sqrt(65791)/128)) & ((y <= sqrt(65791)/128) | (y < -sqrt(1640679)/640))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(1, 640), Pow(Integer(1640679), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 128), Pow(Integer(65791), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(1, 640), Pow(Integer(1640679), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 640), Pow(Integer(1640679), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 128), Pow(Integer(65791), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 128), Pow(Integer(65791), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 128), Pow(Integer(65791), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 640), Pow(Integer(1640679), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_88(y:sympy.Rational):
	#((y >= sqrt(103719)/160) | (y > -sqrt(4159)/32)) & ((y >= sqrt(103719)/160) | (y < -sqrt(103719)/160)) & ((y <= sqrt(4159)/32) | (y > -sqrt(4159)/32)) & ((y <= sqrt(4159)/32) | (y < -sqrt(103719)/160))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(1, 160), Pow(Integer(103719), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 32), Pow(Integer(4159), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(1, 160), Pow(Integer(103719), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 160), Pow(Integer(103719), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 32), Pow(Integer(4159), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 32), Pow(Integer(4159), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 32), Pow(Integer(4159), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 160), Pow(Integer(103719), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_89(y:sympy.Rational):
	#((y >= 3*sqrt(95399)/1280) | (y > -sqrt(34999)/256)) & ((y >= 3*sqrt(95399)/1280) | (y < -3*sqrt(95399)/1280)) & ((y <= sqrt(34999)/256) | (y > -sqrt(34999)/256)) & ((y <= sqrt(34999)/256) | (y < -3*sqrt(95399)/1280))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(3, 1280), Pow(Integer(95399), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 256), Pow(Integer(34999), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(3, 1280), Pow(Integer(95399), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(3, 1280), Pow(Integer(95399), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 256), Pow(Integer(34999), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 256), Pow(Integer(34999), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 256), Pow(Integer(34999), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(3, 1280), Pow(Integer(95399), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_90(y:sympy.Rational):
	#((y >= sqrt(5401839)/2560) | (y > -sqrt(218695)/512)) & ((y >= sqrt(5401839)/2560) | (y < -sqrt(5401839)/2560)) & ((y <= sqrt(218695)/512) | (y > -sqrt(218695)/512)) & ((y <= sqrt(218695)/512) | (y < -sqrt(5401839)/2560))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(1, 2560), Pow(Integer(5401839), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 512), Pow(Integer(218695), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(1, 2560), Pow(Integer(5401839), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2560), Pow(Integer(5401839), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 512), Pow(Integer(218695), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 512), Pow(Integer(218695), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 512), Pow(Integer(218695), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2560), Pow(Integer(5401839), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_91(y:sympy.Rational):
	#((y >= sqrt(3380239)/2560) | (y > -sqrt(137831)/512)) & ((y >= sqrt(3380239)/2560) | (y < -sqrt(3380239)/2560)) & ((y <= sqrt(137831)/512) | (y > -sqrt(137831)/512)) & ((y <= sqrt(137831)/512) | (y < -sqrt(3380239)/2560))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(1, 2560), Pow(Integer(3380239), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 512), Pow(Integer(137831), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(1, 2560), Pow(Integer(3380239), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2560), Pow(Integer(3380239), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 512), Pow(Integer(137831), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 512), Pow(Integer(137831), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 512), Pow(Integer(137831), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2560), Pow(Integer(3380239), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_92(y:sympy.Rational):
	#((y >= sqrt(2726839)/2560) | (y > -sqrt(111695)/512)) & ((y >= sqrt(2726839)/2560) | (y < -sqrt(2726839)/2560)) & ((y <= sqrt(111695)/512) | (y > -sqrt(111695)/512)) & ((y <= sqrt(111695)/512) | (y < -sqrt(2726839)/2560))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(1, 2560), Pow(Integer(2726839), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 512), Pow(Integer(111695), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(1, 2560), Pow(Integer(2726839), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2560), Pow(Integer(2726839), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 512), Pow(Integer(111695), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 512), Pow(Integer(111695), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 512), Pow(Integer(111695), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2560), Pow(Integer(2726839), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_93(y:sympy.Rational):
	#((y >= sqrt(7124991)/1280) | (y > -sqrt(285655)/256)) & ((y >= sqrt(7124991)/1280) | (y < -sqrt(7124991)/1280)) & ((y <= sqrt(285655)/256) | (y > -sqrt(285655)/256)) & ((y <= sqrt(285655)/256) | (y < -sqrt(7124991)/1280))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(1, 1280), Pow(Integer(7124991), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 256), Pow(Integer(285655), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(1, 1280), Pow(Integer(7124991), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1280), Pow(Integer(7124991), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 256), Pow(Integer(285655), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 256), Pow(Integer(285655), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 256), Pow(Integer(285655), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1280), Pow(Integer(7124991), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_94(y:sympy.Rational):
	#((y >= sqrt(5610439)/2560) | (y > -sqrt(227039)/512)) & ((y >= sqrt(5610439)/2560) | (y < -sqrt(5610439)/2560)) & ((y <= sqrt(227039)/512) | (y > -sqrt(227039)/512)) & ((y <= sqrt(227039)/512) | (y < -sqrt(5610439)/2560))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(1, 2560), Pow(Integer(5610439), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 512), Pow(Integer(227039), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(1, 2560), Pow(Integer(5610439), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2560), Pow(Integer(5610439), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 512), Pow(Integer(227039), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 512), Pow(Integer(227039), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 512), Pow(Integer(227039), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2560), Pow(Integer(5610439), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_95(y:sympy.Rational):
	#((y >= sqrt(7145391)/1280) | (y > -sqrt(286471)/256)) & ((y >= sqrt(7145391)/1280) | (y < -sqrt(7145391)/1280)) & ((y <= sqrt(286471)/256) | (y > -sqrt(286471)/256)) & ((y <= sqrt(286471)/256) | (y < -sqrt(7145391)/1280))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(1, 1280), Pow(Integer(7145391), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 256), Pow(Integer(286471), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(1, 1280), Pow(Integer(7145391), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1280), Pow(Integer(7145391), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 256), Pow(Integer(286471), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 256), Pow(Integer(286471), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 256), Pow(Integer(286471), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1280), Pow(Integer(7145391), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_96(y:sympy.Rational):
	#((y >= sqrt(109519)/160) | (y > -sqrt(4391)/32)) & ((y >= sqrt(109519)/160) | (y < -sqrt(109519)/160)) & ((y <= sqrt(4391)/32) | (y > -sqrt(4391)/32)) & ((y <= sqrt(4391)/32) | (y < -sqrt(109519)/160))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(1, 160), Pow(Integer(109519), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 32), Pow(Integer(4391), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(1, 160), Pow(Integer(109519), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 160), Pow(Integer(109519), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 32), Pow(Integer(4391), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 32), Pow(Integer(4391), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 32), Pow(Integer(4391), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 160), Pow(Integer(109519), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_97(y:sympy.Rational):
	#((y >= 19*sqrt(4839)/640) | (y > -sqrt(70039)/128)) & ((y >= 19*sqrt(4839)/640) | (y < -19*sqrt(4839)/640)) & ((y <= sqrt(70039)/128) | (y > -sqrt(70039)/128)) & ((y <= sqrt(70039)/128) | (y < -19*sqrt(4839)/640))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(19, 640), Pow(Integer(4839), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 128), Pow(Integer(70039), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(19, 640), Pow(Integer(4839), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(19, 640), Pow(Integer(4839), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 128), Pow(Integer(70039), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 128), Pow(Integer(70039), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 128), Pow(Integer(70039), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(19, 640), Pow(Integer(4839), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_98(y:sympy.Rational):
	#((y >= sqrt(2836239)/2560) | (y > -sqrt(116071)/512)) & ((y >= sqrt(2836239)/2560) | (y < -sqrt(2836239)/2560)) & ((y <= sqrt(116071)/512) | (y > -sqrt(116071)/512)) & ((y <= sqrt(116071)/512) | (y < -sqrt(2836239)/2560))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(1, 2560), Pow(Integer(2836239), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 512), Pow(Integer(116071), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(1, 2560), Pow(Integer(2836239), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2560), Pow(Integer(2836239), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 512), Pow(Integer(116071), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 512), Pow(Integer(116071), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 512), Pow(Integer(116071), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2560), Pow(Integer(2836239), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_99(y:sympy.Rational):
	#((y >= 3*sqrt(777599)/1280) | (y > -sqrt(280591)/256)) & ((y >= 3*sqrt(777599)/1280) | (y < -3*sqrt(777599)/1280)) & ((y <= sqrt(280591)/256) | (y > -sqrt(280591)/256)) & ((y <= sqrt(280591)/256) | (y < -3*sqrt(777599)/1280))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(3, 1280), Pow(Integer(777599), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 256), Pow(Integer(280591), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(3, 1280), Pow(Integer(777599), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(3, 1280), Pow(Integer(777599), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 256), Pow(Integer(280591), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 256), Pow(Integer(280591), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 256), Pow(Integer(280591), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(3, 1280), Pow(Integer(777599), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_100(y:sympy.Rational):
	#((y >= sqrt(1653279)/640) | (y > -sqrt(66295)/128)) & ((y >= sqrt(1653279)/640) | (y < -sqrt(1653279)/640)) & ((y <= sqrt(66295)/128) | (y > -sqrt(66295)/128)) & ((y <= sqrt(66295)/128) | (y < -sqrt(1653279)/640))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(1, 640), Pow(Integer(1653279), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 128), Pow(Integer(66295), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(1, 640), Pow(Integer(1653279), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 640), Pow(Integer(1653279), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 128), Pow(Integer(66295), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 128), Pow(Integer(66295), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 128), Pow(Integer(66295), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 640), Pow(Integer(1653279), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_101(y:sympy.Rational):
	#((y >= sqrt(6976591)/1280) | (y > -sqrt(279719)/256)) & ((y >= sqrt(6976591)/1280) | (y < -sqrt(6976591)/1280)) & ((y <= sqrt(279719)/256) | (y > -sqrt(279719)/256)) & ((y <= sqrt(279719)/256) | (y < -sqrt(6976591)/1280))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(1, 1280), Pow(Integer(6976591), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 256), Pow(Integer(279719), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(1, 1280), Pow(Integer(6976591), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1280), Pow(Integer(6976591), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 256), Pow(Integer(279719), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 256), Pow(Integer(279719), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 256), Pow(Integer(279719), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1280), Pow(Integer(6976591), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_102(y:sympy.Rational):
	#((y >= 11*sqrt(8871)/1280) | (y > -sqrt(43591)/256)) & ((y >= 11*sqrt(8871)/1280) | (y < -11*sqrt(8871)/1280)) & ((y <= sqrt(43591)/256) | (y > -sqrt(43591)/256)) & ((y <= sqrt(43591)/256) | (y < -11*sqrt(8871)/1280))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(11, 1280), Pow(Integer(8871), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 256), Pow(Integer(43591), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(11, 1280), Pow(Integer(8871), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(11, 1280), Pow(Integer(8871), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 256), Pow(Integer(43591), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 256), Pow(Integer(43591), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 256), Pow(Integer(43591), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(11, 1280), Pow(Integer(8871), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_103(y:sympy.Rational):
	#((y >= sqrt(7041391)/1280) | (y > -sqrt(282311)/256)) & ((y >= sqrt(7041391)/1280) | (y < -sqrt(7041391)/1280)) & ((y <= sqrt(282311)/256) | (y > -sqrt(282311)/256)) & ((y <= sqrt(282311)/256) | (y < -sqrt(7041391)/1280))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(1, 1280), Pow(Integer(7041391), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 256), Pow(Integer(282311), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(1, 1280), Pow(Integer(7041391), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1280), Pow(Integer(7041391), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 256), Pow(Integer(282311), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 256), Pow(Integer(282311), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 256), Pow(Integer(282311), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1280), Pow(Integer(7041391), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_104(y:sympy.Rational):
	#((y >= sqrt(440751)/320) | (y > -sqrt(17671)/64)) & ((y >= sqrt(440751)/320) | (y < -sqrt(440751)/320)) & ((y <= sqrt(17671)/64) | (y > -sqrt(17671)/64)) & ((y <= sqrt(17671)/64) | (y < -sqrt(440751)/320))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(1, 320), Pow(Integer(440751), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 64), Pow(Integer(17671), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(1, 320), Pow(Integer(440751), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 320), Pow(Integer(440751), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 64), Pow(Integer(17671), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 64), Pow(Integer(17671), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 64), Pow(Integer(17671), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 320), Pow(Integer(440751), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_105(y:sympy.Rational):
	#((y >= sqrt(7062591)/1280) | (y > -sqrt(283159)/256)) & ((y >= sqrt(7062591)/1280) | (y < -sqrt(7062591)/1280)) & ((y <= sqrt(283159)/256) | (y > -sqrt(283159)/256)) & ((y <= sqrt(283159)/256) | (y < -sqrt(7062591)/1280))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(1, 1280), Pow(Integer(7062591), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 256), Pow(Integer(283159), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(1, 1280), Pow(Integer(7062591), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1280), Pow(Integer(7062591), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 256), Pow(Integer(283159), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 256), Pow(Integer(283159), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 256), Pow(Integer(283159), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1280), Pow(Integer(7062591), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_106(y:sympy.Rational):
	#((y >= 7*sqrt(35871)/640) | (y > -sqrt(70471)/128)) & ((y >= 7*sqrt(35871)/640) | (y < -7*sqrt(35871)/640)) & ((y <= sqrt(70471)/128) | (y > -sqrt(70471)/128)) & ((y <= sqrt(70471)/128) | (y < -7*sqrt(35871)/640))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(7, 640), Pow(Integer(35871), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 128), Pow(Integer(70471), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(7, 640), Pow(Integer(35871), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(7, 640), Pow(Integer(35871), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 128), Pow(Integer(70471), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 128), Pow(Integer(70471), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 128), Pow(Integer(70471), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(7, 640), Pow(Integer(35871), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_107(y:sympy.Rational):
	#((y >= 3*sqrt(779999)/1280) | (y > -sqrt(281455)/256)) & ((y >= 3*sqrt(779999)/1280) | (y < -3*sqrt(779999)/1280)) & ((y <= sqrt(281455)/256) | (y > -sqrt(281455)/256)) & ((y <= sqrt(281455)/256) | (y < -3*sqrt(779999)/1280))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(3, 1280), Pow(Integer(779999), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 256), Pow(Integer(281455), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(3, 1280), Pow(Integer(779999), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(3, 1280), Pow(Integer(779999), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 256), Pow(Integer(281455), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 256), Pow(Integer(281455), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 256), Pow(Integer(281455), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(3, 1280), Pow(Integer(779999), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_108(y:sympy.Rational):
	#((y >= sqrt(180679)/640) | (y > -sqrt(7391)/128)) & ((y >= sqrt(180679)/640) | (y < -sqrt(180679)/640)) & ((y <= sqrt(7391)/128) | (y > -sqrt(7391)/128)) & ((y <= sqrt(7391)/128) | (y < -sqrt(180679)/640))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(1, 640), Pow(Integer(180679), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 128), Pow(Integer(7391), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(1, 640), Pow(Integer(180679), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 640), Pow(Integer(180679), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 128), Pow(Integer(7391), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 128), Pow(Integer(7391), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 128), Pow(Integer(7391), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 640), Pow(Integer(180679), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_109(y:sympy.Rational):
	#((y >= sqrt(15519)/160) | (y > -sqrt(631)/32)) & ((y >= sqrt(15519)/160) | (y < -sqrt(15519)/160)) & ((y <= sqrt(631)/32) | (y > -sqrt(631)/32)) & ((y <= sqrt(631)/32) | (y < -sqrt(15519)/160))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(1, 160), Pow(Integer(15519), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 32), Pow(Integer(631), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(1, 160), Pow(Integer(15519), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 160), Pow(Integer(15519), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 32), Pow(Integer(631), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 32), Pow(Integer(631), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 32), Pow(Integer(631), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 160), Pow(Integer(15519), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_110(y:sympy.Rational):
	#((y >= 9*sqrt(3559)/640) | (y > -sqrt(11695)/128)) & ((y >= 9*sqrt(3559)/640) | (y < -9*sqrt(3559)/640)) & ((y <= sqrt(11695)/128) | (y > -sqrt(11695)/128)) & ((y <= sqrt(11695)/128) | (y < -9*sqrt(3559)/640))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(9, 640), Pow(Integer(3559), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 128), Pow(Integer(11695), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(9, 640), Pow(Integer(3559), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(9, 640), Pow(Integer(3559), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 128), Pow(Integer(11695), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 128), Pow(Integer(11695), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 128), Pow(Integer(11695), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(9, 640), Pow(Integer(3559), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_111(y:sympy.Rational):
	#((y >= 3*sqrt(459271)/2560) | (y > -sqrt(167959)/512)) & ((y >= 3*sqrt(459271)/2560) | (y < -3*sqrt(459271)/2560)) & ((y <= sqrt(167959)/512) | (y > -sqrt(167959)/512)) & ((y <= sqrt(167959)/512) | (y < -3*sqrt(459271)/2560))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(3, 2560), Pow(Integer(459271), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 512), Pow(Integer(167959), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(3, 2560), Pow(Integer(459271), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(3, 2560), Pow(Integer(459271), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 512), Pow(Integer(167959), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 512), Pow(Integer(167959), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 512), Pow(Integer(167959), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(3, 2560), Pow(Integer(459271), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_112(y:sympy.Rational):
	#((y >= sqrt(4453239)/2560) | (y > -sqrt(180751)/512)) & ((y >= sqrt(4453239)/2560) | (y < -sqrt(4453239)/2560)) & ((y <= sqrt(180751)/512) | (y > -sqrt(180751)/512)) & ((y <= sqrt(180751)/512) | (y < -sqrt(4453239)/2560))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(1, 2560), Pow(Integer(4453239), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 512), Pow(Integer(180751), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(1, 2560), Pow(Integer(4453239), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2560), Pow(Integer(4453239), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 512), Pow(Integer(180751), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 512), Pow(Integer(180751), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 512), Pow(Integer(180751), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2560), Pow(Integer(4453239), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_113(y:sympy.Rational):
	#((y >= sqrt(7282591)/1280) | (y > -sqrt(291959)/256)) & ((y >= sqrt(7282591)/1280) | (y < -sqrt(7282591)/1280)) & ((y <= sqrt(291959)/256) | (y > -sqrt(291959)/256)) & ((y <= sqrt(291959)/256) | (y < -sqrt(7282591)/1280))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(1, 1280), Pow(Integer(7282591), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 256), Pow(Integer(291959), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(1, 1280), Pow(Integer(7282591), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1280), Pow(Integer(7282591), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 256), Pow(Integer(291959), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 256), Pow(Integer(291959), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 256), Pow(Integer(291959), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1280), Pow(Integer(7282591), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_114(y:sympy.Rational):
	#((y >= sqrt(114519)/160) | (y > -sqrt(4591)/32)) & ((y >= sqrt(114519)/160) | (y < -sqrt(114519)/160)) & ((y <= sqrt(4591)/32) | (y > -sqrt(4591)/32)) & ((y <= sqrt(4591)/32) | (y < -sqrt(114519)/160))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(1, 160), Pow(Integer(114519), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 32), Pow(Integer(4591), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(1, 160), Pow(Integer(114519), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 160), Pow(Integer(114519), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 32), Pow(Integer(4591), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 32), Pow(Integer(4591), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 32), Pow(Integer(4591), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 160), Pow(Integer(114519), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_115(y:sympy.Rational):
	#((y >= sqrt(4559439)/2560) | (y > -sqrt(184999)/512)) & ((y >= sqrt(4559439)/2560) | (y < -sqrt(4559439)/2560)) & ((y <= sqrt(184999)/512) | (y > -sqrt(184999)/512)) & ((y <= sqrt(184999)/512) | (y < -sqrt(4559439)/2560))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(1, 2560), Pow(Integer(4559439), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 512), Pow(Integer(184999), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(1, 2560), Pow(Integer(4559439), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2560), Pow(Integer(4559439), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 512), Pow(Integer(184999), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 512), Pow(Integer(184999), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 512), Pow(Integer(184999), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2560), Pow(Integer(4559439), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_116(y:sympy.Rational):
	#((y >= sqrt(125679)/640) | (y > -sqrt(5191)/128)) & ((y >= sqrt(125679)/640) | (y < -sqrt(125679)/640)) & ((y <= sqrt(5191)/128) | (y > -sqrt(5191)/128)) & ((y <= sqrt(5191)/128) | (y < -sqrt(125679)/640))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(1, 640), Pow(Integer(125679), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 128), Pow(Integer(5191), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(1, 640), Pow(Integer(125679), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 640), Pow(Integer(125679), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 128), Pow(Integer(5191), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 128), Pow(Integer(5191), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 128), Pow(Integer(5191), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 640), Pow(Integer(125679), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_117(y:sympy.Rational):
	#((y >= sqrt(1126591)/1280) | (y > -sqrt(45719)/256)) & ((y >= sqrt(1126591)/1280) | (y < -sqrt(1126591)/1280)) & ((y <= sqrt(45719)/256) | (y > -sqrt(45719)/256)) & ((y <= sqrt(45719)/256) | (y < -sqrt(1126591)/1280))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(1, 1280), Pow(Integer(1126591), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 256), Pow(Integer(45719), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(1, 1280), Pow(Integer(1126591), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1280), Pow(Integer(1126591), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 256), Pow(Integer(45719), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 256), Pow(Integer(45719), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 256), Pow(Integer(45719), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1280), Pow(Integer(1126591), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_118(y:sympy.Rational):
	#((y >= sqrt(1808679)/640) | (y > -sqrt(72511)/128)) & ((y >= sqrt(1808679)/640) | (y < -sqrt(1808679)/640)) & ((y <= sqrt(72511)/128) | (y > -sqrt(72511)/128)) & ((y <= sqrt(72511)/128) | (y < -sqrt(1808679)/640))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(1, 640), Pow(Integer(1808679), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 128), Pow(Integer(72511), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(1, 640), Pow(Integer(1808679), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 640), Pow(Integer(1808679), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 128), Pow(Integer(72511), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 128), Pow(Integer(72511), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 128), Pow(Integer(72511), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 640), Pow(Integer(1808679), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_119(y:sympy.Rational):
	#((y >= sqrt(1771)/20) | (y > -sqrt(71)/4)) & ((y >= sqrt(1771)/20) | (y < -sqrt(1771)/20)) & ((y <= sqrt(71)/4) | (y > -sqrt(71)/4)) & ((y <= sqrt(71)/4) | (y < -sqrt(1771)/20))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(1, 20), Pow(Integer(1771), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 4), Pow(Integer(71), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(1, 20), Pow(Integer(1771), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 20), Pow(Integer(1771), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 4), Pow(Integer(71), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 4), Pow(Integer(71), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 4), Pow(Integer(71), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 20), Pow(Integer(1771), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_120(y:sympy.Rational):
	#((y >= 11*sqrt(231)/320) | (y > -sqrt(1159)/64)) & ((y >= 11*sqrt(231)/320) | (y < -11*sqrt(231)/320)) & ((y <= sqrt(1159)/64) | (y > -sqrt(1159)/64)) & ((y <= sqrt(1159)/64) | (y < -11*sqrt(231)/320))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(11, 320), Pow(Integer(231), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 64), Pow(Integer(1159), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(11, 320), Pow(Integer(231), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(11, 320), Pow(Integer(231), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 64), Pow(Integer(1159), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 64), Pow(Integer(1159), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 64), Pow(Integer(1159), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(11, 320), Pow(Integer(231), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_121(y:sympy.Rational):
	#((y >= 3*sqrt(7639)/320) | (y > -sqrt(2791)/64)) & ((y >= 3*sqrt(7639)/320) | (y < -3*sqrt(7639)/320)) & ((y <= sqrt(2791)/64) | (y > -sqrt(2791)/64)) & ((y <= sqrt(2791)/64) | (y < -3*sqrt(7639)/320))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(3, 320), Pow(Integer(7639), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 64), Pow(Integer(2791), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(3, 320), Pow(Integer(7639), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(3, 320), Pow(Integer(7639), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 64), Pow(Integer(2791), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 64), Pow(Integer(2791), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 64), Pow(Integer(2791), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(3, 320), Pow(Integer(7639), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_122(y:sympy.Rational):
	#((y >= 11*sqrt(59871)/1280) | (y > -sqrt(290431)/256)) & ((y >= 11*sqrt(59871)/1280) | (y < -11*sqrt(59871)/1280)) & ((y <= sqrt(290431)/256) | (y > -sqrt(290431)/256)) & ((y <= sqrt(290431)/256) | (y < -11*sqrt(59871)/1280))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(11, 1280), Pow(Integer(59871), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 256), Pow(Integer(290431), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(11, 1280), Pow(Integer(59871), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(11, 1280), Pow(Integer(59871), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 256), Pow(Integer(290431), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 256), Pow(Integer(290431), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 256), Pow(Integer(290431), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(11, 1280), Pow(Integer(59871), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_123(y:sympy.Rational):
	#((y >= 3*sqrt(202031)/640) | (y > -sqrt(72895)/128)) & ((y >= 3*sqrt(202031)/640) | (y < -3*sqrt(202031)/640)) & ((y <= sqrt(72895)/128) | (y > -sqrt(72895)/128)) & ((y <= sqrt(72895)/128) | (y < -3*sqrt(202031)/640))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(3, 640), Pow(Integer(202031), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 128), Pow(Integer(72895), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(3, 640), Pow(Integer(202031), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(3, 640), Pow(Integer(202031), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 128), Pow(Integer(72895), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 128), Pow(Integer(72895), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 128), Pow(Integer(72895), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(3, 640), Pow(Integer(202031), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_124(y:sympy.Rational):
	#((y >= sqrt(7263591)/1280) | (y > -sqrt(291199)/256)) & ((y >= sqrt(7263591)/1280) | (y < -sqrt(7263591)/1280)) & ((y <= sqrt(291199)/256) | (y > -sqrt(291199)/256)) & ((y <= sqrt(291199)/256) | (y < -sqrt(7263591)/1280))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(1, 1280), Pow(Integer(7263591), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 256), Pow(Integer(291199), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(1, 1280), Pow(Integer(7263591), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1280), Pow(Integer(7263591), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 256), Pow(Integer(291199), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 256), Pow(Integer(291199), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 256), Pow(Integer(291199), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1280), Pow(Integer(7263591), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_125(y:sympy.Rational):
	#((y >= 21*sqrt(951)/1280) | (y > -sqrt(17431)/256)) & ((y >= 21*sqrt(951)/1280) | (y < -21*sqrt(951)/1280)) & ((y <= sqrt(17431)/256) | (y > -sqrt(17431)/256)) & ((y <= sqrt(17431)/256) | (y < -21*sqrt(951)/1280))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(21, 1280), Pow(Integer(951), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 256), Pow(Integer(17431), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(21, 1280), Pow(Integer(951), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(21, 1280), Pow(Integer(951), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 256), Pow(Integer(17431), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 256), Pow(Integer(17431), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 256), Pow(Integer(17431), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(21, 1280), Pow(Integer(951), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_126(y:sympy.Rational):
	#((y >= sqrt(1733239)/2560) | (y > -sqrt(71951)/512)) & ((y >= sqrt(1733239)/2560) | (y < -sqrt(1733239)/2560)) & ((y <= sqrt(71951)/512) | (y > -sqrt(71951)/512)) & ((y <= sqrt(71951)/512) | (y < -sqrt(1733239)/2560))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(1, 2560), Pow(Integer(1733239), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 512), Pow(Integer(71951), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(1, 2560), Pow(Integer(1733239), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2560), Pow(Integer(1733239), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 512), Pow(Integer(71951), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 512), Pow(Integer(71951), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 512), Pow(Integer(71951), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2560), Pow(Integer(1733239), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_127(y:sympy.Rational):
	#((y >= sqrt(474991)/1280) | (y > -sqrt(19655)/256)) & ((y >= sqrt(474991)/1280) | (y < -sqrt(474991)/1280)) & ((y <= sqrt(19655)/256) | (y > -sqrt(19655)/256)) & ((y <= sqrt(19655)/256) | (y < -sqrt(474991)/1280))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(1, 1280), Pow(Integer(474991), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 256), Pow(Integer(19655), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(1, 1280), Pow(Integer(474991), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1280), Pow(Integer(474991), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 256), Pow(Integer(19655), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 256), Pow(Integer(19655), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 256), Pow(Integer(19655), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1280), Pow(Integer(474991), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_128(y:sympy.Rational):
	#((y >= 3*sqrt(217271)/2560) | (y > -sqrt(80839)/512)) & ((y >= 3*sqrt(217271)/2560) | (y < -3*sqrt(217271)/2560)) & ((y <= sqrt(80839)/512) | (y > -sqrt(80839)/512)) & ((y <= sqrt(80839)/512) | (y < -3*sqrt(217271)/2560))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(3, 2560), Pow(Integer(217271), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 512), Pow(Integer(80839), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(3, 2560), Pow(Integer(217271), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(3, 2560), Pow(Integer(217271), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 512), Pow(Integer(80839), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 512), Pow(Integer(80839), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 512), Pow(Integer(80839), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(3, 2560), Pow(Integer(217271), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_129(y:sympy.Rational):
	#((y >= sqrt(1844439)/2560) | (y > -sqrt(76399)/512)) & ((y >= sqrt(1844439)/2560) | (y < -sqrt(1844439)/2560)) & ((y <= sqrt(76399)/512) | (y > -sqrt(76399)/512)) & ((y <= sqrt(76399)/512) | (y < -sqrt(1844439)/2560))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(1, 2560), Pow(Integer(1844439), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 512), Pow(Integer(76399), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(1, 2560), Pow(Integer(1844439), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2560), Pow(Integer(1844439), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 512), Pow(Integer(76399), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 512), Pow(Integer(76399), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 512), Pow(Integer(76399), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2560), Pow(Integer(1844439), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_130(y:sympy.Rational):
	#((y >= sqrt(1019991)/1280) | (y > -sqrt(41455)/256)) & ((y >= sqrt(1019991)/1280) | (y < -sqrt(1019991)/1280)) & ((y <= sqrt(41455)/256) | (y > -sqrt(41455)/256)) & ((y <= sqrt(41455)/256) | (y < -sqrt(1019991)/1280))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(1, 1280), Pow(Integer(1019991), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 256), Pow(Integer(41455), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(1, 1280), Pow(Integer(1019991), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1280), Pow(Integer(1019991), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 256), Pow(Integer(41455), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 256), Pow(Integer(41455), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 256), Pow(Integer(41455), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1280), Pow(Integer(1019991), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_131(y:sympy.Rational):
	#((y >= sqrt(2287239)/2560) | (y > -sqrt(94111)/512)) & ((y >= sqrt(2287239)/2560) | (y < -sqrt(2287239)/2560)) & ((y <= sqrt(94111)/512) | (y > -sqrt(94111)/512)) & ((y <= sqrt(94111)/512) | (y < -sqrt(2287239)/2560))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(1, 2560), Pow(Integer(2287239), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 512), Pow(Integer(94111), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(1, 2560), Pow(Integer(2287239), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2560), Pow(Integer(2287239), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 512), Pow(Integer(94111), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 512), Pow(Integer(94111), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 512), Pow(Integer(94111), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2560), Pow(Integer(2287239), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_132(y:sympy.Rational):
	#((y >= 7*sqrt(88711)/2560) | (y > -sqrt(176495)/512)) & ((y >= 7*sqrt(88711)/2560) | (y < -7*sqrt(88711)/2560)) & ((y <= sqrt(176495)/512) | (y > -sqrt(176495)/512)) & ((y <= sqrt(176495)/512) | (y < -7*sqrt(88711)/2560))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(7, 2560), Pow(Integer(88711), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 512), Pow(Integer(176495), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(7, 2560), Pow(Integer(88711), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(7, 2560), Pow(Integer(88711), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 512), Pow(Integer(176495), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 512), Pow(Integer(176495), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 512), Pow(Integer(176495), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(7, 2560), Pow(Integer(88711), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_133(y:sympy.Rational):
	#((y >= sqrt(1827679)/640) | (y > -sqrt(73271)/128)) & ((y >= sqrt(1827679)/640) | (y < -sqrt(1827679)/640)) & ((y <= sqrt(73271)/128) | (y > -sqrt(73271)/128)) & ((y <= sqrt(73271)/128) | (y < -sqrt(1827679)/640))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(1, 640), Pow(Integer(1827679), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 128), Pow(Integer(73271), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(1, 640), Pow(Integer(1827679), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 640), Pow(Integer(1827679), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 128), Pow(Integer(73271), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 128), Pow(Integer(73271), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 128), Pow(Integer(73271), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 640), Pow(Integer(1827679), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_134(y:sympy.Rational):
	#((y >= sqrt(1798879)/640) | (y > -sqrt(72119)/128)) & ((y >= sqrt(1798879)/640) | (y < -sqrt(1798879)/640)) & ((y <= sqrt(72119)/128) | (y > -sqrt(72119)/128)) & ((y <= sqrt(72119)/128) | (y < -sqrt(1798879)/640))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(1, 640), Pow(Integer(1798879), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 128), Pow(Integer(72119), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(1, 640), Pow(Integer(1798879), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 640), Pow(Integer(1798879), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 128), Pow(Integer(72119), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 128), Pow(Integer(72119), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 128), Pow(Integer(72119), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 640), Pow(Integer(1798879), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_135(y:sympy.Rational):
	#((y >= sqrt(4711)/80) | (y > -sqrt(191)/16)) & ((y >= sqrt(4711)/80) | (y < -sqrt(4711)/80)) & ((y <= sqrt(191)/16) | (y > -sqrt(191)/16)) & ((y <= sqrt(191)/16) | (y < -sqrt(4711)/80))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(1, 80), Pow(Integer(4711), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 16), Pow(Integer(191), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(1, 80), Pow(Integer(4711), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 80), Pow(Integer(4711), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 16), Pow(Integer(191), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 16), Pow(Integer(191), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 16), Pow(Integer(191), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 80), Pow(Integer(4711), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_136(y:sympy.Rational):
	#((y >= sqrt(2397439)/2560) | (y > -sqrt(98519)/512)) & ((y >= sqrt(2397439)/2560) | (y < -sqrt(2397439)/2560)) & ((y <= sqrt(98519)/512) | (y > -sqrt(98519)/512)) & ((y <= sqrt(98519)/512) | (y < -sqrt(2397439)/2560))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(1, 2560), Pow(Integer(2397439), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 512), Pow(Integer(98519), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(1, 2560), Pow(Integer(2397439), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2560), Pow(Integer(2397439), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 512), Pow(Integer(98519), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 512), Pow(Integer(98519), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 512), Pow(Integer(98519), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2560), Pow(Integer(2397439), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_137(y:sympy.Rational):
	#((y >= sqrt(450951)/320) | (y > -sqrt(18079)/64)) & ((y >= sqrt(450951)/320) | (y < -sqrt(450951)/320)) & ((y <= sqrt(18079)/64) | (y > -sqrt(18079)/64)) & ((y <= sqrt(18079)/64) | (y < -sqrt(450951)/320))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(1, 320), Pow(Integer(450951), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 64), Pow(Integer(18079), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(1, 320), Pow(Integer(450951), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 320), Pow(Integer(450951), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 64), Pow(Integer(18079), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 64), Pow(Integer(18079), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 64), Pow(Integer(18079), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 320), Pow(Integer(450951), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_138(y:sympy.Rational):
	#((y >= 9*sqrt(88711)/1280) | (y > -sqrt(288079)/256)) & ((y >= 9*sqrt(88711)/1280) | (y < -9*sqrt(88711)/1280)) & ((y <= sqrt(288079)/256) | (y > -sqrt(288079)/256)) & ((y <= sqrt(288079)/256) | (y < -9*sqrt(88711)/1280))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(9, 1280), Pow(Integer(88711), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 256), Pow(Integer(288079), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(9, 1280), Pow(Integer(88711), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(9, 1280), Pow(Integer(88711), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 256), Pow(Integer(288079), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 256), Pow(Integer(288079), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 256), Pow(Integer(288079), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(9, 1280), Pow(Integer(88711), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_139(y:sympy.Rational):
	#((y >= 3*sqrt(17031)/640) | (y > -sqrt(6295)/128)) & ((y >= 3*sqrt(17031)/640) | (y < -3*sqrt(17031)/640)) & ((y <= sqrt(6295)/128) | (y > -sqrt(6295)/128)) & ((y <= sqrt(6295)/128) | (y < -3*sqrt(17031)/640))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(3, 640), Pow(Integer(17031), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 128), Pow(Integer(6295), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(3, 640), Pow(Integer(17031), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(3, 640), Pow(Integer(17031), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 128), Pow(Integer(6295), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 128), Pow(Integer(6295), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 128), Pow(Integer(6295), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(3, 640), Pow(Integer(17031), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_140(y:sympy.Rational):
	#((y >= 3*sqrt(541871)/2560) | (y > -sqrt(197695)/512)) & ((y >= 3*sqrt(541871)/2560) | (y < -3*sqrt(541871)/2560)) & ((y <= sqrt(197695)/512) | (y > -sqrt(197695)/512)) & ((y <= sqrt(197695)/512) | (y < -3*sqrt(541871)/2560))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(3, 2560), Pow(Integer(541871), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 512), Pow(Integer(197695), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(3, 2560), Pow(Integer(541871), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(3, 2560), Pow(Integer(541871), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 512), Pow(Integer(197695), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 512), Pow(Integer(197695), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 512), Pow(Integer(197695), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(3, 2560), Pow(Integer(541871), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_141(y:sympy.Rational):
	#((y >= sqrt(585591)/1280) | (y > -11*sqrt(199)/256)) & ((y >= sqrt(585591)/1280) | (y < -sqrt(585591)/1280)) & ((y <= 11*sqrt(199)/256) | (y > -11*sqrt(199)/256)) & ((y <= 11*sqrt(199)/256) | (y < -sqrt(585591)/1280))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(1, 1280), Pow(Integer(585591), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(11, 256), Pow(Integer(199), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(1, 1280), Pow(Integer(585591), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1280), Pow(Integer(585591), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(11, 256), Pow(Integer(199), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(11, 256), Pow(Integer(199), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(11, 256), Pow(Integer(199), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1280), Pow(Integer(585591), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_142(y:sympy.Rational):
	#((y >= sqrt(7319991)/1280) | (y > -sqrt(293455)/256)) & ((y >= sqrt(7319991)/1280) | (y < -sqrt(7319991)/1280)) & ((y <= sqrt(293455)/256) | (y > -sqrt(293455)/256)) & ((y <= sqrt(293455)/256) | (y < -sqrt(7319991)/1280))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(1, 1280), Pow(Integer(7319991), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 256), Pow(Integer(293455), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(1, 1280), Pow(Integer(7319991), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1280), Pow(Integer(7319991), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 256), Pow(Integer(293455), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 256), Pow(Integer(293455), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 256), Pow(Integer(293455), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1280), Pow(Integer(7319991), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_143(y:sympy.Rational):
	#((y >= sqrt(1179591)/1280) | (y > -sqrt(47839)/256)) & ((y >= sqrt(1179591)/1280) | (y < -sqrt(1179591)/1280)) & ((y <= sqrt(47839)/256) | (y > -sqrt(47839)/256)) & ((y <= sqrt(47839)/256) | (y < -sqrt(1179591)/1280))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(1, 1280), Pow(Integer(1179591), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 256), Pow(Integer(47839), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(1, 1280), Pow(Integer(1179591), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1280), Pow(Integer(1179591), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 256), Pow(Integer(47839), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 256), Pow(Integer(47839), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 256), Pow(Integer(47839), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1280), Pow(Integer(1179591), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_144(y:sympy.Rational):
	#((y >= 3*sqrt(241871)/2560) | (y > -sqrt(89695)/512)) & ((y >= 3*sqrt(241871)/2560) | (y < -3*sqrt(241871)/2560)) & ((y <= sqrt(89695)/512) | (y > -sqrt(89695)/512)) & ((y <= sqrt(89695)/512) | (y < -3*sqrt(241871)/2560))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(3, 2560), Pow(Integer(241871), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 512), Pow(Integer(89695), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(3, 2560), Pow(Integer(241871), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(3, 2560), Pow(Integer(241871), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 512), Pow(Integer(89695), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 512), Pow(Integer(89695), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 512), Pow(Integer(89695), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(3, 2560), Pow(Integer(241871), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_145(y:sympy.Rational):
	#((y >= sqrt(530391)/1280) | (y > -sqrt(21871)/256)) & ((y >= sqrt(530391)/1280) | (y < -sqrt(530391)/1280)) & ((y <= sqrt(21871)/256) | (y > -sqrt(21871)/256)) & ((y <= sqrt(21871)/256) | (y < -sqrt(530391)/1280))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(1, 1280), Pow(Integer(530391), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 256), Pow(Integer(21871), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(1, 1280), Pow(Integer(530391), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1280), Pow(Integer(530391), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 256), Pow(Integer(21871), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 256), Pow(Integer(21871), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 256), Pow(Integer(21871), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1280), Pow(Integer(530391), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_146(y:sympy.Rational):
	#((y >= 3*sqrt(800599)/1280) | (y > -sqrt(288871)/256)) & ((y >= 3*sqrt(800599)/1280) | (y < -3*sqrt(800599)/1280)) & ((y <= sqrt(288871)/256) | (y > -sqrt(288871)/256)) & ((y <= sqrt(288871)/256) | (y < -3*sqrt(800599)/1280))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(3, 1280), Pow(Integer(800599), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 256), Pow(Integer(288871), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(3, 1280), Pow(Integer(800599), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(3, 1280), Pow(Integer(800599), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 256), Pow(Integer(288871), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 256), Pow(Integer(288871), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 256), Pow(Integer(288871), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(3, 1280), Pow(Integer(800599), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_147(y:sympy.Rational):
	#((y >= 3*sqrt(50639)/320) | (y > -11*sqrt(151)/64)) & ((y >= 3*sqrt(50639)/320) | (y < -3*sqrt(50639)/320)) & ((y <= 11*sqrt(151)/64) | (y > -11*sqrt(151)/64)) & ((y <= 11*sqrt(151)/64) | (y < -3*sqrt(50639)/320))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(3, 320), Pow(Integer(50639), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(11, 64), Pow(Integer(151), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(3, 320), Pow(Integer(50639), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(3, 320), Pow(Integer(50639), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(11, 64), Pow(Integer(151), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(11, 64), Pow(Integer(151), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(11, 64), Pow(Integer(151), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(3, 320), Pow(Integer(50639), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_148(y:sympy.Rational):
	#((y >= sqrt(7224991)/1280) | (y > -sqrt(289655)/256)) & ((y >= sqrt(7224991)/1280) | (y < -sqrt(7224991)/1280)) & ((y <= sqrt(289655)/256) | (y > -sqrt(289655)/256)) & ((y <= sqrt(289655)/256) | (y < -sqrt(7224991)/1280))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(1, 1280), Pow(Integer(7224991), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 256), Pow(Integer(289655), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(1, 1280), Pow(Integer(7224991), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1280), Pow(Integer(7224991), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 256), Pow(Integer(289655), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 256), Pow(Integer(289655), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 256), Pow(Integer(289655), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1280), Pow(Integer(7224991), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_149(y:sympy.Rational):
	#((y >= sqrt(1232391)/1280) | (y > -sqrt(49951)/256)) & ((y >= sqrt(1232391)/1280) | (y < -sqrt(1232391)/1280)) & ((y <= sqrt(49951)/256) | (y > -sqrt(49951)/256)) & ((y <= sqrt(49951)/256) | (y < -sqrt(1232391)/1280))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(1, 1280), Pow(Integer(1232391), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 256), Pow(Integer(49951), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(1, 1280), Pow(Integer(1232391), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1280), Pow(Integer(1232391), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 256), Pow(Integer(49951), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 256), Pow(Integer(49951), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 256), Pow(Integer(49951), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1280), Pow(Integer(1232391), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_150(y:sympy.Rational):
	#((y >= sqrt(8719)/160) | (y > -sqrt(359)/32)) & ((y >= sqrt(8719)/160) | (y < -sqrt(8719)/160)) & ((y <= sqrt(359)/32) | (y > -sqrt(359)/32)) & ((y <= sqrt(359)/32) | (y < -sqrt(8719)/160))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(1, 160), Pow(Integer(8719), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 32), Pow(Integer(359), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(1, 160), Pow(Integer(8719), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 160), Pow(Integer(8719), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 32), Pow(Integer(359), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 32), Pow(Integer(359), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 32), Pow(Integer(359), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 160), Pow(Integer(8719), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_151(y:sympy.Rational):
	#((y >= sqrt(4771239)/2560) | (y > -79*sqrt(31)/512)) & ((y >= sqrt(4771239)/2560) | (y < -sqrt(4771239)/2560)) & ((y <= 79*sqrt(31)/512) | (y > -79*sqrt(31)/512)) & ((y <= 79*sqrt(31)/512) | (y < -sqrt(4771239)/2560))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(1, 2560), Pow(Integer(4771239), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(79, 512), Pow(Integer(31), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(1, 2560), Pow(Integer(4771239), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2560), Pow(Integer(4771239), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(79, 512), Pow(Integer(31), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(79, 512), Pow(Integer(31), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(79, 512), Pow(Integer(31), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2560), Pow(Integer(4771239), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_152(y:sympy.Rational):
	#((y >= sqrt(2066239)/2560) | (y > -sqrt(85271)/512)) & ((y >= sqrt(2066239)/2560) | (y < -sqrt(2066239)/2560)) & ((y <= sqrt(85271)/512) | (y > -sqrt(85271)/512)) & ((y <= sqrt(85271)/512) | (y < -sqrt(2066239)/2560))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(1, 2560), Pow(Integer(2066239), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 512), Pow(Integer(85271), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(1, 2560), Pow(Integer(2066239), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2560), Pow(Integer(2066239), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 512), Pow(Integer(85271), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 512), Pow(Integer(85271), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 512), Pow(Integer(85271), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2560), Pow(Integer(2066239), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_153(y:sympy.Rational):
	#((y >= sqrt(261679)/640) | (y > -sqrt(10631)/128)) & ((y >= sqrt(261679)/640) | (y < -sqrt(261679)/640)) & ((y <= sqrt(10631)/128) | (y > -sqrt(10631)/128)) & ((y <= sqrt(10631)/128) | (y < -sqrt(261679)/640))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(1, 640), Pow(Integer(261679), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 128), Pow(Integer(10631), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(1, 640), Pow(Integer(261679), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 640), Pow(Integer(261679), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 128), Pow(Integer(10631), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 128), Pow(Integer(10631), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 128), Pow(Integer(10631), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 640), Pow(Integer(261679), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_154(y:sympy.Rational):
	#((y >= sqrt(4665439)/2560) | (y > -sqrt(189239)/512)) & ((y >= sqrt(4665439)/2560) | (y < -sqrt(4665439)/2560)) & ((y <= sqrt(189239)/512) | (y > -sqrt(189239)/512)) & ((y <= sqrt(189239)/512) | (y < -sqrt(4665439)/2560))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(1, 2560), Pow(Integer(4665439), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 512), Pow(Integer(189239), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(1, 2560), Pow(Integer(4665439), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2560), Pow(Integer(4665439), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 512), Pow(Integer(189239), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 512), Pow(Integer(189239), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 512), Pow(Integer(189239), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2560), Pow(Integer(4665439), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_155(y:sympy.Rational):
	#((y >= sqrt(460351)/320) | (y > -sqrt(18455)/64)) & ((y >= sqrt(460351)/320) | (y < -sqrt(460351)/320)) & ((y <= sqrt(18455)/64) | (y > -sqrt(18455)/64)) & ((y <= sqrt(18455)/64) | (y < -sqrt(460351)/320))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(1, 320), Pow(Integer(460351), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 64), Pow(Integer(18455), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(1, 320), Pow(Integer(460351), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 320), Pow(Integer(460351), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 64), Pow(Integer(18455), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 64), Pow(Integer(18455), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 64), Pow(Integer(18455), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 320), Pow(Integer(460351), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_156(y:sympy.Rational):
	#((y >= sqrt(7301391)/1280) | (y > -sqrt(292711)/256)) & ((y >= sqrt(7301391)/1280) | (y < -sqrt(7301391)/1280)) & ((y <= sqrt(292711)/256) | (y > -sqrt(292711)/256)) & ((y <= sqrt(292711)/256) | (y < -sqrt(7301391)/1280))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(1, 1280), Pow(Integer(7301391), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 256), Pow(Integer(292711), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(1, 1280), Pow(Integer(7301391), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1280), Pow(Integer(7301391), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 256), Pow(Integer(292711), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 256), Pow(Integer(292711), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 256), Pow(Integer(292711), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1280), Pow(Integer(7301391), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_157(y:sympy.Rational):
	#((y >= sqrt(1836879)/640) | (y > -sqrt(73639)/128)) & ((y >= sqrt(1836879)/640) | (y < -sqrt(1836879)/640)) & ((y <= sqrt(73639)/128) | (y > -sqrt(73639)/128)) & ((y <= sqrt(73639)/128) | (y < -sqrt(1836879)/640))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(1, 640), Pow(Integer(1836879), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 128), Pow(Integer(73639), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(1, 640), Pow(Integer(1836879), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 640), Pow(Integer(1836879), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 128), Pow(Integer(73639), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 128), Pow(Integer(73639), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 128), Pow(Integer(73639), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 640), Pow(Integer(1836879), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_158(y:sympy.Rational):
	#((y >= 3*sqrt(817399)/1280) | (y > -sqrt(294919)/256)) & ((y >= 3*sqrt(817399)/1280) | (y < -3*sqrt(817399)/1280)) & ((y <= sqrt(294919)/256) | (y > -sqrt(294919)/256)) & ((y <= sqrt(294919)/256) | (y < -3*sqrt(817399)/1280))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(3, 1280), Pow(Integer(817399), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 256), Pow(Integer(294919), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(3, 1280), Pow(Integer(817399), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(3, 1280), Pow(Integer(817399), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 256), Pow(Integer(294919), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 256), Pow(Integer(294919), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 256), Pow(Integer(294919), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(3, 1280), Pow(Integer(817399), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_159(y:sympy.Rational):
	#((y >= sqrt(4026439)/2560) | (y > -sqrt(163679)/512)) & ((y >= sqrt(4026439)/2560) | (y < -sqrt(4026439)/2560)) & ((y <= sqrt(163679)/512) | (y > -sqrt(163679)/512)) & ((y <= sqrt(163679)/512) | (y < -sqrt(4026439)/2560))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(1, 2560), Pow(Integer(4026439), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 512), Pow(Integer(163679), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(1, 2560), Pow(Integer(4026439), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2560), Pow(Integer(4026439), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 512), Pow(Integer(163679), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 512), Pow(Integer(163679), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 512), Pow(Integer(163679), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2560), Pow(Integer(4026439), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_160(y:sympy.Rational):
	#((y >= sqrt(7338391)/1280) | (y > -sqrt(294191)/256)) & ((y >= sqrt(7338391)/1280) | (y < -sqrt(7338391)/1280)) & ((y <= sqrt(294191)/256) | (y > -sqrt(294191)/256)) & ((y <= sqrt(294191)/256) | (y < -sqrt(7338391)/1280))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(1, 1280), Pow(Integer(7338391), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 256), Pow(Integer(294191), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(1, 1280), Pow(Integer(7338391), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1280), Pow(Integer(7338391), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 256), Pow(Integer(294191), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 256), Pow(Integer(294191), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 256), Pow(Integer(294191), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1280), Pow(Integer(7338391), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_161(y:sympy.Rational):
	#((y >= 3*sqrt(819399)/1280) | (y > -sqrt(295639)/256)) & ((y >= 3*sqrt(819399)/1280) | (y < -3*sqrt(819399)/1280)) & ((y <= sqrt(295639)/256) | (y > -sqrt(295639)/256)) & ((y <= sqrt(295639)/256) | (y < -3*sqrt(819399)/1280))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(3, 1280), Pow(Integer(819399), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 256), Pow(Integer(295639), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(3, 1280), Pow(Integer(819399), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(3, 1280), Pow(Integer(819399), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 256), Pow(Integer(295639), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 256), Pow(Integer(295639), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 256), Pow(Integer(295639), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(3, 1280), Pow(Integer(819399), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_162(y:sympy.Rational):
	#((y >= 21*sqrt(1111)/320) | (y > -sqrt(19639)/64)) & ((y >= 21*sqrt(1111)/320) | (y < -21*sqrt(1111)/320)) & ((y <= sqrt(19639)/64) | (y > -sqrt(19639)/64)) & ((y <= sqrt(19639)/64) | (y < -21*sqrt(1111)/320))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(21, 320), Pow(Integer(1111), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 64), Pow(Integer(19639), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(21, 320), Pow(Integer(1111), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(21, 320), Pow(Integer(1111), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 64), Pow(Integer(19639), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 64), Pow(Integer(19639), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 64), Pow(Integer(19639), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(21, 320), Pow(Integer(1111), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_163(y:sympy.Rational):
	#((y >= sqrt(1903279)/640) | (y > -sqrt(76295)/128)) & ((y >= sqrt(1903279)/640) | (y < -sqrt(1903279)/640)) & ((y <= sqrt(76295)/128) | (y > -sqrt(76295)/128)) & ((y <= sqrt(76295)/128) | (y < -sqrt(1903279)/640))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(1, 640), Pow(Integer(1903279), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 128), Pow(Integer(76295), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(1, 640), Pow(Integer(1903279), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 640), Pow(Integer(1903279), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 128), Pow(Integer(76295), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 128), Pow(Integer(76295), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 128), Pow(Integer(76295), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 640), Pow(Integer(1903279), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_164(y:sympy.Rational):
	#((y >= 3*sqrt(13391)/160) | (y > -sqrt(4831)/32)) & ((y >= 3*sqrt(13391)/160) | (y < -3*sqrt(13391)/160)) & ((y <= sqrt(4831)/32) | (y > -sqrt(4831)/32)) & ((y <= sqrt(4831)/32) | (y < -3*sqrt(13391)/160))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(3, 160), Pow(Integer(13391), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 32), Pow(Integer(4831), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(3, 160), Pow(Integer(13391), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(3, 160), Pow(Integer(13391), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 32), Pow(Integer(4831), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 32), Pow(Integer(4831), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 32), Pow(Integer(4831), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(3, 160), Pow(Integer(13391), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_165(y:sympy.Rational):
	#((y >= sqrt(29911)/80) | (y > -sqrt(1199)/16)) & ((y >= sqrt(29911)/80) | (y < -sqrt(29911)/80)) & ((y <= sqrt(1199)/16) | (y > -sqrt(1199)/16)) & ((y <= sqrt(1199)/16) | (y < -sqrt(29911)/80))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(1, 80), Pow(Integer(29911), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 16), Pow(Integer(1199), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(1, 80), Pow(Integer(29911), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 80), Pow(Integer(29911), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 16), Pow(Integer(1199), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 16), Pow(Integer(1199), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 16), Pow(Integer(1199), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 80), Pow(Integer(29911), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_166(y:sympy.Rational):
	#((y >= sqrt(480351)/320) | (y > -sqrt(19255)/64)) & ((y >= sqrt(480351)/320) | (y < -sqrt(480351)/320)) & ((y <= sqrt(19255)/64) | (y > -sqrt(19255)/64)) & ((y <= sqrt(19255)/64) | (y < -sqrt(480351)/320))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(1, 320), Pow(Integer(480351), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 64), Pow(Integer(19255), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(1, 320), Pow(Integer(480351), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 320), Pow(Integer(480351), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 64), Pow(Integer(19255), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 64), Pow(Integer(19255), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 64), Pow(Integer(19255), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 320), Pow(Integer(480351), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_167(y:sympy.Rational):
	#((y >= sqrt(4240239)/2560) | (y > -sqrt(172231)/512)) & ((y >= sqrt(4240239)/2560) | (y < -sqrt(4240239)/2560)) & ((y <= sqrt(172231)/512) | (y > -sqrt(172231)/512)) & ((y <= sqrt(172231)/512) | (y < -sqrt(4240239)/2560))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(1, 2560), Pow(Integer(4240239), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 512), Pow(Integer(172231), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(1, 2560), Pow(Integer(4240239), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2560), Pow(Integer(4240239), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 512), Pow(Integer(172231), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 512), Pow(Integer(172231), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 512), Pow(Integer(172231), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2560), Pow(Integer(4240239), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_168(y:sympy.Rational):
	#((y >= sqrt(1910679)/640) | (y > -sqrt(76591)/128)) & ((y >= sqrt(1910679)/640) | (y < -sqrt(1910679)/640)) & ((y <= sqrt(76591)/128) | (y > -sqrt(76591)/128)) & ((y <= sqrt(76591)/128) | (y < -sqrt(1910679)/640))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(1, 640), Pow(Integer(1910679), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 128), Pow(Integer(76591), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(1, 640), Pow(Integer(1910679), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 640), Pow(Integer(1910679), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 128), Pow(Integer(76591), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 128), Pow(Integer(76591), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 128), Pow(Integer(76591), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 640), Pow(Integer(1910679), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_169(y:sympy.Rational):
	#((y >= sqrt(476751)/320) | (y > -sqrt(19111)/64)) & ((y >= sqrt(476751)/320) | (y < -sqrt(476751)/320)) & ((y <= sqrt(19111)/64) | (y > -sqrt(19111)/64)) & ((y <= sqrt(19111)/64) | (y < -sqrt(476751)/320))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(1, 320), Pow(Integer(476751), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 64), Pow(Integer(19111), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(1, 320), Pow(Integer(476751), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 320), Pow(Integer(476751), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 64), Pow(Integer(19111), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 64), Pow(Integer(19111), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 64), Pow(Integer(19111), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 320), Pow(Integer(476751), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_170(y:sympy.Rational):
	#((y >= sqrt(3811839)/2560) | (y > -sqrt(155095)/512)) & ((y >= sqrt(3811839)/2560) | (y < -sqrt(3811839)/2560)) & ((y <= sqrt(155095)/512) | (y > -sqrt(155095)/512)) & ((y <= sqrt(155095)/512) | (y < -sqrt(3811839)/2560))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(1, 2560), Pow(Integer(3811839), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 512), Pow(Integer(155095), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(1, 2560), Pow(Integer(3811839), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2560), Pow(Integer(3811839), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 512), Pow(Integer(155095), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 512), Pow(Integer(155095), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 512), Pow(Integer(155095), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2560), Pow(Integer(3811839), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_171(y:sympy.Rational):
	#((y >= sqrt(966391)/1280) | (y > -sqrt(39311)/256)) & ((y >= sqrt(966391)/1280) | (y < -sqrt(966391)/1280)) & ((y <= sqrt(39311)/256) | (y > -sqrt(39311)/256)) & ((y <= sqrt(39311)/256) | (y < -sqrt(966391)/1280))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(1, 1280), Pow(Integer(966391), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 256), Pow(Integer(39311), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(1, 1280), Pow(Integer(966391), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1280), Pow(Integer(966391), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 256), Pow(Integer(39311), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 256), Pow(Integer(39311), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 256), Pow(Integer(39311), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1280), Pow(Integer(966391), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_172(y:sympy.Rational):
	#((y >= sqrt(1917879)/640) | (y > -sqrt(76879)/128)) & ((y >= sqrt(1917879)/640) | (y < -sqrt(1917879)/640)) & ((y <= sqrt(76879)/128) | (y > -sqrt(76879)/128)) & ((y <= sqrt(76879)/128) | (y < -sqrt(1917879)/640))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(1, 640), Pow(Integer(1917879), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 128), Pow(Integer(76879), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(1, 640), Pow(Integer(1917879), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 640), Pow(Integer(1917879), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 128), Pow(Integer(76879), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 128), Pow(Integer(76879), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 128), Pow(Integer(76879), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 640), Pow(Integer(1917879), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_173(y:sympy.Rational):
	#((y >= sqrt(234879)/640) | (y > -11*sqrt(79)/128)) & ((y >= sqrt(234879)/640) | (y < -sqrt(234879)/640)) & ((y <= 11*sqrt(79)/128) | (y > -11*sqrt(79)/128)) & ((y <= 11*sqrt(79)/128) | (y < -sqrt(234879)/640))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(1, 640), Pow(Integer(234879), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(11, 128), Pow(Integer(79), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(1, 640), Pow(Integer(234879), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 640), Pow(Integer(234879), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(11, 128), Pow(Integer(79), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(11, 128), Pow(Integer(79), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(11, 128), Pow(Integer(79), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 640), Pow(Integer(234879), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_174(y:sympy.Rational):
	#((y >= sqrt(1944679)/640) | (y > -sqrt(77951)/128)) & ((y >= sqrt(1944679)/640) | (y < -sqrt(1944679)/640)) & ((y <= sqrt(77951)/128) | (y > -sqrt(77951)/128)) & ((y <= sqrt(77951)/128) | (y < -sqrt(1944679)/640))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(1, 640), Pow(Integer(1944679), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 128), Pow(Integer(77951), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(1, 640), Pow(Integer(1944679), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 640), Pow(Integer(1944679), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 128), Pow(Integer(77951), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 128), Pow(Integer(77951), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 128), Pow(Integer(77951), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 640), Pow(Integer(1944679), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_175(y:sympy.Rational):
	#((y >= sqrt(3704239)/2560) | (y > -sqrt(150791)/512)) & ((y >= sqrt(3704239)/2560) | (y < -sqrt(3704239)/2560)) & ((y <= sqrt(150791)/512) | (y > -sqrt(150791)/512)) & ((y <= sqrt(150791)/512) | (y < -sqrt(3704239)/2560))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(1, 2560), Pow(Integer(3704239), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 512), Pow(Integer(150791), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(1, 2560), Pow(Integer(3704239), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2560), Pow(Integer(3704239), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 512), Pow(Integer(150791), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 512), Pow(Integer(150791), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 512), Pow(Integer(150791), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2560), Pow(Integer(3704239), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_176(y:sympy.Rational):
	#((y >= sqrt(1924879)/640) | (y > -sqrt(77159)/128)) & ((y >= sqrt(1924879)/640) | (y < -sqrt(1924879)/640)) & ((y <= sqrt(77159)/128) | (y > -sqrt(77159)/128)) & ((y <= sqrt(77159)/128) | (y < -sqrt(1924879)/640))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(1, 640), Pow(Integer(1924879), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 128), Pow(Integer(77159), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(1, 640), Pow(Integer(1924879), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 640), Pow(Integer(1924879), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 128), Pow(Integer(77159), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 128), Pow(Integer(77159), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 128), Pow(Integer(77159), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 640), Pow(Integer(1924879), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_177(y:sympy.Rational):
	#((y >= sqrt(483751)/320) | (y > -sqrt(19391)/64)) & ((y >= sqrt(483751)/320) | (y < -sqrt(483751)/320)) & ((y <= sqrt(19391)/64) | (y > -sqrt(19391)/64)) & ((y <= sqrt(19391)/64) | (y < -sqrt(483751)/320))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(1, 320), Pow(Integer(483751), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 64), Pow(Integer(19391), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(1, 320), Pow(Integer(483751), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 320), Pow(Integer(483751), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 64), Pow(Integer(19391), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 64), Pow(Integer(19391), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 64), Pow(Integer(19391), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 320), Pow(Integer(483751), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_178(y:sympy.Rational):
	#((y >= 3*sqrt(435471)/2560) | (y > -sqrt(159391)/512)) & ((y >= 3*sqrt(435471)/2560) | (y < -3*sqrt(435471)/2560)) & ((y <= sqrt(159391)/512) | (y > -sqrt(159391)/512)) & ((y <= sqrt(159391)/512) | (y < -3*sqrt(435471)/2560))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(3, 2560), Pow(Integer(435471), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 512), Pow(Integer(159391), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(3, 2560), Pow(Integer(435471), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(3, 2560), Pow(Integer(435471), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 512), Pow(Integer(159391), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 512), Pow(Integer(159391), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 512), Pow(Integer(159391), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(3, 2560), Pow(Integer(435471), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_179(y:sympy.Rational):
	#((y >= sqrt(383239)/2560) | (y > -sqrt(17951)/512)) & ((y >= sqrt(383239)/2560) | (y < -sqrt(383239)/2560)) & ((y <= sqrt(17951)/512) | (y > -sqrt(17951)/512)) & ((y <= sqrt(17951)/512) | (y < -sqrt(383239)/2560))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(1, 2560), Pow(Integer(383239), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 512), Pow(Integer(17951), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(1, 2560), Pow(Integer(383239), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2560), Pow(Integer(383239), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 512), Pow(Integer(17951), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 512), Pow(Integer(17951), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 512), Pow(Integer(17951), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2560), Pow(Integer(383239), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_180(y:sympy.Rational):
	#((y >= 3*sqrt(214631)/640) | (y > -sqrt(77431)/128)) & ((y >= 3*sqrt(214631)/640) | (y < -3*sqrt(214631)/640)) & ((y <= sqrt(77431)/128) | (y > -sqrt(77431)/128)) & ((y <= sqrt(77431)/128) | (y < -3*sqrt(214631)/640))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(3, 640), Pow(Integer(214631), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 128), Pow(Integer(77431), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(3, 640), Pow(Integer(214631), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(3, 640), Pow(Integer(214631), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 128), Pow(Integer(77431), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 128), Pow(Integer(77431), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 128), Pow(Integer(77431), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(3, 640), Pow(Integer(214631), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_181(y:sympy.Rational):
	#((y >= 7*sqrt(271)/640) | (y > -sqrt(695)/128)) & ((y >= 7*sqrt(271)/640) | (y < -7*sqrt(271)/640)) & ((y <= sqrt(695)/128) | (y > -sqrt(695)/128)) & ((y <= sqrt(695)/128) | (y < -7*sqrt(271)/640))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(7, 640), Pow(Integer(271), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 128), Pow(Integer(695), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(7, 640), Pow(Integer(271), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(7, 640), Pow(Integer(271), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 128), Pow(Integer(695), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 128), Pow(Integer(695), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 128), Pow(Integer(695), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(7, 640), Pow(Integer(271), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_182(y:sympy.Rational):
	#((y >= sqrt(474)/10) | (y > -sqrt(19)/2)) & ((y >= sqrt(474)/10) | (y < -sqrt(474)/10)) & ((y <= sqrt(19)/2) | (y > -sqrt(19)/2)) & ((y <= sqrt(19)/2) | (y < -sqrt(474)/10))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(1, 10), Pow(Integer(474), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2), Pow(Integer(19), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(1, 10), Pow(Integer(474), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 10), Pow(Integer(474), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 2), Pow(Integer(19), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2), Pow(Integer(19), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 2), Pow(Integer(19), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 10), Pow(Integer(474), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_183(y:sympy.Rational):
	#((y >= sqrt(13951)/320) | (y > -sqrt(599)/64)) & ((y >= sqrt(13951)/320) | (y < -sqrt(13951)/320)) & ((y <= sqrt(599)/64) | (y > -sqrt(599)/64)) & ((y <= sqrt(599)/64) | (y < -sqrt(13951)/320))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(1, 320), Pow(Integer(13951), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 64), Pow(Integer(599), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(1, 320), Pow(Integer(13951), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 320), Pow(Integer(13951), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 64), Pow(Integer(599), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 64), Pow(Integer(599), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 64), Pow(Integer(599), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 320), Pow(Integer(13951), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_184(y:sympy.Rational):
	#((y >= sqrt(1938279)/640) | (y > -sqrt(77695)/128)) & ((y >= sqrt(1938279)/640) | (y < -sqrt(1938279)/640)) & ((y <= sqrt(77695)/128) | (y > -sqrt(77695)/128)) & ((y <= sqrt(77695)/128) | (y < -sqrt(1938279)/640))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(1, 640), Pow(Integer(1938279), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 128), Pow(Integer(77695), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(1, 640), Pow(Integer(1938279), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 640), Pow(Integer(1938279), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 128), Pow(Integer(77695), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 128), Pow(Integer(77695), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 128), Pow(Integer(77695), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 640), Pow(Integer(1938279), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_185(y:sympy.Rational):
	#((y >= 9*sqrt(1919)/2560) | (y > -sqrt(8839)/512)) & ((y >= 9*sqrt(1919)/2560) | (y < -9*sqrt(1919)/2560)) & ((y <= sqrt(8839)/512) | (y > -sqrt(8839)/512)) & ((y <= sqrt(8839)/512) | (y < -9*sqrt(1919)/2560))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(9, 2560), Pow(Integer(1919), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 512), Pow(Integer(8839), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(9, 2560), Pow(Integer(1919), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(9, 2560), Pow(Integer(1919), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 512), Pow(Integer(8839), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 512), Pow(Integer(8839), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 512), Pow(Integer(8839), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(9, 2560), Pow(Integer(1919), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_186(y:sympy.Rational):
	#((y >= sqrt(1950879)/640) | (y > -sqrt(78199)/128)) & ((y >= sqrt(1950879)/640) | (y < -sqrt(1950879)/640)) & ((y <= sqrt(78199)/128) | (y > -sqrt(78199)/128)) & ((y <= sqrt(78199)/128) | (y < -sqrt(1950879)/640))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(1, 640), Pow(Integer(1950879), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 128), Pow(Integer(78199), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(1, 640), Pow(Integer(1950879), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 640), Pow(Integer(1950879), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 128), Pow(Integer(78199), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 128), Pow(Integer(78199), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 128), Pow(Integer(78199), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 640), Pow(Integer(1950879), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_187(y:sympy.Rational):
	#((y >= sqrt(122119)/160) | (y > -sqrt(4895)/32)) & ((y >= sqrt(122119)/160) | (y < -sqrt(122119)/160)) & ((y <= sqrt(4895)/32) | (y > -sqrt(4895)/32)) & ((y <= sqrt(4895)/32) | (y < -sqrt(122119)/160))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(1, 160), Pow(Integer(122119), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 32), Pow(Integer(4895), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(1, 160), Pow(Integer(122119), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 160), Pow(Integer(122119), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 32), Pow(Integer(4895), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 32), Pow(Integer(4895), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 32), Pow(Integer(4895), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 160), Pow(Integer(122119), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_188(y:sympy.Rational):
	#((y >= 9*sqrt(24159)/640) | (y > -sqrt(78439)/128)) & ((y >= 9*sqrt(24159)/640) | (y < -9*sqrt(24159)/640)) & ((y <= sqrt(78439)/128) | (y > -sqrt(78439)/128)) & ((y <= sqrt(78439)/128) | (y < -9*sqrt(24159)/640))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(9, 640), Pow(Integer(24159), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 128), Pow(Integer(78439), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(9, 640), Pow(Integer(24159), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(9, 640), Pow(Integer(24159), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 128), Pow(Integer(78439), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 128), Pow(Integer(78439), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 128), Pow(Integer(78439), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(9, 640), Pow(Integer(24159), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_189(y:sympy.Rational):
	#((y >= sqrt(269439)/2560) | (y > -sqrt(13399)/512)) & ((y >= sqrt(269439)/2560) | (y < -sqrt(269439)/2560)) & ((y <= sqrt(13399)/512) | (y > -sqrt(13399)/512)) & ((y <= sqrt(13399)/512) | (y < -sqrt(269439)/2560))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(1, 2560), Pow(Integer(269439), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 512), Pow(Integer(13399), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(1, 2560), Pow(Integer(269439), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2560), Pow(Integer(269439), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 512), Pow(Integer(13399), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 512), Pow(Integer(13399), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 512), Pow(Integer(13399), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2560), Pow(Integer(269439), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_190(y:sympy.Rational):
	#((y >= sqrt(486951)/320) | (y > -sqrt(19519)/64)) & ((y >= sqrt(486951)/320) | (y < -sqrt(486951)/320)) & ((y <= sqrt(19519)/64) | (y > -sqrt(19519)/64)) & ((y <= sqrt(19519)/64) | (y < -sqrt(486951)/320))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(1, 320), Pow(Integer(486951), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 64), Pow(Integer(19519), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(1, 320), Pow(Integer(486951), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 320), Pow(Integer(486951), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 64), Pow(Integer(19519), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 64), Pow(Integer(19519), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 64), Pow(Integer(19519), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 320), Pow(Integer(486951), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_191(y:sympy.Rational):
	#((y >= sqrt(468951)/320) | (y > -sqrt(18799)/64)) & ((y >= sqrt(468951)/320) | (y < -sqrt(468951)/320)) & ((y <= sqrt(18799)/64) | (y > -sqrt(18799)/64)) & ((y <= sqrt(18799)/64) | (y < -sqrt(468951)/320))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(1, 320), Pow(Integer(468951), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 64), Pow(Integer(18799), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(1, 320), Pow(Integer(468951), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 320), Pow(Integer(468951), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 64), Pow(Integer(18799), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 64), Pow(Integer(18799), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 64), Pow(Integer(18799), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 320), Pow(Integer(468951), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_192(y:sympy.Rational):
	#((y >= sqrt(81591)/1280) | (y > -sqrt(3919)/256)) & ((y >= sqrt(81591)/1280) | (y < -sqrt(81591)/1280)) & ((y <= sqrt(3919)/256) | (y > -sqrt(3919)/256)) & ((y <= sqrt(3919)/256) | (y < -sqrt(81591)/1280))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(1, 1280), Pow(Integer(81591), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 256), Pow(Integer(3919), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(1, 1280), Pow(Integer(81591), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1280), Pow(Integer(81591), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 256), Pow(Integer(3919), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 256), Pow(Integer(3919), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 256), Pow(Integer(3919), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1280), Pow(Integer(81591), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_193(y:sympy.Rational):
	#((y >= sqrt(610239)/2560) | (y > -sqrt(27031)/512)) & ((y >= sqrt(610239)/2560) | (y < -sqrt(610239)/2560)) & ((y <= sqrt(27031)/512) | (y > -sqrt(27031)/512)) & ((y <= sqrt(27031)/512) | (y < -sqrt(610239)/2560))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(1, 2560), Pow(Integer(610239), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 512), Pow(Integer(27031), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(1, 2560), Pow(Integer(610239), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2560), Pow(Integer(610239), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 512), Pow(Integer(27031), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 512), Pow(Integer(27031), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 512), Pow(Integer(27031), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2560), Pow(Integer(610239), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_194(y:sympy.Rational):
	#((y >= sqrt(7444591)/1280) | (y > -sqrt(298439)/256)) & ((y >= sqrt(7444591)/1280) | (y < -sqrt(7444591)/1280)) & ((y <= sqrt(298439)/256) | (y > -sqrt(298439)/256)) & ((y <= sqrt(298439)/256) | (y < -sqrt(7444591)/1280))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(1, 1280), Pow(Integer(7444591), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 256), Pow(Integer(298439), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(1, 1280), Pow(Integer(7444591), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1280), Pow(Integer(7444591), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 256), Pow(Integer(298439), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 256), Pow(Integer(298439), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 256), Pow(Integer(298439), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1280), Pow(Integer(7444591), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_195(y:sympy.Rational):
	#((y >= sqrt(307591)/1280) | (y > -sqrt(12959)/256)) & ((y >= sqrt(307591)/1280) | (y < -sqrt(307591)/1280)) & ((y <= sqrt(12959)/256) | (y > -sqrt(12959)/256)) & ((y <= sqrt(12959)/256) | (y < -sqrt(307591)/1280))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(1, 1280), Pow(Integer(307591), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 256), Pow(Integer(12959), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(1, 1280), Pow(Integer(307591), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1280), Pow(Integer(307591), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 256), Pow(Integer(12959), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 256), Pow(Integer(12959), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 256), Pow(Integer(12959), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1280), Pow(Integer(307591), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_196(y:sympy.Rational):
	#((y >= sqrt(496839)/2560) | (y > -sqrt(22495)/512)) & ((y >= sqrt(496839)/2560) | (y < -sqrt(496839)/2560)) & ((y <= sqrt(22495)/512) | (y > -sqrt(22495)/512)) & ((y <= sqrt(22495)/512) | (y < -sqrt(496839)/2560))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(1, 2560), Pow(Integer(496839), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 512), Pow(Integer(22495), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(1, 2560), Pow(Integer(496839), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2560), Pow(Integer(496839), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 512), Pow(Integer(22495), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 512), Pow(Integer(22495), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 512), Pow(Integer(22495), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2560), Pow(Integer(496839), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_197(y:sympy.Rational):
	#((y >= 3*sqrt(191)/160) | (y > -sqrt(79)/32)) & ((y >= 3*sqrt(191)/160) | (y < -3*sqrt(191)/160)) & ((y <= sqrt(79)/32) | (y > -sqrt(79)/32)) & ((y <= sqrt(79)/32) | (y < -3*sqrt(191)/160))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(3, 160), Pow(Integer(191), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 32), Pow(Integer(79), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(3, 160), Pow(Integer(191), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(3, 160), Pow(Integer(191), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 32), Pow(Integer(79), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 32), Pow(Integer(79), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 32), Pow(Integer(79), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(3, 160), Pow(Integer(191), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_198(y:sympy.Rational):
	#((y >= sqrt(116719)/160) | (y > -sqrt(4679)/32)) & ((y >= sqrt(116719)/160) | (y < -sqrt(116719)/160)) & ((y <= sqrt(4679)/32) | (y > -sqrt(4679)/32)) & ((y <= sqrt(4679)/32) | (y < -sqrt(116719)/160))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(1, 160), Pow(Integer(116719), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 32), Pow(Integer(4679), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(1, 160), Pow(Integer(116719), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 160), Pow(Integer(116719), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 32), Pow(Integer(4679), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 32), Pow(Integer(4679), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 32), Pow(Integer(4679), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 160), Pow(Integer(116719), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_199(y:sympy.Rational):
	#((y >= 33*sqrt(1711)/640) | (y > -sqrt(74695)/128)) & ((y >= 33*sqrt(1711)/640) | (y < -33*sqrt(1711)/640)) & ((y <= sqrt(74695)/128) | (y > -sqrt(74695)/128)) & ((y <= sqrt(74695)/128) | (y < -33*sqrt(1711)/640))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(33, 640), Pow(Integer(1711), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 128), Pow(Integer(74695), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(33, 640), Pow(Integer(1711), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(33, 640), Pow(Integer(1711), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 128), Pow(Integer(74695), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 128), Pow(Integer(74695), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 128), Pow(Integer(74695), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(33, 640), Pow(Integer(1711), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_200(y:sympy.Rational):
	#((y >= sqrt(138391)/1280) | (y > -sqrt(6191)/256)) & ((y >= sqrt(138391)/1280) | (y < -sqrt(138391)/1280)) & ((y <= sqrt(6191)/256) | (y > -sqrt(6191)/256)) & ((y <= sqrt(6191)/256) | (y < -sqrt(138391)/1280))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(1, 1280), Pow(Integer(138391), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 256), Pow(Integer(6191), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(1, 1280), Pow(Integer(138391), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1280), Pow(Integer(138391), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 256), Pow(Integer(6191), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 256), Pow(Integer(6191), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 256), Pow(Integer(6191), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1280), Pow(Integer(138391), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_201(y:sympy.Rational):
	#((y >= sqrt(1871679)/640) | (y > -sqrt(75031)/128)) & ((y >= sqrt(1871679)/640) | (y < -sqrt(1871679)/640)) & ((y <= sqrt(75031)/128) | (y > -sqrt(75031)/128)) & ((y <= sqrt(75031)/128) | (y < -sqrt(1871679)/640))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(1, 640), Pow(Integer(1871679), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 128), Pow(Integer(75031), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(1, 640), Pow(Integer(1871679), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 640), Pow(Integer(1871679), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 128), Pow(Integer(75031), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 128), Pow(Integer(75031), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 128), Pow(Integer(75031), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 640), Pow(Integer(1871679), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_202(y:sympy.Rational):
	#((y >= sqrt(1398439)/2560) | (y > -sqrt(58559)/512)) & ((y >= sqrt(1398439)/2560) | (y < -sqrt(1398439)/2560)) & ((y <= sqrt(58559)/512) | (y > -sqrt(58559)/512)) & ((y <= sqrt(58559)/512) | (y < -sqrt(1398439)/2560))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(1, 2560), Pow(Integer(1398439), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 512), Pow(Integer(58559), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(1, 2560), Pow(Integer(1398439), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2560), Pow(Integer(1398439), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 512), Pow(Integer(58559), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 512), Pow(Integer(58559), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 512), Pow(Integer(58559), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2560), Pow(Integer(1398439), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_203(y:sympy.Rational):
	#((y >= sqrt(723439)/2560) | (y > -sqrt(31559)/512)) & ((y >= sqrt(723439)/2560) | (y < -sqrt(723439)/2560)) & ((y <= sqrt(31559)/512) | (y > -sqrt(31559)/512)) & ((y <= sqrt(31559)/512) | (y < -sqrt(723439)/2560))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(1, 2560), Pow(Integer(723439), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 512), Pow(Integer(31559), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(1, 2560), Pow(Integer(723439), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2560), Pow(Integer(723439), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 512), Pow(Integer(31559), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 512), Pow(Integer(31559), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 512), Pow(Integer(31559), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2560), Pow(Integer(723439), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_204(y:sympy.Rational):
	#((y >= sqrt(7478391)/1280) | (y > -sqrt(299791)/256)) & ((y >= sqrt(7478391)/1280) | (y < -sqrt(7478391)/1280)) & ((y <= sqrt(299791)/256) | (y > -sqrt(299791)/256)) & ((y <= sqrt(299791)/256) | (y < -sqrt(7478391)/1280))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(1, 1280), Pow(Integer(7478391), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 256), Pow(Integer(299791), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(1, 1280), Pow(Integer(7478391), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1280), Pow(Integer(7478391), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 256), Pow(Integer(299791), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 256), Pow(Integer(299791), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 256), Pow(Integer(299791), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 1280), Pow(Integer(7478391), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_205(y:sympy.Rational):
	#((y >= sqrt(1510239)/2560) | (y > -sqrt(63031)/512)) & ((y >= sqrt(1510239)/2560) | (y < -sqrt(1510239)/2560)) & ((y <= sqrt(63031)/512) | (y > -sqrt(63031)/512)) & ((y <= sqrt(63031)/512) | (y < -sqrt(1510239)/2560))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(1, 2560), Pow(Integer(1510239), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 512), Pow(Integer(63031), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(1, 2560), Pow(Integer(1510239), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2560), Pow(Integer(1510239), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 512), Pow(Integer(63031), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 512), Pow(Integer(63031), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 512), Pow(Integer(63031), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2560), Pow(Integer(1510239), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_206(y:sympy.Rational):
	#((y >= sqrt(836439)/2560) | (y > -sqrt(36079)/512)) & ((y >= sqrt(836439)/2560) | (y < -sqrt(836439)/2560)) & ((y <= sqrt(36079)/512) | (y > -sqrt(36079)/512)) & ((y <= sqrt(36079)/512) | (y < -sqrt(836439)/2560))

	pre_cond = And(Or(GreaterThan(Symbol('y'), Mul(Rational(1, 2560), Pow(Integer(836439), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 512), Pow(Integer(36079), Rational(1, 2))))), Or(GreaterThan(Symbol('y'), Mul(Rational(1, 2560), Pow(Integer(836439), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2560), Pow(Integer(836439), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 512), Pow(Integer(36079), Rational(1, 2)))), StrictGreaterThan(Symbol('y'), Mul(Integer(-1), Rational(1, 512), Pow(Integer(36079), Rational(1, 2))))), Or(LessThan(Symbol('y'), Mul(Rational(1, 512), Pow(Integer(36079), Rational(1, 2)))), StrictLessThan(Symbol('y'), Mul(Integer(-1), Rational(1, 2560), Pow(Integer(836439), Rational(1, 2))))))

	eval = pre_cond.subs( { 'y':y })

	if eval==True:
		assert eval!=False
		return True
	return False


def post_condition(y:sympy.Rational, x:sympy.Rational):
	# (0 >= x**2 + y**2 - 5) & (0 >= -x**2 - y**2 + 499/100)

	post_cond =  And(GreaterThan(Integer(0), Add(Pow(Symbol('x'), Integer(2)), Pow(Symbol('y'), Integer(2)), Integer(-5))), GreaterThan(Integer(0), Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Rational(499, 100))))

	eval = post_cond.subs( { 'y':y, 'x':x })

	return eval == sympy.logic.boolalg.BooleanTrue





if __name__=="__main__":
	
	ip_0=int(input("enter integer numerator of y:\n"))
	ip_1=int(input("enter integer denominator of y:\n"))
	assert(ip_1!=0), ("Error denominator entered is 0")
	y=sympy.Rational(ip_0,ip_1)
	
	
	
	
	if pre_condition_0(y=y)==True:
		print("pre_condition_0 SAT")
		print('x = 1/8')
		print('y = 571/256')
		exit(0)
	
	
	if pre_condition_1(y=y)==True:
		print("pre_condition_1 SAT")
		print('x = 571/256')
		print('y = 1/8')
		exit(0)
	
	
	if pre_condition_2(y=y)==True:
		print("pre_condition_2 SAT")
		print('x = 255/256')
		print('y = 2')
		exit(0)
	
	
	if pre_condition_3(y=y)==True:
		print("pre_condition_3 SAT")
		print('x = 89/128')
		print('y = 17/8')
		exit(0)
	
	
	if pre_condition_4(y=y)==True:
		print("pre_condition_4 SAT")
		print('x = 55/64')
		print('y = 33/16')
		exit(0)
	
	
	if pre_condition_5(y=y)==True:
		print("pre_condition_5 SAT")
		print('x = 1023/512')
		print('y = -1')
		exit(0)
	
	
	if pre_condition_6(y=y)==True:
		print("pre_condition_6 SAT")
		print('x = 119/128')
		print('y = 65/32')
		exit(0)
	
	
	if pre_condition_7(y=y)==True:
		print("pre_condition_7 SAT")
		print('x = 115/128')
		print('y = 131/64')
		exit(0)
	
	
	if pre_condition_8(y=y)==True:
		print("pre_condition_8 SAT")
		print('x = 143/64')
		print('y = 1/16')
		exit(0)
	
	
	if pre_condition_9(y=y)==True:
		print("pre_condition_9 SAT")
		print('x = 1143/512')
		print('y = 3/32')
		exit(0)
	
	
	if pre_condition_10(y=y)==True:
		print("pre_condition_10 SAT")
		print('x = 1115/512')
		print('y = -1/2')
		exit(0)
	
	
	if pre_condition_11(y=y)==True:
		print("pre_condition_11 SAT")
		print('x = 539/256')
		print('y = -3/4')
		exit(0)
	
	
	if pre_condition_12(y=y)==True:
		print("pre_condition_12 SAT")
		print('x = 1053/512')
		print('y = -7/8')
		exit(0)
	
	
	if pre_condition_13(y=y)==True:
		print("pre_condition_13 SAT")
		print('x = 1039/512')
		print('y = -15/16')
		exit(0)
	
	
	if pre_condition_14(y=y)==True:
		print("pre_condition_14 SAT")
		print('x = 117/128')
		print('y = 261/128')
		exit(0)
	
	
	if pre_condition_15(y=y)==True:
		print("pre_condition_15 SAT")
		print('x = 1099/512')
		print('y = -5/8')
		exit(0)
	
	
	if pre_condition_16(y=y)==True:
		print("pre_condition_16 SAT")
		print('x = 1089/512')
		print('y = -11/16')
		exit(0)
	
	
	if pre_condition_17(y=y)==True:
		print("pre_condition_17 SAT")
		print('x = 271/128')
		print('y = -23/32')
		exit(0)
	
	
	if pre_condition_18(y=y)==True:
		print("pre_condition_18 SAT")
		print('x = 1031/512')
		print('y = -31/32')
		exit(0)
	
	
	if pre_condition_19(y=y)==True:
		print("pre_condition_19 SAT")
		print('x = 225/256')
		print('y = 263/128')
		exit(0)
	
	
	if pre_condition_20(y=y)==True:
		print("pre_condition_20 SAT")
		print('x = 59/64')
		print('y = 521/256')
		exit(0)
	
	
	if pre_condition_21(y=y)==True:
		print("pre_condition_21 SAT")
		print('x = 543/256')
		print('y = -45/64')
		exit(0)
	
	
	if pre_condition_22(y=y)==True:
		print("pre_condition_22 SAT")
		print('x = 1035/512')
		print('y = -61/64')
		exit(0)
	
	
	if pre_condition_23(y=y)==True:
		print("pre_condition_23 SAT")
		print('x = 547/256')
		print('y = -21/32')
		exit(0)
	
	
	if pre_condition_24(y=y)==True:
		print("pre_condition_24 SAT")
		print('x = 223/256')
		print('y = 527/256')
		exit(0)
	
	
	if pre_condition_25(y=y)==True:
		print("pre_condition_25 SAT")
		print('x = 237/256')
		print('y = 2083/1024')
		exit(0)
	
	
	if pre_condition_26(y=y)==True:
		print("pre_condition_26 SAT")
		print('x = 137/64')
		print('y = -41/64')
		exit(0)
	
	
	if pre_condition_27(y=y)==True:
		print("pre_condition_27 SAT")
		print('x = 1033/512')
		print('y = -123/128')
		exit(0)
	
	
	if pre_condition_28(y=y)==True:
		print("pre_condition_28 SAT")
		print('x = 235/256')
		print('y = 2087/1024')
		exit(0)
	
	
	if pre_condition_29(y=y)==True:
		print("pre_condition_29 SAT")
		print('x = 1085/512')
		print('y = -91/128')
		exit(0)
	
	
	if pre_condition_30(y=y)==True:
		print("pre_condition_30 SAT")
		print('x = 29/32')
		print('y = 523/256')
		exit(0)
	
	
	if pre_condition_31(y=y)==True:
		print("pre_condition_31 SAT")
		print('x = 7/8')
		print('y = 1053/512')
		exit(0)
	
	
	if pre_condition_32(y=y)==True:
		print("pre_condition_32 SAT")
		print('x = 233/256')
		print('y = 8359/4096')
		exit(0)
	
	
	if pre_condition_33(y=y)==True:
		print("pre_condition_33 SAT")
		print('x = 231/256')
		print('y = 1047/512')
		exit(0)
	
	
	if pre_condition_34(y=y)==True:
		print("pre_condition_34 SAT")
		print('x = 25/32')
		print('y = 67/32')
		exit(0)
	
	
	if pre_condition_35(y=y)==True:
		print("pre_condition_35 SAT")
		print('x = 517/256')
		print('y = -245/256')
		exit(0)
	
	
	if pre_condition_36(y=y)==True:
		print("pre_condition_36 SAT")
		print('x = 111/128')
		print('y = 1055/512')
		exit(0)
	
	
	if pre_condition_37(y=y)==True:
		print("pre_condition_37 SAT")
		print('x = 129/64')
		print('y = -247/256')
		exit(0)
	
	
	if pre_condition_38(y=y)==True:
		print("pre_condition_38 SAT")
		print('x = 221/256')
		print('y = 2111/1024')
		exit(0)
	
	
	if pre_condition_39(y=y)==True:
		print("pre_condition_39 SAT")
		print('x = 57/64')
		print('y = 525/256')
		exit(0)
	
	
	if pre_condition_40(y=y)==True:
		print("pre_condition_40 SAT")
		print('x = 229/256')
		print('y = 2097/1024')
		exit(0)
	
	
	if pre_condition_41(y=y)==True:
		print("pre_condition_41 SAT")
		print('x = 105/128')
		print('y = 133/64')
		exit(0)
	
	
	if pre_condition_42(y=y)==True:
		print("pre_condition_42 SAT")
		print('x = 103/128')
		print('y = 267/128')
		exit(0)
	
	
	if pre_condition_43(y=y)==True:
		print("pre_condition_43 SAT")
		print('x = 1037/512')
		print('y = -121/128')
		exit(0)
	
	
	if pre_condition_44(y=y)==True:
		print("pre_condition_44 SAT")
		print('x = 113/128')
		print('y = 1051/512')
		exit(0)
	
	
	if pre_condition_45(y=y)==True:
		print("pre_condition_45 SAT")
		print('x = 13/16')
		print('y = 533/256')
		exit(0)
	
	
	if pre_condition_46(y=y)==True:
		print("pre_condition_46 SAT")
		print('x = 259/128')
		print('y = -243/256')
		exit(0)
	
	
	if pre_condition_47(y=y)==True:
		print("pre_condition_47 SAT")
		print('x = 227/256')
		print('y = 2101/1024')
		exit(0)
	
	
	if pre_condition_48(y=y)==True:
		print("pre_condition_48 SAT")
		print('x = 247/256')
		print('y = 129/64')
		exit(0)
	
	
	if pre_condition_49(y=y)==True:
		print("pre_condition_49 SAT")
		print('x = 243/256')
		print('y = 259/128')
		exit(0)
	
	
	if pre_condition_50(y=y)==True:
		print("pre_condition_50 SAT")
		print('x = 1091/512')
		print('y = -43/64')
		exit(0)
	
	
	if pre_condition_51(y=y)==True:
		print("pre_condition_51 SAT")
		print('x = 519/256')
		print('y = -241/256')
		exit(0)
	
	
	if pre_condition_52(y=y)==True:
		print("pre_condition_52 SAT")
		print('x = 17/8')
		print('y = -89/128')
		exit(0)
	
	
	if pre_condition_53(y=y)==True:
		print("pre_condition_53 SAT")
		print('x = 545/256')
		print('y = -87/128')
		exit(0)
	
	
	if pre_condition_54(y=y)==True:
		print("pre_condition_54 SAT")
		print('x = -1087/512')
		print('y = -179/256')
		exit(0)
	
	
	if pre_condition_55(y=y)==True:
		print("pre_condition_55 SAT")
		print('x = 207/256')
		print('y = 4267/2048')
		exit(0)
	
	
	if pre_condition_56(y=y)==True:
		print("pre_condition_56 SAT")
		print('x = 245/256')
		print('y = 517/256')
		exit(0)
	
	
	if pre_condition_57(y=y)==True:
		print("pre_condition_57 SAT")
		print('x = -1081/512')
		print('y = -47/64')
		exit(0)
	
	
	if pre_condition_58(y=y)==True:
		print("pre_condition_58 SAT")
		print('x = 523/256')
		print('y = -29/32')
		exit(0)
	
	
	if pre_condition_59(y=y)==True:
		print("pre_condition_59 SAT")
		print('x = 209/256')
		print('y = 4261/2048')
		exit(0)
	
	
	if pre_condition_60(y=y)==True:
		print("pre_condition_60 SAT")
		print('x = 521/256')
		print('y = -59/64')
		exit(0)
	
	
	if pre_condition_61(y=y)==True:
		print("pre_condition_61 SAT")
		print('x = 549/256')
		print('y = -81/128')
		exit(0)
	
	
	if pre_condition_62(y=y)==True:
		print("pre_condition_62 SAT")
		print('x = 261/128')
		print('y = -117/128')
		exit(0)
	
	
	if pre_condition_63(y=y)==True:
		print("pre_condition_63 SAT")
		print('x = 101/128')
		print('y = 535/256')
		exit(0)
	
	
	if pre_condition_64(y=y)==True:
		print("pre_condition_64 SAT")
		print('x = 123/128')
		print('y = 1033/512')
		exit(0)
	
	
	if pre_condition_65(y=y)==True:
		print("pre_condition_65 SAT")
		print('x = 201/256')
		print('y = 4285/2048')
		exit(0)
	
	
	if pre_condition_66(y=y)==True:
		print("pre_condition_66 SAT")
		print('x = 1043/512')
		print('y = -235/256')
		exit(0)
	
	
	if pre_condition_67(y=y)==True:
		print("pre_condition_67 SAT")
		print('x = 61/64')
		print('y = 1035/512')
		exit(0)
	
	
	if pre_condition_68(y=y)==True:
		print("pre_condition_68 SAT")
		print('x = 241/256')
		print('y = 519/256')
		exit(0)
	
	
	if pre_condition_69(y=y)==True:
		print("pre_condition_69 SAT")
		print('x = 525/256')
		print('y = -57/64')
		exit(0)
	
	
	if pre_condition_70(y=y)==True:
		print("pre_condition_70 SAT")
		print('x = 15/16')
		print('y = 1039/512')
		exit(0)
	
	
	if pre_condition_71(y=y)==True:
		print("pre_condition_71 SAT")
		print('x = -1079/512')
		print('y = -95/128')
		exit(0)
	
	
	if pre_condition_72(y=y)==True:
		print("pre_condition_72 SAT")
		print('x = 65/32')
		print('y = -119/128')
		exit(0)
	
	
	if pre_condition_73(y=y)==True:
		print("pre_condition_73 SAT")
		print('x = 239/256')
		print('y = 2079/1024')
		exit(0)
	
	
	if pre_condition_74(y=y)==True:
		print("pre_condition_74 SAT")
		print('x = 1051/512')
		print('y = -113/128')
		exit(0)
	
	
	if pre_condition_75(y=y)==True:
		print("pre_condition_75 SAT")
		print('x = 263/128')
		print('y = -225/256')
		exit(0)
	
	
	if pre_condition_76(y=y)==True:
		print("pre_condition_76 SAT")
		print('x = 1097/512')
		print('y = -163/256')
		exit(0)
	
	
	if pre_condition_77(y=y)==True:
		print("pre_condition_77 SAT")
		print('x = 131/64')
		print('y = -115/128')
		exit(0)
	
	
	if pre_condition_78(y=y)==True:
		print("pre_condition_78 SAT")
		print('x = 51/64')
		print('y = 1069/512')
		exit(0)
	
	
	if pre_condition_79(y=y)==True:
		print("pre_condition_79 SAT")
		print('x = 121/128')
		print('y = 1037/512')
		exit(0)
	
	
	if pre_condition_80(y=y)==True:
		print("pre_condition_80 SAT")
		print('x = 251/256')
		print('y = 257/128')
		exit(0)
	
	
	if pre_condition_81(y=y)==True:
		print("pre_condition_81 SAT")
		print('x = 253/256')
		print('y = 513/256')
		exit(0)
	
	
	if pre_condition_82(y=y)==True:
		print("pre_condition_82 SAT")
		print('x = 1047/512')
		print('y = -231/256')
		exit(0)
	
	
	if pre_condition_83(y=y)==True:
		print("pre_condition_83 SAT")
		print('x = 249/256')
		print('y = 515/256')
		exit(0)
	
	
	if pre_condition_84(y=y)==True:
		print("pre_condition_84 SAT")
		print('x = -135/64')
		print('y = -189/256')
		exit(0)
	
	
	if pre_condition_85(y=y)==True:
		print("pre_condition_85 SAT")
		print('x = 63/64')
		print('y = 1027/512')
		exit(0)
	
	
	if pre_condition_86(y=y)==True:
		print("pre_condition_86 SAT")
		print('x = 1049/512')
		print('y = -229/256')
		exit(0)
	
	
	if pre_condition_87(y=y)==True:
		print("pre_condition_87 SAT")
		print('x = 127/128')
		print('y = 1025/512')
		exit(0)
	
	
	if pre_condition_88(y=y)==True:
		print("pre_condition_88 SAT")
		print('x = 31/32')
		print('y = 1031/512')
		exit(0)
	
	
	if pre_condition_89(y=y)==True:
		print("pre_condition_89 SAT")
		print('x = -541/256')
		print('y = -93/128')
		exit(0)
	
	
	if pre_condition_90(y=y)==True:
		print("pre_condition_90 SAT")
		print('x = 1045/512')
		print('y = -233/256')
		exit(0)
	
	
	if pre_condition_91(y=y)==True:
		print("pre_condition_91 SAT")
		print('x = -1083/512')
		print('y = -185/256')
		exit(0)
	
	
	if pre_condition_92(y=y)==True:
		print("pre_condition_92 SAT")
		print('x = 1095/512')
		print('y = -83/128')
		exit(0)
	
	
	if pre_condition_93(y=y)==True:
		print("pre_condition_93 SAT")
		print('x = 205/256')
		print('y = 4273/2048')
		exit(0)
	
	
	if pre_condition_94(y=y)==True:
		print("pre_condition_94 SAT")
		print('x = 1041/512')
		print('y = -475/512')
		exit(0)
	
	
	if pre_condition_95(y=y)==True:
		print("pre_condition_95 SAT")
		print('x = 203/256')
		print('y = 4279/2048')
		exit(0)
	
	
	if pre_condition_96(y=y)==True:
		print("pre_condition_96 SAT")
		print('x = 27/32')
		print('y = 265/128')
		exit(0)
	
	
	if pre_condition_97(y=y)==True:
		print("pre_condition_97 SAT")
		print('x = 109/128')
		print('y = 529/256')
		exit(0)
	
	
	if pre_condition_98(y=y)==True:
		print("pre_condition_98 SAT")
		print('x = 1093/512')
		print('y = -85/128')
		exit(0)
	
	
	if pre_condition_99(y=y)==True:
		print("pre_condition_99 SAT")
		print('x = 217/256')
		print('y = 4235/2048')
		exit(0)
	
	
	if pre_condition_100(y=y)==True:
		print("pre_condition_100 SAT")
		print('x = 125/128')
		print('y = 1029/512')
		exit(0)
	
	
	if pre_condition_101(y=y)==True:
		print("pre_condition_101 SAT")
		print('x = 219/256')
		print('y = 1057/512')
		exit(0)
	
	
	if pre_condition_102(y=y)==True:
		print("pre_condition_102 SAT")
		print('x = 533/256')
		print('y = -13/16')
		exit(0)
	
	
	if pre_condition_103(y=y)==True:
		print("pre_condition_103 SAT")
		print('x = 213/256')
		print('y = 531/256')
		exit(0)
	
	
	if pre_condition_104(y=y)==True:
		print("pre_condition_104 SAT")
		print('x = 53/64')
		print('y = 1063/512')
		exit(0)
	
	
	if pre_condition_105(y=y)==True:
		print("pre_condition_105 SAT")
		print('x = 211/256')
		print('y = 2127/1024')
		exit(0)
	
	
	if pre_condition_106(y=y)==True:
		print("pre_condition_106 SAT")
		print('x = 107/128')
		print('y = 1061/512')
		exit(0)
	
	
	if pre_condition_107(y=y)==True:
		print("pre_condition_107 SAT")
		print('x = 215/256')
		print('y = 2121/1024')
		exit(0)
	
	
	if pre_condition_108(y=y)==True:
		print("pre_condition_108 SAT")
		print('x = -273/128')
		print('y = -171/256')
		exit(0)
	
	
	if pre_condition_109(y=y)==True:
		print("pre_condition_109 SAT")
		print('x = 67/32')
		print('y = -25/32')
		exit(0)
	
	
	if pre_condition_110(y=y)==True:
		print("pre_condition_110 SAT")
		print('x = 265/128')
		print('y = -27/32')
		exit(0)
	
	
	if pre_condition_111(y=y)==True:
		print("pre_condition_111 SAT")
		print('x = 1069/512')
		print('y = -51/64')
		exit(0)
	
	
	if pre_condition_112(y=y)==True:
		print("pre_condition_112 SAT")
		print('x = 1063/512')
		print('y = -53/64')
		exit(0)
	
	
	if pre_condition_113(y=y)==True:
		print("pre_condition_113 SAT")
		print('x = 189/256')
		print('y = 135/64')
		exit(0)
	
	
	if pre_condition_114(y=y)==True:
		print("pre_condition_114 SAT")
		print('x = 23/32')
		print('y = 271/128')
		exit(0)
	
	
	if pre_condition_115(y=y)==True:
		print("pre_condition_115 SAT")
		print('x = 1061/512')
		print('y = -107/128')
		exit(0)
	
	
	if pre_condition_116(y=y)==True:
		print("pre_condition_116 SAT")
		print('x = -277/128')
		print('y = -9/16')
		exit(0)
	
	
	if pre_condition_117(y=y)==True:
		print("pre_condition_117 SAT")
		print('x = 531/256')
		print('y = -213/256')
		exit(0)
	
	
	if pre_condition_118(y=y)==True:
		print("pre_condition_118 SAT")
		print('x = 97/128')
		print('y = 269/128')
		exit(0)
	
	
	if pre_condition_119(y=y)==True:
		print("pre_condition_119 SAT")
		print('x = 3/4')
		print('y = 539/256')
		exit(0)
	
	
	if pre_condition_120(y=y)==True:
		print("pre_condition_120 SAT")
		print('x = -139/64')
		print('y = -17/32')
		exit(0)
	
	
	if pre_condition_121(y=y)==True:
		print("pre_condition_121 SAT")
		print('x = 133/64')
		print('y = -105/128')
		exit(0)
	
	
	if pre_condition_122(y=y)==True:
		print("pre_condition_122 SAT")
		print('x = 193/256')
		print('y = 4309/2048')
		exit(0)
	
	
	if pre_condition_123(y=y)==True:
		print("pre_condition_123 SAT")
		print('x = 95/128')
		print('y = 1079/512')
		exit(0)
	
	
	if pre_condition_124(y=y)==True:
		print("pre_condition_124 SAT")
		print('x = 191/256')
		print('y = 8629/4096')
		exit(0)
	
	
	if pre_condition_125(y=y)==True:
		print("pre_condition_125 SAT")
		print('x = -557/256')
		print('y = -33/64')
		exit(0)
	
	
	if pre_condition_126(y=y)==True:
		print("pre_condition_126 SAT")
		print('x = -1113/512')
		print('y = -133/256')
		exit(0)
	
	
	if pre_condition_127(y=y)==True:
		print("pre_condition_127 SAT")
		print('x = -555/256')
		print('y = -35/64')
		exit(0)
	
	
	if pre_condition_128(y=y)==True:
		print("pre_condition_128 SAT")
		print('x = -1109/512')
		print('y = -141/256')
		exit(0)
	
	
	if pre_condition_129(y=y)==True:
		print("pre_condition_129 SAT")
		print('x = -1111/512')
		print('y = -137/256')
		exit(0)
	
	
	if pre_condition_130(y=y)==True:
		print("pre_condition_130 SAT")
		print('x = 535/256')
		print('y = -101/128')
		exit(0)
	
	
	if pre_condition_131(y=y)==True:
		print("pre_condition_131 SAT")
		print('x = -1103/512')
		print('y = -19/32')
		exit(0)
	
	
	if pre_condition_132(y=y)==True:
		print("pre_condition_132 SAT")
		print('x = 1065/512')
		print('y = -209/256')
		exit(0)
	
	
	if pre_condition_133(y=y)==True:
		print("pre_condition_133 SAT")
		print('x = 93/128')
		print('y = 541/256')
		exit(0)
	
	
	if pre_condition_134(y=y)==True:
		print("pre_condition_134 SAT")
		print('x = 99/128')
		print('y = 537/256')
		exit(0)
	
	
	if pre_condition_135(y=y)==True:
		print("pre_condition_135 SAT")
		print('x = 33/16')
		print('y = -55/64')
		exit(0)
	
	
	if pre_condition_136(y=y)==True:
		print("pre_condition_136 SAT")
		print('x = -1101/512')
		print('y = -39/64')
		exit(0)
	
	
	if pre_condition_137(y=y)==True:
		print("pre_condition_137 SAT")
		print('x = 49/64')
		print('y = 1075/512')
		exit(0)
	
	
	if pre_condition_138(y=y)==True:
		print("pre_condition_138 SAT")
		print('x = 199/256')
		print('y = 4291/2048')
		exit(0)
	
	
	if pre_condition_139(y=y)==True:
		print("pre_condition_139 SAT")
		print('x = -275/128')
		print('y = -79/128')
		exit(0)
	
	
	if pre_condition_140(y=y)==True:
		print("pre_condition_140 SAT")
		print('x = 1055/512')
		print('y = -111/128')
		exit(0)
	
	
	if pre_condition_141(y=y)==True:
		print("pre_condition_141 SAT")
		print('x = -551/256')
		print('y = -77/128')
		exit(0)
	
	
	if pre_condition_142(y=y)==True:
		print("pre_condition_142 SAT")
		print('x = 185/256')
		print('y = 4331/2048')
		exit(0)
	
	
	if pre_condition_143(y=y)==True:
		print("pre_condition_143 SAT")
		print('x = 529/256')
		print('y = -109/128')
		exit(0)
	
	
	if pre_condition_144(y=y)==True:
		print("pre_condition_144 SAT")
		print('x = -1105/512')
		print('y = -37/64')
		exit(0)
	
	
	if pre_condition_145(y=y)==True:
		print("pre_condition_145 SAT")
		print('x = -553/256')
		print('y = -73/128')
		exit(0)
	
	
	if pre_condition_146(y=y)==True:
		print("pre_condition_146 SAT")
		print('x = 197/256')
		print('y = 4297/2048')
		exit(0)
	
	
	if pre_condition_147(y=y)==True:
		print("pre_condition_147 SAT")
		print('x = 47/64')
		print('y = 1081/512')
		exit(0)
	
	
	if pre_condition_148(y=y)==True:
		print("pre_condition_148 SAT")
		print('x = 195/256')
		print('y = 4303/2048')
		exit(0)
	
	
	if pre_condition_149(y=y)==True:
		print("pre_condition_149 SAT")
		print('x = 527/256')
		print('y = -223/256')
		exit(0)
	
	
	if pre_condition_150(y=y)==True:
		print("pre_condition_150 SAT")
		print('x = -69/32')
		print('y = -75/128')
		exit(0)
	
	
	if pre_condition_151(y=y)==True:
		print("pre_condition_151 SAT")
		print('x = 1057/512')
		print('y = -219/256')
		exit(0)
	
	
	if pre_condition_152(y=y)==True:
		print("pre_condition_152 SAT")
		print('x = -1107/512')
		print('y = -145/256')
		exit(0)
	
	
	if pre_condition_153(y=y)==True:
		print("pre_condition_153 SAT")
		print('x = -267/128')
		print('y = -103/128')
		exit(0)
	
	
	if pre_condition_154(y=y)==True:
		print("pre_condition_154 SAT")
		print('x = -1059/512')
		print('y = -217/256')
		exit(0)
	
	
	if pre_condition_155(y=y)==True:
		print("pre_condition_155 SAT")
		print('x = 45/64')
		print('y = 543/256')
		exit(0)
	
	
	if pre_condition_156(y=y)==True:
		print("pre_condition_156 SAT")
		print('x = 187/256')
		print('y = 2163/1024')
		exit(0)
	
	
	if pre_condition_157(y=y)==True:
		print("pre_condition_157 SAT")
		print('x = 91/128')
		print('y = 1085/512')
		exit(0)
	
	
	if pre_condition_158(y=y)==True:
		print("pre_condition_158 SAT")
		print('x = 181/256')
		print('y = 2171/1024')
		exit(0)
	
	
	if pre_condition_159(y=y)==True:
		print("pre_condition_159 SAT")
		print('x = -1071/512')
		print('y = -201/256')
		exit(0)
	
	
	if pre_condition_160(y=y)==True:
		print("pre_condition_160 SAT")
		print('x = 183/256')
		print('y = 4337/2048')
		exit(0)
	
	
	if pre_condition_161(y=y)==True:
		print("pre_condition_161 SAT")
		print('x = 179/256')
		print('y = 8695/4096')
		exit(0)
	
	
	if pre_condition_162(y=y)==True:
		print("pre_condition_162 SAT")
		print('x = 29/64')
		print('y = 35/16')
		exit(0)
	
	
	if pre_condition_163(y=y)==True:
		print("pre_condition_163 SAT")
		print('x = 75/128')
		print('y = 69/32')
		exit(0)
	
	
	if pre_condition_164(y=y)==True:
		print("pre_condition_164 SAT")
		print('x = 17/32')
		print('y = 139/64')
		exit(0)
	
	
	if pre_condition_165(y=y)==True:
		print("pre_condition_165 SAT")
		print('x = 9/16')
		print('y = 277/128')
		exit(0)
	
	
	if pre_condition_166(y=y)==True:
		print("pre_condition_166 SAT")
		print('x = 35/64')
		print('y = 555/256')
		exit(0)
	
	
	if pre_condition_167(y=y)==True:
		print("pre_condition_167 SAT")
		print('x = 1067/512')
		print('y = -207/256')
		exit(0)
	
	
	if pre_condition_168(y=y)==True:
		print("pre_condition_168 SAT")
		print('x = 73/128')
		print('y = 553/256')
		exit(0)
	
	
	if pre_condition_169(y=y)==True:
		print("pre_condition_169 SAT")
		print('x = 37/64')
		print('y = 1105/512')
		exit(0)
	
	
	if pre_condition_170(y=y)==True:
		print("pre_condition_170 SAT")
		print('x = 1075/512')
		print('y = -49/64')
		exit(0)
	
	
	if pre_condition_171(y=y)==True:
		print("pre_condition_171 SAT")
		print('x = -537/256')
		print('y = -99/128')
		exit(0)
	
	
	if pre_condition_172(y=y)==True:
		print("pre_condition_172 SAT")
		print('x = 71/128')
		print('y = 2217/1024')
		exit(0)
	
	
	if pre_condition_173(y=y)==True:
		print("pre_condition_173 SAT")
		print('x = -269/128')
		print('y = -97/128')
		exit(0)
	
	
	if pre_condition_174(y=y)==True:
		print("pre_condition_174 SAT")
		print('x = 63/128')
		print('y = 279/128')
		exit(0)
	
	
	if pre_condition_175(y=y)==True:
		print("pre_condition_175 SAT")
		print('x = 1077/512')
		print('y = -193/256')
		exit(0)
	
	
	if pre_condition_176(y=y)==True:
		print("pre_condition_176 SAT")
		print('x = 69/128')
		print('y = 2221/1024')
		exit(0)
	
	
	if pre_condition_177(y=y)==True:
		print("pre_condition_177 SAT")
		print('x = 33/64')
		print('y = 557/256')
		exit(0)
	
	
	if pre_condition_178(y=y)==True:
		print("pre_condition_178 SAT")
		print('x = 1073/512')
		print('y = -199/256')
		exit(0)
	
	
	if pre_condition_179(y=y)==True:
		print("pre_condition_179 SAT")
		print('x = -1137/512')
		print('y = -1/4')
		exit(0)
	
	
	if pre_condition_180(y=y)==True:
		print("pre_condition_180 SAT")
		print('x = 67/128')
		print('y = 2225/1024')
		exit(0)
	
	
	if pre_condition_181(y=y)==True:
		print("pre_condition_181 SAT")
		print('x = -285/128')
		print('y = -3/16')
		exit(0)
	
	
	if pre_condition_182(y=y)==True:
		print("pre_condition_182 SAT")
		print('x = 1/2')
		print('y = 1115/512')
		exit(0)
	
	
	if pre_condition_183(y=y)==True:
		print("pre_condition_183 SAT")
		print('x = -141/64')
		print('y = -3/8')
		exit(0)
	
	
	if pre_condition_184(y=y)==True:
		print("pre_condition_184 SAT")
		print('x = 65/128')
		print('y = 2229/1024')
		exit(0)
	
	
	if pre_condition_185(y=y)==True:
		print("pre_condition_185 SAT")
		print('x = -1141/512')
		print('y = -11/64')
		exit(0)
	
	
	if pre_condition_186(y=y)==True:
		print("pre_condition_186 SAT")
		print('x = 61/128')
		print('y = 559/256')
		exit(0)
	
	
	if pre_condition_187(y=y)==True:
		print("pre_condition_187 SAT")
		print('x = 15/32')
		print('y = 1119/512')
		exit(0)
	
	
	if pre_condition_188(y=y)==True:
		print("pre_condition_188 SAT")
		print('x = 59/128')
		print('y = 2239/1024')
		exit(0)
	
	
	if pre_condition_189(y=y)==True:
		print("pre_condition_189 SAT")
		print('x = -1139/512')
		print('y = -7/32')
		exit(0)
	
	
	if pre_condition_190(y=y)==True:
		print("pre_condition_190 SAT")
		print('x = 31/64')
		print('y = 1117/512')
		exit(0)
	
	
	if pre_condition_191(y=y)==True:
		print("pre_condition_191 SAT")
		print('x = 41/64')
		print('y = 137/64')
		exit(0)
	
	
	if pre_condition_192(y=y)==True:
		print("pre_condition_192 SAT")
		print('x = -569/256')
		print('y = -15/64')
		exit(0)
	
	
	if pre_condition_193(y=y)==True:
		print("pre_condition_193 SAT")
		print('x = -1133/512')
		print('y = -5/16')
		exit(0)
	
	
	if pre_condition_194(y=y)==True:
		print("pre_condition_194 SAT")
		print('x = 171/256')
		print('y = 273/128')
		exit(0)
	
	
	if pre_condition_195(y=y)==True:
		print("pre_condition_195 SAT")
		print('x = -561/256')
		print('y = -7/16')
		exit(0)
	
	
	if pre_condition_196(y=y)==True:
		print("pre_condition_196 SAT")
		print('x = -1135/512')
		print('y = -9/32')
		exit(0)
	
	
	if pre_condition_197(y=y)==True:
		print("pre_condition_197 SAT")
		print('x = -71/32')
		print('y = -17/64')
		exit(0)
	
	
	if pre_condition_198(y=y)==True:
		print("pre_condition_198 SAT")
		print('x = 21/32')
		print('y = 547/256')
		exit(0)
	
	
	if pre_condition_199(y=y)==True:
		print("pre_condition_199 SAT")
		print('x = 85/128')
		print('y = 1093/512')
		exit(0)
	
	
	if pre_condition_200(y=y)==True:
		print("pre_condition_200 SAT")
		print('x = -567/256')
		print('y = -19/64')
		exit(0)
	
	
	if pre_condition_201(y=y)==True:
		print("pre_condition_201 SAT")
		print('x = 83/128')
		print('y = 1095/512')
		exit(0)
	
	
	if pre_condition_202(y=y)==True:
		print("pre_condition_202 SAT")
		print('x = -1119/512')
		print('y = -15/32')
		exit(0)
	
	
	if pre_condition_203(y=y)==True:
		print("pre_condition_203 SAT")
		print('x = -1131/512')
		print('y = -11/32')
		exit(0)
	
	
	if pre_condition_204(y=y)==True:
		print("pre_condition_204 SAT")
		print('x = 167/256')
		print('y = 35023/16384')
		exit(0)
	
	
	if pre_condition_205(y=y)==True:
		print("pre_condition_205 SAT")
		print('x = -1117/512')
		print('y = -31/64')
		exit(0)
	
	
	if pre_condition_206(y=y)==True:
		print("pre_condition_206 SAT")
		print('x = -1129/512')
		print('y = -23/64')
		exit(0)


	print("UNKNOWN")
	exit(0)
