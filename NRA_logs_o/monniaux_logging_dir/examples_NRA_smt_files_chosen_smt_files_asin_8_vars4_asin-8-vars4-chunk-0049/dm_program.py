import sympy
from sympy import *

def pre_condition_0(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (63*skoS2/20 - skoSM*(126*skoS2 + 61)/40 + 73/40 < skoX*(40*skoSM + skoX*(126*skoS2 - skoSM*(126*skoS2 + 61) + 73) + 200)/40)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictLessThan(Add(Mul(Rational(63, 20), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(73, 40)), Mul(Rational(1, 40), Symbol('skoX'), Add(Mul(Integer(40), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(126), Symbol('skoS2')), Mul(Integer(-1), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(73))), Integer(200)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (skoX**2 + 20*skoX > 1)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Pow(Symbol('skoX'), Integer(2)), Mul(Integer(20), Symbol('skoX'))), Integer(1)))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_2(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoSM > 0) & (skoX > 0) & (skoX < 1) & (63*skoS2/40 - skoSM*(126*skoS2 + 61)/40 + 81/80 < skoX*(80*skoSM + skoX*(126*skoS2 - 2*skoSM*(126*skoS2 + 61) + 81) + 360)/80)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictLessThan(Add(Mul(Rational(63, 40), Symbol('skoS2')), Mul(Integer(-1), Rational(1, 40), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Rational(81, 80)), Mul(Rational(1, 80), Symbol('skoX'), Add(Mul(Integer(80), Symbol('skoSM')), Mul(Symbol('skoX'), Add(Mul(Integer(126), Symbol('skoS2')), Mul(Integer(-1), Integer(2), Symbol('skoSM'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(61))), Integer(81))), Integer(360)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_3(delta:sympy.Rational,skoX:sympy.Rational,skoS2:sympy.Rational):
	#(delta >= 0) & (skoS2 > 0) & (skoX > 0) & (skoX < 1) & (63*skoS2/40 + 41/80 > skoX*(skoX*(126*skoS2 + 41) - 440)/80)

	pre_cond = And(GreaterThan(Symbol('delta'), Integer(0)), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictLessThan(Symbol('skoX'), Integer(1)), StrictGreaterThan(Add(Mul(Rational(63, 40), Symbol('skoS2')), Rational(41, 80)), Mul(Rational(1, 80), Symbol('skoX'), Add(Mul(Symbol('skoX'), Add(Mul(Integer(126), Symbol('skoS2')), Integer(41))), Integer(-440)))))

	eval = pre_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2 })

	if eval==True:
		assert eval!=False
		return True
	return False


def post_condition(delta:sympy.Rational, skoX:sympy.Rational, skoS2:sympy.Rational, skoSP:sympy.Rational, skoSM:sympy.Rational):
	# (0 <= delta) & (1 > skoX) & (skoS2 > 0) & (skoSM > 0) & (skoSP > 0) & (skoX > 0) & (skoX*(skoSM + skoSP + skoX*(skoSM*(-63*skoS2/20 - 61/40) + skoSP*(63*skoS2/20 + 13/8) + 1/5) + 4) > skoSM*(-63*skoS2/20 - 61/40) + skoSP*(63*skoS2/20 + 13/8) + 1/5)

	post_cond =  And(LessThan(Integer(0), Symbol('delta')), StrictGreaterThan(Integer(1), Symbol('skoX')), StrictGreaterThan(Symbol('skoS2'), Integer(0)), StrictGreaterThan(Symbol('skoSM'), Integer(0)), StrictGreaterThan(Symbol('skoSP'), Integer(0)), StrictGreaterThan(Symbol('skoX'), Integer(0)), StrictGreaterThan(Mul(Symbol('skoX'), Add(Symbol('skoSM'), Symbol('skoSP'), Mul(Symbol('skoX'), Add(Mul(Symbol('skoSM'), Add(Mul(Integer(-1), Rational(63, 20), Symbol('skoS2')), Rational(-61, 40))), Mul(Symbol('skoSP'), Add(Mul(Rational(63, 20), Symbol('skoS2')), Rational(13, 8))), Rational(1, 5))), Integer(4))), Add(Mul(Symbol('skoSM'), Add(Mul(Integer(-1), Rational(63, 20), Symbol('skoS2')), Rational(-61, 40))), Mul(Symbol('skoSP'), Add(Mul(Rational(63, 20), Symbol('skoS2')), Rational(13, 8))), Rational(1, 5))))

	eval = post_cond.subs( { 'delta':delta, 'skoX':skoX, 'skoS2':skoS2, 'skoSP':skoSP, 'skoSM':skoSM })

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
	
	
	
	
	if pre_condition_0(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_0 SAT")
		print('delta = 0')
		print('skoX = 1/2')
		print('skoS2 = 1')
		print('skoSM = 1')
		print('skoSP = 1')
		exit(0)
	
	
	if pre_condition_1(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_1 SAT")
		print('delta = 0')
		print('skoX = 1/2')
		print('skoS2 = 1')
		print('skoSM = 1')
		print('skoSP = 1')
		exit(0)
	
	
	if pre_condition_2(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_2 SAT")
		print('delta = 0')
		print('skoX = 1/32')
		print('skoS2 = 1')
		print('skoSM = 1')
		print('skoSP = 1/2')
		exit(0)
	
	
	if pre_condition_3(delta=delta,skoX=skoX,skoS2=skoS2)==True:
		print("pre_condition_3 SAT")
		print('delta = 0')
		print('skoX = 1/32')
		print('skoS2 = 1')
		print('skoSM = 1')
		print('skoSP = 1/2')
		exit(0)


	print("Weakest pre-condition UNSAT")
	exit(0)
