import sympy
from sympy import *

def pre_condition_0(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 1/4 > 0) & (-a + y**2 + z**2 + 1/4 < 0) & (4*a - y**3 + 2*y - 1/4 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(1, 4)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(1, 4)), Integer(0)), StrictGreaterThan(Add(Mul(Integer(4), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-1, 4)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_1(a:sympy.Rational,b:sympy.Rational):
	#(a > 1/2048) & (-b + z**2 + 17/64 > 0) & (-a + z**2 + 17/64 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(1, 2048)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(17, 64)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(17, 64)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_2(a:sympy.Rational,b:sympy.Rational):
	#(a > 33/64) & (b < 33/64)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(33, 64)), StrictLessThan(Symbol('b'), Rational(33, 64)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_3(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 > 0) & (-a + y**2 + z**2 < 0) & (3*a - y**3 + 2*y > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2))), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2))), Integer(0)), StrictGreaterThan(Add(Mul(Integer(3), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y'))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_4(a:sympy.Rational,b:sympy.Rational):
	#(a > 0) & (a - z**2 > 0) & (b - z**2 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(0)), StrictGreaterThan(Add(Symbol('a'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2)))), Integer(0)), StrictLessThan(Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('z'), Integer(2)))), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_5(a:sympy.Rational,b:sympy.Rational):
	#(a > 0) & (b < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Integer(0)), StrictLessThan(Symbol('b'), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_6(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 1/4096 > 0) & (-a + y**2 + z**2 + 1/4096 < 0) & (97*a/32 - y**3 + 2*y - 1/4096 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(1, 4096)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(1, 4096)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(97, 32), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-1, 4096)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_7(a:sympy.Rational,b:sympy.Rational):
	#(a > 1/12416) & (-b + z**2 + 1/4096 > 0) & (-a + z**2 + 1/4096 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(1, 12416)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(1, 4096)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(1, 4096)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_8(a:sympy.Rational,b:sympy.Rational):
	#(a > 1/4096) & (b < 1/4096)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(1, 4096)), StrictLessThan(Symbol('b'), Rational(1, 4096)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_9(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 25/65536 > 0) & (-a + y**2 + z**2 + 25/65536 < 0) & (389*a/128 - y**3 + 2*y - 25/65536 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(25, 65536)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(25, 65536)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(389, 128), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-25, 65536)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_10(a:sympy.Rational,b:sympy.Rational):
	#(a > 25/199168) & (-b + z**2 + 25/65536 > 0) & (-a + z**2 + 25/65536 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(25, 199168)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(25, 65536)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(25, 65536)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_11(a:sympy.Rational,b:sympy.Rational):
	#(a > 25/65536) & (b < 25/65536)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(25, 65536)), StrictLessThan(Symbol('b'), Rational(25, 65536)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_12(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 121/262144 > 0) & (-a + y**2 + z**2 + 121/262144 < 0) & (779*a/256 - y**3 + 2*y - 121/262144 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(121, 262144)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(121, 262144)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(779, 256), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-121, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_13(a:sympy.Rational,b:sympy.Rational):
	#(a > 121/797696) & (-b + z**2 + 121/262144 > 0) & (-a + z**2 + 121/262144 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(121, 797696)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(121, 262144)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(121, 262144)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_14(a:sympy.Rational,b:sympy.Rational):
	#(a > 121/262144) & (b < 121/262144)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(121, 262144)), StrictLessThan(Symbol('b'), Rational(121, 262144)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_15(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 441/1048576 > 0) & (-a + y**2 + z**2 + 441/1048576 < 0) & (1557*a/512 - y**3 + 2*y - 441/1048576 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(441, 1048576)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(441, 1048576)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(1557, 512), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-441, 1048576)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_16(a:sympy.Rational,b:sympy.Rational):
	#(a > 12001279/26122125312) & (-b + z**2 + 1765/4194304 > 0) & (-a + z**2 + 1765/4194304 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(12001279, 26122125312)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(1765, 4194304)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(1765, 4194304)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_17(a:sympy.Rational,b:sympy.Rational):
	#(a > 12001279/26122125312) & (b < 1765/4194304)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(12001279, 26122125312)), StrictLessThan(Symbol('b'), Rational(1765, 4194304)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_18(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 8944542635210386846111922166693889/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 8944542635210386846111922166693889/21267647932558653966460912964485513216 < 0) & (7012104619815862273*a/2305843009213693952 - y**3 + 2*y - 8944542635210386846111922166693889/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(8944542635210386846111922166693889, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(8944542635210386846111922166693889, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012104619815862273, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-8944542635210386846111922166693889, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_19(a:sympy.Rational,b:sympy.Rational):
	#(a > 4244818227638516969924765383617975/9239321381415687564314176330517184512) & (-b + z**2 + 8949613237611299763717908979515393/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 8949613237611299763717908979515393/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(4244818227638516969924765383617975, 9239321381415687564314176330517184512)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(8949613237611299763717908979515393, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(8949613237611299763717908979515393, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_20(a:sympy.Rational,b:sympy.Rational):
	#(a > 4244818227638516969924765383617975/9239321381415687564314176330517184512) & (b < 8949613237611299763717908979515393/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(4244818227638516969924765383617975, 9239321381415687564314176330517184512)), StrictLessThan(Symbol('b'), Rational(8949613237611299763717908979515393, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_21(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 8944542635210386846111922166693889/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 8944542635210386846111922166693889/21267647932558653966460912964485513216 < 0) & (7012104619815862273*a/2305843009213693952 - y**3 + 2*y - 8944542635210386846111922166693889/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(8944542635210386846111922166693889, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(8944542635210386846111922166693889, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012104619815862273, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-8944542635210386846111922166693889, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_22(a:sympy.Rational,b:sympy.Rational):
	#(a > 4244818227638516969924765383617975/9239321381415687564314176330517184512) & (-b + z**2 + 8949613237611299763717908979515393/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 8949613237611299763717908979515393/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(4244818227638516969924765383617975, 9239321381415687564314176330517184512)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(8949613237611299763717908979515393, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(8949613237611299763717908979515393, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_23(a:sympy.Rational,b:sympy.Rational):
	#(a > 4244818227638516969924765383617975/9239321381415687564314176330517184512) & (b < 8949613237611299763717908979515393/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(4244818227638516969924765383617975, 9239321381415687564314176330517184512)), StrictLessThan(Symbol('b'), Rational(8949613237611299763717908979515393, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_24(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 1849/4194304 > 0) & (-a + y**2 + z**2 + 1849/4194304 < 0) & (3115*a/1024 - y**3 + 2*y - 1849/4194304 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(1849, 4194304)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(1849, 4194304)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(3115, 1024), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-1849, 4194304)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_25(a:sympy.Rational,b:sympy.Rational):
	#(a > 1849/12759040) & (-b + z**2 + 1849/4194304 > 0) & (-a + z**2 + 1849/4194304 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(1849, 12759040)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(1849, 4194304)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(1849, 4194304)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_26(a:sympy.Rational,b:sympy.Rational):
	#(a > 1849/4194304) & (b < 1849/4194304)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(1849, 4194304)), StrictLessThan(Symbol('b'), Rational(1849, 4194304)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_27(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 28561/67108864 > 0) & (-a + y**2 + z**2 + 28561/67108864 < 0) & (12457*a/4096 - y**3 + 2*y - 28561/67108864 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(28561, 67108864)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(28561, 67108864)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(12457, 4096), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-28561, 67108864)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_28(a:sympy.Rational,b:sympy.Rational):
	#(a > 5629869737/13375601901568) & (-b + z**2 + 114293/268435456 > 0) & (-a + z**2 + 114293/268435456 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(5629869737, 13375601901568)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(114293, 268435456)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(114293, 268435456)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_29(a:sympy.Rational,b:sympy.Rational):
	#(a > 114293/268435456) & (b < 114293/268435456)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(114293, 268435456)), StrictLessThan(Symbol('b'), Rational(114293, 268435456)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_30(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_31(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_32(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_33(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_34(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_35(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_36(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_37(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_38(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_39(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_40(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_41(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_42(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_43(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_44(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_45(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_46(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_47(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_48(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_49(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_50(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_51(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_52(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_53(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_54(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_55(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_56(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_57(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_58(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_59(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_60(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_61(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_62(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_63(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_64(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_65(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_66(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_67(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_68(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_69(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_70(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_71(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_72(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_73(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_74(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_75(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_76(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_77(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_78(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_79(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_80(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_81(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_82(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_83(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_84(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_85(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_86(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_87(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_88(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_89(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_90(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_91(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_92(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_93(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_94(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_95(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_96(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_97(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_98(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_99(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_100(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_101(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_102(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_103(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_104(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_105(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_106(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_107(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_108(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_109(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_110(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_111(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_112(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_113(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_114(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_115(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_116(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_117(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_118(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_119(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_120(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_121(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_122(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_123(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_124(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_125(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_126(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_127(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_128(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_129(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_130(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_131(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_132(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_133(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_134(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_135(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_136(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_137(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_138(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_139(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_140(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_141(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_142(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_143(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_144(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_145(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_146(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_147(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_148(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_149(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_150(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_151(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_152(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_153(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_154(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_155(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_156(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_157(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_158(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_159(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_160(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_161(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_162(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_163(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_164(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_165(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_166(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_167(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_168(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_169(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_170(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_171(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_172(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_173(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_174(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_175(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_176(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_177(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_178(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_179(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_180(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_181(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_182(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_183(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_184(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_185(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_186(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_187(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_188(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_189(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_190(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_191(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_192(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_193(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_194(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_195(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_196(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_197(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_198(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_199(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_200(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_201(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_202(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_203(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_204(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_205(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_206(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_207(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_208(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_209(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_210(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_211(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_212(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_213(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_214(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_215(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_216(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_217(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_218(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_219(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_220(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_221(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_222(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_223(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_224(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_225(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_226(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_227(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_228(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_229(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_230(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_231(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_232(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_233(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_234(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_235(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_236(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_237(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_238(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_239(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_240(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_241(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_242(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_243(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_244(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_245(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_246(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_247(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_248(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_249(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_250(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_251(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_252(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_253(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_254(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_255(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_256(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_257(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_258(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_259(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_260(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_261(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_262(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_263(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_264(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_265(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_266(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_267(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_268(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_269(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_270(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_271(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_272(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_273(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_274(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_275(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_276(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_277(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_278(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_279(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_280(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_281(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_282(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_283(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_284(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_285(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_286(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_287(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_288(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_289(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_290(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_291(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_292(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_293(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_294(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_295(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_296(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_297(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_298(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_299(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_300(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_301(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_302(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_303(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_304(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_305(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_306(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_307(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_308(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_309(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_310(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_311(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_312(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_313(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_314(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_315(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_316(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_317(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_318(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_319(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_320(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_321(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_322(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_323(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_324(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_325(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_326(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_327(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_328(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_329(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_330(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_331(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_332(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_333(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_334(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_335(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_336(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_337(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_338(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_339(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_340(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_341(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_342(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_343(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_344(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_345(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_346(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_347(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_348(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_349(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_350(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_351(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_352(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_353(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_354(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_355(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_356(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_357(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_358(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_359(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_360(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_361(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_362(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_363(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_364(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_365(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_366(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_367(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_368(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_369(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_370(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_371(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_372(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_373(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_374(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_375(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_376(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_377(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_378(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_379(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_380(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_381(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_382(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_383(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_384(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_385(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_386(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_387(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_388(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_389(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_390(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_391(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_392(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_393(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_394(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_395(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_396(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_397(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_398(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_399(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_400(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_401(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_402(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_403(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_404(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_405(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_406(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_407(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_408(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_409(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_410(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_411(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_412(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_413(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_414(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_415(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_416(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_417(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_418(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_419(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_420(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_421(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_422(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_423(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_424(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_425(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_426(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_427(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_428(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_429(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_430(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_431(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_432(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_433(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_434(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_435(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_436(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_437(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_438(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_439(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_440(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_441(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_442(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_443(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_444(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_445(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_446(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_447(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_448(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_449(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_450(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_451(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_452(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_453(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_454(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_455(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_456(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_457(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_458(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_459(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_460(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_461(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_462(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_463(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_464(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_465(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_466(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_467(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_468(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_469(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_470(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_471(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_472(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_473(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_474(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_475(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_476(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_477(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_478(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_479(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_480(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_481(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_482(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_483(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_484(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_485(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_486(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_487(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_488(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_489(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_490(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_491(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_492(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_493(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_494(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_495(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_496(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_497(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_498(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_499(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_500(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_501(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_502(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_503(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_504(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_505(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_506(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_507(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_508(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_509(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_510(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_511(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_512(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_513(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_514(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_515(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_516(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_517(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_518(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_519(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_520(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_521(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_522(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_523(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_524(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_525(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_526(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_527(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_528(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_529(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_530(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_531(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_532(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_533(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_534(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_535(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_536(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_537(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_538(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_539(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_540(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_541(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_542(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_543(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_544(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_545(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_546(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_547(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_548(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_549(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_550(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_551(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_552(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_553(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_554(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_555(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_556(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_557(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_558(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_559(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_560(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_561(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_562(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_563(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_564(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_565(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_566(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_567(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_568(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_569(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_570(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_571(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_572(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_573(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_574(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_575(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_576(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_577(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_578(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_579(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_580(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_581(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_582(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_583(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_584(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_585(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_586(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_587(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_588(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_589(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_590(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_591(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_592(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_593(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_594(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_595(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_596(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_597(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_598(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_599(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_600(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_601(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_602(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_603(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_604(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_605(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_606(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_607(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_608(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_609(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_610(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_611(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_612(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_613(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_614(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_615(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_616(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_617(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_618(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_619(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_620(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_621(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_622(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_623(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_624(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_625(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_626(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_627(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_628(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_629(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_630(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_631(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_632(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_633(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_634(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_635(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_636(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_637(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_638(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_639(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_640(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_641(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_642(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_643(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_644(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_645(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_646(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_647(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_648(a:sympy.Rational,b:sympy.Rational):
	#(-b + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0) & (-a + y**2 + z**2 + 9051342198279614793759750805782529/21267647932558653966460912964485513216 < 0) & (7012667569769283583*a/2305843009213693952 - y**3 + 2*y - 9051342198279614793759750805782529/21267647932558653966460912964485513216 > 0)

	pre_cond = And(StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)), Rational(9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)), StrictGreaterThan(Add(Mul(Rational(7012667569769283583, 2305843009213693952), Symbol('a')), Mul(Integer(-1), Pow(Symbol('y'), Integer(3))), Mul(Integer(2), Symbol('y')), Rational(-9051342198279614793759750805782529, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_649(a:sympy.Rational,b:sympy.Rational):
	#(a > 27224379544505286982345260261179393/64680441966768347759381020736239960064) & (-b + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 > 0) & (-a + z**2 + 9055224378242813746301834459348993/21267647932558653966460912964485513216 < 0)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(27224379544505286982345260261179393, 64680441966768347759381020736239960064)), StrictGreaterThan(Add(Mul(Integer(-1), Symbol('b')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)), StrictLessThan(Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('z'), Integer(2)), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), Integer(0)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def pre_condition_650(a:sympy.Rational,b:sympy.Rational):
	#(a > 9055224378242813746301834459348993/21267647932558653966460912964485513216) & (b < 9055224378242813746301834459348993/21267647932558653966460912964485513216)

	pre_cond = And(StrictGreaterThan(Symbol('a'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)), StrictLessThan(Symbol('b'), Rational(9055224378242813746301834459348993, 21267647932558653966460912964485513216)))

	eval = pre_cond.subs( { 'a':a, 'b':b })

	if eval==True:
		assert eval!=False
		return True
	return False


def post_condition(a:sympy.Rational, b:sympy.Rational, x:sympy.Rational, y:sympy.Rational, z:sympy.Rational):
	# (0 > -a + x**2 + y**2 + z**2) & (0 > b - x**2 - y**2 - z**2) & (0 > -2*a*x - 3*a + x**2 + y**3 - 2*y)

	post_cond =  And(StrictGreaterThan(Integer(0), Add(Mul(Integer(-1), Symbol('a')), Pow(Symbol('x'), Integer(2)), Pow(Symbol('y'), Integer(2)), Pow(Symbol('z'), Integer(2)))), StrictGreaterThan(Integer(0), Add(Symbol('b'), Mul(Integer(-1), Pow(Symbol('x'), Integer(2))), Mul(Integer(-1), Pow(Symbol('y'), Integer(2))), Mul(Integer(-1), Pow(Symbol('z'), Integer(2))))), StrictGreaterThan(Integer(0), Add(Mul(Integer(-1), Integer(2), Symbol('a'), Symbol('x')), Mul(Integer(-1), Integer(3), Symbol('a')), Pow(Symbol('x'), Integer(2)), Pow(Symbol('y'), Integer(3)), Mul(Integer(-1), Integer(2), Symbol('y')))))

	eval = post_cond.subs( { 'a':a, 'b':b, 'x':x, 'y':y, 'z':z })

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
		print('x = 1/2')
		print('y = 1/8')
		print('z = -1/2')
		print('a = 2')
		print('b = -31/64')
		exit(0)
	
	
	if pre_condition_1(a=a,b=b)==True:
		print("pre_condition_1 SAT")
		print('x = 1/2')
		print('y = 1/8')
		print('z = -1/2')
		print('a = 2')
		print('b = -31/64')
		exit(0)
	
	
	if pre_condition_2(a=a,b=b)==True:
		print("pre_condition_2 SAT")
		print('x = 1/2')
		print('y = 1/8')
		print('z = -1/2')
		print('a = 2')
		print('b = -31/64')
		exit(0)
	
	
	if pre_condition_3(a=a,b=b)==True:
		print("pre_condition_3 SAT")
		print('x = 0')
		print('y = 0')
		print('z = 0')
		print('a = 1/2048')
		print('b = -1')
		exit(0)
	
	
	if pre_condition_4(a=a,b=b)==True:
		print("pre_condition_4 SAT")
		print('x = 0')
		print('y = 0')
		print('z = 0')
		print('a = 1/2048')
		print('b = -1')
		exit(0)
	
	
	if pre_condition_5(a=a,b=b)==True:
		print("pre_condition_5 SAT")
		print('x = 0')
		print('y = 0')
		print('z = 0')
		print('a = 1/2048')
		print('b = -1')
		exit(0)
	
	
	if pre_condition_6(a=a,b=b)==True:
		print("pre_condition_6 SAT")
		print('x = 1/64')
		print('y = 0')
		print('z = 0')
		print('a = 3/8192')
		print('b = 1/8192')
		exit(0)
	
	
	if pre_condition_7(a=a,b=b)==True:
		print("pre_condition_7 SAT")
		print('x = 1/64')
		print('y = 0')
		print('z = 0')
		print('a = 3/8192')
		print('b = 1/8192')
		exit(0)
	
	
	if pre_condition_8(a=a,b=b)==True:
		print("pre_condition_8 SAT")
		print('x = 1/64')
		print('y = 0')
		print('z = 0')
		print('a = 3/8192')
		print('b = 1/8192')
		exit(0)
	
	
	if pre_condition_9(a=a,b=b)==True:
		print("pre_condition_9 SAT")
		print('x = 5/256')
		print('y = 0')
		print('z = 0')
		print('a = 7/16384')
		print('b = 3/8192')
		exit(0)
	
	
	if pre_condition_10(a=a,b=b)==True:
		print("pre_condition_10 SAT")
		print('x = 5/256')
		print('y = 0')
		print('z = 0')
		print('a = 7/16384')
		print('b = 3/8192')
		exit(0)
	
	
	if pre_condition_11(a=a,b=b)==True:
		print("pre_condition_11 SAT")
		print('x = 5/256')
		print('y = 0')
		print('z = 0')
		print('a = 7/16384')
		print('b = 3/8192')
		exit(0)
	
	
	if pre_condition_12(a=a,b=b)==True:
		print("pre_condition_12 SAT")
		print('x = 11/512')
		print('y = 0')
		print('z = 0')
		print('a = 31/65536')
		print('b = 7/16384')
		exit(0)
	
	
	if pre_condition_13(a=a,b=b)==True:
		print("pre_condition_13 SAT")
		print('x = 11/512')
		print('y = 0')
		print('z = 0')
		print('a = 31/65536')
		print('b = 7/16384')
		exit(0)
	
	
	if pre_condition_14(a=a,b=b)==True:
		print("pre_condition_14 SAT")
		print('x = 11/512')
		print('y = 0')
		print('z = 0')
		print('a = 31/65536')
		print('b = 7/16384')
		exit(0)
	
	
	if pre_condition_15(a=a,b=b)==True:
		print("pre_condition_15 SAT")
		print('x = 21/1024')
		print('y = -1/2048')
		print('z = 0')
		print('a = 241/524288')
		print('b = 13/32768')
		exit(0)
	
	
	if pre_condition_16(a=a,b=b)==True:
		print("pre_condition_16 SAT")
		print('x = 21/1024')
		print('y = -1/2048')
		print('z = 0')
		print('a = 241/524288')
		print('b = 13/32768')
		exit(0)
	
	
	if pre_condition_17(a=a,b=b)==True:
		print("pre_condition_17 SAT")
		print('x = 21/1024')
		print('y = -1/2048')
		print('z = 0')
		print('a = 241/524288')
		print('b = 13/32768')
		exit(0)
	
	
	if pre_condition_18(a=a,b=b)==True:
		print("pre_condition_18 SAT")
		print('x = 94575592174780417/4611686018427387904')
		print('y = -1/2048')
		print('z = 0')
		print('a = 271199400050022877/590295810358705651712')
		print('b = 62100416736788481/147573952589676412928')
		exit(0)
	
	
	if pre_condition_19(a=a,b=b)==True:
		print("pre_condition_19 SAT")
		print('x = 94575592174780417/4611686018427387904')
		print('y = -1/2048')
		print('z = 0')
		print('a = 271199400050022877/590295810358705651712')
		print('b = 62100416736788481/147573952589676412928')
		exit(0)
	
	
	if pre_condition_20(a=a,b=b)==True:
		print("pre_condition_20 SAT")
		print('x = 94575592174780417/4611686018427387904')
		print('y = -1/2048')
		print('z = 0')
		print('a = 271199400050022877/590295810358705651712')
		print('b = 62100416736788481/147573952589676412928')
		exit(0)
	
	
	if pre_condition_21(a=a,b=b)==True:
		print("pre_condition_21 SAT")
		print('x = 94575592174780417/4611686018427387904')
		print('y = -1/2048')
		print('z = 0')
		print('a = 271199400050022877/590295810358705651712')
		print('b = 62100416736788481/147573952589676412928')
		exit(0)
	
	
	if pre_condition_22(a=a,b=b)==True:
		print("pre_condition_22 SAT")
		print('x = 94575592174780417/4611686018427387904')
		print('y = -1/2048')
		print('z = 0')
		print('a = 271199400050022877/590295810358705651712')
		print('b = 62100416736788481/147573952589676412928')
		exit(0)
	
	
	if pre_condition_23(a=a,b=b)==True:
		print("pre_condition_23 SAT")
		print('x = 94575592174780417/4611686018427387904')
		print('y = -1/2048')
		print('z = 0')
		print('a = 271199400050022877/590295810358705651712')
		print('b = 62100416736788481/147573952589676412928')
		exit(0)
	
	
	if pre_condition_24(a=a,b=b)==True:
		print("pre_condition_24 SAT")
		print('x = 43/2048')
		print('y = 0')
		print('z = 0')
		print('a = 15/32768')
		print('b = 7/16384')
		exit(0)
	
	
	if pre_condition_25(a=a,b=b)==True:
		print("pre_condition_25 SAT")
		print('x = 43/2048')
		print('y = 0')
		print('z = 0')
		print('a = 15/32768')
		print('b = 7/16384')
		exit(0)
	
	
	if pre_condition_26(a=a,b=b)==True:
		print("pre_condition_26 SAT")
		print('x = 43/2048')
		print('y = 0')
		print('z = 0')
		print('a = 15/32768')
		print('b = 7/16384')
		exit(0)
	
	
	if pre_condition_27(a=a,b=b)==True:
		print("pre_condition_27 SAT")
		print('x = 169/8192')
		print('y = -7/16384')
		print('z = 0')
		print('a = 893/2097152')
		print('b = 111/262144')
		exit(0)
	
	
	if pre_condition_28(a=a,b=b)==True:
		print("pre_condition_28 SAT")
		print('x = 169/8192')
		print('y = -7/16384')
		print('z = 0')
		print('a = 893/2097152')
		print('b = 111/262144')
		exit(0)
	
	
	if pre_condition_29(a=a,b=b)==True:
		print("pre_condition_29 SAT")
		print('x = 169/8192')
		print('y = -7/16384')
		print('z = 0')
		print('a = 893/2097152')
		print('b = 111/262144')
		exit(0)
	
	
	if pre_condition_30(a=a,b=b)==True:
		print("pre_condition_30 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_31(a=a,b=b)==True:
		print("pre_condition_31 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_32(a=a,b=b)==True:
		print("pre_condition_32 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_33(a=a,b=b)==True:
		print("pre_condition_33 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_34(a=a,b=b)==True:
		print("pre_condition_34 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_35(a=a,b=b)==True:
		print("pre_condition_35 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_36(a=a,b=b)==True:
		print("pre_condition_36 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_37(a=a,b=b)==True:
		print("pre_condition_37 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_38(a=a,b=b)==True:
		print("pre_condition_38 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_39(a=a,b=b)==True:
		print("pre_condition_39 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_40(a=a,b=b)==True:
		print("pre_condition_40 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_41(a=a,b=b)==True:
		print("pre_condition_41 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_42(a=a,b=b)==True:
		print("pre_condition_42 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_43(a=a,b=b)==True:
		print("pre_condition_43 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_44(a=a,b=b)==True:
		print("pre_condition_44 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_45(a=a,b=b)==True:
		print("pre_condition_45 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_46(a=a,b=b)==True:
		print("pre_condition_46 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_47(a=a,b=b)==True:
		print("pre_condition_47 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_48(a=a,b=b)==True:
		print("pre_condition_48 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_49(a=a,b=b)==True:
		print("pre_condition_49 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_50(a=a,b=b)==True:
		print("pre_condition_50 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_51(a=a,b=b)==True:
		print("pre_condition_51 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_52(a=a,b=b)==True:
		print("pre_condition_52 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_53(a=a,b=b)==True:
		print("pre_condition_53 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_54(a=a,b=b)==True:
		print("pre_condition_54 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_55(a=a,b=b)==True:
		print("pre_condition_55 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_56(a=a,b=b)==True:
		print("pre_condition_56 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_57(a=a,b=b)==True:
		print("pre_condition_57 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_58(a=a,b=b)==True:
		print("pre_condition_58 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_59(a=a,b=b)==True:
		print("pre_condition_59 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_60(a=a,b=b)==True:
		print("pre_condition_60 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_61(a=a,b=b)==True:
		print("pre_condition_61 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_62(a=a,b=b)==True:
		print("pre_condition_62 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_63(a=a,b=b)==True:
		print("pre_condition_63 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_64(a=a,b=b)==True:
		print("pre_condition_64 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_65(a=a,b=b)==True:
		print("pre_condition_65 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_66(a=a,b=b)==True:
		print("pre_condition_66 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_67(a=a,b=b)==True:
		print("pre_condition_67 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_68(a=a,b=b)==True:
		print("pre_condition_68 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_69(a=a,b=b)==True:
		print("pre_condition_69 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_70(a=a,b=b)==True:
		print("pre_condition_70 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_71(a=a,b=b)==True:
		print("pre_condition_71 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_72(a=a,b=b)==True:
		print("pre_condition_72 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_73(a=a,b=b)==True:
		print("pre_condition_73 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_74(a=a,b=b)==True:
		print("pre_condition_74 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_75(a=a,b=b)==True:
		print("pre_condition_75 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_76(a=a,b=b)==True:
		print("pre_condition_76 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_77(a=a,b=b)==True:
		print("pre_condition_77 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_78(a=a,b=b)==True:
		print("pre_condition_78 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_79(a=a,b=b)==True:
		print("pre_condition_79 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_80(a=a,b=b)==True:
		print("pre_condition_80 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_81(a=a,b=b)==True:
		print("pre_condition_81 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_82(a=a,b=b)==True:
		print("pre_condition_82 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_83(a=a,b=b)==True:
		print("pre_condition_83 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_84(a=a,b=b)==True:
		print("pre_condition_84 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_85(a=a,b=b)==True:
		print("pre_condition_85 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_86(a=a,b=b)==True:
		print("pre_condition_86 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_87(a=a,b=b)==True:
		print("pre_condition_87 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_88(a=a,b=b)==True:
		print("pre_condition_88 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_89(a=a,b=b)==True:
		print("pre_condition_89 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_90(a=a,b=b)==True:
		print("pre_condition_90 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_91(a=a,b=b)==True:
		print("pre_condition_91 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_92(a=a,b=b)==True:
		print("pre_condition_92 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_93(a=a,b=b)==True:
		print("pre_condition_93 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_94(a=a,b=b)==True:
		print("pre_condition_94 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_95(a=a,b=b)==True:
		print("pre_condition_95 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_96(a=a,b=b)==True:
		print("pre_condition_96 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_97(a=a,b=b)==True:
		print("pre_condition_97 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_98(a=a,b=b)==True:
		print("pre_condition_98 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_99(a=a,b=b)==True:
		print("pre_condition_99 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_100(a=a,b=b)==True:
		print("pre_condition_100 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_101(a=a,b=b)==True:
		print("pre_condition_101 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_102(a=a,b=b)==True:
		print("pre_condition_102 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_103(a=a,b=b)==True:
		print("pre_condition_103 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_104(a=a,b=b)==True:
		print("pre_condition_104 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_105(a=a,b=b)==True:
		print("pre_condition_105 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_106(a=a,b=b)==True:
		print("pre_condition_106 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_107(a=a,b=b)==True:
		print("pre_condition_107 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_108(a=a,b=b)==True:
		print("pre_condition_108 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_109(a=a,b=b)==True:
		print("pre_condition_109 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_110(a=a,b=b)==True:
		print("pre_condition_110 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_111(a=a,b=b)==True:
		print("pre_condition_111 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_112(a=a,b=b)==True:
		print("pre_condition_112 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_113(a=a,b=b)==True:
		print("pre_condition_113 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_114(a=a,b=b)==True:
		print("pre_condition_114 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_115(a=a,b=b)==True:
		print("pre_condition_115 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_116(a=a,b=b)==True:
		print("pre_condition_116 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_117(a=a,b=b)==True:
		print("pre_condition_117 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_118(a=a,b=b)==True:
		print("pre_condition_118 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_119(a=a,b=b)==True:
		print("pre_condition_119 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_120(a=a,b=b)==True:
		print("pre_condition_120 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_121(a=a,b=b)==True:
		print("pre_condition_121 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_122(a=a,b=b)==True:
		print("pre_condition_122 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_123(a=a,b=b)==True:
		print("pre_condition_123 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_124(a=a,b=b)==True:
		print("pre_condition_124 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_125(a=a,b=b)==True:
		print("pre_condition_125 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_126(a=a,b=b)==True:
		print("pre_condition_126 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_127(a=a,b=b)==True:
		print("pre_condition_127 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_128(a=a,b=b)==True:
		print("pre_condition_128 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_129(a=a,b=b)==True:
		print("pre_condition_129 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_130(a=a,b=b)==True:
		print("pre_condition_130 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_131(a=a,b=b)==True:
		print("pre_condition_131 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_132(a=a,b=b)==True:
		print("pre_condition_132 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_133(a=a,b=b)==True:
		print("pre_condition_133 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_134(a=a,b=b)==True:
		print("pre_condition_134 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_135(a=a,b=b)==True:
		print("pre_condition_135 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_136(a=a,b=b)==True:
		print("pre_condition_136 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_137(a=a,b=b)==True:
		print("pre_condition_137 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_138(a=a,b=b)==True:
		print("pre_condition_138 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_139(a=a,b=b)==True:
		print("pre_condition_139 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_140(a=a,b=b)==True:
		print("pre_condition_140 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_141(a=a,b=b)==True:
		print("pre_condition_141 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_142(a=a,b=b)==True:
		print("pre_condition_142 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_143(a=a,b=b)==True:
		print("pre_condition_143 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_144(a=a,b=b)==True:
		print("pre_condition_144 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_145(a=a,b=b)==True:
		print("pre_condition_145 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_146(a=a,b=b)==True:
		print("pre_condition_146 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_147(a=a,b=b)==True:
		print("pre_condition_147 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_148(a=a,b=b)==True:
		print("pre_condition_148 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_149(a=a,b=b)==True:
		print("pre_condition_149 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_150(a=a,b=b)==True:
		print("pre_condition_150 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_151(a=a,b=b)==True:
		print("pre_condition_151 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_152(a=a,b=b)==True:
		print("pre_condition_152 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_153(a=a,b=b)==True:
		print("pre_condition_153 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_154(a=a,b=b)==True:
		print("pre_condition_154 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_155(a=a,b=b)==True:
		print("pre_condition_155 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_156(a=a,b=b)==True:
		print("pre_condition_156 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_157(a=a,b=b)==True:
		print("pre_condition_157 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_158(a=a,b=b)==True:
		print("pre_condition_158 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_159(a=a,b=b)==True:
		print("pre_condition_159 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_160(a=a,b=b)==True:
		print("pre_condition_160 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_161(a=a,b=b)==True:
		print("pre_condition_161 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_162(a=a,b=b)==True:
		print("pre_condition_162 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_163(a=a,b=b)==True:
		print("pre_condition_163 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_164(a=a,b=b)==True:
		print("pre_condition_164 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_165(a=a,b=b)==True:
		print("pre_condition_165 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_166(a=a,b=b)==True:
		print("pre_condition_166 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_167(a=a,b=b)==True:
		print("pre_condition_167 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_168(a=a,b=b)==True:
		print("pre_condition_168 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_169(a=a,b=b)==True:
		print("pre_condition_169 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_170(a=a,b=b)==True:
		print("pre_condition_170 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_171(a=a,b=b)==True:
		print("pre_condition_171 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_172(a=a,b=b)==True:
		print("pre_condition_172 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_173(a=a,b=b)==True:
		print("pre_condition_173 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_174(a=a,b=b)==True:
		print("pre_condition_174 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_175(a=a,b=b)==True:
		print("pre_condition_175 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_176(a=a,b=b)==True:
		print("pre_condition_176 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_177(a=a,b=b)==True:
		print("pre_condition_177 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_178(a=a,b=b)==True:
		print("pre_condition_178 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_179(a=a,b=b)==True:
		print("pre_condition_179 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_180(a=a,b=b)==True:
		print("pre_condition_180 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_181(a=a,b=b)==True:
		print("pre_condition_181 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_182(a=a,b=b)==True:
		print("pre_condition_182 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_183(a=a,b=b)==True:
		print("pre_condition_183 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_184(a=a,b=b)==True:
		print("pre_condition_184 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_185(a=a,b=b)==True:
		print("pre_condition_185 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_186(a=a,b=b)==True:
		print("pre_condition_186 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_187(a=a,b=b)==True:
		print("pre_condition_187 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_188(a=a,b=b)==True:
		print("pre_condition_188 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_189(a=a,b=b)==True:
		print("pre_condition_189 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_190(a=a,b=b)==True:
		print("pre_condition_190 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_191(a=a,b=b)==True:
		print("pre_condition_191 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_192(a=a,b=b)==True:
		print("pre_condition_192 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_193(a=a,b=b)==True:
		print("pre_condition_193 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_194(a=a,b=b)==True:
		print("pre_condition_194 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_195(a=a,b=b)==True:
		print("pre_condition_195 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_196(a=a,b=b)==True:
		print("pre_condition_196 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_197(a=a,b=b)==True:
		print("pre_condition_197 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_198(a=a,b=b)==True:
		print("pre_condition_198 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_199(a=a,b=b)==True:
		print("pre_condition_199 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_200(a=a,b=b)==True:
		print("pre_condition_200 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_201(a=a,b=b)==True:
		print("pre_condition_201 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_202(a=a,b=b)==True:
		print("pre_condition_202 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_203(a=a,b=b)==True:
		print("pre_condition_203 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_204(a=a,b=b)==True:
		print("pre_condition_204 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_205(a=a,b=b)==True:
		print("pre_condition_205 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_206(a=a,b=b)==True:
		print("pre_condition_206 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_207(a=a,b=b)==True:
		print("pre_condition_207 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_208(a=a,b=b)==True:
		print("pre_condition_208 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_209(a=a,b=b)==True:
		print("pre_condition_209 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_210(a=a,b=b)==True:
		print("pre_condition_210 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_211(a=a,b=b)==True:
		print("pre_condition_211 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_212(a=a,b=b)==True:
		print("pre_condition_212 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_213(a=a,b=b)==True:
		print("pre_condition_213 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_214(a=a,b=b)==True:
		print("pre_condition_214 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_215(a=a,b=b)==True:
		print("pre_condition_215 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_216(a=a,b=b)==True:
		print("pre_condition_216 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_217(a=a,b=b)==True:
		print("pre_condition_217 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_218(a=a,b=b)==True:
		print("pre_condition_218 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_219(a=a,b=b)==True:
		print("pre_condition_219 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_220(a=a,b=b)==True:
		print("pre_condition_220 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_221(a=a,b=b)==True:
		print("pre_condition_221 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_222(a=a,b=b)==True:
		print("pre_condition_222 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_223(a=a,b=b)==True:
		print("pre_condition_223 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_224(a=a,b=b)==True:
		print("pre_condition_224 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_225(a=a,b=b)==True:
		print("pre_condition_225 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_226(a=a,b=b)==True:
		print("pre_condition_226 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_227(a=a,b=b)==True:
		print("pre_condition_227 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_228(a=a,b=b)==True:
		print("pre_condition_228 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_229(a=a,b=b)==True:
		print("pre_condition_229 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_230(a=a,b=b)==True:
		print("pre_condition_230 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_231(a=a,b=b)==True:
		print("pre_condition_231 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_232(a=a,b=b)==True:
		print("pre_condition_232 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_233(a=a,b=b)==True:
		print("pre_condition_233 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_234(a=a,b=b)==True:
		print("pre_condition_234 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_235(a=a,b=b)==True:
		print("pre_condition_235 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_236(a=a,b=b)==True:
		print("pre_condition_236 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_237(a=a,b=b)==True:
		print("pre_condition_237 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_238(a=a,b=b)==True:
		print("pre_condition_238 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_239(a=a,b=b)==True:
		print("pre_condition_239 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_240(a=a,b=b)==True:
		print("pre_condition_240 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_241(a=a,b=b)==True:
		print("pre_condition_241 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_242(a=a,b=b)==True:
		print("pre_condition_242 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_243(a=a,b=b)==True:
		print("pre_condition_243 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_244(a=a,b=b)==True:
		print("pre_condition_244 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_245(a=a,b=b)==True:
		print("pre_condition_245 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_246(a=a,b=b)==True:
		print("pre_condition_246 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_247(a=a,b=b)==True:
		print("pre_condition_247 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_248(a=a,b=b)==True:
		print("pre_condition_248 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_249(a=a,b=b)==True:
		print("pre_condition_249 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_250(a=a,b=b)==True:
		print("pre_condition_250 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_251(a=a,b=b)==True:
		print("pre_condition_251 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_252(a=a,b=b)==True:
		print("pre_condition_252 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_253(a=a,b=b)==True:
		print("pre_condition_253 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_254(a=a,b=b)==True:
		print("pre_condition_254 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_255(a=a,b=b)==True:
		print("pre_condition_255 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_256(a=a,b=b)==True:
		print("pre_condition_256 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_257(a=a,b=b)==True:
		print("pre_condition_257 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_258(a=a,b=b)==True:
		print("pre_condition_258 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_259(a=a,b=b)==True:
		print("pre_condition_259 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_260(a=a,b=b)==True:
		print("pre_condition_260 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_261(a=a,b=b)==True:
		print("pre_condition_261 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_262(a=a,b=b)==True:
		print("pre_condition_262 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_263(a=a,b=b)==True:
		print("pre_condition_263 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_264(a=a,b=b)==True:
		print("pre_condition_264 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_265(a=a,b=b)==True:
		print("pre_condition_265 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_266(a=a,b=b)==True:
		print("pre_condition_266 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_267(a=a,b=b)==True:
		print("pre_condition_267 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_268(a=a,b=b)==True:
		print("pre_condition_268 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_269(a=a,b=b)==True:
		print("pre_condition_269 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_270(a=a,b=b)==True:
		print("pre_condition_270 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_271(a=a,b=b)==True:
		print("pre_condition_271 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_272(a=a,b=b)==True:
		print("pre_condition_272 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_273(a=a,b=b)==True:
		print("pre_condition_273 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_274(a=a,b=b)==True:
		print("pre_condition_274 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_275(a=a,b=b)==True:
		print("pre_condition_275 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_276(a=a,b=b)==True:
		print("pre_condition_276 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_277(a=a,b=b)==True:
		print("pre_condition_277 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_278(a=a,b=b)==True:
		print("pre_condition_278 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_279(a=a,b=b)==True:
		print("pre_condition_279 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_280(a=a,b=b)==True:
		print("pre_condition_280 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_281(a=a,b=b)==True:
		print("pre_condition_281 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_282(a=a,b=b)==True:
		print("pre_condition_282 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_283(a=a,b=b)==True:
		print("pre_condition_283 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_284(a=a,b=b)==True:
		print("pre_condition_284 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_285(a=a,b=b)==True:
		print("pre_condition_285 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_286(a=a,b=b)==True:
		print("pre_condition_286 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_287(a=a,b=b)==True:
		print("pre_condition_287 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_288(a=a,b=b)==True:
		print("pre_condition_288 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_289(a=a,b=b)==True:
		print("pre_condition_289 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_290(a=a,b=b)==True:
		print("pre_condition_290 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_291(a=a,b=b)==True:
		print("pre_condition_291 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_292(a=a,b=b)==True:
		print("pre_condition_292 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_293(a=a,b=b)==True:
		print("pre_condition_293 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_294(a=a,b=b)==True:
		print("pre_condition_294 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_295(a=a,b=b)==True:
		print("pre_condition_295 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_296(a=a,b=b)==True:
		print("pre_condition_296 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_297(a=a,b=b)==True:
		print("pre_condition_297 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_298(a=a,b=b)==True:
		print("pre_condition_298 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_299(a=a,b=b)==True:
		print("pre_condition_299 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_300(a=a,b=b)==True:
		print("pre_condition_300 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_301(a=a,b=b)==True:
		print("pre_condition_301 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_302(a=a,b=b)==True:
		print("pre_condition_302 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_303(a=a,b=b)==True:
		print("pre_condition_303 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_304(a=a,b=b)==True:
		print("pre_condition_304 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_305(a=a,b=b)==True:
		print("pre_condition_305 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_306(a=a,b=b)==True:
		print("pre_condition_306 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_307(a=a,b=b)==True:
		print("pre_condition_307 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_308(a=a,b=b)==True:
		print("pre_condition_308 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_309(a=a,b=b)==True:
		print("pre_condition_309 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_310(a=a,b=b)==True:
		print("pre_condition_310 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_311(a=a,b=b)==True:
		print("pre_condition_311 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_312(a=a,b=b)==True:
		print("pre_condition_312 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_313(a=a,b=b)==True:
		print("pre_condition_313 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_314(a=a,b=b)==True:
		print("pre_condition_314 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_315(a=a,b=b)==True:
		print("pre_condition_315 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_316(a=a,b=b)==True:
		print("pre_condition_316 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_317(a=a,b=b)==True:
		print("pre_condition_317 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_318(a=a,b=b)==True:
		print("pre_condition_318 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_319(a=a,b=b)==True:
		print("pre_condition_319 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_320(a=a,b=b)==True:
		print("pre_condition_320 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_321(a=a,b=b)==True:
		print("pre_condition_321 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_322(a=a,b=b)==True:
		print("pre_condition_322 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_323(a=a,b=b)==True:
		print("pre_condition_323 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_324(a=a,b=b)==True:
		print("pre_condition_324 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_325(a=a,b=b)==True:
		print("pre_condition_325 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_326(a=a,b=b)==True:
		print("pre_condition_326 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_327(a=a,b=b)==True:
		print("pre_condition_327 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_328(a=a,b=b)==True:
		print("pre_condition_328 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_329(a=a,b=b)==True:
		print("pre_condition_329 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_330(a=a,b=b)==True:
		print("pre_condition_330 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_331(a=a,b=b)==True:
		print("pre_condition_331 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_332(a=a,b=b)==True:
		print("pre_condition_332 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_333(a=a,b=b)==True:
		print("pre_condition_333 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_334(a=a,b=b)==True:
		print("pre_condition_334 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_335(a=a,b=b)==True:
		print("pre_condition_335 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_336(a=a,b=b)==True:
		print("pre_condition_336 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_337(a=a,b=b)==True:
		print("pre_condition_337 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_338(a=a,b=b)==True:
		print("pre_condition_338 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_339(a=a,b=b)==True:
		print("pre_condition_339 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_340(a=a,b=b)==True:
		print("pre_condition_340 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_341(a=a,b=b)==True:
		print("pre_condition_341 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_342(a=a,b=b)==True:
		print("pre_condition_342 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_343(a=a,b=b)==True:
		print("pre_condition_343 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_344(a=a,b=b)==True:
		print("pre_condition_344 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_345(a=a,b=b)==True:
		print("pre_condition_345 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_346(a=a,b=b)==True:
		print("pre_condition_346 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_347(a=a,b=b)==True:
		print("pre_condition_347 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_348(a=a,b=b)==True:
		print("pre_condition_348 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_349(a=a,b=b)==True:
		print("pre_condition_349 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_350(a=a,b=b)==True:
		print("pre_condition_350 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_351(a=a,b=b)==True:
		print("pre_condition_351 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_352(a=a,b=b)==True:
		print("pre_condition_352 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_353(a=a,b=b)==True:
		print("pre_condition_353 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_354(a=a,b=b)==True:
		print("pre_condition_354 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_355(a=a,b=b)==True:
		print("pre_condition_355 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_356(a=a,b=b)==True:
		print("pre_condition_356 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_357(a=a,b=b)==True:
		print("pre_condition_357 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_358(a=a,b=b)==True:
		print("pre_condition_358 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_359(a=a,b=b)==True:
		print("pre_condition_359 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_360(a=a,b=b)==True:
		print("pre_condition_360 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_361(a=a,b=b)==True:
		print("pre_condition_361 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_362(a=a,b=b)==True:
		print("pre_condition_362 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_363(a=a,b=b)==True:
		print("pre_condition_363 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_364(a=a,b=b)==True:
		print("pre_condition_364 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_365(a=a,b=b)==True:
		print("pre_condition_365 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_366(a=a,b=b)==True:
		print("pre_condition_366 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_367(a=a,b=b)==True:
		print("pre_condition_367 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_368(a=a,b=b)==True:
		print("pre_condition_368 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_369(a=a,b=b)==True:
		print("pre_condition_369 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_370(a=a,b=b)==True:
		print("pre_condition_370 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_371(a=a,b=b)==True:
		print("pre_condition_371 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_372(a=a,b=b)==True:
		print("pre_condition_372 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_373(a=a,b=b)==True:
		print("pre_condition_373 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_374(a=a,b=b)==True:
		print("pre_condition_374 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_375(a=a,b=b)==True:
		print("pre_condition_375 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_376(a=a,b=b)==True:
		print("pre_condition_376 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_377(a=a,b=b)==True:
		print("pre_condition_377 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_378(a=a,b=b)==True:
		print("pre_condition_378 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_379(a=a,b=b)==True:
		print("pre_condition_379 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_380(a=a,b=b)==True:
		print("pre_condition_380 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_381(a=a,b=b)==True:
		print("pre_condition_381 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_382(a=a,b=b)==True:
		print("pre_condition_382 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_383(a=a,b=b)==True:
		print("pre_condition_383 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_384(a=a,b=b)==True:
		print("pre_condition_384 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_385(a=a,b=b)==True:
		print("pre_condition_385 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_386(a=a,b=b)==True:
		print("pre_condition_386 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_387(a=a,b=b)==True:
		print("pre_condition_387 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_388(a=a,b=b)==True:
		print("pre_condition_388 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_389(a=a,b=b)==True:
		print("pre_condition_389 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_390(a=a,b=b)==True:
		print("pre_condition_390 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_391(a=a,b=b)==True:
		print("pre_condition_391 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_392(a=a,b=b)==True:
		print("pre_condition_392 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_393(a=a,b=b)==True:
		print("pre_condition_393 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_394(a=a,b=b)==True:
		print("pre_condition_394 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_395(a=a,b=b)==True:
		print("pre_condition_395 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_396(a=a,b=b)==True:
		print("pre_condition_396 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_397(a=a,b=b)==True:
		print("pre_condition_397 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_398(a=a,b=b)==True:
		print("pre_condition_398 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_399(a=a,b=b)==True:
		print("pre_condition_399 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_400(a=a,b=b)==True:
		print("pre_condition_400 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_401(a=a,b=b)==True:
		print("pre_condition_401 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_402(a=a,b=b)==True:
		print("pre_condition_402 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_403(a=a,b=b)==True:
		print("pre_condition_403 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_404(a=a,b=b)==True:
		print("pre_condition_404 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_405(a=a,b=b)==True:
		print("pre_condition_405 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_406(a=a,b=b)==True:
		print("pre_condition_406 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_407(a=a,b=b)==True:
		print("pre_condition_407 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_408(a=a,b=b)==True:
		print("pre_condition_408 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_409(a=a,b=b)==True:
		print("pre_condition_409 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_410(a=a,b=b)==True:
		print("pre_condition_410 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_411(a=a,b=b)==True:
		print("pre_condition_411 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_412(a=a,b=b)==True:
		print("pre_condition_412 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_413(a=a,b=b)==True:
		print("pre_condition_413 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_414(a=a,b=b)==True:
		print("pre_condition_414 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_415(a=a,b=b)==True:
		print("pre_condition_415 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_416(a=a,b=b)==True:
		print("pre_condition_416 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_417(a=a,b=b)==True:
		print("pre_condition_417 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_418(a=a,b=b)==True:
		print("pre_condition_418 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_419(a=a,b=b)==True:
		print("pre_condition_419 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_420(a=a,b=b)==True:
		print("pre_condition_420 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_421(a=a,b=b)==True:
		print("pre_condition_421 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_422(a=a,b=b)==True:
		print("pre_condition_422 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_423(a=a,b=b)==True:
		print("pre_condition_423 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_424(a=a,b=b)==True:
		print("pre_condition_424 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_425(a=a,b=b)==True:
		print("pre_condition_425 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_426(a=a,b=b)==True:
		print("pre_condition_426 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_427(a=a,b=b)==True:
		print("pre_condition_427 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_428(a=a,b=b)==True:
		print("pre_condition_428 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_429(a=a,b=b)==True:
		print("pre_condition_429 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_430(a=a,b=b)==True:
		print("pre_condition_430 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_431(a=a,b=b)==True:
		print("pre_condition_431 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_432(a=a,b=b)==True:
		print("pre_condition_432 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_433(a=a,b=b)==True:
		print("pre_condition_433 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_434(a=a,b=b)==True:
		print("pre_condition_434 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_435(a=a,b=b)==True:
		print("pre_condition_435 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_436(a=a,b=b)==True:
		print("pre_condition_436 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_437(a=a,b=b)==True:
		print("pre_condition_437 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_438(a=a,b=b)==True:
		print("pre_condition_438 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_439(a=a,b=b)==True:
		print("pre_condition_439 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_440(a=a,b=b)==True:
		print("pre_condition_440 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_441(a=a,b=b)==True:
		print("pre_condition_441 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_442(a=a,b=b)==True:
		print("pre_condition_442 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_443(a=a,b=b)==True:
		print("pre_condition_443 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_444(a=a,b=b)==True:
		print("pre_condition_444 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_445(a=a,b=b)==True:
		print("pre_condition_445 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_446(a=a,b=b)==True:
		print("pre_condition_446 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_447(a=a,b=b)==True:
		print("pre_condition_447 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_448(a=a,b=b)==True:
		print("pre_condition_448 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_449(a=a,b=b)==True:
		print("pre_condition_449 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_450(a=a,b=b)==True:
		print("pre_condition_450 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_451(a=a,b=b)==True:
		print("pre_condition_451 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_452(a=a,b=b)==True:
		print("pre_condition_452 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_453(a=a,b=b)==True:
		print("pre_condition_453 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_454(a=a,b=b)==True:
		print("pre_condition_454 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_455(a=a,b=b)==True:
		print("pre_condition_455 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_456(a=a,b=b)==True:
		print("pre_condition_456 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_457(a=a,b=b)==True:
		print("pre_condition_457 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_458(a=a,b=b)==True:
		print("pre_condition_458 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_459(a=a,b=b)==True:
		print("pre_condition_459 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_460(a=a,b=b)==True:
		print("pre_condition_460 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_461(a=a,b=b)==True:
		print("pre_condition_461 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_462(a=a,b=b)==True:
		print("pre_condition_462 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_463(a=a,b=b)==True:
		print("pre_condition_463 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_464(a=a,b=b)==True:
		print("pre_condition_464 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_465(a=a,b=b)==True:
		print("pre_condition_465 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_466(a=a,b=b)==True:
		print("pre_condition_466 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_467(a=a,b=b)==True:
		print("pre_condition_467 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_468(a=a,b=b)==True:
		print("pre_condition_468 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_469(a=a,b=b)==True:
		print("pre_condition_469 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_470(a=a,b=b)==True:
		print("pre_condition_470 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_471(a=a,b=b)==True:
		print("pre_condition_471 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_472(a=a,b=b)==True:
		print("pre_condition_472 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_473(a=a,b=b)==True:
		print("pre_condition_473 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_474(a=a,b=b)==True:
		print("pre_condition_474 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_475(a=a,b=b)==True:
		print("pre_condition_475 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_476(a=a,b=b)==True:
		print("pre_condition_476 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_477(a=a,b=b)==True:
		print("pre_condition_477 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_478(a=a,b=b)==True:
		print("pre_condition_478 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_479(a=a,b=b)==True:
		print("pre_condition_479 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_480(a=a,b=b)==True:
		print("pre_condition_480 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_481(a=a,b=b)==True:
		print("pre_condition_481 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_482(a=a,b=b)==True:
		print("pre_condition_482 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_483(a=a,b=b)==True:
		print("pre_condition_483 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_484(a=a,b=b)==True:
		print("pre_condition_484 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_485(a=a,b=b)==True:
		print("pre_condition_485 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_486(a=a,b=b)==True:
		print("pre_condition_486 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_487(a=a,b=b)==True:
		print("pre_condition_487 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_488(a=a,b=b)==True:
		print("pre_condition_488 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_489(a=a,b=b)==True:
		print("pre_condition_489 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_490(a=a,b=b)==True:
		print("pre_condition_490 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_491(a=a,b=b)==True:
		print("pre_condition_491 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_492(a=a,b=b)==True:
		print("pre_condition_492 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_493(a=a,b=b)==True:
		print("pre_condition_493 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_494(a=a,b=b)==True:
		print("pre_condition_494 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_495(a=a,b=b)==True:
		print("pre_condition_495 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_496(a=a,b=b)==True:
		print("pre_condition_496 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_497(a=a,b=b)==True:
		print("pre_condition_497 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_498(a=a,b=b)==True:
		print("pre_condition_498 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_499(a=a,b=b)==True:
		print("pre_condition_499 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_500(a=a,b=b)==True:
		print("pre_condition_500 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_501(a=a,b=b)==True:
		print("pre_condition_501 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_502(a=a,b=b)==True:
		print("pre_condition_502 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_503(a=a,b=b)==True:
		print("pre_condition_503 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_504(a=a,b=b)==True:
		print("pre_condition_504 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_505(a=a,b=b)==True:
		print("pre_condition_505 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_506(a=a,b=b)==True:
		print("pre_condition_506 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_507(a=a,b=b)==True:
		print("pre_condition_507 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_508(a=a,b=b)==True:
		print("pre_condition_508 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_509(a=a,b=b)==True:
		print("pre_condition_509 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_510(a=a,b=b)==True:
		print("pre_condition_510 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_511(a=a,b=b)==True:
		print("pre_condition_511 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_512(a=a,b=b)==True:
		print("pre_condition_512 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_513(a=a,b=b)==True:
		print("pre_condition_513 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_514(a=a,b=b)==True:
		print("pre_condition_514 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_515(a=a,b=b)==True:
		print("pre_condition_515 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_516(a=a,b=b)==True:
		print("pre_condition_516 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_517(a=a,b=b)==True:
		print("pre_condition_517 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_518(a=a,b=b)==True:
		print("pre_condition_518 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_519(a=a,b=b)==True:
		print("pre_condition_519 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_520(a=a,b=b)==True:
		print("pre_condition_520 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_521(a=a,b=b)==True:
		print("pre_condition_521 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_522(a=a,b=b)==True:
		print("pre_condition_522 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_523(a=a,b=b)==True:
		print("pre_condition_523 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_524(a=a,b=b)==True:
		print("pre_condition_524 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_525(a=a,b=b)==True:
		print("pre_condition_525 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_526(a=a,b=b)==True:
		print("pre_condition_526 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_527(a=a,b=b)==True:
		print("pre_condition_527 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_528(a=a,b=b)==True:
		print("pre_condition_528 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_529(a=a,b=b)==True:
		print("pre_condition_529 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_530(a=a,b=b)==True:
		print("pre_condition_530 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_531(a=a,b=b)==True:
		print("pre_condition_531 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_532(a=a,b=b)==True:
		print("pre_condition_532 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_533(a=a,b=b)==True:
		print("pre_condition_533 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_534(a=a,b=b)==True:
		print("pre_condition_534 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_535(a=a,b=b)==True:
		print("pre_condition_535 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_536(a=a,b=b)==True:
		print("pre_condition_536 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_537(a=a,b=b)==True:
		print("pre_condition_537 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_538(a=a,b=b)==True:
		print("pre_condition_538 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_539(a=a,b=b)==True:
		print("pre_condition_539 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_540(a=a,b=b)==True:
		print("pre_condition_540 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_541(a=a,b=b)==True:
		print("pre_condition_541 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_542(a=a,b=b)==True:
		print("pre_condition_542 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_543(a=a,b=b)==True:
		print("pre_condition_543 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_544(a=a,b=b)==True:
		print("pre_condition_544 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_545(a=a,b=b)==True:
		print("pre_condition_545 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_546(a=a,b=b)==True:
		print("pre_condition_546 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_547(a=a,b=b)==True:
		print("pre_condition_547 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_548(a=a,b=b)==True:
		print("pre_condition_548 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_549(a=a,b=b)==True:
		print("pre_condition_549 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_550(a=a,b=b)==True:
		print("pre_condition_550 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_551(a=a,b=b)==True:
		print("pre_condition_551 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_552(a=a,b=b)==True:
		print("pre_condition_552 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_553(a=a,b=b)==True:
		print("pre_condition_553 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_554(a=a,b=b)==True:
		print("pre_condition_554 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_555(a=a,b=b)==True:
		print("pre_condition_555 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_556(a=a,b=b)==True:
		print("pre_condition_556 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_557(a=a,b=b)==True:
		print("pre_condition_557 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_558(a=a,b=b)==True:
		print("pre_condition_558 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_559(a=a,b=b)==True:
		print("pre_condition_559 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_560(a=a,b=b)==True:
		print("pre_condition_560 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_561(a=a,b=b)==True:
		print("pre_condition_561 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_562(a=a,b=b)==True:
		print("pre_condition_562 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_563(a=a,b=b)==True:
		print("pre_condition_563 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_564(a=a,b=b)==True:
		print("pre_condition_564 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_565(a=a,b=b)==True:
		print("pre_condition_565 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_566(a=a,b=b)==True:
		print("pre_condition_566 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_567(a=a,b=b)==True:
		print("pre_condition_567 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_568(a=a,b=b)==True:
		print("pre_condition_568 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_569(a=a,b=b)==True:
		print("pre_condition_569 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_570(a=a,b=b)==True:
		print("pre_condition_570 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_571(a=a,b=b)==True:
		print("pre_condition_571 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_572(a=a,b=b)==True:
		print("pre_condition_572 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_573(a=a,b=b)==True:
		print("pre_condition_573 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_574(a=a,b=b)==True:
		print("pre_condition_574 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_575(a=a,b=b)==True:
		print("pre_condition_575 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_576(a=a,b=b)==True:
		print("pre_condition_576 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_577(a=a,b=b)==True:
		print("pre_condition_577 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_578(a=a,b=b)==True:
		print("pre_condition_578 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_579(a=a,b=b)==True:
		print("pre_condition_579 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_580(a=a,b=b)==True:
		print("pre_condition_580 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_581(a=a,b=b)==True:
		print("pre_condition_581 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_582(a=a,b=b)==True:
		print("pre_condition_582 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_583(a=a,b=b)==True:
		print("pre_condition_583 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_584(a=a,b=b)==True:
		print("pre_condition_584 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_585(a=a,b=b)==True:
		print("pre_condition_585 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_586(a=a,b=b)==True:
		print("pre_condition_586 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_587(a=a,b=b)==True:
		print("pre_condition_587 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_588(a=a,b=b)==True:
		print("pre_condition_588 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_589(a=a,b=b)==True:
		print("pre_condition_589 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_590(a=a,b=b)==True:
		print("pre_condition_590 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_591(a=a,b=b)==True:
		print("pre_condition_591 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_592(a=a,b=b)==True:
		print("pre_condition_592 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_593(a=a,b=b)==True:
		print("pre_condition_593 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_594(a=a,b=b)==True:
		print("pre_condition_594 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_595(a=a,b=b)==True:
		print("pre_condition_595 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_596(a=a,b=b)==True:
		print("pre_condition_596 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_597(a=a,b=b)==True:
		print("pre_condition_597 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_598(a=a,b=b)==True:
		print("pre_condition_598 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_599(a=a,b=b)==True:
		print("pre_condition_599 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_600(a=a,b=b)==True:
		print("pre_condition_600 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_601(a=a,b=b)==True:
		print("pre_condition_601 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_602(a=a,b=b)==True:
		print("pre_condition_602 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_603(a=a,b=b)==True:
		print("pre_condition_603 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_604(a=a,b=b)==True:
		print("pre_condition_604 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_605(a=a,b=b)==True:
		print("pre_condition_605 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_606(a=a,b=b)==True:
		print("pre_condition_606 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_607(a=a,b=b)==True:
		print("pre_condition_607 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_608(a=a,b=b)==True:
		print("pre_condition_608 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_609(a=a,b=b)==True:
		print("pre_condition_609 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_610(a=a,b=b)==True:
		print("pre_condition_610 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_611(a=a,b=b)==True:
		print("pre_condition_611 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_612(a=a,b=b)==True:
		print("pre_condition_612 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_613(a=a,b=b)==True:
		print("pre_condition_613 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_614(a=a,b=b)==True:
		print("pre_condition_614 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_615(a=a,b=b)==True:
		print("pre_condition_615 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_616(a=a,b=b)==True:
		print("pre_condition_616 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_617(a=a,b=b)==True:
		print("pre_condition_617 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_618(a=a,b=b)==True:
		print("pre_condition_618 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_619(a=a,b=b)==True:
		print("pre_condition_619 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_620(a=a,b=b)==True:
		print("pre_condition_620 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_621(a=a,b=b)==True:
		print("pre_condition_621 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_622(a=a,b=b)==True:
		print("pre_condition_622 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_623(a=a,b=b)==True:
		print("pre_condition_623 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_624(a=a,b=b)==True:
		print("pre_condition_624 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_625(a=a,b=b)==True:
		print("pre_condition_625 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_626(a=a,b=b)==True:
		print("pre_condition_626 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_627(a=a,b=b)==True:
		print("pre_condition_627 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_628(a=a,b=b)==True:
		print("pre_condition_628 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_629(a=a,b=b)==True:
		print("pre_condition_629 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_630(a=a,b=b)==True:
		print("pre_condition_630 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_631(a=a,b=b)==True:
		print("pre_condition_631 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_632(a=a,b=b)==True:
		print("pre_condition_632 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_633(a=a,b=b)==True:
		print("pre_condition_633 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_634(a=a,b=b)==True:
		print("pre_condition_634 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_635(a=a,b=b)==True:
		print("pre_condition_635 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_636(a=a,b=b)==True:
		print("pre_condition_636 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_637(a=a,b=b)==True:
		print("pre_condition_637 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_638(a=a,b=b)==True:
		print("pre_condition_638 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_639(a=a,b=b)==True:
		print("pre_condition_639 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_640(a=a,b=b)==True:
		print("pre_condition_640 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_641(a=a,b=b)==True:
		print("pre_condition_641 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_642(a=a,b=b)==True:
		print("pre_condition_642 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_643(a=a,b=b)==True:
		print("pre_condition_643 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_644(a=a,b=b)==True:
		print("pre_condition_644 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_645(a=a,b=b)==True:
		print("pre_condition_645 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_646(a=a,b=b)==True:
		print("pre_condition_646 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_647(a=a,b=b)==True:
		print("pre_condition_647 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_648(a=a,b=b)==True:
		print("pre_condition_648 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_649(a=a,b=b)==True:
		print("pre_condition_649 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)
	
	
	if pre_condition_650(a=a,b=b)==True:
		print("pre_condition_650 SAT")
		print('x = 95138542128201727/4611686018427387904')
		print('y = -7/16384')
		print('z = 0')
		print('a = 62833241236701183/147573952589676412928')
		print('b = 502665929893609461/1180591620717411303424')
		exit(0)


	print("UNKNOWN")
	exit(0)
