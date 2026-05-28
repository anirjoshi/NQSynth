import sympy
from sympy import *

def pre_condition_0(a:sympy.Rational):
	#(a + y**2 - z**2 + 1/4 < 0) & (-a**2 + a - y**2 + 2*y + 11/4 > 0)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Pow(Symbol('y'), Integer(2)), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(1, 4)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('a'), Integer(2))), Symbol('a'), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Mul(Integer(2), Symbol('y')), Rational(11, 4)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1(a:sympy.Rational):
	#(a**2 - a < 11/4) & (a - z**2 + 1/4 < 0)

	pre_cond = And(StrictLessThan(Add(Pow(Symbol('a'), Integer(2)), Mul(Integer(-1), Symbol('a'))), Rational(11, 4)), StrictLessThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(1, 4)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_2(a:sympy.Rational):
	#(a < 3/4) & (a > 1/2 - sqrt(3))

	pre_cond = And(StrictLessThan(Symbol('a'), Rational(3, 4)), StrictGreaterThan(Symbol('a'), Add(Rational(1, 2), Mul(Integer(-1), Pow(Integer(3), Rational(1, 2))))))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_3(a:sympy.Rational):
	#(a + y**2 - z**2 + 9/64 < 0) & (-a**2 + 3*a/4 - y**2 + 2*y + 183/64 > 0)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Pow(Symbol('y'), Integer(2)), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(9, 64)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('a'), Integer(2))), Mul(Rational(3, 4), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Mul(Integer(2), Symbol('y')), Rational(183, 64)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_4(a:sympy.Rational):
	#(a - z**2 + 73/64 < 0) & (4*a**2 - 3*a < 247/16)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(73, 64)), Integer(0)), StrictLessThan(Add(Mul(Integer(4), Pow(Symbol('a'), Integer(2))), Mul(Integer(-1), Integer(3), Symbol('a'))), Rational(247, 16)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_5(a:sympy.Rational):
	#(a > -13/8) & (a < 2313/1024)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(-13, 8)), StrictLessThan(Symbol('a'), Rational(2313, 1024)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_6(a:sympy.Rational):
	#(a + y**2 - z**2 + 121/1024 < 0) & (-a**2 + 11*a/16 - y**2 + 2*y + 2951/1024 > 0)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Pow(Symbol('y'), Integer(2)), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(121, 1024)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('a'), Integer(2))), Mul(Rational(11, 16), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Mul(Integer(2), Symbol('y')), Rational(2951, 1024)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_7(a:sympy.Rational):
	#(a - z**2 + 1145/1024 < 0) & (16*a**2 - 11*a < 3975/64)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(1145, 1024)), Integer(0)), StrictLessThan(Add(Mul(Integer(16), Pow(Symbol('a'), Integer(2))), Mul(Integer(-1), Integer(11), Symbol('a'))), Rational(3975, 64)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_8(a:sympy.Rational):
	#(a > -53/32) & (a < 152345/65536)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(-53, 32)), StrictLessThan(Symbol('a'), Rational(152345, 65536)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_9(a:sympy.Rational):
	#(a + y**2 - z**2 + 1849/16384 < 0) & (-a**2 + 43*a/64 - y**2 + 2*y + 47303/16384 > 0)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Pow(Symbol('y'), Integer(2)), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(1849, 16384)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('a'), Integer(2))), Mul(Rational(43, 64), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Mul(Integer(2), Symbol('y')), Rational(47303, 16384)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_10(a:sympy.Rational):
	#(a - z**2 + 18233/16384 < 0) & (64*a**2 - 43*a < 63687/256)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(18233, 16384)), Integer(0)), StrictLessThan(Add(Mul(Integer(64), Pow(Symbol('a'), Integer(2))), Mul(Integer(-1), Integer(43), Symbol('a'))), Rational(63687, 256)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_11(a:sympy.Rational):
	#(a > -213/128) & (a < 152693/65536)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(-213, 128)), StrictLessThan(Symbol('a'), Rational(152693, 65536)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_12(a:sympy.Rational):
	#(a + y**2 - z**2 + 29241/262144 < 0) & (-a**2 + 171*a/256 - y**2 + 2*y + 757191/262144 > 0)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Pow(Symbol('y'), Integer(2)), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(29241, 262144)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('a'), Integer(2))), Mul(Rational(171, 256), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Mul(Integer(2), Symbol('y')), Rational(757191, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_13(a:sympy.Rational):
	#(a - z**2 + 291385/262144 < 0) & (256*a**2 - 171*a < 1019335/1024)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(291385, 262144)), Integer(0)), StrictLessThan(Add(Mul(Integer(256), Pow(Symbol('a'), Integer(2))), Mul(Integer(-1), Integer(171), Symbol('a'))), Rational(1019335, 1024)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_14(a:sympy.Rational):
	#(a > -853/512) & (a < 9785441/4194304)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(-853, 512)), StrictLessThan(Symbol('a'), Rational(9785441, 4194304)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_15(a:sympy.Rational):
	#(a + y**2 - z**2 + 1868689/16777216 < 0) & (-a**2 + 1367*a/2048 - y**2 + 2*y + 48462959/16777216 > 0)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Pow(Symbol('y'), Integer(2)), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(1868689, 16777216)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('a'), Integer(2))), Mul(Rational(1367, 2048), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Mul(Integer(2), Symbol('y')), Rational(48462959, 16777216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_16(a:sympy.Rational):
	#(a - z**2 + 18645905/16777216 < 0) & (2048*a**2 - 1367*a < 65240175/8192)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(18645905, 16777216)), Integer(0)), StrictLessThan(Add(Mul(Integer(2048), Pow(Symbol('a'), Integer(2))), Mul(Integer(-1), Integer(1367), Symbol('a'))), Rational(65240175, 8192)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_17(a:sympy.Rational):
	#(a > -6825/4096) & (a < 156608405/67108864)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(-6825, 4096)), StrictLessThan(Symbol('a'), Rational(156608405, 67108864)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_18(a:sympy.Rational):
	#(a + y**2 - z**2 + 119574225/1073741824 < 0) & (-a**2 + 10935*a/16384 - y**2 + 2*y + 3101651247/1073741824 > 0)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Pow(Symbol('y'), Integer(2)), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(119574225, 1073741824)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('a'), Integer(2))), Mul(Rational(10935, 16384), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Mul(Integer(2), Symbol('y')), Rational(3101651247, 1073741824)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_19(a:sympy.Rational):
	#(a - z**2 + 1193316049/1073741824 < 0) & (16384*a**2 - 10935*a < 4175393071/65536)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(1193316049, 1073741824)), Integer(0)), StrictLessThan(Add(Mul(Integer(16384), Pow(Symbol('a'), Integer(2))), Mul(Integer(-1), Integer(10935), Symbol('a'))), Rational(4175393071, 65536)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_20(a:sympy.Rational):
	#(a > -54601/32768) & (a < 40092588177/17179869184)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(-54601, 32768)), StrictLessThan(Symbol('a'), Rational(40092588177, 17179869184)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_21(a:sympy.Rational):
	#(a + y**2 - z**2 + 37006430198504726204560759440015369/332306998946228968225951765070086144 < 0) & (-a**2 + 192370554395688963*a/288230376151711744 - y**2 + 2*y + 959914566640182178473294535770243063/332306998946228968225951765070086144 > 0)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Pow(Symbol('y'), Integer(2)), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(37006430198504726204560759440015369, 332306998946228968225951765070086144)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('a'), Integer(2))), Mul(Rational(192370554395688963, 288230376151711744), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Mul(Integer(2), Symbol('y')), Rational(959914566640182178473294535770243063, 332306998946228968225951765070086144)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_22(a:sympy.Rational):
	#(a - z**2 + 369313426668853620471437993139240969/332306998946228968225951765070086144 < 0) & (288230376151711744*a**2 - 192370554395688963*a < 1292221565586411142087560282412941303/1152921504606846976)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(369313426668853620471437993139240969, 332306998946228968225951765070086144)), Integer(0)), StrictLessThan(Add(Mul(Integer(288230376151711744), Pow(Symbol('a'), Integer(2))), Mul(Integer(-1), Integer(192370554395688963), Symbol('a'))), Rational(1292221565586411142087560282412941303, 1152921504606846976)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_23(a:sympy.Rational):
	#(a < 12705924258208537714689598348499902481305/5444517870735015415413993718908291383296) & (a > 192370554395688963/576460752303423488 - sqrt(288230376151711743)/268435456)

	pre_cond = And(StrictLessThan(Symbol('a'), Rational(12705924258208537714689598348499902481305, 5444517870735015415413993718908291383296)), StrictGreaterThan(Symbol('a'), Add(Rational(192370554395688963, 576460752303423488), Mul(Integer(-1), Rational(1, 268435456), Pow(Integer(288230376151711743), Rational(1, 2))))))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_24(a:sympy.Rational):
	#(a + y**2 - z**2 + 606313352372301434184770344590508180225/5444517870735015415413993718908291383296 < 0) & (-a**2 + 24623430962648187265*a/36893488147419103232 - y**2 + 2*y + 15727240259832744812057210812134365969663/5444517870735015415413993718908291383296 > 0)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Pow(Symbol('y'), Integer(2)), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(606313352372301434184770344590508180225, 5444517870735015415413993718908291383296)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('a'), Integer(2))), Mul(Rational(24623430962648187265, 36893488147419103232), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Mul(Integer(2), Symbol('y')), Rational(15727240259832744812057210812134365969663, 5444517870735015415413993718908291383296)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_25(a:sympy.Rational):
	#(a - z**2 + 6050831182542497717853286941518620410625/5444517870735015415413993718908291383296 < 0) & (36893488147419103232*a**2 - 24623430962648187265*a < 21171758130567760151913340805128333933823/147573952589676412928)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(6050831182542497717853286941518620410625, 5444517870735015415413993718908291383296)), Integer(0)), StrictLessThan(Add(Mul(Integer(36893488147419103232), Pow(Symbol('a'), Integer(2))), Mul(Integer(-1), Integer(24623430962648187265), Symbol('a'))), Rational(21171758130567760151913340805128333933823, 147573952589676412928)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_26(a:sympy.Rational):
	#(a < 813179152525346414339585835102428211193689/348449143727040986586495598010130648530944) & (a > 24623430962648187265/73786976294838206464 - sqrt(288230376151711743)/268435456)

	pre_cond = And(StrictLessThan(Symbol('a'), Rational(813179152525346414339585835102428211193689, 348449143727040986586495598010130648530944)), StrictGreaterThan(Symbol('a'), Add(Rational(24623430962648187265, 73786976294838206464), Mul(Integer(-1), Rational(1, 268435456), Pow(Integer(288230376151711743), Rational(1, 2))))))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_27(a:sympy.Rational):
	#(a + y**2 - z**2 + 606313352372301434184770344590508180225/5444517870735015415413993718908291383296 < 0) & (-a**2 + 24623430962648187265*a/36893488147419103232 - y**2 + 2*y + 15727240259832744812057210812134365969663/5444517870735015415413993718908291383296 > 0)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Pow(Symbol('y'), Integer(2)), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(606313352372301434184770344590508180225, 5444517870735015415413993718908291383296)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('a'), Integer(2))), Mul(Rational(24623430962648187265, 36893488147419103232), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Mul(Integer(2), Symbol('y')), Rational(15727240259832744812057210812134365969663, 5444517870735015415413993718908291383296)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_28(a:sympy.Rational):
	#(a - z**2 + 6050831182542497717853286941518620410625/5444517870735015415413993718908291383296 < 0) & (36893488147419103232*a**2 - 24623430962648187265*a < 21171758130567760151913340805128333933823/147573952589676412928)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(6050831182542497717853286941518620410625, 5444517870735015415413993718908291383296)), Integer(0)), StrictLessThan(Add(Mul(Integer(36893488147419103232), Pow(Symbol('a'), Integer(2))), Mul(Integer(-1), Integer(24623430962648187265), Symbol('a'))), Rational(21171758130567760151913340805128333933823, 147573952589676412928)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_29(a:sympy.Rational):
	#(a < 813179152525346414339585835102428211193689/348449143727040986586495598010130648530944) & (a > 24623430962648187265/73786976294838206464 - sqrt(288230376151711743)/268435456)

	pre_cond = And(StrictLessThan(Symbol('a'), Rational(813179152525346414339585835102428211193689, 348449143727040986586495598010130648530944)), StrictGreaterThan(Symbol('a'), Add(Rational(24623430962648187265, 73786976294838206464), Mul(Integer(-1), Rational(1, 268435456), Pow(Integer(288230376151711743), Rational(1, 2))))))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_30(a:sympy.Rational):
	#(a + y**2 - z**2 + 606313352372301434184770344590508180225/5444517870735015415413993718908291383296 < 0) & (-a**2 + 24623430962648187265*a/36893488147419103232 - y**2 + 2*y + 15727240259832744812057210812134365969663/5444517870735015415413993718908291383296 > 0)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Pow(Symbol('y'), Integer(2)), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(606313352372301434184770344590508180225, 5444517870735015415413993718908291383296)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('a'), Integer(2))), Mul(Rational(24623430962648187265, 36893488147419103232), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Mul(Integer(2), Symbol('y')), Rational(15727240259832744812057210812134365969663, 5444517870735015415413993718908291383296)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_31(a:sympy.Rational):
	#(a - z**2 + 6050831182542497717853286941518620410625/5444517870735015415413993718908291383296 < 0) & (36893488147419103232*a**2 - 24623430962648187265*a < 21171758130567760151913340805128333933823/147573952589676412928)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(6050831182542497717853286941518620410625, 5444517870735015415413993718908291383296)), Integer(0)), StrictLessThan(Add(Mul(Integer(36893488147419103232), Pow(Symbol('a'), Integer(2))), Mul(Integer(-1), Integer(24623430962648187265), Symbol('a'))), Rational(21171758130567760151913340805128333933823, 147573952589676412928)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_32(a:sympy.Rational):
	#(a < 813179152525346414339585835102428211193689/348449143727040986586495598010130648530944) & (a > 24623430962648187265/73786976294838206464 - sqrt(288230376151711743)/268435456)

	pre_cond = And(StrictLessThan(Symbol('a'), Rational(813179152525346414339585835102428211193689, 348449143727040986586495598010130648530944)), StrictGreaterThan(Symbol('a'), Add(Rational(24623430962648187265, 73786976294838206464), Mul(Integer(-1), Rational(1, 268435456), Pow(Integer(288230376151711743), Rational(1, 2))))))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_33(a:sympy.Rational):
	#(a + y**2 - z**2 + 606313352372301434184770344590508180225/5444517870735015415413993718908291383296 < 0) & (-a**2 + 24623430962648187265*a/36893488147419103232 - y**2 + 2*y + 15727240259832744812057210812134365969663/5444517870735015415413993718908291383296 > 0)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Pow(Symbol('y'), Integer(2)), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(606313352372301434184770344590508180225, 5444517870735015415413993718908291383296)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('a'), Integer(2))), Mul(Rational(24623430962648187265, 36893488147419103232), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Mul(Integer(2), Symbol('y')), Rational(15727240259832744812057210812134365969663, 5444517870735015415413993718908291383296)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_34(a:sympy.Rational):
	#(a - z**2 + 6050831182542497717853286941518620410625/5444517870735015415413993718908291383296 < 0) & (36893488147419103232*a**2 - 24623430962648187265*a < 21171758130567760151913340805128333933823/147573952589676412928)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(6050831182542497717853286941518620410625, 5444517870735015415413993718908291383296)), Integer(0)), StrictLessThan(Add(Mul(Integer(36893488147419103232), Pow(Symbol('a'), Integer(2))), Mul(Integer(-1), Integer(24623430962648187265), Symbol('a'))), Rational(21171758130567760151913340805128333933823, 147573952589676412928)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_35(a:sympy.Rational):
	#(a < 813179152525346414339585835102428211193689/348449143727040986586495598010130648530944) & (a > 24623430962648187265/73786976294838206464 - sqrt(288230376151711743)/268435456)

	pre_cond = And(StrictLessThan(Symbol('a'), Rational(813179152525346414339585835102428211193689, 348449143727040986586495598010130648530944)), StrictGreaterThan(Symbol('a'), Add(Rational(24623430962648187265, 73786976294838206464), Mul(Integer(-1), Rational(1, 268435456), Pow(Integer(288230376151711743), Rational(1, 2))))))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_36(a:sympy.Rational):
	#(a + y**2 - z**2 + 606313352372301434184770344590508180225/5444517870735015415413993718908291383296 < 0) & (-a**2 + 24623430962648187265*a/36893488147419103232 - y**2 + 2*y + 15727240259832744812057210812134365969663/5444517870735015415413993718908291383296 > 0)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Pow(Symbol('y'), Integer(2)), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(606313352372301434184770344590508180225, 5444517870735015415413993718908291383296)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('a'), Integer(2))), Mul(Rational(24623430962648187265, 36893488147419103232), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Mul(Integer(2), Symbol('y')), Rational(15727240259832744812057210812134365969663, 5444517870735015415413993718908291383296)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_37(a:sympy.Rational):
	#(a - z**2 + 6050831182542497717853286941518620410625/5444517870735015415413993718908291383296 < 0) & (36893488147419103232*a**2 - 24623430962648187265*a < 21171758130567760151913340805128333933823/147573952589676412928)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(6050831182542497717853286941518620410625, 5444517870735015415413993718908291383296)), Integer(0)), StrictLessThan(Add(Mul(Integer(36893488147419103232), Pow(Symbol('a'), Integer(2))), Mul(Integer(-1), Integer(24623430962648187265), Symbol('a'))), Rational(21171758130567760151913340805128333933823, 147573952589676412928)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_38(a:sympy.Rational):
	#(a < 813179152525346414339585835102428211193689/348449143727040986586495598010130648530944) & (a > 24623430962648187265/73786976294838206464 - sqrt(288230376151711743)/268435456)

	pre_cond = And(StrictLessThan(Symbol('a'), Rational(813179152525346414339585835102428211193689, 348449143727040986586495598010130648530944)), StrictGreaterThan(Symbol('a'), Add(Rational(24623430962648187265, 73786976294838206464), Mul(Integer(-1), Rational(1, 268435456), Pow(Integer(288230376151711743), Rational(1, 2))))))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_39(a:sympy.Rational):
	#(a + y**2 - z**2 + 606313352372301434184770344590508180225/5444517870735015415413993718908291383296 < 0) & (-a**2 + 24623430962648187265*a/36893488147419103232 - y**2 + 2*y + 15727240259832744812057210812134365969663/5444517870735015415413993718908291383296 > 0)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Pow(Symbol('y'), Integer(2)), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(606313352372301434184770344590508180225, 5444517870735015415413993718908291383296)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('a'), Integer(2))), Mul(Rational(24623430962648187265, 36893488147419103232), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Mul(Integer(2), Symbol('y')), Rational(15727240259832744812057210812134365969663, 5444517870735015415413993718908291383296)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_40(a:sympy.Rational):
	#(a - z**2 + 6050831182542497717853286941518620410625/5444517870735015415413993718908291383296 < 0) & (36893488147419103232*a**2 - 24623430962648187265*a < 21171758130567760151913340805128333933823/147573952589676412928)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(6050831182542497717853286941518620410625, 5444517870735015415413993718908291383296)), Integer(0)), StrictLessThan(Add(Mul(Integer(36893488147419103232), Pow(Symbol('a'), Integer(2))), Mul(Integer(-1), Integer(24623430962648187265), Symbol('a'))), Rational(21171758130567760151913340805128333933823, 147573952589676412928)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_41(a:sympy.Rational):
	#(a < 813179152525346414339585835102428211193689/348449143727040986586495598010130648530944) & (a > 24623430962648187265/73786976294838206464 - sqrt(288230376151711743)/268435456)

	pre_cond = And(StrictLessThan(Symbol('a'), Rational(813179152525346414339585835102428211193689, 348449143727040986586495598010130648530944)), StrictGreaterThan(Symbol('a'), Add(Rational(24623430962648187265, 73786976294838206464), Mul(Integer(-1), Rational(1, 268435456), Pow(Integer(288230376151711743), Rational(1, 2))))))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_42(a:sympy.Rational):
	#(a + y**2 - z**2 + 606313352372301434184770344590508180225/5444517870735015415413993718908291383296 < 0) & (-a**2 + 24623430962648187265*a/36893488147419103232 - y**2 + 2*y + 15727240259832744812057210812134365969663/5444517870735015415413993718908291383296 > 0)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Pow(Symbol('y'), Integer(2)), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(606313352372301434184770344590508180225, 5444517870735015415413993718908291383296)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('a'), Integer(2))), Mul(Rational(24623430962648187265, 36893488147419103232), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Mul(Integer(2), Symbol('y')), Rational(15727240259832744812057210812134365969663, 5444517870735015415413993718908291383296)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_43(a:sympy.Rational):
	#(a - z**2 + 6050831182542497717853286941518620410625/5444517870735015415413993718908291383296 < 0) & (36893488147419103232*a**2 - 24623430962648187265*a < 21171758130567760151913340805128333933823/147573952589676412928)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(6050831182542497717853286941518620410625, 5444517870735015415413993718908291383296)), Integer(0)), StrictLessThan(Add(Mul(Integer(36893488147419103232), Pow(Symbol('a'), Integer(2))), Mul(Integer(-1), Integer(24623430962648187265), Symbol('a'))), Rational(21171758130567760151913340805128333933823, 147573952589676412928)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_44(a:sympy.Rational):
	#(a < 813179152525346414339585835102428211193689/348449143727040986586495598010130648530944) & (a > 24623430962648187265/73786976294838206464 - sqrt(288230376151711743)/268435456)

	pre_cond = And(StrictLessThan(Symbol('a'), Rational(813179152525346414339585835102428211193689, 348449143727040986586495598010130648530944)), StrictGreaterThan(Symbol('a'), Add(Rational(24623430962648187265, 73786976294838206464), Mul(Integer(-1), Rational(1, 268435456), Pow(Integer(288230376151711743), Rational(1, 2))))))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_45(a:sympy.Rational):
	#(a + y**2 - z**2 + 606313352372301434184770344590508180225/5444517870735015415413993718908291383296 < 0) & (-a**2 + 24623430962648187265*a/36893488147419103232 - y**2 + 2*y + 15727240259832744812057210812134365969663/5444517870735015415413993718908291383296 > 0)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Pow(Symbol('y'), Integer(2)), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(606313352372301434184770344590508180225, 5444517870735015415413993718908291383296)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('a'), Integer(2))), Mul(Rational(24623430962648187265, 36893488147419103232), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Mul(Integer(2), Symbol('y')), Rational(15727240259832744812057210812134365969663, 5444517870735015415413993718908291383296)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_46(a:sympy.Rational):
	#(a - z**2 + 6050831182542497717853286941518620410625/5444517870735015415413993718908291383296 < 0) & (36893488147419103232*a**2 - 24623430962648187265*a < 21171758130567760151913340805128333933823/147573952589676412928)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(6050831182542497717853286941518620410625, 5444517870735015415413993718908291383296)), Integer(0)), StrictLessThan(Add(Mul(Integer(36893488147419103232), Pow(Symbol('a'), Integer(2))), Mul(Integer(-1), Integer(24623430962648187265), Symbol('a'))), Rational(21171758130567760151913340805128333933823, 147573952589676412928)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_47(a:sympy.Rational):
	#(a < 813179152525346414339585835102428211193689/348449143727040986586495598010130648530944) & (a > 24623430962648187265/73786976294838206464 - sqrt(288230376151711743)/268435456)

	pre_cond = And(StrictLessThan(Symbol('a'), Rational(813179152525346414339585835102428211193689, 348449143727040986586495598010130648530944)), StrictGreaterThan(Symbol('a'), Add(Rational(24623430962648187265, 73786976294838206464), Mul(Integer(-1), Rational(1, 268435456), Pow(Integer(288230376151711743), Rational(1, 2))))))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_48(a:sympy.Rational):
	#(a + y**2 - z**2 + 606313352372301434184770344590508180225/5444517870735015415413993718908291383296 < 0) & (-a**2 + 24623430962648187265*a/36893488147419103232 - y**2 + 2*y + 15727240259832744812057210812134365969663/5444517870735015415413993718908291383296 > 0)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Pow(Symbol('y'), Integer(2)), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(606313352372301434184770344590508180225, 5444517870735015415413993718908291383296)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('a'), Integer(2))), Mul(Rational(24623430962648187265, 36893488147419103232), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Mul(Integer(2), Symbol('y')), Rational(15727240259832744812057210812134365969663, 5444517870735015415413993718908291383296)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_49(a:sympy.Rational):
	#(a - z**2 + 6050831182542497717853286941518620410625/5444517870735015415413993718908291383296 < 0) & (36893488147419103232*a**2 - 24623430962648187265*a < 21171758130567760151913340805128333933823/147573952589676412928)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(6050831182542497717853286941518620410625, 5444517870735015415413993718908291383296)), Integer(0)), StrictLessThan(Add(Mul(Integer(36893488147419103232), Pow(Symbol('a'), Integer(2))), Mul(Integer(-1), Integer(24623430962648187265), Symbol('a'))), Rational(21171758130567760151913340805128333933823, 147573952589676412928)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_50(a:sympy.Rational):
	#(a < 813179152525346414339585835102428211193689/348449143727040986586495598010130648530944) & (a > 24623430962648187265/73786976294838206464 - sqrt(288230376151711743)/268435456)

	pre_cond = And(StrictLessThan(Symbol('a'), Rational(813179152525346414339585835102428211193689, 348449143727040986586495598010130648530944)), StrictGreaterThan(Symbol('a'), Add(Rational(24623430962648187265, 73786976294838206464), Mul(Integer(-1), Rational(1, 268435456), Pow(Integer(288230376151711743), Rational(1, 2))))))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_51(a:sympy.Rational):
	#(a + y**2 - z**2 + 606313352372301434184770344590508180225/5444517870735015415413993718908291383296 < 0) & (-a**2 + 24623430962648187265*a/36893488147419103232 - y**2 + 2*y + 15727240259832744812057210812134365969663/5444517870735015415413993718908291383296 > 0)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Pow(Symbol('y'), Integer(2)), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(606313352372301434184770344590508180225, 5444517870735015415413993718908291383296)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('a'), Integer(2))), Mul(Rational(24623430962648187265, 36893488147419103232), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Mul(Integer(2), Symbol('y')), Rational(15727240259832744812057210812134365969663, 5444517870735015415413993718908291383296)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_52(a:sympy.Rational):
	#(a - z**2 + 6050831182542497717853286941518620410625/5444517870735015415413993718908291383296 < 0) & (36893488147419103232*a**2 - 24623430962648187265*a < 21171758130567760151913340805128333933823/147573952589676412928)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(6050831182542497717853286941518620410625, 5444517870735015415413993718908291383296)), Integer(0)), StrictLessThan(Add(Mul(Integer(36893488147419103232), Pow(Symbol('a'), Integer(2))), Mul(Integer(-1), Integer(24623430962648187265), Symbol('a'))), Rational(21171758130567760151913340805128333933823, 147573952589676412928)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_53(a:sympy.Rational):
	#(a < 813179152525346414339585835102428211193689/348449143727040986586495598010130648530944) & (a > 24623430962648187265/73786976294838206464 - sqrt(288230376151711743)/268435456)

	pre_cond = And(StrictLessThan(Symbol('a'), Rational(813179152525346414339585835102428211193689, 348449143727040986586495598010130648530944)), StrictGreaterThan(Symbol('a'), Add(Rational(24623430962648187265, 73786976294838206464), Mul(Integer(-1), Rational(1, 268435456), Pow(Integer(288230376151711743), Rational(1, 2))))))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_54(a:sympy.Rational):
	#(a + y**2 - z**2 + 606313352372301434184770344590508180225/5444517870735015415413993718908291383296 < 0) & (-a**2 + 24623430962648187265*a/36893488147419103232 - y**2 + 2*y + 15727240259832744812057210812134365969663/5444517870735015415413993718908291383296 > 0)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Pow(Symbol('y'), Integer(2)), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(606313352372301434184770344590508180225, 5444517870735015415413993718908291383296)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('a'), Integer(2))), Mul(Rational(24623430962648187265, 36893488147419103232), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Mul(Integer(2), Symbol('y')), Rational(15727240259832744812057210812134365969663, 5444517870735015415413993718908291383296)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_55(a:sympy.Rational):
	#(a - z**2 + 6050831182542497717853286941518620410625/5444517870735015415413993718908291383296 < 0) & (36893488147419103232*a**2 - 24623430962648187265*a < 21171758130567760151913340805128333933823/147573952589676412928)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(6050831182542497717853286941518620410625, 5444517870735015415413993718908291383296)), Integer(0)), StrictLessThan(Add(Mul(Integer(36893488147419103232), Pow(Symbol('a'), Integer(2))), Mul(Integer(-1), Integer(24623430962648187265), Symbol('a'))), Rational(21171758130567760151913340805128333933823, 147573952589676412928)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_56(a:sympy.Rational):
	#(a < 813179152525346414339585835102428211193689/348449143727040986586495598010130648530944) & (a > 24623430962648187265/73786976294838206464 - sqrt(288230376151711743)/268435456)

	pre_cond = And(StrictLessThan(Symbol('a'), Rational(813179152525346414339585835102428211193689, 348449143727040986586495598010130648530944)), StrictGreaterThan(Symbol('a'), Add(Rational(24623430962648187265, 73786976294838206464), Mul(Integer(-1), Rational(1, 268435456), Pow(Integer(288230376151711743), Rational(1, 2))))))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_57(a:sympy.Rational):
	#(a + y**2 - z**2 + 606313352372301434184770344590508180225/5444517870735015415413993718908291383296 < 0) & (-a**2 + 24623430962648187265*a/36893488147419103232 - y**2 + 2*y + 15727240259832744812057210812134365969663/5444517870735015415413993718908291383296 > 0)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Pow(Symbol('y'), Integer(2)), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(606313352372301434184770344590508180225, 5444517870735015415413993718908291383296)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('a'), Integer(2))), Mul(Rational(24623430962648187265, 36893488147419103232), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Mul(Integer(2), Symbol('y')), Rational(15727240259832744812057210812134365969663, 5444517870735015415413993718908291383296)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_58(a:sympy.Rational):
	#(a - z**2 + 6050831182542497717853286941518620410625/5444517870735015415413993718908291383296 < 0) & (36893488147419103232*a**2 - 24623430962648187265*a < 21171758130567760151913340805128333933823/147573952589676412928)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(6050831182542497717853286941518620410625, 5444517870735015415413993718908291383296)), Integer(0)), StrictLessThan(Add(Mul(Integer(36893488147419103232), Pow(Symbol('a'), Integer(2))), Mul(Integer(-1), Integer(24623430962648187265), Symbol('a'))), Rational(21171758130567760151913340805128333933823, 147573952589676412928)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_59(a:sympy.Rational):
	#(a < 813179152525346414339585835102428211193689/348449143727040986586495598010130648530944) & (a > 24623430962648187265/73786976294838206464 - sqrt(288230376151711743)/268435456)

	pre_cond = And(StrictLessThan(Symbol('a'), Rational(813179152525346414339585835102428211193689, 348449143727040986586495598010130648530944)), StrictGreaterThan(Symbol('a'), Add(Rational(24623430962648187265, 73786976294838206464), Mul(Integer(-1), Rational(1, 268435456), Pow(Integer(288230376151711743), Rational(1, 2))))))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_60(a:sympy.Rational):
	#(a + y**2 - z**2 + 606313352372301434184770344590508180225/5444517870735015415413993718908291383296 < 0) & (-a**2 + 24623430962648187265*a/36893488147419103232 - y**2 + 2*y + 15727240259832744812057210812134365969663/5444517870735015415413993718908291383296 > 0)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Pow(Symbol('y'), Integer(2)), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(606313352372301434184770344590508180225, 5444517870735015415413993718908291383296)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('a'), Integer(2))), Mul(Rational(24623430962648187265, 36893488147419103232), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Mul(Integer(2), Symbol('y')), Rational(15727240259832744812057210812134365969663, 5444517870735015415413993718908291383296)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_61(a:sympy.Rational):
	#(a - z**2 + 6050831182542497717853286941518620410625/5444517870735015415413993718908291383296 < 0) & (36893488147419103232*a**2 - 24623430962648187265*a < 21171758130567760151913340805128333933823/147573952589676412928)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(6050831182542497717853286941518620410625, 5444517870735015415413993718908291383296)), Integer(0)), StrictLessThan(Add(Mul(Integer(36893488147419103232), Pow(Symbol('a'), Integer(2))), Mul(Integer(-1), Integer(24623430962648187265), Symbol('a'))), Rational(21171758130567760151913340805128333933823, 147573952589676412928)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_62(a:sympy.Rational):
	#(a < 813179152525346414339585835102428211193689/348449143727040986586495598010130648530944) & (a > 24623430962648187265/73786976294838206464 - sqrt(288230376151711743)/268435456)

	pre_cond = And(StrictLessThan(Symbol('a'), Rational(813179152525346414339585835102428211193689, 348449143727040986586495598010130648530944)), StrictGreaterThan(Symbol('a'), Add(Rational(24623430962648187265, 73786976294838206464), Mul(Integer(-1), Rational(1, 268435456), Pow(Integer(288230376151711743), Rational(1, 2))))))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_63(a:sympy.Rational):
	#(a + y**2 - z**2 + 606313352372301434184770344590508180225/5444517870735015415413993718908291383296 < 0) & (-a**2 + 24623430962648187265*a/36893488147419103232 - y**2 + 2*y + 15727240259832744812057210812134365969663/5444517870735015415413993718908291383296 > 0)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Pow(Symbol('y'), Integer(2)), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(606313352372301434184770344590508180225, 5444517870735015415413993718908291383296)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('a'), Integer(2))), Mul(Rational(24623430962648187265, 36893488147419103232), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Mul(Integer(2), Symbol('y')), Rational(15727240259832744812057210812134365969663, 5444517870735015415413993718908291383296)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_64(a:sympy.Rational):
	#(a - z**2 + 6050831182542497717853286941518620410625/5444517870735015415413993718908291383296 < 0) & (36893488147419103232*a**2 - 24623430962648187265*a < 21171758130567760151913340805128333933823/147573952589676412928)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(6050831182542497717853286941518620410625, 5444517870735015415413993718908291383296)), Integer(0)), StrictLessThan(Add(Mul(Integer(36893488147419103232), Pow(Symbol('a'), Integer(2))), Mul(Integer(-1), Integer(24623430962648187265), Symbol('a'))), Rational(21171758130567760151913340805128333933823, 147573952589676412928)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_65(a:sympy.Rational):
	#(a < 813179152525346414339585835102428211193689/348449143727040986586495598010130648530944) & (a > 24623430962648187265/73786976294838206464 - sqrt(288230376151711743)/268435456)

	pre_cond = And(StrictLessThan(Symbol('a'), Rational(813179152525346414339585835102428211193689, 348449143727040986586495598010130648530944)), StrictGreaterThan(Symbol('a'), Add(Rational(24623430962648187265, 73786976294838206464), Mul(Integer(-1), Rational(1, 268435456), Pow(Integer(288230376151711743), Rational(1, 2))))))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_66(a:sympy.Rational):
	#(a + y**2 - z**2 + 606313352372301434184770344590508180225/5444517870735015415413993718908291383296 < 0) & (-a**2 + 24623430962648187265*a/36893488147419103232 - y**2 + 2*y + 15727240259832744812057210812134365969663/5444517870735015415413993718908291383296 > 0)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Pow(Symbol('y'), Integer(2)), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(606313352372301434184770344590508180225, 5444517870735015415413993718908291383296)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('a'), Integer(2))), Mul(Rational(24623430962648187265, 36893488147419103232), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Mul(Integer(2), Symbol('y')), Rational(15727240259832744812057210812134365969663, 5444517870735015415413993718908291383296)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_67(a:sympy.Rational):
	#(a - z**2 + 6050831182542497717853286941518620410625/5444517870735015415413993718908291383296 < 0) & (36893488147419103232*a**2 - 24623430962648187265*a < 21171758130567760151913340805128333933823/147573952589676412928)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(6050831182542497717853286941518620410625, 5444517870735015415413993718908291383296)), Integer(0)), StrictLessThan(Add(Mul(Integer(36893488147419103232), Pow(Symbol('a'), Integer(2))), Mul(Integer(-1), Integer(24623430962648187265), Symbol('a'))), Rational(21171758130567760151913340805128333933823, 147573952589676412928)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_68(a:sympy.Rational):
	#(a < 813179152525346414339585835102428211193689/348449143727040986586495598010130648530944) & (a > 24623430962648187265/73786976294838206464 - sqrt(288230376151711743)/268435456)

	pre_cond = And(StrictLessThan(Symbol('a'), Rational(813179152525346414339585835102428211193689, 348449143727040986586495598010130648530944)), StrictGreaterThan(Symbol('a'), Add(Rational(24623430962648187265, 73786976294838206464), Mul(Integer(-1), Rational(1, 268435456), Pow(Integer(288230376151711743), Rational(1, 2))))))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_69(a:sympy.Rational):
	#(a + y**2 - z**2 + 606313352372301434184770344590508180225/5444517870735015415413993718908291383296 < 0) & (-a**2 + 24623430962648187265*a/36893488147419103232 - y**2 + 2*y + 15727240259832744812057210812134365969663/5444517870735015415413993718908291383296 > 0)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Pow(Symbol('y'), Integer(2)), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(606313352372301434184770344590508180225, 5444517870735015415413993718908291383296)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('a'), Integer(2))), Mul(Rational(24623430962648187265, 36893488147419103232), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Mul(Integer(2), Symbol('y')), Rational(15727240259832744812057210812134365969663, 5444517870735015415413993718908291383296)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_70(a:sympy.Rational):
	#(a - z**2 + 6050831182542497717853286941518620410625/5444517870735015415413993718908291383296 < 0) & (36893488147419103232*a**2 - 24623430962648187265*a < 21171758130567760151913340805128333933823/147573952589676412928)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(6050831182542497717853286941518620410625, 5444517870735015415413993718908291383296)), Integer(0)), StrictLessThan(Add(Mul(Integer(36893488147419103232), Pow(Symbol('a'), Integer(2))), Mul(Integer(-1), Integer(24623430962648187265), Symbol('a'))), Rational(21171758130567760151913340805128333933823, 147573952589676412928)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_71(a:sympy.Rational):
	#(a < 813179152525346414339585835102428211193689/348449143727040986586495598010130648530944) & (a > 24623430962648187265/73786976294838206464 - sqrt(288230376151711743)/268435456)

	pre_cond = And(StrictLessThan(Symbol('a'), Rational(813179152525346414339585835102428211193689, 348449143727040986586495598010130648530944)), StrictGreaterThan(Symbol('a'), Add(Rational(24623430962648187265, 73786976294838206464), Mul(Integer(-1), Rational(1, 268435456), Pow(Integer(288230376151711743), Rational(1, 2))))))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_72(a:sympy.Rational):
	#(a + y**2 - z**2 + 606313352372301434184770344590508180225/5444517870735015415413993718908291383296 < 0) & (-a**2 + 24623430962648187265*a/36893488147419103232 - y**2 + 2*y + 15727240259832744812057210812134365969663/5444517870735015415413993718908291383296 > 0)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Pow(Symbol('y'), Integer(2)), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(606313352372301434184770344590508180225, 5444517870735015415413993718908291383296)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('a'), Integer(2))), Mul(Rational(24623430962648187265, 36893488147419103232), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Mul(Integer(2), Symbol('y')), Rational(15727240259832744812057210812134365969663, 5444517870735015415413993718908291383296)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_73(a:sympy.Rational):
	#(a - z**2 + 6050831182542497717853286941518620410625/5444517870735015415413993718908291383296 < 0) & (36893488147419103232*a**2 - 24623430962648187265*a < 21171758130567760151913340805128333933823/147573952589676412928)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(6050831182542497717853286941518620410625, 5444517870735015415413993718908291383296)), Integer(0)), StrictLessThan(Add(Mul(Integer(36893488147419103232), Pow(Symbol('a'), Integer(2))), Mul(Integer(-1), Integer(24623430962648187265), Symbol('a'))), Rational(21171758130567760151913340805128333933823, 147573952589676412928)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_74(a:sympy.Rational):
	#(a < 813179152525346414339585835102428211193689/348449143727040986586495598010130648530944) & (a > 24623430962648187265/73786976294838206464 - sqrt(288230376151711743)/268435456)

	pre_cond = And(StrictLessThan(Symbol('a'), Rational(813179152525346414339585835102428211193689, 348449143727040986586495598010130648530944)), StrictGreaterThan(Symbol('a'), Add(Rational(24623430962648187265, 73786976294838206464), Mul(Integer(-1), Rational(1, 268435456), Pow(Integer(288230376151711743), Rational(1, 2))))))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_75(a:sympy.Rational):
	#(a + y**2 - z**2 + 606313352372301434184770344590508180225/5444517870735015415413993718908291383296 < 0) & (-a**2 + 24623430962648187265*a/36893488147419103232 - y**2 + 2*y + 15727240259832744812057210812134365969663/5444517870735015415413993718908291383296 > 0)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Pow(Symbol('y'), Integer(2)), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(606313352372301434184770344590508180225, 5444517870735015415413993718908291383296)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('a'), Integer(2))), Mul(Rational(24623430962648187265, 36893488147419103232), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Mul(Integer(2), Symbol('y')), Rational(15727240259832744812057210812134365969663, 5444517870735015415413993718908291383296)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_76(a:sympy.Rational):
	#(a - z**2 + 6050831182542497717853286941518620410625/5444517870735015415413993718908291383296 < 0) & (36893488147419103232*a**2 - 24623430962648187265*a < 21171758130567760151913340805128333933823/147573952589676412928)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(6050831182542497717853286941518620410625, 5444517870735015415413993718908291383296)), Integer(0)), StrictLessThan(Add(Mul(Integer(36893488147419103232), Pow(Symbol('a'), Integer(2))), Mul(Integer(-1), Integer(24623430962648187265), Symbol('a'))), Rational(21171758130567760151913340805128333933823, 147573952589676412928)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_77(a:sympy.Rational):
	#(a < 813179152525346414339585835102428211193689/348449143727040986586495598010130648530944) & (a > 24623430962648187265/73786976294838206464 - sqrt(288230376151711743)/268435456)

	pre_cond = And(StrictLessThan(Symbol('a'), Rational(813179152525346414339585835102428211193689, 348449143727040986586495598010130648530944)), StrictGreaterThan(Symbol('a'), Add(Rational(24623430962648187265, 73786976294838206464), Mul(Integer(-1), Rational(1, 268435456), Pow(Integer(288230376151711743), Rational(1, 2))))))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_78(a:sympy.Rational):
	#(a + y**2 - z**2 + 606313352372301434184770344590508180225/5444517870735015415413993718908291383296 < 0) & (-a**2 + 24623430962648187265*a/36893488147419103232 - y**2 + 2*y + 15727240259832744812057210812134365969663/5444517870735015415413993718908291383296 > 0)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Pow(Symbol('y'), Integer(2)), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(606313352372301434184770344590508180225, 5444517870735015415413993718908291383296)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('a'), Integer(2))), Mul(Rational(24623430962648187265, 36893488147419103232), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Mul(Integer(2), Symbol('y')), Rational(15727240259832744812057210812134365969663, 5444517870735015415413993718908291383296)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_79(a:sympy.Rational):
	#(a - z**2 + 6050831182542497717853286941518620410625/5444517870735015415413993718908291383296 < 0) & (36893488147419103232*a**2 - 24623430962648187265*a < 21171758130567760151913340805128333933823/147573952589676412928)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(6050831182542497717853286941518620410625, 5444517870735015415413993718908291383296)), Integer(0)), StrictLessThan(Add(Mul(Integer(36893488147419103232), Pow(Symbol('a'), Integer(2))), Mul(Integer(-1), Integer(24623430962648187265), Symbol('a'))), Rational(21171758130567760151913340805128333933823, 147573952589676412928)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_80(a:sympy.Rational):
	#(a < 813179152525346414339585835102428211193689/348449143727040986586495598010130648530944) & (a > 24623430962648187265/73786976294838206464 - sqrt(288230376151711743)/268435456)

	pre_cond = And(StrictLessThan(Symbol('a'), Rational(813179152525346414339585835102428211193689, 348449143727040986586495598010130648530944)), StrictGreaterThan(Symbol('a'), Add(Rational(24623430962648187265, 73786976294838206464), Mul(Integer(-1), Rational(1, 268435456), Pow(Integer(288230376151711743), Rational(1, 2))))))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_81(a:sympy.Rational):
	#(a + y**2 - z**2 + 606313352372301434184770344590508180225/5444517870735015415413993718908291383296 < 0) & (-a**2 + 24623430962648187265*a/36893488147419103232 - y**2 + 2*y + 15727240259832744812057210812134365969663/5444517870735015415413993718908291383296 > 0)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Pow(Symbol('y'), Integer(2)), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(606313352372301434184770344590508180225, 5444517870735015415413993718908291383296)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('a'), Integer(2))), Mul(Rational(24623430962648187265, 36893488147419103232), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Mul(Integer(2), Symbol('y')), Rational(15727240259832744812057210812134365969663, 5444517870735015415413993718908291383296)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_82(a:sympy.Rational):
	#(a - z**2 + 6050831182542497717853286941518620410625/5444517870735015415413993718908291383296 < 0) & (36893488147419103232*a**2 - 24623430962648187265*a < 21171758130567760151913340805128333933823/147573952589676412928)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(6050831182542497717853286941518620410625, 5444517870735015415413993718908291383296)), Integer(0)), StrictLessThan(Add(Mul(Integer(36893488147419103232), Pow(Symbol('a'), Integer(2))), Mul(Integer(-1), Integer(24623430962648187265), Symbol('a'))), Rational(21171758130567760151913340805128333933823, 147573952589676412928)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_83(a:sympy.Rational):
	#(a < 813179152525346414339585835102428211193689/348449143727040986586495598010130648530944) & (a > 24623430962648187265/73786976294838206464 - sqrt(288230376151711743)/268435456)

	pre_cond = And(StrictLessThan(Symbol('a'), Rational(813179152525346414339585835102428211193689, 348449143727040986586495598010130648530944)), StrictGreaterThan(Symbol('a'), Add(Rational(24623430962648187265, 73786976294838206464), Mul(Integer(-1), Rational(1, 268435456), Pow(Integer(288230376151711743), Rational(1, 2))))))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_84(a:sympy.Rational):
	#(a + y**2 - z**2 + 606313352372301434184770344590508180225/5444517870735015415413993718908291383296 < 0) & (-a**2 + 24623430962648187265*a/36893488147419103232 - y**2 + 2*y + 15727240259832744812057210812134365969663/5444517870735015415413993718908291383296 > 0)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Pow(Symbol('y'), Integer(2)), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(606313352372301434184770344590508180225, 5444517870735015415413993718908291383296)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('a'), Integer(2))), Mul(Rational(24623430962648187265, 36893488147419103232), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Mul(Integer(2), Symbol('y')), Rational(15727240259832744812057210812134365969663, 5444517870735015415413993718908291383296)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_85(a:sympy.Rational):
	#(a - z**2 + 6050831182542497717853286941518620410625/5444517870735015415413993718908291383296 < 0) & (36893488147419103232*a**2 - 24623430962648187265*a < 21171758130567760151913340805128333933823/147573952589676412928)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(6050831182542497717853286941518620410625, 5444517870735015415413993718908291383296)), Integer(0)), StrictLessThan(Add(Mul(Integer(36893488147419103232), Pow(Symbol('a'), Integer(2))), Mul(Integer(-1), Integer(24623430962648187265), Symbol('a'))), Rational(21171758130567760151913340805128333933823, 147573952589676412928)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_86(a:sympy.Rational):
	#(a < 813179152525346414339585835102428211193689/348449143727040986586495598010130648530944) & (a > 24623430962648187265/73786976294838206464 - sqrt(288230376151711743)/268435456)

	pre_cond = And(StrictLessThan(Symbol('a'), Rational(813179152525346414339585835102428211193689, 348449143727040986586495598010130648530944)), StrictGreaterThan(Symbol('a'), Add(Rational(24623430962648187265, 73786976294838206464), Mul(Integer(-1), Rational(1, 268435456), Pow(Integer(288230376151711743), Rational(1, 2))))))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_87(a:sympy.Rational):
	#(a + y**2 - z**2 + 606313352372301434184770344590508180225/5444517870735015415413993718908291383296 < 0) & (-a**2 + 24623430962648187265*a/36893488147419103232 - y**2 + 2*y + 15727240259832744812057210812134365969663/5444517870735015415413993718908291383296 > 0)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Pow(Symbol('y'), Integer(2)), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(606313352372301434184770344590508180225, 5444517870735015415413993718908291383296)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('a'), Integer(2))), Mul(Rational(24623430962648187265, 36893488147419103232), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Mul(Integer(2), Symbol('y')), Rational(15727240259832744812057210812134365969663, 5444517870735015415413993718908291383296)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_88(a:sympy.Rational):
	#(a - z**2 + 6050831182542497717853286941518620410625/5444517870735015415413993718908291383296 < 0) & (36893488147419103232*a**2 - 24623430962648187265*a < 21171758130567760151913340805128333933823/147573952589676412928)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(6050831182542497717853286941518620410625, 5444517870735015415413993718908291383296)), Integer(0)), StrictLessThan(Add(Mul(Integer(36893488147419103232), Pow(Symbol('a'), Integer(2))), Mul(Integer(-1), Integer(24623430962648187265), Symbol('a'))), Rational(21171758130567760151913340805128333933823, 147573952589676412928)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_89(a:sympy.Rational):
	#(a < 813179152525346414339585835102428211193689/348449143727040986586495598010130648530944) & (a > 24623430962648187265/73786976294838206464 - sqrt(288230376151711743)/268435456)

	pre_cond = And(StrictLessThan(Symbol('a'), Rational(813179152525346414339585835102428211193689, 348449143727040986586495598010130648530944)), StrictGreaterThan(Symbol('a'), Add(Rational(24623430962648187265, 73786976294838206464), Mul(Integer(-1), Rational(1, 268435456), Pow(Integer(288230376151711743), Rational(1, 2))))))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_90(a:sympy.Rational):
	#(a + y**2 - z**2 + 606313352372301434184770344590508180225/5444517870735015415413993718908291383296 < 0) & (-a**2 + 24623430962648187265*a/36893488147419103232 - y**2 + 2*y + 15727240259832744812057210812134365969663/5444517870735015415413993718908291383296 > 0)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Pow(Symbol('y'), Integer(2)), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(606313352372301434184770344590508180225, 5444517870735015415413993718908291383296)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('a'), Integer(2))), Mul(Rational(24623430962648187265, 36893488147419103232), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Mul(Integer(2), Symbol('y')), Rational(15727240259832744812057210812134365969663, 5444517870735015415413993718908291383296)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_91(a:sympy.Rational):
	#(a - z**2 + 6050831182542497717853286941518620410625/5444517870735015415413993718908291383296 < 0) & (36893488147419103232*a**2 - 24623430962648187265*a < 21171758130567760151913340805128333933823/147573952589676412928)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(6050831182542497717853286941518620410625, 5444517870735015415413993718908291383296)), Integer(0)), StrictLessThan(Add(Mul(Integer(36893488147419103232), Pow(Symbol('a'), Integer(2))), Mul(Integer(-1), Integer(24623430962648187265), Symbol('a'))), Rational(21171758130567760151913340805128333933823, 147573952589676412928)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_92(a:sympy.Rational):
	#(a < 813179152525346414339585835102428211193689/348449143727040986586495598010130648530944) & (a > 24623430962648187265/73786976294838206464 - sqrt(288230376151711743)/268435456)

	pre_cond = And(StrictLessThan(Symbol('a'), Rational(813179152525346414339585835102428211193689, 348449143727040986586495598010130648530944)), StrictGreaterThan(Symbol('a'), Add(Rational(24623430962648187265, 73786976294838206464), Mul(Integer(-1), Rational(1, 268435456), Pow(Integer(288230376151711743), Rational(1, 2))))))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_93(a:sympy.Rational):
	#(a + y**2 - z**2 + 606313352372301434184770344590508180225/5444517870735015415413993718908291383296 < 0) & (-a**2 + 24623430962648187265*a/36893488147419103232 - y**2 + 2*y + 15727240259832744812057210812134365969663/5444517870735015415413993718908291383296 > 0)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Pow(Symbol('y'), Integer(2)), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(606313352372301434184770344590508180225, 5444517870735015415413993718908291383296)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('a'), Integer(2))), Mul(Rational(24623430962648187265, 36893488147419103232), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Mul(Integer(2), Symbol('y')), Rational(15727240259832744812057210812134365969663, 5444517870735015415413993718908291383296)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_94(a:sympy.Rational):
	#(a - z**2 + 6050831182542497717853286941518620410625/5444517870735015415413993718908291383296 < 0) & (36893488147419103232*a**2 - 24623430962648187265*a < 21171758130567760151913340805128333933823/147573952589676412928)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(6050831182542497717853286941518620410625, 5444517870735015415413993718908291383296)), Integer(0)), StrictLessThan(Add(Mul(Integer(36893488147419103232), Pow(Symbol('a'), Integer(2))), Mul(Integer(-1), Integer(24623430962648187265), Symbol('a'))), Rational(21171758130567760151913340805128333933823, 147573952589676412928)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_95(a:sympy.Rational):
	#(a < 813179152525346414339585835102428211193689/348449143727040986586495598010130648530944) & (a > 24623430962648187265/73786976294838206464 - sqrt(288230376151711743)/268435456)

	pre_cond = And(StrictLessThan(Symbol('a'), Rational(813179152525346414339585835102428211193689, 348449143727040986586495598010130648530944)), StrictGreaterThan(Symbol('a'), Add(Rational(24623430962648187265, 73786976294838206464), Mul(Integer(-1), Rational(1, 268435456), Pow(Integer(288230376151711743), Rational(1, 2))))))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_96(a:sympy.Rational):
	#(a + y**2 - z**2 + 606313352372301434184770344590508180225/5444517870735015415413993718908291383296 < 0) & (-a**2 + 24623430962648187265*a/36893488147419103232 - y**2 + 2*y + 15727240259832744812057210812134365969663/5444517870735015415413993718908291383296 > 0)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Pow(Symbol('y'), Integer(2)), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(606313352372301434184770344590508180225, 5444517870735015415413993718908291383296)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('a'), Integer(2))), Mul(Rational(24623430962648187265, 36893488147419103232), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Mul(Integer(2), Symbol('y')), Rational(15727240259832744812057210812134365969663, 5444517870735015415413993718908291383296)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_97(a:sympy.Rational):
	#(a - z**2 + 6050831182542497717853286941518620410625/5444517870735015415413993718908291383296 < 0) & (36893488147419103232*a**2 - 24623430962648187265*a < 21171758130567760151913340805128333933823/147573952589676412928)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(6050831182542497717853286941518620410625, 5444517870735015415413993718908291383296)), Integer(0)), StrictLessThan(Add(Mul(Integer(36893488147419103232), Pow(Symbol('a'), Integer(2))), Mul(Integer(-1), Integer(24623430962648187265), Symbol('a'))), Rational(21171758130567760151913340805128333933823, 147573952589676412928)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_98(a:sympy.Rational):
	#(a < 813179152525346414339585835102428211193689/348449143727040986586495598010130648530944) & (a > 24623430962648187265/73786976294838206464 - sqrt(288230376151711743)/268435456)

	pre_cond = And(StrictLessThan(Symbol('a'), Rational(813179152525346414339585835102428211193689, 348449143727040986586495598010130648530944)), StrictGreaterThan(Symbol('a'), Add(Rational(24623430962648187265, 73786976294838206464), Mul(Integer(-1), Rational(1, 268435456), Pow(Integer(288230376151711743), Rational(1, 2))))))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_99(a:sympy.Rational):
	#(a + y**2 - z**2 + 606313352372301434184770344590508180225/5444517870735015415413993718908291383296 < 0) & (-a**2 + 24623430962648187265*a/36893488147419103232 - y**2 + 2*y + 15727240259832744812057210812134365969663/5444517870735015415413993718908291383296 > 0)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Pow(Symbol('y'), Integer(2)), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(606313352372301434184770344590508180225, 5444517870735015415413993718908291383296)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('a'), Integer(2))), Mul(Rational(24623430962648187265, 36893488147419103232), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Mul(Integer(2), Symbol('y')), Rational(15727240259832744812057210812134365969663, 5444517870735015415413993718908291383296)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_100(a:sympy.Rational):
	#(a - z**2 + 6050831182542497717853286941518620410625/5444517870735015415413993718908291383296 < 0) & (36893488147419103232*a**2 - 24623430962648187265*a < 21171758130567760151913340805128333933823/147573952589676412928)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(6050831182542497717853286941518620410625, 5444517870735015415413993718908291383296)), Integer(0)), StrictLessThan(Add(Mul(Integer(36893488147419103232), Pow(Symbol('a'), Integer(2))), Mul(Integer(-1), Integer(24623430962648187265), Symbol('a'))), Rational(21171758130567760151913340805128333933823, 147573952589676412928)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_101(a:sympy.Rational):
	#(a < 813179152525346414339585835102428211193689/348449143727040986586495598010130648530944) & (a > 24623430962648187265/73786976294838206464 - sqrt(288230376151711743)/268435456)

	pre_cond = And(StrictLessThan(Symbol('a'), Rational(813179152525346414339585835102428211193689, 348449143727040986586495598010130648530944)), StrictGreaterThan(Symbol('a'), Add(Rational(24623430962648187265, 73786976294838206464), Mul(Integer(-1), Rational(1, 268435456), Pow(Integer(288230376151711743), Rational(1, 2))))))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_102(a:sympy.Rational):
	#(a + y**2 - z**2 + 606313352372301434184770344590508180225/5444517870735015415413993718908291383296 < 0) & (-a**2 + 24623430962648187265*a/36893488147419103232 - y**2 + 2*y + 15727240259832744812057210812134365969663/5444517870735015415413993718908291383296 > 0)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Pow(Symbol('y'), Integer(2)), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(606313352372301434184770344590508180225, 5444517870735015415413993718908291383296)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('a'), Integer(2))), Mul(Rational(24623430962648187265, 36893488147419103232), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Mul(Integer(2), Symbol('y')), Rational(15727240259832744812057210812134365969663, 5444517870735015415413993718908291383296)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_103(a:sympy.Rational):
	#(a - z**2 + 6050831182542497717853286941518620410625/5444517870735015415413993718908291383296 < 0) & (36893488147419103232*a**2 - 24623430962648187265*a < 21171758130567760151913340805128333933823/147573952589676412928)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(6050831182542497717853286941518620410625, 5444517870735015415413993718908291383296)), Integer(0)), StrictLessThan(Add(Mul(Integer(36893488147419103232), Pow(Symbol('a'), Integer(2))), Mul(Integer(-1), Integer(24623430962648187265), Symbol('a'))), Rational(21171758130567760151913340805128333933823, 147573952589676412928)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_104(a:sympy.Rational):
	#(a < 813179152525346414339585835102428211193689/348449143727040986586495598010130648530944) & (a > 24623430962648187265/73786976294838206464 - sqrt(288230376151711743)/268435456)

	pre_cond = And(StrictLessThan(Symbol('a'), Rational(813179152525346414339585835102428211193689, 348449143727040986586495598010130648530944)), StrictGreaterThan(Symbol('a'), Add(Rational(24623430962648187265, 73786976294838206464), Mul(Integer(-1), Rational(1, 268435456), Pow(Integer(288230376151711743), Rational(1, 2))))))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_105(a:sympy.Rational):
	#(a + y**2 - z**2 + 606313352372301434184770344590508180225/5444517870735015415413993718908291383296 < 0) & (-a**2 + 24623430962648187265*a/36893488147419103232 - y**2 + 2*y + 15727240259832744812057210812134365969663/5444517870735015415413993718908291383296 > 0)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Pow(Symbol('y'), Integer(2)), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(606313352372301434184770344590508180225, 5444517870735015415413993718908291383296)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('a'), Integer(2))), Mul(Rational(24623430962648187265, 36893488147419103232), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Mul(Integer(2), Symbol('y')), Rational(15727240259832744812057210812134365969663, 5444517870735015415413993718908291383296)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_106(a:sympy.Rational):
	#(a - z**2 + 6050831182542497717853286941518620410625/5444517870735015415413993718908291383296 < 0) & (36893488147419103232*a**2 - 24623430962648187265*a < 21171758130567760151913340805128333933823/147573952589676412928)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(6050831182542497717853286941518620410625, 5444517870735015415413993718908291383296)), Integer(0)), StrictLessThan(Add(Mul(Integer(36893488147419103232), Pow(Symbol('a'), Integer(2))), Mul(Integer(-1), Integer(24623430962648187265), Symbol('a'))), Rational(21171758130567760151913340805128333933823, 147573952589676412928)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_107(a:sympy.Rational):
	#(a < 813179152525346414339585835102428211193689/348449143727040986586495598010130648530944) & (a > 24623430962648187265/73786976294838206464 - sqrt(288230376151711743)/268435456)

	pre_cond = And(StrictLessThan(Symbol('a'), Rational(813179152525346414339585835102428211193689, 348449143727040986586495598010130648530944)), StrictGreaterThan(Symbol('a'), Add(Rational(24623430962648187265, 73786976294838206464), Mul(Integer(-1), Rational(1, 268435456), Pow(Integer(288230376151711743), Rational(1, 2))))))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_108(a:sympy.Rational):
	#(a + y**2 - z**2 + 606313352372301434184770344590508180225/5444517870735015415413993718908291383296 < 0) & (-a**2 + 24623430962648187265*a/36893488147419103232 - y**2 + 2*y + 15727240259832744812057210812134365969663/5444517870735015415413993718908291383296 > 0)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Pow(Symbol('y'), Integer(2)), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(606313352372301434184770344590508180225, 5444517870735015415413993718908291383296)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('a'), Integer(2))), Mul(Rational(24623430962648187265, 36893488147419103232), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Mul(Integer(2), Symbol('y')), Rational(15727240259832744812057210812134365969663, 5444517870735015415413993718908291383296)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_109(a:sympy.Rational):
	#(a - z**2 + 6050831182542497717853286941518620410625/5444517870735015415413993718908291383296 < 0) & (36893488147419103232*a**2 - 24623430962648187265*a < 21171758130567760151913340805128333933823/147573952589676412928)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(6050831182542497717853286941518620410625, 5444517870735015415413993718908291383296)), Integer(0)), StrictLessThan(Add(Mul(Integer(36893488147419103232), Pow(Symbol('a'), Integer(2))), Mul(Integer(-1), Integer(24623430962648187265), Symbol('a'))), Rational(21171758130567760151913340805128333933823, 147573952589676412928)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_110(a:sympy.Rational):
	#(a < 813179152525346414339585835102428211193689/348449143727040986586495598010130648530944) & (a > 24623430962648187265/73786976294838206464 - sqrt(288230376151711743)/268435456)

	pre_cond = And(StrictLessThan(Symbol('a'), Rational(813179152525346414339585835102428211193689, 348449143727040986586495598010130648530944)), StrictGreaterThan(Symbol('a'), Add(Rational(24623430962648187265, 73786976294838206464), Mul(Integer(-1), Rational(1, 268435456), Pow(Integer(288230376151711743), Rational(1, 2))))))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_111(a:sympy.Rational):
	#(a + y**2 - z**2 + 606313352372301434184770344590508180225/5444517870735015415413993718908291383296 < 0) & (-a**2 + 24623430962648187265*a/36893488147419103232 - y**2 + 2*y + 15727240259832744812057210812134365969663/5444517870735015415413993718908291383296 > 0)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Pow(Symbol('y'), Integer(2)), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(606313352372301434184770344590508180225, 5444517870735015415413993718908291383296)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('a'), Integer(2))), Mul(Rational(24623430962648187265, 36893488147419103232), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Mul(Integer(2), Symbol('y')), Rational(15727240259832744812057210812134365969663, 5444517870735015415413993718908291383296)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_112(a:sympy.Rational):
	#(a - z**2 + 6050831182542497717853286941518620410625/5444517870735015415413993718908291383296 < 0) & (36893488147419103232*a**2 - 24623430962648187265*a < 21171758130567760151913340805128333933823/147573952589676412928)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(6050831182542497717853286941518620410625, 5444517870735015415413993718908291383296)), Integer(0)), StrictLessThan(Add(Mul(Integer(36893488147419103232), Pow(Symbol('a'), Integer(2))), Mul(Integer(-1), Integer(24623430962648187265), Symbol('a'))), Rational(21171758130567760151913340805128333933823, 147573952589676412928)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_113(a:sympy.Rational):
	#(a < 813179152525346414339585835102428211193689/348449143727040986586495598010130648530944) & (a > 24623430962648187265/73786976294838206464 - sqrt(288230376151711743)/268435456)

	pre_cond = And(StrictLessThan(Symbol('a'), Rational(813179152525346414339585835102428211193689, 348449143727040986586495598010130648530944)), StrictGreaterThan(Symbol('a'), Add(Rational(24623430962648187265, 73786976294838206464), Mul(Integer(-1), Rational(1, 268435456), Pow(Integer(288230376151711743), Rational(1, 2))))))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_114(a:sympy.Rational):
	#(a + y**2 - z**2 + 606313352372301434184770344590508180225/5444517870735015415413993718908291383296 < 0) & (-a**2 + 24623430962648187265*a/36893488147419103232 - y**2 + 2*y + 15727240259832744812057210812134365969663/5444517870735015415413993718908291383296 > 0)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Pow(Symbol('y'), Integer(2)), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(606313352372301434184770344590508180225, 5444517870735015415413993718908291383296)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('a'), Integer(2))), Mul(Rational(24623430962648187265, 36893488147419103232), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Mul(Integer(2), Symbol('y')), Rational(15727240259832744812057210812134365969663, 5444517870735015415413993718908291383296)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_115(a:sympy.Rational):
	#(a - z**2 + 6050831182542497717853286941518620410625/5444517870735015415413993718908291383296 < 0) & (36893488147419103232*a**2 - 24623430962648187265*a < 21171758130567760151913340805128333933823/147573952589676412928)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(6050831182542497717853286941518620410625, 5444517870735015415413993718908291383296)), Integer(0)), StrictLessThan(Add(Mul(Integer(36893488147419103232), Pow(Symbol('a'), Integer(2))), Mul(Integer(-1), Integer(24623430962648187265), Symbol('a'))), Rational(21171758130567760151913340805128333933823, 147573952589676412928)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_116(a:sympy.Rational):
	#(a < 813179152525346414339585835102428211193689/348449143727040986586495598010130648530944) & (a > 24623430962648187265/73786976294838206464 - sqrt(288230376151711743)/268435456)

	pre_cond = And(StrictLessThan(Symbol('a'), Rational(813179152525346414339585835102428211193689, 348449143727040986586495598010130648530944)), StrictGreaterThan(Symbol('a'), Add(Rational(24623430962648187265, 73786976294838206464), Mul(Integer(-1), Rational(1, 268435456), Pow(Integer(288230376151711743), Rational(1, 2))))))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_117(a:sympy.Rational):
	#(a + y**2 - z**2 + 606313352372301434184770344590508180225/5444517870735015415413993718908291383296 < 0) & (-a**2 + 24623430962648187265*a/36893488147419103232 - y**2 + 2*y + 15727240259832744812057210812134365969663/5444517870735015415413993718908291383296 > 0)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Pow(Symbol('y'), Integer(2)), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(606313352372301434184770344590508180225, 5444517870735015415413993718908291383296)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('a'), Integer(2))), Mul(Rational(24623430962648187265, 36893488147419103232), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Mul(Integer(2), Symbol('y')), Rational(15727240259832744812057210812134365969663, 5444517870735015415413993718908291383296)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_118(a:sympy.Rational):
	#(a - z**2 + 6050831182542497717853286941518620410625/5444517870735015415413993718908291383296 < 0) & (36893488147419103232*a**2 - 24623430962648187265*a < 21171758130567760151913340805128333933823/147573952589676412928)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(6050831182542497717853286941518620410625, 5444517870735015415413993718908291383296)), Integer(0)), StrictLessThan(Add(Mul(Integer(36893488147419103232), Pow(Symbol('a'), Integer(2))), Mul(Integer(-1), Integer(24623430962648187265), Symbol('a'))), Rational(21171758130567760151913340805128333933823, 147573952589676412928)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_119(a:sympy.Rational):
	#(a < 813179152525346414339585835102428211193689/348449143727040986586495598010130648530944) & (a > 24623430962648187265/73786976294838206464 - sqrt(288230376151711743)/268435456)

	pre_cond = And(StrictLessThan(Symbol('a'), Rational(813179152525346414339585835102428211193689, 348449143727040986586495598010130648530944)), StrictGreaterThan(Symbol('a'), Add(Rational(24623430962648187265, 73786976294838206464), Mul(Integer(-1), Rational(1, 268435456), Pow(Integer(288230376151711743), Rational(1, 2))))))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_120(a:sympy.Rational):
	#(a + y**2 - z**2 + 606313352372301434184770344590508180225/5444517870735015415413993718908291383296 < 0) & (-a**2 + 24623430962648187265*a/36893488147419103232 - y**2 + 2*y + 15727240259832744812057210812134365969663/5444517870735015415413993718908291383296 > 0)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Pow(Symbol('y'), Integer(2)), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(606313352372301434184770344590508180225, 5444517870735015415413993718908291383296)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('a'), Integer(2))), Mul(Rational(24623430962648187265, 36893488147419103232), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Mul(Integer(2), Symbol('y')), Rational(15727240259832744812057210812134365969663, 5444517870735015415413993718908291383296)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_121(a:sympy.Rational):
	#(a - z**2 + 6050831182542497717853286941518620410625/5444517870735015415413993718908291383296 < 0) & (36893488147419103232*a**2 - 24623430962648187265*a < 21171758130567760151913340805128333933823/147573952589676412928)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(6050831182542497717853286941518620410625, 5444517870735015415413993718908291383296)), Integer(0)), StrictLessThan(Add(Mul(Integer(36893488147419103232), Pow(Symbol('a'), Integer(2))), Mul(Integer(-1), Integer(24623430962648187265), Symbol('a'))), Rational(21171758130567760151913340805128333933823, 147573952589676412928)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_122(a:sympy.Rational):
	#(a < 813179152525346414339585835102428211193689/348449143727040986586495598010130648530944) & (a > 24623430962648187265/73786976294838206464 - sqrt(288230376151711743)/268435456)

	pre_cond = And(StrictLessThan(Symbol('a'), Rational(813179152525346414339585835102428211193689, 348449143727040986586495598010130648530944)), StrictGreaterThan(Symbol('a'), Add(Rational(24623430962648187265, 73786976294838206464), Mul(Integer(-1), Rational(1, 268435456), Pow(Integer(288230376151711743), Rational(1, 2))))))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_123(a:sympy.Rational):
	#(a + y**2 - z**2 + 606313352372301434184770344590508180225/5444517870735015415413993718908291383296 < 0) & (-a**2 + 24623430962648187265*a/36893488147419103232 - y**2 + 2*y + 15727240259832744812057210812134365969663/5444517870735015415413993718908291383296 > 0)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Pow(Symbol('y'), Integer(2)), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(606313352372301434184770344590508180225, 5444517870735015415413993718908291383296)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('a'), Integer(2))), Mul(Rational(24623430962648187265, 36893488147419103232), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Mul(Integer(2), Symbol('y')), Rational(15727240259832744812057210812134365969663, 5444517870735015415413993718908291383296)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_124(a:sympy.Rational):
	#(a - z**2 + 6050831182542497717853286941518620410625/5444517870735015415413993718908291383296 < 0) & (36893488147419103232*a**2 - 24623430962648187265*a < 21171758130567760151913340805128333933823/147573952589676412928)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(6050831182542497717853286941518620410625, 5444517870735015415413993718908291383296)), Integer(0)), StrictLessThan(Add(Mul(Integer(36893488147419103232), Pow(Symbol('a'), Integer(2))), Mul(Integer(-1), Integer(24623430962648187265), Symbol('a'))), Rational(21171758130567760151913340805128333933823, 147573952589676412928)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_125(a:sympy.Rational):
	#(a < 813179152525346414339585835102428211193689/348449143727040986586495598010130648530944) & (a > 24623430962648187265/73786976294838206464 - sqrt(288230376151711743)/268435456)

	pre_cond = And(StrictLessThan(Symbol('a'), Rational(813179152525346414339585835102428211193689, 348449143727040986586495598010130648530944)), StrictGreaterThan(Symbol('a'), Add(Rational(24623430962648187265, 73786976294838206464), Mul(Integer(-1), Rational(1, 268435456), Pow(Integer(288230376151711743), Rational(1, 2))))))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_126(a:sympy.Rational):
	#(a + y**2 - z**2 + 606313352372301434184770344590508180225/5444517870735015415413993718908291383296 < 0) & (-a**2 + 24623430962648187265*a/36893488147419103232 - y**2 + 2*y + 15727240259832744812057210812134365969663/5444517870735015415413993718908291383296 > 0)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Pow(Symbol('y'), Integer(2)), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(606313352372301434184770344590508180225, 5444517870735015415413993718908291383296)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('a'), Integer(2))), Mul(Rational(24623430962648187265, 36893488147419103232), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Mul(Integer(2), Symbol('y')), Rational(15727240259832744812057210812134365969663, 5444517870735015415413993718908291383296)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_127(a:sympy.Rational):
	#(a - z**2 + 6050831182542497717853286941518620410625/5444517870735015415413993718908291383296 < 0) & (36893488147419103232*a**2 - 24623430962648187265*a < 21171758130567760151913340805128333933823/147573952589676412928)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(6050831182542497717853286941518620410625, 5444517870735015415413993718908291383296)), Integer(0)), StrictLessThan(Add(Mul(Integer(36893488147419103232), Pow(Symbol('a'), Integer(2))), Mul(Integer(-1), Integer(24623430962648187265), Symbol('a'))), Rational(21171758130567760151913340805128333933823, 147573952589676412928)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_128(a:sympy.Rational):
	#(a < 813179152525346414339585835102428211193689/348449143727040986586495598010130648530944) & (a > 24623430962648187265/73786976294838206464 - sqrt(288230376151711743)/268435456)

	pre_cond = And(StrictLessThan(Symbol('a'), Rational(813179152525346414339585835102428211193689, 348449143727040986586495598010130648530944)), StrictGreaterThan(Symbol('a'), Add(Rational(24623430962648187265, 73786976294838206464), Mul(Integer(-1), Rational(1, 268435456), Pow(Integer(288230376151711743), Rational(1, 2))))))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_129(a:sympy.Rational):
	#(a + y**2 - z**2 + 606313352372301434184770344590508180225/5444517870735015415413993718908291383296 < 0) & (-a**2 + 24623430962648187265*a/36893488147419103232 - y**2 + 2*y + 15727240259832744812057210812134365969663/5444517870735015415413993718908291383296 > 0)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Pow(Symbol('y'), Integer(2)), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(606313352372301434184770344590508180225, 5444517870735015415413993718908291383296)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('a'), Integer(2))), Mul(Rational(24623430962648187265, 36893488147419103232), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Mul(Integer(2), Symbol('y')), Rational(15727240259832744812057210812134365969663, 5444517870735015415413993718908291383296)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_130(a:sympy.Rational):
	#(a - z**2 + 6050831182542497717853286941518620410625/5444517870735015415413993718908291383296 < 0) & (36893488147419103232*a**2 - 24623430962648187265*a < 21171758130567760151913340805128333933823/147573952589676412928)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(6050831182542497717853286941518620410625, 5444517870735015415413993718908291383296)), Integer(0)), StrictLessThan(Add(Mul(Integer(36893488147419103232), Pow(Symbol('a'), Integer(2))), Mul(Integer(-1), Integer(24623430962648187265), Symbol('a'))), Rational(21171758130567760151913340805128333933823, 147573952589676412928)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_131(a:sympy.Rational):
	#(a < 813179152525346414339585835102428211193689/348449143727040986586495598010130648530944) & (a > 24623430962648187265/73786976294838206464 - sqrt(288230376151711743)/268435456)

	pre_cond = And(StrictLessThan(Symbol('a'), Rational(813179152525346414339585835102428211193689, 348449143727040986586495598010130648530944)), StrictGreaterThan(Symbol('a'), Add(Rational(24623430962648187265, 73786976294838206464), Mul(Integer(-1), Rational(1, 268435456), Pow(Integer(288230376151711743), Rational(1, 2))))))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_132(a:sympy.Rational):
	#(a + y**2 - z**2 + 606313352372301434184770344590508180225/5444517870735015415413993718908291383296 < 0) & (-a**2 + 24623430962648187265*a/36893488147419103232 - y**2 + 2*y + 15727240259832744812057210812134365969663/5444517870735015415413993718908291383296 > 0)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Pow(Symbol('y'), Integer(2)), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(606313352372301434184770344590508180225, 5444517870735015415413993718908291383296)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('a'), Integer(2))), Mul(Rational(24623430962648187265, 36893488147419103232), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Mul(Integer(2), Symbol('y')), Rational(15727240259832744812057210812134365969663, 5444517870735015415413993718908291383296)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_133(a:sympy.Rational):
	#(a - z**2 + 6050831182542497717853286941518620410625/5444517870735015415413993718908291383296 < 0) & (36893488147419103232*a**2 - 24623430962648187265*a < 21171758130567760151913340805128333933823/147573952589676412928)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(6050831182542497717853286941518620410625, 5444517870735015415413993718908291383296)), Integer(0)), StrictLessThan(Add(Mul(Integer(36893488147419103232), Pow(Symbol('a'), Integer(2))), Mul(Integer(-1), Integer(24623430962648187265), Symbol('a'))), Rational(21171758130567760151913340805128333933823, 147573952589676412928)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_134(a:sympy.Rational):
	#(a < 813179152525346414339585835102428211193689/348449143727040986586495598010130648530944) & (a > 24623430962648187265/73786976294838206464 - sqrt(288230376151711743)/268435456)

	pre_cond = And(StrictLessThan(Symbol('a'), Rational(813179152525346414339585835102428211193689, 348449143727040986586495598010130648530944)), StrictGreaterThan(Symbol('a'), Add(Rational(24623430962648187265, 73786976294838206464), Mul(Integer(-1), Rational(1, 268435456), Pow(Integer(288230376151711743), Rational(1, 2))))))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_135(a:sympy.Rational):
	#(a + y**2 - z**2 + 606313352372301434184770344590508180225/5444517870735015415413993718908291383296 < 0) & (-a**2 + 24623430962648187265*a/36893488147419103232 - y**2 + 2*y + 15727240259832744812057210812134365969663/5444517870735015415413993718908291383296 > 0)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Pow(Symbol('y'), Integer(2)), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(606313352372301434184770344590508180225, 5444517870735015415413993718908291383296)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('a'), Integer(2))), Mul(Rational(24623430962648187265, 36893488147419103232), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Mul(Integer(2), Symbol('y')), Rational(15727240259832744812057210812134365969663, 5444517870735015415413993718908291383296)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_136(a:sympy.Rational):
	#(a - z**2 + 6050831182542497717853286941518620410625/5444517870735015415413993718908291383296 < 0) & (36893488147419103232*a**2 - 24623430962648187265*a < 21171758130567760151913340805128333933823/147573952589676412928)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(6050831182542497717853286941518620410625, 5444517870735015415413993718908291383296)), Integer(0)), StrictLessThan(Add(Mul(Integer(36893488147419103232), Pow(Symbol('a'), Integer(2))), Mul(Integer(-1), Integer(24623430962648187265), Symbol('a'))), Rational(21171758130567760151913340805128333933823, 147573952589676412928)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_137(a:sympy.Rational):
	#(a < 813179152525346414339585835102428211193689/348449143727040986586495598010130648530944) & (a > 24623430962648187265/73786976294838206464 - sqrt(288230376151711743)/268435456)

	pre_cond = And(StrictLessThan(Symbol('a'), Rational(813179152525346414339585835102428211193689, 348449143727040986586495598010130648530944)), StrictGreaterThan(Symbol('a'), Add(Rational(24623430962648187265, 73786976294838206464), Mul(Integer(-1), Rational(1, 268435456), Pow(Integer(288230376151711743), Rational(1, 2))))))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_138(a:sympy.Rational):
	#(a + y**2 - z**2 + 606313352372301434184770344590508180225/5444517870735015415413993718908291383296 < 0) & (-a**2 + 24623430962648187265*a/36893488147419103232 - y**2 + 2*y + 15727240259832744812057210812134365969663/5444517870735015415413993718908291383296 > 0)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Pow(Symbol('y'), Integer(2)), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(606313352372301434184770344590508180225, 5444517870735015415413993718908291383296)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('a'), Integer(2))), Mul(Rational(24623430962648187265, 36893488147419103232), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Mul(Integer(2), Symbol('y')), Rational(15727240259832744812057210812134365969663, 5444517870735015415413993718908291383296)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_139(a:sympy.Rational):
	#(a - z**2 + 6050831182542497717853286941518620410625/5444517870735015415413993718908291383296 < 0) & (36893488147419103232*a**2 - 24623430962648187265*a < 21171758130567760151913340805128333933823/147573952589676412928)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(6050831182542497717853286941518620410625, 5444517870735015415413993718908291383296)), Integer(0)), StrictLessThan(Add(Mul(Integer(36893488147419103232), Pow(Symbol('a'), Integer(2))), Mul(Integer(-1), Integer(24623430962648187265), Symbol('a'))), Rational(21171758130567760151913340805128333933823, 147573952589676412928)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_140(a:sympy.Rational):
	#(a < 813179152525346414339585835102428211193689/348449143727040986586495598010130648530944) & (a > 24623430962648187265/73786976294838206464 - sqrt(288230376151711743)/268435456)

	pre_cond = And(StrictLessThan(Symbol('a'), Rational(813179152525346414339585835102428211193689, 348449143727040986586495598010130648530944)), StrictGreaterThan(Symbol('a'), Add(Rational(24623430962648187265, 73786976294838206464), Mul(Integer(-1), Rational(1, 268435456), Pow(Integer(288230376151711743), Rational(1, 2))))))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_141(a:sympy.Rational):
	#(a + y**2 - z**2 + 606313352372301434184770344590508180225/5444517870735015415413993718908291383296 < 0) & (-a**2 + 24623430962648187265*a/36893488147419103232 - y**2 + 2*y + 15727240259832744812057210812134365969663/5444517870735015415413993718908291383296 > 0)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Pow(Symbol('y'), Integer(2)), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(606313352372301434184770344590508180225, 5444517870735015415413993718908291383296)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('a'), Integer(2))), Mul(Rational(24623430962648187265, 36893488147419103232), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Mul(Integer(2), Symbol('y')), Rational(15727240259832744812057210812134365969663, 5444517870735015415413993718908291383296)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_142(a:sympy.Rational):
	#(a - z**2 + 6050831182542497717853286941518620410625/5444517870735015415413993718908291383296 < 0) & (36893488147419103232*a**2 - 24623430962648187265*a < 21171758130567760151913340805128333933823/147573952589676412928)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(6050831182542497717853286941518620410625, 5444517870735015415413993718908291383296)), Integer(0)), StrictLessThan(Add(Mul(Integer(36893488147419103232), Pow(Symbol('a'), Integer(2))), Mul(Integer(-1), Integer(24623430962648187265), Symbol('a'))), Rational(21171758130567760151913340805128333933823, 147573952589676412928)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_143(a:sympy.Rational):
	#(a < 813179152525346414339585835102428211193689/348449143727040986586495598010130648530944) & (a > 24623430962648187265/73786976294838206464 - sqrt(288230376151711743)/268435456)

	pre_cond = And(StrictLessThan(Symbol('a'), Rational(813179152525346414339585835102428211193689, 348449143727040986586495598010130648530944)), StrictGreaterThan(Symbol('a'), Add(Rational(24623430962648187265, 73786976294838206464), Mul(Integer(-1), Rational(1, 268435456), Pow(Integer(288230376151711743), Rational(1, 2))))))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_144(a:sympy.Rational):
	#(a + y**2 - z**2 + 606313352372301434184770344590508180225/5444517870735015415413993718908291383296 < 0) & (-a**2 + 24623430962648187265*a/36893488147419103232 - y**2 + 2*y + 15727240259832744812057210812134365969663/5444517870735015415413993718908291383296 > 0)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Pow(Symbol('y'), Integer(2)), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(606313352372301434184770344590508180225, 5444517870735015415413993718908291383296)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('a'), Integer(2))), Mul(Rational(24623430962648187265, 36893488147419103232), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Mul(Integer(2), Symbol('y')), Rational(15727240259832744812057210812134365969663, 5444517870735015415413993718908291383296)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_145(a:sympy.Rational):
	#(a - z**2 + 6050831182542497717853286941518620410625/5444517870735015415413993718908291383296 < 0) & (36893488147419103232*a**2 - 24623430962648187265*a < 21171758130567760151913340805128333933823/147573952589676412928)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(6050831182542497717853286941518620410625, 5444517870735015415413993718908291383296)), Integer(0)), StrictLessThan(Add(Mul(Integer(36893488147419103232), Pow(Symbol('a'), Integer(2))), Mul(Integer(-1), Integer(24623430962648187265), Symbol('a'))), Rational(21171758130567760151913340805128333933823, 147573952589676412928)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_146(a:sympy.Rational):
	#(a < 813179152525346414339585835102428211193689/348449143727040986586495598010130648530944) & (a > 24623430962648187265/73786976294838206464 - sqrt(288230376151711743)/268435456)

	pre_cond = And(StrictLessThan(Symbol('a'), Rational(813179152525346414339585835102428211193689, 348449143727040986586495598010130648530944)), StrictGreaterThan(Symbol('a'), Add(Rational(24623430962648187265, 73786976294838206464), Mul(Integer(-1), Rational(1, 268435456), Pow(Integer(288230376151711743), Rational(1, 2))))))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_147(a:sympy.Rational):
	#(a + y**2 - z**2 + 606313352372301434184770344590508180225/5444517870735015415413993718908291383296 < 0) & (-a**2 + 24623430962648187265*a/36893488147419103232 - y**2 + 2*y + 15727240259832744812057210812134365969663/5444517870735015415413993718908291383296 > 0)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Pow(Symbol('y'), Integer(2)), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(606313352372301434184770344590508180225, 5444517870735015415413993718908291383296)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('a'), Integer(2))), Mul(Rational(24623430962648187265, 36893488147419103232), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Mul(Integer(2), Symbol('y')), Rational(15727240259832744812057210812134365969663, 5444517870735015415413993718908291383296)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_148(a:sympy.Rational):
	#(a - z**2 + 6050831182542497717853286941518620410625/5444517870735015415413993718908291383296 < 0) & (36893488147419103232*a**2 - 24623430962648187265*a < 21171758130567760151913340805128333933823/147573952589676412928)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(6050831182542497717853286941518620410625, 5444517870735015415413993718908291383296)), Integer(0)), StrictLessThan(Add(Mul(Integer(36893488147419103232), Pow(Symbol('a'), Integer(2))), Mul(Integer(-1), Integer(24623430962648187265), Symbol('a'))), Rational(21171758130567760151913340805128333933823, 147573952589676412928)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_149(a:sympy.Rational):
	#(a < 813179152525346414339585835102428211193689/348449143727040986586495598010130648530944) & (a > 24623430962648187265/73786976294838206464 - sqrt(288230376151711743)/268435456)

	pre_cond = And(StrictLessThan(Symbol('a'), Rational(813179152525346414339585835102428211193689, 348449143727040986586495598010130648530944)), StrictGreaterThan(Symbol('a'), Add(Rational(24623430962648187265, 73786976294838206464), Mul(Integer(-1), Rational(1, 268435456), Pow(Integer(288230376151711743), Rational(1, 2))))))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_150(a:sympy.Rational):
	#(a + y**2 - z**2 + 606313352372301434184770344590508180225/5444517870735015415413993718908291383296 < 0) & (-a**2 + 24623430962648187265*a/36893488147419103232 - y**2 + 2*y + 15727240259832744812057210812134365969663/5444517870735015415413993718908291383296 > 0)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Pow(Symbol('y'), Integer(2)), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(606313352372301434184770344590508180225, 5444517870735015415413993718908291383296)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('a'), Integer(2))), Mul(Rational(24623430962648187265, 36893488147419103232), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Mul(Integer(2), Symbol('y')), Rational(15727240259832744812057210812134365969663, 5444517870735015415413993718908291383296)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_151(a:sympy.Rational):
	#(a - z**2 + 6050831182542497717853286941518620410625/5444517870735015415413993718908291383296 < 0) & (36893488147419103232*a**2 - 24623430962648187265*a < 21171758130567760151913340805128333933823/147573952589676412928)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(6050831182542497717853286941518620410625, 5444517870735015415413993718908291383296)), Integer(0)), StrictLessThan(Add(Mul(Integer(36893488147419103232), Pow(Symbol('a'), Integer(2))), Mul(Integer(-1), Integer(24623430962648187265), Symbol('a'))), Rational(21171758130567760151913340805128333933823, 147573952589676412928)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_152(a:sympy.Rational):
	#(a < 813179152525346414339585835102428211193689/348449143727040986586495598010130648530944) & (a > 24623430962648187265/73786976294838206464 - sqrt(288230376151711743)/268435456)

	pre_cond = And(StrictLessThan(Symbol('a'), Rational(813179152525346414339585835102428211193689, 348449143727040986586495598010130648530944)), StrictGreaterThan(Symbol('a'), Add(Rational(24623430962648187265, 73786976294838206464), Mul(Integer(-1), Rational(1, 268435456), Pow(Integer(288230376151711743), Rational(1, 2))))))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_153(a:sympy.Rational):
	#(a + y**2 - z**2 + 606313352372301434184770344590508180225/5444517870735015415413993718908291383296 < 0) & (-a**2 + 24623430962648187265*a/36893488147419103232 - y**2 + 2*y + 15727240259832744812057210812134365969663/5444517870735015415413993718908291383296 > 0)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Pow(Symbol('y'), Integer(2)), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(606313352372301434184770344590508180225, 5444517870735015415413993718908291383296)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('a'), Integer(2))), Mul(Rational(24623430962648187265, 36893488147419103232), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Mul(Integer(2), Symbol('y')), Rational(15727240259832744812057210812134365969663, 5444517870735015415413993718908291383296)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_154(a:sympy.Rational):
	#(a - z**2 + 6050831182542497717853286941518620410625/5444517870735015415413993718908291383296 < 0) & (36893488147419103232*a**2 - 24623430962648187265*a < 21171758130567760151913340805128333933823/147573952589676412928)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(6050831182542497717853286941518620410625, 5444517870735015415413993718908291383296)), Integer(0)), StrictLessThan(Add(Mul(Integer(36893488147419103232), Pow(Symbol('a'), Integer(2))), Mul(Integer(-1), Integer(24623430962648187265), Symbol('a'))), Rational(21171758130567760151913340805128333933823, 147573952589676412928)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_155(a:sympy.Rational):
	#(a < 813179152525346414339585835102428211193689/348449143727040986586495598010130648530944) & (a > 24623430962648187265/73786976294838206464 - sqrt(288230376151711743)/268435456)

	pre_cond = And(StrictLessThan(Symbol('a'), Rational(813179152525346414339585835102428211193689, 348449143727040986586495598010130648530944)), StrictGreaterThan(Symbol('a'), Add(Rational(24623430962648187265, 73786976294838206464), Mul(Integer(-1), Rational(1, 268435456), Pow(Integer(288230376151711743), Rational(1, 2))))))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_156(a:sympy.Rational):
	#(a + y**2 - z**2 + 606313352372301434184770344590508180225/5444517870735015415413993718908291383296 < 0) & (-a**2 + 24623430962648187265*a/36893488147419103232 - y**2 + 2*y + 15727240259832744812057210812134365969663/5444517870735015415413993718908291383296 > 0)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Pow(Symbol('y'), Integer(2)), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(606313352372301434184770344590508180225, 5444517870735015415413993718908291383296)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('a'), Integer(2))), Mul(Rational(24623430962648187265, 36893488147419103232), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Mul(Integer(2), Symbol('y')), Rational(15727240259832744812057210812134365969663, 5444517870735015415413993718908291383296)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_157(a:sympy.Rational):
	#(a - z**2 + 6050831182542497717853286941518620410625/5444517870735015415413993718908291383296 < 0) & (36893488147419103232*a**2 - 24623430962648187265*a < 21171758130567760151913340805128333933823/147573952589676412928)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(6050831182542497717853286941518620410625, 5444517870735015415413993718908291383296)), Integer(0)), StrictLessThan(Add(Mul(Integer(36893488147419103232), Pow(Symbol('a'), Integer(2))), Mul(Integer(-1), Integer(24623430962648187265), Symbol('a'))), Rational(21171758130567760151913340805128333933823, 147573952589676412928)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_158(a:sympy.Rational):
	#(a < 813179152525346414339585835102428211193689/348449143727040986586495598010130648530944) & (a > 24623430962648187265/73786976294838206464 - sqrt(288230376151711743)/268435456)

	pre_cond = And(StrictLessThan(Symbol('a'), Rational(813179152525346414339585835102428211193689, 348449143727040986586495598010130648530944)), StrictGreaterThan(Symbol('a'), Add(Rational(24623430962648187265, 73786976294838206464), Mul(Integer(-1), Rational(1, 268435456), Pow(Integer(288230376151711743), Rational(1, 2))))))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_159(a:sympy.Rational):
	#(a + y**2 - z**2 + 606313352372301434184770344590508180225/5444517870735015415413993718908291383296 < 0) & (-a**2 + 24623430962648187265*a/36893488147419103232 - y**2 + 2*y + 15727240259832744812057210812134365969663/5444517870735015415413993718908291383296 > 0)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Pow(Symbol('y'), Integer(2)), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(606313352372301434184770344590508180225, 5444517870735015415413993718908291383296)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('a'), Integer(2))), Mul(Rational(24623430962648187265, 36893488147419103232), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Mul(Integer(2), Symbol('y')), Rational(15727240259832744812057210812134365969663, 5444517870735015415413993718908291383296)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_160(a:sympy.Rational):
	#(a - z**2 + 6050831182542497717853286941518620410625/5444517870735015415413993718908291383296 < 0) & (36893488147419103232*a**2 - 24623430962648187265*a < 21171758130567760151913340805128333933823/147573952589676412928)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(6050831182542497717853286941518620410625, 5444517870735015415413993718908291383296)), Integer(0)), StrictLessThan(Add(Mul(Integer(36893488147419103232), Pow(Symbol('a'), Integer(2))), Mul(Integer(-1), Integer(24623430962648187265), Symbol('a'))), Rational(21171758130567760151913340805128333933823, 147573952589676412928)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_161(a:sympy.Rational):
	#(a < 813179152525346414339585835102428211193689/348449143727040986586495598010130648530944) & (a > 24623430962648187265/73786976294838206464 - sqrt(288230376151711743)/268435456)

	pre_cond = And(StrictLessThan(Symbol('a'), Rational(813179152525346414339585835102428211193689, 348449143727040986586495598010130648530944)), StrictGreaterThan(Symbol('a'), Add(Rational(24623430962648187265, 73786976294838206464), Mul(Integer(-1), Rational(1, 268435456), Pow(Integer(288230376151711743), Rational(1, 2))))))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_162(a:sympy.Rational):
	#(a + y**2 - z**2 + 606313352372301434184770344590508180225/5444517870735015415413993718908291383296 < 0) & (-a**2 + 24623430962648187265*a/36893488147419103232 - y**2 + 2*y + 15727240259832744812057210812134365969663/5444517870735015415413993718908291383296 > 0)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Pow(Symbol('y'), Integer(2)), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(606313352372301434184770344590508180225, 5444517870735015415413993718908291383296)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('a'), Integer(2))), Mul(Rational(24623430962648187265, 36893488147419103232), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Mul(Integer(2), Symbol('y')), Rational(15727240259832744812057210812134365969663, 5444517870735015415413993718908291383296)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_163(a:sympy.Rational):
	#(a - z**2 + 6050831182542497717853286941518620410625/5444517870735015415413993718908291383296 < 0) & (36893488147419103232*a**2 - 24623430962648187265*a < 21171758130567760151913340805128333933823/147573952589676412928)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(6050831182542497717853286941518620410625, 5444517870735015415413993718908291383296)), Integer(0)), StrictLessThan(Add(Mul(Integer(36893488147419103232), Pow(Symbol('a'), Integer(2))), Mul(Integer(-1), Integer(24623430962648187265), Symbol('a'))), Rational(21171758130567760151913340805128333933823, 147573952589676412928)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_164(a:sympy.Rational):
	#(a < 813179152525346414339585835102428211193689/348449143727040986586495598010130648530944) & (a > 24623430962648187265/73786976294838206464 - sqrt(288230376151711743)/268435456)

	pre_cond = And(StrictLessThan(Symbol('a'), Rational(813179152525346414339585835102428211193689, 348449143727040986586495598010130648530944)), StrictGreaterThan(Symbol('a'), Add(Rational(24623430962648187265, 73786976294838206464), Mul(Integer(-1), Rational(1, 268435456), Pow(Integer(288230376151711743), Rational(1, 2))))))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_165(a:sympy.Rational):
	#(a + y**2 - z**2 + 606313352372301434184770344590508180225/5444517870735015415413993718908291383296 < 0) & (-a**2 + 24623430962648187265*a/36893488147419103232 - y**2 + 2*y + 15727240259832744812057210812134365969663/5444517870735015415413993718908291383296 > 0)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Pow(Symbol('y'), Integer(2)), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(606313352372301434184770344590508180225, 5444517870735015415413993718908291383296)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('a'), Integer(2))), Mul(Rational(24623430962648187265, 36893488147419103232), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Mul(Integer(2), Symbol('y')), Rational(15727240259832744812057210812134365969663, 5444517870735015415413993718908291383296)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_166(a:sympy.Rational):
	#(a - z**2 + 6050831182542497717853286941518620410625/5444517870735015415413993718908291383296 < 0) & (36893488147419103232*a**2 - 24623430962648187265*a < 21171758130567760151913340805128333933823/147573952589676412928)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(6050831182542497717853286941518620410625, 5444517870735015415413993718908291383296)), Integer(0)), StrictLessThan(Add(Mul(Integer(36893488147419103232), Pow(Symbol('a'), Integer(2))), Mul(Integer(-1), Integer(24623430962648187265), Symbol('a'))), Rational(21171758130567760151913340805128333933823, 147573952589676412928)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_167(a:sympy.Rational):
	#(a < 813179152525346414339585835102428211193689/348449143727040986586495598010130648530944) & (a > 24623430962648187265/73786976294838206464 - sqrt(288230376151711743)/268435456)

	pre_cond = And(StrictLessThan(Symbol('a'), Rational(813179152525346414339585835102428211193689, 348449143727040986586495598010130648530944)), StrictGreaterThan(Symbol('a'), Add(Rational(24623430962648187265, 73786976294838206464), Mul(Integer(-1), Rational(1, 268435456), Pow(Integer(288230376151711743), Rational(1, 2))))))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_168(a:sympy.Rational):
	#(a + y**2 - z**2 + 606313352372301434184770344590508180225/5444517870735015415413993718908291383296 < 0) & (-a**2 + 24623430962648187265*a/36893488147419103232 - y**2 + 2*y + 15727240259832744812057210812134365969663/5444517870735015415413993718908291383296 > 0)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Pow(Symbol('y'), Integer(2)), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(606313352372301434184770344590508180225, 5444517870735015415413993718908291383296)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('a'), Integer(2))), Mul(Rational(24623430962648187265, 36893488147419103232), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Mul(Integer(2), Symbol('y')), Rational(15727240259832744812057210812134365969663, 5444517870735015415413993718908291383296)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_169(a:sympy.Rational):
	#(a - z**2 + 6050831182542497717853286941518620410625/5444517870735015415413993718908291383296 < 0) & (36893488147419103232*a**2 - 24623430962648187265*a < 21171758130567760151913340805128333933823/147573952589676412928)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(6050831182542497717853286941518620410625, 5444517870735015415413993718908291383296)), Integer(0)), StrictLessThan(Add(Mul(Integer(36893488147419103232), Pow(Symbol('a'), Integer(2))), Mul(Integer(-1), Integer(24623430962648187265), Symbol('a'))), Rational(21171758130567760151913340805128333933823, 147573952589676412928)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_170(a:sympy.Rational):
	#(a < 813179152525346414339585835102428211193689/348449143727040986586495598010130648530944) & (a > 24623430962648187265/73786976294838206464 - sqrt(288230376151711743)/268435456)

	pre_cond = And(StrictLessThan(Symbol('a'), Rational(813179152525346414339585835102428211193689, 348449143727040986586495598010130648530944)), StrictGreaterThan(Symbol('a'), Add(Rational(24623430962648187265, 73786976294838206464), Mul(Integer(-1), Rational(1, 268435456), Pow(Integer(288230376151711743), Rational(1, 2))))))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_171(a:sympy.Rational):
	#(a + y**2 - z**2 + 606313352372301434184770344590508180225/5444517870735015415413993718908291383296 < 0) & (-a**2 + 24623430962648187265*a/36893488147419103232 - y**2 + 2*y + 15727240259832744812057210812134365969663/5444517870735015415413993718908291383296 > 0)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Pow(Symbol('y'), Integer(2)), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(606313352372301434184770344590508180225, 5444517870735015415413993718908291383296)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('a'), Integer(2))), Mul(Rational(24623430962648187265, 36893488147419103232), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Mul(Integer(2), Symbol('y')), Rational(15727240259832744812057210812134365969663, 5444517870735015415413993718908291383296)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_172(a:sympy.Rational):
	#(a - z**2 + 6050831182542497717853286941518620410625/5444517870735015415413993718908291383296 < 0) & (36893488147419103232*a**2 - 24623430962648187265*a < 21171758130567760151913340805128333933823/147573952589676412928)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(6050831182542497717853286941518620410625, 5444517870735015415413993718908291383296)), Integer(0)), StrictLessThan(Add(Mul(Integer(36893488147419103232), Pow(Symbol('a'), Integer(2))), Mul(Integer(-1), Integer(24623430962648187265), Symbol('a'))), Rational(21171758130567760151913340805128333933823, 147573952589676412928)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_173(a:sympy.Rational):
	#(a < 813179152525346414339585835102428211193689/348449143727040986586495598010130648530944) & (a > 24623430962648187265/73786976294838206464 - sqrt(288230376151711743)/268435456)

	pre_cond = And(StrictLessThan(Symbol('a'), Rational(813179152525346414339585835102428211193689, 348449143727040986586495598010130648530944)), StrictGreaterThan(Symbol('a'), Add(Rational(24623430962648187265, 73786976294838206464), Mul(Integer(-1), Rational(1, 268435456), Pow(Integer(288230376151711743), Rational(1, 2))))))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_174(a:sympy.Rational):
	#(a + y**2 - z**2 + 606313352372301434184770344590508180225/5444517870735015415413993718908291383296 < 0) & (-a**2 + 24623430962648187265*a/36893488147419103232 - y**2 + 2*y + 15727240259832744812057210812134365969663/5444517870735015415413993718908291383296 > 0)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Pow(Symbol('y'), Integer(2)), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(606313352372301434184770344590508180225, 5444517870735015415413993718908291383296)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('a'), Integer(2))), Mul(Rational(24623430962648187265, 36893488147419103232), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Mul(Integer(2), Symbol('y')), Rational(15727240259832744812057210812134365969663, 5444517870735015415413993718908291383296)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_175(a:sympy.Rational):
	#(a - z**2 + 6050831182542497717853286941518620410625/5444517870735015415413993718908291383296 < 0) & (36893488147419103232*a**2 - 24623430962648187265*a < 21171758130567760151913340805128333933823/147573952589676412928)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(6050831182542497717853286941518620410625, 5444517870735015415413993718908291383296)), Integer(0)), StrictLessThan(Add(Mul(Integer(36893488147419103232), Pow(Symbol('a'), Integer(2))), Mul(Integer(-1), Integer(24623430962648187265), Symbol('a'))), Rational(21171758130567760151913340805128333933823, 147573952589676412928)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_176(a:sympy.Rational):
	#(a < 813179152525346414339585835102428211193689/348449143727040986586495598010130648530944) & (a > 24623430962648187265/73786976294838206464 - sqrt(288230376151711743)/268435456)

	pre_cond = And(StrictLessThan(Symbol('a'), Rational(813179152525346414339585835102428211193689, 348449143727040986586495598010130648530944)), StrictGreaterThan(Symbol('a'), Add(Rational(24623430962648187265, 73786976294838206464), Mul(Integer(-1), Rational(1, 268435456), Pow(Integer(288230376151711743), Rational(1, 2))))))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_177(a:sympy.Rational):
	#(a + y**2 - z**2 + 606313352372301434184770344590508180225/5444517870735015415413993718908291383296 < 0) & (-a**2 + 24623430962648187265*a/36893488147419103232 - y**2 + 2*y + 15727240259832744812057210812134365969663/5444517870735015415413993718908291383296 > 0)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Pow(Symbol('y'), Integer(2)), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(606313352372301434184770344590508180225, 5444517870735015415413993718908291383296)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('a'), Integer(2))), Mul(Rational(24623430962648187265, 36893488147419103232), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Mul(Integer(2), Symbol('y')), Rational(15727240259832744812057210812134365969663, 5444517870735015415413993718908291383296)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_178(a:sympy.Rational):
	#(a - z**2 + 6050831182542497717853286941518620410625/5444517870735015415413993718908291383296 < 0) & (36893488147419103232*a**2 - 24623430962648187265*a < 21171758130567760151913340805128333933823/147573952589676412928)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(6050831182542497717853286941518620410625, 5444517870735015415413993718908291383296)), Integer(0)), StrictLessThan(Add(Mul(Integer(36893488147419103232), Pow(Symbol('a'), Integer(2))), Mul(Integer(-1), Integer(24623430962648187265), Symbol('a'))), Rational(21171758130567760151913340805128333933823, 147573952589676412928)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_179(a:sympy.Rational):
	#(a < 813179152525346414339585835102428211193689/348449143727040986586495598010130648530944) & (a > 24623430962648187265/73786976294838206464 - sqrt(288230376151711743)/268435456)

	pre_cond = And(StrictLessThan(Symbol('a'), Rational(813179152525346414339585835102428211193689, 348449143727040986586495598010130648530944)), StrictGreaterThan(Symbol('a'), Add(Rational(24623430962648187265, 73786976294838206464), Mul(Integer(-1), Rational(1, 268435456), Pow(Integer(288230376151711743), Rational(1, 2))))))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_180(a:sympy.Rational):
	#(a + y**2 - z**2 + 606313352372301434184770344590508180225/5444517870735015415413993718908291383296 < 0) & (-a**2 + 24623430962648187265*a/36893488147419103232 - y**2 + 2*y + 15727240259832744812057210812134365969663/5444517870735015415413993718908291383296 > 0)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Pow(Symbol('y'), Integer(2)), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(606313352372301434184770344590508180225, 5444517870735015415413993718908291383296)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('a'), Integer(2))), Mul(Rational(24623430962648187265, 36893488147419103232), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Mul(Integer(2), Symbol('y')), Rational(15727240259832744812057210812134365969663, 5444517870735015415413993718908291383296)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_181(a:sympy.Rational):
	#(a - z**2 + 6050831182542497717853286941518620410625/5444517870735015415413993718908291383296 < 0) & (36893488147419103232*a**2 - 24623430962648187265*a < 21171758130567760151913340805128333933823/147573952589676412928)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(6050831182542497717853286941518620410625, 5444517870735015415413993718908291383296)), Integer(0)), StrictLessThan(Add(Mul(Integer(36893488147419103232), Pow(Symbol('a'), Integer(2))), Mul(Integer(-1), Integer(24623430962648187265), Symbol('a'))), Rational(21171758130567760151913340805128333933823, 147573952589676412928)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_182(a:sympy.Rational):
	#(a < 813179152525346414339585835102428211193689/348449143727040986586495598010130648530944) & (a > 24623430962648187265/73786976294838206464 - sqrt(288230376151711743)/268435456)

	pre_cond = And(StrictLessThan(Symbol('a'), Rational(813179152525346414339585835102428211193689, 348449143727040986586495598010130648530944)), StrictGreaterThan(Symbol('a'), Add(Rational(24623430962648187265, 73786976294838206464), Mul(Integer(-1), Rational(1, 268435456), Pow(Integer(288230376151711743), Rational(1, 2))))))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_183(a:sympy.Rational):
	#(a + y**2 - z**2 + 606313352372301434184770344590508180225/5444517870735015415413993718908291383296 < 0) & (-a**2 + 24623430962648187265*a/36893488147419103232 - y**2 + 2*y + 15727240259832744812057210812134365969663/5444517870735015415413993718908291383296 > 0)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Pow(Symbol('y'), Integer(2)), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(606313352372301434184770344590508180225, 5444517870735015415413993718908291383296)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('a'), Integer(2))), Mul(Rational(24623430962648187265, 36893488147419103232), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Mul(Integer(2), Symbol('y')), Rational(15727240259832744812057210812134365969663, 5444517870735015415413993718908291383296)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_184(a:sympy.Rational):
	#(a - z**2 + 6050831182542497717853286941518620410625/5444517870735015415413993718908291383296 < 0) & (36893488147419103232*a**2 - 24623430962648187265*a < 21171758130567760151913340805128333933823/147573952589676412928)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(6050831182542497717853286941518620410625, 5444517870735015415413993718908291383296)), Integer(0)), StrictLessThan(Add(Mul(Integer(36893488147419103232), Pow(Symbol('a'), Integer(2))), Mul(Integer(-1), Integer(24623430962648187265), Symbol('a'))), Rational(21171758130567760151913340805128333933823, 147573952589676412928)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_185(a:sympy.Rational):
	#(a < 813179152525346414339585835102428211193689/348449143727040986586495598010130648530944) & (a > 24623430962648187265/73786976294838206464 - sqrt(288230376151711743)/268435456)

	pre_cond = And(StrictLessThan(Symbol('a'), Rational(813179152525346414339585835102428211193689, 348449143727040986586495598010130648530944)), StrictGreaterThan(Symbol('a'), Add(Rational(24623430962648187265, 73786976294838206464), Mul(Integer(-1), Rational(1, 268435456), Pow(Integer(288230376151711743), Rational(1, 2))))))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_186(a:sympy.Rational):
	#(a + y**2 - z**2 + 606313352372301434184770344590508180225/5444517870735015415413993718908291383296 < 0) & (-a**2 + 24623430962648187265*a/36893488147419103232 - y**2 + 2*y + 15727240259832744812057210812134365969663/5444517870735015415413993718908291383296 > 0)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Pow(Symbol('y'), Integer(2)), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(606313352372301434184770344590508180225, 5444517870735015415413993718908291383296)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('a'), Integer(2))), Mul(Rational(24623430962648187265, 36893488147419103232), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Mul(Integer(2), Symbol('y')), Rational(15727240259832744812057210812134365969663, 5444517870735015415413993718908291383296)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_187(a:sympy.Rational):
	#(a - z**2 + 6050831182542497717853286941518620410625/5444517870735015415413993718908291383296 < 0) & (36893488147419103232*a**2 - 24623430962648187265*a < 21171758130567760151913340805128333933823/147573952589676412928)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(6050831182542497717853286941518620410625, 5444517870735015415413993718908291383296)), Integer(0)), StrictLessThan(Add(Mul(Integer(36893488147419103232), Pow(Symbol('a'), Integer(2))), Mul(Integer(-1), Integer(24623430962648187265), Symbol('a'))), Rational(21171758130567760151913340805128333933823, 147573952589676412928)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_188(a:sympy.Rational):
	#(a < 813179152525346414339585835102428211193689/348449143727040986586495598010130648530944) & (a > 24623430962648187265/73786976294838206464 - sqrt(288230376151711743)/268435456)

	pre_cond = And(StrictLessThan(Symbol('a'), Rational(813179152525346414339585835102428211193689, 348449143727040986586495598010130648530944)), StrictGreaterThan(Symbol('a'), Add(Rational(24623430962648187265, 73786976294838206464), Mul(Integer(-1), Rational(1, 268435456), Pow(Integer(288230376151711743), Rational(1, 2))))))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_189(a:sympy.Rational):
	#(a + y**2 - z**2 + 606313352372301434184770344590508180225/5444517870735015415413993718908291383296 < 0) & (-a**2 + 24623430962648187265*a/36893488147419103232 - y**2 + 2*y + 15727240259832744812057210812134365969663/5444517870735015415413993718908291383296 > 0)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Pow(Symbol('y'), Integer(2)), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(606313352372301434184770344590508180225, 5444517870735015415413993718908291383296)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('a'), Integer(2))), Mul(Rational(24623430962648187265, 36893488147419103232), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Mul(Integer(2), Symbol('y')), Rational(15727240259832744812057210812134365969663, 5444517870735015415413993718908291383296)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_190(a:sympy.Rational):
	#(a - z**2 + 6050831182542497717853286941518620410625/5444517870735015415413993718908291383296 < 0) & (36893488147419103232*a**2 - 24623430962648187265*a < 21171758130567760151913340805128333933823/147573952589676412928)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(6050831182542497717853286941518620410625, 5444517870735015415413993718908291383296)), Integer(0)), StrictLessThan(Add(Mul(Integer(36893488147419103232), Pow(Symbol('a'), Integer(2))), Mul(Integer(-1), Integer(24623430962648187265), Symbol('a'))), Rational(21171758130567760151913340805128333933823, 147573952589676412928)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_191(a:sympy.Rational):
	#(a < 813179152525346414339585835102428211193689/348449143727040986586495598010130648530944) & (a > 24623430962648187265/73786976294838206464 - sqrt(288230376151711743)/268435456)

	pre_cond = And(StrictLessThan(Symbol('a'), Rational(813179152525346414339585835102428211193689, 348449143727040986586495598010130648530944)), StrictGreaterThan(Symbol('a'), Add(Rational(24623430962648187265, 73786976294838206464), Mul(Integer(-1), Rational(1, 268435456), Pow(Integer(288230376151711743), Rational(1, 2))))))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_192(a:sympy.Rational):
	#(a + y**2 - z**2 + 606313352372301434184770344590508180225/5444517870735015415413993718908291383296 < 0) & (-a**2 + 24623430962648187265*a/36893488147419103232 - y**2 + 2*y + 15727240259832744812057210812134365969663/5444517870735015415413993718908291383296 > 0)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Pow(Symbol('y'), Integer(2)), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(606313352372301434184770344590508180225, 5444517870735015415413993718908291383296)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('a'), Integer(2))), Mul(Rational(24623430962648187265, 36893488147419103232), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Mul(Integer(2), Symbol('y')), Rational(15727240259832744812057210812134365969663, 5444517870735015415413993718908291383296)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_193(a:sympy.Rational):
	#(a - z**2 + 6050831182542497717853286941518620410625/5444517870735015415413993718908291383296 < 0) & (36893488147419103232*a**2 - 24623430962648187265*a < 21171758130567760151913340805128333933823/147573952589676412928)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(6050831182542497717853286941518620410625, 5444517870735015415413993718908291383296)), Integer(0)), StrictLessThan(Add(Mul(Integer(36893488147419103232), Pow(Symbol('a'), Integer(2))), Mul(Integer(-1), Integer(24623430962648187265), Symbol('a'))), Rational(21171758130567760151913340805128333933823, 147573952589676412928)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_194(a:sympy.Rational):
	#(a < 813179152525346414339585835102428211193689/348449143727040986586495598010130648530944) & (a > 24623430962648187265/73786976294838206464 - sqrt(288230376151711743)/268435456)

	pre_cond = And(StrictLessThan(Symbol('a'), Rational(813179152525346414339585835102428211193689, 348449143727040986586495598010130648530944)), StrictGreaterThan(Symbol('a'), Add(Rational(24623430962648187265, 73786976294838206464), Mul(Integer(-1), Rational(1, 268435456), Pow(Integer(288230376151711743), Rational(1, 2))))))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_195(a:sympy.Rational):
	#(a + y**2 - z**2 + 606313352372301434184770344590508180225/5444517870735015415413993718908291383296 < 0) & (-a**2 + 24623430962648187265*a/36893488147419103232 - y**2 + 2*y + 15727240259832744812057210812134365969663/5444517870735015415413993718908291383296 > 0)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Pow(Symbol('y'), Integer(2)), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(606313352372301434184770344590508180225, 5444517870735015415413993718908291383296)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('a'), Integer(2))), Mul(Rational(24623430962648187265, 36893488147419103232), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Mul(Integer(2), Symbol('y')), Rational(15727240259832744812057210812134365969663, 5444517870735015415413993718908291383296)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_196(a:sympy.Rational):
	#(a - z**2 + 6050831182542497717853286941518620410625/5444517870735015415413993718908291383296 < 0) & (36893488147419103232*a**2 - 24623430962648187265*a < 21171758130567760151913340805128333933823/147573952589676412928)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(6050831182542497717853286941518620410625, 5444517870735015415413993718908291383296)), Integer(0)), StrictLessThan(Add(Mul(Integer(36893488147419103232), Pow(Symbol('a'), Integer(2))), Mul(Integer(-1), Integer(24623430962648187265), Symbol('a'))), Rational(21171758130567760151913340805128333933823, 147573952589676412928)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_197(a:sympy.Rational):
	#(a < 813179152525346414339585835102428211193689/348449143727040986586495598010130648530944) & (a > 24623430962648187265/73786976294838206464 - sqrt(288230376151711743)/268435456)

	pre_cond = And(StrictLessThan(Symbol('a'), Rational(813179152525346414339585835102428211193689, 348449143727040986586495598010130648530944)), StrictGreaterThan(Symbol('a'), Add(Rational(24623430962648187265, 73786976294838206464), Mul(Integer(-1), Rational(1, 268435456), Pow(Integer(288230376151711743), Rational(1, 2))))))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_198(a:sympy.Rational):
	#(a + y**2 - z**2 + 606313352372301434184770344590508180225/5444517870735015415413993718908291383296 < 0) & (-a**2 + 24623430962648187265*a/36893488147419103232 - y**2 + 2*y + 15727240259832744812057210812134365969663/5444517870735015415413993718908291383296 > 0)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Pow(Symbol('y'), Integer(2)), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(606313352372301434184770344590508180225, 5444517870735015415413993718908291383296)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('a'), Integer(2))), Mul(Rational(24623430962648187265, 36893488147419103232), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Mul(Integer(2), Symbol('y')), Rational(15727240259832744812057210812134365969663, 5444517870735015415413993718908291383296)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_199(a:sympy.Rational):
	#(a - z**2 + 6050831182542497717853286941518620410625/5444517870735015415413993718908291383296 < 0) & (36893488147419103232*a**2 - 24623430962648187265*a < 21171758130567760151913340805128333933823/147573952589676412928)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(6050831182542497717853286941518620410625, 5444517870735015415413993718908291383296)), Integer(0)), StrictLessThan(Add(Mul(Integer(36893488147419103232), Pow(Symbol('a'), Integer(2))), Mul(Integer(-1), Integer(24623430962648187265), Symbol('a'))), Rational(21171758130567760151913340805128333933823, 147573952589676412928)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_200(a:sympy.Rational):
	#(a < 813179152525346414339585835102428211193689/348449143727040986586495598010130648530944) & (a > 24623430962648187265/73786976294838206464 - sqrt(288230376151711743)/268435456)

	pre_cond = And(StrictLessThan(Symbol('a'), Rational(813179152525346414339585835102428211193689, 348449143727040986586495598010130648530944)), StrictGreaterThan(Symbol('a'), Add(Rational(24623430962648187265, 73786976294838206464), Mul(Integer(-1), Rational(1, 268435456), Pow(Integer(288230376151711743), Rational(1, 2))))))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_201(a:sympy.Rational):
	#(a + y**2 - z**2 + 606313352372301434184770344590508180225/5444517870735015415413993718908291383296 < 0) & (-a**2 + 24623430962648187265*a/36893488147419103232 - y**2 + 2*y + 15727240259832744812057210812134365969663/5444517870735015415413993718908291383296 > 0)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Pow(Symbol('y'), Integer(2)), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(606313352372301434184770344590508180225, 5444517870735015415413993718908291383296)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('a'), Integer(2))), Mul(Rational(24623430962648187265, 36893488147419103232), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Mul(Integer(2), Symbol('y')), Rational(15727240259832744812057210812134365969663, 5444517870735015415413993718908291383296)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_202(a:sympy.Rational):
	#(a - z**2 + 6050831182542497717853286941518620410625/5444517870735015415413993718908291383296 < 0) & (36893488147419103232*a**2 - 24623430962648187265*a < 21171758130567760151913340805128333933823/147573952589676412928)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(6050831182542497717853286941518620410625, 5444517870735015415413993718908291383296)), Integer(0)), StrictLessThan(Add(Mul(Integer(36893488147419103232), Pow(Symbol('a'), Integer(2))), Mul(Integer(-1), Integer(24623430962648187265), Symbol('a'))), Rational(21171758130567760151913340805128333933823, 147573952589676412928)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_203(a:sympy.Rational):
	#(a < 813179152525346414339585835102428211193689/348449143727040986586495598010130648530944) & (a > 24623430962648187265/73786976294838206464 - sqrt(288230376151711743)/268435456)

	pre_cond = And(StrictLessThan(Symbol('a'), Rational(813179152525346414339585835102428211193689, 348449143727040986586495598010130648530944)), StrictGreaterThan(Symbol('a'), Add(Rational(24623430962648187265, 73786976294838206464), Mul(Integer(-1), Rational(1, 268435456), Pow(Integer(288230376151711743), Rational(1, 2))))))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_204(a:sympy.Rational):
	#(a + y**2 - z**2 + 606313352372301434184770344590508180225/5444517870735015415413993718908291383296 < 0) & (-a**2 + 24623430962648187265*a/36893488147419103232 - y**2 + 2*y + 15727240259832744812057210812134365969663/5444517870735015415413993718908291383296 > 0)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Pow(Symbol('y'), Integer(2)), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(606313352372301434184770344590508180225, 5444517870735015415413993718908291383296)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('a'), Integer(2))), Mul(Rational(24623430962648187265, 36893488147419103232), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Mul(Integer(2), Symbol('y')), Rational(15727240259832744812057210812134365969663, 5444517870735015415413993718908291383296)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_205(a:sympy.Rational):
	#(a - z**2 + 6050831182542497717853286941518620410625/5444517870735015415413993718908291383296 < 0) & (36893488147419103232*a**2 - 24623430962648187265*a < 21171758130567760151913340805128333933823/147573952589676412928)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(6050831182542497717853286941518620410625, 5444517870735015415413993718908291383296)), Integer(0)), StrictLessThan(Add(Mul(Integer(36893488147419103232), Pow(Symbol('a'), Integer(2))), Mul(Integer(-1), Integer(24623430962648187265), Symbol('a'))), Rational(21171758130567760151913340805128333933823, 147573952589676412928)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_206(a:sympy.Rational):
	#(a < 813179152525346414339585835102428211193689/348449143727040986586495598010130648530944) & (a > 24623430962648187265/73786976294838206464 - sqrt(288230376151711743)/268435456)

	pre_cond = And(StrictLessThan(Symbol('a'), Rational(813179152525346414339585835102428211193689, 348449143727040986586495598010130648530944)), StrictGreaterThan(Symbol('a'), Add(Rational(24623430962648187265, 73786976294838206464), Mul(Integer(-1), Rational(1, 268435456), Pow(Integer(288230376151711743), Rational(1, 2))))))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_207(a:sympy.Rational):
	#(a + y**2 - z**2 + 606313352372301434184770344590508180225/5444517870735015415413993718908291383296 < 0) & (-a**2 + 24623430962648187265*a/36893488147419103232 - y**2 + 2*y + 15727240259832744812057210812134365969663/5444517870735015415413993718908291383296 > 0)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Pow(Symbol('y'), Integer(2)), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(606313352372301434184770344590508180225, 5444517870735015415413993718908291383296)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('a'), Integer(2))), Mul(Rational(24623430962648187265, 36893488147419103232), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Mul(Integer(2), Symbol('y')), Rational(15727240259832744812057210812134365969663, 5444517870735015415413993718908291383296)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_208(a:sympy.Rational):
	#(a - z**2 + 6050831182542497717853286941518620410625/5444517870735015415413993718908291383296 < 0) & (36893488147419103232*a**2 - 24623430962648187265*a < 21171758130567760151913340805128333933823/147573952589676412928)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(6050831182542497717853286941518620410625, 5444517870735015415413993718908291383296)), Integer(0)), StrictLessThan(Add(Mul(Integer(36893488147419103232), Pow(Symbol('a'), Integer(2))), Mul(Integer(-1), Integer(24623430962648187265), Symbol('a'))), Rational(21171758130567760151913340805128333933823, 147573952589676412928)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_209(a:sympy.Rational):
	#(a < 813179152525346414339585835102428211193689/348449143727040986586495598010130648530944) & (a > 24623430962648187265/73786976294838206464 - sqrt(288230376151711743)/268435456)

	pre_cond = And(StrictLessThan(Symbol('a'), Rational(813179152525346414339585835102428211193689, 348449143727040986586495598010130648530944)), StrictGreaterThan(Symbol('a'), Add(Rational(24623430962648187265, 73786976294838206464), Mul(Integer(-1), Rational(1, 268435456), Pow(Integer(288230376151711743), Rational(1, 2))))))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_210(a:sympy.Rational):
	#(a + y**2 - z**2 + 606313352372301434184770344590508180225/5444517870735015415413993718908291383296 < 0) & (-a**2 + 24623430962648187265*a/36893488147419103232 - y**2 + 2*y + 15727240259832744812057210812134365969663/5444517870735015415413993718908291383296 > 0)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Pow(Symbol('y'), Integer(2)), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(606313352372301434184770344590508180225, 5444517870735015415413993718908291383296)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('a'), Integer(2))), Mul(Rational(24623430962648187265, 36893488147419103232), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Mul(Integer(2), Symbol('y')), Rational(15727240259832744812057210812134365969663, 5444517870735015415413993718908291383296)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_211(a:sympy.Rational):
	#(a - z**2 + 6050831182542497717853286941518620410625/5444517870735015415413993718908291383296 < 0) & (36893488147419103232*a**2 - 24623430962648187265*a < 21171758130567760151913340805128333933823/147573952589676412928)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(6050831182542497717853286941518620410625, 5444517870735015415413993718908291383296)), Integer(0)), StrictLessThan(Add(Mul(Integer(36893488147419103232), Pow(Symbol('a'), Integer(2))), Mul(Integer(-1), Integer(24623430962648187265), Symbol('a'))), Rational(21171758130567760151913340805128333933823, 147573952589676412928)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_212(a:sympy.Rational):
	#(a < 813179152525346414339585835102428211193689/348449143727040986586495598010130648530944) & (a > 24623430962648187265/73786976294838206464 - sqrt(288230376151711743)/268435456)

	pre_cond = And(StrictLessThan(Symbol('a'), Rational(813179152525346414339585835102428211193689, 348449143727040986586495598010130648530944)), StrictGreaterThan(Symbol('a'), Add(Rational(24623430962648187265, 73786976294838206464), Mul(Integer(-1), Rational(1, 268435456), Pow(Integer(288230376151711743), Rational(1, 2))))))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_213(a:sympy.Rational):
	#(a + y**2 - z**2 + 606313352372301434184770344590508180225/5444517870735015415413993718908291383296 < 0) & (-a**2 + 24623430962648187265*a/36893488147419103232 - y**2 + 2*y + 15727240259832744812057210812134365969663/5444517870735015415413993718908291383296 > 0)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Pow(Symbol('y'), Integer(2)), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(606313352372301434184770344590508180225, 5444517870735015415413993718908291383296)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('a'), Integer(2))), Mul(Rational(24623430962648187265, 36893488147419103232), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Mul(Integer(2), Symbol('y')), Rational(15727240259832744812057210812134365969663, 5444517870735015415413993718908291383296)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_214(a:sympy.Rational):
	#(a - z**2 + 6050831182542497717853286941518620410625/5444517870735015415413993718908291383296 < 0) & (36893488147419103232*a**2 - 24623430962648187265*a < 21171758130567760151913340805128333933823/147573952589676412928)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(6050831182542497717853286941518620410625, 5444517870735015415413993718908291383296)), Integer(0)), StrictLessThan(Add(Mul(Integer(36893488147419103232), Pow(Symbol('a'), Integer(2))), Mul(Integer(-1), Integer(24623430962648187265), Symbol('a'))), Rational(21171758130567760151913340805128333933823, 147573952589676412928)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_215(a:sympy.Rational):
	#(a < 813179152525346414339585835102428211193689/348449143727040986586495598010130648530944) & (a > 24623430962648187265/73786976294838206464 - sqrt(288230376151711743)/268435456)

	pre_cond = And(StrictLessThan(Symbol('a'), Rational(813179152525346414339585835102428211193689, 348449143727040986586495598010130648530944)), StrictGreaterThan(Symbol('a'), Add(Rational(24623430962648187265, 73786976294838206464), Mul(Integer(-1), Rational(1, 268435456), Pow(Integer(288230376151711743), Rational(1, 2))))))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_216(a:sympy.Rational):
	#(a + y**2 - z**2 + 606313352372301434184770344590508180225/5444517870735015415413993718908291383296 < 0) & (-a**2 + 24623430962648187265*a/36893488147419103232 - y**2 + 2*y + 15727240259832744812057210812134365969663/5444517870735015415413993718908291383296 > 0)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Pow(Symbol('y'), Integer(2)), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(606313352372301434184770344590508180225, 5444517870735015415413993718908291383296)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('a'), Integer(2))), Mul(Rational(24623430962648187265, 36893488147419103232), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Mul(Integer(2), Symbol('y')), Rational(15727240259832744812057210812134365969663, 5444517870735015415413993718908291383296)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_217(a:sympy.Rational):
	#(a - z**2 + 6050831182542497717853286941518620410625/5444517870735015415413993718908291383296 < 0) & (36893488147419103232*a**2 - 24623430962648187265*a < 21171758130567760151913340805128333933823/147573952589676412928)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(6050831182542497717853286941518620410625, 5444517870735015415413993718908291383296)), Integer(0)), StrictLessThan(Add(Mul(Integer(36893488147419103232), Pow(Symbol('a'), Integer(2))), Mul(Integer(-1), Integer(24623430962648187265), Symbol('a'))), Rational(21171758130567760151913340805128333933823, 147573952589676412928)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_218(a:sympy.Rational):
	#(a < 813179152525346414339585835102428211193689/348449143727040986586495598010130648530944) & (a > 24623430962648187265/73786976294838206464 - sqrt(288230376151711743)/268435456)

	pre_cond = And(StrictLessThan(Symbol('a'), Rational(813179152525346414339585835102428211193689, 348449143727040986586495598010130648530944)), StrictGreaterThan(Symbol('a'), Add(Rational(24623430962648187265, 73786976294838206464), Mul(Integer(-1), Rational(1, 268435456), Pow(Integer(288230376151711743), Rational(1, 2))))))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_219(a:sympy.Rational):
	#(a + y**2 - z**2 + 606313352372301434184770344590508180225/5444517870735015415413993718908291383296 < 0) & (-a**2 + 24623430962648187265*a/36893488147419103232 - y**2 + 2*y + 15727240259832744812057210812134365969663/5444517870735015415413993718908291383296 > 0)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Pow(Symbol('y'), Integer(2)), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(606313352372301434184770344590508180225, 5444517870735015415413993718908291383296)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('a'), Integer(2))), Mul(Rational(24623430962648187265, 36893488147419103232), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Mul(Integer(2), Symbol('y')), Rational(15727240259832744812057210812134365969663, 5444517870735015415413993718908291383296)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_220(a:sympy.Rational):
	#(a - z**2 + 6050831182542497717853286941518620410625/5444517870735015415413993718908291383296 < 0) & (36893488147419103232*a**2 - 24623430962648187265*a < 21171758130567760151913340805128333933823/147573952589676412928)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(6050831182542497717853286941518620410625, 5444517870735015415413993718908291383296)), Integer(0)), StrictLessThan(Add(Mul(Integer(36893488147419103232), Pow(Symbol('a'), Integer(2))), Mul(Integer(-1), Integer(24623430962648187265), Symbol('a'))), Rational(21171758130567760151913340805128333933823, 147573952589676412928)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_221(a:sympy.Rational):
	#(a < 813179152525346414339585835102428211193689/348449143727040986586495598010130648530944) & (a > 24623430962648187265/73786976294838206464 - sqrt(288230376151711743)/268435456)

	pre_cond = And(StrictLessThan(Symbol('a'), Rational(813179152525346414339585835102428211193689, 348449143727040986586495598010130648530944)), StrictGreaterThan(Symbol('a'), Add(Rational(24623430962648187265, 73786976294838206464), Mul(Integer(-1), Rational(1, 268435456), Pow(Integer(288230376151711743), Rational(1, 2))))))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_222(a:sympy.Rational):
	#(a + y**2 - z**2 + 606313352372301434184770344590508180225/5444517870735015415413993718908291383296 < 0) & (-a**2 + 24623430962648187265*a/36893488147419103232 - y**2 + 2*y + 15727240259832744812057210812134365969663/5444517870735015415413993718908291383296 > 0)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Pow(Symbol('y'), Integer(2)), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(606313352372301434184770344590508180225, 5444517870735015415413993718908291383296)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('a'), Integer(2))), Mul(Rational(24623430962648187265, 36893488147419103232), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Mul(Integer(2), Symbol('y')), Rational(15727240259832744812057210812134365969663, 5444517870735015415413993718908291383296)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_223(a:sympy.Rational):
	#(a - z**2 + 6050831182542497717853286941518620410625/5444517870735015415413993718908291383296 < 0) & (36893488147419103232*a**2 - 24623430962648187265*a < 21171758130567760151913340805128333933823/147573952589676412928)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(6050831182542497717853286941518620410625, 5444517870735015415413993718908291383296)), Integer(0)), StrictLessThan(Add(Mul(Integer(36893488147419103232), Pow(Symbol('a'), Integer(2))), Mul(Integer(-1), Integer(24623430962648187265), Symbol('a'))), Rational(21171758130567760151913340805128333933823, 147573952589676412928)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_224(a:sympy.Rational):
	#(a < 813179152525346414339585835102428211193689/348449143727040986586495598010130648530944) & (a > 24623430962648187265/73786976294838206464 - sqrt(288230376151711743)/268435456)

	pre_cond = And(StrictLessThan(Symbol('a'), Rational(813179152525346414339585835102428211193689, 348449143727040986586495598010130648530944)), StrictGreaterThan(Symbol('a'), Add(Rational(24623430962648187265, 73786976294838206464), Mul(Integer(-1), Rational(1, 268435456), Pow(Integer(288230376151711743), Rational(1, 2))))))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_225(a:sympy.Rational):
	#(a + y**2 - z**2 + 606313352372301434184770344590508180225/5444517870735015415413993718908291383296 < 0) & (-a**2 + 24623430962648187265*a/36893488147419103232 - y**2 + 2*y + 15727240259832744812057210812134365969663/5444517870735015415413993718908291383296 > 0)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Pow(Symbol('y'), Integer(2)), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(606313352372301434184770344590508180225, 5444517870735015415413993718908291383296)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('a'), Integer(2))), Mul(Rational(24623430962648187265, 36893488147419103232), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Mul(Integer(2), Symbol('y')), Rational(15727240259832744812057210812134365969663, 5444517870735015415413993718908291383296)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_226(a:sympy.Rational):
	#(a - z**2 + 6050831182542497717853286941518620410625/5444517870735015415413993718908291383296 < 0) & (36893488147419103232*a**2 - 24623430962648187265*a < 21171758130567760151913340805128333933823/147573952589676412928)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(6050831182542497717853286941518620410625, 5444517870735015415413993718908291383296)), Integer(0)), StrictLessThan(Add(Mul(Integer(36893488147419103232), Pow(Symbol('a'), Integer(2))), Mul(Integer(-1), Integer(24623430962648187265), Symbol('a'))), Rational(21171758130567760151913340805128333933823, 147573952589676412928)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_227(a:sympy.Rational):
	#(a < 813179152525346414339585835102428211193689/348449143727040986586495598010130648530944) & (a > 24623430962648187265/73786976294838206464 - sqrt(288230376151711743)/268435456)

	pre_cond = And(StrictLessThan(Symbol('a'), Rational(813179152525346414339585835102428211193689, 348449143727040986586495598010130648530944)), StrictGreaterThan(Symbol('a'), Add(Rational(24623430962648187265, 73786976294838206464), Mul(Integer(-1), Rational(1, 268435456), Pow(Integer(288230376151711743), Rational(1, 2))))))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_228(a:sympy.Rational):
	#(a + y**2 - z**2 + 606313352372301434184770344590508180225/5444517870735015415413993718908291383296 < 0) & (-a**2 + 24623430962648187265*a/36893488147419103232 - y**2 + 2*y + 15727240259832744812057210812134365969663/5444517870735015415413993718908291383296 > 0)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Pow(Symbol('y'), Integer(2)), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(606313352372301434184770344590508180225, 5444517870735015415413993718908291383296)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('a'), Integer(2))), Mul(Rational(24623430962648187265, 36893488147419103232), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Mul(Integer(2), Symbol('y')), Rational(15727240259832744812057210812134365969663, 5444517870735015415413993718908291383296)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_229(a:sympy.Rational):
	#(a - z**2 + 6050831182542497717853286941518620410625/5444517870735015415413993718908291383296 < 0) & (36893488147419103232*a**2 - 24623430962648187265*a < 21171758130567760151913340805128333933823/147573952589676412928)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(6050831182542497717853286941518620410625, 5444517870735015415413993718908291383296)), Integer(0)), StrictLessThan(Add(Mul(Integer(36893488147419103232), Pow(Symbol('a'), Integer(2))), Mul(Integer(-1), Integer(24623430962648187265), Symbol('a'))), Rational(21171758130567760151913340805128333933823, 147573952589676412928)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_230(a:sympy.Rational):
	#(a < 813179152525346414339585835102428211193689/348449143727040986586495598010130648530944) & (a > 24623430962648187265/73786976294838206464 - sqrt(288230376151711743)/268435456)

	pre_cond = And(StrictLessThan(Symbol('a'), Rational(813179152525346414339585835102428211193689, 348449143727040986586495598010130648530944)), StrictGreaterThan(Symbol('a'), Add(Rational(24623430962648187265, 73786976294838206464), Mul(Integer(-1), Rational(1, 268435456), Pow(Integer(288230376151711743), Rational(1, 2))))))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_231(a:sympy.Rational):
	#(a + y**2 - z**2 + 606313352372301434184770344590508180225/5444517870735015415413993718908291383296 < 0) & (-a**2 + 24623430962648187265*a/36893488147419103232 - y**2 + 2*y + 15727240259832744812057210812134365969663/5444517870735015415413993718908291383296 > 0)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Pow(Symbol('y'), Integer(2)), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(606313352372301434184770344590508180225, 5444517870735015415413993718908291383296)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('a'), Integer(2))), Mul(Rational(24623430962648187265, 36893488147419103232), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Mul(Integer(2), Symbol('y')), Rational(15727240259832744812057210812134365969663, 5444517870735015415413993718908291383296)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_232(a:sympy.Rational):
	#(a - z**2 + 6050831182542497717853286941518620410625/5444517870735015415413993718908291383296 < 0) & (36893488147419103232*a**2 - 24623430962648187265*a < 21171758130567760151913340805128333933823/147573952589676412928)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(6050831182542497717853286941518620410625, 5444517870735015415413993718908291383296)), Integer(0)), StrictLessThan(Add(Mul(Integer(36893488147419103232), Pow(Symbol('a'), Integer(2))), Mul(Integer(-1), Integer(24623430962648187265), Symbol('a'))), Rational(21171758130567760151913340805128333933823, 147573952589676412928)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_233(a:sympy.Rational):
	#(a < 813179152525346414339585835102428211193689/348449143727040986586495598010130648530944) & (a > 24623430962648187265/73786976294838206464 - sqrt(288230376151711743)/268435456)

	pre_cond = And(StrictLessThan(Symbol('a'), Rational(813179152525346414339585835102428211193689, 348449143727040986586495598010130648530944)), StrictGreaterThan(Symbol('a'), Add(Rational(24623430962648187265, 73786976294838206464), Mul(Integer(-1), Rational(1, 268435456), Pow(Integer(288230376151711743), Rational(1, 2))))))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_234(a:sympy.Rational):
	#(a + y**2 - z**2 + 606313352372301434184770344590508180225/5444517870735015415413993718908291383296 < 0) & (-a**2 + 24623430962648187265*a/36893488147419103232 - y**2 + 2*y + 15727240259832744812057210812134365969663/5444517870735015415413993718908291383296 > 0)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Pow(Symbol('y'), Integer(2)), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(606313352372301434184770344590508180225, 5444517870735015415413993718908291383296)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('a'), Integer(2))), Mul(Rational(24623430962648187265, 36893488147419103232), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Mul(Integer(2), Symbol('y')), Rational(15727240259832744812057210812134365969663, 5444517870735015415413993718908291383296)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_235(a:sympy.Rational):
	#(a - z**2 + 6050831182542497717853286941518620410625/5444517870735015415413993718908291383296 < 0) & (36893488147419103232*a**2 - 24623430962648187265*a < 21171758130567760151913340805128333933823/147573952589676412928)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(6050831182542497717853286941518620410625, 5444517870735015415413993718908291383296)), Integer(0)), StrictLessThan(Add(Mul(Integer(36893488147419103232), Pow(Symbol('a'), Integer(2))), Mul(Integer(-1), Integer(24623430962648187265), Symbol('a'))), Rational(21171758130567760151913340805128333933823, 147573952589676412928)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_236(a:sympy.Rational):
	#(a < 813179152525346414339585835102428211193689/348449143727040986586495598010130648530944) & (a > 24623430962648187265/73786976294838206464 - sqrt(288230376151711743)/268435456)

	pre_cond = And(StrictLessThan(Symbol('a'), Rational(813179152525346414339585835102428211193689, 348449143727040986586495598010130648530944)), StrictGreaterThan(Symbol('a'), Add(Rational(24623430962648187265, 73786976294838206464), Mul(Integer(-1), Rational(1, 268435456), Pow(Integer(288230376151711743), Rational(1, 2))))))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_237(a:sympy.Rational):
	#(a + y**2 - z**2 + 606313352372301434184770344590508180225/5444517870735015415413993718908291383296 < 0) & (-a**2 + 24623430962648187265*a/36893488147419103232 - y**2 + 2*y + 15727240259832744812057210812134365969663/5444517870735015415413993718908291383296 > 0)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Pow(Symbol('y'), Integer(2)), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(606313352372301434184770344590508180225, 5444517870735015415413993718908291383296)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('a'), Integer(2))), Mul(Rational(24623430962648187265, 36893488147419103232), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Mul(Integer(2), Symbol('y')), Rational(15727240259832744812057210812134365969663, 5444517870735015415413993718908291383296)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_238(a:sympy.Rational):
	#(a - z**2 + 6050831182542497717853286941518620410625/5444517870735015415413993718908291383296 < 0) & (36893488147419103232*a**2 - 24623430962648187265*a < 21171758130567760151913340805128333933823/147573952589676412928)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(6050831182542497717853286941518620410625, 5444517870735015415413993718908291383296)), Integer(0)), StrictLessThan(Add(Mul(Integer(36893488147419103232), Pow(Symbol('a'), Integer(2))), Mul(Integer(-1), Integer(24623430962648187265), Symbol('a'))), Rational(21171758130567760151913340805128333933823, 147573952589676412928)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_239(a:sympy.Rational):
	#(a < 813179152525346414339585835102428211193689/348449143727040986586495598010130648530944) & (a > 24623430962648187265/73786976294838206464 - sqrt(288230376151711743)/268435456)

	pre_cond = And(StrictLessThan(Symbol('a'), Rational(813179152525346414339585835102428211193689, 348449143727040986586495598010130648530944)), StrictGreaterThan(Symbol('a'), Add(Rational(24623430962648187265, 73786976294838206464), Mul(Integer(-1), Rational(1, 268435456), Pow(Integer(288230376151711743), Rational(1, 2))))))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_240(a:sympy.Rational):
	#(a + y**2 - z**2 + 606313352372301434184770344590508180225/5444517870735015415413993718908291383296 < 0) & (-a**2 + 24623430962648187265*a/36893488147419103232 - y**2 + 2*y + 15727240259832744812057210812134365969663/5444517870735015415413993718908291383296 > 0)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Pow(Symbol('y'), Integer(2)), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(606313352372301434184770344590508180225, 5444517870735015415413993718908291383296)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('a'), Integer(2))), Mul(Rational(24623430962648187265, 36893488147419103232), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Mul(Integer(2), Symbol('y')), Rational(15727240259832744812057210812134365969663, 5444517870735015415413993718908291383296)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_241(a:sympy.Rational):
	#(a - z**2 + 6050831182542497717853286941518620410625/5444517870735015415413993718908291383296 < 0) & (36893488147419103232*a**2 - 24623430962648187265*a < 21171758130567760151913340805128333933823/147573952589676412928)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(6050831182542497717853286941518620410625, 5444517870735015415413993718908291383296)), Integer(0)), StrictLessThan(Add(Mul(Integer(36893488147419103232), Pow(Symbol('a'), Integer(2))), Mul(Integer(-1), Integer(24623430962648187265), Symbol('a'))), Rational(21171758130567760151913340805128333933823, 147573952589676412928)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_242(a:sympy.Rational):
	#(a < 813179152525346414339585835102428211193689/348449143727040986586495598010130648530944) & (a > 24623430962648187265/73786976294838206464 - sqrt(288230376151711743)/268435456)

	pre_cond = And(StrictLessThan(Symbol('a'), Rational(813179152525346414339585835102428211193689, 348449143727040986586495598010130648530944)), StrictGreaterThan(Symbol('a'), Add(Rational(24623430962648187265, 73786976294838206464), Mul(Integer(-1), Rational(1, 268435456), Pow(Integer(288230376151711743), Rational(1, 2))))))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_243(a:sympy.Rational):
	#(a + y**2 - z**2 + 606313352372301434184770344590508180225/5444517870735015415413993718908291383296 < 0) & (-a**2 + 24623430962648187265*a/36893488147419103232 - y**2 + 2*y + 15727240259832744812057210812134365969663/5444517870735015415413993718908291383296 > 0)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Pow(Symbol('y'), Integer(2)), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(606313352372301434184770344590508180225, 5444517870735015415413993718908291383296)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('a'), Integer(2))), Mul(Rational(24623430962648187265, 36893488147419103232), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Mul(Integer(2), Symbol('y')), Rational(15727240259832744812057210812134365969663, 5444517870735015415413993718908291383296)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_244(a:sympy.Rational):
	#(a - z**2 + 6050831182542497717853286941518620410625/5444517870735015415413993718908291383296 < 0) & (36893488147419103232*a**2 - 24623430962648187265*a < 21171758130567760151913340805128333933823/147573952589676412928)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(6050831182542497717853286941518620410625, 5444517870735015415413993718908291383296)), Integer(0)), StrictLessThan(Add(Mul(Integer(36893488147419103232), Pow(Symbol('a'), Integer(2))), Mul(Integer(-1), Integer(24623430962648187265), Symbol('a'))), Rational(21171758130567760151913340805128333933823, 147573952589676412928)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_245(a:sympy.Rational):
	#(a < 813179152525346414339585835102428211193689/348449143727040986586495598010130648530944) & (a > 24623430962648187265/73786976294838206464 - sqrt(288230376151711743)/268435456)

	pre_cond = And(StrictLessThan(Symbol('a'), Rational(813179152525346414339585835102428211193689, 348449143727040986586495598010130648530944)), StrictGreaterThan(Symbol('a'), Add(Rational(24623430962648187265, 73786976294838206464), Mul(Integer(-1), Rational(1, 268435456), Pow(Integer(288230376151711743), Rational(1, 2))))))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_246(a:sympy.Rational):
	#(a + y**2 - z**2 + 606313352372301434184770344590508180225/5444517870735015415413993718908291383296 < 0) & (-a**2 + 24623430962648187265*a/36893488147419103232 - y**2 + 2*y + 15727240259832744812057210812134365969663/5444517870735015415413993718908291383296 > 0)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Pow(Symbol('y'), Integer(2)), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(606313352372301434184770344590508180225, 5444517870735015415413993718908291383296)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('a'), Integer(2))), Mul(Rational(24623430962648187265, 36893488147419103232), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Mul(Integer(2), Symbol('y')), Rational(15727240259832744812057210812134365969663, 5444517870735015415413993718908291383296)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_247(a:sympy.Rational):
	#(a - z**2 + 6050831182542497717853286941518620410625/5444517870735015415413993718908291383296 < 0) & (36893488147419103232*a**2 - 24623430962648187265*a < 21171758130567760151913340805128333933823/147573952589676412928)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(6050831182542497717853286941518620410625, 5444517870735015415413993718908291383296)), Integer(0)), StrictLessThan(Add(Mul(Integer(36893488147419103232), Pow(Symbol('a'), Integer(2))), Mul(Integer(-1), Integer(24623430962648187265), Symbol('a'))), Rational(21171758130567760151913340805128333933823, 147573952589676412928)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_248(a:sympy.Rational):
	#(a < 813179152525346414339585835102428211193689/348449143727040986586495598010130648530944) & (a > 24623430962648187265/73786976294838206464 - sqrt(288230376151711743)/268435456)

	pre_cond = And(StrictLessThan(Symbol('a'), Rational(813179152525346414339585835102428211193689, 348449143727040986586495598010130648530944)), StrictGreaterThan(Symbol('a'), Add(Rational(24623430962648187265, 73786976294838206464), Mul(Integer(-1), Rational(1, 268435456), Pow(Integer(288230376151711743), Rational(1, 2))))))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_249(a:sympy.Rational):
	#(a + y**2 - z**2 + 606313352372301434184770344590508180225/5444517870735015415413993718908291383296 < 0) & (-a**2 + 24623430962648187265*a/36893488147419103232 - y**2 + 2*y + 15727240259832744812057210812134365969663/5444517870735015415413993718908291383296 > 0)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Pow(Symbol('y'), Integer(2)), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(606313352372301434184770344590508180225, 5444517870735015415413993718908291383296)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('a'), Integer(2))), Mul(Rational(24623430962648187265, 36893488147419103232), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Mul(Integer(2), Symbol('y')), Rational(15727240259832744812057210812134365969663, 5444517870735015415413993718908291383296)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_250(a:sympy.Rational):
	#(a - z**2 + 6050831182542497717853286941518620410625/5444517870735015415413993718908291383296 < 0) & (36893488147419103232*a**2 - 24623430962648187265*a < 21171758130567760151913340805128333933823/147573952589676412928)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(6050831182542497717853286941518620410625, 5444517870735015415413993718908291383296)), Integer(0)), StrictLessThan(Add(Mul(Integer(36893488147419103232), Pow(Symbol('a'), Integer(2))), Mul(Integer(-1), Integer(24623430962648187265), Symbol('a'))), Rational(21171758130567760151913340805128333933823, 147573952589676412928)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_251(a:sympy.Rational):
	#(a < 813179152525346414339585835102428211193689/348449143727040986586495598010130648530944) & (a > 24623430962648187265/73786976294838206464 - sqrt(288230376151711743)/268435456)

	pre_cond = And(StrictLessThan(Symbol('a'), Rational(813179152525346414339585835102428211193689, 348449143727040986586495598010130648530944)), StrictGreaterThan(Symbol('a'), Add(Rational(24623430962648187265, 73786976294838206464), Mul(Integer(-1), Rational(1, 268435456), Pow(Integer(288230376151711743), Rational(1, 2))))))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_252(a:sympy.Rational):
	#(a + y**2 - z**2 + 606313352372301434184770344590508180225/5444517870735015415413993718908291383296 < 0) & (-a**2 + 24623430962648187265*a/36893488147419103232 - y**2 + 2*y + 15727240259832744812057210812134365969663/5444517870735015415413993718908291383296 > 0)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Pow(Symbol('y'), Integer(2)), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(606313352372301434184770344590508180225, 5444517870735015415413993718908291383296)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('a'), Integer(2))), Mul(Rational(24623430962648187265, 36893488147419103232), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Mul(Integer(2), Symbol('y')), Rational(15727240259832744812057210812134365969663, 5444517870735015415413993718908291383296)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_253(a:sympy.Rational):
	#(a - z**2 + 6050831182542497717853286941518620410625/5444517870735015415413993718908291383296 < 0) & (36893488147419103232*a**2 - 24623430962648187265*a < 21171758130567760151913340805128333933823/147573952589676412928)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(6050831182542497717853286941518620410625, 5444517870735015415413993718908291383296)), Integer(0)), StrictLessThan(Add(Mul(Integer(36893488147419103232), Pow(Symbol('a'), Integer(2))), Mul(Integer(-1), Integer(24623430962648187265), Symbol('a'))), Rational(21171758130567760151913340805128333933823, 147573952589676412928)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_254(a:sympy.Rational):
	#(a < 813179152525346414339585835102428211193689/348449143727040986586495598010130648530944) & (a > 24623430962648187265/73786976294838206464 - sqrt(288230376151711743)/268435456)

	pre_cond = And(StrictLessThan(Symbol('a'), Rational(813179152525346414339585835102428211193689, 348449143727040986586495598010130648530944)), StrictGreaterThan(Symbol('a'), Add(Rational(24623430962648187265, 73786976294838206464), Mul(Integer(-1), Rational(1, 268435456), Pow(Integer(288230376151711743), Rational(1, 2))))))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_255(a:sympy.Rational):
	#(a + y**2 - z**2 + 606313352372301434184770344590508180225/5444517870735015415413993718908291383296 < 0) & (-a**2 + 24623430962648187265*a/36893488147419103232 - y**2 + 2*y + 15727240259832744812057210812134365969663/5444517870735015415413993718908291383296 > 0)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Pow(Symbol('y'), Integer(2)), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(606313352372301434184770344590508180225, 5444517870735015415413993718908291383296)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('a'), Integer(2))), Mul(Rational(24623430962648187265, 36893488147419103232), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Mul(Integer(2), Symbol('y')), Rational(15727240259832744812057210812134365969663, 5444517870735015415413993718908291383296)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_256(a:sympy.Rational):
	#(a - z**2 + 6050831182542497717853286941518620410625/5444517870735015415413993718908291383296 < 0) & (36893488147419103232*a**2 - 24623430962648187265*a < 21171758130567760151913340805128333933823/147573952589676412928)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(6050831182542497717853286941518620410625, 5444517870735015415413993718908291383296)), Integer(0)), StrictLessThan(Add(Mul(Integer(36893488147419103232), Pow(Symbol('a'), Integer(2))), Mul(Integer(-1), Integer(24623430962648187265), Symbol('a'))), Rational(21171758130567760151913340805128333933823, 147573952589676412928)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_257(a:sympy.Rational):
	#(a < 813179152525346414339585835102428211193689/348449143727040986586495598010130648530944) & (a > 24623430962648187265/73786976294838206464 - sqrt(288230376151711743)/268435456)

	pre_cond = And(StrictLessThan(Symbol('a'), Rational(813179152525346414339585835102428211193689, 348449143727040986586495598010130648530944)), StrictGreaterThan(Symbol('a'), Add(Rational(24623430962648187265, 73786976294838206464), Mul(Integer(-1), Rational(1, 268435456), Pow(Integer(288230376151711743), Rational(1, 2))))))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_258(a:sympy.Rational):
	#(a + y**2 - z**2 + 606313352372301434184770344590508180225/5444517870735015415413993718908291383296 < 0) & (-a**2 + 24623430962648187265*a/36893488147419103232 - y**2 + 2*y + 15727240259832744812057210812134365969663/5444517870735015415413993718908291383296 > 0)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Pow(Symbol('y'), Integer(2)), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(606313352372301434184770344590508180225, 5444517870735015415413993718908291383296)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('a'), Integer(2))), Mul(Rational(24623430962648187265, 36893488147419103232), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Mul(Integer(2), Symbol('y')), Rational(15727240259832744812057210812134365969663, 5444517870735015415413993718908291383296)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_259(a:sympy.Rational):
	#(a - z**2 + 6050831182542497717853286941518620410625/5444517870735015415413993718908291383296 < 0) & (36893488147419103232*a**2 - 24623430962648187265*a < 21171758130567760151913340805128333933823/147573952589676412928)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(6050831182542497717853286941518620410625, 5444517870735015415413993718908291383296)), Integer(0)), StrictLessThan(Add(Mul(Integer(36893488147419103232), Pow(Symbol('a'), Integer(2))), Mul(Integer(-1), Integer(24623430962648187265), Symbol('a'))), Rational(21171758130567760151913340805128333933823, 147573952589676412928)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_260(a:sympy.Rational):
	#(a < 813179152525346414339585835102428211193689/348449143727040986586495598010130648530944) & (a > 24623430962648187265/73786976294838206464 - sqrt(288230376151711743)/268435456)

	pre_cond = And(StrictLessThan(Symbol('a'), Rational(813179152525346414339585835102428211193689, 348449143727040986586495598010130648530944)), StrictGreaterThan(Symbol('a'), Add(Rational(24623430962648187265, 73786976294838206464), Mul(Integer(-1), Rational(1, 268435456), Pow(Integer(288230376151711743), Rational(1, 2))))))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_261(a:sympy.Rational):
	#(a + y**2 - z**2 + 606313352372301434184770344590508180225/5444517870735015415413993718908291383296 < 0) & (-a**2 + 24623430962648187265*a/36893488147419103232 - y**2 + 2*y + 15727240259832744812057210812134365969663/5444517870735015415413993718908291383296 > 0)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Pow(Symbol('y'), Integer(2)), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(606313352372301434184770344590508180225, 5444517870735015415413993718908291383296)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('a'), Integer(2))), Mul(Rational(24623430962648187265, 36893488147419103232), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Mul(Integer(2), Symbol('y')), Rational(15727240259832744812057210812134365969663, 5444517870735015415413993718908291383296)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_262(a:sympy.Rational):
	#(a - z**2 + 6050831182542497717853286941518620410625/5444517870735015415413993718908291383296 < 0) & (36893488147419103232*a**2 - 24623430962648187265*a < 21171758130567760151913340805128333933823/147573952589676412928)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(6050831182542497717853286941518620410625, 5444517870735015415413993718908291383296)), Integer(0)), StrictLessThan(Add(Mul(Integer(36893488147419103232), Pow(Symbol('a'), Integer(2))), Mul(Integer(-1), Integer(24623430962648187265), Symbol('a'))), Rational(21171758130567760151913340805128333933823, 147573952589676412928)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_263(a:sympy.Rational):
	#(a < 813179152525346414339585835102428211193689/348449143727040986586495598010130648530944) & (a > 24623430962648187265/73786976294838206464 - sqrt(288230376151711743)/268435456)

	pre_cond = And(StrictLessThan(Symbol('a'), Rational(813179152525346414339585835102428211193689, 348449143727040986586495598010130648530944)), StrictGreaterThan(Symbol('a'), Add(Rational(24623430962648187265, 73786976294838206464), Mul(Integer(-1), Rational(1, 268435456), Pow(Integer(288230376151711743), Rational(1, 2))))))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_264(a:sympy.Rational):
	#(a + y**2 - z**2 + 606313352372301434184770344590508180225/5444517870735015415413993718908291383296 < 0) & (-a**2 + 24623430962648187265*a/36893488147419103232 - y**2 + 2*y + 15727240259832744812057210812134365969663/5444517870735015415413993718908291383296 > 0)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Pow(Symbol('y'), Integer(2)), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(606313352372301434184770344590508180225, 5444517870735015415413993718908291383296)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('a'), Integer(2))), Mul(Rational(24623430962648187265, 36893488147419103232), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Mul(Integer(2), Symbol('y')), Rational(15727240259832744812057210812134365969663, 5444517870735015415413993718908291383296)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_265(a:sympy.Rational):
	#(a - z**2 + 6050831182542497717853286941518620410625/5444517870735015415413993718908291383296 < 0) & (36893488147419103232*a**2 - 24623430962648187265*a < 21171758130567760151913340805128333933823/147573952589676412928)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(6050831182542497717853286941518620410625, 5444517870735015415413993718908291383296)), Integer(0)), StrictLessThan(Add(Mul(Integer(36893488147419103232), Pow(Symbol('a'), Integer(2))), Mul(Integer(-1), Integer(24623430962648187265), Symbol('a'))), Rational(21171758130567760151913340805128333933823, 147573952589676412928)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_266(a:sympy.Rational):
	#(a < 813179152525346414339585835102428211193689/348449143727040986586495598010130648530944) & (a > 24623430962648187265/73786976294838206464 - sqrt(288230376151711743)/268435456)

	pre_cond = And(StrictLessThan(Symbol('a'), Rational(813179152525346414339585835102428211193689, 348449143727040986586495598010130648530944)), StrictGreaterThan(Symbol('a'), Add(Rational(24623430962648187265, 73786976294838206464), Mul(Integer(-1), Rational(1, 268435456), Pow(Integer(288230376151711743), Rational(1, 2))))))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_267(a:sympy.Rational):
	#(a + y**2 - z**2 + 606313352372301434184770344590508180225/5444517870735015415413993718908291383296 < 0) & (-a**2 + 24623430962648187265*a/36893488147419103232 - y**2 + 2*y + 15727240259832744812057210812134365969663/5444517870735015415413993718908291383296 > 0)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Pow(Symbol('y'), Integer(2)), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(606313352372301434184770344590508180225, 5444517870735015415413993718908291383296)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('a'), Integer(2))), Mul(Rational(24623430962648187265, 36893488147419103232), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Mul(Integer(2), Symbol('y')), Rational(15727240259832744812057210812134365969663, 5444517870735015415413993718908291383296)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_268(a:sympy.Rational):
	#(a - z**2 + 6050831182542497717853286941518620410625/5444517870735015415413993718908291383296 < 0) & (36893488147419103232*a**2 - 24623430962648187265*a < 21171758130567760151913340805128333933823/147573952589676412928)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(6050831182542497717853286941518620410625, 5444517870735015415413993718908291383296)), Integer(0)), StrictLessThan(Add(Mul(Integer(36893488147419103232), Pow(Symbol('a'), Integer(2))), Mul(Integer(-1), Integer(24623430962648187265), Symbol('a'))), Rational(21171758130567760151913340805128333933823, 147573952589676412928)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_269(a:sympy.Rational):
	#(a < 813179152525346414339585835102428211193689/348449143727040986586495598010130648530944) & (a > 24623430962648187265/73786976294838206464 - sqrt(288230376151711743)/268435456)

	pre_cond = And(StrictLessThan(Symbol('a'), Rational(813179152525346414339585835102428211193689, 348449143727040986586495598010130648530944)), StrictGreaterThan(Symbol('a'), Add(Rational(24623430962648187265, 73786976294838206464), Mul(Integer(-1), Rational(1, 268435456), Pow(Integer(288230376151711743), Rational(1, 2))))))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_270(a:sympy.Rational):
	#(a + y**2 - z**2 + 606313352372301434184770344590508180225/5444517870735015415413993718908291383296 < 0) & (-a**2 + 24623430962648187265*a/36893488147419103232 - y**2 + 2*y + 15727240259832744812057210812134365969663/5444517870735015415413993718908291383296 > 0)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Pow(Symbol('y'), Integer(2)), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(606313352372301434184770344590508180225, 5444517870735015415413993718908291383296)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('a'), Integer(2))), Mul(Rational(24623430962648187265, 36893488147419103232), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Mul(Integer(2), Symbol('y')), Rational(15727240259832744812057210812134365969663, 5444517870735015415413993718908291383296)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_271(a:sympy.Rational):
	#(a - z**2 + 6050831182542497717853286941518620410625/5444517870735015415413993718908291383296 < 0) & (36893488147419103232*a**2 - 24623430962648187265*a < 21171758130567760151913340805128333933823/147573952589676412928)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(6050831182542497717853286941518620410625, 5444517870735015415413993718908291383296)), Integer(0)), StrictLessThan(Add(Mul(Integer(36893488147419103232), Pow(Symbol('a'), Integer(2))), Mul(Integer(-1), Integer(24623430962648187265), Symbol('a'))), Rational(21171758130567760151913340805128333933823, 147573952589676412928)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_272(a:sympy.Rational):
	#(a < 813179152525346414339585835102428211193689/348449143727040986586495598010130648530944) & (a > 24623430962648187265/73786976294838206464 - sqrt(288230376151711743)/268435456)

	pre_cond = And(StrictLessThan(Symbol('a'), Rational(813179152525346414339585835102428211193689, 348449143727040986586495598010130648530944)), StrictGreaterThan(Symbol('a'), Add(Rational(24623430962648187265, 73786976294838206464), Mul(Integer(-1), Rational(1, 268435456), Pow(Integer(288230376151711743), Rational(1, 2))))))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_273(a:sympy.Rational):
	#(a + y**2 - z**2 + 606313352372301434184770344590508180225/5444517870735015415413993718908291383296 < 0) & (-a**2 + 24623430962648187265*a/36893488147419103232 - y**2 + 2*y + 15727240259832744812057210812134365969663/5444517870735015415413993718908291383296 > 0)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Pow(Symbol('y'), Integer(2)), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(606313352372301434184770344590508180225, 5444517870735015415413993718908291383296)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('a'), Integer(2))), Mul(Rational(24623430962648187265, 36893488147419103232), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Mul(Integer(2), Symbol('y')), Rational(15727240259832744812057210812134365969663, 5444517870735015415413993718908291383296)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_274(a:sympy.Rational):
	#(a - z**2 + 6050831182542497717853286941518620410625/5444517870735015415413993718908291383296 < 0) & (36893488147419103232*a**2 - 24623430962648187265*a < 21171758130567760151913340805128333933823/147573952589676412928)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(6050831182542497717853286941518620410625, 5444517870735015415413993718908291383296)), Integer(0)), StrictLessThan(Add(Mul(Integer(36893488147419103232), Pow(Symbol('a'), Integer(2))), Mul(Integer(-1), Integer(24623430962648187265), Symbol('a'))), Rational(21171758130567760151913340805128333933823, 147573952589676412928)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_275(a:sympy.Rational):
	#(a < 813179152525346414339585835102428211193689/348449143727040986586495598010130648530944) & (a > 24623430962648187265/73786976294838206464 - sqrt(288230376151711743)/268435456)

	pre_cond = And(StrictLessThan(Symbol('a'), Rational(813179152525346414339585835102428211193689, 348449143727040986586495598010130648530944)), StrictGreaterThan(Symbol('a'), Add(Rational(24623430962648187265, 73786976294838206464), Mul(Integer(-1), Rational(1, 268435456), Pow(Integer(288230376151711743), Rational(1, 2))))))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_276(a:sympy.Rational):
	#(a + y**2 - z**2 + 606313352372301434184770344590508180225/5444517870735015415413993718908291383296 < 0) & (-a**2 + 24623430962648187265*a/36893488147419103232 - y**2 + 2*y + 15727240259832744812057210812134365969663/5444517870735015415413993718908291383296 > 0)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Pow(Symbol('y'), Integer(2)), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(606313352372301434184770344590508180225, 5444517870735015415413993718908291383296)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('a'), Integer(2))), Mul(Rational(24623430962648187265, 36893488147419103232), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Mul(Integer(2), Symbol('y')), Rational(15727240259832744812057210812134365969663, 5444517870735015415413993718908291383296)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_277(a:sympy.Rational):
	#(a - z**2 + 6050831182542497717853286941518620410625/5444517870735015415413993718908291383296 < 0) & (36893488147419103232*a**2 - 24623430962648187265*a < 21171758130567760151913340805128333933823/147573952589676412928)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(6050831182542497717853286941518620410625, 5444517870735015415413993718908291383296)), Integer(0)), StrictLessThan(Add(Mul(Integer(36893488147419103232), Pow(Symbol('a'), Integer(2))), Mul(Integer(-1), Integer(24623430962648187265), Symbol('a'))), Rational(21171758130567760151913340805128333933823, 147573952589676412928)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_278(a:sympy.Rational):
	#(a < 813179152525346414339585835102428211193689/348449143727040986586495598010130648530944) & (a > 24623430962648187265/73786976294838206464 - sqrt(288230376151711743)/268435456)

	pre_cond = And(StrictLessThan(Symbol('a'), Rational(813179152525346414339585835102428211193689, 348449143727040986586495598010130648530944)), StrictGreaterThan(Symbol('a'), Add(Rational(24623430962648187265, 73786976294838206464), Mul(Integer(-1), Rational(1, 268435456), Pow(Integer(288230376151711743), Rational(1, 2))))))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_279(a:sympy.Rational):
	#(a + y**2 - z**2 + 606313352372301434184770344590508180225/5444517870735015415413993718908291383296 < 0) & (-a**2 + 24623430962648187265*a/36893488147419103232 - y**2 + 2*y + 15727240259832744812057210812134365969663/5444517870735015415413993718908291383296 > 0)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Pow(Symbol('y'), Integer(2)), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(606313352372301434184770344590508180225, 5444517870735015415413993718908291383296)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('a'), Integer(2))), Mul(Rational(24623430962648187265, 36893488147419103232), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Mul(Integer(2), Symbol('y')), Rational(15727240259832744812057210812134365969663, 5444517870735015415413993718908291383296)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_280(a:sympy.Rational):
	#(a - z**2 + 6050831182542497717853286941518620410625/5444517870735015415413993718908291383296 < 0) & (36893488147419103232*a**2 - 24623430962648187265*a < 21171758130567760151913340805128333933823/147573952589676412928)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(6050831182542497717853286941518620410625, 5444517870735015415413993718908291383296)), Integer(0)), StrictLessThan(Add(Mul(Integer(36893488147419103232), Pow(Symbol('a'), Integer(2))), Mul(Integer(-1), Integer(24623430962648187265), Symbol('a'))), Rational(21171758130567760151913340805128333933823, 147573952589676412928)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_281(a:sympy.Rational):
	#(a < 813179152525346414339585835102428211193689/348449143727040986586495598010130648530944) & (a > 24623430962648187265/73786976294838206464 - sqrt(288230376151711743)/268435456)

	pre_cond = And(StrictLessThan(Symbol('a'), Rational(813179152525346414339585835102428211193689, 348449143727040986586495598010130648530944)), StrictGreaterThan(Symbol('a'), Add(Rational(24623430962648187265, 73786976294838206464), Mul(Integer(-1), Rational(1, 268435456), Pow(Integer(288230376151711743), Rational(1, 2))))))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_282(a:sympy.Rational):
	#(a + y**2 - z**2 + 606313352372301434184770344590508180225/5444517870735015415413993718908291383296 < 0) & (-a**2 + 24623430962648187265*a/36893488147419103232 - y**2 + 2*y + 15727240259832744812057210812134365969663/5444517870735015415413993718908291383296 > 0)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Pow(Symbol('y'), Integer(2)), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(606313352372301434184770344590508180225, 5444517870735015415413993718908291383296)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('a'), Integer(2))), Mul(Rational(24623430962648187265, 36893488147419103232), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Mul(Integer(2), Symbol('y')), Rational(15727240259832744812057210812134365969663, 5444517870735015415413993718908291383296)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_283(a:sympy.Rational):
	#(a - z**2 + 6050831182542497717853286941518620410625/5444517870735015415413993718908291383296 < 0) & (36893488147419103232*a**2 - 24623430962648187265*a < 21171758130567760151913340805128333933823/147573952589676412928)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(6050831182542497717853286941518620410625, 5444517870735015415413993718908291383296)), Integer(0)), StrictLessThan(Add(Mul(Integer(36893488147419103232), Pow(Symbol('a'), Integer(2))), Mul(Integer(-1), Integer(24623430962648187265), Symbol('a'))), Rational(21171758130567760151913340805128333933823, 147573952589676412928)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_284(a:sympy.Rational):
	#(a < 813179152525346414339585835102428211193689/348449143727040986586495598010130648530944) & (a > 24623430962648187265/73786976294838206464 - sqrt(288230376151711743)/268435456)

	pre_cond = And(StrictLessThan(Symbol('a'), Rational(813179152525346414339585835102428211193689, 348449143727040986586495598010130648530944)), StrictGreaterThan(Symbol('a'), Add(Rational(24623430962648187265, 73786976294838206464), Mul(Integer(-1), Rational(1, 268435456), Pow(Integer(288230376151711743), Rational(1, 2))))))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_285(a:sympy.Rational):
	#(a + y**2 - z**2 + 606313352372301434184770344590508180225/5444517870735015415413993718908291383296 < 0) & (-a**2 + 24623430962648187265*a/36893488147419103232 - y**2 + 2*y + 15727240259832744812057210812134365969663/5444517870735015415413993718908291383296 > 0)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Pow(Symbol('y'), Integer(2)), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(606313352372301434184770344590508180225, 5444517870735015415413993718908291383296)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('a'), Integer(2))), Mul(Rational(24623430962648187265, 36893488147419103232), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Mul(Integer(2), Symbol('y')), Rational(15727240259832744812057210812134365969663, 5444517870735015415413993718908291383296)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_286(a:sympy.Rational):
	#(a - z**2 + 6050831182542497717853286941518620410625/5444517870735015415413993718908291383296 < 0) & (36893488147419103232*a**2 - 24623430962648187265*a < 21171758130567760151913340805128333933823/147573952589676412928)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(6050831182542497717853286941518620410625, 5444517870735015415413993718908291383296)), Integer(0)), StrictLessThan(Add(Mul(Integer(36893488147419103232), Pow(Symbol('a'), Integer(2))), Mul(Integer(-1), Integer(24623430962648187265), Symbol('a'))), Rational(21171758130567760151913340805128333933823, 147573952589676412928)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_287(a:sympy.Rational):
	#(a < 813179152525346414339585835102428211193689/348449143727040986586495598010130648530944) & (a > 24623430962648187265/73786976294838206464 - sqrt(288230376151711743)/268435456)

	pre_cond = And(StrictLessThan(Symbol('a'), Rational(813179152525346414339585835102428211193689, 348449143727040986586495598010130648530944)), StrictGreaterThan(Symbol('a'), Add(Rational(24623430962648187265, 73786976294838206464), Mul(Integer(-1), Rational(1, 268435456), Pow(Integer(288230376151711743), Rational(1, 2))))))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_288(a:sympy.Rational):
	#(a + y**2 - z**2 + 606313352372301434184770344590508180225/5444517870735015415413993718908291383296 < 0) & (-a**2 + 24623430962648187265*a/36893488147419103232 - y**2 + 2*y + 15727240259832744812057210812134365969663/5444517870735015415413993718908291383296 > 0)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Pow(Symbol('y'), Integer(2)), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(606313352372301434184770344590508180225, 5444517870735015415413993718908291383296)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('a'), Integer(2))), Mul(Rational(24623430962648187265, 36893488147419103232), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Mul(Integer(2), Symbol('y')), Rational(15727240259832744812057210812134365969663, 5444517870735015415413993718908291383296)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_289(a:sympy.Rational):
	#(a - z**2 + 6050831182542497717853286941518620410625/5444517870735015415413993718908291383296 < 0) & (36893488147419103232*a**2 - 24623430962648187265*a < 21171758130567760151913340805128333933823/147573952589676412928)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(6050831182542497717853286941518620410625, 5444517870735015415413993718908291383296)), Integer(0)), StrictLessThan(Add(Mul(Integer(36893488147419103232), Pow(Symbol('a'), Integer(2))), Mul(Integer(-1), Integer(24623430962648187265), Symbol('a'))), Rational(21171758130567760151913340805128333933823, 147573952589676412928)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_290(a:sympy.Rational):
	#(a < 813179152525346414339585835102428211193689/348449143727040986586495598010130648530944) & (a > 24623430962648187265/73786976294838206464 - sqrt(288230376151711743)/268435456)

	pre_cond = And(StrictLessThan(Symbol('a'), Rational(813179152525346414339585835102428211193689, 348449143727040986586495598010130648530944)), StrictGreaterThan(Symbol('a'), Add(Rational(24623430962648187265, 73786976294838206464), Mul(Integer(-1), Rational(1, 268435456), Pow(Integer(288230376151711743), Rational(1, 2))))))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_291(a:sympy.Rational):
	#(a + y**2 - z**2 + 606313352372301434184770344590508180225/5444517870735015415413993718908291383296 < 0) & (-a**2 + 24623430962648187265*a/36893488147419103232 - y**2 + 2*y + 15727240259832744812057210812134365969663/5444517870735015415413993718908291383296 > 0)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Pow(Symbol('y'), Integer(2)), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(606313352372301434184770344590508180225, 5444517870735015415413993718908291383296)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('a'), Integer(2))), Mul(Rational(24623430962648187265, 36893488147419103232), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Mul(Integer(2), Symbol('y')), Rational(15727240259832744812057210812134365969663, 5444517870735015415413993718908291383296)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_292(a:sympy.Rational):
	#(a - z**2 + 6050831182542497717853286941518620410625/5444517870735015415413993718908291383296 < 0) & (36893488147419103232*a**2 - 24623430962648187265*a < 21171758130567760151913340805128333933823/147573952589676412928)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(6050831182542497717853286941518620410625, 5444517870735015415413993718908291383296)), Integer(0)), StrictLessThan(Add(Mul(Integer(36893488147419103232), Pow(Symbol('a'), Integer(2))), Mul(Integer(-1), Integer(24623430962648187265), Symbol('a'))), Rational(21171758130567760151913340805128333933823, 147573952589676412928)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_293(a:sympy.Rational):
	#(a < 813179152525346414339585835102428211193689/348449143727040986586495598010130648530944) & (a > 24623430962648187265/73786976294838206464 - sqrt(288230376151711743)/268435456)

	pre_cond = And(StrictLessThan(Symbol('a'), Rational(813179152525346414339585835102428211193689, 348449143727040986586495598010130648530944)), StrictGreaterThan(Symbol('a'), Add(Rational(24623430962648187265, 73786976294838206464), Mul(Integer(-1), Rational(1, 268435456), Pow(Integer(288230376151711743), Rational(1, 2))))))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_294(a:sympy.Rational):
	#(a + y**2 - z**2 + 606313352372301434184770344590508180225/5444517870735015415413993718908291383296 < 0) & (-a**2 + 24623430962648187265*a/36893488147419103232 - y**2 + 2*y + 15727240259832744812057210812134365969663/5444517870735015415413993718908291383296 > 0)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Pow(Symbol('y'), Integer(2)), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(606313352372301434184770344590508180225, 5444517870735015415413993718908291383296)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('a'), Integer(2))), Mul(Rational(24623430962648187265, 36893488147419103232), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Mul(Integer(2), Symbol('y')), Rational(15727240259832744812057210812134365969663, 5444517870735015415413993718908291383296)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_295(a:sympy.Rational):
	#(a - z**2 + 6050831182542497717853286941518620410625/5444517870735015415413993718908291383296 < 0) & (36893488147419103232*a**2 - 24623430962648187265*a < 21171758130567760151913340805128333933823/147573952589676412928)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(6050831182542497717853286941518620410625, 5444517870735015415413993718908291383296)), Integer(0)), StrictLessThan(Add(Mul(Integer(36893488147419103232), Pow(Symbol('a'), Integer(2))), Mul(Integer(-1), Integer(24623430962648187265), Symbol('a'))), Rational(21171758130567760151913340805128333933823, 147573952589676412928)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_296(a:sympy.Rational):
	#(a < 813179152525346414339585835102428211193689/348449143727040986586495598010130648530944) & (a > 24623430962648187265/73786976294838206464 - sqrt(288230376151711743)/268435456)

	pre_cond = And(StrictLessThan(Symbol('a'), Rational(813179152525346414339585835102428211193689, 348449143727040986586495598010130648530944)), StrictGreaterThan(Symbol('a'), Add(Rational(24623430962648187265, 73786976294838206464), Mul(Integer(-1), Rational(1, 268435456), Pow(Integer(288230376151711743), Rational(1, 2))))))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_297(a:sympy.Rational):
	#(a + y**2 - z**2 + 606313352372301434184770344590508180225/5444517870735015415413993718908291383296 < 0) & (-a**2 + 24623430962648187265*a/36893488147419103232 - y**2 + 2*y + 15727240259832744812057210812134365969663/5444517870735015415413993718908291383296 > 0)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Pow(Symbol('y'), Integer(2)), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(606313352372301434184770344590508180225, 5444517870735015415413993718908291383296)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('a'), Integer(2))), Mul(Rational(24623430962648187265, 36893488147419103232), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Mul(Integer(2), Symbol('y')), Rational(15727240259832744812057210812134365969663, 5444517870735015415413993718908291383296)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_298(a:sympy.Rational):
	#(a - z**2 + 6050831182542497717853286941518620410625/5444517870735015415413993718908291383296 < 0) & (36893488147419103232*a**2 - 24623430962648187265*a < 21171758130567760151913340805128333933823/147573952589676412928)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(6050831182542497717853286941518620410625, 5444517870735015415413993718908291383296)), Integer(0)), StrictLessThan(Add(Mul(Integer(36893488147419103232), Pow(Symbol('a'), Integer(2))), Mul(Integer(-1), Integer(24623430962648187265), Symbol('a'))), Rational(21171758130567760151913340805128333933823, 147573952589676412928)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_299(a:sympy.Rational):
	#(a < 813179152525346414339585835102428211193689/348449143727040986586495598010130648530944) & (a > 24623430962648187265/73786976294838206464 - sqrt(288230376151711743)/268435456)

	pre_cond = And(StrictLessThan(Symbol('a'), Rational(813179152525346414339585835102428211193689, 348449143727040986586495598010130648530944)), StrictGreaterThan(Symbol('a'), Add(Rational(24623430962648187265, 73786976294838206464), Mul(Integer(-1), Rational(1, 268435456), Pow(Integer(288230376151711743), Rational(1, 2))))))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_300(a:sympy.Rational):
	#(a + y**2 - z**2 + 606313352372301434184770344590508180225/5444517870735015415413993718908291383296 < 0) & (-a**2 + 24623430962648187265*a/36893488147419103232 - y**2 + 2*y + 15727240259832744812057210812134365969663/5444517870735015415413993718908291383296 > 0)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Pow(Symbol('y'), Integer(2)), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(606313352372301434184770344590508180225, 5444517870735015415413993718908291383296)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('a'), Integer(2))), Mul(Rational(24623430962648187265, 36893488147419103232), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Mul(Integer(2), Symbol('y')), Rational(15727240259832744812057210812134365969663, 5444517870735015415413993718908291383296)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_301(a:sympy.Rational):
	#(a - z**2 + 6050831182542497717853286941518620410625/5444517870735015415413993718908291383296 < 0) & (36893488147419103232*a**2 - 24623430962648187265*a < 21171758130567760151913340805128333933823/147573952589676412928)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(6050831182542497717853286941518620410625, 5444517870735015415413993718908291383296)), Integer(0)), StrictLessThan(Add(Mul(Integer(36893488147419103232), Pow(Symbol('a'), Integer(2))), Mul(Integer(-1), Integer(24623430962648187265), Symbol('a'))), Rational(21171758130567760151913340805128333933823, 147573952589676412928)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_302(a:sympy.Rational):
	#(a < 813179152525346414339585835102428211193689/348449143727040986586495598010130648530944) & (a > 24623430962648187265/73786976294838206464 - sqrt(288230376151711743)/268435456)

	pre_cond = And(StrictLessThan(Symbol('a'), Rational(813179152525346414339585835102428211193689, 348449143727040986586495598010130648530944)), StrictGreaterThan(Symbol('a'), Add(Rational(24623430962648187265, 73786976294838206464), Mul(Integer(-1), Rational(1, 268435456), Pow(Integer(288230376151711743), Rational(1, 2))))))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_303(a:sympy.Rational):
	#(a + y**2 - z**2 + 606313352372301434184770344590508180225/5444517870735015415413993718908291383296 < 0) & (-a**2 + 24623430962648187265*a/36893488147419103232 - y**2 + 2*y + 15727240259832744812057210812134365969663/5444517870735015415413993718908291383296 > 0)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Pow(Symbol('y'), Integer(2)), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(606313352372301434184770344590508180225, 5444517870735015415413993718908291383296)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('a'), Integer(2))), Mul(Rational(24623430962648187265, 36893488147419103232), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Mul(Integer(2), Symbol('y')), Rational(15727240259832744812057210812134365969663, 5444517870735015415413993718908291383296)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_304(a:sympy.Rational):
	#(a - z**2 + 6050831182542497717853286941518620410625/5444517870735015415413993718908291383296 < 0) & (36893488147419103232*a**2 - 24623430962648187265*a < 21171758130567760151913340805128333933823/147573952589676412928)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(6050831182542497717853286941518620410625, 5444517870735015415413993718908291383296)), Integer(0)), StrictLessThan(Add(Mul(Integer(36893488147419103232), Pow(Symbol('a'), Integer(2))), Mul(Integer(-1), Integer(24623430962648187265), Symbol('a'))), Rational(21171758130567760151913340805128333933823, 147573952589676412928)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_305(a:sympy.Rational):
	#(a < 813179152525346414339585835102428211193689/348449143727040986586495598010130648530944) & (a > 24623430962648187265/73786976294838206464 - sqrt(288230376151711743)/268435456)

	pre_cond = And(StrictLessThan(Symbol('a'), Rational(813179152525346414339585835102428211193689, 348449143727040986586495598010130648530944)), StrictGreaterThan(Symbol('a'), Add(Rational(24623430962648187265, 73786976294838206464), Mul(Integer(-1), Rational(1, 268435456), Pow(Integer(288230376151711743), Rational(1, 2))))))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_306(a:sympy.Rational):
	#(a + y**2 - z**2 + 606313352372301434184770344590508180225/5444517870735015415413993718908291383296 < 0) & (-a**2 + 24623430962648187265*a/36893488147419103232 - y**2 + 2*y + 15727240259832744812057210812134365969663/5444517870735015415413993718908291383296 > 0)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Pow(Symbol('y'), Integer(2)), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(606313352372301434184770344590508180225, 5444517870735015415413993718908291383296)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('a'), Integer(2))), Mul(Rational(24623430962648187265, 36893488147419103232), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Mul(Integer(2), Symbol('y')), Rational(15727240259832744812057210812134365969663, 5444517870735015415413993718908291383296)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_307(a:sympy.Rational):
	#(a - z**2 + 6050831182542497717853286941518620410625/5444517870735015415413993718908291383296 < 0) & (36893488147419103232*a**2 - 24623430962648187265*a < 21171758130567760151913340805128333933823/147573952589676412928)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(6050831182542497717853286941518620410625, 5444517870735015415413993718908291383296)), Integer(0)), StrictLessThan(Add(Mul(Integer(36893488147419103232), Pow(Symbol('a'), Integer(2))), Mul(Integer(-1), Integer(24623430962648187265), Symbol('a'))), Rational(21171758130567760151913340805128333933823, 147573952589676412928)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_308(a:sympy.Rational):
	#(a < 813179152525346414339585835102428211193689/348449143727040986586495598010130648530944) & (a > 24623430962648187265/73786976294838206464 - sqrt(288230376151711743)/268435456)

	pre_cond = And(StrictLessThan(Symbol('a'), Rational(813179152525346414339585835102428211193689, 348449143727040986586495598010130648530944)), StrictGreaterThan(Symbol('a'), Add(Rational(24623430962648187265, 73786976294838206464), Mul(Integer(-1), Rational(1, 268435456), Pow(Integer(288230376151711743), Rational(1, 2))))))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_309(a:sympy.Rational):
	#(a + y**2 - z**2 + 606313352372301434184770344590508180225/5444517870735015415413993718908291383296 < 0) & (-a**2 + 24623430962648187265*a/36893488147419103232 - y**2 + 2*y + 15727240259832744812057210812134365969663/5444517870735015415413993718908291383296 > 0)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Pow(Symbol('y'), Integer(2)), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(606313352372301434184770344590508180225, 5444517870735015415413993718908291383296)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('a'), Integer(2))), Mul(Rational(24623430962648187265, 36893488147419103232), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Mul(Integer(2), Symbol('y')), Rational(15727240259832744812057210812134365969663, 5444517870735015415413993718908291383296)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_310(a:sympy.Rational):
	#(a - z**2 + 6050831182542497717853286941518620410625/5444517870735015415413993718908291383296 < 0) & (36893488147419103232*a**2 - 24623430962648187265*a < 21171758130567760151913340805128333933823/147573952589676412928)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(6050831182542497717853286941518620410625, 5444517870735015415413993718908291383296)), Integer(0)), StrictLessThan(Add(Mul(Integer(36893488147419103232), Pow(Symbol('a'), Integer(2))), Mul(Integer(-1), Integer(24623430962648187265), Symbol('a'))), Rational(21171758130567760151913340805128333933823, 147573952589676412928)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_311(a:sympy.Rational):
	#(a < 813179152525346414339585835102428211193689/348449143727040986586495598010130648530944) & (a > 24623430962648187265/73786976294838206464 - sqrt(288230376151711743)/268435456)

	pre_cond = And(StrictLessThan(Symbol('a'), Rational(813179152525346414339585835102428211193689, 348449143727040986586495598010130648530944)), StrictGreaterThan(Symbol('a'), Add(Rational(24623430962648187265, 73786976294838206464), Mul(Integer(-1), Rational(1, 268435456), Pow(Integer(288230376151711743), Rational(1, 2))))))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_312(a:sympy.Rational):
	#(a + y**2 - z**2 + 606313352372301434184770344590508180225/5444517870735015415413993718908291383296 < 0) & (-a**2 + 24623430962648187265*a/36893488147419103232 - y**2 + 2*y + 15727240259832744812057210812134365969663/5444517870735015415413993718908291383296 > 0)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Pow(Symbol('y'), Integer(2)), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(606313352372301434184770344590508180225, 5444517870735015415413993718908291383296)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('a'), Integer(2))), Mul(Rational(24623430962648187265, 36893488147419103232), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Mul(Integer(2), Symbol('y')), Rational(15727240259832744812057210812134365969663, 5444517870735015415413993718908291383296)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_313(a:sympy.Rational):
	#(a - z**2 + 6050831182542497717853286941518620410625/5444517870735015415413993718908291383296 < 0) & (36893488147419103232*a**2 - 24623430962648187265*a < 21171758130567760151913340805128333933823/147573952589676412928)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(6050831182542497717853286941518620410625, 5444517870735015415413993718908291383296)), Integer(0)), StrictLessThan(Add(Mul(Integer(36893488147419103232), Pow(Symbol('a'), Integer(2))), Mul(Integer(-1), Integer(24623430962648187265), Symbol('a'))), Rational(21171758130567760151913340805128333933823, 147573952589676412928)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_314(a:sympy.Rational):
	#(a < 813179152525346414339585835102428211193689/348449143727040986586495598010130648530944) & (a > 24623430962648187265/73786976294838206464 - sqrt(288230376151711743)/268435456)

	pre_cond = And(StrictLessThan(Symbol('a'), Rational(813179152525346414339585835102428211193689, 348449143727040986586495598010130648530944)), StrictGreaterThan(Symbol('a'), Add(Rational(24623430962648187265, 73786976294838206464), Mul(Integer(-1), Rational(1, 268435456), Pow(Integer(288230376151711743), Rational(1, 2))))))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_315(a:sympy.Rational):
	#(a + y**2 - z**2 + 606313352372301434184770344590508180225/5444517870735015415413993718908291383296 < 0) & (-a**2 + 24623430962648187265*a/36893488147419103232 - y**2 + 2*y + 15727240259832744812057210812134365969663/5444517870735015415413993718908291383296 > 0)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Pow(Symbol('y'), Integer(2)), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(606313352372301434184770344590508180225, 5444517870735015415413993718908291383296)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('a'), Integer(2))), Mul(Rational(24623430962648187265, 36893488147419103232), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Mul(Integer(2), Symbol('y')), Rational(15727240259832744812057210812134365969663, 5444517870735015415413993718908291383296)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_316(a:sympy.Rational):
	#(a - z**2 + 6050831182542497717853286941518620410625/5444517870735015415413993718908291383296 < 0) & (36893488147419103232*a**2 - 24623430962648187265*a < 21171758130567760151913340805128333933823/147573952589676412928)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(6050831182542497717853286941518620410625, 5444517870735015415413993718908291383296)), Integer(0)), StrictLessThan(Add(Mul(Integer(36893488147419103232), Pow(Symbol('a'), Integer(2))), Mul(Integer(-1), Integer(24623430962648187265), Symbol('a'))), Rational(21171758130567760151913340805128333933823, 147573952589676412928)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_317(a:sympy.Rational):
	#(a < 813179152525346414339585835102428211193689/348449143727040986586495598010130648530944) & (a > 24623430962648187265/73786976294838206464 - sqrt(288230376151711743)/268435456)

	pre_cond = And(StrictLessThan(Symbol('a'), Rational(813179152525346414339585835102428211193689, 348449143727040986586495598010130648530944)), StrictGreaterThan(Symbol('a'), Add(Rational(24623430962648187265, 73786976294838206464), Mul(Integer(-1), Rational(1, 268435456), Pow(Integer(288230376151711743), Rational(1, 2))))))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_318(a:sympy.Rational):
	#(a + y**2 - z**2 + 606313352372301434184770344590508180225/5444517870735015415413993718908291383296 < 0) & (-a**2 + 24623430962648187265*a/36893488147419103232 - y**2 + 2*y + 15727240259832744812057210812134365969663/5444517870735015415413993718908291383296 > 0)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Pow(Symbol('y'), Integer(2)), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(606313352372301434184770344590508180225, 5444517870735015415413993718908291383296)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('a'), Integer(2))), Mul(Rational(24623430962648187265, 36893488147419103232), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Mul(Integer(2), Symbol('y')), Rational(15727240259832744812057210812134365969663, 5444517870735015415413993718908291383296)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_319(a:sympy.Rational):
	#(a - z**2 + 6050831182542497717853286941518620410625/5444517870735015415413993718908291383296 < 0) & (36893488147419103232*a**2 - 24623430962648187265*a < 21171758130567760151913340805128333933823/147573952589676412928)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(6050831182542497717853286941518620410625, 5444517870735015415413993718908291383296)), Integer(0)), StrictLessThan(Add(Mul(Integer(36893488147419103232), Pow(Symbol('a'), Integer(2))), Mul(Integer(-1), Integer(24623430962648187265), Symbol('a'))), Rational(21171758130567760151913340805128333933823, 147573952589676412928)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_320(a:sympy.Rational):
	#(a < 813179152525346414339585835102428211193689/348449143727040986586495598010130648530944) & (a > 24623430962648187265/73786976294838206464 - sqrt(288230376151711743)/268435456)

	pre_cond = And(StrictLessThan(Symbol('a'), Rational(813179152525346414339585835102428211193689, 348449143727040986586495598010130648530944)), StrictGreaterThan(Symbol('a'), Add(Rational(24623430962648187265, 73786976294838206464), Mul(Integer(-1), Rational(1, 268435456), Pow(Integer(288230376151711743), Rational(1, 2))))))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_321(a:sympy.Rational):
	#(a + y**2 - z**2 + 606313352372301434184770344590508180225/5444517870735015415413993718908291383296 < 0) & (-a**2 + 24623430962648187265*a/36893488147419103232 - y**2 + 2*y + 15727240259832744812057210812134365969663/5444517870735015415413993718908291383296 > 0)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Pow(Symbol('y'), Integer(2)), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(606313352372301434184770344590508180225, 5444517870735015415413993718908291383296)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('a'), Integer(2))), Mul(Rational(24623430962648187265, 36893488147419103232), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Mul(Integer(2), Symbol('y')), Rational(15727240259832744812057210812134365969663, 5444517870735015415413993718908291383296)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_322(a:sympy.Rational):
	#(a - z**2 + 6050831182542497717853286941518620410625/5444517870735015415413993718908291383296 < 0) & (36893488147419103232*a**2 - 24623430962648187265*a < 21171758130567760151913340805128333933823/147573952589676412928)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(6050831182542497717853286941518620410625, 5444517870735015415413993718908291383296)), Integer(0)), StrictLessThan(Add(Mul(Integer(36893488147419103232), Pow(Symbol('a'), Integer(2))), Mul(Integer(-1), Integer(24623430962648187265), Symbol('a'))), Rational(21171758130567760151913340805128333933823, 147573952589676412928)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_323(a:sympy.Rational):
	#(a < 813179152525346414339585835102428211193689/348449143727040986586495598010130648530944) & (a > 24623430962648187265/73786976294838206464 - sqrt(288230376151711743)/268435456)

	pre_cond = And(StrictLessThan(Symbol('a'), Rational(813179152525346414339585835102428211193689, 348449143727040986586495598010130648530944)), StrictGreaterThan(Symbol('a'), Add(Rational(24623430962648187265, 73786976294838206464), Mul(Integer(-1), Rational(1, 268435456), Pow(Integer(288230376151711743), Rational(1, 2))))))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_324(a:sympy.Rational):
	#(a + y**2 - z**2 + 606313352372301434184770344590508180225/5444517870735015415413993718908291383296 < 0) & (-a**2 + 24623430962648187265*a/36893488147419103232 - y**2 + 2*y + 15727240259832744812057210812134365969663/5444517870735015415413993718908291383296 > 0)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Pow(Symbol('y'), Integer(2)), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(606313352372301434184770344590508180225, 5444517870735015415413993718908291383296)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('a'), Integer(2))), Mul(Rational(24623430962648187265, 36893488147419103232), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Mul(Integer(2), Symbol('y')), Rational(15727240259832744812057210812134365969663, 5444517870735015415413993718908291383296)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_325(a:sympy.Rational):
	#(a - z**2 + 6050831182542497717853286941518620410625/5444517870735015415413993718908291383296 < 0) & (36893488147419103232*a**2 - 24623430962648187265*a < 21171758130567760151913340805128333933823/147573952589676412928)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(6050831182542497717853286941518620410625, 5444517870735015415413993718908291383296)), Integer(0)), StrictLessThan(Add(Mul(Integer(36893488147419103232), Pow(Symbol('a'), Integer(2))), Mul(Integer(-1), Integer(24623430962648187265), Symbol('a'))), Rational(21171758130567760151913340805128333933823, 147573952589676412928)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_326(a:sympy.Rational):
	#(a < 813179152525346414339585835102428211193689/348449143727040986586495598010130648530944) & (a > 24623430962648187265/73786976294838206464 - sqrt(288230376151711743)/268435456)

	pre_cond = And(StrictLessThan(Symbol('a'), Rational(813179152525346414339585835102428211193689, 348449143727040986586495598010130648530944)), StrictGreaterThan(Symbol('a'), Add(Rational(24623430962648187265, 73786976294838206464), Mul(Integer(-1), Rational(1, 268435456), Pow(Integer(288230376151711743), Rational(1, 2))))))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_327(a:sympy.Rational):
	#(a + y**2 - z**2 + 606313352372301434184770344590508180225/5444517870735015415413993718908291383296 < 0) & (-a**2 + 24623430962648187265*a/36893488147419103232 - y**2 + 2*y + 15727240259832744812057210812134365969663/5444517870735015415413993718908291383296 > 0)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Pow(Symbol('y'), Integer(2)), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(606313352372301434184770344590508180225, 5444517870735015415413993718908291383296)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('a'), Integer(2))), Mul(Rational(24623430962648187265, 36893488147419103232), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Mul(Integer(2), Symbol('y')), Rational(15727240259832744812057210812134365969663, 5444517870735015415413993718908291383296)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_328(a:sympy.Rational):
	#(a - z**2 + 6050831182542497717853286941518620410625/5444517870735015415413993718908291383296 < 0) & (36893488147419103232*a**2 - 24623430962648187265*a < 21171758130567760151913340805128333933823/147573952589676412928)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(6050831182542497717853286941518620410625, 5444517870735015415413993718908291383296)), Integer(0)), StrictLessThan(Add(Mul(Integer(36893488147419103232), Pow(Symbol('a'), Integer(2))), Mul(Integer(-1), Integer(24623430962648187265), Symbol('a'))), Rational(21171758130567760151913340805128333933823, 147573952589676412928)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_329(a:sympy.Rational):
	#(a < 813179152525346414339585835102428211193689/348449143727040986586495598010130648530944) & (a > 24623430962648187265/73786976294838206464 - sqrt(288230376151711743)/268435456)

	pre_cond = And(StrictLessThan(Symbol('a'), Rational(813179152525346414339585835102428211193689, 348449143727040986586495598010130648530944)), StrictGreaterThan(Symbol('a'), Add(Rational(24623430962648187265, 73786976294838206464), Mul(Integer(-1), Rational(1, 268435456), Pow(Integer(288230376151711743), Rational(1, 2))))))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_330(a:sympy.Rational):
	#(a + y**2 - z**2 + 606313352372301434184770344590508180225/5444517870735015415413993718908291383296 < 0) & (-a**2 + 24623430962648187265*a/36893488147419103232 - y**2 + 2*y + 15727240259832744812057210812134365969663/5444517870735015415413993718908291383296 > 0)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Pow(Symbol('y'), Integer(2)), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(606313352372301434184770344590508180225, 5444517870735015415413993718908291383296)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('a'), Integer(2))), Mul(Rational(24623430962648187265, 36893488147419103232), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Mul(Integer(2), Symbol('y')), Rational(15727240259832744812057210812134365969663, 5444517870735015415413993718908291383296)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_331(a:sympy.Rational):
	#(a - z**2 + 6050831182542497717853286941518620410625/5444517870735015415413993718908291383296 < 0) & (36893488147419103232*a**2 - 24623430962648187265*a < 21171758130567760151913340805128333933823/147573952589676412928)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(6050831182542497717853286941518620410625, 5444517870735015415413993718908291383296)), Integer(0)), StrictLessThan(Add(Mul(Integer(36893488147419103232), Pow(Symbol('a'), Integer(2))), Mul(Integer(-1), Integer(24623430962648187265), Symbol('a'))), Rational(21171758130567760151913340805128333933823, 147573952589676412928)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_332(a:sympy.Rational):
	#(a < 813179152525346414339585835102428211193689/348449143727040986586495598010130648530944) & (a > 24623430962648187265/73786976294838206464 - sqrt(288230376151711743)/268435456)

	pre_cond = And(StrictLessThan(Symbol('a'), Rational(813179152525346414339585835102428211193689, 348449143727040986586495598010130648530944)), StrictGreaterThan(Symbol('a'), Add(Rational(24623430962648187265, 73786976294838206464), Mul(Integer(-1), Rational(1, 268435456), Pow(Integer(288230376151711743), Rational(1, 2))))))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_333(a:sympy.Rational):
	#(a + y**2 - z**2 + 606313352372301434184770344590508180225/5444517870735015415413993718908291383296 < 0) & (-a**2 + 24623430962648187265*a/36893488147419103232 - y**2 + 2*y + 15727240259832744812057210812134365969663/5444517870735015415413993718908291383296 > 0)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Pow(Symbol('y'), Integer(2)), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(606313352372301434184770344590508180225, 5444517870735015415413993718908291383296)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('a'), Integer(2))), Mul(Rational(24623430962648187265, 36893488147419103232), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Mul(Integer(2), Symbol('y')), Rational(15727240259832744812057210812134365969663, 5444517870735015415413993718908291383296)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_334(a:sympy.Rational):
	#(a - z**2 + 6050831182542497717853286941518620410625/5444517870735015415413993718908291383296 < 0) & (36893488147419103232*a**2 - 24623430962648187265*a < 21171758130567760151913340805128333933823/147573952589676412928)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(6050831182542497717853286941518620410625, 5444517870735015415413993718908291383296)), Integer(0)), StrictLessThan(Add(Mul(Integer(36893488147419103232), Pow(Symbol('a'), Integer(2))), Mul(Integer(-1), Integer(24623430962648187265), Symbol('a'))), Rational(21171758130567760151913340805128333933823, 147573952589676412928)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_335(a:sympy.Rational):
	#(a < 813179152525346414339585835102428211193689/348449143727040986586495598010130648530944) & (a > 24623430962648187265/73786976294838206464 - sqrt(288230376151711743)/268435456)

	pre_cond = And(StrictLessThan(Symbol('a'), Rational(813179152525346414339585835102428211193689, 348449143727040986586495598010130648530944)), StrictGreaterThan(Symbol('a'), Add(Rational(24623430962648187265, 73786976294838206464), Mul(Integer(-1), Rational(1, 268435456), Pow(Integer(288230376151711743), Rational(1, 2))))))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_336(a:sympy.Rational):
	#(a + y**2 - z**2 + 606313352372301434184770344590508180225/5444517870735015415413993718908291383296 < 0) & (-a**2 + 24623430962648187265*a/36893488147419103232 - y**2 + 2*y + 15727240259832744812057210812134365969663/5444517870735015415413993718908291383296 > 0)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Pow(Symbol('y'), Integer(2)), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(606313352372301434184770344590508180225, 5444517870735015415413993718908291383296)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('a'), Integer(2))), Mul(Rational(24623430962648187265, 36893488147419103232), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Mul(Integer(2), Symbol('y')), Rational(15727240259832744812057210812134365969663, 5444517870735015415413993718908291383296)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_337(a:sympy.Rational):
	#(a - z**2 + 6050831182542497717853286941518620410625/5444517870735015415413993718908291383296 < 0) & (36893488147419103232*a**2 - 24623430962648187265*a < 21171758130567760151913340805128333933823/147573952589676412928)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(6050831182542497717853286941518620410625, 5444517870735015415413993718908291383296)), Integer(0)), StrictLessThan(Add(Mul(Integer(36893488147419103232), Pow(Symbol('a'), Integer(2))), Mul(Integer(-1), Integer(24623430962648187265), Symbol('a'))), Rational(21171758130567760151913340805128333933823, 147573952589676412928)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_338(a:sympy.Rational):
	#(a < 813179152525346414339585835102428211193689/348449143727040986586495598010130648530944) & (a > 24623430962648187265/73786976294838206464 - sqrt(288230376151711743)/268435456)

	pre_cond = And(StrictLessThan(Symbol('a'), Rational(813179152525346414339585835102428211193689, 348449143727040986586495598010130648530944)), StrictGreaterThan(Symbol('a'), Add(Rational(24623430962648187265, 73786976294838206464), Mul(Integer(-1), Rational(1, 268435456), Pow(Integer(288230376151711743), Rational(1, 2))))))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_339(a:sympy.Rational):
	#(a + y**2 - z**2 + 606313352372301434184770344590508180225/5444517870735015415413993718908291383296 < 0) & (-a**2 + 24623430962648187265*a/36893488147419103232 - y**2 + 2*y + 15727240259832744812057210812134365969663/5444517870735015415413993718908291383296 > 0)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Pow(Symbol('y'), Integer(2)), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(606313352372301434184770344590508180225, 5444517870735015415413993718908291383296)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('a'), Integer(2))), Mul(Rational(24623430962648187265, 36893488147419103232), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Mul(Integer(2), Symbol('y')), Rational(15727240259832744812057210812134365969663, 5444517870735015415413993718908291383296)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_340(a:sympy.Rational):
	#(a - z**2 + 6050831182542497717853286941518620410625/5444517870735015415413993718908291383296 < 0) & (36893488147419103232*a**2 - 24623430962648187265*a < 21171758130567760151913340805128333933823/147573952589676412928)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(6050831182542497717853286941518620410625, 5444517870735015415413993718908291383296)), Integer(0)), StrictLessThan(Add(Mul(Integer(36893488147419103232), Pow(Symbol('a'), Integer(2))), Mul(Integer(-1), Integer(24623430962648187265), Symbol('a'))), Rational(21171758130567760151913340805128333933823, 147573952589676412928)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_341(a:sympy.Rational):
	#(a < 813179152525346414339585835102428211193689/348449143727040986586495598010130648530944) & (a > 24623430962648187265/73786976294838206464 - sqrt(288230376151711743)/268435456)

	pre_cond = And(StrictLessThan(Symbol('a'), Rational(813179152525346414339585835102428211193689, 348449143727040986586495598010130648530944)), StrictGreaterThan(Symbol('a'), Add(Rational(24623430962648187265, 73786976294838206464), Mul(Integer(-1), Rational(1, 268435456), Pow(Integer(288230376151711743), Rational(1, 2))))))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_342(a:sympy.Rational):
	#(a + y**2 - z**2 + 606313352372301434184770344590508180225/5444517870735015415413993718908291383296 < 0) & (-a**2 + 24623430962648187265*a/36893488147419103232 - y**2 + 2*y + 15727240259832744812057210812134365969663/5444517870735015415413993718908291383296 > 0)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Pow(Symbol('y'), Integer(2)), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(606313352372301434184770344590508180225, 5444517870735015415413993718908291383296)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('a'), Integer(2))), Mul(Rational(24623430962648187265, 36893488147419103232), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Mul(Integer(2), Symbol('y')), Rational(15727240259832744812057210812134365969663, 5444517870735015415413993718908291383296)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_343(a:sympy.Rational):
	#(a - z**2 + 6050831182542497717853286941518620410625/5444517870735015415413993718908291383296 < 0) & (36893488147419103232*a**2 - 24623430962648187265*a < 21171758130567760151913340805128333933823/147573952589676412928)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(6050831182542497717853286941518620410625, 5444517870735015415413993718908291383296)), Integer(0)), StrictLessThan(Add(Mul(Integer(36893488147419103232), Pow(Symbol('a'), Integer(2))), Mul(Integer(-1), Integer(24623430962648187265), Symbol('a'))), Rational(21171758130567760151913340805128333933823, 147573952589676412928)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_344(a:sympy.Rational):
	#(a < 813179152525346414339585835102428211193689/348449143727040986586495598010130648530944) & (a > 24623430962648187265/73786976294838206464 - sqrt(288230376151711743)/268435456)

	pre_cond = And(StrictLessThan(Symbol('a'), Rational(813179152525346414339585835102428211193689, 348449143727040986586495598010130648530944)), StrictGreaterThan(Symbol('a'), Add(Rational(24623430962648187265, 73786976294838206464), Mul(Integer(-1), Rational(1, 268435456), Pow(Integer(288230376151711743), Rational(1, 2))))))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_345(a:sympy.Rational):
	#(a + y**2 - z**2 + 606313352372301434184770344590508180225/5444517870735015415413993718908291383296 < 0) & (-a**2 + 24623430962648187265*a/36893488147419103232 - y**2 + 2*y + 15727240259832744812057210812134365969663/5444517870735015415413993718908291383296 > 0)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Pow(Symbol('y'), Integer(2)), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(606313352372301434184770344590508180225, 5444517870735015415413993718908291383296)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('a'), Integer(2))), Mul(Rational(24623430962648187265, 36893488147419103232), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Mul(Integer(2), Symbol('y')), Rational(15727240259832744812057210812134365969663, 5444517870735015415413993718908291383296)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_346(a:sympy.Rational):
	#(a - z**2 + 6050831182542497717853286941518620410625/5444517870735015415413993718908291383296 < 0) & (36893488147419103232*a**2 - 24623430962648187265*a < 21171758130567760151913340805128333933823/147573952589676412928)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(6050831182542497717853286941518620410625, 5444517870735015415413993718908291383296)), Integer(0)), StrictLessThan(Add(Mul(Integer(36893488147419103232), Pow(Symbol('a'), Integer(2))), Mul(Integer(-1), Integer(24623430962648187265), Symbol('a'))), Rational(21171758130567760151913340805128333933823, 147573952589676412928)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_347(a:sympy.Rational):
	#(a < 813179152525346414339585835102428211193689/348449143727040986586495598010130648530944) & (a > 24623430962648187265/73786976294838206464 - sqrt(288230376151711743)/268435456)

	pre_cond = And(StrictLessThan(Symbol('a'), Rational(813179152525346414339585835102428211193689, 348449143727040986586495598010130648530944)), StrictGreaterThan(Symbol('a'), Add(Rational(24623430962648187265, 73786976294838206464), Mul(Integer(-1), Rational(1, 268435456), Pow(Integer(288230376151711743), Rational(1, 2))))))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_348(a:sympy.Rational):
	#(a + y**2 - z**2 + 606313352372301434184770344590508180225/5444517870735015415413993718908291383296 < 0) & (-a**2 + 24623430962648187265*a/36893488147419103232 - y**2 + 2*y + 15727240259832744812057210812134365969663/5444517870735015415413993718908291383296 > 0)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Pow(Symbol('y'), Integer(2)), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(606313352372301434184770344590508180225, 5444517870735015415413993718908291383296)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('a'), Integer(2))), Mul(Rational(24623430962648187265, 36893488147419103232), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Mul(Integer(2), Symbol('y')), Rational(15727240259832744812057210812134365969663, 5444517870735015415413993718908291383296)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_349(a:sympy.Rational):
	#(a - z**2 + 6050831182542497717853286941518620410625/5444517870735015415413993718908291383296 < 0) & (36893488147419103232*a**2 - 24623430962648187265*a < 21171758130567760151913340805128333933823/147573952589676412928)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(6050831182542497717853286941518620410625, 5444517870735015415413993718908291383296)), Integer(0)), StrictLessThan(Add(Mul(Integer(36893488147419103232), Pow(Symbol('a'), Integer(2))), Mul(Integer(-1), Integer(24623430962648187265), Symbol('a'))), Rational(21171758130567760151913340805128333933823, 147573952589676412928)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_350(a:sympy.Rational):
	#(a < 813179152525346414339585835102428211193689/348449143727040986586495598010130648530944) & (a > 24623430962648187265/73786976294838206464 - sqrt(288230376151711743)/268435456)

	pre_cond = And(StrictLessThan(Symbol('a'), Rational(813179152525346414339585835102428211193689, 348449143727040986586495598010130648530944)), StrictGreaterThan(Symbol('a'), Add(Rational(24623430962648187265, 73786976294838206464), Mul(Integer(-1), Rational(1, 268435456), Pow(Integer(288230376151711743), Rational(1, 2))))))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_351(a:sympy.Rational):
	#(a + y**2 - z**2 + 606313352372301434184770344590508180225/5444517870735015415413993718908291383296 < 0) & (-a**2 + 24623430962648187265*a/36893488147419103232 - y**2 + 2*y + 15727240259832744812057210812134365969663/5444517870735015415413993718908291383296 > 0)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Pow(Symbol('y'), Integer(2)), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(606313352372301434184770344590508180225, 5444517870735015415413993718908291383296)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('a'), Integer(2))), Mul(Rational(24623430962648187265, 36893488147419103232), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Mul(Integer(2), Symbol('y')), Rational(15727240259832744812057210812134365969663, 5444517870735015415413993718908291383296)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_352(a:sympy.Rational):
	#(a - z**2 + 6050831182542497717853286941518620410625/5444517870735015415413993718908291383296 < 0) & (36893488147419103232*a**2 - 24623430962648187265*a < 21171758130567760151913340805128333933823/147573952589676412928)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(6050831182542497717853286941518620410625, 5444517870735015415413993718908291383296)), Integer(0)), StrictLessThan(Add(Mul(Integer(36893488147419103232), Pow(Symbol('a'), Integer(2))), Mul(Integer(-1), Integer(24623430962648187265), Symbol('a'))), Rational(21171758130567760151913340805128333933823, 147573952589676412928)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_353(a:sympy.Rational):
	#(a < 813179152525346414339585835102428211193689/348449143727040986586495598010130648530944) & (a > 24623430962648187265/73786976294838206464 - sqrt(288230376151711743)/268435456)

	pre_cond = And(StrictLessThan(Symbol('a'), Rational(813179152525346414339585835102428211193689, 348449143727040986586495598010130648530944)), StrictGreaterThan(Symbol('a'), Add(Rational(24623430962648187265, 73786976294838206464), Mul(Integer(-1), Rational(1, 268435456), Pow(Integer(288230376151711743), Rational(1, 2))))))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_354(a:sympy.Rational):
	#(a + y**2 - z**2 + 606313352372301434184770344590508180225/5444517870735015415413993718908291383296 < 0) & (-a**2 + 24623430962648187265*a/36893488147419103232 - y**2 + 2*y + 15727240259832744812057210812134365969663/5444517870735015415413993718908291383296 > 0)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Pow(Symbol('y'), Integer(2)), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(606313352372301434184770344590508180225, 5444517870735015415413993718908291383296)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('a'), Integer(2))), Mul(Rational(24623430962648187265, 36893488147419103232), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Mul(Integer(2), Symbol('y')), Rational(15727240259832744812057210812134365969663, 5444517870735015415413993718908291383296)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_355(a:sympy.Rational):
	#(a - z**2 + 6050831182542497717853286941518620410625/5444517870735015415413993718908291383296 < 0) & (36893488147419103232*a**2 - 24623430962648187265*a < 21171758130567760151913340805128333933823/147573952589676412928)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(6050831182542497717853286941518620410625, 5444517870735015415413993718908291383296)), Integer(0)), StrictLessThan(Add(Mul(Integer(36893488147419103232), Pow(Symbol('a'), Integer(2))), Mul(Integer(-1), Integer(24623430962648187265), Symbol('a'))), Rational(21171758130567760151913340805128333933823, 147573952589676412928)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_356(a:sympy.Rational):
	#(a < 813179152525346414339585835102428211193689/348449143727040986586495598010130648530944) & (a > 24623430962648187265/73786976294838206464 - sqrt(288230376151711743)/268435456)

	pre_cond = And(StrictLessThan(Symbol('a'), Rational(813179152525346414339585835102428211193689, 348449143727040986586495598010130648530944)), StrictGreaterThan(Symbol('a'), Add(Rational(24623430962648187265, 73786976294838206464), Mul(Integer(-1), Rational(1, 268435456), Pow(Integer(288230376151711743), Rational(1, 2))))))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_357(a:sympy.Rational):
	#(a + y**2 - z**2 + 606313352372301434184770344590508180225/5444517870735015415413993718908291383296 < 0) & (-a**2 + 24623430962648187265*a/36893488147419103232 - y**2 + 2*y + 15727240259832744812057210812134365969663/5444517870735015415413993718908291383296 > 0)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Pow(Symbol('y'), Integer(2)), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(606313352372301434184770344590508180225, 5444517870735015415413993718908291383296)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('a'), Integer(2))), Mul(Rational(24623430962648187265, 36893488147419103232), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Mul(Integer(2), Symbol('y')), Rational(15727240259832744812057210812134365969663, 5444517870735015415413993718908291383296)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_358(a:sympy.Rational):
	#(a - z**2 + 6050831182542497717853286941518620410625/5444517870735015415413993718908291383296 < 0) & (36893488147419103232*a**2 - 24623430962648187265*a < 21171758130567760151913340805128333933823/147573952589676412928)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(6050831182542497717853286941518620410625, 5444517870735015415413993718908291383296)), Integer(0)), StrictLessThan(Add(Mul(Integer(36893488147419103232), Pow(Symbol('a'), Integer(2))), Mul(Integer(-1), Integer(24623430962648187265), Symbol('a'))), Rational(21171758130567760151913340805128333933823, 147573952589676412928)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_359(a:sympy.Rational):
	#(a < 813179152525346414339585835102428211193689/348449143727040986586495598010130648530944) & (a > 24623430962648187265/73786976294838206464 - sqrt(288230376151711743)/268435456)

	pre_cond = And(StrictLessThan(Symbol('a'), Rational(813179152525346414339585835102428211193689, 348449143727040986586495598010130648530944)), StrictGreaterThan(Symbol('a'), Add(Rational(24623430962648187265, 73786976294838206464), Mul(Integer(-1), Rational(1, 268435456), Pow(Integer(288230376151711743), Rational(1, 2))))))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_360(a:sympy.Rational):
	#(a + y**2 - z**2 + 606313352372301434184770344590508180225/5444517870735015415413993718908291383296 < 0) & (-a**2 + 24623430962648187265*a/36893488147419103232 - y**2 + 2*y + 15727240259832744812057210812134365969663/5444517870735015415413993718908291383296 > 0)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Pow(Symbol('y'), Integer(2)), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(606313352372301434184770344590508180225, 5444517870735015415413993718908291383296)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('a'), Integer(2))), Mul(Rational(24623430962648187265, 36893488147419103232), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Mul(Integer(2), Symbol('y')), Rational(15727240259832744812057210812134365969663, 5444517870735015415413993718908291383296)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_361(a:sympy.Rational):
	#(a - z**2 + 6050831182542497717853286941518620410625/5444517870735015415413993718908291383296 < 0) & (36893488147419103232*a**2 - 24623430962648187265*a < 21171758130567760151913340805128333933823/147573952589676412928)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(6050831182542497717853286941518620410625, 5444517870735015415413993718908291383296)), Integer(0)), StrictLessThan(Add(Mul(Integer(36893488147419103232), Pow(Symbol('a'), Integer(2))), Mul(Integer(-1), Integer(24623430962648187265), Symbol('a'))), Rational(21171758130567760151913340805128333933823, 147573952589676412928)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_362(a:sympy.Rational):
	#(a < 813179152525346414339585835102428211193689/348449143727040986586495598010130648530944) & (a > 24623430962648187265/73786976294838206464 - sqrt(288230376151711743)/268435456)

	pre_cond = And(StrictLessThan(Symbol('a'), Rational(813179152525346414339585835102428211193689, 348449143727040986586495598010130648530944)), StrictGreaterThan(Symbol('a'), Add(Rational(24623430962648187265, 73786976294838206464), Mul(Integer(-1), Rational(1, 268435456), Pow(Integer(288230376151711743), Rational(1, 2))))))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_363(a:sympy.Rational):
	#(a + y**2 - z**2 + 606313352372301434184770344590508180225/5444517870735015415413993718908291383296 < 0) & (-a**2 + 24623430962648187265*a/36893488147419103232 - y**2 + 2*y + 15727240259832744812057210812134365969663/5444517870735015415413993718908291383296 > 0)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Pow(Symbol('y'), Integer(2)), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(606313352372301434184770344590508180225, 5444517870735015415413993718908291383296)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('a'), Integer(2))), Mul(Rational(24623430962648187265, 36893488147419103232), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Mul(Integer(2), Symbol('y')), Rational(15727240259832744812057210812134365969663, 5444517870735015415413993718908291383296)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_364(a:sympy.Rational):
	#(a - z**2 + 6050831182542497717853286941518620410625/5444517870735015415413993718908291383296 < 0) & (36893488147419103232*a**2 - 24623430962648187265*a < 21171758130567760151913340805128333933823/147573952589676412928)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(6050831182542497717853286941518620410625, 5444517870735015415413993718908291383296)), Integer(0)), StrictLessThan(Add(Mul(Integer(36893488147419103232), Pow(Symbol('a'), Integer(2))), Mul(Integer(-1), Integer(24623430962648187265), Symbol('a'))), Rational(21171758130567760151913340805128333933823, 147573952589676412928)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_365(a:sympy.Rational):
	#(a < 813179152525346414339585835102428211193689/348449143727040986586495598010130648530944) & (a > 24623430962648187265/73786976294838206464 - sqrt(288230376151711743)/268435456)

	pre_cond = And(StrictLessThan(Symbol('a'), Rational(813179152525346414339585835102428211193689, 348449143727040986586495598010130648530944)), StrictGreaterThan(Symbol('a'), Add(Rational(24623430962648187265, 73786976294838206464), Mul(Integer(-1), Rational(1, 268435456), Pow(Integer(288230376151711743), Rational(1, 2))))))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_366(a:sympy.Rational):
	#(a + y**2 - z**2 + 606313352372301434184770344590508180225/5444517870735015415413993718908291383296 < 0) & (-a**2 + 24623430962648187265*a/36893488147419103232 - y**2 + 2*y + 15727240259832744812057210812134365969663/5444517870735015415413993718908291383296 > 0)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Pow(Symbol('y'), Integer(2)), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(606313352372301434184770344590508180225, 5444517870735015415413993718908291383296)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('a'), Integer(2))), Mul(Rational(24623430962648187265, 36893488147419103232), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Mul(Integer(2), Symbol('y')), Rational(15727240259832744812057210812134365969663, 5444517870735015415413993718908291383296)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_367(a:sympy.Rational):
	#(a - z**2 + 6050831182542497717853286941518620410625/5444517870735015415413993718908291383296 < 0) & (36893488147419103232*a**2 - 24623430962648187265*a < 21171758130567760151913340805128333933823/147573952589676412928)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(6050831182542497717853286941518620410625, 5444517870735015415413993718908291383296)), Integer(0)), StrictLessThan(Add(Mul(Integer(36893488147419103232), Pow(Symbol('a'), Integer(2))), Mul(Integer(-1), Integer(24623430962648187265), Symbol('a'))), Rational(21171758130567760151913340805128333933823, 147573952589676412928)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_368(a:sympy.Rational):
	#(a < 813179152525346414339585835102428211193689/348449143727040986586495598010130648530944) & (a > 24623430962648187265/73786976294838206464 - sqrt(288230376151711743)/268435456)

	pre_cond = And(StrictLessThan(Symbol('a'), Rational(813179152525346414339585835102428211193689, 348449143727040986586495598010130648530944)), StrictGreaterThan(Symbol('a'), Add(Rational(24623430962648187265, 73786976294838206464), Mul(Integer(-1), Rational(1, 268435456), Pow(Integer(288230376151711743), Rational(1, 2))))))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_369(a:sympy.Rational):
	#(a + y**2 - z**2 + 606313352372301434184770344590508180225/5444517870735015415413993718908291383296 < 0) & (-a**2 + 24623430962648187265*a/36893488147419103232 - y**2 + 2*y + 15727240259832744812057210812134365969663/5444517870735015415413993718908291383296 > 0)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Pow(Symbol('y'), Integer(2)), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(606313352372301434184770344590508180225, 5444517870735015415413993718908291383296)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('a'), Integer(2))), Mul(Rational(24623430962648187265, 36893488147419103232), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Mul(Integer(2), Symbol('y')), Rational(15727240259832744812057210812134365969663, 5444517870735015415413993718908291383296)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_370(a:sympy.Rational):
	#(a - z**2 + 6050831182542497717853286941518620410625/5444517870735015415413993718908291383296 < 0) & (36893488147419103232*a**2 - 24623430962648187265*a < 21171758130567760151913340805128333933823/147573952589676412928)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(6050831182542497717853286941518620410625, 5444517870735015415413993718908291383296)), Integer(0)), StrictLessThan(Add(Mul(Integer(36893488147419103232), Pow(Symbol('a'), Integer(2))), Mul(Integer(-1), Integer(24623430962648187265), Symbol('a'))), Rational(21171758130567760151913340805128333933823, 147573952589676412928)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_371(a:sympy.Rational):
	#(a < 813179152525346414339585835102428211193689/348449143727040986586495598010130648530944) & (a > 24623430962648187265/73786976294838206464 - sqrt(288230376151711743)/268435456)

	pre_cond = And(StrictLessThan(Symbol('a'), Rational(813179152525346414339585835102428211193689, 348449143727040986586495598010130648530944)), StrictGreaterThan(Symbol('a'), Add(Rational(24623430962648187265, 73786976294838206464), Mul(Integer(-1), Rational(1, 268435456), Pow(Integer(288230376151711743), Rational(1, 2))))))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_372(a:sympy.Rational):
	#(a + y**2 - z**2 + 606313352372301434184770344590508180225/5444517870735015415413993718908291383296 < 0) & (-a**2 + 24623430962648187265*a/36893488147419103232 - y**2 + 2*y + 15727240259832744812057210812134365969663/5444517870735015415413993718908291383296 > 0)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Pow(Symbol('y'), Integer(2)), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(606313352372301434184770344590508180225, 5444517870735015415413993718908291383296)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('a'), Integer(2))), Mul(Rational(24623430962648187265, 36893488147419103232), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Mul(Integer(2), Symbol('y')), Rational(15727240259832744812057210812134365969663, 5444517870735015415413993718908291383296)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_373(a:sympy.Rational):
	#(a - z**2 + 6050831182542497717853286941518620410625/5444517870735015415413993718908291383296 < 0) & (36893488147419103232*a**2 - 24623430962648187265*a < 21171758130567760151913340805128333933823/147573952589676412928)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(6050831182542497717853286941518620410625, 5444517870735015415413993718908291383296)), Integer(0)), StrictLessThan(Add(Mul(Integer(36893488147419103232), Pow(Symbol('a'), Integer(2))), Mul(Integer(-1), Integer(24623430962648187265), Symbol('a'))), Rational(21171758130567760151913340805128333933823, 147573952589676412928)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_374(a:sympy.Rational):
	#(a < 813179152525346414339585835102428211193689/348449143727040986586495598010130648530944) & (a > 24623430962648187265/73786976294838206464 - sqrt(288230376151711743)/268435456)

	pre_cond = And(StrictLessThan(Symbol('a'), Rational(813179152525346414339585835102428211193689, 348449143727040986586495598010130648530944)), StrictGreaterThan(Symbol('a'), Add(Rational(24623430962648187265, 73786976294838206464), Mul(Integer(-1), Rational(1, 268435456), Pow(Integer(288230376151711743), Rational(1, 2))))))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_375(a:sympy.Rational):
	#(a + y**2 - z**2 + 606313352372301434184770344590508180225/5444517870735015415413993718908291383296 < 0) & (-a**2 + 24623430962648187265*a/36893488147419103232 - y**2 + 2*y + 15727240259832744812057210812134365969663/5444517870735015415413993718908291383296 > 0)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Pow(Symbol('y'), Integer(2)), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(606313352372301434184770344590508180225, 5444517870735015415413993718908291383296)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('a'), Integer(2))), Mul(Rational(24623430962648187265, 36893488147419103232), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Mul(Integer(2), Symbol('y')), Rational(15727240259832744812057210812134365969663, 5444517870735015415413993718908291383296)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_376(a:sympy.Rational):
	#(a - z**2 + 6050831182542497717853286941518620410625/5444517870735015415413993718908291383296 < 0) & (36893488147419103232*a**2 - 24623430962648187265*a < 21171758130567760151913340805128333933823/147573952589676412928)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(6050831182542497717853286941518620410625, 5444517870735015415413993718908291383296)), Integer(0)), StrictLessThan(Add(Mul(Integer(36893488147419103232), Pow(Symbol('a'), Integer(2))), Mul(Integer(-1), Integer(24623430962648187265), Symbol('a'))), Rational(21171758130567760151913340805128333933823, 147573952589676412928)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_377(a:sympy.Rational):
	#(a < 813179152525346414339585835102428211193689/348449143727040986586495598010130648530944) & (a > 24623430962648187265/73786976294838206464 - sqrt(288230376151711743)/268435456)

	pre_cond = And(StrictLessThan(Symbol('a'), Rational(813179152525346414339585835102428211193689, 348449143727040986586495598010130648530944)), StrictGreaterThan(Symbol('a'), Add(Rational(24623430962648187265, 73786976294838206464), Mul(Integer(-1), Rational(1, 268435456), Pow(Integer(288230376151711743), Rational(1, 2))))))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_378(a:sympy.Rational):
	#(a + y**2 - z**2 + 606313352372301434184770344590508180225/5444517870735015415413993718908291383296 < 0) & (-a**2 + 24623430962648187265*a/36893488147419103232 - y**2 + 2*y + 15727240259832744812057210812134365969663/5444517870735015415413993718908291383296 > 0)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Pow(Symbol('y'), Integer(2)), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(606313352372301434184770344590508180225, 5444517870735015415413993718908291383296)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('a'), Integer(2))), Mul(Rational(24623430962648187265, 36893488147419103232), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Mul(Integer(2), Symbol('y')), Rational(15727240259832744812057210812134365969663, 5444517870735015415413993718908291383296)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_379(a:sympy.Rational):
	#(a - z**2 + 6050831182542497717853286941518620410625/5444517870735015415413993718908291383296 < 0) & (36893488147419103232*a**2 - 24623430962648187265*a < 21171758130567760151913340805128333933823/147573952589676412928)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(6050831182542497717853286941518620410625, 5444517870735015415413993718908291383296)), Integer(0)), StrictLessThan(Add(Mul(Integer(36893488147419103232), Pow(Symbol('a'), Integer(2))), Mul(Integer(-1), Integer(24623430962648187265), Symbol('a'))), Rational(21171758130567760151913340805128333933823, 147573952589676412928)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_380(a:sympy.Rational):
	#(a < 813179152525346414339585835102428211193689/348449143727040986586495598010130648530944) & (a > 24623430962648187265/73786976294838206464 - sqrt(288230376151711743)/268435456)

	pre_cond = And(StrictLessThan(Symbol('a'), Rational(813179152525346414339585835102428211193689, 348449143727040986586495598010130648530944)), StrictGreaterThan(Symbol('a'), Add(Rational(24623430962648187265, 73786976294838206464), Mul(Integer(-1), Rational(1, 268435456), Pow(Integer(288230376151711743), Rational(1, 2))))))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_381(a:sympy.Rational):
	#(a + y**2 - z**2 + 606313352372301434184770344590508180225/5444517870735015415413993718908291383296 < 0) & (-a**2 + 24623430962648187265*a/36893488147419103232 - y**2 + 2*y + 15727240259832744812057210812134365969663/5444517870735015415413993718908291383296 > 0)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Pow(Symbol('y'), Integer(2)), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(606313352372301434184770344590508180225, 5444517870735015415413993718908291383296)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('a'), Integer(2))), Mul(Rational(24623430962648187265, 36893488147419103232), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Mul(Integer(2), Symbol('y')), Rational(15727240259832744812057210812134365969663, 5444517870735015415413993718908291383296)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_382(a:sympy.Rational):
	#(a - z**2 + 6050831182542497717853286941518620410625/5444517870735015415413993718908291383296 < 0) & (36893488147419103232*a**2 - 24623430962648187265*a < 21171758130567760151913340805128333933823/147573952589676412928)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(6050831182542497717853286941518620410625, 5444517870735015415413993718908291383296)), Integer(0)), StrictLessThan(Add(Mul(Integer(36893488147419103232), Pow(Symbol('a'), Integer(2))), Mul(Integer(-1), Integer(24623430962648187265), Symbol('a'))), Rational(21171758130567760151913340805128333933823, 147573952589676412928)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_383(a:sympy.Rational):
	#(a < 813179152525346414339585835102428211193689/348449143727040986586495598010130648530944) & (a > 24623430962648187265/73786976294838206464 - sqrt(288230376151711743)/268435456)

	pre_cond = And(StrictLessThan(Symbol('a'), Rational(813179152525346414339585835102428211193689, 348449143727040986586495598010130648530944)), StrictGreaterThan(Symbol('a'), Add(Rational(24623430962648187265, 73786976294838206464), Mul(Integer(-1), Rational(1, 268435456), Pow(Integer(288230376151711743), Rational(1, 2))))))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_384(a:sympy.Rational):
	#(a + y**2 - z**2 + 606313352372301434184770344590508180225/5444517870735015415413993718908291383296 < 0) & (-a**2 + 24623430962648187265*a/36893488147419103232 - y**2 + 2*y + 15727240259832744812057210812134365969663/5444517870735015415413993718908291383296 > 0)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Pow(Symbol('y'), Integer(2)), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(606313352372301434184770344590508180225, 5444517870735015415413993718908291383296)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('a'), Integer(2))), Mul(Rational(24623430962648187265, 36893488147419103232), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Mul(Integer(2), Symbol('y')), Rational(15727240259832744812057210812134365969663, 5444517870735015415413993718908291383296)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_385(a:sympy.Rational):
	#(a - z**2 + 6050831182542497717853286941518620410625/5444517870735015415413993718908291383296 < 0) & (36893488147419103232*a**2 - 24623430962648187265*a < 21171758130567760151913340805128333933823/147573952589676412928)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(6050831182542497717853286941518620410625, 5444517870735015415413993718908291383296)), Integer(0)), StrictLessThan(Add(Mul(Integer(36893488147419103232), Pow(Symbol('a'), Integer(2))), Mul(Integer(-1), Integer(24623430962648187265), Symbol('a'))), Rational(21171758130567760151913340805128333933823, 147573952589676412928)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_386(a:sympy.Rational):
	#(a < 813179152525346414339585835102428211193689/348449143727040986586495598010130648530944) & (a > 24623430962648187265/73786976294838206464 - sqrt(288230376151711743)/268435456)

	pre_cond = And(StrictLessThan(Symbol('a'), Rational(813179152525346414339585835102428211193689, 348449143727040986586495598010130648530944)), StrictGreaterThan(Symbol('a'), Add(Rational(24623430962648187265, 73786976294838206464), Mul(Integer(-1), Rational(1, 268435456), Pow(Integer(288230376151711743), Rational(1, 2))))))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_387(a:sympy.Rational):
	#(a + y**2 - z**2 + 606313352372301434184770344590508180225/5444517870735015415413993718908291383296 < 0) & (-a**2 + 24623430962648187265*a/36893488147419103232 - y**2 + 2*y + 15727240259832744812057210812134365969663/5444517870735015415413993718908291383296 > 0)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Pow(Symbol('y'), Integer(2)), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(606313352372301434184770344590508180225, 5444517870735015415413993718908291383296)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('a'), Integer(2))), Mul(Rational(24623430962648187265, 36893488147419103232), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Mul(Integer(2), Symbol('y')), Rational(15727240259832744812057210812134365969663, 5444517870735015415413993718908291383296)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_388(a:sympy.Rational):
	#(a - z**2 + 6050831182542497717853286941518620410625/5444517870735015415413993718908291383296 < 0) & (36893488147419103232*a**2 - 24623430962648187265*a < 21171758130567760151913340805128333933823/147573952589676412928)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(6050831182542497717853286941518620410625, 5444517870735015415413993718908291383296)), Integer(0)), StrictLessThan(Add(Mul(Integer(36893488147419103232), Pow(Symbol('a'), Integer(2))), Mul(Integer(-1), Integer(24623430962648187265), Symbol('a'))), Rational(21171758130567760151913340805128333933823, 147573952589676412928)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_389(a:sympy.Rational):
	#(a < 813179152525346414339585835102428211193689/348449143727040986586495598010130648530944) & (a > 24623430962648187265/73786976294838206464 - sqrt(288230376151711743)/268435456)

	pre_cond = And(StrictLessThan(Symbol('a'), Rational(813179152525346414339585835102428211193689, 348449143727040986586495598010130648530944)), StrictGreaterThan(Symbol('a'), Add(Rational(24623430962648187265, 73786976294838206464), Mul(Integer(-1), Rational(1, 268435456), Pow(Integer(288230376151711743), Rational(1, 2))))))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_390(a:sympy.Rational):
	#(a + y**2 - z**2 + 606313352372301434184770344590508180225/5444517870735015415413993718908291383296 < 0) & (-a**2 + 24623430962648187265*a/36893488147419103232 - y**2 + 2*y + 15727240259832744812057210812134365969663/5444517870735015415413993718908291383296 > 0)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Pow(Symbol('y'), Integer(2)), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(606313352372301434184770344590508180225, 5444517870735015415413993718908291383296)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('a'), Integer(2))), Mul(Rational(24623430962648187265, 36893488147419103232), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Mul(Integer(2), Symbol('y')), Rational(15727240259832744812057210812134365969663, 5444517870735015415413993718908291383296)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_391(a:sympy.Rational):
	#(a - z**2 + 6050831182542497717853286941518620410625/5444517870735015415413993718908291383296 < 0) & (36893488147419103232*a**2 - 24623430962648187265*a < 21171758130567760151913340805128333933823/147573952589676412928)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(6050831182542497717853286941518620410625, 5444517870735015415413993718908291383296)), Integer(0)), StrictLessThan(Add(Mul(Integer(36893488147419103232), Pow(Symbol('a'), Integer(2))), Mul(Integer(-1), Integer(24623430962648187265), Symbol('a'))), Rational(21171758130567760151913340805128333933823, 147573952589676412928)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_392(a:sympy.Rational):
	#(a < 813179152525346414339585835102428211193689/348449143727040986586495598010130648530944) & (a > 24623430962648187265/73786976294838206464 - sqrt(288230376151711743)/268435456)

	pre_cond = And(StrictLessThan(Symbol('a'), Rational(813179152525346414339585835102428211193689, 348449143727040986586495598010130648530944)), StrictGreaterThan(Symbol('a'), Add(Rational(24623430962648187265, 73786976294838206464), Mul(Integer(-1), Rational(1, 268435456), Pow(Integer(288230376151711743), Rational(1, 2))))))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_393(a:sympy.Rational):
	#(a + y**2 - z**2 + 606313352372301434184770344590508180225/5444517870735015415413993718908291383296 < 0) & (-a**2 + 24623430962648187265*a/36893488147419103232 - y**2 + 2*y + 15727240259832744812057210812134365969663/5444517870735015415413993718908291383296 > 0)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Pow(Symbol('y'), Integer(2)), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(606313352372301434184770344590508180225, 5444517870735015415413993718908291383296)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('a'), Integer(2))), Mul(Rational(24623430962648187265, 36893488147419103232), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Mul(Integer(2), Symbol('y')), Rational(15727240259832744812057210812134365969663, 5444517870735015415413993718908291383296)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_394(a:sympy.Rational):
	#(a - z**2 + 6050831182542497717853286941518620410625/5444517870735015415413993718908291383296 < 0) & (36893488147419103232*a**2 - 24623430962648187265*a < 21171758130567760151913340805128333933823/147573952589676412928)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(6050831182542497717853286941518620410625, 5444517870735015415413993718908291383296)), Integer(0)), StrictLessThan(Add(Mul(Integer(36893488147419103232), Pow(Symbol('a'), Integer(2))), Mul(Integer(-1), Integer(24623430962648187265), Symbol('a'))), Rational(21171758130567760151913340805128333933823, 147573952589676412928)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_395(a:sympy.Rational):
	#(a < 813179152525346414339585835102428211193689/348449143727040986586495598010130648530944) & (a > 24623430962648187265/73786976294838206464 - sqrt(288230376151711743)/268435456)

	pre_cond = And(StrictLessThan(Symbol('a'), Rational(813179152525346414339585835102428211193689, 348449143727040986586495598010130648530944)), StrictGreaterThan(Symbol('a'), Add(Rational(24623430962648187265, 73786976294838206464), Mul(Integer(-1), Rational(1, 268435456), Pow(Integer(288230376151711743), Rational(1, 2))))))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_396(a:sympy.Rational):
	#(a + y**2 - z**2 + 606313352372301434184770344590508180225/5444517870735015415413993718908291383296 < 0) & (-a**2 + 24623430962648187265*a/36893488147419103232 - y**2 + 2*y + 15727240259832744812057210812134365969663/5444517870735015415413993718908291383296 > 0)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Pow(Symbol('y'), Integer(2)), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(606313352372301434184770344590508180225, 5444517870735015415413993718908291383296)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('a'), Integer(2))), Mul(Rational(24623430962648187265, 36893488147419103232), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Mul(Integer(2), Symbol('y')), Rational(15727240259832744812057210812134365969663, 5444517870735015415413993718908291383296)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_397(a:sympy.Rational):
	#(a - z**2 + 6050831182542497717853286941518620410625/5444517870735015415413993718908291383296 < 0) & (36893488147419103232*a**2 - 24623430962648187265*a < 21171758130567760151913340805128333933823/147573952589676412928)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(6050831182542497717853286941518620410625, 5444517870735015415413993718908291383296)), Integer(0)), StrictLessThan(Add(Mul(Integer(36893488147419103232), Pow(Symbol('a'), Integer(2))), Mul(Integer(-1), Integer(24623430962648187265), Symbol('a'))), Rational(21171758130567760151913340805128333933823, 147573952589676412928)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_398(a:sympy.Rational):
	#(a < 813179152525346414339585835102428211193689/348449143727040986586495598010130648530944) & (a > 24623430962648187265/73786976294838206464 - sqrt(288230376151711743)/268435456)

	pre_cond = And(StrictLessThan(Symbol('a'), Rational(813179152525346414339585835102428211193689, 348449143727040986586495598010130648530944)), StrictGreaterThan(Symbol('a'), Add(Rational(24623430962648187265, 73786976294838206464), Mul(Integer(-1), Rational(1, 268435456), Pow(Integer(288230376151711743), Rational(1, 2))))))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_399(a:sympy.Rational):
	#(a + y**2 - z**2 + 606313352372301434184770344590508180225/5444517870735015415413993718908291383296 < 0) & (-a**2 + 24623430962648187265*a/36893488147419103232 - y**2 + 2*y + 15727240259832744812057210812134365969663/5444517870735015415413993718908291383296 > 0)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Pow(Symbol('y'), Integer(2)), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(606313352372301434184770344590508180225, 5444517870735015415413993718908291383296)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('a'), Integer(2))), Mul(Rational(24623430962648187265, 36893488147419103232), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Mul(Integer(2), Symbol('y')), Rational(15727240259832744812057210812134365969663, 5444517870735015415413993718908291383296)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_400(a:sympy.Rational):
	#(a - z**2 + 6050831182542497717853286941518620410625/5444517870735015415413993718908291383296 < 0) & (36893488147419103232*a**2 - 24623430962648187265*a < 21171758130567760151913340805128333933823/147573952589676412928)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(6050831182542497717853286941518620410625, 5444517870735015415413993718908291383296)), Integer(0)), StrictLessThan(Add(Mul(Integer(36893488147419103232), Pow(Symbol('a'), Integer(2))), Mul(Integer(-1), Integer(24623430962648187265), Symbol('a'))), Rational(21171758130567760151913340805128333933823, 147573952589676412928)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_401(a:sympy.Rational):
	#(a < 813179152525346414339585835102428211193689/348449143727040986586495598010130648530944) & (a > 24623430962648187265/73786976294838206464 - sqrt(288230376151711743)/268435456)

	pre_cond = And(StrictLessThan(Symbol('a'), Rational(813179152525346414339585835102428211193689, 348449143727040986586495598010130648530944)), StrictGreaterThan(Symbol('a'), Add(Rational(24623430962648187265, 73786976294838206464), Mul(Integer(-1), Rational(1, 268435456), Pow(Integer(288230376151711743), Rational(1, 2))))))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_402(a:sympy.Rational):
	#(a + y**2 - z**2 + 606313352372301434184770344590508180225/5444517870735015415413993718908291383296 < 0) & (-a**2 + 24623430962648187265*a/36893488147419103232 - y**2 + 2*y + 15727240259832744812057210812134365969663/5444517870735015415413993718908291383296 > 0)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Pow(Symbol('y'), Integer(2)), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(606313352372301434184770344590508180225, 5444517870735015415413993718908291383296)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('a'), Integer(2))), Mul(Rational(24623430962648187265, 36893488147419103232), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Mul(Integer(2), Symbol('y')), Rational(15727240259832744812057210812134365969663, 5444517870735015415413993718908291383296)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_403(a:sympy.Rational):
	#(a - z**2 + 6050831182542497717853286941518620410625/5444517870735015415413993718908291383296 < 0) & (36893488147419103232*a**2 - 24623430962648187265*a < 21171758130567760151913340805128333933823/147573952589676412928)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(6050831182542497717853286941518620410625, 5444517870735015415413993718908291383296)), Integer(0)), StrictLessThan(Add(Mul(Integer(36893488147419103232), Pow(Symbol('a'), Integer(2))), Mul(Integer(-1), Integer(24623430962648187265), Symbol('a'))), Rational(21171758130567760151913340805128333933823, 147573952589676412928)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_404(a:sympy.Rational):
	#(a < 813179152525346414339585835102428211193689/348449143727040986586495598010130648530944) & (a > 24623430962648187265/73786976294838206464 - sqrt(288230376151711743)/268435456)

	pre_cond = And(StrictLessThan(Symbol('a'), Rational(813179152525346414339585835102428211193689, 348449143727040986586495598010130648530944)), StrictGreaterThan(Symbol('a'), Add(Rational(24623430962648187265, 73786976294838206464), Mul(Integer(-1), Rational(1, 268435456), Pow(Integer(288230376151711743), Rational(1, 2))))))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_405(a:sympy.Rational):
	#(a + y**2 - z**2 + 606313352372301434184770344590508180225/5444517870735015415413993718908291383296 < 0) & (-a**2 + 24623430962648187265*a/36893488147419103232 - y**2 + 2*y + 15727240259832744812057210812134365969663/5444517870735015415413993718908291383296 > 0)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Pow(Symbol('y'), Integer(2)), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(606313352372301434184770344590508180225, 5444517870735015415413993718908291383296)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('a'), Integer(2))), Mul(Rational(24623430962648187265, 36893488147419103232), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Mul(Integer(2), Symbol('y')), Rational(15727240259832744812057210812134365969663, 5444517870735015415413993718908291383296)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_406(a:sympy.Rational):
	#(a - z**2 + 6050831182542497717853286941518620410625/5444517870735015415413993718908291383296 < 0) & (36893488147419103232*a**2 - 24623430962648187265*a < 21171758130567760151913340805128333933823/147573952589676412928)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(6050831182542497717853286941518620410625, 5444517870735015415413993718908291383296)), Integer(0)), StrictLessThan(Add(Mul(Integer(36893488147419103232), Pow(Symbol('a'), Integer(2))), Mul(Integer(-1), Integer(24623430962648187265), Symbol('a'))), Rational(21171758130567760151913340805128333933823, 147573952589676412928)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_407(a:sympy.Rational):
	#(a < 813179152525346414339585835102428211193689/348449143727040986586495598010130648530944) & (a > 24623430962648187265/73786976294838206464 - sqrt(288230376151711743)/268435456)

	pre_cond = And(StrictLessThan(Symbol('a'), Rational(813179152525346414339585835102428211193689, 348449143727040986586495598010130648530944)), StrictGreaterThan(Symbol('a'), Add(Rational(24623430962648187265, 73786976294838206464), Mul(Integer(-1), Rational(1, 268435456), Pow(Integer(288230376151711743), Rational(1, 2))))))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_408(a:sympy.Rational):
	#(a + y**2 - z**2 + 606313352372301434184770344590508180225/5444517870735015415413993718908291383296 < 0) & (-a**2 + 24623430962648187265*a/36893488147419103232 - y**2 + 2*y + 15727240259832744812057210812134365969663/5444517870735015415413993718908291383296 > 0)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Pow(Symbol('y'), Integer(2)), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(606313352372301434184770344590508180225, 5444517870735015415413993718908291383296)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('a'), Integer(2))), Mul(Rational(24623430962648187265, 36893488147419103232), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Mul(Integer(2), Symbol('y')), Rational(15727240259832744812057210812134365969663, 5444517870735015415413993718908291383296)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_409(a:sympy.Rational):
	#(a - z**2 + 6050831182542497717853286941518620410625/5444517870735015415413993718908291383296 < 0) & (36893488147419103232*a**2 - 24623430962648187265*a < 21171758130567760151913340805128333933823/147573952589676412928)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(6050831182542497717853286941518620410625, 5444517870735015415413993718908291383296)), Integer(0)), StrictLessThan(Add(Mul(Integer(36893488147419103232), Pow(Symbol('a'), Integer(2))), Mul(Integer(-1), Integer(24623430962648187265), Symbol('a'))), Rational(21171758130567760151913340805128333933823, 147573952589676412928)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_410(a:sympy.Rational):
	#(a < 813179152525346414339585835102428211193689/348449143727040986586495598010130648530944) & (a > 24623430962648187265/73786976294838206464 - sqrt(288230376151711743)/268435456)

	pre_cond = And(StrictLessThan(Symbol('a'), Rational(813179152525346414339585835102428211193689, 348449143727040986586495598010130648530944)), StrictGreaterThan(Symbol('a'), Add(Rational(24623430962648187265, 73786976294838206464), Mul(Integer(-1), Rational(1, 268435456), Pow(Integer(288230376151711743), Rational(1, 2))))))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_411(a:sympy.Rational):
	#(a + y**2 - z**2 + 606313352372301434184770344590508180225/5444517870735015415413993718908291383296 < 0) & (-a**2 + 24623430962648187265*a/36893488147419103232 - y**2 + 2*y + 15727240259832744812057210812134365969663/5444517870735015415413993718908291383296 > 0)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Pow(Symbol('y'), Integer(2)), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(606313352372301434184770344590508180225, 5444517870735015415413993718908291383296)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('a'), Integer(2))), Mul(Rational(24623430962648187265, 36893488147419103232), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Mul(Integer(2), Symbol('y')), Rational(15727240259832744812057210812134365969663, 5444517870735015415413993718908291383296)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_412(a:sympy.Rational):
	#(a - z**2 + 6050831182542497717853286941518620410625/5444517870735015415413993718908291383296 < 0) & (36893488147419103232*a**2 - 24623430962648187265*a < 21171758130567760151913340805128333933823/147573952589676412928)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(6050831182542497717853286941518620410625, 5444517870735015415413993718908291383296)), Integer(0)), StrictLessThan(Add(Mul(Integer(36893488147419103232), Pow(Symbol('a'), Integer(2))), Mul(Integer(-1), Integer(24623430962648187265), Symbol('a'))), Rational(21171758130567760151913340805128333933823, 147573952589676412928)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_413(a:sympy.Rational):
	#(a < 813179152525346414339585835102428211193689/348449143727040986586495598010130648530944) & (a > 24623430962648187265/73786976294838206464 - sqrt(288230376151711743)/268435456)

	pre_cond = And(StrictLessThan(Symbol('a'), Rational(813179152525346414339585835102428211193689, 348449143727040986586495598010130648530944)), StrictGreaterThan(Symbol('a'), Add(Rational(24623430962648187265, 73786976294838206464), Mul(Integer(-1), Rational(1, 268435456), Pow(Integer(288230376151711743), Rational(1, 2))))))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_414(a:sympy.Rational):
	#(a + y**2 - z**2 + 606313352372301434184770344590508180225/5444517870735015415413993718908291383296 < 0) & (-a**2 + 24623430962648187265*a/36893488147419103232 - y**2 + 2*y + 15727240259832744812057210812134365969663/5444517870735015415413993718908291383296 > 0)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Pow(Symbol('y'), Integer(2)), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(606313352372301434184770344590508180225, 5444517870735015415413993718908291383296)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('a'), Integer(2))), Mul(Rational(24623430962648187265, 36893488147419103232), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Mul(Integer(2), Symbol('y')), Rational(15727240259832744812057210812134365969663, 5444517870735015415413993718908291383296)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_415(a:sympy.Rational):
	#(a - z**2 + 6050831182542497717853286941518620410625/5444517870735015415413993718908291383296 < 0) & (36893488147419103232*a**2 - 24623430962648187265*a < 21171758130567760151913340805128333933823/147573952589676412928)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(6050831182542497717853286941518620410625, 5444517870735015415413993718908291383296)), Integer(0)), StrictLessThan(Add(Mul(Integer(36893488147419103232), Pow(Symbol('a'), Integer(2))), Mul(Integer(-1), Integer(24623430962648187265), Symbol('a'))), Rational(21171758130567760151913340805128333933823, 147573952589676412928)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_416(a:sympy.Rational):
	#(a < 813179152525346414339585835102428211193689/348449143727040986586495598010130648530944) & (a > 24623430962648187265/73786976294838206464 - sqrt(288230376151711743)/268435456)

	pre_cond = And(StrictLessThan(Symbol('a'), Rational(813179152525346414339585835102428211193689, 348449143727040986586495598010130648530944)), StrictGreaterThan(Symbol('a'), Add(Rational(24623430962648187265, 73786976294838206464), Mul(Integer(-1), Rational(1, 268435456), Pow(Integer(288230376151711743), Rational(1, 2))))))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_417(a:sympy.Rational):
	#(a + y**2 - z**2 + 606313352372301434184770344590508180225/5444517870735015415413993718908291383296 < 0) & (-a**2 + 24623430962648187265*a/36893488147419103232 - y**2 + 2*y + 15727240259832744812057210812134365969663/5444517870735015415413993718908291383296 > 0)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Pow(Symbol('y'), Integer(2)), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(606313352372301434184770344590508180225, 5444517870735015415413993718908291383296)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('a'), Integer(2))), Mul(Rational(24623430962648187265, 36893488147419103232), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Mul(Integer(2), Symbol('y')), Rational(15727240259832744812057210812134365969663, 5444517870735015415413993718908291383296)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_418(a:sympy.Rational):
	#(a - z**2 + 6050831182542497717853286941518620410625/5444517870735015415413993718908291383296 < 0) & (36893488147419103232*a**2 - 24623430962648187265*a < 21171758130567760151913340805128333933823/147573952589676412928)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(6050831182542497717853286941518620410625, 5444517870735015415413993718908291383296)), Integer(0)), StrictLessThan(Add(Mul(Integer(36893488147419103232), Pow(Symbol('a'), Integer(2))), Mul(Integer(-1), Integer(24623430962648187265), Symbol('a'))), Rational(21171758130567760151913340805128333933823, 147573952589676412928)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_419(a:sympy.Rational):
	#(a < 813179152525346414339585835102428211193689/348449143727040986586495598010130648530944) & (a > 24623430962648187265/73786976294838206464 - sqrt(288230376151711743)/268435456)

	pre_cond = And(StrictLessThan(Symbol('a'), Rational(813179152525346414339585835102428211193689, 348449143727040986586495598010130648530944)), StrictGreaterThan(Symbol('a'), Add(Rational(24623430962648187265, 73786976294838206464), Mul(Integer(-1), Rational(1, 268435456), Pow(Integer(288230376151711743), Rational(1, 2))))))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_420(a:sympy.Rational):
	#(a + y**2 - z**2 + 606313352372301434184770344590508180225/5444517870735015415413993718908291383296 < 0) & (-a**2 + 24623430962648187265*a/36893488147419103232 - y**2 + 2*y + 15727240259832744812057210812134365969663/5444517870735015415413993718908291383296 > 0)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Pow(Symbol('y'), Integer(2)), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(606313352372301434184770344590508180225, 5444517870735015415413993718908291383296)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('a'), Integer(2))), Mul(Rational(24623430962648187265, 36893488147419103232), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Mul(Integer(2), Symbol('y')), Rational(15727240259832744812057210812134365969663, 5444517870735015415413993718908291383296)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_421(a:sympy.Rational):
	#(a - z**2 + 6050831182542497717853286941518620410625/5444517870735015415413993718908291383296 < 0) & (36893488147419103232*a**2 - 24623430962648187265*a < 21171758130567760151913340805128333933823/147573952589676412928)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(6050831182542497717853286941518620410625, 5444517870735015415413993718908291383296)), Integer(0)), StrictLessThan(Add(Mul(Integer(36893488147419103232), Pow(Symbol('a'), Integer(2))), Mul(Integer(-1), Integer(24623430962648187265), Symbol('a'))), Rational(21171758130567760151913340805128333933823, 147573952589676412928)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_422(a:sympy.Rational):
	#(a < 813179152525346414339585835102428211193689/348449143727040986586495598010130648530944) & (a > 24623430962648187265/73786976294838206464 - sqrt(288230376151711743)/268435456)

	pre_cond = And(StrictLessThan(Symbol('a'), Rational(813179152525346414339585835102428211193689, 348449143727040986586495598010130648530944)), StrictGreaterThan(Symbol('a'), Add(Rational(24623430962648187265, 73786976294838206464), Mul(Integer(-1), Rational(1, 268435456), Pow(Integer(288230376151711743), Rational(1, 2))))))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_423(a:sympy.Rational):
	#(a + y**2 - z**2 + 606313352372301434184770344590508180225/5444517870735015415413993718908291383296 < 0) & (-a**2 + 24623430962648187265*a/36893488147419103232 - y**2 + 2*y + 15727240259832744812057210812134365969663/5444517870735015415413993718908291383296 > 0)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Pow(Symbol('y'), Integer(2)), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(606313352372301434184770344590508180225, 5444517870735015415413993718908291383296)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('a'), Integer(2))), Mul(Rational(24623430962648187265, 36893488147419103232), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Mul(Integer(2), Symbol('y')), Rational(15727240259832744812057210812134365969663, 5444517870735015415413993718908291383296)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_424(a:sympy.Rational):
	#(a - z**2 + 6050831182542497717853286941518620410625/5444517870735015415413993718908291383296 < 0) & (36893488147419103232*a**2 - 24623430962648187265*a < 21171758130567760151913340805128333933823/147573952589676412928)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(6050831182542497717853286941518620410625, 5444517870735015415413993718908291383296)), Integer(0)), StrictLessThan(Add(Mul(Integer(36893488147419103232), Pow(Symbol('a'), Integer(2))), Mul(Integer(-1), Integer(24623430962648187265), Symbol('a'))), Rational(21171758130567760151913340805128333933823, 147573952589676412928)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_425(a:sympy.Rational):
	#(a < 813179152525346414339585835102428211193689/348449143727040986586495598010130648530944) & (a > 24623430962648187265/73786976294838206464 - sqrt(288230376151711743)/268435456)

	pre_cond = And(StrictLessThan(Symbol('a'), Rational(813179152525346414339585835102428211193689, 348449143727040986586495598010130648530944)), StrictGreaterThan(Symbol('a'), Add(Rational(24623430962648187265, 73786976294838206464), Mul(Integer(-1), Rational(1, 268435456), Pow(Integer(288230376151711743), Rational(1, 2))))))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_426(a:sympy.Rational):
	#(a + y**2 - z**2 + 606313352372301434184770344590508180225/5444517870735015415413993718908291383296 < 0) & (-a**2 + 24623430962648187265*a/36893488147419103232 - y**2 + 2*y + 15727240259832744812057210812134365969663/5444517870735015415413993718908291383296 > 0)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Pow(Symbol('y'), Integer(2)), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(606313352372301434184770344590508180225, 5444517870735015415413993718908291383296)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('a'), Integer(2))), Mul(Rational(24623430962648187265, 36893488147419103232), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Mul(Integer(2), Symbol('y')), Rational(15727240259832744812057210812134365969663, 5444517870735015415413993718908291383296)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_427(a:sympy.Rational):
	#(a - z**2 + 6050831182542497717853286941518620410625/5444517870735015415413993718908291383296 < 0) & (36893488147419103232*a**2 - 24623430962648187265*a < 21171758130567760151913340805128333933823/147573952589676412928)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(6050831182542497717853286941518620410625, 5444517870735015415413993718908291383296)), Integer(0)), StrictLessThan(Add(Mul(Integer(36893488147419103232), Pow(Symbol('a'), Integer(2))), Mul(Integer(-1), Integer(24623430962648187265), Symbol('a'))), Rational(21171758130567760151913340805128333933823, 147573952589676412928)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_428(a:sympy.Rational):
	#(a < 813179152525346414339585835102428211193689/348449143727040986586495598010130648530944) & (a > 24623430962648187265/73786976294838206464 - sqrt(288230376151711743)/268435456)

	pre_cond = And(StrictLessThan(Symbol('a'), Rational(813179152525346414339585835102428211193689, 348449143727040986586495598010130648530944)), StrictGreaterThan(Symbol('a'), Add(Rational(24623430962648187265, 73786976294838206464), Mul(Integer(-1), Rational(1, 268435456), Pow(Integer(288230376151711743), Rational(1, 2))))))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_429(a:sympy.Rational):
	#(a + y**2 - z**2 + 606313352372301434184770344590508180225/5444517870735015415413993718908291383296 < 0) & (-a**2 + 24623430962648187265*a/36893488147419103232 - y**2 + 2*y + 15727240259832744812057210812134365969663/5444517870735015415413993718908291383296 > 0)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Pow(Symbol('y'), Integer(2)), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(606313352372301434184770344590508180225, 5444517870735015415413993718908291383296)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('a'), Integer(2))), Mul(Rational(24623430962648187265, 36893488147419103232), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Mul(Integer(2), Symbol('y')), Rational(15727240259832744812057210812134365969663, 5444517870735015415413993718908291383296)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_430(a:sympy.Rational):
	#(a - z**2 + 6050831182542497717853286941518620410625/5444517870735015415413993718908291383296 < 0) & (36893488147419103232*a**2 - 24623430962648187265*a < 21171758130567760151913340805128333933823/147573952589676412928)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(6050831182542497717853286941518620410625, 5444517870735015415413993718908291383296)), Integer(0)), StrictLessThan(Add(Mul(Integer(36893488147419103232), Pow(Symbol('a'), Integer(2))), Mul(Integer(-1), Integer(24623430962648187265), Symbol('a'))), Rational(21171758130567760151913340805128333933823, 147573952589676412928)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_431(a:sympy.Rational):
	#(a < 813179152525346414339585835102428211193689/348449143727040986586495598010130648530944) & (a > 24623430962648187265/73786976294838206464 - sqrt(288230376151711743)/268435456)

	pre_cond = And(StrictLessThan(Symbol('a'), Rational(813179152525346414339585835102428211193689, 348449143727040986586495598010130648530944)), StrictGreaterThan(Symbol('a'), Add(Rational(24623430962648187265, 73786976294838206464), Mul(Integer(-1), Rational(1, 268435456), Pow(Integer(288230376151711743), Rational(1, 2))))))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_432(a:sympy.Rational):
	#(a + y**2 - z**2 + 606313352372301434184770344590508180225/5444517870735015415413993718908291383296 < 0) & (-a**2 + 24623430962648187265*a/36893488147419103232 - y**2 + 2*y + 15727240259832744812057210812134365969663/5444517870735015415413993718908291383296 > 0)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Pow(Symbol('y'), Integer(2)), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(606313352372301434184770344590508180225, 5444517870735015415413993718908291383296)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('a'), Integer(2))), Mul(Rational(24623430962648187265, 36893488147419103232), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Mul(Integer(2), Symbol('y')), Rational(15727240259832744812057210812134365969663, 5444517870735015415413993718908291383296)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_433(a:sympy.Rational):
	#(a - z**2 + 6050831182542497717853286941518620410625/5444517870735015415413993718908291383296 < 0) & (36893488147419103232*a**2 - 24623430962648187265*a < 21171758130567760151913340805128333933823/147573952589676412928)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(6050831182542497717853286941518620410625, 5444517870735015415413993718908291383296)), Integer(0)), StrictLessThan(Add(Mul(Integer(36893488147419103232), Pow(Symbol('a'), Integer(2))), Mul(Integer(-1), Integer(24623430962648187265), Symbol('a'))), Rational(21171758130567760151913340805128333933823, 147573952589676412928)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_434(a:sympy.Rational):
	#(a < 813179152525346414339585835102428211193689/348449143727040986586495598010130648530944) & (a > 24623430962648187265/73786976294838206464 - sqrt(288230376151711743)/268435456)

	pre_cond = And(StrictLessThan(Symbol('a'), Rational(813179152525346414339585835102428211193689, 348449143727040986586495598010130648530944)), StrictGreaterThan(Symbol('a'), Add(Rational(24623430962648187265, 73786976294838206464), Mul(Integer(-1), Rational(1, 268435456), Pow(Integer(288230376151711743), Rational(1, 2))))))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_435(a:sympy.Rational):
	#(a + y**2 - z**2 + 606313352372301434184770344590508180225/5444517870735015415413993718908291383296 < 0) & (-a**2 + 24623430962648187265*a/36893488147419103232 - y**2 + 2*y + 15727240259832744812057210812134365969663/5444517870735015415413993718908291383296 > 0)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Pow(Symbol('y'), Integer(2)), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(606313352372301434184770344590508180225, 5444517870735015415413993718908291383296)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('a'), Integer(2))), Mul(Rational(24623430962648187265, 36893488147419103232), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Mul(Integer(2), Symbol('y')), Rational(15727240259832744812057210812134365969663, 5444517870735015415413993718908291383296)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_436(a:sympy.Rational):
	#(a - z**2 + 6050831182542497717853286941518620410625/5444517870735015415413993718908291383296 < 0) & (36893488147419103232*a**2 - 24623430962648187265*a < 21171758130567760151913340805128333933823/147573952589676412928)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(6050831182542497717853286941518620410625, 5444517870735015415413993718908291383296)), Integer(0)), StrictLessThan(Add(Mul(Integer(36893488147419103232), Pow(Symbol('a'), Integer(2))), Mul(Integer(-1), Integer(24623430962648187265), Symbol('a'))), Rational(21171758130567760151913340805128333933823, 147573952589676412928)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_437(a:sympy.Rational):
	#(a < 813179152525346414339585835102428211193689/348449143727040986586495598010130648530944) & (a > 24623430962648187265/73786976294838206464 - sqrt(288230376151711743)/268435456)

	pre_cond = And(StrictLessThan(Symbol('a'), Rational(813179152525346414339585835102428211193689, 348449143727040986586495598010130648530944)), StrictGreaterThan(Symbol('a'), Add(Rational(24623430962648187265, 73786976294838206464), Mul(Integer(-1), Rational(1, 268435456), Pow(Integer(288230376151711743), Rational(1, 2))))))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_438(a:sympy.Rational):
	#(a + y**2 - z**2 + 606313352372301434184770344590508180225/5444517870735015415413993718908291383296 < 0) & (-a**2 + 24623430962648187265*a/36893488147419103232 - y**2 + 2*y + 15727240259832744812057210812134365969663/5444517870735015415413993718908291383296 > 0)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Pow(Symbol('y'), Integer(2)), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(606313352372301434184770344590508180225, 5444517870735015415413993718908291383296)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('a'), Integer(2))), Mul(Rational(24623430962648187265, 36893488147419103232), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Mul(Integer(2), Symbol('y')), Rational(15727240259832744812057210812134365969663, 5444517870735015415413993718908291383296)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_439(a:sympy.Rational):
	#(a - z**2 + 6050831182542497717853286941518620410625/5444517870735015415413993718908291383296 < 0) & (36893488147419103232*a**2 - 24623430962648187265*a < 21171758130567760151913340805128333933823/147573952589676412928)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(6050831182542497717853286941518620410625, 5444517870735015415413993718908291383296)), Integer(0)), StrictLessThan(Add(Mul(Integer(36893488147419103232), Pow(Symbol('a'), Integer(2))), Mul(Integer(-1), Integer(24623430962648187265), Symbol('a'))), Rational(21171758130567760151913340805128333933823, 147573952589676412928)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_440(a:sympy.Rational):
	#(a < 813179152525346414339585835102428211193689/348449143727040986586495598010130648530944) & (a > 24623430962648187265/73786976294838206464 - sqrt(288230376151711743)/268435456)

	pre_cond = And(StrictLessThan(Symbol('a'), Rational(813179152525346414339585835102428211193689, 348449143727040986586495598010130648530944)), StrictGreaterThan(Symbol('a'), Add(Rational(24623430962648187265, 73786976294838206464), Mul(Integer(-1), Rational(1, 268435456), Pow(Integer(288230376151711743), Rational(1, 2))))))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_441(a:sympy.Rational):
	#(a + y**2 - z**2 + 606313352372301434184770344590508180225/5444517870735015415413993718908291383296 < 0) & (-a**2 + 24623430962648187265*a/36893488147419103232 - y**2 + 2*y + 15727240259832744812057210812134365969663/5444517870735015415413993718908291383296 > 0)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Pow(Symbol('y'), Integer(2)), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(606313352372301434184770344590508180225, 5444517870735015415413993718908291383296)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('a'), Integer(2))), Mul(Rational(24623430962648187265, 36893488147419103232), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Mul(Integer(2), Symbol('y')), Rational(15727240259832744812057210812134365969663, 5444517870735015415413993718908291383296)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_442(a:sympy.Rational):
	#(a - z**2 + 6050831182542497717853286941518620410625/5444517870735015415413993718908291383296 < 0) & (36893488147419103232*a**2 - 24623430962648187265*a < 21171758130567760151913340805128333933823/147573952589676412928)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(6050831182542497717853286941518620410625, 5444517870735015415413993718908291383296)), Integer(0)), StrictLessThan(Add(Mul(Integer(36893488147419103232), Pow(Symbol('a'), Integer(2))), Mul(Integer(-1), Integer(24623430962648187265), Symbol('a'))), Rational(21171758130567760151913340805128333933823, 147573952589676412928)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_443(a:sympy.Rational):
	#(a < 813179152525346414339585835102428211193689/348449143727040986586495598010130648530944) & (a > 24623430962648187265/73786976294838206464 - sqrt(288230376151711743)/268435456)

	pre_cond = And(StrictLessThan(Symbol('a'), Rational(813179152525346414339585835102428211193689, 348449143727040986586495598010130648530944)), StrictGreaterThan(Symbol('a'), Add(Rational(24623430962648187265, 73786976294838206464), Mul(Integer(-1), Rational(1, 268435456), Pow(Integer(288230376151711743), Rational(1, 2))))))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_444(a:sympy.Rational):
	#(a + y**2 - z**2 + 606313352372301434184770344590508180225/5444517870735015415413993718908291383296 < 0) & (-a**2 + 24623430962648187265*a/36893488147419103232 - y**2 + 2*y + 15727240259832744812057210812134365969663/5444517870735015415413993718908291383296 > 0)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Pow(Symbol('y'), Integer(2)), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(606313352372301434184770344590508180225, 5444517870735015415413993718908291383296)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('a'), Integer(2))), Mul(Rational(24623430962648187265, 36893488147419103232), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Mul(Integer(2), Symbol('y')), Rational(15727240259832744812057210812134365969663, 5444517870735015415413993718908291383296)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_445(a:sympy.Rational):
	#(a - z**2 + 6050831182542497717853286941518620410625/5444517870735015415413993718908291383296 < 0) & (36893488147419103232*a**2 - 24623430962648187265*a < 21171758130567760151913340805128333933823/147573952589676412928)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(6050831182542497717853286941518620410625, 5444517870735015415413993718908291383296)), Integer(0)), StrictLessThan(Add(Mul(Integer(36893488147419103232), Pow(Symbol('a'), Integer(2))), Mul(Integer(-1), Integer(24623430962648187265), Symbol('a'))), Rational(21171758130567760151913340805128333933823, 147573952589676412928)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_446(a:sympy.Rational):
	#(a < 813179152525346414339585835102428211193689/348449143727040986586495598010130648530944) & (a > 24623430962648187265/73786976294838206464 - sqrt(288230376151711743)/268435456)

	pre_cond = And(StrictLessThan(Symbol('a'), Rational(813179152525346414339585835102428211193689, 348449143727040986586495598010130648530944)), StrictGreaterThan(Symbol('a'), Add(Rational(24623430962648187265, 73786976294838206464), Mul(Integer(-1), Rational(1, 268435456), Pow(Integer(288230376151711743), Rational(1, 2))))))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_447(a:sympy.Rational):
	#(a + y**2 - z**2 + 606313352372301434184770344590508180225/5444517870735015415413993718908291383296 < 0) & (-a**2 + 24623430962648187265*a/36893488147419103232 - y**2 + 2*y + 15727240259832744812057210812134365969663/5444517870735015415413993718908291383296 > 0)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Pow(Symbol('y'), Integer(2)), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(606313352372301434184770344590508180225, 5444517870735015415413993718908291383296)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(-1), Pow(Symbol('a'), Integer(2))), Mul(Rational(24623430962648187265, 36893488147419103232), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Mul(Integer(2), Symbol('y')), Rational(15727240259832744812057210812134365969663, 5444517870735015415413993718908291383296)), Integer(0)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_448(a:sympy.Rational):
	#(a - z**2 + 6050831182542497717853286941518620410625/5444517870735015415413993718908291383296 < 0) & (36893488147419103232*a**2 - 24623430962648187265*a < 21171758130567760151913340805128333933823/147573952589676412928)

	pre_cond = And(StrictLessThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))), Rational(6050831182542497717853286941518620410625, 5444517870735015415413993718908291383296)), Integer(0)), StrictLessThan(Add(Mul(Integer(36893488147419103232), Pow(Symbol('a'), Integer(2))), Mul(Integer(-1), Integer(24623430962648187265), Symbol('a'))), Rational(21171758130567760151913340805128333933823, 147573952589676412928)))

	eval = pre_cond.subs( { 'a':a })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_449(a:sympy.Rational):