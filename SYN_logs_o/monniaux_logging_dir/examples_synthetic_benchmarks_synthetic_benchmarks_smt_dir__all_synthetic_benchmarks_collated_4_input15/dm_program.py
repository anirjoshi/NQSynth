import sympy
from sympy import *

def pre_condition_0(a:sympy.Rational,b:sympy.Rational):
	#(y**4 < 4095/4096) & (a**2 - a/4 + b**2 - 2*b*y + y**2 - 63/64 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(4)), Rational(4095, 4096)), StrictLessThan(Add(Pow(Symbol('a'), Integer(2)), Mul(Integer(-1), Rational(1, 4), Symbol('a')), Pow(Symbol('b'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('b'), Symbol('y')), Pow(Symbol('y'), Integer(2)), Rational(-63, 64)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1(a:sympy.Rational,b:sympy.Rational):
	#a**2 - a/4 + b**2 - 63/64 < 0

	pre_cond = StrictLessThan(Add(Pow(Symbol('a'), Integer(2)), Mul(Integer(-1), Rational(1, 4), Symbol('a')), Pow(Symbol('b'), Integer(2)), Rational(-63, 64)), Integer(0))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_2(a:sympy.Rational,b:sympy.Rational):
	#(y**4 < 1) & (a**2 + b**2 - 2*b*y + y**2 - 1 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(4)), Integer(1)), StrictLessThan(Add(Pow(Symbol('a'), Integer(2)), Pow(Symbol('b'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('b'), Symbol('y')), Pow(Symbol('y'), Integer(2)), Integer(-1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_3(a:sympy.Rational,b:sympy.Rational):
	#a**2 + b**2 - 1 < 0

	pre_cond = StrictLessThan(Add(Pow(Symbol('a'), Integer(2)), Pow(Symbol('b'), Integer(2)), Integer(-1)), Integer(0))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_4(a:sympy.Rational,b:sympy.Rational):
	#(y**4 < 15/16) & (a**2 + a + b**2 - 2*b*y + y**2 - 3/4 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(4)), Rational(15, 16)), StrictLessThan(Add(Pow(Symbol('a'), Integer(2)), Symbol('a'), Pow(Symbol('b'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('b'), Symbol('y')), Pow(Symbol('y'), Integer(2)), Rational(-3, 4)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_5(a:sympy.Rational,b:sympy.Rational):
	#a**2 + a + b**2 - 3/4 < 0

	pre_cond = StrictLessThan(Add(Pow(Symbol('a'), Integer(2)), Symbol('a'), Pow(Symbol('b'), Integer(2)), Rational(-3, 4)), Integer(0))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_6(a:sympy.Rational,b:sympy.Rational):
	#(y**4 < 255/256) & (a**2 - a/2 + b**2 - 2*b*y + y**2 - 15/16 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(4)), Rational(255, 256)), StrictLessThan(Add(Pow(Symbol('a'), Integer(2)), Mul(Integer(-1), Rational(1, 2), Symbol('a')), Pow(Symbol('b'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('b'), Symbol('y')), Pow(Symbol('y'), Integer(2)), Rational(-15, 16)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_7(a:sympy.Rational,b:sympy.Rational):
	#a**2 - a/2 + b**2 - 63*b/32 + 129/4096 < 0

	pre_cond = StrictLessThan(Add(Pow(Symbol('a'), Integer(2)), Mul(Integer(-1), Rational(1, 2), Symbol('a')), Pow(Symbol('b'), Integer(2)), Mul(Integer(-1), Rational(63, 32), Symbol('b')), Rational(129, 4096)), Integer(0))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_8(a:sympy.Rational,b:sympy.Rational):
	#(y**4 < 65535/65536) & (a**2 - a/8 + b**2 - 2*b*y + y**2 - 255/256 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(4)), Rational(65535, 65536)), StrictLessThan(Add(Pow(Symbol('a'), Integer(2)), Mul(Integer(-1), Rational(1, 8), Symbol('a')), Pow(Symbol('b'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('b'), Symbol('y')), Pow(Symbol('y'), Integer(2)), Rational(-255, 256)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_9(a:sympy.Rational,b:sympy.Rational):
	#a**2 - a/8 + b**2 + 63*b/32 - 111/4096 < 0

	pre_cond = StrictLessThan(Add(Pow(Symbol('a'), Integer(2)), Mul(Integer(-1), Rational(1, 8), Symbol('a')), Pow(Symbol('b'), Integer(2)), Mul(Rational(63, 32), Symbol('b')), Rational(-111, 4096)), Integer(0))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_10(a:sympy.Rational,b:sympy.Rational):
	#(y**4 < 1048575/1048576) & (a**2 - a/16 + b**2 - 2*b*y + y**2 - 1023/1024 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(4)), Rational(1048575, 1048576)), StrictLessThan(Add(Pow(Symbol('a'), Integer(2)), Mul(Integer(-1), Rational(1, 16), Symbol('a')), Pow(Symbol('b'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('b'), Symbol('y')), Pow(Symbol('y'), Integer(2)), Rational(-1023, 1024)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_11(a:sympy.Rational,b:sympy.Rational):
	#a**2 - a/16 + b**2 + 262143*b/131072 + 66584577/68719476736 < 0

	pre_cond = StrictLessThan(Add(Pow(Symbol('a'), Integer(2)), Mul(Integer(-1), Rational(1, 16), Symbol('a')), Pow(Symbol('b'), Integer(2)), Mul(Rational(262143, 131072), Symbol('b')), Rational(66584577, 68719476736)), Integer(0))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_12(a:sympy.Rational,b:sympy.Rational):
	#(y**4 < 16777135/16777216) & (a**2 - 3*a/32 + b**2 - 2*b*y + y**2 - 4087/4096 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(4)), Rational(16777135, 16777216)), StrictLessThan(Add(Pow(Symbol('a'), Integer(2)), Mul(Integer(-1), Rational(3, 32), Symbol('a')), Pow(Symbol('b'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('b'), Symbol('y')), Pow(Symbol('y'), Integer(2)), Rational(-4087, 4096)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_13(a:sympy.Rational,b:sympy.Rational):
	#a**2 - 3*a/32 + b**2 + 262143*b/131072 + 150470657/68719476736 < 0

	pre_cond = StrictLessThan(Add(Pow(Symbol('a'), Integer(2)), Mul(Integer(-1), Rational(3, 32), Symbol('a')), Pow(Symbol('b'), Integer(2)), Mul(Rational(262143, 131072), Symbol('b')), Rational(150470657, 68719476736)), Integer(0))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_14(a:sympy.Rational,b:sympy.Rational):
	#(y**4 < 16777215/16777216) & (a**2 - a/32 + b**2 - 2*b*y + y**2 - 4095/4096 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(4)), Rational(16777215, 16777216)), StrictLessThan(Add(Pow(Symbol('a'), Integer(2)), Mul(Integer(-1), Rational(1, 32), Symbol('a')), Pow(Symbol('b'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('b'), Symbol('y')), Pow(Symbol('y'), Integer(2)), Rational(-4095, 4096)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_15(a:sympy.Rational,b:sympy.Rational):
	#a**2 - a/32 + b**2 + 1048575*b/524288 + 266338305/1099511627776 < 0

	pre_cond = StrictLessThan(Add(Pow(Symbol('a'), Integer(2)), Mul(Integer(-1), Rational(1, 32), Symbol('a')), Pow(Symbol('b'), Integer(2)), Mul(Rational(1048575, 524288), Symbol('b')), Rational(266338305, 1099511627776)), Integer(0))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_16(a:sympy.Rational,b:sympy.Rational):
	#(y**4 < 268434831/268435456) & (a**2 - 5*a/64 + b**2 - 2*b*y + y**2 - 16359/16384 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(4)), Rational(268434831, 268435456)), StrictLessThan(Add(Pow(Symbol('a'), Integer(2)), Mul(Integer(-1), Rational(5, 64), Symbol('a')), Pow(Symbol('b'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('b'), Symbol('y')), Pow(Symbol('y'), Integer(2)), Rational(-16359, 16384)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_17(a:sympy.Rational,b:sympy.Rational):
	#a**2 - 5*a/64 + b**2 + 1048575*b/524288 + 1675624449/1099511627776 < 0

	pre_cond = StrictLessThan(Add(Pow(Symbol('a'), Integer(2)), Mul(Integer(-1), Rational(5, 64), Symbol('a')), Pow(Symbol('b'), Integer(2)), Mul(Rational(1048575, 524288), Symbol('b')), Rational(1675624449, 1099511627776)), Integer(0))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_18(a:sympy.Rational,b:sympy.Rational):
	#(y**4 < 4294960735/4294967296) & (a**2 - 9*a/128 + b**2 - 2*b*y + y**2 - 65455/65536 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(4)), Rational(4294960735, 4294967296)), StrictLessThan(Add(Pow(Symbol('a'), Integer(2)), Mul(Integer(-1), Rational(9, 128), Symbol('a')), Pow(Symbol('b'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('b'), Symbol('y')), Pow(Symbol('y'), Integer(2)), Rational(-65455, 65536)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_19(a:sympy.Rational,b:sympy.Rational):
	#a**2 - 9*a/128 + b**2 + 2097151*b/1048576 + 5431623681/4398046511104 < 0

	pre_cond = StrictLessThan(Add(Pow(Symbol('a'), Integer(2)), Mul(Integer(-1), Rational(9, 128), Symbol('a')), Pow(Symbol('b'), Integer(2)), Mul(Rational(2097151, 1048576), Symbol('b')), Rational(5431623681, 4398046511104)), Integer(0))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_20(a:sympy.Rational,b:sympy.Rational):
	#(y**4 < 268435375/268435456) & (a**2 - 3*a/64 + b**2 - 2*b*y + y**2 - 16375/16384 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('y'), Integer(4)), Rational(268435375, 268435456)), StrictLessThan(Add(Pow(Symbol('a'), Integer(2)), Mul(Integer(-1), Rational(3, 64), Symbol('a')), Pow(Symbol('b'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('b'), Symbol('y')), Pow(Symbol('y'), Integer(2)), Rational(-16375, 16384)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_21(a:sympy.Rational,b:sympy.Rational):
	#a**2 - 3*a/64 + b**2 + 4194303*b/2097152 + 9655287809/17592186044416 < 0

	pre_cond = StrictLessThan(Add(Pow(Symbol('a'), Integer(2)), Mul(Integer(-1), Rational(3, 64), Symbol('a')), Pow(Symbol('b'), Integer(2)), Mul(Rational(4194303, 2097152), Symbol('b')), Rational(9655287809, 17592186044416)), Integer(0))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def post_condition(a:sympy.Rational, b:sympy.Rational, x:sympy.Rational, y:sympy.Rational):
	# (0 > x**4 + y**4 - 1) & (0 > a**2 - 2*a*x + b**2 - 2*b*y + x**2 + y**2 - 1)

	post_cond =  And(StrictGreaterThan(Integer(0), Add(Pow(Symbol('x'), Integer(4)), Pow(Symbol('y'), Integer(4)), Integer(-1))), StrictGreaterThan(Integer(0), Add(Pow(Symbol('a'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('a'), Symbol('x')), Pow(Symbol('b'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('b'), Symbol('y')), Pow(Symbol('x'), Integer(2)), Pow(Symbol('y'), Integer(2)), Integer(-1))))

	eval = post_cond.subs( { 'a':a, 'b':b, 'x':x, 'y':y })

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
	
	
	
	
	if pre_condition_0(a=a,b=b)==True:
		print("pre_condition_0 SAT")
		print('x = 1/8')
		print('y = 0')
		print('a = 1/2')
		print('b = 0')
		exit(0)
	
	
	if pre_condition_1(a=a,b=b)==True:
		print("pre_condition_1 SAT")
		print('x = 1/8')
		print('y = 0')
		print('a = 1/2')
		print('b = 0')
		exit(0)
	
	
	if pre_condition_2(a=a,b=b)==True:
		print("pre_condition_2 SAT")
		print('x = 0')
		print('y = 0')
		print('a = -1/2')
		print('b = -13/16')
		exit(0)
	
	
	if pre_condition_3(a=a,b=b)==True:
		print("pre_condition_3 SAT")
		print('x = 0')
		print('y = 0')
		print('a = -1/2')
		print('b = -13/16')
		exit(0)
	
	
	if pre_condition_4(a=a,b=b)==True:
		print("pre_condition_4 SAT")
		print('x = -1/2')
		print('y = 0')
		print('a = -5/4')
		print('b = 0')
		exit(0)
	
	
	if pre_condition_5(a=a,b=b)==True:
		print("pre_condition_5 SAT")
		print('x = -1/2')
		print('y = 0')
		print('a = -5/4')
		print('b = 0')
		exit(0)
	
	
	if pre_condition_6(a=a,b=b)==True:
		print("pre_condition_6 SAT")
		print('x = 1/4')
		print('y = 63/64')
		print('a = 1')
		print('b = 3/2')
		exit(0)
	
	
	if pre_condition_7(a=a,b=b)==True:
		print("pre_condition_7 SAT")
		print('x = 1/4')
		print('y = 63/64')
		print('a = 1')
		print('b = 3/2')
		exit(0)
	
	
	if pre_condition_8(a=a,b=b)==True:
		print("pre_condition_8 SAT")
		print('x = 1/16')
		print('y = -63/64')
		print('a = 1/16')
		print('b = -1015/512')
		exit(0)
	
	
	if pre_condition_9(a=a,b=b)==True:
		print("pre_condition_9 SAT")
		print('x = 1/16')
		print('y = -63/64')
		print('a = 1/16')
		print('b = -1015/512')
		exit(0)
	
	
	if pre_condition_10(a=a,b=b)==True:
		print("pre_condition_10 SAT")
		print('x = 1/32')
		print('y = -262143/262144')
		print('a = 1/32')
		print('b = -4095/2048')
		exit(0)
	
	
	if pre_condition_11(a=a,b=b)==True:
		print("pre_condition_11 SAT")
		print('x = 1/32')
		print('y = -262143/262144')
		print('a = 1/32')
		print('b = -4095/2048')
		exit(0)
	
	
	if pre_condition_12(a=a,b=b)==True:
		print("pre_condition_12 SAT")
		print('x = 3/64')
		print('y = -262143/262144')
		print('a = 3/4')
		print('b = -219/128')
		exit(0)
	
	
	if pre_condition_13(a=a,b=b)==True:
		print("pre_condition_13 SAT")
		print('x = 3/64')
		print('y = -262143/262144')
		print('a = 3/4')
		print('b = -219/128')
		exit(0)
	
	
	if pre_condition_14(a=a,b=b)==True:
		print("pre_condition_14 SAT")
		print('x = 1/64')
		print('y = -1048575/1048576')
		print('a = 1/64')
		print('b = -16383/8192')
		exit(0)
	
	
	if pre_condition_15(a=a,b=b)==True:
		print("pre_condition_15 SAT")
		print('x = 1/64')
		print('y = -1048575/1048576')
		print('a = 1/64')
		print('b = -16383/8192')
		exit(0)
	
	
	if pre_condition_16(a=a,b=b)==True:
		print("pre_condition_16 SAT")
		print('x = 5/128')
		print('y = -1048575/1048576')
		print('a = 5/128')
		print('b = -65535/32768')
		exit(0)
	
	
	if pre_condition_17(a=a,b=b)==True:
		print("pre_condition_17 SAT")
		print('x = 5/128')
		print('y = -1048575/1048576')
		print('a = 5/128')
		print('b = -65535/32768')
		exit(0)
	
	
	if pre_condition_18(a=a,b=b)==True:
		print("pre_condition_18 SAT")
		print('x = 9/256')
		print('y = -2097151/2097152')
		print('a = 35/1024')
		print('b = -524287/262144')
		exit(0)
	
	
	if pre_condition_19(a=a,b=b)==True:
		print("pre_condition_19 SAT")
		print('x = 9/256')
		print('y = -2097151/2097152')
		print('a = 35/1024')
		print('b = -524287/262144')
		exit(0)
	
	
	if pre_condition_20(a=a,b=b)==True:
		print("pre_condition_20 SAT")
		print('x = 3/128')
		print('y = -4194303/4194304')
		print('a = 3/128')
		print('b = -65535/32768')
		exit(0)
	
	
	if pre_condition_21(a=a,b=b)==True:
		print("pre_condition_21 SAT")
		print('x = 3/128')
		print('y = -4194303/4194304')
		print('a = 3/128')
		print('b = -65535/32768')
		exit(0)


	print("UNKNOWN")
	exit(0)
