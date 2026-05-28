import sympy
from sympy import *

def pre_condition_0(a:sympy.Rational,b:sympy.Rational):
	#(-b**100 + x**100 + 1/1267650600228229401496703205376 > 0) & (-a**100 + x**100 + 1/1267650600228229401496703205376 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('b'), Integer(100))), Pow(Symbol('x'), Integer(100)), Rational(1, 1267650600228229401496703205376)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Pow(Symbol('a'), Integer(100))), Pow(Symbol('x'), Integer(100)), Rational(1, 1267650600228229401496703205376)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1(a:sympy.Rational,b:sympy.Rational):
	#(a**100 > 1606938044258990275541962092341162602522202993782792835301377/2037035976334486086268445688409378161051468393665936250636140449354381299763336706183397376) & (b**100 < 1606938044258990275541962092341162602522202993782792835301377/2037035976334486086268445688409378161051468393665936250636140449354381299763336706183397376)

	pre_cond = And(StrictGreaterThan(Pow(Symbol('a'), Integer(100)), Rational(1606938044258990275541962092341162602522202993782792835301377, 2037035976334486086268445688409378161051468393665936250636140449354381299763336706183397376)), StrictLessThan(Pow(Symbol('b'), Integer(100)), Rational(1606938044258990275541962092341162602522202993782792835301377, 2037035976334486086268445688409378161051468393665936250636140449354381299763336706183397376)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_2(a:sympy.Rational,b:sympy.Rational):
	#(-b**100 + x**100 + 1267650600228229401496703205376 > 0) & (-a**100 + x**100 + 1267650600228229401496703205376 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('b'), Integer(100))), Pow(Symbol('x'), Integer(100)), Integer(1267650600228229401496703205376)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Pow(Symbol('a'), Integer(100))), Pow(Symbol('x'), Integer(100)), Integer(1267650600228229401496703205376)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_3(a:sympy.Rational,b:sympy.Rational):
	#(a**100 > 1267650600228229401496703205377) & (b**100 < 1267650600228229401496703205377)

	pre_cond = And(StrictGreaterThan(Pow(Symbol('a'), Integer(100)), Integer(1267650600228229401496703205377)), StrictLessThan(Pow(Symbol('b'), Integer(100)), Integer(1267650600228229401496703205377)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_4(a:sympy.Rational,b:sympy.Rational):
	#(-b**100 + x**100 + 1267650600228229401496703205376 > 0) & (-a**100 + x**100 + 1267650600228229401496703205376 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('b'), Integer(100))), Pow(Symbol('x'), Integer(100)), Integer(1267650600228229401496703205376)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Pow(Symbol('a'), Integer(100))), Pow(Symbol('x'), Integer(100)), Integer(1267650600228229401496703205376)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_5(a:sympy.Rational,b:sympy.Rational):
	#(a**100 > 1267650600228229401496703205377) & (b**100 < 1267650600228229401496703205377)

	pre_cond = And(StrictGreaterThan(Pow(Symbol('a'), Integer(100)), Integer(1267650600228229401496703205377)), StrictLessThan(Pow(Symbol('b'), Integer(100)), Integer(1267650600228229401496703205377)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_6(a:sympy.Rational,b:sympy.Rational):
	#(-b**100 + x**100 + 1267650600228229401496703205376 > 0) & (-a**100 + x**100 + 1267650600228229401496703205376 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('b'), Integer(100))), Pow(Symbol('x'), Integer(100)), Integer(1267650600228229401496703205376)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Pow(Symbol('a'), Integer(100))), Pow(Symbol('x'), Integer(100)), Integer(1267650600228229401496703205376)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_7(a:sympy.Rational,b:sympy.Rational):
	#(a**100 > 1267650600228229401496703205377) & (b**100 < 1267650600228229401496703205377)

	pre_cond = And(StrictGreaterThan(Pow(Symbol('a'), Integer(100)), Integer(1267650600228229401496703205377)), StrictLessThan(Pow(Symbol('b'), Integer(100)), Integer(1267650600228229401496703205377)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_8(a:sympy.Rational,b:sympy.Rational):
	#(-b**100 + x**100 + 1267650600228229401496703205376 > 0) & (-a**100 + x**100 + 1267650600228229401496703205376 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('b'), Integer(100))), Pow(Symbol('x'), Integer(100)), Integer(1267650600228229401496703205376)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Pow(Symbol('a'), Integer(100))), Pow(Symbol('x'), Integer(100)), Integer(1267650600228229401496703205376)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_9(a:sympy.Rational,b:sympy.Rational):
	#(a**100 > 1267650600228229401496703205377) & (b**100 < 1267650600228229401496703205377)

	pre_cond = And(StrictGreaterThan(Pow(Symbol('a'), Integer(100)), Integer(1267650600228229401496703205377)), StrictLessThan(Pow(Symbol('b'), Integer(100)), Integer(1267650600228229401496703205377)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_10(a:sympy.Rational,b:sympy.Rational):
	#(-b**100 + x**100 + 1267650600228229401496703205376 > 0) & (-a**100 + x**100 + 1267650600228229401496703205376 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('b'), Integer(100))), Pow(Symbol('x'), Integer(100)), Integer(1267650600228229401496703205376)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Pow(Symbol('a'), Integer(100))), Pow(Symbol('x'), Integer(100)), Integer(1267650600228229401496703205376)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_11(a:sympy.Rational,b:sympy.Rational):
	#(a**100 > 1267650600228229401496703205377) & (b**100 < 1267650600228229401496703205377)

	pre_cond = And(StrictGreaterThan(Pow(Symbol('a'), Integer(100)), Integer(1267650600228229401496703205377)), StrictLessThan(Pow(Symbol('b'), Integer(100)), Integer(1267650600228229401496703205377)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_12(a:sympy.Rational,b:sympy.Rational):
	#(-b**100 + x**100 + 1267650600228229401496703205376 > 0) & (-a**100 + x**100 + 1267650600228229401496703205376 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('b'), Integer(100))), Pow(Symbol('x'), Integer(100)), Integer(1267650600228229401496703205376)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Pow(Symbol('a'), Integer(100))), Pow(Symbol('x'), Integer(100)), Integer(1267650600228229401496703205376)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_13(a:sympy.Rational,b:sympy.Rational):
	#(a**100 > 1267650600228229401496703205377) & (b**100 < 1267650600228229401496703205377)

	pre_cond = And(StrictGreaterThan(Pow(Symbol('a'), Integer(100)), Integer(1267650600228229401496703205377)), StrictLessThan(Pow(Symbol('b'), Integer(100)), Integer(1267650600228229401496703205377)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_14(a:sympy.Rational,b:sympy.Rational):
	#(-b**100 + x**100 + 1267650600228229401496703205376 > 0) & (-a**100 + x**100 + 1267650600228229401496703205376 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('b'), Integer(100))), Pow(Symbol('x'), Integer(100)), Integer(1267650600228229401496703205376)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Pow(Symbol('a'), Integer(100))), Pow(Symbol('x'), Integer(100)), Integer(1267650600228229401496703205376)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_15(a:sympy.Rational,b:sympy.Rational):
	#(a**100 > 1267650600228229401496703205377) & (b**100 < 1267650600228229401496703205377)

	pre_cond = And(StrictGreaterThan(Pow(Symbol('a'), Integer(100)), Integer(1267650600228229401496703205377)), StrictLessThan(Pow(Symbol('b'), Integer(100)), Integer(1267650600228229401496703205377)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_16(a:sympy.Rational,b:sympy.Rational):
	#(-b**100 + x**100 + 1267650600228229401496703205376 > 0) & (-a**100 + x**100 + 1267650600228229401496703205376 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('b'), Integer(100))), Pow(Symbol('x'), Integer(100)), Integer(1267650600228229401496703205376)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Pow(Symbol('a'), Integer(100))), Pow(Symbol('x'), Integer(100)), Integer(1267650600228229401496703205376)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_17(a:sympy.Rational,b:sympy.Rational):
	#(a**100 > 1267650600228229401496703205377) & (b**100 < 1267650600228229401496703205377)

	pre_cond = And(StrictGreaterThan(Pow(Symbol('a'), Integer(100)), Integer(1267650600228229401496703205377)), StrictLessThan(Pow(Symbol('b'), Integer(100)), Integer(1267650600228229401496703205377)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_18(a:sympy.Rational,b:sympy.Rational):
	#(-b**100 + x**100 + 1267650600228229401496703205376 > 0) & (-a**100 + x**100 + 1267650600228229401496703205376 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('b'), Integer(100))), Pow(Symbol('x'), Integer(100)), Integer(1267650600228229401496703205376)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Pow(Symbol('a'), Integer(100))), Pow(Symbol('x'), Integer(100)), Integer(1267650600228229401496703205376)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_19(a:sympy.Rational,b:sympy.Rational):
	#(a**100 > 1267650600228229401496703205377) & (b**100 < 1267650600228229401496703205377)

	pre_cond = And(StrictGreaterThan(Pow(Symbol('a'), Integer(100)), Integer(1267650600228229401496703205377)), StrictLessThan(Pow(Symbol('b'), Integer(100)), Integer(1267650600228229401496703205377)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_20(a:sympy.Rational,b:sympy.Rational):
	#(-b**100 + x**100 + 1267650600228229401496703205376 > 0) & (-a**100 + x**100 + 1267650600228229401496703205376 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('b'), Integer(100))), Pow(Symbol('x'), Integer(100)), Integer(1267650600228229401496703205376)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Pow(Symbol('a'), Integer(100))), Pow(Symbol('x'), Integer(100)), Integer(1267650600228229401496703205376)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_21(a:sympy.Rational,b:sympy.Rational):
	#(a**100 > 1267650600228229401496703205377) & (b**100 < 1267650600228229401496703205377)

	pre_cond = And(StrictGreaterThan(Pow(Symbol('a'), Integer(100)), Integer(1267650600228229401496703205377)), StrictLessThan(Pow(Symbol('b'), Integer(100)), Integer(1267650600228229401496703205377)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def post_condition(a:sympy.Rational, b:sympy.Rational, y:sympy.Rational, x:sympy.Rational):
	# (0 > -a**100 + x**100 + y**100) & (0 > b**100 - x**100 - y**100)

	post_cond =  And(StrictGreaterThan(Integer(0), Add(Mul(Integer(-1), Pow(Symbol('a'), Integer(100))), Pow(Symbol('x'), Integer(100)), Pow(Symbol('y'), Integer(100)))), StrictGreaterThan(Integer(0), Add(Pow(Symbol('b'), Integer(100)), Mul(Integer(-1), Pow(Symbol('x'), Integer(100))), Mul(Integer(-1), Pow(Symbol('y'), Integer(100))))))

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
		print('y = 1/2')
		print('a = -1')
		print('b = 0')
		exit(0)
	
	
	if pre_condition_1(a=a,b=b)==True:
		print("pre_condition_1 SAT")
		print('x = 1/8')
		print('y = 1/2')
		print('a = -1')
		print('b = 0')
		exit(0)
	
	
	if pre_condition_2(a=a,b=b)==True:
		print("pre_condition_2 SAT")
		print('x = 1')
		print('y = 2')
		print('a = -4')
		print('b = -2')
		exit(0)
	
	
	if pre_condition_3(a=a,b=b)==True:
		print("pre_condition_3 SAT")
		print('x = 1')
		print('y = 2')
		print('a = -4')
		print('b = -2')
		exit(0)
	
	
	if pre_condition_4(a=a,b=b)==True:
		print("pre_condition_4 SAT")
		print('x = 1')
		print('y = 2')
		print('a = -4')
		print('b = -2')
		exit(0)
	
	
	if pre_condition_5(a=a,b=b)==True:
		print("pre_condition_5 SAT")
		print('x = 1')
		print('y = 2')
		print('a = -4')
		print('b = -2')
		exit(0)
	
	
	if pre_condition_6(a=a,b=b)==True:
		print("pre_condition_6 SAT")
		print('x = 1')
		print('y = 2')
		print('a = -4')
		print('b = -2')
		exit(0)
	
	
	if pre_condition_7(a=a,b=b)==True:
		print("pre_condition_7 SAT")
		print('x = 1')
		print('y = 2')
		print('a = -4')
		print('b = -2')
		exit(0)
	
	
	if pre_condition_8(a=a,b=b)==True:
		print("pre_condition_8 SAT")
		print('x = 1')
		print('y = 2')
		print('a = -4')
		print('b = -2')
		exit(0)
	
	
	if pre_condition_9(a=a,b=b)==True:
		print("pre_condition_9 SAT")
		print('x = 1')
		print('y = 2')
		print('a = -4')
		print('b = -2')
		exit(0)
	
	
	if pre_condition_10(a=a,b=b)==True:
		print("pre_condition_10 SAT")
		print('x = 1')
		print('y = 2')
		print('a = -4')
		print('b = -2')
		exit(0)
	
	
	if pre_condition_11(a=a,b=b)==True:
		print("pre_condition_11 SAT")
		print('x = 1')
		print('y = 2')
		print('a = -4')
		print('b = -2')
		exit(0)
	
	
	if pre_condition_12(a=a,b=b)==True:
		print("pre_condition_12 SAT")
		print('x = 1')
		print('y = 2')
		print('a = -4')
		print('b = -2')
		exit(0)
	
	
	if pre_condition_13(a=a,b=b)==True:
		print("pre_condition_13 SAT")
		print('x = 1')
		print('y = 2')
		print('a = -4')
		print('b = -2')
		exit(0)
	
	
	if pre_condition_14(a=a,b=b)==True:
		print("pre_condition_14 SAT")
		print('x = 1')
		print('y = 2')
		print('a = -4')
		print('b = -2')
		exit(0)
	
	
	if pre_condition_15(a=a,b=b)==True:
		print("pre_condition_15 SAT")
		print('x = 1')
		print('y = 2')
		print('a = -4')
		print('b = -2')
		exit(0)
	
	
	if pre_condition_16(a=a,b=b)==True:
		print("pre_condition_16 SAT")
		print('x = 1')
		print('y = 2')
		print('a = -4')
		print('b = -2')
		exit(0)
	
	
	if pre_condition_17(a=a,b=b)==True:
		print("pre_condition_17 SAT")
		print('x = 1')
		print('y = 2')
		print('a = -4')
		print('b = -2')
		exit(0)
	
	
	if pre_condition_18(a=a,b=b)==True:
		print("pre_condition_18 SAT")
		print('x = 1')
		print('y = 2')
		print('a = -4')
		print('b = -2')
		exit(0)
	
	
	if pre_condition_19(a=a,b=b)==True:
		print("pre_condition_19 SAT")
		print('x = 1')
		print('y = 2')
		print('a = -4')
		print('b = -2')
		exit(0)
	
	
	if pre_condition_20(a=a,b=b)==True:
		print("pre_condition_20 SAT")
		print('x = 1')
		print('y = 2')
		print('a = -4')
		print('b = -2')
		exit(0)
	
	
	if pre_condition_21(a=a,b=b)==True:
		print("pre_condition_21 SAT")
		print('x = 1')
		print('y = 2')
		print('a = -4')
		print('b = -2')
		exit(0)


	print("UNKNOWN")
	exit(0)
