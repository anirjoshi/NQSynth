import sympy
from sympy import *

def pre_condition_0(a:sympy.Rational,b:sympy.Rational):
	#(x**2 < 1) & (a**2 + b**2 - 2*b*x + x**2 - 1 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Integer(1)), StrictLessThan(Add(Pow(Symbol('a'), Integer(2)), Pow(Symbol('b'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('b'), Symbol('x')), Pow(Symbol('x'), Integer(2)), Integer(-1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1(a:sympy.Rational,b:sympy.Rational):
	#a**2 + b**2 - b/4 - 63/64 < 0

	pre_cond = StrictLessThan(Add(Pow(Symbol('a'), Integer(2)), Pow(Symbol('b'), Integer(2)), Mul(Integer(-1), Rational(1, 4), Symbol('b')), Rational(-63, 64)), Integer(0))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_2(a:sympy.Rational,b:sympy.Rational):
	#(x**2 < 3/4) & (a**2 + a + b**2 - 2*b*x + x**2 - 3/4 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(3, 4)), StrictLessThan(Add(Pow(Symbol('a'), Integer(2)), Symbol('a'), Pow(Symbol('b'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('b'), Symbol('x')), Pow(Symbol('x'), Integer(2)), Rational(-3, 4)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_3(a:sympy.Rational,b:sympy.Rational):
	#a**2 + a + b**2 - 3/4 < 0

	pre_cond = StrictLessThan(Add(Pow(Symbol('a'), Integer(2)), Symbol('a'), Pow(Symbol('b'), Integer(2)), Rational(-3, 4)), Integer(0))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_4(a:sympy.Rational,b:sympy.Rational):
	#(x**2 < 15/16) & (a**2 + a/2 + b**2 - 2*b*x + x**2 - 15/16 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(15, 16)), StrictLessThan(Add(Pow(Symbol('a'), Integer(2)), Mul(Rational(1, 2), Symbol('a')), Pow(Symbol('b'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('b'), Symbol('x')), Pow(Symbol('x'), Integer(2)), Rational(-15, 16)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_5(a:sympy.Rational,b:sympy.Rational):
	#a**2 + a/2 + b**2 + 7*b/4 - 11/64 < 0

	pre_cond = StrictLessThan(Add(Pow(Symbol('a'), Integer(2)), Mul(Rational(1, 2), Symbol('a')), Pow(Symbol('b'), Integer(2)), Mul(Rational(7, 4), Symbol('b')), Rational(-11, 64)), Integer(0))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_6(a:sympy.Rational,b:sympy.Rational):
	#(x**2 < 207/256) & (a**2 + 7*a/8 + b**2 - 2*b*x + x**2 - 207/256 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(207, 256)), StrictLessThan(Add(Pow(Symbol('a'), Integer(2)), Mul(Rational(7, 8), Symbol('a')), Pow(Symbol('b'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('b'), Symbol('x')), Pow(Symbol('x'), Integer(2)), Rational(-207, 256)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_7(a:sympy.Rational,b:sympy.Rational):
	#a**2 + 7*a/8 + b**2 + 113*b/64 - 479/16384 < 0

	pre_cond = StrictLessThan(Add(Pow(Symbol('a'), Integer(2)), Mul(Rational(7, 8), Symbol('a')), Pow(Symbol('b'), Integer(2)), Mul(Rational(113, 64), Symbol('b')), Rational(-479, 16384)), Integer(0))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_8(a:sympy.Rational,b:sympy.Rational):
	#(x**2 < 799/1024) & (a**2 + 15*a/16 + b**2 - 2*b*x + x**2 - 799/1024 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(799, 1024)), StrictLessThan(Add(Pow(Symbol('a'), Integer(2)), Mul(Rational(15, 16), Symbol('a')), Pow(Symbol('b'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('b'), Symbol('x')), Pow(Symbol('x'), Integer(2)), Rational(-799, 1024)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_9(a:sympy.Rational,b:sympy.Rational):
	#a**2 + 15*a/16 + b**2 + 7*b/4 - 15/1024 < 0

	pre_cond = StrictLessThan(Add(Pow(Symbol('a'), Integer(2)), Mul(Rational(15, 16), Symbol('a')), Pow(Symbol('b'), Integer(2)), Mul(Rational(7, 4), Symbol('b')), Rational(-15, 1024)), Integer(0))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_10(a:sympy.Rational,b:sympy.Rational):
	#(x**2 < 3255/4096) & (a**2 + 29*a/32 + b**2 - 2*b*x + x**2 - 3255/4096 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(3255, 4096)), StrictLessThan(Add(Pow(Symbol('a'), Integer(2)), Mul(Rational(29, 32), Symbol('a')), Pow(Symbol('b'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('b'), Symbol('x')), Pow(Symbol('x'), Integer(2)), Rational(-3255, 4096)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_11(a:sympy.Rational,b:sympy.Rational):
	#a**2 + 29*a/32 + b**2 + 57*b/32 - 3/2048 < 0

	pre_cond = StrictLessThan(Add(Pow(Symbol('a'), Integer(2)), Mul(Rational(29, 32), Symbol('a')), Pow(Symbol('b'), Integer(2)), Mul(Rational(57, 32), Symbol('b')), Rational(-3, 2048)), Integer(0))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_12(a:sympy.Rational,b:sympy.Rational):
	#(x**2 < 834207/1048576) & (a**2 + 463*a/512 + b**2 - 2*b*x + x**2 - 834207/1048576 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(834207, 1048576)), StrictLessThan(Add(Pow(Symbol('a'), Integer(2)), Mul(Rational(463, 512), Symbol('a')), Pow(Symbol('b'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('b'), Symbol('x')), Pow(Symbol('x'), Integer(2)), Rational(-834207, 1048576)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_13(a:sympy.Rational,b:sympy.Rational):
	#a**2 + 463*a/512 + b**2 + 233817*b/131072 - 200463/68719476736 < 0

	pre_cond = StrictLessThan(Add(Pow(Symbol('a'), Integer(2)), Mul(Rational(463, 512), Symbol('a')), Pow(Symbol('b'), Integer(2)), Mul(Rational(233817, 131072), Symbol('b')), Rational(-200463, 68719476736)), Integer(0))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_14(a:sympy.Rational,b:sympy.Rational):
	#(x**2 < 54670827007/68719476736) & (a**2 + 118527*a/131072 + b**2 - 2*b*x + x**2 - 54670827007/68719476736 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(54670827007, 68719476736)), StrictLessThan(Add(Pow(Symbol('a'), Integer(2)), Mul(Rational(118527, 131072), Symbol('a')), Pow(Symbol('b'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('b'), Symbol('x')), Pow(Symbol('x'), Integer(2)), Rational(-54670827007, 68719476736)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_15(a:sympy.Rational,b:sympy.Rational):
	#a**2 + 118527*a/131072 + b**2 + 7482173*b/4194304 - 14053239/70368744177664 < 0

	pre_cond = StrictLessThan(Add(Pow(Symbol('a'), Integer(2)), Mul(Rational(118527, 131072), Symbol('a')), Pow(Symbol('b'), Integer(2)), Mul(Rational(7482173, 4194304), Symbol('b')), Rational(-14053239, 70368744177664)), Integer(0))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_16(a:sympy.Rational,b:sympy.Rational):
	#(x**2 < 54670827007/68719476736) & (a**2 + 118527*a/131072 + b**2 - 2*b*x + x**2 - 54670827007/68719476736 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(54670827007, 68719476736)), StrictLessThan(Add(Pow(Symbol('a'), Integer(2)), Mul(Rational(118527, 131072), Symbol('a')), Pow(Symbol('b'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('b'), Symbol('x')), Pow(Symbol('x'), Integer(2)), Rational(-54670827007, 68719476736)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_17(a:sympy.Rational,b:sympy.Rational):
	#a**2 + 118527*a/131072 + b**2 + 32135692371481365*b/18014398509481984 - 12880193710088263/1298074214633706907132624082305024 < 0

	pre_cond = StrictLessThan(Add(Pow(Symbol('a'), Integer(2)), Mul(Rational(118527, 131072), Symbol('a')), Pow(Symbol('b'), Integer(2)), Mul(Rational(32135692371481365, 18014398509481984), Symbol('b')), Rational(-12880193710088263, 1298074214633706907132624082305024)), Integer(0))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_18(a:sympy.Rational,b:sympy.Rational):
	#(x**2 < 258175681048621386119212724912127/324518553658426726783156020576256) & (a**2 + 8145113419087873*a/9007199254740992 + b**2 - 2*b*x + x**2 - 258175681048621386119212724912127/324518553658426726783156020576256 < 0)

	pre_cond = And(StrictLessThan(Pow(Symbol('x'), Integer(2)), Rational(258175681048621386119212724912127, 324518553658426726783156020576256)), StrictLessThan(Add(Pow(Symbol('a'), Integer(2)), Mul(Rational(8145113419087873, 9007199254740992), Symbol('a')), Pow(Symbol('b'), Integer(2)), Mul(Integer(-1), Integer(2), Symbol('b'), Symbol('x')), Pow(Symbol('x'), Integer(2)), Rational(-258175681048621386119212724912127, 324518553658426726783156020576256)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_19(a:sympy.Rational,b:sympy.Rational):
	#a**2 + 8145113419087873*a/9007199254740992 + b**2 + 257085538971850913*b/144115188075855872 - 253231872478570943/83076749736557242056487941267521536 < 0

	pre_cond = StrictLessThan(Add(Pow(Symbol('a'), Integer(2)), Mul(Rational(8145113419087873, 9007199254740992), Symbol('a')), Pow(Symbol('b'), Integer(2)), Mul(Rational(257085538971850913, 144115188075855872), Symbol('b')), Rational(-253231872478570943, 83076749736557242056487941267521536)), Integer(0))

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
		print('y = -1/2')
		print('a = -1')
		print('b = -1/2')
		exit(0)
	
	
	if pre_condition_3(a=a,b=b)==True:
		print("pre_condition_3 SAT")
		print('x = 0')
		print('y = -1/2')
		print('a = -1')
		print('b = -1/2')
		exit(0)
	
	
	if pre_condition_4(a=a,b=b)==True:
		print("pre_condition_4 SAT")
		print('x = -7/8')
		print('y = -1/4')
		print('a = -1')
		print('b = -1')
		exit(0)
	
	
	if pre_condition_5(a=a,b=b)==True:
		print("pre_condition_5 SAT")
		print('x = -7/8')
		print('y = -1/4')
		print('a = -1')
		print('b = -1')
		exit(0)
	
	
	if pre_condition_6(a=a,b=b)==True:
		print("pre_condition_6 SAT")
		print('x = -113/128')
		print('y = -7/16')
		print('a = -3/8')
		print('b = -15/8')
		exit(0)
	
	
	if pre_condition_7(a=a,b=b)==True:
		print("pre_condition_7 SAT")
		print('x = -113/128')
		print('y = -7/16')
		print('a = -3/8')
		print('b = -15/8')
		exit(0)
	
	
	if pre_condition_8(a=a,b=b)==True:
		print("pre_condition_8 SAT")
		print('x = -7/8')
		print('y = -15/32')
		print('a = -11/8')
		print('b = -1/2')
		exit(0)
	
	
	if pre_condition_9(a=a,b=b)==True:
		print("pre_condition_9 SAT")
		print('x = -7/8')
		print('y = -15/32')
		print('a = -11/8')
		print('b = -1/2')
		exit(0)
	
	
	if pre_condition_10(a=a,b=b)==True:
		print("pre_condition_10 SAT")
		print('x = -57/64')
		print('y = -29/64')
		print('a = -1')
		print('b = -221/128')
		exit(0)
	
	
	if pre_condition_11(a=a,b=b)==True:
		print("pre_condition_11 SAT")
		print('x = -57/64')
		print('y = -29/64')
		print('a = -1')
		print('b = -221/128')
		exit(0)
	
	
	if pre_condition_12(a=a,b=b)==True:
		print("pre_condition_12 SAT")
		print('x = -233817/262144')
		print('y = -463/1024')
		print('a = -1')
		print('b = -885/512')
		exit(0)
	
	
	if pre_condition_13(a=a,b=b)==True:
		print("pre_condition_13 SAT")
		print('x = -233817/262144')
		print('y = -463/1024')
		print('a = -1')
		print('b = -885/512')
		exit(0)
	
	
	if pre_condition_14(a=a,b=b)==True:
		print("pre_condition_14 SAT")
		print('x = -7482173/8388608')
		print('y = -118527/262144')
		print('a = -1')
		print('b = -906241/524288')
		exit(0)
	
	
	if pre_condition_15(a=a,b=b)==True:
		print("pre_condition_15 SAT")
		print('x = -7482173/8388608')
		print('y = -118527/262144')
		print('a = -1')
		print('b = -906241/524288')
		exit(0)
	
	
	if pre_condition_16(a=a,b=b)==True:
		print("pre_condition_16 SAT")
		print('x = -32135692371481365/36028797018963968')
		print('y = -118527/262144')
		print('a = -1')
		print('b = -14499857/8388608')
		exit(0)
	
	
	if pre_condition_17(a=a,b=b)==True:
		print("pre_condition_17 SAT")
		print('x = -32135692371481365/36028797018963968')
		print('y = -118527/262144')
		print('a = -1')
		print('b = -14499857/8388608')
		exit(0)
	
	
	if pre_condition_18(a=a,b=b)==True:
		print("pre_condition_18 SAT")
		print('x = -257085538971850913/288230376151711744')
		print('y = -8145113419087873/18014398509481984')
		print('a = -1')
		print('b = -31138206681195037/18014398509481984')
		exit(0)
	
	
	if pre_condition_19(a=a,b=b)==True:
		print("pre_condition_19 SAT")
		print('x = -257085538971850913/288230376151711744')
		print('y = -8145113419087873/18014398509481984')
		print('a = -1')
		print('b = -31138206681195037/18014398509481984')
		exit(0)


	print("UNKNOWN")
	exit(0)
