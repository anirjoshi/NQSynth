import sympy
from sympy import *

def pre_condition_0(a:sympy.Rational,b:sympy.Rational):
	#(b + y**3 + y > 0) & (a + y**3 + y < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('b'), Pow(Symbol('y'), Integer(3)), Symbol('y')), Integer(0)), StrictLessThan(Add(Symbol('a'), Pow(Symbol('y'), Integer(3)), Symbol('y')), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1(a:sympy.Rational,b:sympy.Rational):
	#(b > 0) & (a < 0)

	pre_cond = And(StrictGreaterThan(Symbol('b'), Integer(0)), StrictLessThan(Symbol('a'), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_2(a:sympy.Rational,b:sympy.Rational):
	#(b + y**3 + y**2/4 + y + 3/8 > 0) & (a + y**3 + y**2/4 + y - 5/8 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('b'), Pow(Symbol('y'), Integer(3)), Mul(Rational(1, 4), Pow(Symbol('y'), Integer(2))), Symbol('y'), Rational(3, 8)), Integer(0)), StrictLessThan(Add(Symbol('a'), Pow(Symbol('y'), Integer(3)), Mul(Rational(1, 4), Pow(Symbol('y'), Integer(2))), Symbol('y'), Rational(-5, 8)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_3(a:sympy.Rational,b:sympy.Rational):
	#(b > -3/8) & (a < 5/8)

	pre_cond = And(StrictGreaterThan(Symbol('b'), Rational(-3, 8)), StrictLessThan(Symbol('a'), Rational(5, 8)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_4(a:sympy.Rational,b:sympy.Rational):
	#(b + y**3 + 25*y**2/64 + y + 195/512 > 0) & (a + y**3 + 25*y**2/64 + y - 445/512 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('b'), Pow(Symbol('y'), Integer(3)), Mul(Rational(25, 64), Pow(Symbol('y'), Integer(2))), Symbol('y'), Rational(195, 512)), Integer(0)), StrictLessThan(Add(Symbol('a'), Pow(Symbol('y'), Integer(3)), Mul(Rational(25, 64), Pow(Symbol('y'), Integer(2))), Symbol('y'), Rational(-445, 512)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_5(a:sympy.Rational,b:sympy.Rational):
	#(b > -2105/4096) & (a < 3015/4096)

	pre_cond = And(StrictGreaterThan(Symbol('b'), Rational(-2105, 4096)), StrictLessThan(Symbol('a'), Rational(3015, 4096)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_6(a:sympy.Rational,b:sympy.Rational):
	#(b + y**3 + y**2 + y > 0) & (a + y**3 + y**2 + y - 2 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('b'), Pow(Symbol('y'), Integer(3)), Pow(Symbol('y'), Integer(2)), Symbol('y')), Integer(0)), StrictLessThan(Add(Symbol('a'), Pow(Symbol('y'), Integer(3)), Pow(Symbol('y'), Integer(2)), Symbol('y'), Integer(-2)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_7(a:sympy.Rational,b:sympy.Rational):
	#(b > 1) & (a < 3)

	pre_cond = And(StrictGreaterThan(Symbol('b'), Integer(1)), StrictLessThan(Symbol('a'), Integer(3)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_8(a:sympy.Rational,b:sympy.Rational):
	#(b + y**3 + 4*y**2 + y - 6 > 0) & (a + y**3 + 4*y**2 + y - 10 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('b'), Pow(Symbol('y'), Integer(3)), Mul(Integer(4), Pow(Symbol('y'), Integer(2))), Symbol('y'), Integer(-6)), Integer(0)), StrictLessThan(Add(Symbol('a'), Pow(Symbol('y'), Integer(3)), Mul(Integer(4), Pow(Symbol('y'), Integer(2))), Symbol('y'), Integer(-10)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_9(a:sympy.Rational,b:sympy.Rational):
	#(b > 0) & (a < 4)

	pre_cond = And(StrictGreaterThan(Symbol('b'), Integer(0)), StrictLessThan(Symbol('a'), Integer(4)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_10(a:sympy.Rational,b:sympy.Rational):
	#(b + y**3 + 169*y**2/16 + y - 1989/64 > 0) & (a + y**3 + 169*y**2/16 + y - 2405/64 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('b'), Pow(Symbol('y'), Integer(3)), Mul(Rational(169, 16), Pow(Symbol('y'), Integer(2))), Symbol('y'), Rational(-1989, 64)), Integer(0)), StrictLessThan(Add(Symbol('a'), Pow(Symbol('y'), Integer(3)), Mul(Rational(169, 16), Pow(Symbol('y'), Integer(2))), Symbol('y'), Rational(-2405, 64)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_11(a:sympy.Rational,b:sympy.Rational):
	#(b > -75/64) & (a < 341/64)

	pre_cond = And(StrictGreaterThan(Symbol('b'), Rational(-75, 64)), StrictLessThan(Symbol('a'), Rational(341, 64)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_12(a:sympy.Rational,b:sympy.Rational):
	#(b + y**3 + 729*y**2/64 + y - 17955/512 > 0) & (a + y**3 + 729*y**2/64 + y - 21411/512 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('b'), Pow(Symbol('y'), Integer(3)), Mul(Rational(729, 64), Pow(Symbol('y'), Integer(2))), Symbol('y'), Rational(-17955, 512)), Integer(0)), StrictLessThan(Add(Symbol('a'), Pow(Symbol('y'), Integer(3)), Mul(Rational(729, 64), Pow(Symbol('y'), Integer(2))), Symbol('y'), Rational(-21411, 512)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_13(a:sympy.Rational,b:sympy.Rational):
	#(b > -253/512) & (a < 3203/512)

	pre_cond = And(StrictGreaterThan(Symbol('b'), Rational(-253, 512)), StrictLessThan(Symbol('a'), Rational(3203, 512)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_14(a:sympy.Rational,b:sympy.Rational):
	#(b + y**3 + 11025*y**2/1024 + y - 1050105/32768 > 0) & (a + y**3 + 11025*y**2/1024 + y - 1265145/32768 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('b'), Pow(Symbol('y'), Integer(3)), Mul(Rational(11025, 1024), Pow(Symbol('y'), Integer(2))), Symbol('y'), Rational(-1050105, 32768)), Integer(0)), StrictLessThan(Add(Symbol('a'), Pow(Symbol('y'), Integer(3)), Mul(Rational(11025, 1024), Pow(Symbol('y'), Integer(2))), Symbol('y'), Rational(-1265145, 32768)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_15(a:sympy.Rational,b:sympy.Rational):
	#(b > -88977/1048576) & (a < 6792303/1048576)

	pre_cond = And(StrictGreaterThan(Symbol('b'), Rational(-88977, 1048576)), StrictLessThan(Symbol('a'), Rational(6792303, 1048576)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_16(a:sympy.Rational,b:sympy.Rational):
	#(b + y**3 + 40870449*y**2/4096 + y - 261258594729/262144 > 0) & (a + y**3 + 40870449*y**2/4096 + y - 261310966185/262144 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('b'), Pow(Symbol('y'), Integer(3)), Mul(Rational(40870449, 4096), Pow(Symbol('y'), Integer(2))), Symbol('y'), Rational(-261258594729, 262144)), Integer(0)), StrictLessThan(Add(Symbol('a'), Pow(Symbol('y'), Integer(3)), Mul(Rational(40870449, 4096), Pow(Symbol('y'), Integer(2))), Symbol('y'), Rational(-261310966185, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_17(a:sympy.Rational,b:sympy.Rational):
	#(b > -47513431/262144) & (a < 4858025/262144)

	pre_cond = And(StrictGreaterThan(Symbol('b'), Rational(-47513431, 262144)), StrictLessThan(Symbol('a'), Rational(4858025, 262144)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_18(a:sympy.Rational,b:sympy.Rational):
	#(b + y**3 + 532455625*y**2/65536 + y - 12284901303675/16777216 > 0) & (a + y**3 + 532455625*y**2/65536 + y - 12287925790075/16777216 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('b'), Pow(Symbol('y'), Integer(3)), Mul(Rational(532455625, 65536), Pow(Symbol('y'), Integer(2))), Symbol('y'), Rational(-12284901303675, 16777216)), Integer(0)), StrictLessThan(Add(Symbol('a'), Pow(Symbol('y'), Integer(3)), Mul(Rational(532455625, 65536), Pow(Symbol('y'), Integer(2))), Symbol('y'), Rational(-12287925790075, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_19(a:sympy.Rational,b:sympy.Rational):
	#(b > -2409707205/16777216) & (a < 614779195/16777216)

	pre_cond = And(StrictGreaterThan(Symbol('b'), Rational(-2409707205, 16777216)), StrictLessThan(Symbol('a'), Rational(614779195, 16777216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_20(a:sympy.Rational,b:sympy.Rational):
	#(b + y**3 + 8078953689*y**2/1048576 + y - 726066345271779/1073741824 > 0) & (a + y**3 + 8078953689*y**2/1048576 + y - 726254843584995/1073741824 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('b'), Pow(Symbol('y'), Integer(3)), Mul(Rational(8078953689, 1048576), Pow(Symbol('y'), Integer(2))), Symbol('y'), Rational(-726066345271779, 1073741824)), Integer(0)), StrictLessThan(Add(Symbol('a'), Pow(Symbol('y'), Integer(3)), Mul(Rational(8078953689, 1048576), Pow(Symbol('y'), Integer(2))), Symbol('y'), Rational(-726254843584995, 1073741824)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_21(a:sympy.Rational,b:sympy.Rational):
	#(b > -144684408621/1073741824) & (a < 43813904595/1073741824)

	pre_cond = And(StrictGreaterThan(Symbol('b'), Rational(-144684408621, 1073741824)), StrictLessThan(Symbol('a'), Rational(43813904595, 1073741824)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_22(a:sympy.Rational,b:sympy.Rational):
	#(b + y**3 + 32410249*y**2/4096 + y - 184488229029/262144 > 0) & (a + y**3 + 32410249*y**2/4096 + y - 184534866085/262144 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('b'), Pow(Symbol('y'), Integer(3)), Mul(Rational(32410249, 4096), Pow(Symbol('y'), Integer(2))), Symbol('y'), Rational(-184488229029, 262144)), Integer(0)), StrictLessThan(Add(Symbol('a'), Pow(Symbol('y'), Integer(3)), Mul(Rational(32410249, 4096), Pow(Symbol('y'), Integer(2))), Symbol('y'), Rational(-184534866085, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_23(a:sympy.Rational,b:sympy.Rational):
	#(b > -141879941/1048576) & (a < 44668283/1048576)

	pre_cond = And(StrictGreaterThan(Symbol('b'), Rational(-141879941, 1048576)), StrictLessThan(Symbol('a'), Rational(44668283, 1048576)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def post_condition(a:sympy.Rational, b:sympy.Rational, x:sympy.Rational, y:sympy.Rational):
	# (0 > a + x**3 + x**2*y**2 + x + y**3 + y) & (0 > -b - x**3 - x**2*y**2 + x - y**3 - y)

	post_cond =  And(StrictGreaterThan(Integer(0), Add(Symbol('a'), Pow(Symbol('x'), Integer(3)), Mul(Pow(Symbol('x'), Integer(2)), Pow(Symbol('y'), Integer(2))), Symbol('x'), Pow(Symbol('y'), Integer(3)), Symbol('y'))), StrictGreaterThan(Integer(0), Add(Mul(Integer(-1), Symbol('b')), Mul(Integer(-1), Pow(Symbol('x'), Integer(3))), Mul(Integer(-1), Pow(Symbol('x'), Integer(2)), Pow(Symbol('y'), Integer(2))), Symbol('x'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(-1), Symbol('y')))))

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
		print('a = -1')
		print('x = 0')
		print('y = 0')
		print('b = 1')
		exit(0)
	
	
	if pre_condition_1(a=a,b=b)==True:
		print("pre_condition_1 SAT")
		print('a = -1')
		print('x = 0')
		print('y = 0')
		print('b = 1')
		exit(0)
	
	
	if pre_condition_2(a=a,b=b)==True:
		print("pre_condition_2 SAT")
		print('a = 1/2')
		print('x = -1/2')
		print('y = 0')
		print('b = -1/4')
		exit(0)
	
	
	if pre_condition_3(a=a,b=b)==True:
		print("pre_condition_3 SAT")
		print('a = 1/2')
		print('x = -1/2')
		print('y = 0')
		print('b = -1/4')
		exit(0)
	
	
	if pre_condition_4(a=a,b=b)==True:
		print("pre_condition_4 SAT")
		print('a = 11/16')
		print('x = -5/8')
		print('y = 1/8')
		print('b = -65/128')
		exit(0)
	
	
	if pre_condition_5(a=a,b=b)==True:
		print("pre_condition_5 SAT")
		print('a = 11/16')
		print('x = -5/8')
		print('y = 1/8')
		print('b = -65/128')
		exit(0)
	
	
	if pre_condition_6(a=a,b=b)==True:
		print("pre_condition_6 SAT")
		print('a = 1')
		print('x = -1')
		print('y = -1')
		print('b = 9/8')
		exit(0)
	
	
	if pre_condition_7(a=a,b=b)==True:
		print("pre_condition_7 SAT")
		print('a = 1')
		print('x = -1')
		print('y = -1')
		print('b = 9/8')
		exit(0)
	
	
	if pre_condition_8(a=a,b=b)==True:
		print("pre_condition_8 SAT")
		print('a = 7/2')
		print('x = -2')
		print('y = -2')
		print('b = 1')
		exit(0)
	
	
	if pre_condition_9(a=a,b=b)==True:
		print("pre_condition_9 SAT")
		print('a = 7/2')
		print('x = -2')
		print('y = -2')
		print('b = 1')
		exit(0)
	
	
	if pre_condition_10(a=a,b=b)==True:
		print("pre_condition_10 SAT")
		print('a = 5')
		print('x = -13/4')
		print('y = -2')
		print('b = -1')
		exit(0)
	
	
	if pre_condition_11(a=a,b=b)==True:
		print("pre_condition_11 SAT")
		print('a = 5')
		print('x = -13/4')
		print('y = -2')
		print('b = -1')
		exit(0)
	
	
	if pre_condition_12(a=a,b=b)==True:
		print("pre_condition_12 SAT")
		print('a = 6')
		print('x = -27/8')
		print('y = -2')
		print('b = -1/4')
		exit(0)
	
	
	if pre_condition_13(a=a,b=b)==True:
		print("pre_condition_13 SAT")
		print('a = 6')
		print('x = -27/8')
		print('y = -2')
		print('b = -1/4')
		exit(0)
	
	
	if pre_condition_14(a=a,b=b)==True:
		print("pre_condition_14 SAT")
		print('a = 51/8')
		print('x = -105/32')
		print('y = -63/32')
		print('b = 0')
		exit(0)
	
	
	if pre_condition_15(a=a,b=b)==True:
		print("pre_condition_15 SAT")
		print('a = 51/8')
		print('x = -105/32')
		print('y = -63/32')
		print('b = 0')
		exit(0)
	
	
	if pre_condition_16(a=a,b=b)==True:
		print("pre_condition_16 SAT")
		print('a = 7')
		print('x = -6393/64')
		print('y = -10')
		print('b = -181')
		exit(0)
	
	
	if pre_condition_17(a=a,b=b)==True:
		print("pre_condition_17 SAT")
		print('a = 7')
		print('x = -6393/64')
		print('y = -10')
		print('b = -181')
		exit(0)
	
	
	if pre_condition_18(a=a,b=b)==True:
		print("pre_condition_18 SAT")
		print('a = 19')
		print('x = -23075/256')
		print('y = -19/2')
		print('b = -143')
		exit(0)
	
	
	if pre_condition_19(a=a,b=b)==True:
		print("pre_condition_19 SAT")
		print('a = 19')
		print('x = -23075/256')
		print('y = -19/2')
		print('b = -143')
		exit(0)
	
	
	if pre_condition_20(a=a,b=b)==True:
		print("pre_condition_20 SAT")
		print('a = 37')
		print('x = -89883/1024')
		print('y = -75/8')
		print('b = -134')
		exit(0)
	
	
	if pre_condition_21(a=a,b=b)==True:
		print("pre_condition_21 SAT")
		print('a = 37')
		print('x = -89883/1024')
		print('y = -75/8')
		print('b = -134')
		exit(0)
	
	
	if pre_condition_22(a=a,b=b)==True:
		print("pre_condition_22 SAT")
		print('a = 41')
		print('x = -5693/64')
		print('y = -151/16')
		print('b = -135')
		exit(0)
	
	
	if pre_condition_23(a=a,b=b)==True:
		print("pre_condition_23 SAT")
		print('a = 41')
		print('x = -5693/64')
		print('y = -151/16')
		print('b = -135')
		exit(0)


	print("UNKNOWN")
	exit(0)
