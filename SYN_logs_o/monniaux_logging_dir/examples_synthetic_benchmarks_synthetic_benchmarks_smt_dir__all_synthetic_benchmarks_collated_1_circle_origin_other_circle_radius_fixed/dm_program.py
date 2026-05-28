import sympy
from sympy import *

def pre_condition_0(r:sympy.Rational):
	#(y**2 > 1599/64) & (-r**2 + y**2 + 1/64 < 0)

	pre_cond = And(StrictGreaterThan(Pow(Symbol('y'), Integer(2)), Rational(1599, 64)), StrictLessThan(Add(Mul(Integer(-1), Pow(Symbol('r'), Integer(2))), Pow(Symbol('y'), Integer(2)), Rational(1, 64)), Integer(0)))

	eval = pre_cond.subs( { 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1(r:sympy.Rational):
	#r**2 > 1601/64

	pre_cond = StrictGreaterThan(Pow(Symbol('r'), Integer(2)), Rational(1601, 64))

	eval = pre_cond.subs( { 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_2(r:sympy.Rational):
	#(y**2 > 6399/256) & (-r**2 + y**2 + 1/256 < 0)

	pre_cond = And(StrictGreaterThan(Pow(Symbol('y'), Integer(2)), Rational(6399, 256)), StrictLessThan(Add(Mul(Integer(-1), Pow(Symbol('r'), Integer(2))), Pow(Symbol('y'), Integer(2)), Rational(1, 256)), Integer(0)))

	eval = pre_cond.subs( { 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_3(r:sympy.Rational):
	#r**2 > 6401/256

	pre_cond = StrictGreaterThan(Pow(Symbol('r'), Integer(2)), Rational(6401, 256))

	eval = pre_cond.subs( { 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_4(r:sympy.Rational):
	#(y**2 > 25591/1024) & (-r**2 + y**2 + 9/1024 < 0)

	pre_cond = And(StrictGreaterThan(Pow(Symbol('y'), Integer(2)), Rational(25591, 1024)), StrictLessThan(Add(Mul(Integer(-1), Pow(Symbol('r'), Integer(2))), Pow(Symbol('y'), Integer(2)), Rational(9, 1024)), Integer(0)))

	eval = pre_cond.subs( { 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_5(r:sympy.Rational):
	#r**2 > 419454985/16777216

	pre_cond = StrictGreaterThan(Pow(Symbol('r'), Integer(2)), Rational(419454985, 16777216))

	eval = pre_cond.subs( { 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_6(r:sympy.Rational):
	#(y**2 > 409431/16384) & (-r**2 + y**2 + 169/16384 < 0)

	pre_cond = And(StrictGreaterThan(Pow(Symbol('y'), Integer(2)), Rational(409431, 16384)), StrictLessThan(Add(Mul(Integer(-1), Pow(Symbol('r'), Integer(2))), Pow(Symbol('y'), Integer(2)), Rational(169, 16384)), Integer(0)))

	eval = pre_cond.subs( { 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_7(r:sympy.Rational):
	#r**2 > 26214977/1048576

	pre_cond = StrictGreaterThan(Pow(Symbol('r'), Integer(2)), Rational(26214977, 1048576))

	eval = pre_cond.subs( { 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_8(r:sympy.Rational):
	#(y**2 > 102351/4096) & (-r**2 + y**2 + 49/4096 < 0)

	pre_cond = And(StrictGreaterThan(Pow(Symbol('y'), Integer(2)), Rational(102351, 4096)), StrictLessThan(Add(Mul(Integer(-1), Pow(Symbol('r'), Integer(2))), Pow(Symbol('y'), Integer(2)), Rational(49, 4096)), Integer(0)))

	eval = pre_cond.subs( { 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_9(r:sympy.Rational):
	#r**2 > 6710985065/268435456

	pre_cond = StrictGreaterThan(Pow(Symbol('r'), Integer(2)), Rational(6710985065, 268435456))

	eval = pre_cond.subs( { 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_10(r:sympy.Rational):
	#(y**2 > 1637439/65536) & (-r**2 + y**2 + 961/65536 < 0)

	pre_cond = And(StrictGreaterThan(Pow(Symbol('y'), Integer(2)), Rational(1637439, 65536)), StrictLessThan(Add(Mul(Integer(-1), Pow(Symbol('r'), Integer(2))), Pow(Symbol('y'), Integer(2)), Rational(961, 65536)), Integer(0)))

	eval = pre_cond.subs( { 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_11(r:sympy.Rational):
	#r**2 > 104857673/4194304

	pre_cond = StrictGreaterThan(Pow(Symbol('r'), Integer(2)), Rational(104857673, 4194304))

	eval = pre_cond.subs( { 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_12(r:sympy.Rational):
	#(y**2 > 1637439/65536) & (-r**2 + y**2 + 961/65536 < 0)

	pre_cond = And(StrictGreaterThan(Pow(Symbol('y'), Integer(2)), Rational(1637439, 65536)), StrictLessThan(Add(Mul(Integer(-1), Pow(Symbol('r'), Integer(2))), Pow(Symbol('y'), Integer(2)), Rational(961, 65536)), Integer(0)))

	eval = pre_cond.subs( { 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_13(r:sympy.Rational):
	#r**2 > 507060240091291761920605610618737/20282409603651670423947251286016

	pre_cond = StrictGreaterThan(Pow(Symbol('r'), Integer(2)), Rational(507060240091291761920605610618737, 20282409603651670423947251286016))

	eval = pre_cond.subs( { 'r':r })

	if eval==True:
		assert eval!=False
		return True
	return False


def post_condition(r:sympy.Rational, x:sympy.Rational, y:sympy.Rational):
	# (0 > -r**2 + x**2 + y**2) & (0 > -x**2 - y**2 + 25)

	post_cond =  And(StrictGreaterThan(Integer(0), Add(Mul(Integer(-1), Pow(Symbol('r'), Integer(2))), Pow(Symbol('x'), Integer(2)), Pow(Symbol('y'), Integer(2)))), StrictGreaterThan(Integer(0), Add(Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Integer(25))))

	eval = post_cond.subs( { 'r':r, 'x':x, 'y':y })

	return eval == sympy.logic.boolalg.BooleanTrue





if __name__=="__main__":
	
	ip_0=int(input("enter integer numerator of r:\n"))
	ip_1=int(input("enter integer denominator of r:\n"))
	assert(ip_1!=0), ("Error denominator entered is 0")
	r=sympy.Rational(ip_0,ip_1)
	
	
	
	
	if pre_condition_0(r=r)==True:
		print("pre_condition_0 SAT")
		print('x = 1/8')
		print('y = 5')
		print('r = -6')
		exit(0)
	
	
	if pre_condition_1(r=r)==True:
		print("pre_condition_1 SAT")
		print('x = 1/8')
		print('y = 5')
		print('r = -6')
		exit(0)
	
	
	if pre_condition_2(r=r)==True:
		print("pre_condition_2 SAT")
		print('x = -1/16')
		print('y = -5')
		print('r = -5121/1024')
		exit(0)
	
	
	if pre_condition_3(r=r)==True:
		print("pre_condition_3 SAT")
		print('x = -1/16')
		print('y = -5')
		print('r = -5121/1024')
		exit(0)
	
	
	if pre_condition_4(r=r)==True:
		print("pre_condition_4 SAT")
		print('x = 3/32')
		print('y = -20477/4096')
		print('r = -20481/4096')
		exit(0)
	
	
	if pre_condition_5(r=r)==True:
		print("pre_condition_5 SAT")
		print('x = 3/32')
		print('y = -20477/4096')
		print('r = -20481/4096')
		exit(0)
	
	
	if pre_condition_6(r=r)==True:
		print("pre_condition_6 SAT")
		print('x = -13/128')
		print('y = -5119/1024')
		print('r = 40961/8192')
		exit(0)
	
	
	if pre_condition_7(r=r)==True:
		print("pre_condition_7 SAT")
		print('x = -13/128')
		print('y = -5119/1024')
		print('r = 40961/8192')
		exit(0)
	
	
	if pre_condition_8(r=r)==True:
		print("pre_condition_8 SAT")
		print('x = -7/64')
		print('y = -81901/16384')
		print('r = 327683/65536')
		exit(0)
	
	
	if pre_condition_9(r=r)==True:
		print("pre_condition_9 SAT")
		print('x = -7/64')
		print('y = -81901/16384')
		print('r = 327683/65536')
		exit(0)
	
	
	if pre_condition_10(r=r)==True:
		print("pre_condition_10 SAT")
		print('x = -31/256')
		print('y = -10237/2048')
		print('r = 163841/32768')
		exit(0)
	
	
	if pre_condition_11(r=r)==True:
		print("pre_condition_11 SAT")
		print('x = -31/256')
		print('y = -10237/2048')
		print('r = 163841/32768')
		exit(0)
	
	
	if pre_condition_12(r=r)==True:
		print("pre_condition_12 SAT")
		print('x = 31/256')
		print('y = -22511393226472089/4503599627370496')
		print('r = 5242881/1048576')
		exit(0)
	
	
	if pre_condition_13(r=r)==True:
		print("pre_condition_13 SAT")
		print('x = 31/256')
		print('y = -22511393226472089/4503599627370496')
		print('r = 5242881/1048576')
		exit(0)


	print("Weakest pre-condition UNSAT")
	exit(0)
