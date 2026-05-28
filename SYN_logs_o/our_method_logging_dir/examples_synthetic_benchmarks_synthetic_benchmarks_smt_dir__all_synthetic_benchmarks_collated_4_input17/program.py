import sympy
from sympy import *
from NQS.helper_program_cav import get_lambda_val

def pre_condition_0(a:sympy.Rational,b:sympy.Rational):
	#(a < 0) & (27*a**2 - 196 < 0) & (27*a**2 - 16 < 0) & (27*b**2 - 4 < 0) & Eq(-a**3 + 3*a**2*b - 3*a*b**2 + 4*a + b**3 + 4*b, 0) & (-a**3 + 3*a**2*b - 3*a*b**2 + 4*a + b**3 + 4*b > 0)

	pre_cond = And(StrictLessThan(Symbol('a'), Integer(0)), StrictLessThan(Add(Mul(Integer(27), Pow(Symbol('a'), Integer(2))), Integer(-196)), Integer(0)), StrictLessThan(Add(Mul(Integer(27), Pow(Symbol('a'), Integer(2))), Integer(-16)), Integer(0)), StrictLessThan(Add(Mul(Integer(27), Pow(Symbol('b'), Integer(2))), Integer(-4)), Integer(0)), Equality(Add(Mul(Integer(-1), Pow(Symbol('a'), Integer(3))), Mul(Integer(3), Pow(Symbol('a'), Integer(2)), Symbol('b')), Mul(Integer(-1), Integer(3), Symbol('a'), Pow(Symbol('b'), Integer(2))), Mul(Integer(4), Symbol('a')), Pow(Symbol('b'), Integer(3)), Mul(Integer(4), Symbol('b'))), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('a'), Integer(3))), Mul(Integer(3), Pow(Symbol('a'), Integer(2)), Symbol('b')), Mul(Integer(-1), Integer(3), Symbol('a'), Pow(Symbol('b'), Integer(2))), Mul(Integer(4), Symbol('a')), Pow(Symbol('b'), Integer(3)), Mul(Integer(4), Symbol('b'))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1(a:sympy.Rational,b:sympy.Rational):
	#-a + b > 0

	pre_cond = StrictGreaterThan(Add(Mul(Integer(-1), Symbol('a')), Symbol('b')), Integer(0))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_2(a:sympy.Rational,b:sympy.Rational):
	#(3538944*a + 4681873 < 0) & (905969664*a**2 + 2397118976*a - 6721085833 < 0) & (905969664*a**2 + 2397118976*a + 1063144071 < 0) & (905969664*b**2 + 3321963008*b + 2815933063 < 0) & Eq(-64*a**3 + 192*a**2*b + 98*a**2 - 192*a*b**2 - 196*a*b + 256*a + 64*b**3 + 98*b**2 + 256*b + 791, 0) & (-64*a**3 + 192*a**2*b + 98*a**2 - 192*a*b**2 - 196*a*b + 256*a + 64*b**3 + 98*b**2 + 256*b + 791 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(3538944), Symbol('a')), Integer(4681873)), Integer(0)), StrictLessThan(Add(Mul(Integer(905969664), Pow(Symbol('a'), Integer(2))), Mul(Integer(2397118976), Symbol('a')), Integer(-6721085833)), Integer(0)), StrictLessThan(Add(Mul(Integer(905969664), Pow(Symbol('a'), Integer(2))), Mul(Integer(2397118976), Symbol('a')), Integer(1063144071)), Integer(0)), StrictLessThan(Add(Mul(Integer(905969664), Pow(Symbol('b'), Integer(2))), Mul(Integer(3321963008), Symbol('b')), Integer(2815933063)), Integer(0)), Equality(Add(Mul(Integer(-1), Integer(64), Pow(Symbol('a'), Integer(3))), Mul(Integer(192), Pow(Symbol('a'), Integer(2)), Symbol('b')), Mul(Integer(98), Pow(Symbol('a'), Integer(2))), Mul(Integer(-1), Integer(192), Symbol('a'), Pow(Symbol('b'), Integer(2))), Mul(Integer(-1), Integer(196), Symbol('a'), Symbol('b')), Mul(Integer(256), Symbol('a')), Mul(Integer(64), Pow(Symbol('b'), Integer(3))), Mul(Integer(98), Pow(Symbol('b'), Integer(2))), Mul(Integer(256), Symbol('b')), Integer(791)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Integer(64), Pow(Symbol('a'), Integer(3))), Mul(Integer(192), Pow(Symbol('a'), Integer(2)), Symbol('b')), Mul(Integer(98), Pow(Symbol('a'), Integer(2))), Mul(Integer(-1), Integer(192), Symbol('a'), Pow(Symbol('b'), Integer(2))), Mul(Integer(-1), Integer(196), Symbol('a'), Symbol('b')), Mul(Integer(256), Symbol('a')), Mul(Integer(64), Pow(Symbol('b'), Integer(3))), Mul(Integer(98), Pow(Symbol('b'), Integer(2))), Mul(Integer(256), Symbol('b')), Integer(791)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_3(a:sympy.Rational,b:sympy.Rational):
	#-a + b + 2 > 0

	pre_cond = StrictGreaterThan(Add(Mul(Integer(-1), Symbol('a')), Symbol('b'), Integer(2)), Integer(0))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_4(a:sympy.Rational,b:sympy.Rational):
	#(3538944*a + 22648249 < 0) & (-96*a + 96*b + 169 > 0) & (905969664*a**2 + 11595903488*a + 36793541741 <= 0) & (905969664*a**2 + 11595903488*a + 37058339949 > 0) & (905969664*b**2 + 14785671680*b + 55395824749 < 0) & (48*a**2 - 96*a*b - 169*a + 48*b**2 + 169*b + 64 < 0) & (-64*a**3 + 192*a**2*b + 338*a**2 - 192*a*b**2 - 676*a*b + 256*a + 64*b**3 + 338*b**2 + 256*b + 3029 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(3538944), Symbol('a')), Integer(22648249)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Integer(96), Symbol('a')), Mul(Integer(96), Symbol('b')), Integer(169)), Integer(0)), LessThan(Add(Mul(Integer(905969664), Pow(Symbol('a'), Integer(2))), Mul(Integer(11595903488), Symbol('a')), Integer(36793541741)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(905969664), Pow(Symbol('a'), Integer(2))), Mul(Integer(11595903488), Symbol('a')), Integer(37058339949)), Integer(0)), StrictLessThan(Add(Mul(Integer(905969664), Pow(Symbol('b'), Integer(2))), Mul(Integer(14785671680), Symbol('b')), Integer(55395824749)), Integer(0)), StrictLessThan(Add(Mul(Integer(48), Pow(Symbol('a'), Integer(2))), Mul(Integer(-1), Integer(96), Symbol('a'), Symbol('b')), Mul(Integer(-1), Integer(169), Symbol('a')), Mul(Integer(48), Pow(Symbol('b'), Integer(2))), Mul(Integer(169), Symbol('b')), Integer(64)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Integer(64), Pow(Symbol('a'), Integer(3))), Mul(Integer(192), Pow(Symbol('a'), Integer(2)), Symbol('b')), Mul(Integer(338), Pow(Symbol('a'), Integer(2))), Mul(Integer(-1), Integer(192), Symbol('a'), Pow(Symbol('b'), Integer(2))), Mul(Integer(-1), Integer(676), Symbol('a'), Symbol('b')), Mul(Integer(256), Symbol('a')), Mul(Integer(64), Pow(Symbol('b'), Integer(3))), Mul(Integer(338), Pow(Symbol('b'), Integer(2))), Mul(Integer(256), Symbol('b')), Integer(3029)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_5(a:sympy.Rational,b:sympy.Rational):
	#-a + b + 6 > 0

	pre_cond = StrictGreaterThan(Add(Mul(Integer(-1), Symbol('a')), Symbol('b'), Integer(6)), Integer(0))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_6(a:sympy.Rational,b:sympy.Rational):
	#(536870912*a + 9704843307 < 0) & (-512*a + 512*b + 1587 > 0) & (237494511599616*a**2 + 8586224248061952*a + 69196707499760549 <= 0) & (237494511599616*a**2 + 8586224248061952*a + 69781368009546661 > 0) & (237494511599616*b**2 + 10058504677392384*b + 87060995053607845 < 0) & (768*a**2 - 1536*a*b - 4761*a + 768*b**2 + 4761*b + 1024 < 0) & (-4096*a**3 + 12288*a**2*b + 38088*a**2 - 12288*a*b**2 - 76176*a*b + 16384*a + 4096*b**3 + 38088*b**2 + 16384*b + 399165 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(536870912), Symbol('a')), Integer(9704843307)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Integer(512), Symbol('a')), Mul(Integer(512), Symbol('b')), Integer(1587)), Integer(0)), LessThan(Add(Mul(Integer(237494511599616), Pow(Symbol('a'), Integer(2))), Mul(Integer(8586224248061952), Symbol('a')), Integer(69196707499760549)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(237494511599616), Pow(Symbol('a'), Integer(2))), Mul(Integer(8586224248061952), Symbol('a')), Integer(69781368009546661)), Integer(0)), StrictLessThan(Add(Mul(Integer(237494511599616), Pow(Symbol('b'), Integer(2))), Mul(Integer(10058504677392384), Symbol('b')), Integer(87060995053607845)), Integer(0)), StrictLessThan(Add(Mul(Integer(768), Pow(Symbol('a'), Integer(2))), Mul(Integer(-1), Integer(1536), Symbol('a'), Symbol('b')), Mul(Integer(-1), Integer(4761), Symbol('a')), Mul(Integer(768), Pow(Symbol('b'), Integer(2))), Mul(Integer(4761), Symbol('b')), Integer(1024)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Integer(4096), Pow(Symbol('a'), Integer(3))), Mul(Integer(12288), Pow(Symbol('a'), Integer(2)), Symbol('b')), Mul(Integer(38088), Pow(Symbol('a'), Integer(2))), Mul(Integer(-1), Integer(12288), Symbol('a'), Pow(Symbol('b'), Integer(2))), Mul(Integer(-1), Integer(76176), Symbol('a'), Symbol('b')), Mul(Integer(16384), Symbol('a')), Mul(Integer(4096), Pow(Symbol('b'), Integer(3))), Mul(Integer(38088), Pow(Symbol('b'), Integer(2))), Mul(Integer(16384), Symbol('b')), Integer(399165)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_7(a:sympy.Rational,b:sympy.Rational):
	#-a + b + 10 > 0

	pre_cond = StrictGreaterThan(Add(Mul(Integer(-1), Symbol('a')), Symbol('b'), Integer(10)), Integer(0))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_8(a:sympy.Rational,b:sympy.Rational):
	#(14495514624*a + 584972005753 < 0) & (-1536*a + 1536*b + 6889 > 0) & (237494511599616*a**2 + 19168362684514304*a + 288424771374979507 <= 0) & (237494511599616*a**2 + 19168362684514304*a + 289841286519364019 > 0) & (237494511599616*b**2 + 21298700823068672*b + 331053418509146547 < 0) & (768*a**2 - 1536*a*b - 6889*a + 768*b**2 + 6889*b + 1024 < 0) & (-4096*a**3 + 12288*a**2*b + 55112*a**2 - 12288*a*b**2 - 110224*a*b + 16384*a + 4096*b**3 + 55112*b**2 + 16384*b + 656779 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(14495514624), Symbol('a')), Integer(584972005753)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Integer(1536), Symbol('a')), Mul(Integer(1536), Symbol('b')), Integer(6889)), Integer(0)), LessThan(Add(Mul(Integer(237494511599616), Pow(Symbol('a'), Integer(2))), Mul(Integer(19168362684514304), Symbol('a')), Integer(288424771374979507)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(237494511599616), Pow(Symbol('a'), Integer(2))), Mul(Integer(19168362684514304), Symbol('a')), Integer(289841286519364019)), Integer(0)), StrictLessThan(Add(Mul(Integer(237494511599616), Pow(Symbol('b'), Integer(2))), Mul(Integer(21298700823068672), Symbol('b')), Integer(331053418509146547)), Integer(0)), StrictLessThan(Add(Mul(Integer(768), Pow(Symbol('a'), Integer(2))), Mul(Integer(-1), Integer(1536), Symbol('a'), Symbol('b')), Mul(Integer(-1), Integer(6889), Symbol('a')), Mul(Integer(768), Pow(Symbol('b'), Integer(2))), Mul(Integer(6889), Symbol('b')), Integer(1024)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Integer(4096), Pow(Symbol('a'), Integer(3))), Mul(Integer(12288), Pow(Symbol('a'), Integer(2)), Symbol('b')), Mul(Integer(55112), Pow(Symbol('a'), Integer(2))), Mul(Integer(-1), Integer(12288), Symbol('a'), Pow(Symbol('b'), Integer(2))), Mul(Integer(-1), Integer(110224), Symbol('a'), Symbol('b')), Mul(Integer(16384), Symbol('a')), Mul(Integer(4096), Pow(Symbol('b'), Integer(3))), Mul(Integer(55112), Pow(Symbol('b'), Integer(2))), Mul(Integer(16384), Symbol('b')), Integer(656779)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_9(a:sympy.Rational,b:sympy.Rational):
	#-a + b + 14 > 0

	pre_cond = StrictGreaterThan(Add(Mul(Integer(-1), Symbol('a')), Symbol('b'), Integer(14)), Integer(0))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_10(a:sympy.Rational,b:sympy.Rational):
	#(3799912185593856*a + 286593702497231401 < 0) & (-98304*a + 98304*b + 573049 > 0) & (31875973759370105192448*a**2 + 4808244451035790616559616*a + 111992547761836149300579797 <= 0) & (31875973759370105192448*a**2 + 4808244451035790616559616*a + 112329999227273740930305493 > 0) & (31875973759370105192448*b**2 + 5179877240888355708731392*b + 122691111896775324120698325 < 0) & (49152*a**2 - 98304*a*b - 573049*a + 49152*b**2 + 573049*b + 65536 < 0) & (-2097152*a**3 + 6291456*a**2*b + 36675136*a**2 - 6291456*a*b**2 - 73350272*a*b + 8388608*a + 2097152*b**3 + 36675136*b**2 + 8388608*b + 483408845 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(3799912185593856), Symbol('a')), Integer(286593702497231401)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Integer(98304), Symbol('a')), Mul(Integer(98304), Symbol('b')), Integer(573049)), Integer(0)), LessThan(Add(Mul(Integer(31875973759370105192448), Pow(Symbol('a'), Integer(2))), Mul(Integer(4808244451035790616559616), Symbol('a')), Integer(111992547761836149300579797)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(31875973759370105192448), Pow(Symbol('a'), Integer(2))), Mul(Integer(4808244451035790616559616), Symbol('a')), Integer(112329999227273740930305493)), Integer(0)), StrictLessThan(Add(Mul(Integer(31875973759370105192448), Pow(Symbol('b'), Integer(2))), Mul(Integer(5179877240888355708731392), Symbol('b')), Integer(122691111896775324120698325)), Integer(0)), StrictLessThan(Add(Mul(Integer(49152), Pow(Symbol('a'), Integer(2))), Mul(Integer(-1), Integer(98304), Symbol('a'), Symbol('b')), Mul(Integer(-1), Integer(573049), Symbol('a')), Mul(Integer(49152), Pow(Symbol('b'), Integer(2))), Mul(Integer(573049), Symbol('b')), Integer(65536)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Integer(2097152), Pow(Symbol('a'), Integer(3))), Mul(Integer(6291456), Pow(Symbol('a'), Integer(2)), Symbol('b')), Mul(Integer(36675136), Pow(Symbol('a'), Integer(2))), Mul(Integer(-1), Integer(6291456), Symbol('a'), Pow(Symbol('b'), Integer(2))), Mul(Integer(-1), Integer(73350272), Symbol('a'), Symbol('b')), Mul(Integer(8388608), Symbol('a')), Mul(Integer(2097152), Pow(Symbol('b'), Integer(3))), Mul(Integer(36675136), Pow(Symbol('b'), Integer(2))), Mul(Integer(8388608), Symbol('b')), Integer(483408845)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_11(a:sympy.Rational,b:sympy.Rational):
	#-a + b + 18 > 0

	pre_cond = StrictGreaterThan(Add(Mul(Integer(-1), Symbol('a')), Symbol('b'), Integer(18)), Integer(0))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_12(a:sympy.Rational,b:sympy.Rational):
	#(536870912*a + 68434549155 < 0) & (-512*a + 512*b + 3675 > 0) & (237494511599616*a**2 + 60546509281198080*a + 1982640179074982057 <= 0) & (237494511599616*a**2 + 60546509281198080*a + 1986542819395657897 > 0) & (237494511599616*b**2 + 63955854320762880*b + 2114201763153076393 < 0) & (768*a**2 - 1536*a*b - 11025*a + 768*b**2 + 11025*b + 1024 < 0) & (-4096*a**3 + 12288*a**2*b + 88200*a**2 - 12288*a*b**2 - 176400*a*b + 16384*a + 4096*b**3 + 88200*b**2 + 16384*b + 1265145 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(536870912), Symbol('a')), Integer(68434549155)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Integer(512), Symbol('a')), Mul(Integer(512), Symbol('b')), Integer(3675)), Integer(0)), LessThan(Add(Mul(Integer(237494511599616), Pow(Symbol('a'), Integer(2))), Mul(Integer(60546509281198080), Symbol('a')), Integer(1982640179074982057)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(237494511599616), Pow(Symbol('a'), Integer(2))), Mul(Integer(60546509281198080), Symbol('a')), Integer(1986542819395657897)), Integer(0)), StrictLessThan(Add(Mul(Integer(237494511599616), Pow(Symbol('b'), Integer(2))), Mul(Integer(63955854320762880), Symbol('b')), Integer(2114201763153076393)), Integer(0)), StrictLessThan(Add(Mul(Integer(768), Pow(Symbol('a'), Integer(2))), Mul(Integer(-1), Integer(1536), Symbol('a'), Symbol('b')), Mul(Integer(-1), Integer(11025), Symbol('a')), Mul(Integer(768), Pow(Symbol('b'), Integer(2))), Mul(Integer(11025), Symbol('b')), Integer(1024)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Integer(4096), Pow(Symbol('a'), Integer(3))), Mul(Integer(12288), Pow(Symbol('a'), Integer(2)), Symbol('b')), Mul(Integer(88200), Pow(Symbol('a'), Integer(2))), Mul(Integer(-1), Integer(12288), Symbol('a'), Pow(Symbol('b'), Integer(2))), Mul(Integer(-1), Integer(176400), Symbol('a'), Symbol('b')), Mul(Integer(16384), Symbol('a')), Mul(Integer(4096), Pow(Symbol('b'), Integer(3))), Mul(Integer(88200), Pow(Symbol('b'), Integer(2))), Mul(Integer(16384), Symbol('b')), Integer(1265145)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_13(a:sympy.Rational,b:sympy.Rational):
	#-a + b + 22 > 0

	pre_cond = StrictGreaterThan(Add(Mul(Integer(-1), Symbol('a')), Symbol('b'), Integer(22)), Integer(0))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_14(a:sympy.Rational,b:sympy.Rational):
	#(140737488355328*a + 28065059888700795 < 0) & (-32768*a + 32768*b + 279075 > 0) & (31875973759370105192448*a**2 + 12713046438753068321341440*a + 548468860912578644070896371 <= 0) & (31875973759370105192448*a**2 + 12713046438753068321341440*a + 549215947028441078375387891 > 0) & (31875973759370105192448*b**2 + 13256002211268706267299840*b + 575191846398015689388724979 < 0) & (49152*a**2 - 98304*a*b - 837225*a + 49152*b**2 + 837225*b + 65536 < 0) & (-2097152*a**3 + 6291456*a**2*b + 53582400*a**2 - 6291456*a*b**2 - 107164800*a*b + 8388608*a + 2097152*b**3 + 53582400*b**2 + 8388608*b + 826026315 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(140737488355328), Symbol('a')), Integer(28065059888700795)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Integer(32768), Symbol('a')), Mul(Integer(32768), Symbol('b')), Integer(279075)), Integer(0)), LessThan(Add(Mul(Integer(31875973759370105192448), Pow(Symbol('a'), Integer(2))), Mul(Integer(12713046438753068321341440), Symbol('a')), Integer(548468860912578644070896371)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(31875973759370105192448), Pow(Symbol('a'), Integer(2))), Mul(Integer(12713046438753068321341440), Symbol('a')), Integer(549215947028441078375387891)), Integer(0)), StrictLessThan(Add(Mul(Integer(31875973759370105192448), Pow(Symbol('b'), Integer(2))), Mul(Integer(13256002211268706267299840), Symbol('b')), Integer(575191846398015689388724979)), Integer(0)), StrictLessThan(Add(Mul(Integer(49152), Pow(Symbol('a'), Integer(2))), Mul(Integer(-1), Integer(98304), Symbol('a'), Symbol('b')), Mul(Integer(-1), Integer(837225), Symbol('a')), Mul(Integer(49152), Pow(Symbol('b'), Integer(2))), Mul(Integer(837225), Symbol('b')), Integer(65536)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Integer(2097152), Pow(Symbol('a'), Integer(3))), Mul(Integer(6291456), Pow(Symbol('a'), Integer(2)), Symbol('b')), Mul(Integer(53582400), Pow(Symbol('a'), Integer(2))), Mul(Integer(-1), Integer(6291456), Symbol('a'), Pow(Symbol('b'), Integer(2))), Mul(Integer(-1), Integer(107164800), Symbol('a'), Symbol('b')), Mul(Integer(8388608), Symbol('a')), Mul(Integer(2097152), Pow(Symbol('b'), Integer(3))), Mul(Integer(53582400), Pow(Symbol('b'), Integer(2))), Mul(Integer(8388608), Symbol('b')), Integer(826026315)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_15(a:sympy.Rational,b:sympy.Rational):
	#-a + b + 26 > 0

	pre_cond = StrictGreaterThan(Add(Mul(Integer(-1), Symbol('a')), Symbol('b'), Integer(26)), Integer(0))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_16(a:sympy.Rational,b:sympy.Rational):
	#(243194379878006784*a + 71842146461335250209 < 0) & (-393216*a + 393216*b + 3876961 > 0) & (16320498564797493858533376*a**2 + 9642489672683657129363505152*a + 525201092758213612908348279089 <= 0) & (16320498564797493858533376*a**2 + 9642489672683657129363505152*a + 525717853695756989402546538801 > 0) & (16320498564797493858533376*b**2 + 9964317555762045885605740544*b + 544738119204312948826762742065 < 0) & (196608*a**2 - 393216*a*b - 3876961*a + 196608*b**2 + 3876961*b + 262144 < 0) & (-16777216*a**3 + 50331648*a**2*b + 496251008*a**2 - 50331648*a*b**2 - 992502016*a*b + 67108864*a + 16777216*b**3 + 496251008*b**2 + 67108864*b + 8149897745 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(243194379878006784), Symbol('a')), Integer(71842146461335250209)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Integer(393216), Symbol('a')), Mul(Integer(393216), Symbol('b')), Integer(3876961)), Integer(0)), LessThan(Add(Mul(Integer(16320498564797493858533376), Pow(Symbol('a'), Integer(2))), Mul(Integer(9642489672683657129363505152), Symbol('a')), Integer(525201092758213612908348279089)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(16320498564797493858533376), Pow(Symbol('a'), Integer(2))), Mul(Integer(9642489672683657129363505152), Symbol('a')), Integer(525717853695756989402546538801)), Integer(0)), StrictLessThan(Add(Mul(Integer(16320498564797493858533376), Pow(Symbol('b'), Integer(2))), Mul(Integer(9964317555762045885605740544), Symbol('b')), Integer(544738119204312948826762742065)), Integer(0)), StrictLessThan(Add(Mul(Integer(196608), Pow(Symbol('a'), Integer(2))), Mul(Integer(-1), Integer(393216), Symbol('a'), Symbol('b')), Mul(Integer(-1), Integer(3876961), Symbol('a')), Mul(Integer(196608), Pow(Symbol('b'), Integer(2))), Mul(Integer(3876961), Symbol('b')), Integer(262144)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Integer(16777216), Pow(Symbol('a'), Integer(3))), Mul(Integer(50331648), Pow(Symbol('a'), Integer(2)), Symbol('b')), Mul(Integer(496251008), Pow(Symbol('a'), Integer(2))), Mul(Integer(-1), Integer(50331648), Symbol('a'), Pow(Symbol('b'), Integer(2))), Mul(Integer(-1), Integer(992502016), Symbol('a'), Symbol('b')), Mul(Integer(67108864), Symbol('a')), Mul(Integer(16777216), Pow(Symbol('b'), Integer(3))), Mul(Integer(496251008), Pow(Symbol('b'), Integer(2))), Mul(Integer(67108864), Symbol('b')), Integer(8149897745)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_17(a:sympy.Rational,b:sympy.Rational):
	#-a + b + 30 > 0

	pre_cond = StrictGreaterThan(Add(Mul(Integer(-1), Symbol('a')), Symbol('b'), Integer(30)), Integer(0))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_18(a:sympy.Rational,b:sympy.Rational):
	#(243194379878006784*a + 101912338481792457529 < 0) & (-393216*a + 393216*b + 4405801 > 0) & (16320498564797493858533376*a**2 + 13678442526193153017078874112*a + 911396345717009784929205256339 <= 0) & (16320498564797493858533376*a**2 + 13678442526193153017078874112*a + 912067223206437765493370814611 > 0) & (16320498564797493858533376*b**2 + 14044169601883274290065833984*b + 938089920094280047090328567955 < 0) & (196608*a**2 - 393216*a*b - 4405801*a + 196608*b**2 + 4405801*b + 262144 < 0) & (-16777216*a**3 + 50331648*a**2*b + 563942528*a**2 - 50331648*a*b**2 - 1127885056*a*b + 67108864*a + 16777216*b**3 + 563942528*b**2 + 67108864*b + 9798016555 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(243194379878006784), Symbol('a')), Integer(101912338481792457529)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Integer(393216), Symbol('a')), Mul(Integer(393216), Symbol('b')), Integer(4405801)), Integer(0)), LessThan(Add(Mul(Integer(16320498564797493858533376), Pow(Symbol('a'), Integer(2))), Mul(Integer(13678442526193153017078874112), Symbol('a')), Integer(911396345717009784929205256339)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(16320498564797493858533376), Pow(Symbol('a'), Integer(2))), Mul(Integer(13678442526193153017078874112), Symbol('a')), Integer(912067223206437765493370814611)), Integer(0)), StrictLessThan(Add(Mul(Integer(16320498564797493858533376), Pow(Symbol('b'), Integer(2))), Mul(Integer(14044169601883274290065833984), Symbol('b')), Integer(938089920094280047090328567955)), Integer(0)), StrictLessThan(Add(Mul(Integer(196608), Pow(Symbol('a'), Integer(2))), Mul(Integer(-1), Integer(393216), Symbol('a'), Symbol('b')), Mul(Integer(-1), Integer(4405801), Symbol('a')), Mul(Integer(196608), Pow(Symbol('b'), Integer(2))), Mul(Integer(4405801), Symbol('b')), Integer(262144)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Integer(16777216), Pow(Symbol('a'), Integer(3))), Mul(Integer(50331648), Pow(Symbol('a'), Integer(2)), Symbol('b')), Mul(Integer(563942528), Pow(Symbol('a'), Integer(2))), Mul(Integer(-1), Integer(50331648), Symbol('a'), Pow(Symbol('b'), Integer(2))), Mul(Integer(-1), Integer(1127885056), Symbol('a'), Symbol('b')), Mul(Integer(67108864), Symbol('a')), Mul(Integer(16777216), Pow(Symbol('b'), Integer(3))), Mul(Integer(563942528), Pow(Symbol('b'), Integer(2))), Mul(Integer(67108864), Symbol('b')), Integer(9798016555)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_19(a:sympy.Rational,b:sympy.Rational):
	#-a + b + 34 > 0

	pre_cond = StrictGreaterThan(Add(Mul(Integer(-1), Symbol('a')), Symbol('b'), Integer(34)), Integer(0))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_20(a:sympy.Rational,b:sympy.Rational):
	#(36893488147419103232*a + 21135929531321204151867 < 0) & (-2097152*a + 2097152*b + 26302563 > 0) & (4278320775770274230051373318144*a**2 + 4902018809809599693194841846448128*a + 389614094683458292189010281284189971 <= 0) & (4278320775770274230051373318144*a**2 + 4902018809809599693194841846448128*a + 389835256101189514752104922412957459 > 0) & (4278320775770274230051373318144*b**2 + 5009336545232598609308888648908800*b + 398835413684938955201538469344526099 < 0) & (3145728*a**2 - 6291456*a*b - 78907689*a + 3145728*b**2 + 78907689*b + 4194304 < 0) & (-1073741824*a**3 + 3221225472*a**2*b + 40400736768*a**2 - 3221225472*a*b**2 - 80801473536*a*b + 4294967296*a + 1073741824*b**3 + 40400736768*b**2 + 4294967296*b + 738195003819 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(36893488147419103232), Symbol('a')), Integer(21135929531321204151867)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Integer(2097152), Symbol('a')), Mul(Integer(2097152), Symbol('b')), Integer(26302563)), Integer(0)), LessThan(Add(Mul(Integer(4278320775770274230051373318144), Pow(Symbol('a'), Integer(2))), Mul(Integer(4902018809809599693194841846448128), Symbol('a')), Integer(389614094683458292189010281284189971)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(4278320775770274230051373318144), Pow(Symbol('a'), Integer(2))), Mul(Integer(4902018809809599693194841846448128), Symbol('a')), Integer(389835256101189514752104922412957459)), Integer(0)), StrictLessThan(Add(Mul(Integer(4278320775770274230051373318144), Pow(Symbol('b'), Integer(2))), Mul(Integer(5009336545232598609308888648908800), Symbol('b')), Integer(398835413684938955201538469344526099)), Integer(0)), StrictLessThan(Add(Mul(Integer(3145728), Pow(Symbol('a'), Integer(2))), Mul(Integer(-1), Integer(6291456), Symbol('a'), Symbol('b')), Mul(Integer(-1), Integer(78907689), Symbol('a')), Mul(Integer(3145728), Pow(Symbol('b'), Integer(2))), Mul(Integer(78907689), Symbol('b')), Integer(4194304)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Integer(1073741824), Pow(Symbol('a'), Integer(3))), Mul(Integer(3221225472), Pow(Symbol('a'), Integer(2)), Symbol('b')), Mul(Integer(40400736768), Pow(Symbol('a'), Integer(2))), Mul(Integer(-1), Integer(3221225472), Symbol('a'), Pow(Symbol('b'), Integer(2))), Mul(Integer(-1), Integer(80801473536), Symbol('a'), Symbol('b')), Mul(Integer(4294967296), Symbol('a')), Mul(Integer(1073741824), Pow(Symbol('b'), Integer(3))), Mul(Integer(40400736768), Pow(Symbol('b'), Integer(2))), Mul(Integer(4294967296), Symbol('b')), Integer(738195003819)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_21(a:sympy.Rational,b:sympy.Rational):
	#-a + b + 38 > 0

	pre_cond = StrictGreaterThan(Add(Mul(Integer(-1), Symbol('a')), Symbol('b'), Integer(38)), Integer(0))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_22(a:sympy.Rational,b:sympy.Rational):
	#(36893488147419103232*a + 28084129715847126407955 < 0) & (-2097152*a + 2097152*b + 29109675 > 0) & (4278320775770274230051373318144*a**2 + 6513502607973999766318212678942720*a + 606055922793583343098901961918531713 <= 0) & (4278320775770274230051373318144*a**2 + 6513502607973999766318212678942720*a + 606327522193344439801634563374598273 > 0) & (4278320775770274230051373318144*b**2 + 6632273710238805138077313316945920*b + 617880496379263452988126657345374337 < 0) & (3145728*a**2 - 6291456*a*b - 87329025*a + 3145728*b**2 + 87329025*b + 4194304 < 0) & (-1073741824*a**3 + 3221225472*a**2*b + 44712460800*a**2 - 3221225472*a*b**2 - 89424921600*a*b + 4294967296*a + 1073741824*b**3 + 44712460800*b**2 + 4294967296*b + 855285509505 > 0)

	pre_cond = And(StrictLessThan(Add(Mul(Integer(36893488147419103232), Symbol('a')), Integer(28084129715847126407955)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Integer(2097152), Symbol('a')), Mul(Integer(2097152), Symbol('b')), Integer(29109675)), Integer(0)), LessThan(Add(Mul(Integer(4278320775770274230051373318144), Pow(Symbol('a'), Integer(2))), Mul(Integer(6513502607973999766318212678942720), Symbol('a')), Integer(606055922793583343098901961918531713)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(4278320775770274230051373318144), Pow(Symbol('a'), Integer(2))), Mul(Integer(6513502607973999766318212678942720), Symbol('a')), Integer(606327522193344439801634563374598273)), Integer(0)), StrictLessThan(Add(Mul(Integer(4278320775770274230051373318144), Pow(Symbol('b'), Integer(2))), Mul(Integer(6632273710238805138077313316945920), Symbol('b')), Integer(617880496379263452988126657345374337)), Integer(0)), StrictLessThan(Add(Mul(Integer(3145728), Pow(Symbol('a'), Integer(2))), Mul(Integer(-1), Integer(6291456), Symbol('a'), Symbol('b')), Mul(Integer(-1), Integer(87329025), Symbol('a')), Mul(Integer(3145728), Pow(Symbol('b'), Integer(2))), Mul(Integer(87329025), Symbol('b')), Integer(4194304)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Integer(1073741824), Pow(Symbol('a'), Integer(3))), Mul(Integer(3221225472), Pow(Symbol('a'), Integer(2)), Symbol('b')), Mul(Integer(44712460800), Pow(Symbol('a'), Integer(2))), Mul(Integer(-1), Integer(3221225472), Symbol('a'), Pow(Symbol('b'), Integer(2))), Mul(Integer(-1), Integer(89424921600), Symbol('a'), Symbol('b')), Mul(Integer(4294967296), Symbol('a')), Mul(Integer(1073741824), Pow(Symbol('b'), Integer(3))), Mul(Integer(44712460800), Pow(Symbol('b'), Integer(2))), Mul(Integer(4294967296), Symbol('b')), Integer(855285509505)), Integer(0)))

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



#return post-condition single variable
def return_post_condition_single_var(post_condition, a:sympy.Rational=None, b:sympy.Rational=None, x:sympy.Rational=None, y:sympy.Rational=None):
	assert a!=None
	assert b!=None


	if x==None:
		assert y!=None
		return lambda x: post_condition(a=a, b=b, x=x, y=y)

	if y==None:
		assert x!=None
		return lambda y: post_condition(a=a, b=b, x=x, y=y)


	return post_condition(a=a, b=b, x=x, y=y)


def get_univariate_poly( a:sympy.Rational, b:sympy.Rational, x:sympy.Rational, y:sympy.Rational ):


	post_cond =  And(StrictGreaterThan(Integer(0), Add(Symbol('a'), Pow(Symbol('x'), Integer(3)), Mul(Pow(Symbol('x'), Integer(2)), Pow(Symbol('y'), Integer(2))), Symbol('x'), Pow(Symbol('y'), Integer(3)), Symbol('y'))), StrictGreaterThan(Integer(0), Add(Mul(Integer(-1), Symbol('b')), Mul(Integer(-1), Pow(Symbol('x'), Integer(3))), Mul(Integer(-1), Pow(Symbol('x'), Integer(2)), Pow(Symbol('y'), Integer(2))), Symbol('x'), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(-1), Symbol('y')))))

	eval = post_cond.subs( { 'a':a, 'b':b, 'x':x, 'y':y })
	return eval



if __name__=="__main__":
	
	ip_0=int(input("enter numerator of a:\n"))
	ip_1=int(input("enter denominator of a:\n"))
	assert(ip_1!=0), ("Error denominator entered is 0")
	a=sympy.Rational(ip_0,ip_1)
	
	
	ip_0=int(input("enter numerator of b:\n"))
	ip_1=int(input("enter denominator of b:\n"))
	assert(ip_1!=0), ("Error denominator entered is 0")
	b=sympy.Rational(ip_0,ip_1)
	
	
	lambda_var_0 = sympy.symbols('lambda_var_0')
	
	
	if pre_condition_0(a=a,b=b)==True:
		all_vals = dict()
		all_vals['a'] = a
		all_vals['b'] = b
		all_vals['x'] = Symbol('lambda_var_0')
		all_vals['y'] = Integer(0)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_0 SAT")

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_1(a=a,b=b)==True:
		all_vals = dict()
		all_vals['a'] = a
		all_vals['b'] = b
		all_vals['x'] = Integer(0)
		all_vals['y'] = Symbol('lambda_var_0')
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_1 SAT")

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_2(a=a,b=b)==True:
		all_vals = dict()
		all_vals['a'] = a
		all_vals['b'] = b
		all_vals['x'] = Add(Symbol('lambda_var_0'), Integer(-1))
		all_vals['y'] = Rational(7, 8)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_2 SAT")

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_3(a=a,b=b)==True:
		all_vals = dict()
		all_vals['a'] = a
		all_vals['b'] = b
		all_vals['x'] = Integer(-1)
		all_vals['y'] = Add(Symbol('lambda_var_0'), Rational(7, 8))
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_3 SAT")

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_4(a=a,b=b)==True:
		all_vals = dict()
		all_vals['a'] = a
		all_vals['b'] = b
		all_vals['x'] = Add(Symbol('lambda_var_0'), Integer(-3))
		all_vals['y'] = Rational(13, 8)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_4 SAT")

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_5(a=a,b=b)==True:
		all_vals = dict()
		all_vals['a'] = a
		all_vals['b'] = b
		all_vals['x'] = Integer(-3)
		all_vals['y'] = Add(Symbol('lambda_var_0'), Rational(13, 8))
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_5 SAT")

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_6(a=a,b=b)==True:
		all_vals = dict()
		all_vals['a'] = a
		all_vals['b'] = b
		all_vals['x'] = Add(Symbol('lambda_var_0'), Integer(-5))
		all_vals['y'] = Rational(69, 32)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_6 SAT")

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_7(a=a,b=b)==True:
		all_vals = dict()
		all_vals['a'] = a
		all_vals['b'] = b
		all_vals['x'] = Integer(-5)
		all_vals['y'] = Add(Symbol('lambda_var_0'), Rational(69, 32))
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_7 SAT")

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_8(a=a,b=b)==True:
		all_vals = dict()
		all_vals['a'] = a
		all_vals['b'] = b
		all_vals['x'] = Add(Symbol('lambda_var_0'), Integer(-7))
		all_vals['y'] = Rational(83, 32)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_8 SAT")

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_9(a=a,b=b)==True:
		all_vals = dict()
		all_vals['a'] = a
		all_vals['b'] = b
		all_vals['x'] = Integer(-7)
		all_vals['y'] = Add(Symbol('lambda_var_0'), Rational(83, 32))
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_9 SAT")

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_10(a=a,b=b)==True:
		all_vals = dict()
		all_vals['a'] = a
		all_vals['b'] = b
		all_vals['x'] = Add(Symbol('lambda_var_0'), Integer(-9))
		all_vals['y'] = Rational(757, 256)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_10 SAT")

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_11(a=a,b=b)==True:
		all_vals = dict()
		all_vals['a'] = a
		all_vals['b'] = b
		all_vals['x'] = Integer(-9)
		all_vals['y'] = Add(Symbol('lambda_var_0'), Rational(757, 256))
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_11 SAT")

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_12(a=a,b=b)==True:
		all_vals = dict()
		all_vals['a'] = a
		all_vals['b'] = b
		all_vals['x'] = Add(Symbol('lambda_var_0'), Integer(-11))
		all_vals['y'] = Rational(105, 32)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_12 SAT")

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_13(a=a,b=b)==True:
		all_vals = dict()
		all_vals['a'] = a
		all_vals['b'] = b
		all_vals['x'] = Integer(-11)
		all_vals['y'] = Add(Symbol('lambda_var_0'), Rational(105, 32))
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_13 SAT")

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_14(a=a,b=b)==True:
		all_vals = dict()
		all_vals['a'] = a
		all_vals['b'] = b
		all_vals['x'] = Add(Symbol('lambda_var_0'), Integer(-13))
		all_vals['y'] = Rational(915, 256)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_14 SAT")

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_15(a=a,b=b)==True:
		all_vals = dict()
		all_vals['a'] = a
		all_vals['b'] = b
		all_vals['x'] = Integer(-13)
		all_vals['y'] = Add(Symbol('lambda_var_0'), Rational(915, 256))
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_15 SAT")

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_16(a=a,b=b)==True:
		all_vals = dict()
		all_vals['a'] = a
		all_vals['b'] = b
		all_vals['x'] = Add(Symbol('lambda_var_0'), Integer(-15))
		all_vals['y'] = Rational(1969, 512)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_16 SAT")

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_17(a=a,b=b)==True:
		all_vals = dict()
		all_vals['a'] = a
		all_vals['b'] = b
		all_vals['x'] = Integer(-15)
		all_vals['y'] = Add(Symbol('lambda_var_0'), Rational(1969, 512))
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_17 SAT")

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_18(a=a,b=b)==True:
		all_vals = dict()
		all_vals['a'] = a
		all_vals['b'] = b
		all_vals['x'] = Add(Symbol('lambda_var_0'), Integer(-17))
		all_vals['y'] = Rational(2099, 512)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_18 SAT")

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_19(a=a,b=b)==True:
		all_vals = dict()
		all_vals['a'] = a
		all_vals['b'] = b
		all_vals['x'] = Integer(-17)
		all_vals['y'] = Add(Symbol('lambda_var_0'), Rational(2099, 512))
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_19 SAT")

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_20(a=a,b=b)==True:
		all_vals = dict()
		all_vals['a'] = a
		all_vals['b'] = b
		all_vals['x'] = Add(Symbol('lambda_var_0'), Integer(-19))
		all_vals['y'] = Rational(8883, 2048)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_20 SAT")

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_21(a=a,b=b)==True:
		all_vals = dict()
		all_vals['a'] = a
		all_vals['b'] = b
		all_vals['x'] = Integer(-19)
		all_vals['y'] = Add(Symbol('lambda_var_0'), Rational(8883, 2048))
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_21 SAT")

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass
	
	
	if pre_condition_22(a=a,b=b)==True:
		all_vals = dict()
		all_vals['a'] = a
		all_vals['b'] = b
		all_vals['x'] = Add(Symbol('lambda_var_0'), Integer(-21))
		all_vals['y'] = Rational(9345, 2048)
		uv_poly_expr = get_univariate_poly(**all_vals)
		solution_exists,  lambda_val = get_lambda_val(uv_poly_expr)

		if solution_exists:
			print("pre_condition_22 SAT")

			print("x=", all_vals["x"].subs( { 'lambda_var_0':lambda_val } ))

			print("y=", all_vals["y"].subs( { 'lambda_var_0':lambda_val } ))

			print("SAT")
			exit(0)
		pass


	print("UNKNOWN")
