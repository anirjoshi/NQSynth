import sympy
from sympy import *

def pre_condition_0(a:sympy.Rational):
	#(4*a - y**3 + 2*y - 1/4 > 0) & (a*y**2 + a - z**2 + 1/4 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(4), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-1, 4)), Integer(0)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(2))), Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(1, 4)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1(a:sympy.Rational):
	#(a > 1/2048) & (65*a/64 - z**2 + 1/4 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(1, 2048)), StrictLessThan(Add(Mul(Rational(65, 64), Symbol('a')), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(1, 4)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_2(a:sympy.Rational):
	#(a > 1/2048) & (a < 48/65)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(1, 2048)), StrictLessThan(Symbol('a'), Rational(48, 65)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_3(a:sympy.Rational):
	#(3*a - y**3 + 2*y > 0) & (a*y**2 + a - z**2 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(3), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y'))), Integer(0)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(2))), Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2)))), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_4(a:sympy.Rational):
	#(a > -7/24) & (5*a/4 - z**2 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(-7, 24)), StrictLessThan(Add(Mul(Rational(5, 4), Symbol('a')), Mul(Integer(-1), Pow(Symbol('z'), Integer(2)))), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_5(a:sympy.Rational):
	#(a > -7/24) & (a < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(-7, 24)), StrictLessThan(Symbol('a'), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_6(a:sympy.Rational):
	#(a + y**3 - 2*y + 4 < 0) & (a*y**2 + a - z**2 + 4 < 0)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Pow(Symbol('y'), Integer(3)), Mul(Integer(-1), Integer(2), Symbol('y')), Integer(4)), Integer(0)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(2))), Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Integer(4)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_7(a:sympy.Rational):
	#(a < -5) & (2*a - z**2 + 4 < 0)

	pre_cond = And(StrictLessThan(Symbol('a'), Integer(-5)), StrictLessThan(Add(Mul(Integer(2), Symbol('a')), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Integer(4)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_8(a:sympy.Rational):
	#a < -5

	pre_cond = StrictLessThan(Symbol('a'), Integer(-5))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_9(a:sympy.Rational):
	#(a - y**3 + 2*y - 1 > 0) & (a*y**2 + a - z**2 + 1 < 0)

	pre_cond = And(StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Integer(-1)), Integer(0)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(2))), Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_10(a:sympy.Rational):
	#(a > -55/64) & (65*a/16 - z**2 + 1 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(-55, 64)), StrictLessThan(Add(Mul(Rational(65, 16), Symbol('a')), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Integer(1)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_11(a:sympy.Rational):
	#(a > -55/64) & (a < -12/65)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(-55, 64)), StrictLessThan(Symbol('a'), Rational(-12, 65)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_12(a:sympy.Rational):
	#(41*a/32 - y**3 + 2*y - 3025/4096 > 0) & (a*y**2 + a - z**2 + 3025/4096 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Rational(41, 32), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-3025, 4096)), Integer(0)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(2))), Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(3025, 4096)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_13(a:sympy.Rational):
	#(a > -4591/5248) & (65*a/16 - z**2 + 3025/4096 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(-4591, 5248)), StrictLessThan(Add(Mul(Rational(65, 16), Symbol('a')), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(3025, 4096)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_14(a:sympy.Rational):
	#(a > -4591/5248) & (a < -605/3328)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(-4591, 5248)), StrictLessThan(Symbol('a'), Rational(-605, 3328)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_15(a:sympy.Rational):
	#(6251905487804879*a/5000000000000000 - y**3 + 2*y - 76529157594298392042589976204641/100000000000000000000000000000000 > 0) & (a*y**2 + a - z**2 + 76529157594298392042589976204641/100000000000000000000000000000000 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Rational(6251905487804879, 5000000000000000), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-76529157594298392042589976204641, 100000000000000000000000000000000)), Integer(0)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(2))), Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(76529157594298392042589976204641, 100000000000000000000000000000000)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_16(a:sympy.Rational):
	#(a > -109408342405701607957410023795359/125038109756097580000000000000000) & (65*a/16 - z**2 + 76529157594298392042589976204641/100000000000000000000000000000000 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(-109408342405701607957410023795359, 125038109756097580000000000000000)), StrictLessThan(Add(Mul(Rational(65, 16), Symbol('a')), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(76529157594298392042589976204641, 100000000000000000000000000000000)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_17(a:sympy.Rational):
	#(a > -109408342405701607957410023795359/125038109756097580000000000000000) & (a < -76529157594298392042589976204641/406250000000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(-109408342405701607957410023795359, 125038109756097580000000000000000)), StrictLessThan(Symbol('a'), Rational(-76529157594298392042589976204641, 406250000000000000000000000000000)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_18(a:sympy.Rational):
	#(625000029038217*a/500000000000000 - y**3 + 2*y - 765624949183121093218046539089/1000000000000000000000000000000 > 0) & (a*y**2 + a - z**2 + 765624949183121093218046539089/1000000000000000000000000000000 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Rational(625000029038217, 500000000000000), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-765624949183121093218046539089, 1000000000000000000000000000000)), Integer(0)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(2))), Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(765624949183121093218046539089, 1000000000000000000000000000000)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_19(a:sympy.Rational):
	#(a > -1093750050816878906781953460911/1250000058076434000000000000000) & (65*a/16 - z**2 + 765624949183121093218046539089/1000000000000000000000000000000 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(-1093750050816878906781953460911, 1250000058076434000000000000000)), StrictLessThan(Add(Mul(Rational(65, 16), Symbol('a')), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(765624949183121093218046539089, 1000000000000000000000000000000)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_20(a:sympy.Rational):
	#(a > -1093750050816878906781953460911/1250000058076434000000000000000) & (a < -765624949183121093218046539089/4062500000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(-1093750050816878906781953460911, 1250000058076434000000000000000)), StrictLessThan(Symbol('a'), Rational(-765624949183121093218046539089, 4062500000000000000000000000000)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_21(a:sympy.Rational):
	#(6250000000000007*a/5000000000000000 - y**3 + 2*y - 76562499999999877500000000000049/100000000000000000000000000000000 > 0) & (a*y**2 + a - z**2 + 76562499999999877500000000000049/100000000000000000000000000000000 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Rational(6250000000000007, 5000000000000000), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-76562499999999877500000000000049, 100000000000000000000000000000000)), Integer(0)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(2))), Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(76562499999999877500000000000049, 100000000000000000000000000000000)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_22(a:sympy.Rational):
	#(a > -109375000000000122499999999999951/125000000000000140000000000000000) & (65*a/16 - z**2 + 76562499999999877500000000000049/100000000000000000000000000000000 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(-109375000000000122499999999999951, 125000000000000140000000000000000)), StrictLessThan(Add(Mul(Rational(65, 16), Symbol('a')), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(76562499999999877500000000000049, 100000000000000000000000000000000)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_23(a:sympy.Rational):
	#(a > -109375000000000122499999999999951/125000000000000140000000000000000) & (a < -76562499999999877500000000000049/406250000000000000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(-109375000000000122499999999999951, 125000000000000140000000000000000)), StrictLessThan(Symbol('a'), Rational(-76562499999999877500000000000049, 406250000000000000000000000000000)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_24(a:sympy.Rational):
	#(19*a/16 - y**3 + 2*y - 841/1024 > 0) & (a*y**2 + a - z**2 + 841/1024 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Rational(19, 16), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-841, 1024)), Integer(0)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(2))), Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(841, 1024)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_25(a:sympy.Rational):
	#(a > -2295457/2490368) & (67009*a/16384 - z**2 + 841/1024 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(-2295457, 2490368)), StrictLessThan(Add(Mul(Rational(67009, 16384), Symbol('a')), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(841, 1024)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_26(a:sympy.Rational):
	#(a > -2295457/2490368) & (a < -13456/67009)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(-2295457, 2490368)), StrictLessThan(Symbol('a'), Rational(-13456, 67009)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_27(a:sympy.Rational):
	#(2891329715126439*a/2500000000000000 - y**3 + 2*y - 21239841794676549900685756820721/25000000000000000000000000000000 > 0) & (a*y**2 + a - z**2 + 21239841794676549900685756820721/25000000000000000000000000000000 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Rational(2891329715126439, 2500000000000000), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-21239841794676549900685756820721, 25000000000000000000000000000000)), Integer(0)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(2))), Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(21239841794676549900685756820721, 25000000000000000000000000000000)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_28(a:sympy.Rational):
	#(a > -2961818287140024186382138131031/3212588572362710000000000000000) & (67009*a/16384 - z**2 + 21239841794676549900685756820721/25000000000000000000000000000000 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(-2961818287140024186382138131031, 3212588572362710000000000000000)), StrictLessThan(Add(Mul(Rational(67009, 16384), Symbol('a')), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(21239841794676549900685756820721, 25000000000000000000000000000000)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_29(a:sympy.Rational):
	#(a > -2961818287140024186382138131031/3212588572362710000000000000000) & (a < -21239841794676549900685756820721/102247619628906250000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(-2961818287140024186382138131031, 3212588572362710000000000000000)), StrictLessThan(Symbol('a'), Rational(-21239841794676549900685756820721, 102247619628906250000000000000000)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_30(a:sympy.Rational):
	#(5780586370069343*a/5000000000000000 - y**3 + 2*y - 84997587679751173301314628451649/100000000000000000000000000000000 > 0) & (a*y**2 + a - z**2 + 84997587679751173301314628451649/100000000000000000000000000000000 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Rational(5780586370069343, 5000000000000000), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-84997587679751173301314628451649, 100000000000000000000000000000000)), Integer(0)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(2))), Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(84997587679751173301314628451649, 100000000000000000000000000000000)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_31(a:sympy.Rational):
	#(a > -106587237835995897011185371548351/115611727401386860000000000000000) & (67009*a/16384 - z**2 + 84997587679751173301314628451649/100000000000000000000000000000000 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(-106587237835995897011185371548351, 115611727401386860000000000000000)), StrictLessThan(Add(Mul(Rational(67009, 16384), Symbol('a')), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(84997587679751173301314628451649, 100000000000000000000000000000000)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_32(a:sympy.Rational):
	#(a > -106587237835995897011185371548351/115611727401386860000000000000000) & (a < -84997587679751173301314628451649/408990478515625000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(-106587237835995897011185371548351, 115611727401386860000000000000000)), StrictLessThan(Symbol('a'), Rational(-84997587679751173301314628451649, 408990478515625000000000000000000)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_33(a:sympy.Rational):
	#(1156117199668841*a/1000000000000000 - y**3 + 2*y - 3399903781357076768440066283281/4000000000000000000000000000000 > 0) & (a*y**2 + a - z**2 + 3399903781357076768440066283281/4000000000000000000000000000000 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Rational(1156117199668841, 1000000000000000), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-3399903781357076768440066283281, 4000000000000000000000000000000)), Integer(0)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(2))), Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(3399903781357076768440066283281, 4000000000000000000000000000000)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_34(a:sympy.Rational):
	#(a > -4263489239272806044059933716719/4624468798675364000000000000000) & (67009*a/16384 - z**2 + 3399903781357076768440066283281/4000000000000000000000000000000 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(-4263489239272806044059933716719, 4624468798675364000000000000000)), StrictLessThan(Add(Mul(Rational(67009, 16384), Symbol('a')), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(3399903781357076768440066283281, 4000000000000000000000000000000)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_35(a:sympy.Rational):
	#(a > -4263489239272806044059933716719/4624468798675364000000000000000) & (a < -3399903781357076768440066283281/16359619140625000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(-4263489239272806044059933716719, 4624468798675364000000000000000)), StrictLessThan(Symbol('a'), Rational(-3399903781357076768440066283281, 16359619140625000000000000000000)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_36(a:sympy.Rational):
	#(5780585998344193*a/5000000000000000 - y**3 + 2*y - 84997594533927140476937696821249/100000000000000000000000000000000 > 0) & (a*y**2 + a - z**2 + 84997594533927140476937696821249/100000000000000000000000000000000 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Rational(5780585998344193, 5000000000000000), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-84997594533927140476937696821249, 100000000000000000000000000000000)), Integer(0)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(2))), Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(84997594533927140476937696821249, 100000000000000000000000000000000)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_37(a:sympy.Rational):
	#(a > -106587230981819929835562303178751/115611719966883860000000000000000) & (67009*a/16384 - z**2 + 84997594533927140476937696821249/100000000000000000000000000000000 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(-106587230981819929835562303178751, 115611719966883860000000000000000)), StrictLessThan(Add(Mul(Rational(67009, 16384), Symbol('a')), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(84997594533927140476937696821249, 100000000000000000000000000000000)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_38(a:sympy.Rational):
	#(a > -106587230981819929835562303178751/115611719966883860000000000000000) & (a < -84997594533927140476937696821249/408990478515625000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(-106587230981819929835562303178751, 115611719966883860000000000000000)), StrictLessThan(Symbol('a'), Rational(-84997594533927140476937696821249, 408990478515625000000000000000000)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_39(a:sympy.Rational):
	#(5780585998344193*a/5000000000000000 - y**3 + 2*y - 84997594533927140476937696821249/100000000000000000000000000000000 > 0) & (a*y**2 + a - z**2 + 84997594533927140476937696821249/100000000000000000000000000000000 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Rational(5780585998344193, 5000000000000000), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-84997594533927140476937696821249, 100000000000000000000000000000000)), Integer(0)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(2))), Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(84997594533927140476937696821249, 100000000000000000000000000000000)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_40(a:sympy.Rational):
	#(a > -106587230981819929835562303178751/115611719966883860000000000000000) & (67009*a/16384 - z**2 + 84997594533927140476937696821249/100000000000000000000000000000000 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(-106587230981819929835562303178751, 115611719966883860000000000000000)), StrictLessThan(Add(Mul(Rational(67009, 16384), Symbol('a')), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(84997594533927140476937696821249, 100000000000000000000000000000000)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_41(a:sympy.Rational):
	#(a > -106587230981819929835562303178751/115611719966883860000000000000000) & (a < -84997594533927140476937696821249/408990478515625000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(-106587230981819929835562303178751, 115611719966883860000000000000000)), StrictLessThan(Symbol('a'), Rational(-84997594533927140476937696821249, 408990478515625000000000000000000)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_42(a:sympy.Rational):
	#(5780585998344193*a/5000000000000000 - y**3 + 2*y - 84997594533927140476937696821249/100000000000000000000000000000000 > 0) & (a*y**2 + a - z**2 + 84997594533927140476937696821249/100000000000000000000000000000000 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Rational(5780585998344193, 5000000000000000), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-84997594533927140476937696821249, 100000000000000000000000000000000)), Integer(0)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(2))), Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(84997594533927140476937696821249, 100000000000000000000000000000000)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_43(a:sympy.Rational):
	#(a > -106587230981819929835562303178751/115611719966883860000000000000000) & (67009*a/16384 - z**2 + 84997594533927140476937696821249/100000000000000000000000000000000 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(-106587230981819929835562303178751, 115611719966883860000000000000000)), StrictLessThan(Add(Mul(Rational(67009, 16384), Symbol('a')), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(84997594533927140476937696821249, 100000000000000000000000000000000)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_44(a:sympy.Rational):
	#(a > -106587230981819929835562303178751/115611719966883860000000000000000) & (a < -84997594533927140476937696821249/408990478515625000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(-106587230981819929835562303178751, 115611719966883860000000000000000)), StrictLessThan(Symbol('a'), Rational(-84997594533927140476937696821249, 408990478515625000000000000000000)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_45(a:sympy.Rational):
	#(5780585998344193*a/5000000000000000 - y**3 + 2*y - 84997594533927140476937696821249/100000000000000000000000000000000 > 0) & (a*y**2 + a - z**2 + 84997594533927140476937696821249/100000000000000000000000000000000 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Rational(5780585998344193, 5000000000000000), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-84997594533927140476937696821249, 100000000000000000000000000000000)), Integer(0)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(2))), Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(84997594533927140476937696821249, 100000000000000000000000000000000)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_46(a:sympy.Rational):
	#(a > -106587230981819929835562303178751/115611719966883860000000000000000) & (67009*a/16384 - z**2 + 84997594533927140476937696821249/100000000000000000000000000000000 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(-106587230981819929835562303178751, 115611719966883860000000000000000)), StrictLessThan(Add(Mul(Rational(67009, 16384), Symbol('a')), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(84997594533927140476937696821249, 100000000000000000000000000000000)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_47(a:sympy.Rational):
	#(a > -106587230981819929835562303178751/115611719966883860000000000000000) & (a < -84997594533927140476937696821249/408990478515625000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(-106587230981819929835562303178751, 115611719966883860000000000000000)), StrictLessThan(Symbol('a'), Rational(-84997594533927140476937696821249, 408990478515625000000000000000000)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_48(a:sympy.Rational):
	#(5780585998344193*a/5000000000000000 - y**3 + 2*y - 84997594533927140476937696821249/100000000000000000000000000000000 > 0) & (a*y**2 + a - z**2 + 84997594533927140476937696821249/100000000000000000000000000000000 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Rational(5780585998344193, 5000000000000000), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-84997594533927140476937696821249, 100000000000000000000000000000000)), Integer(0)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(2))), Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(84997594533927140476937696821249, 100000000000000000000000000000000)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_49(a:sympy.Rational):
	#(a > -106587230981819929835562303178751/115611719966883860000000000000000) & (67009*a/16384 - z**2 + 84997594533927140476937696821249/100000000000000000000000000000000 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(-106587230981819929835562303178751, 115611719966883860000000000000000)), StrictLessThan(Add(Mul(Rational(67009, 16384), Symbol('a')), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(84997594533927140476937696821249, 100000000000000000000000000000000)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_50(a:sympy.Rational):
	#(a > -106587230981819929835562303178751/115611719966883860000000000000000) & (a < -84997594533927140476937696821249/408990478515625000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(-106587230981819929835562303178751, 115611719966883860000000000000000)), StrictLessThan(Symbol('a'), Rational(-84997594533927140476937696821249, 408990478515625000000000000000000)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_51(a:sympy.Rational):
	#(5780585998344193*a/5000000000000000 - y**3 + 2*y - 84997594533927140476937696821249/100000000000000000000000000000000 > 0) & (a*y**2 + a - z**2 + 84997594533927140476937696821249/100000000000000000000000000000000 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Rational(5780585998344193, 5000000000000000), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-84997594533927140476937696821249, 100000000000000000000000000000000)), Integer(0)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(2))), Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(84997594533927140476937696821249, 100000000000000000000000000000000)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_52(a:sympy.Rational):
	#(a > -106587230981819929835562303178751/115611719966883860000000000000000) & (67009*a/16384 - z**2 + 84997594533927140476937696821249/100000000000000000000000000000000 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(-106587230981819929835562303178751, 115611719966883860000000000000000)), StrictLessThan(Add(Mul(Rational(67009, 16384), Symbol('a')), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(84997594533927140476937696821249, 100000000000000000000000000000000)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_53(a:sympy.Rational):
	#(a > -106587230981819929835562303178751/115611719966883860000000000000000) & (a < -84997594533927140476937696821249/408990478515625000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(-106587230981819929835562303178751, 115611719966883860000000000000000)), StrictLessThan(Symbol('a'), Rational(-84997594533927140476937696821249, 408990478515625000000000000000000)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_54(a:sympy.Rational):
	#(5780585998344193*a/5000000000000000 - y**3 + 2*y - 84997594533927140476937696821249/100000000000000000000000000000000 > 0) & (a*y**2 + a - z**2 + 84997594533927140476937696821249/100000000000000000000000000000000 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Rational(5780585998344193, 5000000000000000), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-84997594533927140476937696821249, 100000000000000000000000000000000)), Integer(0)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(2))), Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(84997594533927140476937696821249, 100000000000000000000000000000000)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_55(a:sympy.Rational):
	#(a > -106587230981819929835562303178751/115611719966883860000000000000000) & (67009*a/16384 - z**2 + 84997594533927140476937696821249/100000000000000000000000000000000 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(-106587230981819929835562303178751, 115611719966883860000000000000000)), StrictLessThan(Add(Mul(Rational(67009, 16384), Symbol('a')), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(84997594533927140476937696821249, 100000000000000000000000000000000)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_56(a:sympy.Rational):
	#(a > -106587230981819929835562303178751/115611719966883860000000000000000) & (a < -84997594533927140476937696821249/408990478515625000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(-106587230981819929835562303178751, 115611719966883860000000000000000)), StrictLessThan(Symbol('a'), Rational(-84997594533927140476937696821249, 408990478515625000000000000000000)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_57(a:sympy.Rational):
	#(5780585998344193*a/5000000000000000 - y**3 + 2*y - 84997594533927140476937696821249/100000000000000000000000000000000 > 0) & (a*y**2 + a - z**2 + 84997594533927140476937696821249/100000000000000000000000000000000 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Rational(5780585998344193, 5000000000000000), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-84997594533927140476937696821249, 100000000000000000000000000000000)), Integer(0)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(2))), Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(84997594533927140476937696821249, 100000000000000000000000000000000)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_58(a:sympy.Rational):
	#(a > -106587230981819929835562303178751/115611719966883860000000000000000) & (67009*a/16384 - z**2 + 84997594533927140476937696821249/100000000000000000000000000000000 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(-106587230981819929835562303178751, 115611719966883860000000000000000)), StrictLessThan(Add(Mul(Rational(67009, 16384), Symbol('a')), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(84997594533927140476937696821249, 100000000000000000000000000000000)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_59(a:sympy.Rational):
	#(a > -106587230981819929835562303178751/115611719966883860000000000000000) & (a < -84997594533927140476937696821249/408990478515625000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(-106587230981819929835562303178751, 115611719966883860000000000000000)), StrictLessThan(Symbol('a'), Rational(-84997594533927140476937696821249, 408990478515625000000000000000000)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_60(a:sympy.Rational):
	#(5780585998344193*a/5000000000000000 - y**3 + 2*y - 84997594533927140476937696821249/100000000000000000000000000000000 > 0) & (a*y**2 + a - z**2 + 84997594533927140476937696821249/100000000000000000000000000000000 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Rational(5780585998344193, 5000000000000000), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-84997594533927140476937696821249, 100000000000000000000000000000000)), Integer(0)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(2))), Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(84997594533927140476937696821249, 100000000000000000000000000000000)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_61(a:sympy.Rational):
	#(a > -106587230981819929835562303178751/115611719966883860000000000000000) & (67009*a/16384 - z**2 + 84997594533927140476937696821249/100000000000000000000000000000000 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(-106587230981819929835562303178751, 115611719966883860000000000000000)), StrictLessThan(Add(Mul(Rational(67009, 16384), Symbol('a')), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(84997594533927140476937696821249, 100000000000000000000000000000000)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_62(a:sympy.Rational):
	#(a > -106587230981819929835562303178751/115611719966883860000000000000000) & (a < -84997594533927140476937696821249/408990478515625000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(-106587230981819929835562303178751, 115611719966883860000000000000000)), StrictLessThan(Symbol('a'), Rational(-84997594533927140476937696821249, 408990478515625000000000000000000)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_63(a:sympy.Rational):
	#(5780585998344193*a/5000000000000000 - y**3 + 2*y - 84997594533927140476937696821249/100000000000000000000000000000000 > 0) & (a*y**2 + a - z**2 + 84997594533927140476937696821249/100000000000000000000000000000000 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Rational(5780585998344193, 5000000000000000), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-84997594533927140476937696821249, 100000000000000000000000000000000)), Integer(0)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(2))), Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(84997594533927140476937696821249, 100000000000000000000000000000000)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_64(a:sympy.Rational):
	#(a > -106587230981819929835562303178751/115611719966883860000000000000000) & (67009*a/16384 - z**2 + 84997594533927140476937696821249/100000000000000000000000000000000 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(-106587230981819929835562303178751, 115611719966883860000000000000000)), StrictLessThan(Add(Mul(Rational(67009, 16384), Symbol('a')), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(84997594533927140476937696821249, 100000000000000000000000000000000)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_65(a:sympy.Rational):
	#(a > -106587230981819929835562303178751/115611719966883860000000000000000) & (a < -84997594533927140476937696821249/408990478515625000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(-106587230981819929835562303178751, 115611719966883860000000000000000)), StrictLessThan(Symbol('a'), Rational(-84997594533927140476937696821249, 408990478515625000000000000000000)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_66(a:sympy.Rational):
	#(5780585998344193*a/5000000000000000 - y**3 + 2*y - 84997594533927140476937696821249/100000000000000000000000000000000 > 0) & (a*y**2 + a - z**2 + 84997594533927140476937696821249/100000000000000000000000000000000 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Rational(5780585998344193, 5000000000000000), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-84997594533927140476937696821249, 100000000000000000000000000000000)), Integer(0)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(2))), Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(84997594533927140476937696821249, 100000000000000000000000000000000)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_67(a:sympy.Rational):
	#(a > -106587230981819929835562303178751/115611719966883860000000000000000) & (67009*a/16384 - z**2 + 84997594533927140476937696821249/100000000000000000000000000000000 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(-106587230981819929835562303178751, 115611719966883860000000000000000)), StrictLessThan(Add(Mul(Rational(67009, 16384), Symbol('a')), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(84997594533927140476937696821249, 100000000000000000000000000000000)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_68(a:sympy.Rational):
	#(a > -106587230981819929835562303178751/115611719966883860000000000000000) & (a < -84997594533927140476937696821249/408990478515625000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(-106587230981819929835562303178751, 115611719966883860000000000000000)), StrictLessThan(Symbol('a'), Rational(-84997594533927140476937696821249, 408990478515625000000000000000000)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_69(a:sympy.Rational):
	#(5780585998344193*a/5000000000000000 - y**3 + 2*y - 84997594533927140476937696821249/100000000000000000000000000000000 > 0) & (a*y**2 + a - z**2 + 84997594533927140476937696821249/100000000000000000000000000000000 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Rational(5780585998344193, 5000000000000000), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-84997594533927140476937696821249, 100000000000000000000000000000000)), Integer(0)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(2))), Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(84997594533927140476937696821249, 100000000000000000000000000000000)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_70(a:sympy.Rational):
	#(a > -106587230981819929835562303178751/115611719966883860000000000000000) & (67009*a/16384 - z**2 + 84997594533927140476937696821249/100000000000000000000000000000000 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(-106587230981819929835562303178751, 115611719966883860000000000000000)), StrictLessThan(Add(Mul(Rational(67009, 16384), Symbol('a')), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(84997594533927140476937696821249, 100000000000000000000000000000000)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_71(a:sympy.Rational):
	#(a > -106587230981819929835562303178751/115611719966883860000000000000000) & (a < -84997594533927140476937696821249/408990478515625000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(-106587230981819929835562303178751, 115611719966883860000000000000000)), StrictLessThan(Symbol('a'), Rational(-84997594533927140476937696821249, 408990478515625000000000000000000)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_72(a:sympy.Rational):
	#(5780585998344193*a/5000000000000000 - y**3 + 2*y - 84997594533927140476937696821249/100000000000000000000000000000000 > 0) & (a*y**2 + a - z**2 + 84997594533927140476937696821249/100000000000000000000000000000000 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Rational(5780585998344193, 5000000000000000), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-84997594533927140476937696821249, 100000000000000000000000000000000)), Integer(0)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(2))), Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(84997594533927140476937696821249, 100000000000000000000000000000000)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_73(a:sympy.Rational):
	#(a > -106587230981819929835562303178751/115611719966883860000000000000000) & (67009*a/16384 - z**2 + 84997594533927140476937696821249/100000000000000000000000000000000 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(-106587230981819929835562303178751, 115611719966883860000000000000000)), StrictLessThan(Add(Mul(Rational(67009, 16384), Symbol('a')), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(84997594533927140476937696821249, 100000000000000000000000000000000)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_74(a:sympy.Rational):
	#(a > -106587230981819929835562303178751/115611719966883860000000000000000) & (a < -84997594533927140476937696821249/408990478515625000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(-106587230981819929835562303178751, 115611719966883860000000000000000)), StrictLessThan(Symbol('a'), Rational(-84997594533927140476937696821249, 408990478515625000000000000000000)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_75(a:sympy.Rational):
	#(5780585998344193*a/5000000000000000 - y**3 + 2*y - 84997594533927140476937696821249/100000000000000000000000000000000 > 0) & (a*y**2 + a - z**2 + 84997594533927140476937696821249/100000000000000000000000000000000 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Rational(5780585998344193, 5000000000000000), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-84997594533927140476937696821249, 100000000000000000000000000000000)), Integer(0)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(2))), Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(84997594533927140476937696821249, 100000000000000000000000000000000)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_76(a:sympy.Rational):
	#(a > -106587230981819929835562303178751/115611719966883860000000000000000) & (67009*a/16384 - z**2 + 84997594533927140476937696821249/100000000000000000000000000000000 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(-106587230981819929835562303178751, 115611719966883860000000000000000)), StrictLessThan(Add(Mul(Rational(67009, 16384), Symbol('a')), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(84997594533927140476937696821249, 100000000000000000000000000000000)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_77(a:sympy.Rational):
	#(a > -106587230981819929835562303178751/115611719966883860000000000000000) & (a < -84997594533927140476937696821249/408990478515625000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(-106587230981819929835562303178751, 115611719966883860000000000000000)), StrictLessThan(Symbol('a'), Rational(-84997594533927140476937696821249, 408990478515625000000000000000000)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_78(a:sympy.Rational):
	#(5780585998344193*a/5000000000000000 - y**3 + 2*y - 84997594533927140476937696821249/100000000000000000000000000000000 > 0) & (a*y**2 + a - z**2 + 84997594533927140476937696821249/100000000000000000000000000000000 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Rational(5780585998344193, 5000000000000000), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-84997594533927140476937696821249, 100000000000000000000000000000000)), Integer(0)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(2))), Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(84997594533927140476937696821249, 100000000000000000000000000000000)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_79(a:sympy.Rational):
	#(a > -106587230981819929835562303178751/115611719966883860000000000000000) & (67009*a/16384 - z**2 + 84997594533927140476937696821249/100000000000000000000000000000000 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(-106587230981819929835562303178751, 115611719966883860000000000000000)), StrictLessThan(Add(Mul(Rational(67009, 16384), Symbol('a')), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(84997594533927140476937696821249, 100000000000000000000000000000000)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_80(a:sympy.Rational):
	#(a > -106587230981819929835562303178751/115611719966883860000000000000000) & (a < -84997594533927140476937696821249/408990478515625000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(-106587230981819929835562303178751, 115611719966883860000000000000000)), StrictLessThan(Symbol('a'), Rational(-84997594533927140476937696821249, 408990478515625000000000000000000)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_81(a:sympy.Rational):
	#(5780585998344193*a/5000000000000000 - y**3 + 2*y - 84997594533927140476937696821249/100000000000000000000000000000000 > 0) & (a*y**2 + a - z**2 + 84997594533927140476937696821249/100000000000000000000000000000000 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Rational(5780585998344193, 5000000000000000), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-84997594533927140476937696821249, 100000000000000000000000000000000)), Integer(0)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(2))), Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(84997594533927140476937696821249, 100000000000000000000000000000000)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_82(a:sympy.Rational):
	#(a > -106587230981819929835562303178751/115611719966883860000000000000000) & (67009*a/16384 - z**2 + 84997594533927140476937696821249/100000000000000000000000000000000 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(-106587230981819929835562303178751, 115611719966883860000000000000000)), StrictLessThan(Add(Mul(Rational(67009, 16384), Symbol('a')), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(84997594533927140476937696821249, 100000000000000000000000000000000)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_83(a:sympy.Rational):
	#(a > -106587230981819929835562303178751/115611719966883860000000000000000) & (a < -84997594533927140476937696821249/408990478515625000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(-106587230981819929835562303178751, 115611719966883860000000000000000)), StrictLessThan(Symbol('a'), Rational(-84997594533927140476937696821249, 408990478515625000000000000000000)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_84(a:sympy.Rational):
	#(5780585998344193*a/5000000000000000 - y**3 + 2*y - 84997594533927140476937696821249/100000000000000000000000000000000 > 0) & (a*y**2 + a - z**2 + 84997594533927140476937696821249/100000000000000000000000000000000 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Rational(5780585998344193, 5000000000000000), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-84997594533927140476937696821249, 100000000000000000000000000000000)), Integer(0)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(2))), Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(84997594533927140476937696821249, 100000000000000000000000000000000)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_85(a:sympy.Rational):
	#(a > -106587230981819929835562303178751/115611719966883860000000000000000) & (67009*a/16384 - z**2 + 84997594533927140476937696821249/100000000000000000000000000000000 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(-106587230981819929835562303178751, 115611719966883860000000000000000)), StrictLessThan(Add(Mul(Rational(67009, 16384), Symbol('a')), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(84997594533927140476937696821249, 100000000000000000000000000000000)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_86(a:sympy.Rational):
	#(a > -106587230981819929835562303178751/115611719966883860000000000000000) & (a < -84997594533927140476937696821249/408990478515625000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(-106587230981819929835562303178751, 115611719966883860000000000000000)), StrictLessThan(Symbol('a'), Rational(-84997594533927140476937696821249, 408990478515625000000000000000000)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_87(a:sympy.Rational):
	#(5780585998344193*a/5000000000000000 - y**3 + 2*y - 84997594533927140476937696821249/100000000000000000000000000000000 > 0) & (a*y**2 + a - z**2 + 84997594533927140476937696821249/100000000000000000000000000000000 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Rational(5780585998344193, 5000000000000000), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-84997594533927140476937696821249, 100000000000000000000000000000000)), Integer(0)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(2))), Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(84997594533927140476937696821249, 100000000000000000000000000000000)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_88(a:sympy.Rational):
	#(a > -106587230981819929835562303178751/115611719966883860000000000000000) & (67009*a/16384 - z**2 + 84997594533927140476937696821249/100000000000000000000000000000000 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(-106587230981819929835562303178751, 115611719966883860000000000000000)), StrictLessThan(Add(Mul(Rational(67009, 16384), Symbol('a')), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(84997594533927140476937696821249, 100000000000000000000000000000000)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_89(a:sympy.Rational):
	#(a > -106587230981819929835562303178751/115611719966883860000000000000000) & (a < -84997594533927140476937696821249/408990478515625000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(-106587230981819929835562303178751, 115611719966883860000000000000000)), StrictLessThan(Symbol('a'), Rational(-84997594533927140476937696821249, 408990478515625000000000000000000)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_90(a:sympy.Rational):
	#(5780585998344193*a/5000000000000000 - y**3 + 2*y - 84997594533927140476937696821249/100000000000000000000000000000000 > 0) & (a*y**2 + a - z**2 + 84997594533927140476937696821249/100000000000000000000000000000000 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Rational(5780585998344193, 5000000000000000), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-84997594533927140476937696821249, 100000000000000000000000000000000)), Integer(0)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(2))), Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(84997594533927140476937696821249, 100000000000000000000000000000000)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_91(a:sympy.Rational):
	#(a > -106587230981819929835562303178751/115611719966883860000000000000000) & (67009*a/16384 - z**2 + 84997594533927140476937696821249/100000000000000000000000000000000 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(-106587230981819929835562303178751, 115611719966883860000000000000000)), StrictLessThan(Add(Mul(Rational(67009, 16384), Symbol('a')), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(84997594533927140476937696821249, 100000000000000000000000000000000)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_92(a:sympy.Rational):
	#(a > -106587230981819929835562303178751/115611719966883860000000000000000) & (a < -84997594533927140476937696821249/408990478515625000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(-106587230981819929835562303178751, 115611719966883860000000000000000)), StrictLessThan(Symbol('a'), Rational(-84997594533927140476937696821249, 408990478515625000000000000000000)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_93(a:sympy.Rational):
	#(5780585998344193*a/5000000000000000 - y**3 + 2*y - 84997594533927140476937696821249/100000000000000000000000000000000 > 0) & (a*y**2 + a - z**2 + 84997594533927140476937696821249/100000000000000000000000000000000 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Rational(5780585998344193, 5000000000000000), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-84997594533927140476937696821249, 100000000000000000000000000000000)), Integer(0)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(2))), Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(84997594533927140476937696821249, 100000000000000000000000000000000)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_94(a:sympy.Rational):
	#(a > -106587230981819929835562303178751/115611719966883860000000000000000) & (67009*a/16384 - z**2 + 84997594533927140476937696821249/100000000000000000000000000000000 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(-106587230981819929835562303178751, 115611719966883860000000000000000)), StrictLessThan(Add(Mul(Rational(67009, 16384), Symbol('a')), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(84997594533927140476937696821249, 100000000000000000000000000000000)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_95(a:sympy.Rational):
	#(a > -106587230981819929835562303178751/115611719966883860000000000000000) & (a < -84997594533927140476937696821249/408990478515625000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(-106587230981819929835562303178751, 115611719966883860000000000000000)), StrictLessThan(Symbol('a'), Rational(-84997594533927140476937696821249, 408990478515625000000000000000000)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_96(a:sympy.Rational):
	#(5780585998344193*a/5000000000000000 - y**3 + 2*y - 84997594533927140476937696821249/100000000000000000000000000000000 > 0) & (a*y**2 + a - z**2 + 84997594533927140476937696821249/100000000000000000000000000000000 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Rational(5780585998344193, 5000000000000000), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-84997594533927140476937696821249, 100000000000000000000000000000000)), Integer(0)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(2))), Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(84997594533927140476937696821249, 100000000000000000000000000000000)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_97(a:sympy.Rational):
	#(a > -106587230981819929835562303178751/115611719966883860000000000000000) & (67009*a/16384 - z**2 + 84997594533927140476937696821249/100000000000000000000000000000000 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(-106587230981819929835562303178751, 115611719966883860000000000000000)), StrictLessThan(Add(Mul(Rational(67009, 16384), Symbol('a')), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(84997594533927140476937696821249, 100000000000000000000000000000000)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_98(a:sympy.Rational):
	#(a > -106587230981819929835562303178751/115611719966883860000000000000000) & (a < -84997594533927140476937696821249/408990478515625000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(-106587230981819929835562303178751, 115611719966883860000000000000000)), StrictLessThan(Symbol('a'), Rational(-84997594533927140476937696821249, 408990478515625000000000000000000)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_99(a:sympy.Rational):
	#(5780585998344193*a/5000000000000000 - y**3 + 2*y - 84997594533927140476937696821249/100000000000000000000000000000000 > 0) & (a*y**2 + a - z**2 + 84997594533927140476937696821249/100000000000000000000000000000000 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Rational(5780585998344193, 5000000000000000), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-84997594533927140476937696821249, 100000000000000000000000000000000)), Integer(0)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(2))), Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(84997594533927140476937696821249, 100000000000000000000000000000000)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_100(a:sympy.Rational):
	#(a > -106587230981819929835562303178751/115611719966883860000000000000000) & (67009*a/16384 - z**2 + 84997594533927140476937696821249/100000000000000000000000000000000 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(-106587230981819929835562303178751, 115611719966883860000000000000000)), StrictLessThan(Add(Mul(Rational(67009, 16384), Symbol('a')), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(84997594533927140476937696821249, 100000000000000000000000000000000)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_101(a:sympy.Rational):
	#(a > -106587230981819929835562303178751/115611719966883860000000000000000) & (a < -84997594533927140476937696821249/408990478515625000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(-106587230981819929835562303178751, 115611719966883860000000000000000)), StrictLessThan(Symbol('a'), Rational(-84997594533927140476937696821249, 408990478515625000000000000000000)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_102(a:sympy.Rational):
	#(5780585998344193*a/5000000000000000 - y**3 + 2*y - 84997594533927140476937696821249/100000000000000000000000000000000 > 0) & (a*y**2 + a - z**2 + 84997594533927140476937696821249/100000000000000000000000000000000 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Rational(5780585998344193, 5000000000000000), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-84997594533927140476937696821249, 100000000000000000000000000000000)), Integer(0)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(2))), Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(84997594533927140476937696821249, 100000000000000000000000000000000)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_103(a:sympy.Rational):
	#(a > -106587230981819929835562303178751/115611719966883860000000000000000) & (67009*a/16384 - z**2 + 84997594533927140476937696821249/100000000000000000000000000000000 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(-106587230981819929835562303178751, 115611719966883860000000000000000)), StrictLessThan(Add(Mul(Rational(67009, 16384), Symbol('a')), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(84997594533927140476937696821249, 100000000000000000000000000000000)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_104(a:sympy.Rational):
	#(a > -106587230981819929835562303178751/115611719966883860000000000000000) & (a < -84997594533927140476937696821249/408990478515625000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(-106587230981819929835562303178751, 115611719966883860000000000000000)), StrictLessThan(Symbol('a'), Rational(-84997594533927140476937696821249, 408990478515625000000000000000000)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_105(a:sympy.Rational):
	#(5780585998344193*a/5000000000000000 - y**3 + 2*y - 84997594533927140476937696821249/100000000000000000000000000000000 > 0) & (a*y**2 + a - z**2 + 84997594533927140476937696821249/100000000000000000000000000000000 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Rational(5780585998344193, 5000000000000000), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-84997594533927140476937696821249, 100000000000000000000000000000000)), Integer(0)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(2))), Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(84997594533927140476937696821249, 100000000000000000000000000000000)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_106(a:sympy.Rational):
	#(a > -106587230981819929835562303178751/115611719966883860000000000000000) & (67009*a/16384 - z**2 + 84997594533927140476937696821249/100000000000000000000000000000000 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(-106587230981819929835562303178751, 115611719966883860000000000000000)), StrictLessThan(Add(Mul(Rational(67009, 16384), Symbol('a')), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(84997594533927140476937696821249, 100000000000000000000000000000000)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_107(a:sympy.Rational):
	#(a > -106587230981819929835562303178751/115611719966883860000000000000000) & (a < -84997594533927140476937696821249/408990478515625000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(-106587230981819929835562303178751, 115611719966883860000000000000000)), StrictLessThan(Symbol('a'), Rational(-84997594533927140476937696821249, 408990478515625000000000000000000)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_108(a:sympy.Rational):
	#(5780585998344193*a/5000000000000000 - y**3 + 2*y - 84997594533927140476937696821249/100000000000000000000000000000000 > 0) & (a*y**2 + a - z**2 + 84997594533927140476937696821249/100000000000000000000000000000000 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Rational(5780585998344193, 5000000000000000), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-84997594533927140476937696821249, 100000000000000000000000000000000)), Integer(0)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(2))), Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(84997594533927140476937696821249, 100000000000000000000000000000000)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_109(a:sympy.Rational):
	#(a > -106587230981819929835562303178751/115611719966883860000000000000000) & (67009*a/16384 - z**2 + 84997594533927140476937696821249/100000000000000000000000000000000 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(-106587230981819929835562303178751, 115611719966883860000000000000000)), StrictLessThan(Add(Mul(Rational(67009, 16384), Symbol('a')), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(84997594533927140476937696821249, 100000000000000000000000000000000)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_110(a:sympy.Rational):
	#(a > -106587230981819929835562303178751/115611719966883860000000000000000) & (a < -84997594533927140476937696821249/408990478515625000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(-106587230981819929835562303178751, 115611719966883860000000000000000)), StrictLessThan(Symbol('a'), Rational(-84997594533927140476937696821249, 408990478515625000000000000000000)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_111(a:sympy.Rational):
	#(5780585998344193*a/5000000000000000 - y**3 + 2*y - 84997594533927140476937696821249/100000000000000000000000000000000 > 0) & (a*y**2 + a - z**2 + 84997594533927140476937696821249/100000000000000000000000000000000 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Rational(5780585998344193, 5000000000000000), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-84997594533927140476937696821249, 100000000000000000000000000000000)), Integer(0)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(2))), Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(84997594533927140476937696821249, 100000000000000000000000000000000)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_112(a:sympy.Rational):
	#(a > -106587230981819929835562303178751/115611719966883860000000000000000) & (67009*a/16384 - z**2 + 84997594533927140476937696821249/100000000000000000000000000000000 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(-106587230981819929835562303178751, 115611719966883860000000000000000)), StrictLessThan(Add(Mul(Rational(67009, 16384), Symbol('a')), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(84997594533927140476937696821249, 100000000000000000000000000000000)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_113(a:sympy.Rational):
	#(a > -106587230981819929835562303178751/115611719966883860000000000000000) & (a < -84997594533927140476937696821249/408990478515625000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(-106587230981819929835562303178751, 115611719966883860000000000000000)), StrictLessThan(Symbol('a'), Rational(-84997594533927140476937696821249, 408990478515625000000000000000000)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_114(a:sympy.Rational):
	#(5780585998344193*a/5000000000000000 - y**3 + 2*y - 84997594533927140476937696821249/100000000000000000000000000000000 > 0) & (a*y**2 + a - z**2 + 84997594533927140476937696821249/100000000000000000000000000000000 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Rational(5780585998344193, 5000000000000000), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-84997594533927140476937696821249, 100000000000000000000000000000000)), Integer(0)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(2))), Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(84997594533927140476937696821249, 100000000000000000000000000000000)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_115(a:sympy.Rational):
	#(a > -106587230981819929835562303178751/115611719966883860000000000000000) & (67009*a/16384 - z**2 + 84997594533927140476937696821249/100000000000000000000000000000000 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(-106587230981819929835562303178751, 115611719966883860000000000000000)), StrictLessThan(Add(Mul(Rational(67009, 16384), Symbol('a')), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(84997594533927140476937696821249, 100000000000000000000000000000000)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_116(a:sympy.Rational):
	#(a > -106587230981819929835562303178751/115611719966883860000000000000000) & (a < -84997594533927140476937696821249/408990478515625000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(-106587230981819929835562303178751, 115611719966883860000000000000000)), StrictLessThan(Symbol('a'), Rational(-84997594533927140476937696821249, 408990478515625000000000000000000)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_117(a:sympy.Rational):
	#(5780585998344193*a/5000000000000000 - y**3 + 2*y - 84997594533927140476937696821249/100000000000000000000000000000000 > 0) & (a*y**2 + a - z**2 + 84997594533927140476937696821249/100000000000000000000000000000000 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Rational(5780585998344193, 5000000000000000), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-84997594533927140476937696821249, 100000000000000000000000000000000)), Integer(0)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(2))), Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(84997594533927140476937696821249, 100000000000000000000000000000000)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_118(a:sympy.Rational):
	#(a > -106587230981819929835562303178751/115611719966883860000000000000000) & (67009*a/16384 - z**2 + 84997594533927140476937696821249/100000000000000000000000000000000 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(-106587230981819929835562303178751, 115611719966883860000000000000000)), StrictLessThan(Add(Mul(Rational(67009, 16384), Symbol('a')), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(84997594533927140476937696821249, 100000000000000000000000000000000)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_119(a:sympy.Rational):
	#(a > -106587230981819929835562303178751/115611719966883860000000000000000) & (a < -84997594533927140476937696821249/408990478515625000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(-106587230981819929835562303178751, 115611719966883860000000000000000)), StrictLessThan(Symbol('a'), Rational(-84997594533927140476937696821249, 408990478515625000000000000000000)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_120(a:sympy.Rational):
	#(5780585998344193*a/5000000000000000 - y**3 + 2*y - 84997594533927140476937696821249/100000000000000000000000000000000 > 0) & (a*y**2 + a - z**2 + 84997594533927140476937696821249/100000000000000000000000000000000 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Rational(5780585998344193, 5000000000000000), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-84997594533927140476937696821249, 100000000000000000000000000000000)), Integer(0)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(2))), Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(84997594533927140476937696821249, 100000000000000000000000000000000)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_121(a:sympy.Rational):
	#(a > -106587230981819929835562303178751/115611719966883860000000000000000) & (67009*a/16384 - z**2 + 84997594533927140476937696821249/100000000000000000000000000000000 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(-106587230981819929835562303178751, 115611719966883860000000000000000)), StrictLessThan(Add(Mul(Rational(67009, 16384), Symbol('a')), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(84997594533927140476937696821249, 100000000000000000000000000000000)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_122(a:sympy.Rational):
	#(a > -106587230981819929835562303178751/115611719966883860000000000000000) & (a < -84997594533927140476937696821249/408990478515625000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(-106587230981819929835562303178751, 115611719966883860000000000000000)), StrictLessThan(Symbol('a'), Rational(-84997594533927140476937696821249, 408990478515625000000000000000000)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_123(a:sympy.Rational):
	#(5780585998344193*a/5000000000000000 - y**3 + 2*y - 84997594533927140476937696821249/100000000000000000000000000000000 > 0) & (a*y**2 + a - z**2 + 84997594533927140476937696821249/100000000000000000000000000000000 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Rational(5780585998344193, 5000000000000000), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-84997594533927140476937696821249, 100000000000000000000000000000000)), Integer(0)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(2))), Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(84997594533927140476937696821249, 100000000000000000000000000000000)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_124(a:sympy.Rational):
	#(a > -106587230981819929835562303178751/115611719966883860000000000000000) & (67009*a/16384 - z**2 + 84997594533927140476937696821249/100000000000000000000000000000000 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(-106587230981819929835562303178751, 115611719966883860000000000000000)), StrictLessThan(Add(Mul(Rational(67009, 16384), Symbol('a')), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(84997594533927140476937696821249, 100000000000000000000000000000000)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_125(a:sympy.Rational):
	#(a > -106587230981819929835562303178751/115611719966883860000000000000000) & (a < -84997594533927140476937696821249/408990478515625000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(-106587230981819929835562303178751, 115611719966883860000000000000000)), StrictLessThan(Symbol('a'), Rational(-84997594533927140476937696821249, 408990478515625000000000000000000)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_126(a:sympy.Rational):
	#(5780585998344193*a/5000000000000000 - y**3 + 2*y - 84997594533927140476937696821249/100000000000000000000000000000000 > 0) & (a*y**2 + a - z**2 + 84997594533927140476937696821249/100000000000000000000000000000000 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Rational(5780585998344193, 5000000000000000), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-84997594533927140476937696821249, 100000000000000000000000000000000)), Integer(0)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(2))), Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(84997594533927140476937696821249, 100000000000000000000000000000000)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_127(a:sympy.Rational):
	#(a > -106587230981819929835562303178751/115611719966883860000000000000000) & (67009*a/16384 - z**2 + 84997594533927140476937696821249/100000000000000000000000000000000 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(-106587230981819929835562303178751, 115611719966883860000000000000000)), StrictLessThan(Add(Mul(Rational(67009, 16384), Symbol('a')), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(84997594533927140476937696821249, 100000000000000000000000000000000)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_128(a:sympy.Rational):
	#(a > -106587230981819929835562303178751/115611719966883860000000000000000) & (a < -84997594533927140476937696821249/408990478515625000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(-106587230981819929835562303178751, 115611719966883860000000000000000)), StrictLessThan(Symbol('a'), Rational(-84997594533927140476937696821249, 408990478515625000000000000000000)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_129(a:sympy.Rational):
	#(5780585998344193*a/5000000000000000 - y**3 + 2*y - 84997594533927140476937696821249/100000000000000000000000000000000 > 0) & (a*y**2 + a - z**2 + 84997594533927140476937696821249/100000000000000000000000000000000 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Rational(5780585998344193, 5000000000000000), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-84997594533927140476937696821249, 100000000000000000000000000000000)), Integer(0)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(2))), Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(84997594533927140476937696821249, 100000000000000000000000000000000)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_130(a:sympy.Rational):
	#(a > -106587230981819929835562303178751/115611719966883860000000000000000) & (67009*a/16384 - z**2 + 84997594533927140476937696821249/100000000000000000000000000000000 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(-106587230981819929835562303178751, 115611719966883860000000000000000)), StrictLessThan(Add(Mul(Rational(67009, 16384), Symbol('a')), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(84997594533927140476937696821249, 100000000000000000000000000000000)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_131(a:sympy.Rational):
	#(a > -106587230981819929835562303178751/115611719966883860000000000000000) & (a < -84997594533927140476937696821249/408990478515625000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(-106587230981819929835562303178751, 115611719966883860000000000000000)), StrictLessThan(Symbol('a'), Rational(-84997594533927140476937696821249, 408990478515625000000000000000000)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_132(a:sympy.Rational):
	#(5780585998344193*a/5000000000000000 - y**3 + 2*y - 84997594533927140476937696821249/100000000000000000000000000000000 > 0) & (a*y**2 + a - z**2 + 84997594533927140476937696821249/100000000000000000000000000000000 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Rational(5780585998344193, 5000000000000000), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-84997594533927140476937696821249, 100000000000000000000000000000000)), Integer(0)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(2))), Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(84997594533927140476937696821249, 100000000000000000000000000000000)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_133(a:sympy.Rational):
	#(a > -106587230981819929835562303178751/115611719966883860000000000000000) & (67009*a/16384 - z**2 + 84997594533927140476937696821249/100000000000000000000000000000000 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(-106587230981819929835562303178751, 115611719966883860000000000000000)), StrictLessThan(Add(Mul(Rational(67009, 16384), Symbol('a')), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(84997594533927140476937696821249, 100000000000000000000000000000000)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_134(a:sympy.Rational):
	#(a > -106587230981819929835562303178751/115611719966883860000000000000000) & (a < -84997594533927140476937696821249/408990478515625000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(-106587230981819929835562303178751, 115611719966883860000000000000000)), StrictLessThan(Symbol('a'), Rational(-84997594533927140476937696821249, 408990478515625000000000000000000)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_135(a:sympy.Rational):
	#(5780585998344193*a/5000000000000000 - y**3 + 2*y - 84997594533927140476937696821249/100000000000000000000000000000000 > 0) & (a*y**2 + a - z**2 + 84997594533927140476937696821249/100000000000000000000000000000000 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Rational(5780585998344193, 5000000000000000), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-84997594533927140476937696821249, 100000000000000000000000000000000)), Integer(0)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(2))), Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(84997594533927140476937696821249, 100000000000000000000000000000000)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_136(a:sympy.Rational):
	#(a > -106587230981819929835562303178751/115611719966883860000000000000000) & (67009*a/16384 - z**2 + 84997594533927140476937696821249/100000000000000000000000000000000 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(-106587230981819929835562303178751, 115611719966883860000000000000000)), StrictLessThan(Add(Mul(Rational(67009, 16384), Symbol('a')), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(84997594533927140476937696821249, 100000000000000000000000000000000)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_137(a:sympy.Rational):
	#(a > -106587230981819929835562303178751/115611719966883860000000000000000) & (a < -84997594533927140476937696821249/408990478515625000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(-106587230981819929835562303178751, 115611719966883860000000000000000)), StrictLessThan(Symbol('a'), Rational(-84997594533927140476937696821249, 408990478515625000000000000000000)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_138(a:sympy.Rational):
	#(5780585998344193*a/5000000000000000 - y**3 + 2*y - 84997594533927140476937696821249/100000000000000000000000000000000 > 0) & (a*y**2 + a - z**2 + 84997594533927140476937696821249/100000000000000000000000000000000 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Rational(5780585998344193, 5000000000000000), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-84997594533927140476937696821249, 100000000000000000000000000000000)), Integer(0)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(2))), Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(84997594533927140476937696821249, 100000000000000000000000000000000)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_139(a:sympy.Rational):
	#(a > -106587230981819929835562303178751/115611719966883860000000000000000) & (67009*a/16384 - z**2 + 84997594533927140476937696821249/100000000000000000000000000000000 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(-106587230981819929835562303178751, 115611719966883860000000000000000)), StrictLessThan(Add(Mul(Rational(67009, 16384), Symbol('a')), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(84997594533927140476937696821249, 100000000000000000000000000000000)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_140(a:sympy.Rational):
	#(a > -106587230981819929835562303178751/115611719966883860000000000000000) & (a < -84997594533927140476937696821249/408990478515625000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(-106587230981819929835562303178751, 115611719966883860000000000000000)), StrictLessThan(Symbol('a'), Rational(-84997594533927140476937696821249, 408990478515625000000000000000000)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_141(a:sympy.Rational):
	#(5780585998344193*a/5000000000000000 - y**3 + 2*y - 84997594533927140476937696821249/100000000000000000000000000000000 > 0) & (a*y**2 + a - z**2 + 84997594533927140476937696821249/100000000000000000000000000000000 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Rational(5780585998344193, 5000000000000000), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-84997594533927140476937696821249, 100000000000000000000000000000000)), Integer(0)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(2))), Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(84997594533927140476937696821249, 100000000000000000000000000000000)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_142(a:sympy.Rational):
	#(a > -106587230981819929835562303178751/115611719966883860000000000000000) & (67009*a/16384 - z**2 + 84997594533927140476937696821249/100000000000000000000000000000000 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(-106587230981819929835562303178751, 115611719966883860000000000000000)), StrictLessThan(Add(Mul(Rational(67009, 16384), Symbol('a')), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(84997594533927140476937696821249, 100000000000000000000000000000000)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_143(a:sympy.Rational):
	#(a > -106587230981819929835562303178751/115611719966883860000000000000000) & (a < -84997594533927140476937696821249/408990478515625000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(-106587230981819929835562303178751, 115611719966883860000000000000000)), StrictLessThan(Symbol('a'), Rational(-84997594533927140476937696821249, 408990478515625000000000000000000)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_144(a:sympy.Rational):
	#(5780585998344193*a/5000000000000000 - y**3 + 2*y - 84997594533927140476937696821249/100000000000000000000000000000000 > 0) & (a*y**2 + a - z**2 + 84997594533927140476937696821249/100000000000000000000000000000000 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Rational(5780585998344193, 5000000000000000), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-84997594533927140476937696821249, 100000000000000000000000000000000)), Integer(0)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(2))), Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(84997594533927140476937696821249, 100000000000000000000000000000000)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_145(a:sympy.Rational):
	#(a > -106587230981819929835562303178751/115611719966883860000000000000000) & (67009*a/16384 - z**2 + 84997594533927140476937696821249/100000000000000000000000000000000 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(-106587230981819929835562303178751, 115611719966883860000000000000000)), StrictLessThan(Add(Mul(Rational(67009, 16384), Symbol('a')), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(84997594533927140476937696821249, 100000000000000000000000000000000)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_146(a:sympy.Rational):
	#(a > -106587230981819929835562303178751/115611719966883860000000000000000) & (a < -84997594533927140476937696821249/408990478515625000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(-106587230981819929835562303178751, 115611719966883860000000000000000)), StrictLessThan(Symbol('a'), Rational(-84997594533927140476937696821249, 408990478515625000000000000000000)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_147(a:sympy.Rational):
	#(5780585998344193*a/5000000000000000 - y**3 + 2*y - 84997594533927140476937696821249/100000000000000000000000000000000 > 0) & (a*y**2 + a - z**2 + 84997594533927140476937696821249/100000000000000000000000000000000 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Rational(5780585998344193, 5000000000000000), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-84997594533927140476937696821249, 100000000000000000000000000000000)), Integer(0)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(2))), Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(84997594533927140476937696821249, 100000000000000000000000000000000)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_148(a:sympy.Rational):
	#(a > -106587230981819929835562303178751/115611719966883860000000000000000) & (67009*a/16384 - z**2 + 84997594533927140476937696821249/100000000000000000000000000000000 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(-106587230981819929835562303178751, 115611719966883860000000000000000)), StrictLessThan(Add(Mul(Rational(67009, 16384), Symbol('a')), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(84997594533927140476937696821249, 100000000000000000000000000000000)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_149(a:sympy.Rational):
	#(a > -106587230981819929835562303178751/115611719966883860000000000000000) & (a < -84997594533927140476937696821249/408990478515625000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(-106587230981819929835562303178751, 115611719966883860000000000000000)), StrictLessThan(Symbol('a'), Rational(-84997594533927140476937696821249, 408990478515625000000000000000000)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_150(a:sympy.Rational):
	#(5780585998344193*a/5000000000000000 - y**3 + 2*y - 84997594533927140476937696821249/100000000000000000000000000000000 > 0) & (a*y**2 + a - z**2 + 84997594533927140476937696821249/100000000000000000000000000000000 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Rational(5780585998344193, 5000000000000000), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-84997594533927140476937696821249, 100000000000000000000000000000000)), Integer(0)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(2))), Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(84997594533927140476937696821249, 100000000000000000000000000000000)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_151(a:sympy.Rational):
	#(a > -106587230981819929835562303178751/115611719966883860000000000000000) & (67009*a/16384 - z**2 + 84997594533927140476937696821249/100000000000000000000000000000000 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(-106587230981819929835562303178751, 115611719966883860000000000000000)), StrictLessThan(Add(Mul(Rational(67009, 16384), Symbol('a')), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(84997594533927140476937696821249, 100000000000000000000000000000000)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_152(a:sympy.Rational):
	#(a > -106587230981819929835562303178751/115611719966883860000000000000000) & (a < -84997594533927140476937696821249/408990478515625000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(-106587230981819929835562303178751, 115611719966883860000000000000000)), StrictLessThan(Symbol('a'), Rational(-84997594533927140476937696821249, 408990478515625000000000000000000)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_153(a:sympy.Rational):
	#(5780585998344193*a/5000000000000000 - y**3 + 2*y - 84997594533927140476937696821249/100000000000000000000000000000000 > 0) & (a*y**2 + a - z**2 + 84997594533927140476937696821249/100000000000000000000000000000000 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Rational(5780585998344193, 5000000000000000), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-84997594533927140476937696821249, 100000000000000000000000000000000)), Integer(0)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(2))), Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(84997594533927140476937696821249, 100000000000000000000000000000000)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_154(a:sympy.Rational):
	#(a > -106587230981819929835562303178751/115611719966883860000000000000000) & (67009*a/16384 - z**2 + 84997594533927140476937696821249/100000000000000000000000000000000 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(-106587230981819929835562303178751, 115611719966883860000000000000000)), StrictLessThan(Add(Mul(Rational(67009, 16384), Symbol('a')), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(84997594533927140476937696821249, 100000000000000000000000000000000)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_155(a:sympy.Rational):
	#(a > -106587230981819929835562303178751/115611719966883860000000000000000) & (a < -84997594533927140476937696821249/408990478515625000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(-106587230981819929835562303178751, 115611719966883860000000000000000)), StrictLessThan(Symbol('a'), Rational(-84997594533927140476937696821249, 408990478515625000000000000000000)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_156(a:sympy.Rational):
	#(5780585998344193*a/5000000000000000 - y**3 + 2*y - 84997594533927140476937696821249/100000000000000000000000000000000 > 0) & (a*y**2 + a - z**2 + 84997594533927140476937696821249/100000000000000000000000000000000 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Rational(5780585998344193, 5000000000000000), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-84997594533927140476937696821249, 100000000000000000000000000000000)), Integer(0)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(2))), Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(84997594533927140476937696821249, 100000000000000000000000000000000)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_157(a:sympy.Rational):
	#(a > -106587230981819929835562303178751/115611719966883860000000000000000) & (67009*a/16384 - z**2 + 84997594533927140476937696821249/100000000000000000000000000000000 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(-106587230981819929835562303178751, 115611719966883860000000000000000)), StrictLessThan(Add(Mul(Rational(67009, 16384), Symbol('a')), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(84997594533927140476937696821249, 100000000000000000000000000000000)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_158(a:sympy.Rational):
	#(a > -106587230981819929835562303178751/115611719966883860000000000000000) & (a < -84997594533927140476937696821249/408990478515625000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(-106587230981819929835562303178751, 115611719966883860000000000000000)), StrictLessThan(Symbol('a'), Rational(-84997594533927140476937696821249, 408990478515625000000000000000000)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_159(a:sympy.Rational):
	#(5780585998344193*a/5000000000000000 - y**3 + 2*y - 84997594533927140476937696821249/100000000000000000000000000000000 > 0) & (a*y**2 + a - z**2 + 84997594533927140476937696821249/100000000000000000000000000000000 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Rational(5780585998344193, 5000000000000000), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-84997594533927140476937696821249, 100000000000000000000000000000000)), Integer(0)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(2))), Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(84997594533927140476937696821249, 100000000000000000000000000000000)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_160(a:sympy.Rational):
	#(a > -106587230981819929835562303178751/115611719966883860000000000000000) & (67009*a/16384 - z**2 + 84997594533927140476937696821249/100000000000000000000000000000000 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(-106587230981819929835562303178751, 115611719966883860000000000000000)), StrictLessThan(Add(Mul(Rational(67009, 16384), Symbol('a')), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(84997594533927140476937696821249, 100000000000000000000000000000000)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_161(a:sympy.Rational):
	#(a > -106587230981819929835562303178751/115611719966883860000000000000000) & (a < -84997594533927140476937696821249/408990478515625000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(-106587230981819929835562303178751, 115611719966883860000000000000000)), StrictLessThan(Symbol('a'), Rational(-84997594533927140476937696821249, 408990478515625000000000000000000)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_162(a:sympy.Rational):
	#(5780585998344193*a/5000000000000000 - y**3 + 2*y - 84997594533927140476937696821249/100000000000000000000000000000000 > 0) & (a*y**2 + a - z**2 + 84997594533927140476937696821249/100000000000000000000000000000000 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Rational(5780585998344193, 5000000000000000), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-84997594533927140476937696821249, 100000000000000000000000000000000)), Integer(0)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(2))), Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(84997594533927140476937696821249, 100000000000000000000000000000000)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_163(a:sympy.Rational):
	#(a > -106587230981819929835562303178751/115611719966883860000000000000000) & (67009*a/16384 - z**2 + 84997594533927140476937696821249/100000000000000000000000000000000 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(-106587230981819929835562303178751, 115611719966883860000000000000000)), StrictLessThan(Add(Mul(Rational(67009, 16384), Symbol('a')), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(84997594533927140476937696821249, 100000000000000000000000000000000)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_164(a:sympy.Rational):
	#(a > -106587230981819929835562303178751/115611719966883860000000000000000) & (a < -84997594533927140476937696821249/408990478515625000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(-106587230981819929835562303178751, 115611719966883860000000000000000)), StrictLessThan(Symbol('a'), Rational(-84997594533927140476937696821249, 408990478515625000000000000000000)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_165(a:sympy.Rational):
	#(5780585998344193*a/5000000000000000 - y**3 + 2*y - 84997594533927140476937696821249/100000000000000000000000000000000 > 0) & (a*y**2 + a - z**2 + 84997594533927140476937696821249/100000000000000000000000000000000 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Rational(5780585998344193, 5000000000000000), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-84997594533927140476937696821249, 100000000000000000000000000000000)), Integer(0)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(2))), Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(84997594533927140476937696821249, 100000000000000000000000000000000)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_166(a:sympy.Rational):
	#(a > -106587230981819929835562303178751/115611719966883860000000000000000) & (67009*a/16384 - z**2 + 84997594533927140476937696821249/100000000000000000000000000000000 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(-106587230981819929835562303178751, 115611719966883860000000000000000)), StrictLessThan(Add(Mul(Rational(67009, 16384), Symbol('a')), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(84997594533927140476937696821249, 100000000000000000000000000000000)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_167(a:sympy.Rational):
	#(a > -106587230981819929835562303178751/115611719966883860000000000000000) & (a < -84997594533927140476937696821249/408990478515625000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(-106587230981819929835562303178751, 115611719966883860000000000000000)), StrictLessThan(Symbol('a'), Rational(-84997594533927140476937696821249, 408990478515625000000000000000000)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_168(a:sympy.Rational):
	#(5780585998344193*a/5000000000000000 - y**3 + 2*y - 84997594533927140476937696821249/100000000000000000000000000000000 > 0) & (a*y**2 + a - z**2 + 84997594533927140476937696821249/100000000000000000000000000000000 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Rational(5780585998344193, 5000000000000000), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-84997594533927140476937696821249, 100000000000000000000000000000000)), Integer(0)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(2))), Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(84997594533927140476937696821249, 100000000000000000000000000000000)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_169(a:sympy.Rational):
	#(a > -106587230981819929835562303178751/115611719966883860000000000000000) & (67009*a/16384 - z**2 + 84997594533927140476937696821249/100000000000000000000000000000000 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(-106587230981819929835562303178751, 115611719966883860000000000000000)), StrictLessThan(Add(Mul(Rational(67009, 16384), Symbol('a')), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(84997594533927140476937696821249, 100000000000000000000000000000000)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_170(a:sympy.Rational):
	#(a > -106587230981819929835562303178751/115611719966883860000000000000000) & (a < -84997594533927140476937696821249/408990478515625000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(-106587230981819929835562303178751, 115611719966883860000000000000000)), StrictLessThan(Symbol('a'), Rational(-84997594533927140476937696821249, 408990478515625000000000000000000)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_171(a:sympy.Rational):
	#(5780585998344193*a/5000000000000000 - y**3 + 2*y - 84997594533927140476937696821249/100000000000000000000000000000000 > 0) & (a*y**2 + a - z**2 + 84997594533927140476937696821249/100000000000000000000000000000000 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Rational(5780585998344193, 5000000000000000), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-84997594533927140476937696821249, 100000000000000000000000000000000)), Integer(0)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(2))), Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(84997594533927140476937696821249, 100000000000000000000000000000000)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_172(a:sympy.Rational):
	#(a > -106587230981819929835562303178751/115611719966883860000000000000000) & (67009*a/16384 - z**2 + 84997594533927140476937696821249/100000000000000000000000000000000 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(-106587230981819929835562303178751, 115611719966883860000000000000000)), StrictLessThan(Add(Mul(Rational(67009, 16384), Symbol('a')), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(84997594533927140476937696821249, 100000000000000000000000000000000)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_173(a:sympy.Rational):
	#(a > -106587230981819929835562303178751/115611719966883860000000000000000) & (a < -84997594533927140476937696821249/408990478515625000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(-106587230981819929835562303178751, 115611719966883860000000000000000)), StrictLessThan(Symbol('a'), Rational(-84997594533927140476937696821249, 408990478515625000000000000000000)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_174(a:sympy.Rational):
	#(5780585998344193*a/5000000000000000 - y**3 + 2*y - 84997594533927140476937696821249/100000000000000000000000000000000 > 0) & (a*y**2 + a - z**2 + 84997594533927140476937696821249/100000000000000000000000000000000 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Rational(5780585998344193, 5000000000000000), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-84997594533927140476937696821249, 100000000000000000000000000000000)), Integer(0)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(2))), Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(84997594533927140476937696821249, 100000000000000000000000000000000)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_175(a:sympy.Rational):
	#(a > -106587230981819929835562303178751/115611719966883860000000000000000) & (67009*a/16384 - z**2 + 84997594533927140476937696821249/100000000000000000000000000000000 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(-106587230981819929835562303178751, 115611719966883860000000000000000)), StrictLessThan(Add(Mul(Rational(67009, 16384), Symbol('a')), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(84997594533927140476937696821249, 100000000000000000000000000000000)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_176(a:sympy.Rational):
	#(a > -106587230981819929835562303178751/115611719966883860000000000000000) & (a < -84997594533927140476937696821249/408990478515625000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(-106587230981819929835562303178751, 115611719966883860000000000000000)), StrictLessThan(Symbol('a'), Rational(-84997594533927140476937696821249, 408990478515625000000000000000000)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_177(a:sympy.Rational):
	#(5780585998344193*a/5000000000000000 - y**3 + 2*y - 84997594533927140476937696821249/100000000000000000000000000000000 > 0) & (a*y**2 + a - z**2 + 84997594533927140476937696821249/100000000000000000000000000000000 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Rational(5780585998344193, 5000000000000000), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-84997594533927140476937696821249, 100000000000000000000000000000000)), Integer(0)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(2))), Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(84997594533927140476937696821249, 100000000000000000000000000000000)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_178(a:sympy.Rational):
	#(a > -106587230981819929835562303178751/115611719966883860000000000000000) & (67009*a/16384 - z**2 + 84997594533927140476937696821249/100000000000000000000000000000000 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(-106587230981819929835562303178751, 115611719966883860000000000000000)), StrictLessThan(Add(Mul(Rational(67009, 16384), Symbol('a')), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(84997594533927140476937696821249, 100000000000000000000000000000000)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_179(a:sympy.Rational):
	#(a > -106587230981819929835562303178751/115611719966883860000000000000000) & (a < -84997594533927140476937696821249/408990478515625000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(-106587230981819929835562303178751, 115611719966883860000000000000000)), StrictLessThan(Symbol('a'), Rational(-84997594533927140476937696821249, 408990478515625000000000000000000)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_180(a:sympy.Rational):
	#(5780585998344193*a/5000000000000000 - y**3 + 2*y - 84997594533927140476937696821249/100000000000000000000000000000000 > 0) & (a*y**2 + a - z**2 + 84997594533927140476937696821249/100000000000000000000000000000000 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Rational(5780585998344193, 5000000000000000), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-84997594533927140476937696821249, 100000000000000000000000000000000)), Integer(0)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(2))), Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(84997594533927140476937696821249, 100000000000000000000000000000000)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_181(a:sympy.Rational):
	#(a > -106587230981819929835562303178751/115611719966883860000000000000000) & (67009*a/16384 - z**2 + 84997594533927140476937696821249/100000000000000000000000000000000 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(-106587230981819929835562303178751, 115611719966883860000000000000000)), StrictLessThan(Add(Mul(Rational(67009, 16384), Symbol('a')), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(84997594533927140476937696821249, 100000000000000000000000000000000)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_182(a:sympy.Rational):
	#(a > -106587230981819929835562303178751/115611719966883860000000000000000) & (a < -84997594533927140476937696821249/408990478515625000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(-106587230981819929835562303178751, 115611719966883860000000000000000)), StrictLessThan(Symbol('a'), Rational(-84997594533927140476937696821249, 408990478515625000000000000000000)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_183(a:sympy.Rational):
	#(5780585998344193*a/5000000000000000 - y**3 + 2*y - 84997594533927140476937696821249/100000000000000000000000000000000 > 0) & (a*y**2 + a - z**2 + 84997594533927140476937696821249/100000000000000000000000000000000 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Rational(5780585998344193, 5000000000000000), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-84997594533927140476937696821249, 100000000000000000000000000000000)), Integer(0)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(2))), Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(84997594533927140476937696821249, 100000000000000000000000000000000)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_184(a:sympy.Rational):
	#(a > -106587230981819929835562303178751/115611719966883860000000000000000) & (67009*a/16384 - z**2 + 84997594533927140476937696821249/100000000000000000000000000000000 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(-106587230981819929835562303178751, 115611719966883860000000000000000)), StrictLessThan(Add(Mul(Rational(67009, 16384), Symbol('a')), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(84997594533927140476937696821249, 100000000000000000000000000000000)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_185(a:sympy.Rational):
	#(a > -106587230981819929835562303178751/115611719966883860000000000000000) & (a < -84997594533927140476937696821249/408990478515625000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(-106587230981819929835562303178751, 115611719966883860000000000000000)), StrictLessThan(Symbol('a'), Rational(-84997594533927140476937696821249, 408990478515625000000000000000000)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_186(a:sympy.Rational):
	#(5780585998344193*a/5000000000000000 - y**3 + 2*y - 84997594533927140476937696821249/100000000000000000000000000000000 > 0) & (a*y**2 + a - z**2 + 84997594533927140476937696821249/100000000000000000000000000000000 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Rational(5780585998344193, 5000000000000000), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-84997594533927140476937696821249, 100000000000000000000000000000000)), Integer(0)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(2))), Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(84997594533927140476937696821249, 100000000000000000000000000000000)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_187(a:sympy.Rational):
	#(a > -106587230981819929835562303178751/115611719966883860000000000000000) & (67009*a/16384 - z**2 + 84997594533927140476937696821249/100000000000000000000000000000000 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(-106587230981819929835562303178751, 115611719966883860000000000000000)), StrictLessThan(Add(Mul(Rational(67009, 16384), Symbol('a')), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(84997594533927140476937696821249, 100000000000000000000000000000000)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_188(a:sympy.Rational):
	#(a > -106587230981819929835562303178751/115611719966883860000000000000000) & (a < -84997594533927140476937696821249/408990478515625000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(-106587230981819929835562303178751, 115611719966883860000000000000000)), StrictLessThan(Symbol('a'), Rational(-84997594533927140476937696821249, 408990478515625000000000000000000)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_189(a:sympy.Rational):
	#(5780585998344193*a/5000000000000000 - y**3 + 2*y - 84997594533927140476937696821249/100000000000000000000000000000000 > 0) & (a*y**2 + a - z**2 + 84997594533927140476937696821249/100000000000000000000000000000000 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Rational(5780585998344193, 5000000000000000), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-84997594533927140476937696821249, 100000000000000000000000000000000)), Integer(0)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(2))), Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(84997594533927140476937696821249, 100000000000000000000000000000000)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_190(a:sympy.Rational):
	#(a > -106587230981819929835562303178751/115611719966883860000000000000000) & (67009*a/16384 - z**2 + 84997594533927140476937696821249/100000000000000000000000000000000 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(-106587230981819929835562303178751, 115611719966883860000000000000000)), StrictLessThan(Add(Mul(Rational(67009, 16384), Symbol('a')), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(84997594533927140476937696821249, 100000000000000000000000000000000)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_191(a:sympy.Rational):
	#(a > -106587230981819929835562303178751/115611719966883860000000000000000) & (a < -84997594533927140476937696821249/408990478515625000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(-106587230981819929835562303178751, 115611719966883860000000000000000)), StrictLessThan(Symbol('a'), Rational(-84997594533927140476937696821249, 408990478515625000000000000000000)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_192(a:sympy.Rational):
	#(5780585998344193*a/5000000000000000 - y**3 + 2*y - 84997594533927140476937696821249/100000000000000000000000000000000 > 0) & (a*y**2 + a - z**2 + 84997594533927140476937696821249/100000000000000000000000000000000 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Rational(5780585998344193, 5000000000000000), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-84997594533927140476937696821249, 100000000000000000000000000000000)), Integer(0)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(2))), Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(84997594533927140476937696821249, 100000000000000000000000000000000)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_193(a:sympy.Rational):
	#(a > -106587230981819929835562303178751/115611719966883860000000000000000) & (67009*a/16384 - z**2 + 84997594533927140476937696821249/100000000000000000000000000000000 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(-106587230981819929835562303178751, 115611719966883860000000000000000)), StrictLessThan(Add(Mul(Rational(67009, 16384), Symbol('a')), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(84997594533927140476937696821249, 100000000000000000000000000000000)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_194(a:sympy.Rational):
	#(a > -106587230981819929835562303178751/115611719966883860000000000000000) & (a < -84997594533927140476937696821249/408990478515625000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(-106587230981819929835562303178751, 115611719966883860000000000000000)), StrictLessThan(Symbol('a'), Rational(-84997594533927140476937696821249, 408990478515625000000000000000000)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_195(a:sympy.Rational):
	#(5780585998344193*a/5000000000000000 - y**3 + 2*y - 84997594533927140476937696821249/100000000000000000000000000000000 > 0) & (a*y**2 + a - z**2 + 84997594533927140476937696821249/100000000000000000000000000000000 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Rational(5780585998344193, 5000000000000000), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-84997594533927140476937696821249, 100000000000000000000000000000000)), Integer(0)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(2))), Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(84997594533927140476937696821249, 100000000000000000000000000000000)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_196(a:sympy.Rational):
	#(a > -106587230981819929835562303178751/115611719966883860000000000000000) & (67009*a/16384 - z**2 + 84997594533927140476937696821249/100000000000000000000000000000000 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(-106587230981819929835562303178751, 115611719966883860000000000000000)), StrictLessThan(Add(Mul(Rational(67009, 16384), Symbol('a')), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(84997594533927140476937696821249, 100000000000000000000000000000000)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_197(a:sympy.Rational):
	#(a > -106587230981819929835562303178751/115611719966883860000000000000000) & (a < -84997594533927140476937696821249/408990478515625000000000000000000)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(-106587230981819929835562303178751, 115611719966883860000000000000000)), StrictLessThan(Symbol('a'), Rational(-84997594533927140476937696821249, 408990478515625000000000000000000)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_198(a:sympy.Rational):
	#(5780585998344193*a/5000000000000000 - y**3 + 2*y - 84997594533927140476937696821249/100000000000000000000000000000000 > 0) & (a*y**2 + a - z**2 + 84997594533927140476937696821249/100000000000000000000000000000000 < 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Rational(5780585998344193, 5000000000000000), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-84997594533927140476937696821249, 100000000000000000000000000000000)), Integer(0)), StrictLessThan(Add(Mul(Symbol('a'), Pow(Symbol('y'), Integer(2))), Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(84997594533927140476937696821249, 100000000000000000000000000000000)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_199(a:sympy.Rational):
	#(a > -106587230981819929835562303178751/115611719966883860000000000000000) & (67009*a/16384 - z**2 + 84997594533927140476937696821249/100000000000000000000000000000000 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(-106587230981819929835562303178751, 115611719966883860000000000000000)), StrictLessThan(Add(Mul(Rational(67009, 16384), Symbol('a')), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(84997594533927140476937696821249, 100000000000000000000000000000000)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_200(a:sympy.Rational):